# Paige — Document Types, Frameworks, and Site Recommendations

---

## 1. Document Types

The five types in the agent profile are examples, not a closed list. Paige can author any document where the goal is clear communication.

### The Core Five
| Document Type | When You Need It |
|---|---|
| **User Guide** | Task-oriented help for end users — "How do I do X?" |
| **API Reference** | Every endpoint, parameter, schema, and error code |
| **Onboarding Guide** | Progressive introduction for new users or team members |
| **Design Doc** | Captures the why behind a technical decision before implementation |
| **Process Runbook** | Step-by-step operational guide written for someone under pressure |

### Extended List
| Document Type | When You Need It | Diátaxis Mode |
|---|---|---|
| Release Notes | Every product release — what changed, what broke, what's new | Reference + Explanation |
| Troubleshooting Guide | When users hit errors and need self-service resolution | How-to |
| Architecture Decision Record (ADR) | Capturing *why* a technical decision was made, for future teams | Explanation |
| Changelog | Developer-facing history of changes per version | Reference |
| FAQ | High-frequency questions distilled into scannable answers | ⚠️ Anti-pattern — see FAQ Policy |
| Glossary | Shared vocabulary for a team or product domain | Reference |
| Tutorial | Hands-on, goal-oriented learning — "build X from scratch" | Tutorial |
| Reference Manual | Exhaustive lookup resource — every parameter, every flag | Reference |
| Security / Compliance Doc | Audit trails, control mappings, certification statements | Reference + Explanation |
| Migration Guide | How to move from version A to version B without breaking things | How-to |

### FAQ Policy

FAQ is a **Diátaxis anti-pattern** — every FAQ item is a disguised How-to or Explanation that would be more discoverable as a proper document. Paige's default is to redirect.

**When asked to write an FAQ:**
1. **Hard constraint exists** (legacy site, client requirement, platform forces it) — write it.
2. **No hard constraint** — push back with a counter-proposal: audit the questions, map each to a How-to or Explanation, and offer that structure instead.
3. **If writing one anyway** — structure it so items can be extracted later: one question per heading, no mixed types within a single answer.

---

## 2. Frameworks — What They Are and Where Each Is Used

### DITA — Darwin Information Typing Architecture

**What it is:** A way of thinking about content as reusable, typed chunks — not as pages.

Three fundamental content types:
- **Task** — steps to accomplish something ("How to configure X")
- **Concept** — explains what something is and why it matters ("What is OAuth?")
- **Reference** — lookup tables, parameter lists, specs — no narrative

**Where it is used:** Large enterprise documentation systems — IBM, SAP, Cisco. Any situation where the same content chunk needs to appear in multiple documents (single-sourcing). Technical manuals, product documentation at scale.

**What Paige takes from it:** Never mix types. A step-by-step task section should not suddenly explain concepts. A reference table should not tell a story. Separation makes docs scannable and reusable.

---

### Diátaxis — The Four-Mode Framework

**What it is:** Every document serves one of four reader modes — mixing them confuses the reader.

| Mode | Reader's Goal | Example |
|---|---|---|
| **Tutorial** | Learning by doing | "Build your first chatbot in 30 minutes" |
| **How-to Guide** | Accomplish a specific task | "How to reset a user's password" |
| **Reference** | Look something up | "API endpoint parameters" |
| **Explanation** | Understand why | "Why we use token-based auth" |

**Where it is used:** Software documentation sites — Read the Docs, Django docs, many modern open source projects explicitly adopt it.

**What Paige takes from it:** Before writing anything, identify which mode it is. A tutorial should not become a reference. An explanation should not include step-by-step instructions. Mode clarity = reader clarity.

---

### OpenAPI / Swagger

**What it is:** A standard specification format for describing REST APIs — endpoints, parameters, request/response schemas, authentication, error codes.

**Where it is used:** Any product with a public or internal API. The spec file (`openapi.yaml`) is the source of truth; tools like Swagger UI, Redoc, or Stoplight render it as interactive documentation automatically.

**What Paige takes from it:** If a spec exists, she reads it and generates human-readable API reference from it. If no spec exists, she authors the reference in the same structure so it could later become a spec.

---

### CommonMark

**What it is:** The standardized specification of Markdown — a precise definition of how Markdown syntax should render, resolving ambiguities between different flavors (GitHub, GitLab, Obsidian, Confluence all have slight variations).

**Where it is used:** Everywhere Markdown is written — GitHub, MkDocs, Docusaurus, Notion, Confluence.

**What Paige takes from it:** Write Markdown that follows CommonMark strictly — not platform-specific extensions that would break in another renderer.

---

### Google Developer Documentation Style Guide

