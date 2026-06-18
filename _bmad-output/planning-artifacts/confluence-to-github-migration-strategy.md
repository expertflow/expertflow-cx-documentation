# Confluence to GitHub Migration Strategy
# ExpertFlow CX Documentation

**Date**: 2026-06-18
**Scope**: All ExpertFlow product documentation
**Target**: Single Docusaurus site on GitHub Pages (`https://expertflow.github.io/expertflow-cx-documentation/`)

---

## 1. Current State: docs.expertflow.com

The existing Confluence + Scroll Sites portal is **product-version-centric**:

| Space | Content | Notes |
|---|---|---|
| ExpertFlow CX 5.4.0 | Core platform docs | Version-frozen |
| CX Knowledgebase | Operational/infra hub | Always-current (`/latest/`) |
| Voice Recording 14.8.0 | Add-on | Own version |
| WFM 1.0 | Add-on | Own version |
| CRM Connectors (30+) | ServiceNow, Salesforce, SAP, Dynamics, HubSpot, Zoho… | Flat alphabetical |
| Cisco CC Add-ons (6) | Cisco-specific modules | Separate section |
| Legacy Docs (5) | Campaigns, Surveys, Dashboards | Archived |

**Core problem**: Navigation is product-first. Users pick a product, then hunt for their task inside it. Personas are an afterthought. Content types (tutorial, how-to, explanation, reference) are mixed on the same page.

---

## 2. Framework: Diátaxis Organises Everything

The migration does not preserve either Confluence structure. All content — from both the versioned CX space and the CX Knowledgebase — is sorted through the Diátaxis lens first.

| Diátaxis Type | Reader's need | Maps to |
|---|---|---|
| **Tutorial** | Learning — "take me through it" | `Getting_Started/` |
| **How-to** | Task — "help me do X" | `How-to_Guides/` |
| **Explanation** | Understanding — "help me understand X" | `Capabilities/`, `Solutions/`, `Platform_Overview/` |
| **Reference** | Information — "just give me the spec" | `Reference/` |

**The rule that prevents future conflicts**: a page has one Diátaxis type. If a page contains both task steps and conceptual background, split it into two pages.

**Violation pattern to eliminate**: Confluence pages that are simultaneously a deployment guide, a feature explanation, and a troubleshooting reference. These must be decomposed on migration.

---

## 3. The Merge Conflict Resolved: CX Knowledgebase vs CX Versioned Space

These two Confluence spaces feel like different worlds because they serve different purposes — not because they cover different products.

| | ExpertFlow CX 5.4.0 | CX Knowledgebase |
|---|---|---|
| Nature | Version-frozen product docs | Always-current operational hub |
| Content | Features, UI how-tos, release behaviour | Kubernetes, HA, sizing, GraphQL APIs, governance |
| Update cadence | Locks with each release | Continuous |
| Owner | Product team | Platform/ops/infra team |

**Resolution — sort by Diátaxis type, not by source space:**

| Content | Source space | Diátaxis type | Destination |
|---|---|---|---|
| Kubernetes deployment guide | Knowledgebase | How-to | `How-to_Guides/Platform_Operator/` |
| HA sizing specifications | Knowledgebase | Reference | `Reference/Architecture_and_Infrastructure/` |
| "What is tenant management" | Knowledgebase | Explanation | `Capabilities/` |
| CRM connector setup steps | Knowledgebase | How-to | `How-to_Guides/Administrator/` |
| CRM connector event schemas | CX 5.4.0 | Reference | `Reference/API_and_SDK/` |
| Channel configuration guide | CX 5.4.0 | How-to | `How-to_Guides/Administrator/` |
| Business discovery questionnaire | Knowledgebase | **Not documentation** | Do not migrate |

The source space is irrelevant. The Diátaxis type determines placement.

---

## 4. Single Docs Space Architecture

One Docusaurus site. One GitHub repo. All products.

```
docs/cx/
  Getting_Started/                    ← Tutorial (per persona)
    For_Administrators/
    For_Agents/
    For_Platform_Operators/           ← absorbs Knowledgebase onboarding content
    For_Developers_and_Integrators/
    For_Conversation_Designers/
    For_Supervisors_and_QA_Leads/
    For_Partners/

  Platform_Overview/                  ← Explanation (evaluation/orientation)

  Capabilities/                       ← Explanation (feature understanding)
    Digital_Channels/
    AI_and_Automation/
    Integrations_and_Connectors/
      ServiceNow/                     ← what this connector does (explanation)
      Salesforce/
      …(30+ connectors — one folder each)
    Voice_Recording/                  ← add-on explanation
    Workforce_Management/             ← add-on explanation
    Quality_Management/
    Routing_and_Queue_Management/
    Reporting_and_Analytics/
    Security_and_Compliance/

  How-to_Guides/                      ← How-to (task guides, per persona)
    Administrator/
      Integrations/                   ← connector configuration tasks
    Platform_Operator/                ← absorbs Knowledgebase infra how-tos
    Developer_Integrator/
    Agent/
    Supervisor_and_QA_Lead/
    Conversation_Designer/
    Partner/

  Reference/                          ← Reference (specs, schemas, APIs)
    API_and_SDK/                      ← GraphQL, postMessage events, public APIs
    Architecture_and_Infrastructure/  ← sizing tables, system requirements
    Connector_Specs/                  ← per-connector technical reference
    Schemas_and_Data_Model/
    Glossary/

  Solutions/                          ← Explanation (business outcomes)
    Campaign_Manager/
    Quality_Management/
    Surveys/
    Workforce_Management/
```

