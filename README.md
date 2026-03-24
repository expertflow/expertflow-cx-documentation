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

The documentation is organised into 5 top-level sections:

| # | Section | Purpose |
| --- | --- | --- |
| 1 | **Getting Started** | Role-based entry points — one path per persona |
| 2 | **Platform Overview** | Evaluation and orientation content |
| 3 | **Capabilities** | Topic-based browsing — what the platform can do |
| 4 | **How-to Guides** | Task-based guides organised by persona |
| 5 | **Reference** | Schemas, APIs, glossary |

Personas: Agent · Administrator · Supervisor & QA Lead · Conversation Designer / AI Specialist · Developer / Integrator · Hosting Partner · Platform Operator (cross-cutting sub-path)

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

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the branch and PR workflow.
