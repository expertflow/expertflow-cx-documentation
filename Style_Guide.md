# ExpertFlow CX Documentation — Style Guide

**Version:** 1.0  
**Date:** 2026-07-13  
**Maintained alongside:** `Phase3/Content_Placement_Guide.yaml` · `Phase3/Persona_Model.md` · `CONTRIBUTING.md`

---

## 1. Purpose

This guide is the single reference for anyone writing or reviewing ExpertFlow CX documentation. It covers tone and formatting, document types, where content belongs, frontmatter, audience tagging, and special formatting patterns. When in doubt, the canonical rule source is `Phase3/Content_Placement_Guide.yaml`.

---

## 2. Tone and Writing Style

- **Professional, helpful, and concise.** Write for a technical audience who needs to act, not be impressed.
- **Task-first.** Lead with what the reader needs to do or know, not with background history.
- **Active voice.** "Click Save" not "The Save button should be clicked."
- **Second person.** Address the reader as "you."
- **No marketing language.** Avoid superlatives ("powerful", "seamless", "world-class"). Describe what the platform does, not how great it is.
- **Format:** Standard GitHub Flavored Markdown.
- **Images:** Place in `docs-site/static/img/` and reference with a relative path.

---

## 3. Document Types (Diátaxis)

Every document belongs to exactly one type. The type determines what content is allowed and which section of the site it lives in.

| `doc-type` value | Purpose | What it contains | What it must NOT contain |
|---|---|---|---|
| `tutorial` | First steps for a new user | Achievable, task-focused steps for a single session | Feature explanations, reference specs |
| `how-to` | Step-by-step task guide | Numbered steps to complete a specific task | Explanations of why a feature exists |
| `explanation` | Capability or concept overview | What a feature does, how it fits the platform | Step-by-step instructions |
| `reference` | Technical look-up content | Specs, schemas, APIs, port lists, sizing tables | Task guides, concept explanations |
| `landing` | Section index page | Navigation links and brief section description | Primary content |

**Diátaxis discipline is strict:** explanation content never contains step-by-step instructions. How-to content never explains why a feature exists. If you find yourself doing both, split the document.

---

## 4. Content Structure

All active documentation lives under `docs-site/docs/cx/`.

```
docs-site/docs/cx/
  Getting_Started/       # tutorial — one quick-start per persona
  Solutions/             # explanation — business-outcome overviews
  Platform_Overview/     # orientation — evaluation content, no task instructions
  Capabilities/          # explanation — feature-domain browsing, not persona-based
  How-to_Guides/         # how-to — task guides, organised by persona subfolder
  Reference/             # reference — specs, APIs, schemas, hardware sizing
```

### Sidebar order is fixed

Do not reorder, merge, or insert new top-level sections without updating `Phase3/Content_Placement_Guide.yaml` first.

| # | Section | Purpose |
|---|---|---|
| 1 | Getting Started | Universal onboarding entry point — role-based first steps |
| 2 | Solutions | Business-outcome overviews for evaluation audiences |
| 3 | Platform Overview | Platform-level orientation for anyone evaluating or onboarding |
| 4 | Capabilities | Feature-domain reference browsing, consulted after orientation |
| 5 | How-to Guides | Task instructions by persona, reached from Getting Started or Capabilities |
| 6 | Reference | Technical lookup (specs, APIs, schemas), consulted on demand |

### Section rules at a glance

**Getting Started** — one quick-start per persona; content must be achievable in a single session; link out to How-to Guides for deeper task coverage.

**Solutions** — lead with the business problem, not the feature; cover outcomes, supported channels, and links to Capabilities and How-to Guides; no step-by-step configuration.

**Platform Overview** — orientation and evaluation content only; no step-by-step task instructions; no detailed specs or sizing tables (link to Reference instead).

**Capabilities** — feature explanations organised by topic domain; tag with all relevant persona audience values; no task steps.

**How-to Guides** — place in the primary persona's subfolder; tag all relevant audiences in frontmatter; do not duplicate content across persona folders — link instead.

**Reference** — if a reader needs to look something up (a schema, a flag value, a port number, a sizing table), it belongs here; no audience tag required for pure reference material.

---

## 5. Personas and Audience Tags

There are 7 personas across 3 clusters. Use these exact `audience` tag values in frontmatter.

### Cluster 1 — Contact Center Users

| Persona | `audience` tag | Owns |
|---|---|---|
| Agent | `agent` | Handling interactions, managing presence, applying wrap-up codes, using co-pilot |
| Supervisor / QA Lead | `supervisor-qa` | Real-time monitoring, QA workflow, transcript review, historical reporting, WFM schedules |

