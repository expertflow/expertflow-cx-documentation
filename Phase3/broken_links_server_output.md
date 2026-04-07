# Broken Links — Docusaurus Build Output
Generated: 2026-07-10 | Source: `npm run build` in `docs-site/`
Rescanned: 2026-07-10 | Source: filesystem check against `Restructured/`

---

## Summary

| Category | Count |
|---|---|
| Sitewide layout broken links | 3 |
| Unique missing files (recurring) | 4 |
| Page-specific broken links | 30+ |

**Rescan status:** 2 of 3 sitewide links resolved. 4 of 4 recurring files exist on disk (but some have wrong link paths). Several Category 3 links resolved; remaining broken items noted below.

---

## Category 1: Sitewide Broken Links (layout/navbar — appear on every page)

Fixing these will resolve the majority of the broken link count.

| Status | Broken Target |
|---|---|
| [x] | `/expertflow-cx-documentation/docs/cx/Getting_Started/For_Agents` — `Getting_Started/For_Agents/index.md` exists |
| [x] | `/expertflow-cx-documentation/docs/cx/Getting_Started/For_Administrators` — `Getting_Started/For_Administrators/index.md` exists |
| [ ] | `/expertflow-cx-documentation/docs/cx/Getting_Started/For_Hosting_Partners` — folder and index still missing |

> These paths exist as folders but are missing index pages.

---

## Category 2: Recurring Missing Files (linked from many pages)

