#!/usr/bin/env python3
"""M4 Re-tagging Script: Update frontmatter audience tags in Restructured/.

Reads Phase3/Content_Mapping_Table.csv and updates the `audience` frontmatter
field in each file in Restructured/ to match the new persona tag schema.

Usage:
    python3 retag_m4.py          # dry run (default)
    python3 retag_m4.py --run    # execute updates
"""

import csv
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
RESTRUCTURED = BASE / "Restructured"
CSV_PATH = BASE / "Phase3" / "Content_Mapping_Table.csv"

DRY_RUN = "--run" not in sys.argv

# Reuse same path-computation logic from migrate_m3.py
NAV_SECTION_FOLDER = {
    "Getting Started":   "Getting_Started",
    "Platform Overview": "Platform_Overview",
    "Capabilities":      "Capabilities",
    "How-to Guides":     "How-to_Guides",
    "Reference":         "Reference",
    "UNMAPPED":          "_unmapped",
}

NAV_SUB_FOLDER = {
    "Digital Channels":                              "Digital_Channels",
    "Voice & Video":                                 "Voice_and_Video",
    "Reporting & Analytics":                         "Reporting_and_Analytics",
    "Security & Compliance":                         "Security_and_Compliance",
    "Workforce Management":                          "Workforce_Management",
    "For Agents":                                    "For_Agents",
    "For Administrators":                            "For_Administrators",
    "For Supervisors & QA Leads":                    "For_Supervisors_and_QA_Leads",
    "For Conversation Designers":                    "For_Conversation_Designers",
    "For Developers & Integrators":                  "For_Developers_and_Integrators",
    "For Hosting Partners":                          "For_Hosting_Partners",
    "Agent":                                         "Agent",
    "Administrator":                                 "Administrator",
    "Supervisor & QA Lead":                          "Supervisor_and_QA_Lead",
    "Conversation Designer / AI Specialist":         "Conversation_Designer",
    "Developer / Integrator":                        "Developer_Integrator",
    "Hosting Partner":                               "Hosting_Partner",
    "Glossary":                                      "Glossary",
    "Schemas & Data Model > CIM Message Schema":     "Schemas_and_Data_Model/CIM_Message_Schema",
    "Schemas & Data Model > Socket Events":          "Schemas_and_Data_Model/Socket_Events",
}

FUNCTIONAL_AREAS_RENAME = {
    "Digital_Channel_Management":    "Digital_Channels",
    "Performance_Insights_Data":     "Reporting_and_Analytics",
    "Security_Compliance":           "Security_and_Compliance",
    "Voice_Real_Time_Media":         "Voice_and_Video",
    "Workforce_Schedule_Management": "Workforce_Management",
}


def compute_dest_rel(row: dict) -> Path:
    current = row["current_path"]
    nav_section = row["nav_section"]
    nav_sub = row["nav_sub_section"].strip()
    action = row["action"].strip()
    section_folder = NAV_SECTION_FOLDER.get(nav_section, nav_section.replace(" ", "_"))

    if action == "RENAME section":
        parts = Path(current).parts
        if len(parts) == 2:
            return Path(section_folder) / parts[1]
        old_sub = parts[1]
        new_sub = FUNCTIONAL_AREAS_RENAME.get(old_sub, old_sub)
        return Path(section_folder) / new_sub / Path(*parts[2:])

    filename = Path(current).name
    if nav_sub in ("(review needed)", ""):
        return Path(section_folder) / filename
    sub_path = NAV_SUB_FOLDER.get(nav_sub, nav_sub.replace(" ", "_"))
    return Path(section_folder) / sub_path / filename


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def update_frontmatter(content: str, new_audience) -> tuple:
    """Return (updated_content, changed).
    new_audience=None means remove audience key; [] means empty list.
    """
    match = FRONTMATTER_RE.match(content)
    if not match:
        # No frontmatter — prepend one if we have a tag to add
        if new_audience:
            tag_str = "[" + ", ".join(new_audience) + "]"
            new_fm = f"---\naudience: {tag_str}\n---\n"
            return new_fm + content, True
        return content, False

    fm_text = match.group(1)
    body = content[match.end():]

    # Parse audience line
    audience_re = re.compile(r"^audience:.*$", re.MULTILINE)
    existing = audience_re.search(fm_text)

    if new_audience is None:
        # Remove audience line entirely
        if existing:
            new_fm_text = audience_re.sub("", fm_text).strip()
            return f"---\n{new_fm_text}\n---\n{body}", True
        return content, False
    else:
        tag_str = "[" + ", ".join(new_audience) + "]"
        new_line = f"audience: {tag_str}"
        if existing:
            current_line = existing.group(0)
            if current_line == new_line:
                return content, False  # already correct
            new_fm_text = audience_re.sub(new_line, fm_text)
        else:
            # Prepend audience line to frontmatter
            new_fm_text = new_line + "\n" + fm_text
        return f"---\n{new_fm_text}\n---\n{body}", True


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Mode: {'DRY RUN (pass --run to execute)' if DRY_RUN else 'LIVE'}")
    print(f"Target: {RESTRUCTURED}\n")

    updated = 0
    unchanged = 0
    missing = 0
    errors = []

    for row in rows:
        dest_rel = compute_dest_rel(row)
        file_path = RESTRUCTURED / dest_rel

        if not file_path.exists():
            missing += 1
            continue

        # Determine new audience tag
        csv_tag = row["audience_tag"].strip()
        notes = row["notes"]

        if not csv_tag:
            # Capabilities / Reference / UNMAPPED — no audience tag
            new_audience = None
        else:
            # Strip surrounding brackets if present (CSV stores e.g. "administrator")
            tag_value = csv_tag.strip("[]")
            tags = [t.strip() for t in tag_value.split(",")]
            # Platform Operator dual-tag
            if "Platform Operator" in notes and "platform-operator" not in tags:
                tags.append("platform-operator")
            new_audience = tags

        try:
            content = file_path.read_text(encoding="utf-8")
            new_content, changed = update_frontmatter(content, new_audience)
        except Exception as e:
            errors.append(f"{dest_rel}: {e}")
            continue

        if changed:
            if not DRY_RUN:
                file_path.write_text(new_content, encoding="utf-8")
            updated += 1
            if DRY_RUN and updated <= 15:
                tag_display = str(new_audience) if new_audience else "(remove)"
                print(f"  UPDATE {dest_rel}  →  {tag_display}")
        else:
            unchanged += 1

    print(f"\nSummary:")
    print(f"  Updated:   {updated}")
    print(f"  Unchanged: {unchanged}")
    print(f"  Missing:   {missing}")
    if errors:
        print(f"  Errors ({len(errors)}):")
        for e in errors[:10]:
            print(f"    {e}")


if __name__ == "__main__":
    main()
