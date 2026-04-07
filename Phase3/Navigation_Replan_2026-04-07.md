# Navigation & Structure Replan
**Date:** 2026-04-07
**Status:** Awaiting Phase 0 decisions before execution
**Supersedes:** `Final_Navigation_Tree_v11.yaml` (archived — stale, references old Phase4 paths)

---

## Context

The `Restructured/` folder is the authoritative content state (~410 files). It is symlinked into the Docusaurus site as `docs-site/docs/cx`. The `sidebars.js` is the live navigation config. The old `Final_Navigation_Tree_v11.yaml` predates the current folder structure and cannot be patched — it still references `Role-Based_Guides/...` paths that no longer exist.

`Content_Mapping_Table.csv` is also stale — significant file changes were made after it was generated. The actual `Restructured/` folder is the source of truth.

---

## Audit Findings

### How-to_Guides — file distribution

| Folder | Files | Status |
|---|---|---|
| Administrator | 65 | Correct |
| Supervisor_and_QA_Lead | 47 | Correct |
| Developer_Integrator | 44 | Correct |
| Hosting_Partner | 38 | **Wrong — all Platform Operator infra content** |
| Agent | 19 | Correct |
| Conversation_Designer | 17 | Correct |
| Reseller_Partner | 7 | Correct content, wrong name |
| Platform_Operator | 0 | **Empty — never populated** |

### Capabilities — coverage vs. Persona_Model scope

| Topic (per Persona_Model) | Folder exists | Status |
|---|---|---|
| Digital Channels | ✓ | Populated |
| Voice & Video | ✓ | Populated |
| Reporting & Analytics | ✓ | Populated |
| Security & Compliance | ✓ | Populated |
| Workforce Management | ✓ | Thin (3 files) |
| Customer Management | ✓ | Thin (2 files) |
| AI & Automation | ✗ | **Missing entirely** |
| Quality Management | ✗ | **Missing — content is in Supervisor_and_QA How-to** |
| Routing & Queue Management | ✗ | **Missing — content is in Administrator How-to** |
| Conversation Studio | ✗ | **File is in Platform_Overview/ — wrong section** |
| Integrations & Connectors | ✗ | **Missing — content is in Developer_Integrator How-to** |

### Reference — coverage vs. Persona_Model spec

| Sub-section (per Persona_Model) | Folder exists | Status |
|---|---|---|
| Schemas & Data Model | ✓ | CIM + Socket Events populated |
| Glossary | ✓ | 1 file |
| Architecture & Infrastructure | ✗ | **No folder** |
| API & SDK | ✗ | **No folder — AgentManager SDK floating in root** |

### Other findings

- `Getting_Started/For_Hosting_Partners/` contains quick-starts for **two distinct personas** (Platform Operator + Partner) — they need separate entry points
- `_unmapped/Archive-Notice.md` is a meta-file about retired content — not a publishable docs page
- `sidebars.js` line 204–207: label says "Platform Operator" but `dirName` points to `Hosting_Partner/` — wrong in both directions
- `sidebars.js` "Reseller Partner" label doesn't match persona model canonical name "Partner"

---

## The 6 Structural Problems

**P1 — Platform Operator identity crisis**
`Platform_Operator/` was created as a placeholder and never populated. All its content lives in `Hosting_Partner/` under the wrong name. These are two distinct personas per the model.

**P2 — Partner naming drift**
Three names for one persona: folder = `Reseller_Partner/`, model = `Partner`, audience tag = `partner`. An AI agent following the model will be confused.

**P3 — Getting_Started doesn't reflect the persona split**
`For_Hosting_Partners/` contains quick-starts for two distinct personas. They need separate entry points.

**P4 — Capabilities is 40% missing**
AI & Automation, Quality Management, Routing & Queue Management, Integrations & Connectors, and Conversation Studio are listed as Capabilities topics in the model but have no folder there. Content exists — it's in the wrong section type.

**P5 — Reference has no internal structure**
No `Architecture_and_Infrastructure/` or `API_and_SDK/` sub-folders. `Agent-Desk-Developer-Guide.md` is floating in the root. Hardware Sizing is in `Hosting_Partner/` instead of Reference.

**P6 — The YAML is the wrong tool for AI agent content placement**
A nav tree (per-file inventory) tells an agent what exists. A placement agent needs rules: given audience + content type → which folder. These are different documents serving different purposes.

---

## Revised Artifact Strategy