### Cluster 2 — Platform People

| Persona | `audience` tag | Owns |
|---|---|---|
| Administrator | `administrator` | Queue and routing config, channel setup, user and team management, business hours, license monitoring |
| Platform Operator | `platform-operator` | Installation, upgrades, health monitoring, backup/restore, Kubernetes, SSL/networking |
| Partner | `partner` | Tenant onboarding and lifecycle, subscription tiers, license management across tenants, white-labeling |

> **Partner** applies to multi-tenant and hosted deployments only. In single-tenant self-hosted deployments this function does not exist.

> **Platform Operator** is deployment-agnostic — tag any installation, upgrade, monitoring, backup, or infrastructure content with this value regardless of deployment model.

### Cluster 3 — Builders

| Persona | `audience` tag | Owns |
|---|---|---|
| Conversation Designer / AI Specialist | `conversation-designer` | Conversation Studio flow design, bot connector registration, NLU tuning, handover logic |
| Developer / Integrator | `developer-integrator` | AgentManager SDK, WebChannel SDK, CRM connectors, webhooks, Third-party Activity API |

### Retired tags — never use

| Retired tag | Replace with |
|---|---|
| `hosting-partner` | `platform-operator` and/or `partner` |
| `reseller-partner` | `partner` |
| `platform-overview` | Not a persona — do not use as an audience tag |

### Tagging rules

- A document can carry multiple audience tags. Example — a monitoring guide for Platform Operator and Partner:
  ```yaml
  audience:
    - platform-operator
    - partner
  ```
- Capabilities content is feature-domain-based, not persona-based. Tag it with the audience tags of every persona that would read it.
- Reference content (hardware sizing, schemas, port lists) carries no audience tag — it is accessed by whoever needs it.

### Persona sub-paths (for large teams with split roles)

**Supervisor / QA Lead** sub-paths: `monitoring` · `quality` · `reporting` · `workforce_management`

**Conversation Designer** sub-paths: `flow_design` · `ai_nlu`

**Developer / Integrator** sub-paths: `ui_sdk` · `integration`

---

## 6. Frontmatter

Every document requires these fields:

```yaml
---
title:        # Human-readable title shown in the sidebar and page heading
summary:      # One sentence — what this document covers
doc-type:     # how-to | tutorial | explanation | reference | landing
last-updated: # YYYY-MM-DD
---
```

### Optional fields

```yaml
audience:      # list — one or more persona tags (required for persona-specific docs; omit for pure reference)
product-area:  # list — feature domains, e.g. [reporting, routing, digital-channels]
difficulty:    # beginner | intermediate | advanced (omit if not meaningful)
keywords:      # list — additional search terms and synonyms not in the title
aliases:       # list — former page titles or common shorthand for search/redirects
```

### `audience` is required for persona-specific docs; omit for pure reference content

Valid `doc-type` values: `how-to` · `tutorial` · `explanation` · `reference` · `landing`

---

## 7. Content Placement Rules

### Where does this content go?

| Content type | Correct section |
|---|---|
| First steps for a new persona | `Getting_Started/<For_PersonaName>/` |
| Business outcome overview | `Solutions/` |
| Platform orientation for evaluation | `Platform_Overview/` |
| What a feature does | `Capabilities/` |
| How to complete a task | `How-to_Guides/<PersonaFolder>/` |
| API spec, schema, port list, sizing table | `Reference/` |
| Hardware sizing | `Reference/Architecture_and_Infrastructure/` — never in a persona folder |

### Multi-audience content

Place in the **primary persona's** folder. Add all audience tags in frontmatter. Do not duplicate the file in other persona folders — use links.

**Example:** A monitoring guide relevant to both Platform Operator and Partner goes in `How-to_Guides/Platform_Operator/` with `audience: [platform-operator, partner]`. The Partner index links to it.

### Channel naming convention

Every channel under `Capabilities/Digital_Channels/` must have its own subfolder. The channel overview is always `index.md` inside that subfolder.

```
# Correct
Capabilities/Digital_Channels/Facebook/index.md
Capabilities/Digital_Channels/WhatsApp/index.md
Capabilities/Digital_Channels/Email/index.md

# Wrong
Capabilities/Digital_Channels/Facebook-Channel-Overview.md
Capabilities/Digital_Channels/Email-Channel-Overview.md
```

### Sidebar `index.md` rule

When a folder uses its `index.md` as the Docusaurus category link, that `index.md` must **not** also appear as a child item inside `items: []`. Never use `{ type: 'autogenerated' }` on a directory whose `index.md` is the category link — autogenerated will surface it as a duplicate child. Always list children explicitly.

