---
title: "Agent Performance Dashboard Reference"
summary: "Reference guide for Supervisors and Agents to interpret real-time productivity and SLA performance metrics."
audience: [supervisor, agent]
product-area: [reporting, dashboards]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Agent Performance Dashboard Reference

The **Agent Performance Dashboard** provides real-time visibility into your team's productivity and SLA compliance. As a Supervisor (Sam), this is your primary tool for monitoring efficiency and identifying bottlenecks.

## 1. Key Performance Indicators (KPIs)
The dashboard is built around a core set of metrics that define agent success.

| KPI | Description | Business Goal |
| :--- | :--- | :--- |
| **Total Handle Time** | Total time an agent spent on a conversation. | Efficiency tracking. |
| **Talk Time** | Duration spent in chat-based interactions. | Interaction depth. |
| **Total Hold Time** | Time conversations were placed on hold. | Minimize customer wait. |
| **Ready Time** | Time spent available for new tasks. | Capacity monitoring. |
| **Not Ready Time** | Time spent on breaks, meetings, etc. | Adherence tracking. |
| **Answered Conversations** | Total number of successful interactions. | Volume tracking. |
| **RONA (Ring No Answer)** | Offered tasks that the agent failed to accept. | Identify missing agents. |
| **SLA Breach** | Conversations not answered within the SLA limit. | Compliance tracking. |
| **Occupancy %** | % of logged-in time spent handling tasks. | Resource optimization. |

## 2. Real-Time Status Monitoring
The dashboard displays the current state of every agent in your team.
- **Active Agents:** Currently in a conversation.
- **Ready Agents:** Available for assignment.
- **Not Ready Agents:** Inactive for a specific reason (requires Reason Code).

### Why use this dashboard?
1. **Identify Bottlenecks:** If your "SLA Breach" count is high, you may need to move more agents into the "Ready" state.
2. **Monitor RONA:** High RONA counts indicate that agents are leaving their desks without setting themselves to "Not Ready."
3. **Coaching Opportunity:** Look at the "Handle Time" and "Occupancy %" to find high-performers and those who may need additional training.

---

*For detailed data on long-term trends, check the [Historical Reports Reference](Historical-Reports-Reference.md).*
