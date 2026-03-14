---
title: "Realtime Detailed Dashboards"
summary: "Reference for the ExpertFlow CX realtime detailed dashboards — covering Queued Conversations Detail, Ongoing Conversations Detail, My Past Conversations, and Available Agents Detail dashboards with all columns, filters, and known limitations."
audience: [supervisor, agent]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["realtime dashboards CX", "ongoing conversations dashboard", "queued conversations dashboard", "available agents dashboard", "my past conversations", "supervisor real-time view", "agent state dashboard", "CX detailed dashboards"]
aliases: ["detailed dashboards CX", "realtime supervisor dashboards", "ongoing conversation dashboard", "agent detail dashboard"]
last-updated: 2026-03-10
---

# Realtime Detailed Dashboards

The Detailed Dashboards are embedded in Agent Desk and refresh every **10 seconds**. They display live conversation and agent data in detail — complementing the [Summary Dashboard](Summary-Dashboard.md)'s aggregated statistics.

## Dashboard Overview

| Dashboard | Purpose | Agent Access |
|---|---|---|
| **Queued Conversations Detail** | Conversations currently waiting in a queue | No |
| **Ongoing Conversations Detail** | Conversations active with agents, supervisors, or bots | No |
| **My Past Conversations** | Agent's own recently handled conversations | Yes (own conversations only) |
| **Available Agents Detail** | Agent list with state and active conversation count | Yes (own team only) |

## Saved Filters

Filter selections are shared across all detailed dashboards. Selecting Team A and Queue B on the Queued Conversations dashboard automatically applies those filters when you navigate to the Ongoing Conversations or Available Agents dashboards.

- Saved filters are stored in the browser cache.
- Selecting "All Teams" in the Available Agents Detail dashboard does **not** save that filter across other dashboards.
- If dashboards or filters get stuck, wait a few seconds and refresh.

---

## Queued Conversations Detail

Lists all conversations currently enqueued and waiting to be assigned to an agent.

### Filters

Select **Team** first, then **Queue(s)**.

### Columns

| Column | Description |
|---|---|
| **Customer** | Customer name (if identified), channel identifier, and channel type icon. |
| **Waiting Since** | Time the conversation has been queued (shown as "X minutes ago"). |
| **Queue Name** | Queue where the conversation is waiting. |

### Notes

- Shows all queues in the selected team when no specific queue is chosen.
- Agents cannot access this dashboard.
- Queue association changes take effect on agent's next login, not in real time.

---

## Ongoing Conversations Detail

Lists all inbound conversations currently active with agents, supervisors, or bots.

### Filters

| Filter | Description |
|---|---|
| **Answered by** | Toggle between **Agents** (default) and **Bots** to see agent-handled or bot-handled conversations. |
| **Team** | Filter by supervisor's team. |
| **Queue(s)** | Filter by one or multiple queues associated with the team. |

For supervisors: **Primary supervisors** see all agents in their team by default. **Secondary supervisors** see only their assigned agents by default, with an option to view other secondary supervisor agents or all team agents.

### Columns

| Column | Description |
|---|---|
| **Direction** | Inbound or Outbound. |
| **Channel** | Channel through which the customer initiated the conversation (WhatsApp, Facebook, Webchat, etc.). |
| **Customer** | Name (if identified) and channel identity. |
| **Active Since** | Time since the conversation became active (shown as "X minutes ago"). |
| **Agent** | Agent name and username. |
| **Queue Name** | Queue the conversation was routed through. |

### Notes and Limitations

- Only **inbound** conversations appear on this dashboard — outbound conversations are not shown.
- On-hold conversations appear with an **on-hold** status.
- A conversation active with multiple agents from **different queues** shows as two rows; from the **same queue**, as one row.
- Conversations with agents not in the supervisor's team are not visible.
- After a **consult transfer**, the new primary agent's conversation does not appear on this dashboard.
- After a **direct named agent transfer**, the conversation disappears from the dashboard.
- Agents cannot access this dashboard.

---

## My Past Conversations

Available from **CX 4.10.5** and **CX 5.1** onwards.

Displays an agent's recently handled conversations so they can reopen interactions for follow-up, deferred replies, and re-engagement on email and digital channels.

**Agents see only their own past conversations.**

### Columns

| Column | Description |
|---|---|
| **Customer Name** | The customer in the past conversation. |
| **Channel** | Communication channel (Email, Chat, WhatsApp, etc.). |
| **Conversation End Time** | When the conversation was closed. |
| **Action** | Opens the interaction history and enables sending a follow-up message if needed. |

### Filters

| Filter | Description |
|---|---|
| **Search by customer name** | Find a specific customer's conversation. |
| **Channel filter** | Filter by one or more channels. |
| **Time filter** | Default: Last 24 hours. Options: Last 3 days, Last 7 days. |

### Sorting and Pagination

- Conversations are sorted by most recent activity (newest first).
- 25 conversations per page with pagination controls.

---

## Available Agents Detail

Displays all team agents with their current state and active conversation count. Supervisors can change an agent's global state or force-log them out from this dashboard.

### Filters

| Filter | Description |
|---|---|
| **Search Agent** | Find a specific agent by name. |
| **Team** | Filter by team. |

### Columns

| Column | Description |
|---|---|
| **Agent** | Agent name and current global state (Ready, Not Ready). |
| **Active Conversations** | Number of conversations currently active with this agent. |
| **MRD State** | Agent's state per MRD, shown as colored circles. |

### State Change Actions

Supervisors can change an agent's **global** state (not per-MRD) from this dashboard:

| Current State | Available Action |
|---|---|
| Not Ready | Change to **Ready** |
| Any state | **Force Log Out** |

See [Force Logout Agent](Force-Logout-Agent.md) for the full impact of forced logout by state.

### Notes and Limitations

- Agents can access this dashboard but see only their own team's states.
- Primary supervisors see all team agents; secondary supervisors see only their assigned agents by default.
- The **Reserved** MRD state is not currently shown — the Logout option appears even for Reserved agents.
- Team membership changes in Keycloak take effect on agent's next login.

---

## Related Articles

- [Summary Dashboard](Summary-Dashboard.md)
- [Team Stats Dashboard](Team-Stats-Dashboard.md)
- [Silent Monitoring](Silent-Monitoring.md)
- [Force Logout Agent](Force-Logout-Agent.md)
- [Monitoring Your Team in Real Time](../Getting_Started/Monitoring-Your-Team-in-Real-Time.md)
