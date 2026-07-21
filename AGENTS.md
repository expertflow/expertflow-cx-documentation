# ExpertFlow CX Documentation Project

This file provides guidance to any AI coding tool (Claude Code, Codex, Gemini CLI, etc.) for working in this repository.

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

## Tone and writing style — apply when generating or editing content

- Professional, helpful, and concise. Write for a technical audience who needs to act, not be impressed.
- Task-first: lead with what the reader needs to do or know, not background history.
- Active voice ("Click Save", not "The Save button should be clicked").
- Second person — address the reader as "you".
- No marketing language — avoid superlatives ("powerful", "seamless", "world-class"); describe what the platform does, not how great it is.
- Format: standard GitHub Flavored Markdown. Images go in `docs-site/static/img/`, referenced with a relative path.

## Formatting patterns

**Admonitions** — use Docusaurus admonitions to highlight information; choose the type by severity, not preference:

| Type | When to use |
|---|---|
| `:::note` | Neutral supplementary information the reader should be aware of |
| `:::tip` | Best practices, shortcuts, or helpful suggestions |
| `:::caution` | Restrictions, conditional behavior, or things that may cause confusion if missed |
| `:::danger` | Actions that can cause data loss, system failure, or irreversible consequences |

Leave a blank line after the opening `:::type` and before the closing `:::`, or Markdown inside will not render. Keep content concise — if it exceeds 3–4 bullet points, move it into the main body. Do not nest admonitions.

**FAQ pages** — use the native `<details>`/`<summary>` pattern, one block per question, grouped under `##` headings by topic. Leave a blank line between `<summary>` and the answer body, or Markdown inside will not render. Do not use the old grouped-bullet format (`- **Question?** Answer`) for new FAQ pages.

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
