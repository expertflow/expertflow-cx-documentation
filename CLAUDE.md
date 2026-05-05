# ExpertFlow CX Documentation Project

## What this project is
A Docusaurus documentation site for the ExpertFlow CX contact center platform.
All content lives under `docs-site/docs/cx/`.

## Authoritative rule files — read these before making any content decisions

| File | Purpose |
|---|---|
| `Phase3/Content_Placement_Guide.yaml` | Canonical rules: where content goes, frontmatter spec, section definitions, edge cases, audit triggers |
| `Phase3/Persona_Model.md` | Persona definitions, clusters, golden paths, and audience tag values |

When in doubt about placement, frontmatter, or audience tags — the YAML is the source of truth.

## Content structure

```
docs-site/docs/cx/
  Getting_Started/       # tutorial — one quick-start per persona
  Platform_Overview/     # orientation — evaluation content, no task instructions
  Capabilities/          # explanation — feature-domain browsing, not persona-based
  How-to_Guides/         # how-to — task guides, organised by persona subfolder
  Reference/             # reference — specs, APIs, schemas, hardware sizing
  Solutions/             # explanation — business-outcome overviews, not config steps
```

Sidebar order is fixed (see `sidebar_top_level_order` in the YAML). Do not reorder top-level sections.

## Frontmatter — required fields for every doc

```yaml
title:        # human-readable, shown in sidebar
summary:      # one sentence — what this doc covers
doc-type:     # how-to | tutorial | explanation | reference | landing
last-updated: # YYYY-MM-DD
```

`audience` is optional for pure reference content; required for persona-specific docs.
Valid audience tags: `agent`, `supervisor-qa`, `administrator`, `platform-operator`, `partner`, `conversation-designer`, `developer-integrator`.
Retired tags (never use): `hosting-partner`, `reseller-partner`, `platform-overview`.

## Key rules to apply on every content change

1. **Placement first** — check `Content_Placement_Guide.yaml` sections and edge_cases before placing any file.
2. **No duplication** — multi-audience content lives in the primary persona folder; other personas link to it.
3. **Diátaxis discipline** — explanation content never contains step-by-step instructions; how-to content never explains why a feature exists.
4. **Channel naming** — channel overviews must be `Capabilities/Digital_Channels/<ChannelName>/index.md`, never a flat file.
5. **Sidebar index.md rule** — when `index.md` is the category link, it must NOT also appear in `items: []`.

## Slash commands available in this project

| Command | When to use |
|---|---|
| `/doc-review` | Review a content change (PR or local diff) against the guidelines |