### Retire `Final_Navigation_Tree_v11.yaml`
Move to `Phase3/archive/`. It is redundant with `sidebars.js` and becomes stale every time a file moves.

### Create two purpose-built documents instead

**1. `Content_Placement_Guide.yaml`** — AI agent placement rulebook
Structured as rules, not inventory. Defines:
- Every persona: canonical name, audience tag, folder paths, content ownership, explicit exclusions
- Every section: what Diátaxis type lives there, what doesn't
- Edge case rules: multi-audience content, hardware sizing, cross-cutting features
- Frontmatter spec: required fields and valid values

Example structure:
```yaml
personas:
  platform-operator:
    canonical_name: Platform Operator
    audience_tag: platform-operator
    how_to_folder: How-to_Guides/Platform_Operator/
    getting_started_folder: Getting_Started/For_Platform_Operators/
    owns:
      - installation and initial deployment (RKE2, Helm, networking, SSL)
      - version upgrades and patch procedures
      - platform health monitoring and alerting
      - backup and restore
      - infrastructure troubleshooting
    not:
      - tenant management (→ partner)
      - business configuration — queues, routing, channels (→ administrator)
  partner:
    canonical_name: Partner
    audience_tag: partner
    how_to_folder: How-to_Guides/Partner/
    getting_started_folder: Getting_Started/For_Partners/
    owns:
      - tenant onboarding and provisioning
      - tenant lifecycle management
      - subscription tiers and capacity planning
      - license management across tenants
      - white-labeling

sections:
  getting_started:
    diátaxis_type: tutorial
    rule: first-steps content per persona — one quick-start per persona, no deep task guides
  platform_overview:
    diátaxis_type: orientation
    rule: evaluation and orientation content — not a persona path, no step-by-step tasks
    not: detailed architecture diagrams, hardware sizing tables, port/network requirements (→ Reference)
  capabilities:
    diátaxis_type: explanation
    rule: feature-level explanations — what the platform can do, organised by topic
    not: step-by-step task instructions (→ How-to Guides), API specs (→ Reference)
  how_to_guides:
    diátaxis_type: how-to
    rule: task-based guides organised by persona
  reference:
    diátaxis_type: reference
    rule: technical lookup content — APIs, schemas, hardware sizing, deployment specs
    sub_sections:
      - Architecture_and_Infrastructure
      - API_and_SDK
      - Schemas_and_Data_Model
      - Glossary

edge_cases:
  hardware_sizing: always Reference/Architecture_and_Infrastructure/ — never in a persona folder
  multi_audience: place in primary audience folder, add all audience tags in frontmatter
  connector_overview: Capabilities/Integrations_and_Connectors/ (explanation of what it does)
  connector_configuration: How-to_Guides/{persona}/ (steps to configure it)
```

**2. `sidebars.js`** — Docusaurus rendering config only
Maintained by humans after structural changes. Not auto-generated.

---

## Phase 0 — Decisions Required Before Execution

| # | Decision | Options | Recommendation |
|---|---|---|---|
| D1 | `Reseller_Partner/` folder name | Keep, or rename to `Partner/` | **Rename** — matches model canonical name and audience tag |
| D2 | Missing Capabilities topics | Create empty folders now, or wait for content | **Create folders + index.md now** — structure leads content creation |
| D3 | `Hosting_Partner/` after migration | Delete, or keep as redirect/alias | **Delete** — keeping it perpetuates the confusion that caused P1 |
| D4 | `Conversation-Studio.md` in Platform_Overview | Keep, or move to Capabilities | **Move to Capabilities** — it's a feature explanation; Platform_Overview keeps a summary pointer |

---

## Phase 1 — Folder Restructure

Python script with dry-run option. All moves logged to a migration report.

### 1a. Resolve Platform Operator / Hosting Partner

| Action | From | To |
|---|---|---|
| Move ~36 infra/ops files | `How-to_Guides/Hosting_Partner/` | `How-to_Guides/Platform_Operator/` |
| Move 1 file | `How-to_Guides/Hosting_Partner/Onboarding-a-New-Tenant.md` | `How-to_Guides/Partner/` |
| Move 1 file | `How-to_Guides/Hosting_Partner/Hardware-Sizing-Calculator.md` | `Reference/Architecture_and_Infrastructure/` |
| Delete | `How-to_Guides/Hosting_Partner/` | — |

### 1b. Fix Getting_Started persona split

