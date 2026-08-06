# ExpertFlow CX Documentation — Style Guide

**Maintained alongside:** `AGENTS.md` (placement, frontmatter, and content rules) · `Phase3/Content_Placement_Guide.yaml` · `Phase3/Persona_Model.md`

This is a standalone reference for writing style and formatting patterns, meant to be passed as context to any AI agent or skill preparing feature documentation without pulling in unrelated project setup instructions. For placement, frontmatter, and persona rules, see `AGENTS.md` and `Phase3/Content_Placement_Guide.yaml` — those are canonical and not restated here.

---

## Tone and Writing Style

- **Professional, helpful, and concise.** Write for a technical audience who needs to act, not be impressed.
- **Task-first.** Lead with what the reader needs to do or know, not with background history.
- **Active voice.** "Click Save" not "The Save button should be clicked."
- **Second person.** Address the reader as "you."
- **No marketing language.** Avoid superlatives ("powerful", "seamless", "world-class"). Describe what the platform does, not how great it is.
- **Format:** Standard GitHub Flavored Markdown.
- **Images:** Place in `docs-site/static/img/` and reference with a relative path.

---

## Formatting Patterns

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

- Choose the type based on content severity, not preference.
- Keep admonition content concise. If it exceeds 3-4 bullet points, move the content into the main body.
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

- One `<details>` block per question, do not nest them.
- Leave a blank line between the `<summary>` closing tag and the answer body, or Markdown inside the block will not render correctly.
- Group questions under H2 headings by topic (e.g. `## Contracts`, `## Troubleshooting`).
- Do not use the old grouped-bullet format (`- **Question?** Answer`) for new FAQ pages.
