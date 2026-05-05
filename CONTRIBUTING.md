# Contributing to Expertflow CX Documentation

Welcome! We're glad you're here. This guide will help you understand our simple workflow for contributing to the documentation.

## GitHub Flow

We follow the [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) model. It's a simple, branch-based workflow that supports teams and projects where deployments happen regularly.

### 1. Create a Branch

Always create a new branch from `main` for your work. Use a descriptive name that reflects your changes:

```bash
git checkout -b docs/update-agent-guide
```

*   `docs/` prefix for documentation updates.
*   `fix/` prefix for correcting errors.
*   `feature/` prefix for new sections or architectural changes.

### 2. Make Your Changes

Make your edits to the markdown files. Most of the active documentation is located in:
*   `Phase4/`: The structured documentation content.
*   `docs-site/`: The Docusaurus configuration and site structure.

### 3. Commit and Push

Commit your changes with clear, concise messages:

```bash
git add .
git commit -m "docs: add detailed agent desk setup steps"
git push origin docs/update-agent-guide
```

### 4. Open a Pull Request

Go to the GitHub repository and open a **Pull Request (PR)** from your branch to `main`.
*   Provide a clear description of what changed and why.
*   Link any relevant issues.
*   The deployment workflow will automatically build your changes upon merge.

### 5. Review and Merge

Wait for feedback or approval from other collaborators. Once approved, your PR will be merged into `main`, and the documentation site will be updated automatically.

---

## Local Development (Optional)

If you want to preview your changes locally using Docusaurus:

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
