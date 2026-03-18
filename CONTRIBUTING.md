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
