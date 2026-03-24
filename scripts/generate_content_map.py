"""
generate_content_map.py

Milestone 1: Full Content Mapping
Walks all Phase4 markdown files, applies the revised navigation structure rules
from Navigation_Skeleton_Tree.md, and outputs a CSV mapping table.

Output: Phase3/Content_Mapping_Table.csv
"""

import csv
import re
from pathlib import Path

PHASE4_DIR = Path("Phase4")
OUTPUT_CSV = Path("Phase3/Content_Mapping_Table.csv")

# ---------------------------------------------------------------------------
# Mapping rules — derived from Navigation_Skeleton_Tree.md
# Order matters: more specific rules first.
# Each rule: (path_fragment_match, nav_section, nav_sub_section, audience_tag)
# ---------------------------------------------------------------------------
PATH_RULES = [
    # --- Reference: CIM Schema and Socket Events move OUT of role folder ---
    ("Frontend_Developer/CIM-Message-Schema", "Reference", "Schemas & Data Model > CIM Message Schema", "developer-integrator"),
    ("Frontend_Developer/Socket_Events",       "Reference", "Schemas & Data Model > Socket Events",      "developer-integrator"),

    # --- Platform Overview (entire Decision_Maker folder repurposed) ---
    ("Role_Based_Guides/Decision_Maker",       "Platform Overview", "",                                   "platform-overview"),

    # --- Getting Started: known exceptions that don't belong there ---
    ("Getting_Started/Cisco-Contact-Center-Integration-Reference", "How-to Guides", "Developer / Integrator", "developer-integrator"),
    ("Getting_Started/Configuring-AI-Powered-Quality-Audits",      "How-to Guides", "Conversation Designer / AI Specialist", "conversation-designer"),
    ("Getting_Started/Glossary-of-Key-Terms",                      "Reference",     "Glossary",              ""),
    ("Getting_Started/Expertflow-CX-Platform-Overview",            "Platform Overview", "",                  "platform-overview"),
    ("Getting_Started/Security-and-Compliance-Whitepaper",         "Platform Overview", "",                  "platform-overview"),

    # --- Getting Started: role-based entry points (remaining files) ---
    ("Getting_Started/Agent-Quick-Start-Guide",                    "Getting Started", "For Agents",           "agent"),
    ("Getting_Started/Monitoring-Your-Team-in-Real-Time",          "Getting Started", "For Supervisors & QA Leads", "supervisor-qa"),
    ("Getting_Started/Evaluator-Guide",                            "Getting Started", "For Supervisors & QA Leads", "supervisor-qa"),
    ("Getting_Started/Managing-the-Quality-Assurance-Workflow",    "Getting Started", "For Supervisors & QA Leads", "supervisor-qa"),
    ("Getting_Started/Unified-Admin-Guide",                        "Getting Started", "For Administrators",    "administrator"),
    ("Getting_Started/Channel-Onboarding-Guide",                   "Getting Started", "For Administrators",    "administrator"),
    ("Getting_Started/Deploying-the-RKE2-Control-Plane",           "Getting Started", "For Hosting Partners",  "hosting-partner"),
    ("Getting_Started/Onboarding-a-New-Tenant",                    "Getting Started", "For Hosting Partners",  "hosting-partner"),
    ("Getting_Started/Conversation-Studio-Configuration-Guide",    "Getting Started", "For Conversation Designers", "conversation-designer"),
    ("Getting_Started/Agent-Desk-Developer-Guide",                 "Getting Started", "For Developers & Integrators", "developer-integrator"),
    ("Getting_Started",                                            "Getting Started", "(review needed)",       ""),

    # --- How-to Guides: Supervisor & QA Lead (merged cluster) ---
    ("Role_Based_Guides/Supervisor",                               "How-to Guides",  "Supervisor & QA Lead",   "supervisor-qa"),
    ("Role_Based_Guides/Human_Evaluator",                          "How-to Guides",  "Supervisor & QA Lead",   "supervisor-qa"),
    ("Role_Based_Guides/Quality_Manager",                          "How-to Guides",  "Supervisor & QA Lead",   "supervisor-qa"),

    # --- How-to Guides: Agent ---
    ("Role_Based_Guides/Agent",                                    "How-to Guides",  "Agent",                  "agent"),

    # --- Capabilities > Security & Compliance: Vulnerability Reports ---
    ("Role_Based_Guides/Solution_Admin/Vulnerability-Report",      "Capabilities",   "Security & Compliance",  "administrator"),

    # --- How-to Guides: Administrator ---
    ("Role_Based_Guides/Solution_Admin",                           "How-to Guides",  "Administrator",          "administrator"),

    # --- How-to Guides: Hosting Partner (merged cluster) ---
    ("Role_Based_Guides/Infrastructure_Hosting_Partner",           "How-to Guides",  "Hosting Partner",        "hosting-partner"),
    ("Role_Based_Guides/Reseller",                                 "How-to Guides",  "Hosting Partner",        "hosting-partner"),

    # --- How-to Guides: Conversation Designer / AI Specialist (merged) ---
    ("Role_Based_Guides/Conversation_Designer",                    "How-to Guides",  "Conversation Designer / AI Specialist", "conversation-designer"),
    ("Role_Based_Guides/AI_Quality_NLU_Specialist",                "How-to Guides",  "Conversation Designer / AI Specialist", "conversation-designer"),

    # --- How-to Guides: Developer / Integrator (merged) ---
    ("Role_Based_Guides/Frontend_Developer",                       "How-to Guides",  "Developer / Integrator", "developer-integrator"),
    ("Role_Based_Guides/Integration_Specialist",                   "How-to Guides",  "Developer / Integrator", "developer-integrator"),

    # --- Capabilities (Functional Areas — rename only, no file moves) ---
    ("Functional_Areas/Digital_Channel_Management",                "Capabilities",   "Digital Channels",       ""),
    ("Functional_Areas/Voice_Real_Time_Media",                     "Capabilities",   "Voice & Video",          ""),
    ("Functional_Areas/Performance_Insights_Data",                 "Capabilities",   "Reporting & Analytics",  ""),
    ("Functional_Areas/Security_Compliance",                       "Capabilities",   "Security & Compliance",  ""),
    ("Functional_Areas/Workforce_Schedule_Management",             "Capabilities",   "Workforce Management",   ""),
    ("Functional_Areas",                                           "Capabilities",   "(review needed)",        ""),
]

