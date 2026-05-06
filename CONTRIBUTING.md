# Contributing to Expertflow CX Documentation

Welcome! We're glad you're here. This guide will help you understand our workflow for contributing to the documentation.

## GitHub Flow

We follow the [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) model — a simple, branch-based workflow where deployments happen on merge to `main`.

### 1. Create a Branch

Always create a new branch from `main` for your work. Use a descriptive name that reflects your changes:

```bash
git checkout -b docs/update-agent-guide
```

* `docs/` — documentation updates
* `fix/` — correcting errors
* `feature/` — new sections or structural changes

### 2. Make Your Changes

All active documentation lives under `docs-site/docs/cx/`. The structure is:

```text
docs-site/docs/cx/
  Getting_Started/       # tutorial — one quick-start per persona
  Platform_Overview/     # orientation — evaluation content, no task instructions
  Capabilities/          # explanation — feature-domain browsing, not persona-based
  How-to_Guides/         # how-to — task guides, organised by persona subfolder
  Reference/             # reference — specs, APIs, schemas, hardware sizing
  Solutions/             # explanation — business-outcome overviews, not config steps
```

Before placing or moving any file, read the authoritative rule files:

| File | Purpose |
| --- | --- |
| `Phase3/Content_Placement_Guide.yaml` | Where content goes, frontmatter spec, section definitions, edge cases |
| `Phase3/Persona_Model.md` | Persona definitions, audience tag values, and golden paths |

### 3. Frontmatter

Every document requires these frontmatter fields:

```yaml
---
title:        # human-readable title shown in the sidebar
summary:      # one sentence — what this doc covers
doc-type:     # how-to | tutorial | explanation | reference | landing
last-updated: # YYYY-MM-DD
---
```

`audience` is optional for pure reference content and required for all persona-specific docs. Valid values: `agent`, `supervisor-qa`, `administrator`, `platform-operator`, `partner`, `conversation-designer`, `developer-integrator`.

Never use retired tags: `hosting-partner`, `reseller-partner`, `platform-overview`.

### 4. Key Content Rules

1. **Placement first** — check `Content_Placement_Guide.yaml` sections and `edge_cases` before placing any file.
2. **No duplication** — multi-audience content lives in the primary persona folder; other personas link to it.
3. **Diátaxis discipline** — explanation content never contains step-by-step instructions; how-to content never explains why a feature exists.
4. **Channel naming** — channel overviews must be `Capabilities/Digital_Channels/<ChannelName>/index.md`, never a flat file.
5. **Sidebar `index.md` rule** — when `index.md` is the category link, it must NOT also appear in `items: []`.
6. **Sidebar order is fixed** — do not reorder top-level sections (see `sidebar_top_level_order` in the YAML).

### 5. Commit and Push

Commit your changes with clear, concise messages:

```bash
git add docs-site/docs/cx/path/to/changed-file.md
git commit -m "docs: add detailed agent desk setup steps"
git push origin docs/update-agent-guide
```

### 6. Open a Pull Request

Go to the GitHub repository and open a **Pull Request (PR)** from your branch to `main`.

* Provide a clear description of what changed and why.
* Link any relevant issues.
* The deployment workflow will automatically build your changes upon merge.

### 7. Review and Merge

Wait for feedback or approval from other collaborators. Once approved, your PR will be merged into `main` and the documentation site will update automatically.

---

## Reviewing Your Changes

Run `/doc-review` in Claude Code to review a content change (local diff or PR) against the placement and frontmatter guidelines before opening a PR.

---

## Local Development (Optional)

To preview your changes locally using Docusaurus:

1.  Navigate to the `docs-site` directory:
    ```bash
    cd docs-site
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the development server:
    ```bash
    npm run start
    ```
    The site will be available at `http://localhost:3000`.

## Style Guidelines

*   **Markdown:** Use standard GitHub Flavored Markdown.
*   **Images:** Place images in `docs-site/static/img/` and reference them accordingly.
*   **Tone:** Maintain a professional, helpful, and concise technical tone.

### FAQ Pages

FAQ pages use the native HTML `<details>` / `<summary>` expand/collapse pattern — the Docusaurus equivalent of the Confluence expand macro. Each question is a `<summary>` and the answer is the body of the `<details>` block.

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

Rules:
*   One `<details>` block per question — do not nest them.
*   Leave a blank line between the `<summary>` closing tag and the answer body, or Markdown inside the block will not render correctly.
*   Group questions under H2 headings by topic (e.g. `## Contracts`, `## Troubleshooting`).
*   Do not use the old grouped-bullet format (`- **Question?** Answer`) for new FAQ pages.

### Admonitions (Callout Panels)

Use Docusaurus admonitions to highlight important information — the equivalent of Confluence's Note, Warning, Tip, and Info panels. They render as styled, colored panels with an icon and label.

**Syntax:**

```md
:::note

Content goes here.

:::
```

**Available types:**

| Type | Color | When to use |
|---|---|---|
| `:::note` | Blue | Neutral supplementary information the reader should be aware of. |
| `:::tip` | Green | Best practices, shortcuts, or helpful suggestions. |
| `:::caution` | Yellow | Restrictions, conditional behavior, or things that may cause confusion if missed. |
| `:::danger` | Red | Actions that can cause data loss, system failure, or irreversible consequences. |

**Example:**

```md
:::caution

- A bot connector that is associated with a Channel **cannot be deleted** until the association is removed.
- The **API URL** field appears only when the Bot Type is **Rasa** or **Custom**.

:::
```

Rules:
*   Choose the type based on content — not preference. Match the severity of the message to the color.
*   Keep admonition content concise. If it exceeds 3–4 bullet points, consider moving the content into the main body.
*   Leave a blank line after the opening `:::type` and before the closing `:::`, or Markdown inside will not render correctly.
*   Do not nest admonitions.
