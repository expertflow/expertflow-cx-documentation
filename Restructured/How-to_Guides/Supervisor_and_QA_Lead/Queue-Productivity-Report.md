---
title: "Queue Productivity Report"
summary: "Detailed reference for Supervisors to analyze agent productivity and task outcomes on a per-queue basis."
audience: [supervisor-qa]
product-area: [reporting, analytics]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Queue Productivity Report

The **Queue Productivity Report** provides a granular view of how individual agents are performing within specific queues. As a Supervisor (Sam), you use this to identify which queues are most efficient and where your team may need additional training.

## 1. Key Performance Metrics
This report tracks the entire lifecycle of interactions from the moment they are offered to the agent until they are closed.

### Interaction Outcome Metrics:
- **Offered:** Total tasks the system attempted to assign to the agent.
- **Done:** Tasks successfully handled and closed by the agent.
- **Cancelled:** Tasks where the customer left before the agent could join.
- **RONA (Ring No Answer):** Tasks that the agent failed to accept before the timer expired.
- **Transferred (IN/OUT):** Tasks moved between agents or teams.

### Efficiency & Speed Metrics:
- **Average Handle Duration:** The mean time taken to close a task once answered.
- **Average Wrap-up Duration:** The time spent in the "Wrap-up" state after the interaction ends.
- **Speed of Answer (Min/Max/Avg):** How long the agent's desk rang before they clicked "Accept."

## 2. Report Columns Reference
| Field | Description | Format |
| :--- | :--- | :--- |
| **Agent Name** | The name of the team member. | Text |
| **Queue Name** | The specific queue being analyzed (e.g., "Support-WhatsApp"). | Text |
| **MRD Name** | The media routing domain (e.g., CHAT or VOICE). | Text |
| **Total Handle Duration** | The cumulative time the agent spent handling tasks in this queue. | HH:MM:SS |
| **Total Speed of Answer** | The cumulative time the agent's desk rang across all tasks. | HH:MM:SS |

## 3. Using Filters for Insights
- **Agent Filter:** Compare the performance of two agents in the same queue to identify coaching opportunities.
- **Queue Filter:** See which queues have the highest "RONA" or "Cancelled" counts—this may indicate that the queue is understaffed or that agents are avoiding certain types of interactions.
- **Date Range:** Analyze productivity over a specific day or week to measure the impact of team changes.

---

*For real-time data on agent status, check the [Agent Performance Dashboard Reference](Agent-Performance-Dashboard-Reference.md).*
