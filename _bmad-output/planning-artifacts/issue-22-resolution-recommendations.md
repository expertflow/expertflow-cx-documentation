# Issue #22 Resolution Recommendations
## Should ExpertFlow Consolidate All Product Docs Into One Site?

**Date:** 2026-06-23
**Status:** Draft — awaiting stakeholder review
**Authors:** Mary (Business Analyst), Paige (Technical Writer)
**Linked:** [PR #20](https://github.com/expertflow/expertflow-cx-documentation/pull/20) · [Issue #22](https://github.com/expertflow/expertflow-cx-documentation/issues/22)
**Reviewer:** @jawadbokhari

---

## 1. Purpose

This is a decision brief — not a strategy document. It directly answers the four questions raised in issue #22 and asks for a single approval so blocked work can move forward. The full migration strategy (authored by @navira-zainab in PR #20) remains intact and is referenced throughout; this document resolves the consensus gate that must precede it.

---

## 2. Background

- PR #20 proposed an org-wide migration strategy: all ExpertFlow Confluence spaces → single Docusaurus site on GitHub Pages, organised by the Diátaxis framework.
- It was parked because the CX Confluence→GitHub migration is already complete, this repo is scoped to CX only, and the PR implicitly made an org-wide strategic decision that had not been ratified.
- Issue #22 was opened as the venue to reach that consensus before forming the strategy.
- This document resolves that consensus gate with four concrete recommendations.

---

## 3. Recommendations

### Q1 — Single org-wide documentation site, or keep per-product spaces?

**Recommendation: Single org-wide Docusaurus site.**

| Signal | Evidence |
|---|---|
| Users cross product boundaries | CRM connectors, add-ons (WFM, Voice Recording, Cisco), and the CX platform are purchased and operated together by the same administrators and platform operators |
| Product-first navigation is the root cause of Confluence's UX failure | Users must already know which product they are in before they can find their task — the anti-pattern the CX migration was designed to eliminate |
| Independent versioning is already solved | The dual-plugin Docusaurus config in PR #20 (`cx` plugin + `connectors` plugin) handles different product release cadences without forcing separate sites |
| CX migration validated the model | 425 pages migrated, Diátaxis structure enforced, `Content_Placement_Guide.yaml` working in production — the framework is proven |

**What this means in practice:** One GitHub repo, one Docusaurus site, one GitHub Pages deployment, one Algolia DocSearch index. Each product area lives under its own path (`/cx/`, `/connectors/`, `/wfm/`) but shares a unified navigation structure and search.

---

### Q2 — Organising principle and ownership?

**Recommendation: Diátaxis-first, persona as secondary axis. Not product-first.**

The key insight from PR #20 stands: the source Confluence space is irrelevant. A Kubernetes deployment guide from the CX Knowledgebase and a channel configuration guide from the versioned CX space both land in `How-to_Guides/Platform_Operator/` — not in separate product silos.

For users who navigate by product (e.g., "I need the WFM docs"), a lightweight `Solutions/` landing page per product provides an entry point that links out to the relevant Capabilities, How-to, and Reference pages. This is orientation, not duplication.

**Ownership model:**

| Layer | Owner | Mechanism |
|---|---|---|
| Infrastructure (repo, GitHub Pages, CI/CD) | Platform / DevOps team | GitHub Actions pipeline |
| Content framework (Diátaxis rules, `Content_Placement_Guide.yaml`, persona model) | CX documentation team | Org-standard governance files already in this repo root |
| Content per product area | Each product team | PRs reviewed against the shared framework |
| Migration project management | Designated docs lead (cross-team) | Tracking issue per phase |

**Governance gap addressed:** When a product team places content in the wrong Diátaxis type, the enforcement mechanism is a CODEOWNERS entry requiring CX docs team approval on any changes to `Content_Placement_Guide.yaml` and `CLAUDE.md`. PRs that violate placement rules are flagged at review, not post-merge.

---

### Q3 — Where does the strategy live?

**Recommendation: Rename this repo to `expertflow/expertflow-docs` and expand its scope. No new repo needed.**

The original recommendation was to create a new repo. That was an overcorrection. The simpler and correct path is to rename this repo — GitHub automatically redirects all existing URLs (GitHub Pages, clone URLs, web URLs) to the new name, so nothing breaks.

The `docs-site/` Docusaurus installation already exists, the governance files are already in place, and the CX content is already live. Expanding scope here avoids a content migration exercise that adds no value.

**Revised repo structure (in-place expansion):**

```
expertflow/expertflow-docs              ← renamed from expertflow-cx-documentation
  docs-site/
    docs/cx/                            ← unchanged — CX content stays exactly here
    docs/connectors/                    ← added: Phase 3 CRM connector content
    docs/wfm/                           ← added: Phase 4 WFM content
    docs/voice-recording/               ← added: Phase 4 Voice Recording content
    docusaurus.config.js                ← extended with dual-plugin config from PR #20
    sidebars-cx.js                      ← renamed from sidebars.js
    sidebars-connectors.js              ← added
  _strategy/
    migration-strategy.md               ← PR #20's document, merged here
    issue-22-resolution.md              ← this document
  CLAUDE.md                             ← scope updated from CX-only to org-wide
  Content_Placement_Guide.yaml          ← scope updated from CX-only to org-wide
  Persona_Model.md                      ← unchanged, already applicable org-wide
```

**URL continuity:** GitHub handles this natively. On repo rename, all existing URLs — `github.com/expertflow/expertflow-cx-documentation`, the GitHub Pages URL, and all clone remotes — automatically redirect to the new name. No manual redirect setup required.

---

### Q4 — Retrofit CX into the new model, or leave it?

**Recommendation: Leave CX exactly where it is. Zero content migration required.**

The CX content at `docs-site/docs/cx/` does not move. The folder structure already matches the architecture in PR #20 — it was designed with CX as a sub-path of a larger site. No Diátaxis re-classification, no link changes, no content rewriting.

**What actually needs doing** (bounded, one-time setup):

| Artifact | Action | Effort |
|---|---|---|
| `docs-site/docs/cx/` | No change — stays exactly where it is | None |
| `docusaurus.config.js` | Extend with dual-plugin config from PR #20 | ~2 hours |
| `sidebars.js` | Rename to `sidebars-cx.js`; add `sidebars-connectors.js` | ~30 minutes |
| `CLAUDE.md` | Update scope language from CX-only to org-wide | ~1 hour |
| `Content_Placement_Guide.yaml` | Update scope language from CX-only to org-wide | ~1 hour |
| `Persona_Model.md` | No change — already applicable org-wide | None |
| Repo rename | GitHub Settings → rename to `expertflow-docs` | ~5 minutes |
| GitHub Actions CI/CD | Set up (not currently configured in this repo) | ~2 hours |

**Total estimated effort: half a day of setup**, before any new product content migration begins. This is significantly less than the originally proposed new-repo approach.

---

## 4. Resolution Steps

| Step | Action | Owner | Prerequisite |
|---|---|---|---|
| 1 | Ratify direction in issue #22 | @jawadbokhari | This document approved |
| 2 | Rename repo to `expertflow-docs` via GitHub Settings | @jawadbokhari | Step 1 |
| 3 | Extend `docusaurus.config.js` with dual-plugin config; rename `sidebars.js` → `sidebars-cx.js` | CX docs team | Step 2 |
| 4 | Update `CLAUDE.md` and `Content_Placement_Guide.yaml` scope from CX-only to org-wide | CX docs team | Step 3 |
| 5 | Add CODEOWNERS file; set up GitHub Actions CI/CD | Platform / DevOps | Step 3 |
| 6 | Re-raise @navira-zainab's strategy doc as `_strategy/migration-strategy.md` in this repo | @navira-zainab | Step 4 |
| 7 | Execute migration phases 2–5 (Knowledgebase → Connectors → Add-ons → Legacy) | Per-product teams against shared framework | Step 6 |

---

## 5. Fallback — If Single Site Is Not Approved

If the org-wide single-site direction is not approved, the per-product alternative is:

- Each product maintains its own Docusaurus repo and GitHub Pages deployment
- `expertflow-cx-documentation` stays as-is — no changes needed
- PR #20's strategy document is archived in issue #22 as a reference, not actioned
- @navira-zainab's connector template pattern (three pages per connector: explanation + how-to + reference) can still be adopted within the CX repo scope

**Trade-offs of the per-product path:**

| Trade-off | Impact |
|---|---|
| No unified search across products | Users searching for connector setup may not find CX how-to guides in the same query |
| Cross-linking between products becomes external links | Fragile — breaks if URLs change; harder to maintain |
| Multiple deployment pipelines | Each team manages their own CI/CD, GitHub Pages, Algolia instance |
| Framework drift | Without a shared `Content_Placement_Guide.yaml`, Diátaxis discipline erodes product-by-product over time |

The single-site path is the stronger recommendation. But if org alignment is not achievable in the near term, the per-product path preserves the CX team's work without loss.

---

## 6. Decision Requested

**@jawadbokhari — one question:**

> Do you approve the single org-wide Docusaurus site direction as described above?

If **yes**: Step 1 is complete. Step 2 (rename this repo to `expertflow-docs`) can begin immediately — it takes five minutes in GitHub Settings.

If **no** or **partial**: please comment with which recommendation(s) need revision and this document will be updated before any implementation work starts.

No migration work begins until this is approved.