# Files/patterns that likely belong in the Platform Operator sub-path
# (flagged with a note, not moved to a separate section — sub-path within Admin/Hosting)
# Explicit stems confirmed as Platform Operator content:
PLATFORM_OPERATOR_STEMS = [
    "mongodb-slow-query-logs",
    "redis-slowlogs",
    "ha-in-ef-sip-proxy",
    "system-behaviour-in-failover",
    "rke2-uninstallation",
    "upgrade-to-mongodb-version-8",
    "audit-trail-implementation",
    "logging-and-tracing-opensearch",
    "upgrade-guide-postgres-vault-cisco",
]

# Files that likely belong in Reference despite sitting in role folders
REFERENCE_KEYWORDS = [
    "hardware-sizing", "sizing-guidelines", "sizing-calculator",
    "deployment-topology", "kubernetes-distributions",
    "platform-objects-and-data-model", "conversation-life-cycle-objects",
    "interaction-model-overview", "routing-engine-developer-guide",
    "scheduler-api", "queue-flushing-api", "business-calendar-api",
    "form-apis", "javascript-sdk", "agentmanager-sdk",
    "customer-facing-sdk", "reporting-database-schema",
    "sip-proxy-architecture", "system-behaviour-in-failover",
    "voice-message-schema", "agent-task-routing-lifecycle",
]


