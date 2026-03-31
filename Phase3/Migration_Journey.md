# Phase4 → Restructured: Migration Journey

**Project:** ExpertFlow CX Docs — Navigation & Persona Model Restructure
**Migration period:** 2026-03-24 → 2026-03-31
**Status:** Complete. Phase4 archived. `Restructured/` is the active content tree.

---

## Why We Migrated

The Phase4 documentation tree had accumulated structural debt over time:

- **12-persona model was overcrowded** — system users, decision makers, and infrastructure partners were treated as peers in the same navigation tier, causing overlap and confusion
- **Duplicate golden paths** — content like hardware sizing appeared in both the CTO and Hosting Partner paths
- **Role merging ignored** — smaller deployments where one person covers multiple roles had no guidance
- **Operational content had no home** — monitoring, upgrades, and backup guides were scattered or missing entirely

The migration was not a content rewrite. It was a **structural reorganisation** of ~400 existing documents into a cleaner, Diataxis-aligned navigation model.

---

## What Changed

### Persona Model

| Phase4 (12 personas) | Restructured |
| --- | --- |
| Agent | Agent (unchanged) |
| Supervisor | Supervisor & QA Lead (merged) |
| Human Evaluator | ↑ merged into Supervisor & QA Lead |
| Quality Manager | ↑ merged into Supervisor & QA Lead |
| Solution Admin | Administrator (renamed) |
| Conversation Designer | Conversation Designer / AI Specialist (merged) |
| AI / NLU Specialist | ↑ merged into Conversation Designer |
| Frontend Developer | Developer / Integrator (merged) |
| Integration Specialist | ↑ merged into Developer / Integrator |
| Infrastructure / Hosting Partner | Hosting Partner (merged) |
| Reseller | ↑ merged into Hosting Partner |
| Decision Maker / CTO | Removed as persona → became **Platform Overview** section |
| *(gap)* | **Platform Operator** added (new sub-path for operational guides, shared by Admin + Hosting Partner) |

### Top-Level Navigation

| Phase4 | Restructured |
| --- | --- |
| `Getting_Started/` | `Getting_Started/` (role-based entry points) |
| `Functional_Areas/` | `Capabilities/` (renamed; Diataxis: cross-cutting reference) |
| `Role_Based_Guides/` | `How-to_Guides/` (reorganised by persona cluster) |
| *(none)* | `Platform_Overview/` (new; non-persona orientation content) |
| *(none)* | `Reference/` (new; APIs, schemas, hardware sizing, deployment specs) |

### Notable Content Moves

| Content | From | To |
| --- | --- | --- |
| CIM Message Schema | `Role_Based_Guides/Frontend_Developer/` | `Reference/Schemas_and_Data_Model/CIM_Message_Schema/` |
| Socket Events | `Role_Based_Guides/Frontend_Developer/` | `Reference/Schemas_and_Data_Model/Socket_Events/` |
| Vulnerability Reports (3 files) | `Role_Based_Guides/Solution_Admin/` | `Capabilities/Security_and_Compliance/` |
| Hardware Sizing, Deployment Topology | (scattered) | `Reference/` (single home) |
| Decision Maker content (12 files) | `Role_Based_Guides/Decision_Maker/` | `Platform_Overview/` |
| Reseller content | `Role_Based_Guides/Reseller/` | `How-to_Guides/Hosting_Partner/` |

---

## How It Was Done (Milestones)

| # | Milestone | What happened |
| --- | --- | --- |
| M1 | Persona Model & Navigation Design | Designed the reduced persona model and 5-section nav structure. Outputs: `Revised_Persona_Model.md`, `Navigation_Skeleton_Tree.md` |
| M2 | Full Content Mapping | Script-generated a master CSV mapping all 403 Phase4 files to their new locations, sections, and audience tags. Output: `Content_Mapping_Table.csv` |
| M3 | Folder Restructure | Migration script physically moved/renamed files per the CSV into the new `Restructured/` folder tree |
| M4 | Metadata Re-tagging | Updated frontmatter `audience` tags on all files to the new 8-value tag schema. Platform Operator files dual-tagged. |
| M5 | Content Gap Filling | Created 5 placeholder files for identified gaps (Platform Operator guides, Hosting Partner quick-start, Conversation Designer quick-start). Content still TODO. |
| M6 | Navigation Config Update | `docs-site/docs/cx` symlink re-pointed from `Phase4/` → `Restructured/`. `sidebars.js` replaced with explicit 5-section manual config. |
| M7 | Cross-link Audit | 508 broken links found post-move → 504 auto-repaired across 253 files → 4 unresolvable (documented below) |

---

## Known Open Items

### Unresolvable Broken Links (4)

Manual fix required if these pages are ever published:

| File | Broken link | Reason |
| --- | --- | --- |
| `Capabilities/Voice_and_Video/Voice-Message-Schema.md` | `../../Developer/CIM-Message-Schema/` | Directory link, no `index.md` at target |
| `How-to_Guides/Hosting_Partner/Hardware-Sizing-Calculator.md` | `Partner-Lab-Demo-Setup.md` | File never existed in Phase4 |
| `Platform_Overview/Platform-Architecture.md` | `./cx_architecture.svg` | SVG was not copied into `Restructured/` |
| `Platform_Overview/index.md` | `Platform-Architecture-and-Scalability.md` | File never existed |

### Placeholder Content (5 files — content not yet written)

| File | Priority |
| --- | --- |
| `How-to_Guides/Platform_Operator/Monitoring-the-Platform.md` | High |
| `How-to_Guides/Platform_Operator/Upgrading-the-Platform.md` | High |
| `How-to_Guides/Platform_Operator/Backup-and-Restore.md` | High |
| `Getting_Started/For_Hosting_Partners/Hosting-Partner-Quick-Start.md` | Medium |
| `Getting_Started/For_Conversation_Designers/Conversation-Designer-Quick-Start.md` | Medium |

---

## Current State (as of 2026-03-31)

- `Restructured/` — active content tree, ~408 files, served by docs site
- `archive/Phase4/` — original content tree, archived for reference (not deleted)
- `Phase3/` — all project artefacts (persona model, mapping CSV, nav tree, scripts, this document)
- `docs-site/` — Docusaurus site, symlinked to `Restructured/`

---

## Reference Files

| File | Purpose |
| --- | --- |
| `Phase3/Revised_Persona_Model.md` | Canonical persona definitions and golden paths |
| `Phase3/Navigation_Skeleton_Tree.md` | 2-level nav skeleton with source mapping |
| `Phase3/Content_Mapping_Table.csv` | Master mapping: every file → section, action, audience tag |
| `Phase3/broken_links_report.md` | Full M7 link audit results |
| `Phase3/Gap_Analysis.md` | Content gap analysis produced during M2 |
| `archive/Phase4/` | Original Phase4 content tree (archived 2026-03-31) |