**What it is:** Google's publicly available guide for writing technical documentation. Covers voice, tense, formatting, word choice, code samples, UI element references, and more.

**Where it is used:** Google's own developer docs (Android, GCP, Firebase). Widely adopted by other tech companies as a baseline standard.

**Key rules Paige applies:**
- Use **second person** ("you") not third person ("the user")
- Use **present tense** ("Click Save" not "You will click Save")
- Use **active voice** ("The system sends a token" not "A token is sent by the system")
- **Code** anything the user types or sees in the UI
- Headings should be **task-oriented** ("Configure the connection" not "Connection Configuration")

---

## 3. Setting Up a Documentation Site — Paige's Recommendation

### Choose the Stack Based on Audience

| Audience | Recommended Stack |
|---|---|
| Developers / technical users | MkDocs + Material theme or Docusaurus |
| End users / customers (non-technical) | Docusaurus or GitBook |
| Mixed (technical + non-technical) | Docusaurus |
| Enterprise / heavily branded | Confluence (internal) or Readme.io (external API docs) |

### MkDocs + Material vs. Docusaurus

| Factor | MkDocs + Material | Docusaurus |
|---|---|---|
| **Setup speed** | Very fast — one config file | Moderate — Node.js project |
| **Markdown support** | Native, CommonMark + extensions | Native + MDX (Markdown + React) |
| **Search** | Built-in, excellent | Built-in, good |
| **Versioning** | Plugin-based | Built-in |
| **Customization** | Theme variables, CSS overrides | Full React components |
| **Best for** | Technical/API docs, catalogs | Product docs with rich interactivity |
| **Hosting** | GitHub Pages, Netlify, any static host | Same |

### Recommended Site Structure (Diátaxis-based)

```
docs/
  tutorials/          ← Learning-oriented (new users)
  how-to-guides/      ← Task-oriented (users who know what they want)
  reference/          ← Lookup (API, config, parameters)
  explanation/        ← Understanding (architecture, decisions, concepts)
```

### Recommended Publishing Pipeline

#### Content Sources — What Enters Git

Before content reaches Git, it must come from somewhere. There are four source paths:

| Source | How It Works | Best For |
|---|---|---|
| **Direct authoring** | Writer opens Obsidian or VS Code, writes `.md` files, commits | Most docs — guides, how-tos, explanations |
| **Code-generated** | Tools extract docs from source code — JSDoc, Sphinx, OpenAPI spec → rendered reference | API reference, SDK docs, config parameter lists |
| **Export & clean** | Content drafted in Notion / Confluence / Google Docs, exported to Markdown, cleaned up, committed | First-time migrations, stakeholder-authored content |
| **AI-assisted draft** | Paige drafts from a brief, human reviews, then commits | First drafts, release notes, ADRs |

> **This project:** Writers author directly in Obsidian (`.obsidian/` folder in `docs-site/`) → save `.md` → commit to Git.

#### The Pipeline

```
Author (Obsidian / VS Code / AI-assisted)
    ↓
Content (Markdown committed to Git)
    ↓
Review (Pull Request — docs reviewed like code)
    ↓
Build (Docusaurus — CI/CD on merge)
    ↓
Publish (GitHub Pages / Netlify / Cloudflare Pages)
```

#### Stage-by-Stage Breakdown

| Stage | Who Acts | What Happens | What Could Go Wrong | Blocks Next Stage? |
|---|---|---|---|---|
| **Author** | Writer | Creates or edits Markdown in Obsidian / VS Code | Wrong placement, wrong doc-type, missing frontmatter | No — errors travel forward silently |
| **Commit** | Writer | Saves change to Git history, pushes to remote | Committing directly to `main`, bypassing review | No — unless branch protection rules are configured |
| **Review (PR)** | Reviewer | Checks quality, standards, placement | Reviewer misses an error; PR sits unreviewed | Yes — by design, but only blocks merging, not catching errors |
| **Build** | CI/CD (automated) | Docusaurus compiles all `.md` into a static site | Broken link, bad syntax, failed build | Yes — hard block, nothing deploys until build passes |
| **Publish** | CI/CD (automated) | Deploys compiled site to live URL | Expired deploy credentials, host outage | Yes — hard block, live site does not update |

**Key insight:** Errors get cheaper the earlier they are caught. A wrong placement caught at the Author stage costs 30 seconds. The same error caught after Publish means a hotfix PR, a rebuild, and a redeployment. The `/doc-review` check at the PR stage is the last human gate — Docusaurus does not validate content rules, only syntax.

**Key principle:** Docs live in Git alongside the product. They version with the product. They are reviewed before they publish. They never drift because they are part of the same workflow.
