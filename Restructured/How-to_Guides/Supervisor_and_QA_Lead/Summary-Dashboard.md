---
title: "Summary Dashboard"
summary: "Reference for the ExpertFlow CX Summary Dashboard — covering queue stats panels, agent state pie chart, bot stats, dashboard filters, and theme synchronization behaviour."
audience: [supervisor-qa]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["summary dashboard CX", "supervisor dashboard", "queue stats dashboard", "agent states dashboard", "real-time summary", "service level dashboard", "average handle time dashboard", "Grafana CX dashboard"]
aliases: ["CX supervisor dashboard", "queue stats summary", "real-time supervisor view"]
last-updated: 2026-03-10
---

# Summary Dashboard

The Summary Dashboard is the first screen displayed after login. It provides summary statistics of all conversations being queued, active with agents and bots, and the overall distribution of agent states. The dashboard is built in Grafana and refreshes automatically.

## Who Sees What

| Role | View |
|---|---|
| **Supervisor** | Must first select a **Team** from the teams assigned to them. Then select one or more queues from that team. |
| **Agent** | Sees only the **Queues** dropdown with queues they belong to. |

> A supervisor must have at least one team with at least one agent, and the agent must have logged in at least once, before team and queue data is visible on the dashboard.

## Dashboard Filters

Apply filters in this sequence to scope the data displayed:

| Filter | Description |
|---|---|
| **Bot Name** | Filter to conversations currently active with a specific bot. |
| **Team Name** | Selects the team to monitor. Drives which queues appear in the Queues dropdown. |
| **Queue Name** | Filters queue stats to selected queue(s). Supports multi-select. |
| **MRD Name** | Filters agent state data to agents in the selected MRD. |

## Dashboard Panels

The dashboard is organized into three rows.

### Queue Stats Row

| Panel | Description |
|---|---|
| **Service Level %** | Service level of selected queues. Retrieved from the historical database — updates at the ETL interval (default 5 minutes). |
| **Active with Agents** | Number of conversations currently active with agents, filtered by selected queues. Live value. |
| **Average Wait Time** | Average time conversations remain queued before being answered. Format: `HH:MM:SS`. For multiple queues, averaged across selections. |
| **Average Handle Time (AHT)** | Average duration of closed tasks. Calculated as `Total Handled Duration ÷ Total Handled Tasks`. For multiple agents handling the same conversation, durations are summed. For multiple queues, averaged. Format: `HH:MM:SS`. |

### Queue Summary Statistics Table

A tabular list of all queues associated with the selected team, showing:

| Column | Description |
|---|---|
| **Queue Name** | Name of the queue. All queues appear whether or not they have active conversations. |
| **MRD Name** | MRD associated with this queue. |
| **Total Queued** | Number of conversations currently waiting in this queue. |
| **Oldest in Queue** | Longest wait time among currently queued conversations. Format: `HH:MM:SS`. Shows `00:00:00` if queue is empty. |
| **Not Ready** | Agent count in NOT_READY state on this queue's MRD. |
| **Ready** | Agent count in READY state on this queue's MRD. |
| **Active** | Agent count in ACTIVE state on this queue's MRD. |
| **Pending Not Ready** | Agent count in PENDING_NOT_READY state on this queue's MRD. |
| **Busy** | Agent count in BUSY state on this queue's MRD. |

> Service Level, Average Wait Time, and AHT are derived from historical data — they update at the ETL interval, not in real time.

### Agent States Row

A pie chart showing the count of agents in each MRD state (Not Ready, Ready, Active, Busy, Pending Not Ready). Filtered by the **MRD Name** filter.

### Bot Stats Row

Shows the number of active conversations currently being handled by the bot. Filtered by the **Bot Name** filter. A conversation is considered active with the bot until an agent joins it.

## Theme Synchronization

- Changing the Agent Desk theme on any screen automatically applies the same theme to the Summary Dashboard when it is next opened.
- Changing the theme while on the Summary Dashboard causes the dashboard to reload with the updated theme.
- The last-used theme (including dark mode) persists across login sessions.

## Important Notes

- Agent attribute changes or team membership changes in Keycloak take effect upon the **agent's next login** — not in real time on the dashboard.
- If a supervisor is also an agent, they see only teams they **supervise** on the dashboard — not the team they belong to as an agent.

## Related Articles

- [Realtime Detailed Dashboards](Realtime-Detailed-Dashboards.md)
- [Team Stats Dashboard](Team-Stats-Dashboard.md)
- [Monitoring Your Team in Real Time](../../Getting_Started/For_Supervisors_and_QA_Leads/Monitoring-Your-Team-in-Real-Time.md)
- [Key Reporting Metrics](../../Capabilities/Reporting_and_Analytics/Key-Reporting-Metrics.md)