**CRM Connectors pattern** (30+ connectors, one template per connector):

```
Capabilities/Integrations_and_Connectors/ServiceNow/
  index.md              ← explanation: what this connector does, compatibility
How-to_Guides/Administrator/Integrations/
  ServiceNow-setup.md   ← how-to: step-by-step configuration
Reference/Connector_Specs/ServiceNow/
  field-mappings.md     ← reference: field mapping tables, event schemas
```

---

## 5. Versioning Strategy

### What to Version — Diátaxis Decides

Not all content types need version snapshots equally:

| Diátaxis type | Version sensitivity | Reason |
|---|---|---|
| **How-to** | High — version these | Steps reference specific UI, menus, config options that change per release |
| **Reference** | High — version these | API specs, schemas, field definitions must be accurate for the version running in production |
| **Tutorial** | Medium — update in-place | Getting started flows change rarely; rewrite rather than archive |
| **Explanation** | Low — update in-place | Conceptual understanding rarely changes with minor releases |

Docusaurus versions the entire docs instance at once — How-to and Reference content gets frozen accurately, while Explanation and Tutorial pages come along for free without added maintenance cost.

### When to Cut a Version Snapshot

Cut a version at every product release that changes **UI behaviour** or **API contracts**. Do not cut a version for Explanation or Tutorial updates.

```bash
npm run docusaurus docs:version 5.4.0
```

### Keeping It Manageable — Avoid Confluence-Style Sprawl

Cap to two live versions: current (in progress) + one prior stable release. Older versions are archived as static HTML, not actively maintained.

```js
// docusaurus.config.js
docs: {
  lastVersion: 'current',
  versions: {
    current: { label: '5.5 (latest)', badge: true },
    '5.4.0': { label: '5.4.0' },
  },
  onlyIncludeVersions: ['current', '5.4.0'],
}
```

### CRM Connectors — Independent Version Clock

Connectors have their own release cadence (e.g., ServiceNow connector v3.2 ≠ CX platform 5.4.0). Use a **separate docs plugin instance** for connectors so their versions are independent of the CX platform version.

```js
// docusaurus.config.js
plugins: [
  // CX Platform — versioned with platform releases
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'cx',
      path: 'docs/cx',
      routeBasePath: 'cx',
      sidebarPath: './sidebars-cx.js',
      versions: {
        current: { label: '5.5 (latest)' },
        '5.4.0': { label: '5.4.0' },
      },
      onlyIncludeVersions: ['current', '5.4.0'],
    },
  ],
  // CRM Connectors — versioned independently
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'connectors',
      path: 'docs/connectors',
      routeBasePath: 'connectors',
      sidebarPath: './sidebars-connectors.js',
    },
  ],
],
```

Both within the same single Docusaurus site and GitHub repo. One deployment pipeline.

---

## 6. Migration Phasing

| Phase | Scope | Status | Notes |
|---|---|---|---|
| **1 — CX Core** | 425 pages, Diátaxis structure | Test complete | Ship to GitHub Pages |
| **2 — Knowledgebase audit** | Classify each KB page by Diátaxis type, place in single-space structure | Not started | Eliminates duplication; highest priority |
| **3 — CRM Connectors** | 30+ connectors using the three-page template | Not started | Large user segment; use template approach |
| **4 — Add-ons** | Voice Recording, WFM, Cisco modules | Not started | Fold into Capabilities/ and How-to_Guides/ |
| **5 — Legacy archive** | Campaigns, Surveys, Dashboards legacy | Not started | Redirect to nearest current equivalent; freeze as static |

---

## 7. What This Delivers Over Confluence

| Problem in Confluence | Resolution in Docusaurus + GitHub |
|---|---|
| Product-first navigation — users hunt for their task | Persona-first → task — users find their role, then their goal |
| Mixed content types on one page | Diátaxis enforcement via `CLAUDE.md` and `Content_Placement_Guide.yaml` |
| No PR review workflow for doc changes | Full GitHub PR flow — every change is reviewable |
| Scroll Sites versioning is paid and proprietary | Docusaurus built-in versioning, free and open |
| Poor search | Algolia DocSearch integration (free for OSS docs) |
| CX 5.4.0 and CX Knowledgebase are duplicate/overlapping spaces | Single unified structure, source-space is irrelevant — Diátaxis type determines placement |
| Connector docs are 30 flat alphabetical pages | Template-driven: explanation + how-to + reference per connector |
| Business strategy content mixed with user docs | Not migrated — does not belong in user-facing documentation |

---

## 8. Immediate Next Actions

1. **Enable Docusaurus versioning** — tag current 425 pages as `5.4.0` before next release cycle
2. **Audit CX Knowledgebase** — classify each page by Diátaxis type, map to destination folder
3. **Design connector template** — three pages per connector (explanation, how-to, reference)
4. **Set up GitHub Actions CI/CD** — auto-deploy to GitHub Pages on merge to `main`
5. **Configure Algolia DocSearch** — apply once the site is live on a public URL
