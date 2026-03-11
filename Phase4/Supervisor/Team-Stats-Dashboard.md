---
title: "Team Stats Dashboard"
summary: "Reference for the ExpertFlow CX Team Stats Dashboard — an updated summary view covering queue performance, agent and channel state distribution, bot activity metrics, and call volume trends."
audience: [supervisor]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["team stats dashboard", "supervisor team dashboard", "queue performance dashboard", "agent states pie chart", "bot activity dashboard", "abandon rate dashboard", "channel distribution CX", "call trends supervisor"]
aliases: ["team dashboard CX", "team stats supervisor", "CX team performance dashboard"]
last-updated: 2026-03-10
---

# Team Stats Dashboard

The Team Stats Dashboard is an updated Summary Dashboard that provides real-time insights into queue performance, agent states, channel distribution, bot activity, and call volume trends. It helps supervisors and managers track service levels and workload distribution across all channels.

## Dashboard Structure

The dashboard has three main sections:

1. **Queue Stats** — Performance metrics for queues and customer interactions.
2. **Agent & Channel States** — Real-time distribution of agent states and channel types.
3. **Bot Activity & Call Trends** — Bot workload and call volume over time.

---

## Dashboard Filters

| Filter | Description |
|---|---|
| **Team Name** | Select the team to monitor. Drives queue and agent data. |
| **Queue Name** | Filter queue statistics to selected queue(s). Supports multi-select. |
| **MRD Name** | Filter agent state data by Media Routing Domain. |
| **Bot Name** | Filter bot activity to a specific bot. |

---

## Section 1: Queue Stats

### KPI Panels

| Panel | Description |
|---|---|
| **Service Level %** | Percentage of interactions answered within the configured SL threshold. Historical data — updates at ETL interval (default 5 minutes). |
| **Active with Agents** | Live count of conversations currently being handled by agents. |
| **Active with Bots** | Live count of conversations currently being handled by bots. |
| **Abandon Rate** | Percentage of customers who left the queue before being answered. |
| **Answer Wait Time** | Average time customers waited before being answered. Format: `HH:MM:SS`. |
| **Average Handle Time (AHT)** | Average time agents spend handling tasks. Formula: `Total Handled Duration ÷ Total Handled Tasks`. |

### Queue Performance Table

Per-queue breakdown for the selected team:

| Column | Description |
|---|---|
| **Queue Name** | Name of the queue. |
| **Channel** | Channel type associated with this queue. |
| **Total Queued** | Current number of conversations waiting in the queue. |
| **Answered** | Total conversations answered from this queue. |
| **Abandoned** | Total conversations abandoned before being answered. |
| **Service Level %** | SL compliance for this queue. |
| **Avg Wait** | Average waiting time for this queue. |
| **Max Wait** | Maximum waiting time observed in this queue. |

---

## Section 2: Agent & Channel States

### Agent States Pie Chart

Live distribution of agents across MRD states:
- Not Ready
- Ready
- Active
- Busy
- Pending Not Ready

### Channel Category Distribution Pie Chart

Live distribution of active interactions by channel type:
- Chat
- LinkedIn
- Voice
- (and any other configured channels)

---

## Section 3: Bot Activity & Call Trends

### Bot Activity Table

Per-bot metrics:

| Column | Description |
|---|---|
| **Bot Name** | Name of the bot. |
| **Channel** | Channel the bot handles. |
| **Assigned** | Total conversations routed to this bot. |
| **Completed** | Conversations successfully resolved by the bot without escalation. |
| **Escalated to Agent** | Conversations handed off to a human agent. |
| **Avg Response Time** | Average bot response time. |

### Calls Trends Bar Graph

Displays the volume of calls routed to the queue over time — useful for identifying peak periods and managing staffing.

---

## Data Freshness

| Panel Type | Update Frequency |
|---|---|
| Agent active, Bot active, Agent States | **Real time** |
| Service Level, Answer Wait Time, AHT | **Historical** — updates at ETL interval (default: 5 minutes) |

---

## Related Articles

- [Summary Dashboard](Summary-Dashboard.md)
- [Realtime Detailed Dashboards](Realtime-Detailed-Dashboards.md)
- [SLA Calculations](SLA-Calculations.md)
- [Monitoring Your Team in Real Time](Monitoring-Your-Team-in-Real-Time.md)
