---
title: "Agent Availability Report"
summary: "Reference for the Agent Availability Report in ExpertFlow CX — detailing all report columns, state duration metrics, availability percentage calculation, and available filters."
audience: [supervisor, solution-admin]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["agent availability report", "MRD availability", "agent ready duration", "agent not-ready duration", "agent logged-in duration", "availability percentage", "agent state report", "CX reporting"]
aliases: ["availability report", "agent MRD availability", "agent state duration report"]
last-updated: 2026-03-10
---

# Agent Availability Report

The Agent Availability Report provides MRD-wise availability statistics for each agent across a selected time period. It helps supervisors identify which agents are spending adequate time in a ready state and take corrective action to improve contact center performance.

## Report Columns

| Column | Description |
|---|---|
| **Date** | The date for the reported interval. |
| **Agent Name** | Full name of the agent. |
| **Agent Extension** | The agent's assigned extension number. |
| **MRD Name** | The Media Routing Domain the agent is assigned to (e.g., Chat MRD, Voice MRD). Each agent-MRD combination appears as a separate row. |
| **Logged-in Duration** | Total time the agent was logged in to this MRD. Format: `HH:MM:SS`. |
| **NOT-Ready Duration** | Total time the agent spent in NOT_READY state on this MRD. Format: `HH:MM:SS`. |
| **Ready Duration** | Total time the agent spent in READY state on this MRD. Format: `HH:MM:SS`. |
| **Active Duration** | Total time the agent spent in ACTIVE state (handling a conversation) on this MRD. Format: `HH:MM:SS`. |
| **Busy Duration** | Total time the agent spent in BUSY state on this MRD. Format: `HH:MM:SS`. |
| **PENDING_NOT_READY Duration** | Total time the agent spent in PENDING_NOT_READY state on this MRD. Format: `HH:MM:SS`. |
| **Total Talk Duration** | Combined time in ACTIVE + BUSY states. Format: `HH:MM:SS`. |
| **Availability %** | Percentage of logged-in time the agent was available/ready. Calculated as: `(Ready Duration + Active Duration) / Logged-in Duration × 100`. |

## Report Filters

| Filter | Description |
|---|---|
| **Date/Time** | Filter data for a specific date or date range. |
| **Agent** | Filter to see MRD-wise statistics for a selected agent. |
| **MRD** | Filter by a single MRD or view all MRDs. |

## Understanding Agent States

| State | Meaning |
|---|---|
| **READY** | Agent is available and waiting for interactions. |
| **ACTIVE** | Agent is handling an active conversation. |
| **BUSY** | Agent is on a call (voice) or handling a high-priority task. |
| **NOT_READY** | Agent has set themselves unavailable with a not-ready reason. |
| **PENDING_NOT_READY** | Agent's current conversation is finishing; they will move to NOT_READY when it ends. |

## How to Read the Report

- **Availability %** is the primary KPI. A high availability percentage indicates the agent was ready and accessible for most of their logged-in time.
- Agents with a high **NOT-Ready Duration** relative to logged-in time may require coaching or workload review.
- The report is **MRD-specific** — an agent active on Voice MRD but not-ready on Chat MRD will show separately for each.

## Data Freshness

This is a historical report. Data updates after conversations are closed and processed by the ETL pipeline (default: every 5 minutes). Active conversations are not reflected until finalized.

## Related Articles

- [Reports and Analytics](Reports-and-Analytics.md)
- [Key Reporting Metrics](Key-Reporting-Metrics.md)
- [Presence and Availability Reports](../../Supervisor/Presence-and-Availability-Reports.md)
- [Agent MRD States Reference](../../Agent/Agent-MRD-States-Reference.md)
