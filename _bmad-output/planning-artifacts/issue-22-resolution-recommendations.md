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
| Content framework (Diátaxis rules, `Content_Placement_Guide.yaml`, persona model) | CX documentation team | Org-standard governance files in root of new repo |
| Content per product area | Each product team | PRs reviewed against the shared framework |
| Migration project management | Designated docs lead (cross-team) | Tracking issue per phase |

**Governance gap addressed:** When a product team places content in the wrong Diátaxis type, the enforcement mechanism is a CODEOWNERS entry requiring CX docs team approval on any changes to `Content_Placement_Guide.yaml` and `CLAUDE.md`. PRs that violate placement rules are flagged at review, not post-merge.

---

### Q3 — Where does the strategy live?

**Recommendation: Create a new `expertflow/expertflow-docs` repo. The strategy document moves there.**

The current `expertflow-cx-documentation` repo is correctly scoped to CX. An org-wide strategy document has no business living in it — which is exactly why PR #20 was parked.

**Proposed repo structure:**

```
expertflow/expertflow-docs
  docs/cx/                          ← CX content (ported from current repo)
  docs/connectors/                  ← CRM connector content (Phase 3)
  docs/wfm/                         ← WFM (Phase 4)
  docs/voice-recording/             ← Voice Recording (Phase 4)
  _strategy/
    migration-strategy.md           ← PR #20's document, re-raised here
    issue-22-resolution.md          ← this document
  CLAUDE.md                         ← org-wide content governance
  Content_Placement_Guide.yaml      ← elevated from CX-only to org standard
  Persona_Model.md                  ← elevated from CX-only to org standard
```

**URL continuity:** The existing CX GitHub Pages URL (`expertflow.github.io/expertflow-cx-documentation/`) must not break silently. The plan:

1. The old repo stays live and publicly accessible during the transition (it is not deleted, only eventually archived).
2. A redirect notice is added to the old site's homepage pointing to the new URL.
3. The new repo publishes to a new GitHub Pages URL (e.g., `expertflow.github.io/expertflow-docs/`).
4. Once the new site is stable and indexed, the old repo is archived with a static redirect in place.

SEO note: GitHub Pages does not support HTTP 301 redirects natively. A JavaScript meta-redirect in the old site's `index.html` is the practical option, or a custom domain with redirect rules if a custom domain is in use.

---

### Q4 — Retrofit CX into the new model, or leave it?

**Recommendation: Move CX content as-is. No content rewrite required.**

The CX folder structure (`Getting_Started/`, `Platform_Overview/`, `Capabilities/`, `How-to_Guides/`, `Reference/`, `Solutions/`) already matches the architecture proposed in PR #20. The strategy document's folder tree uses `docs/cx/…` — it was designed with CX as a sub-path of a larger site.

**What the move actually involves** (not zero effort, but bounded):

| Artifact | Action |
|---|---|
| `docs-site/docs/cx/` | Copy to `docs/cx/` in new repo — no content changes |
| `docusaurus.config.js` | Port and extend with dual-plugin config from PR #20 |
| `sidebars.js` | Port as-is; rename to `sidebars-cx.js` |
| `CLAUDE.md` | Port to repo root; update paths to reflect new structure |
| `Content_Placement_Guide.yaml` | Port to repo root; remove CX-specific scope language |
| `Persona_Model.md` | Port to repo root |
| GitHub Actions CI/CD | Recreate in new repo (currently not set up in either repo) |

Estimated effort: 1–2 days of setup work for an engineer familiar with Docusaurus, before any new content migration begins.

---

## 4. Resolution Steps

| Step | Action | Owner | Prerequisite |
|---|---|---|---|
| 1 | Ratify direction in issue #22 | @jawadbokhari | This document approved |
| 2 | Create `expertflow/expertflow-docs` repo | Platform / DevOps | Step 1 |
| 3 | Re-raise @navira-zainab's strategy doc as `_strategy/migration-strategy.md` in new repo | @navira-zainab | Step 2 |
| 4 | Port CX content + all config and governance files to new repo | CX docs team | Step 3 |
| 5 | Add redirect notice to `expertflow-cx-documentation`; archive repo | @jawadbokhari | Step 4 verified live |
| 6 | Execute migration phases 2–5 (Knowledgebase → Connectors → Add-ons → Legacy) | Per-product teams against shared framework | Step 5 |

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

If **yes**: Step 1 is complete. Step 2 (create `expertflow/expertflow-docs`) can begin immediately.

If **no** or **partial**: please comment with which recommendation(s) need revision and this document will be updated before any implementation work starts.

No migration work begins until this is approved.
