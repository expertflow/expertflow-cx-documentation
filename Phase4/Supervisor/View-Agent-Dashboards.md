---
title: "View Agent Dashboards"
summary: "Reference for the dashboards available to agents in ExpertFlow CX Agent Desk — covering the Summary Dashboard (queue-scoped view) and the Available Agents Detail dashboard, including theme synchronization behavior."
audience: [agent, supervisor]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["agent dashboard CX", "summary dashboard agent", "available agents detail agent", "agent desk dashboard CX", "queue stats agent CX", "agent team dashboard CX", "agent dashboard theme CX"]
aliases: ["agent dashboard view CX", "agent summary dashboard CX", "agent desk dashboards CX"]
last-updated: 2026-03-10
---

# View Agent Dashboards

The real-time dashboards embedded in Agent Desk provide agents with live statistics on queues and team activity. Agents see a scoped version of the same dashboards available to supervisors.

**Agents have access to two dashboards:**

1. **Summary Dashboard** — queue statistics for the queues the agent belongs to
2. **Available Agents Detail** — state and conversation count for all agents in the agent's team

---

## Summary Dashboard

After login, the **Summary Dashboard** is the first screen displayed.

**What agents see:**

| Panel | Scope |
|---|---|
| **Queue Stats** | Statistics for queues the agent is a member of only |
| **Queue Summary Stats** | Per-queue breakdown for the agent's queues only |

Agents do not see the Agent States panel, Bot Stats panel, or any other panels visible to supervisors.

To select which queue data to display, select one or multiple queues from the **Queues** dropdown at the top of the dashboard.

---

## Available Agents Detail

This dashboard shows the current state and active conversation count for all agents in the agent's own team.

**What agents see:**
- All agents in their team
- Each agent's current global state and MRD state(s)
- Number of active conversations per agent

> Agents can view their team's data only. They cannot see agents from other teams.

---

## Theme Synchronization

The Summary Dashboard theme stays in sync with Agent Desk:

| Trigger | Behavior |
|---|---|
| Theme changed on any Agent Desk screen | Summary Dashboard adopts the new theme when next opened |
| Theme changed while on the Summary Dashboard | Dashboard reloads immediately with the updated theme |
| Logout while using dark theme | Dark theme is restored on next login for both Agent Desk and the Summary Dashboard |

---

## Related Articles

- [Summary Dashboard](Summary-Dashboard.md)
- [Realtime Detailed Dashboards](Realtime-Detailed-Dashboards.md)
- [Impact of Team Structure on Dashboards](Impact-of-Team-Structure-on-Dashboards.md)
- [Monitoring Your Team in Real Time](Monitoring-Your-Team-in-Real-Time.md)
