# Documentation Restructure: Project Plan & Status

**Project:** ExpertFlow CX Docs — Navigation & Persona Model Restructure
**Started:** 2026-03-24
**Last updated:** 2026-03-31 (Phase4 archived; migration journey documented)

---

## Background

The existing Phase4 documentation was built on a 12-persona model that:

- Mixed system users, decision makers, and infrastructure partners as peers
- Created overlapping golden paths (e.g. hardware sizing in both CTO and Host paths)
- Ignored real-world role merging in smaller deployments
- Left operational support content (monitoring, upgrades, backup) with no home

This project redesigns the navigation structure and re-maps all ~400 documents to it.

---

## Key Design Decisions

| Decision | Resolution |
| --- | --- |
| 12 personas → reduced set | Consolidated to 5 operational personas + Platform Overview (non-persona) |
| Decision Maker / CTO | Removed as persona path → becomes **Platform Overview** section |
| Supervisor + Evaluator + QA Manager | Merged → **Supervisor & QA Lead** |
| Multi-tenant Host + Reseller | Merged → **Hosting Partner** |
| Conversation Designer + AI/NLU Specialist | Merged → **Conversation Designer / AI Specialist** |
| Frontend Developer + Integration Specialist | Merged → **Developer / Integrator** |
| "Functional Areas" naming | Renamed → **Capabilities** |
| Operational support content | New named sub-path → **Platform Operator** (shared by Admin + Hosting Partner) |
| CIM Message Schema + Socket Events | Moved from Frontend_Developer role folder → **Reference** |
| Hardware Sizing, Deployment Topology, Architecture Diagrams | Single home in **Reference**, linked from Platform Overview and role paths |
| Vulnerability Reports | Moved from Solution_Admin → **Capabilities > Security & Compliance** |

---

## Top-Level Navigation Structure

| # | Section | Diataxis Type | Purpose |
| --- | --- | --- | --- |
| 1 | **Getting Started** | Tutorial | Role-based entry points — first steps per persona |
| 2 | **Platform Overview** | Orientation | Evaluation/orientation content — not a persona path |
| 3 | **Capabilities** | Cross-cutting | Topic-based browsing (replaces "Functional Areas") |
| 4 | **How-to Guides** | How-to | Task-based guides organised by persona cluster |
| 5 | **Reference** | Reference | APIs, SDKs, schemas, hardware sizing, deployment specs |

---

## Milestones

### M1 — Persona Model & Navigation Design

Status: ✅ Complete

Redesign the persona model and define the new navigation structure.

| Output | File | Status |
| --- | --- | --- |
| Revised persona model | `Phase3/Revised_Persona_Model.md` | ✅ Done |
| Navigation skeleton tree | `Phase3/Navigation_Skeleton_Tree.md` | ✅ Done |

---

### M2 — Full Content Mapping

Status: ✅ Complete

Map all ~400 Phase4 files to the new navigation structure. Produce a master CSV as the decision record for all subsequent milestones.

| Output | File | Status |
| --- | --- | --- |
| Mapping script | `generate_content_map.py` | ✅ Done |
| Master mapping table | `Phase3/Content_Mapping_Table.csv` | ✅ Done |

Mapping summary (403 files):

| Nav Section | Files |
| --- | --- |
| How-to Guides | 230 |
| Capabilities | 92 |
| Reference | 55 |
| Platform Overview | 12 |
| Getting Started | 11 |
| Unmapped (index/meta) | 3 |

Actions required across all files:

| Action | Count |
| --- | --- |
| KEEP (retag audience tag only) | 161 |
| RENAME section (Functional Areas → Capabilities) | 89 |
| MOVE → Reference (CIM Schema, Socket Events, SDK/API files) | 55 |
| MERGE → Hosting Partner (Host + Reseller folders) | 40 |
| MERGE → Developer / Integrator | 24 |
| MOVE → Platform Overview (Decision_Maker folder) | 12 |
| MERGE → Supervisor & QA Lead | 12 |
| MOVE → Capabilities/Security & Compliance (Vulnerability Reports) | 3 |
| MERGE → Conversation Designer | 5 |
| MOVE → How-to Guides (misplaced Getting Started files) | 2 |

Flagged for dual-tagging (Platform Operator sub-path, 9 files):

- `Infrastructure_Hosting_Partner/HA-in-EF-SIP-Proxy.md`
- `Infrastructure_Hosting_Partner/RKE2-Uninstallation.md`
- `Infrastructure_Hosting_Partner/System-Behaviour-in-Failover.md`
- `Infrastructure_Hosting_Partner/Upgrade-to-MongoDB-Version-8.x.md`
- `Infrastructure_Hosting_Partner/Audit-Trail-Implementation-OpenSearch.md`
- `Solution_Admin/MongoDB-Slow-Query-Logs.md`
- `Solution_Admin/Redis-Slowlogs.md`
- `Frontend_Developer/Upgrade-Guide-Postgres-Vault-Cisco.md`
- `Integration_Specialist/Logging-and-Tracing-OpenSearch.md`

---

### M3 — Folder Restructure

Status: ✅ Complete

Physically reorganise the Phase4 folder structure to match the new navigation tree.
Script-based — write a migration script that moves/renames files per `Content_Mapping_Table.csv`.

Key moves:

