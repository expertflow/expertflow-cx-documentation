# ExpertFlow CX Documentation

This repository contains the ExpertFlow CX platform documentation, restructured from a legacy Confluence knowledge base into a persona-driven, Diátaxis-compliant framework published via Docusaurus.

## Current Status

Restructure project in progress — see [Phase3/Restructure_Project_Plan.md](Phase3/Restructure_Project_Plan.md) for milestone status.

| Milestone | Status |
| --- | --- |
| M1 — Persona Model & Navigation Design | ✅ Complete |
| M2 — Full Content Mapping | ✅ Complete |
| M3 — Folder Restructure | ✅ Complete |
| M4 — Metadata Re-tagging | ✅ Complete |
| M5 — Content Gap Filling (placeholders) | ✅ Complete |
| M6 — Navigation Config Update | ✅ Complete |
| M7 — Cross-link Audit | 🔲 Not started |

## Navigation Structure

The documentation is organised into 6 top-level sections (order is fixed — do not change without updating `Phase3/Content_Placement_Guide.yaml`):

| # | Section | Purpose |
| --- | --- | --- |
| 1 | **Getting Started** | Role-based entry points — one path per persona |
| 2 | **Solutions** | Business-outcome overviews for pre-sales and evaluation audiences |
| 3 | **Platform Overview** | Evaluation and orientation content |
| 4 | **Capabilities** | Topic-based browsing — what the platform can do |
| 5 | **How-to Guides** | Task-based guides organised by persona |
| 6 | **Reference** | Schemas, APIs, SDKs, hardware sizing, glossary |

Personas: Agent · Administrator · Supervisor & QA Lead · Conversation Designer / AI Specialist · Developer / Integrator · Platform Operator · Partner

## Repository Structure

```text
DocWithGeminiCLI/
├── Restructured/          # Live content — source of truth for the docs site
│   ├── Getting_Started/
│   ├── Platform_Overview/
│   ├── Capabilities/
│   ├── How-to_Guides/
│   └── Reference/
├── Phase3/                # Restructure project artefacts
│   ├── Restructure_Project_Plan.md
│   ├── Revised_Persona_Model.md
│   ├── Navigation_Skeleton_Tree.md
│   └── Content_Mapping_Table.csv
├── Phase4/                # Previous structure (source for M3 migration — do not edit)
├── docs-site/             # Docusaurus site configuration
├── scripts/               # Migration and maintenance scripts
│   ├── migrate_m3.py      # M3 folder restructure
│   ├── retag_m4.py        # M4 metadata re-tagging
│   ├── generate_content_map.py  # M2 content mapping
│   ├── check_links.py     # M7 link checker
│   ├── repair_links.py    # M7 link repair
│   └── archive/           # Superseded scripts from earlier phases
└── archive/               # Historical project reports and prompts
```

## Running the Docs Site Locally

```bash
cd docs-site
npm install
npm run start      # Dev server at http://localhost:3000
npm run build      # Production build
```

## Working with Claude Code

This project uses [Claude Code](https://claude.ai/code) as an AI assistant. Two project-specific files configure how it works.

### CLAUDE.md — always-on project context

[CLAUDE.md](CLAUDE.md) is loaded automatically at the start of every Claude Code session. It tells Claude:

- Where the authoritative rule files live (`Phase3/`)
- The content structure and section purposes
- Required frontmatter fields and valid audience tag values
- The five key rules to apply on every content change

You do not need to do anything to activate it — Claude reads it on startup.

### /doc-review — content review command

Run `/doc-review` in Claude Code to review changed documentation files against the project guidelines before merging.

```bash
/doc-review              # reviews your current working diff against main
/doc-review my-branch    # reviews a specific branch
```

The command checks:

| Check | What it validates |
| --- | --- |
| **Frontmatter** | All required fields present, valid `doc-type`, valid `audience` tags, no retired tags |
| **Content placement** | File is in the correct section and persona subfolder per `Phase3/Content_Placement_Guide.yaml` |
| **Diátaxis discipline** | Content type matches the section — e.g. no step-by-step instructions inside a Capabilities explanation doc |
| **Sidebar rules** | `index.md` not duplicated as a child item; correct top-level section order |
| **Audit triggers** | Any open rule-change alerts that affect the files being changed |

Output is a structured report with **FAIL** (must fix before merge), **WARN** (should fix), and **PASS** items.

### Audit triggers — tracking rule changes

When a content placement rule is updated in `Phase3/Content_Placement_Guide.yaml`, existing files may no longer comply. The `audit_triggers` section at the bottom of that file records:

- Which rule changed and when
- Which folder needs to be swept (`sweep`)
- What to check in those files (`check`)
- Whether the sweep is complete (`status: open` or `closed`)

**If you change a rule**, add an `open` trigger entry at the same time. `/doc-review` will automatically flag non-compliant files as they are touched in future PRs. Set `status: closed` once all affected files have been updated.

### Authoritative rule files

| File | Purpose |
| --- | --- |
| [Phase3/Content_Placement_Guide.yaml](Phase3/Content_Placement_Guide.yaml) | Where content goes, frontmatter spec, section rules, edge cases, audit triggers |
| [Phase3/Persona_Model.md](Phase3/Persona_Model.md) | Persona definitions, clusters, golden paths, valid audience tag values |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and PR workflow.