def read_frontmatter_title(filepath: Path) -> str:
    """Extract title from YAML frontmatter if present."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
        if text.startswith("---"):
            end = text.find("---", 3)
            if end != -1:
                fm = text[3:end]
                m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
                if m:
                    return m.group(1).strip()
    except Exception:
        pass
    return ""


def classify_file(rel_path: str) -> tuple:
    """Return (nav_section, nav_sub_section, audience_tag) for a file path."""
    norm = rel_path.replace("\\", "/")

    for fragment, section, sub, audience in PATH_RULES:
        if fragment in norm:
            return section, sub, audience

    return "UNMAPPED", "", ""


def flag_notes(rel_path: str, nav_section: str) -> str:
    """Add advisory notes for files needing extra attention."""
    notes = []
    lower = rel_path.lower()
    stem = Path(rel_path).stem.lower()

    if any(stem.startswith(kw) or kw in stem for kw in PLATFORM_OPERATOR_STEMS):
        notes.append("⚑ Platform Operator — add platform-operator audience tag")

    if nav_section == "How-to Guides" and any(kw in lower for kw in REFERENCE_KEYWORDS):
        notes.append("⚑ Consider moving to Reference")

    if nav_section == "Getting Started" and "(review needed)" in rel_path:
        notes.append("⚑ Review: may not be entry-point content")

    if "index" in rel_path.lower():
        notes.append("index file — update or remove")

    return "; ".join(notes)


def determine_action(rel_path: str, nav_section: str, nav_sub: str) -> str:
    """Determine what needs to happen to this file."""
    norm = rel_path.replace("\\", "/")

    # Vulnerability reports move to Capabilities > Security & Compliance
    if "Vulnerability-Report" in norm:
        return "MOVE → Capabilities/Security & Compliance"

    # Files that are physically moving to a different section
    if "Decision_Maker" in norm:
        return "MOVE → Platform Overview"
    if "CIM-Message-Schema" in norm or "Socket_Events" in norm:
        return "MOVE → Reference"
    if nav_section == "Platform Overview" and "Getting_Started" in norm:
        return "MOVE → Platform Overview"
    if nav_section == "Reference" and "Getting_Started" in norm:
        return "MOVE → Reference"
    if nav_section == "How-to Guides" and "Getting_Started" in norm:
        return "MOVE → How-to Guides"

    # Folder renames only (content stays, path changes)
    if "Functional_Areas" in norm:
        return "RENAME section"
    if "Infrastructure_Hosting_Partner" in norm or "Reseller" in norm:
        return "MERGE → Hosting Partner"
    if "Human_Evaluator" in norm or "Quality_Manager" in norm:
        return "MERGE → Supervisor & QA Lead"
    if "AI_Quality_NLU_Specialist" in norm:
        return "MERGE → Conversation Designer"
    if "Integration_Specialist" in norm:
        return "MERGE → Developer / Integrator"

    return "KEEP (retag)"


def main():
    rows = []

    for md_file in sorted(PHASE4_DIR.rglob("*.md")):
        rel_path = str(md_file.relative_to(PHASE4_DIR))
        title = read_frontmatter_title(md_file) or md_file.stem.replace("-", " ")
        nav_section, nav_sub, audience = classify_file(rel_path)
        action = determine_action(rel_path, nav_section, nav_sub)
        notes = flag_notes(rel_path, nav_section)

        rows.append({
            "current_path": rel_path,
            "title": title,
            "nav_section": nav_section,
            "nav_sub_section": nav_sub,
            "audience_tag": audience,
            "action": action,
            "notes": notes,
        })

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "current_path", "title", "nav_section", "nav_sub_section",
            "audience_tag", "action", "notes"
        ])
        writer.writeheader()
        writer.writerows(rows)

    # Summary
    from collections import Counter
    section_counts = Counter(r["nav_section"] for r in rows)
    action_counts = Counter(r["action"] for r in rows)
    flagged = [r for r in rows if r["notes"]]

    print(f"\nContent Mapping Complete — {len(rows)} files processed")
    print(f"Output: {OUTPUT_CSV}\n")
    print("Files per nav section:")
    for section, count in sorted(section_counts.items()):
        print(f"  {count:>4}  {section}")
    print("\nActions required:")
    for action, count in sorted(action_counts.items(), key=lambda x: -x[1]):
        print(f"  {count:>4}  {action}")
    print(f"\nFiles needing review: {len(flagged)}")


if __name__ == "__main__":
    main()