- `Role_Based_Guides/Decision_Maker/` → `Platform_Overview/`
- `Role_Based_Guides/Frontend_Developer/CIM-Message-Schema/` → `Reference/Schemas_and_Data_Model/CIM_Message_Schema/`
- `Role_Based_Guides/Frontend_Developer/Socket_Events/` → `Reference/Schemas_and_Data_Model/Socket_Events/`
- `Role_Based_Guides/Infrastructure_Hosting_Partner/` + `Role_Based_Guides/Reseller/` → `How-to_Guides/Hosting_Partner/`
- `Role_Based_Guides/Human_Evaluator/` + `Role_Based_Guides/Quality_Manager/` → merged into `How-to_Guides/Supervisor_QA_Lead/`
- `Role_Based_Guides/AI_Quality_NLU_Specialist/` → merged into `How-to_Guides/Conversation_Designer/`
- `Role_Based_Guides/Integration_Specialist/` → merged into `How-to_Guides/Developer_Integrator/`
- `Functional_Areas/` → `Capabilities/` (rename only)
- 3 x Vulnerability Report files → `Capabilities/Security_Compliance/`
- Selected SDK/API reference files from `Frontend_Developer/` → `Reference/API_and_SDK/`

Prerequisite: Review and approve `Content_Mapping_Table.csv`

---

### M4 — Metadata Re-tagging

Status: ✅ Complete

Update frontmatter `audience` tags on all files to match the new persona tag schema.

New audience tag schema:

```text
agent | supervisor-qa | administrator | hosting-partner |
platform-operator | conversation-designer | developer-integrator | platform-overview
```

Notes:

- Platform Operator files get dual-tagged (e.g. `[hosting-partner, platform-operator]`)
- `platform-overview` tagged files have no persona golden path
- Reference files carry no audience tag (accessed via Reference nav + search)
- Script-based — read CSV, update frontmatter per row

---

### M5 — Content Gap Filling

Status: ✅ Complete (placeholders — content to be written)

Write missing content identified during mapping.

| Gap | Target Location | Status |
| --- | --- | --- |
| Platform Operator — Monitoring | `How-to_Guides/Platform_Operator/Monitoring-the-Platform.md` | ✅ Placeholder — **TODO: write content** |
| Platform Operator — Upgrading | `How-to_Guides/Platform_Operator/Upgrading-the-Platform.md` | ✅ Placeholder — **TODO: write content** |
| Platform Operator — Backup & Restore | `How-to_Guides/Platform_Operator/Backup-and-Restore.md` | ✅ Placeholder — **TODO: write content** |
| Hosting Partner quick-start | `Getting_Started/For_Hosting_Partners/Hosting-Partner-Quick-Start.md` | ✅ Placeholder — **TODO: write content** |
| Conversation Designer quick-start | `Getting_Started/For_Conversation_Designers/Conversation-Designer-Quick-Start.md` | ✅ Placeholder — **TODO: write content** |

---

### M6 — Navigation Config Update

Status: ✅ Complete

Update the docs site navigation config to reflect the new 5-section structure.

Changes made:

- `docs-site/docs/cx` symlink re-pointed from `Phase4/` → `Restructured/`
- `docs-site/sidebars.js` replaced autogenerated sidebar with explicit 5-section manual config (correct labels, ordered, `_unmapped` excluded)
- `docs-site/docusaurus.config.js` footer links updated to the new 5 sections

---

### M7 — Cross-link Audit

Status: ✅ Complete

Fix internal links broken by file moves in M3.

Results: 508 broken links found → 504 auto-repaired across 253 files → 4 remaining (unresolvable).

Unresolvable links (manual fix if needed):

- `Capabilities/Voice_and_Video/Voice-Message-Schema.md` → `../../Developer/CIM-Message-Schema/` (directory link, no index.md)
- `How-to_Guides/Hosting_Partner/Hardware-Sizing-Calculator.md` → `Partner-Lab-Demo-Setup.md` (file never existed)
- `Platform_Overview/Platform-Architecture.md` → `./cx_architecture.svg` (SVG not copied to Restructured/)
- `Platform_Overview/index.md` → `Platform-Architecture-and-Scalability.md` (file never existed)

Script: `scripts/audit_links_m7.py`  |  Full report: `Phase3/broken_links_report.md`

---

## Content Gaps Summary

| Gap | Priority | Milestone |
| --- | --- | --- |
| Platform Operator sub-path (3–5 guides needed) | High — sub-path has zero content | M5 |
| Hosting Partner quick-start | Medium | M5 |
| Conversation Designer quick-start | Medium | M5 |

---

## Post-Migration

**2026-03-31** — Phase4 archived to `archive/Phase4/`. `Restructured/` is now the sole active content tree.

Migration history documented in `Phase3/Migration_Journey.md`.

---

## Reference Files

| File | Purpose |
| --- | --- |
| `Phase3/Migration_Journey.md` | Full migration narrative — why, what changed, how, open items |
| `Phase3/Revised_Persona_Model.md` | Canonical persona definitions, golden paths, nav structure decisions |
| `Phase3/Navigation_Skeleton_Tree.md` | 2-level nav skeleton with source mapping and gap analysis |
| `Phase3/Content_Mapping_Table.csv` | Master mapping: every file → new section, action, audience tag |
| `Phase3/broken_links_report.md` | Full M7 link audit results (508 found, 504 repaired, 4 unresolvable) |
| `generate_content_map.py` | Script that produced the mapping table |
| `check_links.py` / `repair_links.py` | Existing link audit/repair scripts (reuse in M7) |
| `archive/Phase4/` | Original Phase4 content tree (archived 2026-03-31) |
