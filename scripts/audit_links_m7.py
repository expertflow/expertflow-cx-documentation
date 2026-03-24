#!/usr/bin/env python3
"""M7 Cross-link Audit & Repair Script.

Scans all markdown files in Restructured/, finds broken internal links,
and repairs them by looking up the target filename in the new folder tree.

Usage:
    python3 scripts/audit_links_m7.py           # dry run — report only
    python3 scripts/audit_links_m7.py --run     # execute repairs
    python3 scripts/audit_links_m7.py --report  # write broken_links_report.md
"""

import csv
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent.parent
RESTRUCTURED = BASE / "Restructured"
REPORT_PATH = BASE / "Phase3" / "broken_links_report.md"

DRY_RUN = "--run" not in sys.argv
WRITE_REPORT = "--report" in sys.argv or "--run" not in sys.argv

LINK_RE = re.compile(r"(\[([^\]]*)\]\(([^)]+)\))")


# ── 1. Build filename index ───────────────────────────────────────────────────

def build_index(root: Path) -> dict[str, list[Path]]:
    """Map every filename (case-insensitive) → list of absolute paths in root."""
    index: dict[str, list[Path]] = defaultdict(list)
    for p in root.rglob("*.md"):
        index[p.name.lower()].append(p)
    return index


# ── 2. Scan for broken links ──────────────────────────────────────────────────

