---
title: "Agent Interaction Log"
summary: "Detailed historical log of all tasks handled by agents, including task outcomes, alerting duration, and transcripts."
audience: [supervisor-qa]
product-area: [reporting, analytics]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Agent Interaction Log

The **Agent Interaction Log** (Task Detail) provides a complete history of every interaction offered to your team. As a Supervisor (Sam), this is your primary tool for auditing individual agent performance and reviewing customer conversation transcripts.

## 1. Interaction Performance Metrics
Each row in the log represents a specific task assigned to an agent.

| Field | Description | Format |
| :--- | :--- | :--- |
| **Queue Duration** | Time the customer waited in the queue before being reserved. | HH:MM:SS |
| **Alert Duration** | How long the agent's desk "rang" before they accepted. | HH:MM:SS |
| **Talk Time** | The active time spent interacting with the customer. | HH:MM:SS |
| **Wrap-up Duration** | Time the agent spent concluding the task. | HH:MM:SS |
| **Transcript** | A link to the full text of the interaction. | Link |

## 2. Understanding Task Dispositions
The **Disposition** explains the final state of the task assignment.

- **DONE:** The agent successfully completed the task and left the conversation.
- **RONA (Ring No Answer):** The task was offered to the agent, but they failed to accept it within the preconfigured timeout.
- **AGENT_LOGOUT:** The agent signed out while the task was still active.
- **CANCELLED:** The customer left the queue or closed their browser before the agent could accept the task.
- **TRANSFERRED:** The agent moved the task to another team member.

## 3. Reporting Filters
- **Customer Name/ID:** Track all tasks related to a specific customer (including anonymous "Jane Doe" entries).
- **Agent Name:** Audit the daily task log for a specific team member.
- **Queue Name:** Analyze which queues are generating the most RONA or Cancelled dispositions.

---

*For help on managing agent states during these tasks, see [Presence and Availability Reports](Presence-and-Availability-Reports.md).*