### Connector docs

| Part | Location |
|---|---|
| What the connector does and what it supports | `Capabilities/Integrations_and_Connectors/` |
| How to deploy and configure it | `How-to_Guides/Developer_Integrator/` |

### Routing and queues

| Part | Location |
|---|---|
| How routing works (explanation) | `Capabilities/Routing_and_Queue_Management/` |
| How to configure queues and routing rules | `How-to_Guides/Administrator/` |

### Quality management

| Part | Location |
|---|---|
| What QM features exist | `Capabilities/Quality_Management/` |
| How to use QM features | `How-to_Guides/Supervisor_and_QA_Lead/` |

### Platform architecture

| Part | Location |
|---|---|
| Orientation summary — what the layers are | `Platform_Overview/Platform-Architecture.md` |
| Detailed reference — deployment topology, exact diagrams, port lists | `Reference/Architecture_and_Infrastructure/` |

---

## 8. Formatting Patterns

### Admonitions (Callout Panels)

Use Docusaurus admonitions to highlight important information. They render as styled, colored panels.

**Syntax:**

```md
:::note

Content goes here.

:::
```

**Available types:**

| Type | Color | When to use |
|---|---|---|
| `:::note` | Blue | Neutral supplementary information the reader should be aware of |
| `:::tip` | Green | Best practices, shortcuts, or helpful suggestions |
| `:::caution` | Yellow | Restrictions, conditional behavior, or things that may cause confusion if missed |
| `:::danger` | Red | Actions that can cause data loss, system failure, or irreversible consequences |

**Rules:**

- Choose the type based on content severity — not preference.
- Keep admonition content concise. If it exceeds 3–4 bullet points, move the content into the main body.
- Leave a blank line after the opening `:::type` and before the closing `:::`, or Markdown inside will not render correctly.
- Do not nest admonitions.

**Example:**

```md
:::caution

- A bot connector that is associated with a Channel **cannot be deleted** until the association is removed.
- The **API URL** field appears only when the Bot Type is **Rasa** or **Custom**.

:::
```

### FAQ Pages

Use the native HTML `<details>` / `<summary>` expand/collapse pattern.

```md
## Section Heading

<details>
<summary>Question goes here?</summary>

Answer goes here. Can include multiple paragraphs, lists, or code blocks.

</details>

<details>
<summary>Another question?</summary>

Another answer.

</details>
```

**Rules:**

- One `<details>` block per question — do not nest them.
- Leave a blank line between the `<summary>` closing tag and the answer body, or Markdown inside the block will not render correctly.
- Group questions under H2 headings by topic (e.g. `## Contracts`, `## Troubleshooting`).
- Do not use the old grouped-bullet format (`- **Question?** Answer`) for new FAQ pages.

---

## 9. No-Duplication Rule

Content lives in one place. Every other path that needs it **links** to it.

**Example — Hardware Sizing:**

```
CTO reading Platform Overview
  └── "What infrastructure do I need?"
        → links to Reference/Architecture_and_Infrastructure/

Platform Operator following their golden path
  └── Step: "Hardware Sizing for Large Scale Clusters"
        → links to same Reference page
```

Same page, different arrival path. Never copy content to serve two audiences — update the audience tags and add a link instead.

---

## 10. Quick Reference Checklist

Before opening a PR, confirm:

- [ ] Frontmatter has `title`, `summary`, `doc-type`, and `last-updated`
- [ ] `audience` tag is present for any persona-specific doc (omitted for pure reference)
- [ ] Only valid audience tags are used — no retired tags (`hosting-partner`, `reseller-partner`, `platform-overview`)
- [ ] File is placed in the correct section per Section 7
- [ ] How-to docs contain only steps, no capability explanations
- [ ] Explanation docs contain no step-by-step instructions
- [ ] Channel overview files follow the `Capabilities/Digital_Channels/<Channel>/index.md` pattern
- [ ] No content is duplicated — secondary audiences link to the primary file
- [ ] `index.md` is not listed as a child item in any sidebar category that already uses it as the category link
- [ ] Admonitions and FAQ blocks follow the formatting rules in Section 8

---

## 11. Source Files

| File | What it governs |
|---|---|
| `Phase3/Content_Placement_Guide.yaml` | Canonical placement rules, frontmatter spec, edge cases, audit triggers |
| `Phase3/Persona_Model.md` | Persona definitions, golden paths, cluster structure |
| `CONTRIBUTING.md` | Contribution workflow, branch naming, PR process, local dev setup |
| `CLAUDE.md` | AI agent instructions for this project |
