# Persona Model — Change History & Migration Notes

**Related file:** `Persona_Model.md`

---

## Why the 12-Persona Model Was Replaced

The original model drew vertical role lines (job titles) through horizontal system layers. This caused:

- Overlapping golden paths (e.g., hardware sizing appeared for both CTO and Host)
- Personas that aren't documentation users (Decision Maker / CTO = pre-sales evaluation, not task-based use)
- Real-world role collapse ignored (in most deployments, 1 person covers 2–3 theoretical personas)
- Operational support content (monitoring, upgrades, maintenance) had no persona home

The revised model organises personas around **what people are trying to do**, not org chart titles.

---

## What Happened to the Decision Maker / CTO

The CTO is a **pre-sales evaluation persona**, not a documentation user. They need to assess platform suitability, not complete tasks.

**Resolution:** Removed as a persona entry point. Content moved to the **Platform Overview** top-level nav section. A CTO searching "ExpertFlow security compliance" lands directly on the relevant page — they don't navigate through a persona selector.

---

## Migration Map: 12 Personas → Current Model

| Original Persona | Maps To |
|---|---|
| Agent (Amy) | Cluster 1: Agent |
| Supervisor (Sam) | Cluster 1: Supervisor / QA Lead |
| Human Evaluator (Eva) | Cluster 1: Supervisor / QA Lead |
| Quality Manager (Quentin) | Cluster 1: Supervisor / QA Lead |
| Solution Admin (Olivia) | Cluster 2: Administrator |
| Decision Maker (CTO) | → Platform Overview section (not a persona) |
| Frontend Developer (Dev) | Cluster 3: Developer / Integrator |
| Conversation Designer (Dave) | Cluster 3: Conversation Designer / AI Specialist |
| Integration Specialist (Ian) | Cluster 3: Developer / Integrator |
| AI QA & NLU Specialist | Cluster 3: Conversation Designer / AI Specialist |
| Multi-tenant Partner (Host) | Cluster 2: Platform Operator + Partner |
| Reseller (Cloud) | Cluster 2: Partner |

---

## Archived Files

The following files are superseded and moved to `/archive/`:

- `Final_12_Persona_Model.md` — original 12-persona model
- `Persona_Map.md` — golden paths for the 12-persona model
