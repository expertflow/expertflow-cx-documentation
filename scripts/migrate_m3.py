#!/usr/bin/env python3
"""M3 Migration Script: Restructure Phase4 docs to new navigation tree.

Reads Phase3/Content_Mapping_Table.csv and copies files from Phase4/ to Restructured/.
Non-destructive — Phase4 is not modified.

Usage:
    python3 migrate_m3.py          # dry run (default)
    python3 migrate_m3.py --run    # execute copies
"""

import csv
import os
import shutil
import sys
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).parent
PHASE4 = BASE / "Phase4"
DEST = BASE / "Restructured"
CSV_PATH = BASE / "Phase3" / "Content_Mapping_Table.csv"

DRY_RUN = "--run" not in sys.argv

# nav_section → top-level folder name
NAV_SECTION_FOLDER = {
    "Getting Started":   "Getting_Started",
    "Platform Overview": "Platform_Overview",
    "Capabilities":      "Capabilities",
    "How-to Guides":     "How-to_Guides",
    "Reference":         "Reference",
    "UNMAPPED":          "_unmapped",
}

# nav_sub_section → subfolder path (may contain '/' for nested)
NAV_SUB_FOLDER = {
    # Capabilities
    "Digital Channels":                              "Digital_Channels",
    "Voice & Video":                                 "Voice_and_Video",
    "Reporting & Analytics":                         "Reporting_and_Analytics",
    "Security & Compliance":                         "Security_and_Compliance",
    "Workforce Management":                          "Workforce_Management",
    # Getting Started
    "For Agents":                                    "For_Agents",
    "For Administrators":                            "For_Administrators",
    "For Supervisors & QA Leads":                    "For_Supervisors_and_QA_Leads",
    "For Conversation Designers":                    "For_Conversation_Designers",
    "For Developers & Integrators":                  "For_Developers_and_Integrators",
    "For Hosting Partners":                          "For_Hosting_Partners",
    # How-to Guides
    "Agent":                                         "Agent",
    "Administrator":                                 "Administrator",
    "Supervisor & QA Lead":                          "Supervisor_and_QA_Lead",
    "Conversation Designer / AI Specialist":         "Conversation_Designer",
    "Developer / Integrator":                        "Developer_Integrator",
    "Hosting Partner":                               "Hosting_Partner",
    # Reference
    "Glossary":                                      "Glossary",
    "Schemas & Data Model > CIM Message Schema":     "Schemas_and_Data_Model/CIM_Message_Schema",
    "Schemas & Data Model > Socket Events":          "Schemas_and_Data_Model/Socket_Events",
}

# Old Functional_Areas subfolder → new Capabilities subfolder
FUNCTIONAL_AREAS_RENAME = {
    "Digital_Channel_Management":   "Digital_Channels",
    "Performance_Insights_Data":    "Reporting_and_Analytics",
    "Security_Compliance":          "Security_and_Compliance",
    "Voice_Real_Time_Media":        "Voice_and_Video",
    "Workforce_Schedule_Management": "Workforce_Management",
}


def compute_dest_rel(row: dict) -> Path:
    """Return the destination path relative to DEST for a given CSV row."""
    current = row["current_path"]
    nav_section = row["nav_section"]
    nav_sub = row["nav_sub_section"].strip()
    action = row["action"].strip()

    section_folder = NAV_SECTION_FOLDER.get(nav_section, nav_section.replace(" ", "_"))

    if action == "RENAME section":
        # Functional_Areas/{old_sub}/...rel... → Capabilities/{new_sub}/...rel...
        parts = Path(current).parts
        # parts[0] = 'Functional_Areas', parts[1] = subfolder (or filename if file is at root)
        if len(parts) == 2:
            # File sits directly in Functional_Areas/ (e.g. index.md) → Capabilities/filename
            return Path(section_folder) / parts[1]
        old_sub = parts[1]
        new_sub = FUNCTIONAL_AREAS_RENAME.get(old_sub, old_sub)
        rel_within = Path(*parts[2:])
        return Path(section_folder) / new_sub / rel_within

    # All other actions: place file in section/subsection using just the filename
    filename = Path(current).name

    if nav_sub in ("(review needed)", ""):
        # No subsection folder — place at section root
        return Path(section_folder) / filename

    sub_path = NAV_SUB_FOLDER.get(nav_sub)
    if sub_path is None:
        # Unknown subsection — use it sanitised
        sub_path = nav_sub.replace(" ", "_").replace("/", "_").replace("&", "and").replace(">", "")
    return Path(section_folder) / sub_path / filename


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"Mode: {'DRY RUN (pass --run to execute)' if DRY_RUN else 'LIVE'}")
    print(f"Source: {PHASE4}")
    print(f"Destination: {DEST}")
    print(f"Rows in CSV: {len(rows)}\n")

    copied = 0
    skipped_missing = 0
    collision_log: dict[Path, list[str]] = defaultdict(list)
    ops: list[tuple[Path, Path]] = []

    for row in rows:
        src = PHASE4 / row["current_path"]
        dest_rel = compute_dest_rel(row)
        dest = DEST / dest_rel

        collision_log[dest_rel].append(row["current_path"])

        if not src.exists():
            skipped_missing += 1
            print(f"  MISSING  {row['current_path']}")
            continue

        ops.append((src, dest))

    # Report collisions (multiple source files mapping to same dest)
    collisions = {k: v for k, v in collision_log.items() if len(v) > 1}
    if collisions:
        print(f"COLLISIONS ({len(collisions)} destination paths have multiple sources):")
        for dest_rel, sources in sorted(collisions.items()):
            print(f"  {dest_rel}")
            for s in sources:
                print(f"    <- {s}")
        print()

    if not DRY_RUN:
        for src, dest in ops:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied += 1
    else:
        # Dry run: just count and show a sample
        copied = len(ops)
        print("Sample of planned copies (first 20):")
        for src, dest in ops[:20]:
            print(f"  {src.relative_to(PHASE4)}")
            print(f"    → {dest.relative_to(DEST)}")

    print(f"\nSummary:")
    print(f"  Files to copy / copied: {copied}")
    print(f"  Missing source files:   {skipped_missing}")
    print(f"  Destination collisions: {len(collisions)}")


if __name__ == "__main__":
    main()