| Action | Detail |
|---|---|
| Create | `Getting_Started/For_Platform_Operators/` |
| Move | `For_Hosting_Partners/Platform-Operator-Quick-Start.md` → `For_Platform_Operators/` |
| Rename | `Getting_Started/For_Hosting_Partners/` → `Getting_Started/For_Partners/` |

### 1c. Rename Partner folder

| Action | Detail |
|---|---|
| Rename | `How-to_Guides/Reseller_Partner/` → `How-to_Guides/Partner/` |
| Update | `Partner/index.md` — update title and internal references |

### 1d. Create missing Reference sub-structure

| Action | Detail |
|---|---|
| Create | `Reference/Architecture_and_Infrastructure/` + `index.md` |
| Create | `Reference/API_and_SDK/` + `index.md` |
| Move | `Reference/Agent-Desk-Developer-Guide.md` → `Reference/API_and_SDK/` |

### 1e. Create missing Capabilities sub-structure

| Action | Detail |
|---|---|
| Create | `Capabilities/AI_and_Automation/` + `index.md` |
| Create | `Capabilities/Quality_Management/` + `index.md` |
| Create | `Capabilities/Routing_and_Queue_Management/` + `index.md` |
| Create | `Capabilities/Integrations_and_Connectors/` + `index.md` |
| Move | `Platform_Overview/Conversation-Studio.md` → `Capabilities/` |
| Add | Summary pointer in `Platform_Overview/index.md` for Conversation Studio |

### 1f. Resolve _unmapped

| Action | Detail |
|---|---|
| Move | `_unmapped/Archive-Notice.md` → `Phase3/` (not a publishable docs page) |

---

## Phase 2 — Fix `sidebars.js`

Execute after Phase 1. All changes are mechanical.

| Fix | Change |
|---|---|
| Getting Started | Replace `For_Hosting_Partners` block with `For_Platform_Operators` + `For_Partners` entries |
| How-to: Platform Operator | Change `dirName` from `Hosting_Partner` → `Platform_Operator`; fix index link |
| How-to: Partner | Rename label "Reseller Partner" → "Partner"; change `dirName` to `Partner` |
| Capabilities | Add `AI_and_Automation`, `Quality_Management`, `Routing_and_Queue_Management`, `Integrations_and_Connectors` as autogenerated categories |
| Reference | Add `Architecture_and_Infrastructure` and `API_and_SDK` categories |
| Reference | Move `Agent-Desk-Developer-Guide` entry from root into `API_and_SDK` |

---

## Phase 3 — Write `Content_Placement_Guide.yaml`

New file: `Phase3/Content_Placement_Guide.yaml`

Covers:
- All 7 personas with canonical names, audience tags, folder paths, ownership rules, and explicit exclusions
- All 5 top-level sections with Diátaxis type, inclusion rules, and exclusion rules
- Edge case rules (multi-audience, hardware sizing, connector docs, etc.)
- Frontmatter spec: required fields (`title`, `audience`, `type`), valid values per field

This document is maintained alongside `Persona_Model.md` and is the primary input for any AI agent doing content placement decisions.

---

## Phase 4 — Archive old YAML

Move `Final_Navigation_Tree_v11.yaml` → `Phase3/archive/Final_Navigation_Tree_v11.yaml`

Add a note at the top of the archived file explaining it was superseded by `Content_Placement_Guide.yaml` and the live `sidebars.js`.

---

## Execution Sequencing

```
Phase 0 (decisions) → Phase 1 (folders) → Phase 2 (sidebars.js) → Phase 4 (archive YAML)
                    ↘ Phase 3 (placement guide) — can run in parallel with Phase 1
```

Phase 1 must complete before Phase 2 (sidebars.js depends on folder names).
Phase 3 can start immediately — it is a new document independent of folder moves.
Phase 4 is the final cleanup step.

---

## Key Files

| File | Role |
|---|---|
| `Phase3/Persona_Model.md` | Authoritative persona and structure spec — start here |
| `Phase3/Navigation_Replan_2026-04-07.md` | This document |
| `Phase3/Content_Placement_Guide.yaml` | AI agent placement rulebook (to be created in Phase 3) |
| `DocWithGeminiCLI/Restructured/` | Authoritative content folder |
| `docs-site/sidebars.js` | Live Docusaurus navigation config |
| `Phase3/archive/Final_Navigation_Tree_v11.yaml` | Retired nav tree (to be archived in Phase 4) |