| Status | Missing File |
|---|---|
| [x] | `Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `Getting_Started/For_Supervisors_and_QA_Leads/Managing-the-Quality-Assurance-Workflow.md` — file exists |
| [x] | `Getting_Started/For_Supervisors_and_QA_Leads/Evaluator-Guide.md` — file exists |
| [x] | `Platform_Overview/Voice-Recording-and-Compliance-Features.md` — file exists |

---

## Category 3: Page-Specific Broken Links

| Status | Source Page | Broken Link Target |
|---|---|---|
| [ ] | `How-to_Guides/Agent/Consult-Transfer-Conference` | `../Voice_and_Video/CTI-Call-Controls.md` — resolves to `How-to_Guides/Voice_and_Video/` which doesn't exist; file is at `Capabilities/Voice_and_Video/CTI-Call-Controls.md` |
| [x] | `How-to_Guides/Developer_Integrator/LinkedIn-Standard-Tier-Upgrade` | `../Hosting_Partner/LinkedIn-Connector-Deployment.md` — file exists at `How-to_Guides/Platform_Operator/LinkedIn-Connector-Deployment.md`; link path is wrong but file is present |
| [ ] | `How-to_Guides/Partner/Onboarding-a-New-Tenant` | `../For_Administrators/Unified-Admin-Guide.md` — file missing; no `Unified-Admin-Guide.md` found anywhere |
| [ ] | `How-to_Guides/Partner/White-Labeling-the-Interface` | `../../Getting_Started/For_Hosting_Partners/Onboarding-a-New-Tenant.md` — `For_Hosting_Partners/` folder missing entirely |
| [x] | `How-to_Guides/Platform_Operator/Voice-Recording-Components-Deployment` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Managing-the-Quality-Assurance-Workflow.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/AI-Driven-Quality-Management` | `Managing-the-Quality-Assurance-Workflow.md`, `Evaluator-Guide.md` — both files exist in `Getting_Started/For_Supervisors_and_QA_Leads/` |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/As-a-Quality-Manager` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Evaluator-Guide.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/As-a-Supervisor` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Auditing-and-Scoring-Conversations` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Managing-the-Quality-Assurance-Workflow.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Compatibility-Guide-Media-Recording` | `Evaluator-Guide.md`, `Platform_Overview/Voice-Recording-and-Compliance-Features.md` — both files exist |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Designing-Evaluation-Forms` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Managing-the-Quality-Assurance-Workflow.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/EFSwitch-Monitoring-Dashboards` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [ ] | `How-to_Guides/Supervisor_and_QA_Lead/Finding-Conversations-for-Audit` | `/docs/cx/Capabilities/Digital_Channels/Conversation-View` — missing (file is at `Capabilities/Conversation-View.md`, not inside `Digital_Channels/`); `Managing-the-Quality-Assurance-Workflow.md` ✅ exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Force-Logout-Agent` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [ ] | `How-to_Guides/Supervisor_and_QA_Lead/Handle-Voice-Recording` | `Evaluator-Guide.md` ✅ exists; `Conversation-View` — missing at relative path; `Voice-Recording-and-Compliance-Features.md` ✅ exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Managing-Teams-and-Members` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Playing-Screen-Recordings` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Evaluator-Guide.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Realtime-Detailed-Dashboards` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [ ] | `How-to_Guides/Supervisor_and_QA_Lead/Review-Scheduler` | `Managing-the-Quality-Assurance-Workflow.md` ✅ exists; `Workforce-Management-Overview.md` — missing at relative path (file is at `Capabilities/Workforce_Management/Workforce-Management-Overview.md`) |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Summary-Dashboard` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Supervisor-AI-Assistance` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [ ] | `How-to_Guides/Supervisor_and_QA_Lead/Supervisor-Assistance` | `../../Capabilities/Digital_Channels/Agent-Hand-Raise.md` — missing at that path; file is at `How-to_Guides/Agent/Agent-Hand-Raise.md` |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Team-Announcements` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/Team-Stats-Dashboard` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `How-to_Guides/Supervisor_and_QA_Lead/View-Agent-Dashboards` | `../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md` — file exists |
| [x] | `Platform_Overview/Platform-Architecture` | `./cx_architecture.svg` — file exists at `Platform_Overview/cx_architecture.svg` |
| [x] | `Platform_Overview/Security-and-Compliance-Whitepaper` | `Voice-Recording-and-Compliance-Features.md` — file exists at `Platform_Overview/Voice-Recording-and-Compliance-Features.md` |
| [x] | `Reference` (index) | `Agent-Desk-Developer-Guide.md` — file exists at `Reference/API_and_SDK/Agent-Desk-Developer-Guide.md` |
| [ ] | `Reference/Architecture_and_Infrastructure/Hardware-Sizing-Calculator` | `../Administrator/Sizing-Guidelines.md` — resolves to `Reference/Administrator/` which doesn't exist (file is at `How-to_Guides/Administrator/Sizing-Guidelines.md`); `Kubernetes-Distributions.md`, `Helm-Based-Application-Deployment.md`, `CX-Voice-Deployment.md`, `Deployment-of-Mongo-using-ReplicaSet.md` — all files exist but are in `How-to_Guides/Platform_Operator/`, not relative to `Reference/Architecture_and_Infrastructure/` |
| [ ] | `Reference/Dialer-Performance-Benchmarks` | `../Getting_Started/For_Hosting_Partners/Deploying-the-RKE2-Control-Plane.md` — `For_Hosting_Partners/` folder missing; file is at `How-to_Guides/Platform_Operator/Deploying-the-RKE2-Control-Plane.md` |
| [ ] | Homepage (`/`) | `Monitoring-Your-Team-in-Real-Time` ✅ exists; `Managing-the-Quality-Assurance-Workflow` ✅ exists; `Evaluator-Guide` ✅ exists; `Agent-Desk-Developer-Guide` ✅ exists; `Conversation-Studio-Configuration-Guide` ❌ missing (not found anywhere); `Deploying-the-RKE2-Control-Plane` ✅ exists (wrong path in link); `Onboarding-a-New-Tenant` ✅ exists at `How-to_Guides/Partner/` |

---

## Fix Priority

1. **High** — Category 1 sitewide links (3 fixes, eliminates noise across all pages)
2. **High** — Category 2 recurring missing files (4 files, fixes ~20 pages)
3. **Medium** — Category 3 page-specific links (fix individually)