def scan(root: Path) -> list[dict]:
    """Return list of broken link records."""
    broken = []
    for md_file in sorted(root.rglob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        for full_match, _text, raw_link in LINK_RE.findall(content):
            # Skip external, anchor-only, mailto
            if raw_link.startswith(("http", "#", "mailto:")):
                continue
            clean = raw_link.split("#")[0]
            anchor = raw_link.split("#")[1] if "#" in raw_link else ""
            if not clean:
                continue
            target = (md_file.parent / clean).resolve()
            if not target.exists():
                broken.append({
                    "file": md_file,
                    "full_match": full_match,
                    "raw_link": raw_link,
                    "clean_link": clean,
                    "anchor": anchor,
                    "target_stem": Path(clean).name,   # filename incl. ext
                })
    return broken


# Old Functional_Areas subfolder → new Capabilities subfolder (for index.md disambiguation)
FUNCTIONAL_AREAS_RENAME = {
    "digital_channel_management": "Digital_Channels",
    "performance_insights_data":  "Reporting_and_Analytics",
    "security_compliance":        "Security_and_Compliance",
    "voice_real_time_media":      "Voice_and_Video",
    "workforce_schedule_management": "Workforce_Management",
}


def _disambiguate(rec: dict, candidates: list[Path]):
    """Try to pick the right candidate when multiple exist."""
    src = rec["file"]
    clean = rec["clean_link"].lower()

    # ── Rule 1: Old Functional_Areas subfolder index links ─────────────────
    # e.g. "Voice_Real_Time_Media/index.md" → Capabilities/Voice_and_Video/index.md
    parts = Path(clean).parts
    if len(parts) >= 2 and parts[-1] == "index.md":
        old_sub = parts[-2].lower()
        new_sub = FUNCTIONAL_AREAS_RENAME.get(old_sub)
        if new_sub:
            target = RESTRUCTURED / "Capabilities" / new_sub / "index.md"
            if target.exists():
                return target

    # ── Rule 2: Socket_Events index links → Reference ─────────────────────
    if "socket_events" in clean.lower():
        target = RESTRUCTURED / "Reference" / "Schemas_and_Data_Model" / "Socket_Events" / "index.md"
        if target.exists():
            return target

    # ── Rule 3: WhatsApp/index.md → Capabilities/Digital_Channels/WhatsApp/index.md ──
    if clean.endswith("whatsapp/index.md"):
        target = RESTRUCTURED / "Capabilities" / "Digital_Channels" / "WhatsApp" / "index.md"
        if target.exists():
            return target

    # ── Rule 4: Decision_Maker index → Platform_Overview ─────────────────
    if "decision_maker" in clean.lower():
        target = RESTRUCTURED / "Platform_Overview" / "index.md"
        if target.exists():
            return target

    # ── Rule 5: Same-section preference ───────────────────────────────────
    try:
        src_rel = src.relative_to(RESTRUCTURED)
        src_section = src_rel.parts[0]  # e.g. "Capabilities", "How-to_Guides"
    except ValueError:
        src_section = None

    if src_section:
        same_section = [c for c in candidates if c.relative_to(RESTRUCTURED).parts[0] == src_section]
        if len(same_section) == 1:
            return same_section[0]

    # ── Rule 6: Getting_Started persona → prefer Capabilities for overview/
    #            limitations content, prefer How-to_Guides for config tasks ──
    if src_section == "Getting_Started":
        fname = Path(clean).stem.lower()
        if any(kw in fname for kw in ("-overview", "-features", "-limitations", "-capabilities")):
            caps = [c for c in candidates if c.relative_to(RESTRUCTURED).parts[0] == "Capabilities"]
            if len(caps) == 1:
                return caps[0]
        else:
            howto = [c for c in candidates if c.relative_to(RESTRUCTURED).parts[0] == "How-to_Guides"]
            if len(howto) == 1:
                return howto[0]

    return None  # still ambiguous


# ── 3. Resolve broken links ───────────────────────────────────────────────────

def resolve(broken: list[dict], index: dict[str, list[Path]]) -> tuple[list, list, list]:
    """
    Returns:
        fixable   — (record, new_abs_path) pairs with exactly one candidate
        ambiguous — records with multiple candidates (after disambiguation)
        lost      — records with zero candidates
    """
    fixable, ambiguous, lost = [], [], []
    for rec in broken:
        stem = rec["target_stem"].lower()
        candidates = index.get(stem, [])
        if len(candidates) == 0:
            lost.append(rec)
        elif len(candidates) == 1:
            fixable.append((rec, candidates[0]))
        else:
            # Try disambiguation
            picked = _disambiguate(rec, candidates)
            if picked:
                fixable.append((rec, picked))
            else:
                rec["candidates"] = candidates
                ambiguous.append(rec)
    return fixable, ambiguous, lost


# ── 4. Apply repairs ──────────────────────────────────────────────────────────

def repair(fixable: list[tuple], dry_run: bool) -> int:
    """Rewrite links in files. Returns number of files changed."""
    # Group by file
    by_file: dict[Path, list[tuple]] = defaultdict(list)
    for rec, new_path in fixable:
        by_file[rec["file"]].append((rec, new_path))

    changed = 0
    for md_file, repairs in by_file.items():
        content = md_file.read_text(encoding="utf-8")
        new_content = content
        for rec, new_path in repairs:
            new_rel = os.path.relpath(new_path, md_file.parent)
            if rec["anchor"]:
                new_rel = f"{new_rel}#{rec['anchor']}"
            # Replace only this exact match (first occurrence per link instance)
            new_content = new_content.replace(rec["full_match"],
                f"[{_extract_text(rec['full_match'])}]({new_rel})", 1)
        if new_content != content:
            if not dry_run:
                md_file.write_text(new_content, encoding="utf-8")
            changed += 1
    return changed


def _extract_text(full_match: str) -> str:
    m = re.match(r"\[([^\]]*)\]", full_match)
    return m.group(1) if m else ""


# ── 5. Report ─────────────────────────────────────────────────────────────────

def write_report(fixable, ambiguous, lost, dry_run: bool):
    lines = [
        "# M7 Broken Links Report",
        "",
        f"Generated: 2026-03-24  |  Mode: {'DRY RUN' if dry_run else 'LIVE'}",
        "",
        f"| Category | Count |",
        f"| --- | --- |",
        f"| Auto-fixable | {len(fixable)} |",
        f"| Ambiguous (multiple candidates) | {len(ambiguous)} |",
        f"| Lost (target not found anywhere) | {len(lost)} |",
        f"| **Total broken** | **{len(fixable)+len(ambiguous)+len(lost)}** |",
        "",
    ]

    if ambiguous:
        lines += [
            "## Ambiguous Links (manual review needed)",
            "",
            "| File | Link | Candidates |",
            "| --- | --- | --- |",
        ]
        for rec in ambiguous:
            cands = ", ".join(str(c.relative_to(RESTRUCTURED)) for c in rec["candidates"])
            lines.append(
                f"| {rec['file'].relative_to(RESTRUCTURED)} "
                f"| `{rec['raw_link']}` | {cands} |"
            )
        lines.append("")

    if lost:
        lines += [
            "## Lost Links (target not found in Restructured/)",
            "",
            "| File | Link |",
            "| --- | --- |",
        ]
        for rec in lost:
            lines.append(
                f"| {rec['file'].relative_to(RESTRUCTURED)} | `{rec['raw_link']}` |"
            )
        lines.append("")

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written to {REPORT_PATH.relative_to(BASE)}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print(f"Mode: {'DRY RUN' if DRY_RUN else 'LIVE'}")
    print(f"Scanning: {RESTRUCTURED}\n")

    index = build_index(RESTRUCTURED)
    broken = scan(RESTRUCTURED)
    fixable, ambiguous, lost = resolve(broken, index)

    print(f"Broken links found:      {len(broken)}")
    print(f"  Auto-fixable:          {len(fixable)}")
    print(f"  Ambiguous:             {len(ambiguous)}")
    print(f"  Lost (no match):       {len(lost)}")

    changed = repair(fixable, dry_run=DRY_RUN)
    print(f"\nFiles {'to be changed' if DRY_RUN else 'changed'}: {changed}")

    if WRITE_REPORT:
        write_report(fixable, ambiguous, lost, DRY_RUN)


if __name__ == "__main__":
    main()
