---
sidebar_position: 1
title: "Monitoring Your Team in Real Time"
summary: "Getting started guide for supervisors — how to use the Summary Dashboard and Detailed Dashboards to monitor queues, agents, and live conversations."
audience: [supervisor-qa]
product-area: [reporting]
doc-type: tutorial
difficulty: beginner
keywords: ["supervisor monitoring", "real-time dashboard", "summary dashboard", "queue stats", "agent states", "silent monitoring", "barge-in"]
aliases: ["supervisor real-time monitoring", "monitor team CX", "supervisor dashboard guide"]
last-updated: 2026-03-27
---

# Monitoring Your Team in Real Time

As a Supervisor, your two primary tools are the **Summary Dashboard** (aggregated stats) and the **Detailed Dashboards** (live conversation and agent lists). This guide walks you through using both.

---

## Step 1: Check Queue Health on the Summary Dashboard

The Summary Dashboard is your first screen after login. It refreshes automatically.

1. Select your **Team Name** from the filter at the top.
2. Select one or more **Queues** to scope the data.
3. Review the key panels:

| Panel | What to look for |
|---|---|
| **Service Level %** | Is the queue meeting its target (e.g., 80/20)? |
| **Average Wait Time** | Are customers waiting too long? |
| **Total Queued** | How many conversations are waiting right now? |
| **Oldest in Queue** | Who has been waiting the longest? |

> Service Level and AHT update at the ETL interval (default 5 minutes) — they are not live values.

→ Full reference: [Summary Dashboard](../../How-to_Guides/Supervisor_and_QA_Lead/Summary-Dashboard.md)

---

## Step 2: Drill Into Live Conversations

Switch to the **Ongoing Conversations Detail** dashboard to see every active interaction.

- Filter by **Team** and **Queue(s)** to narrow the list.
- Toggle **Answered by: Bots** to see bot-handled conversations separately.
- Each row shows the customer, channel, agent, queue, and how long the conversation has been active.

→ Full reference: [Realtime Detailed Dashboards](../../How-to_Guides/Supervisor_and_QA_Lead/Realtime-Detailed-Dashboards.md)

---

## Step 3: Monitor or Intervene in a Conversation

From **Ongoing Conversations Detail**, you can take direct action on any live conversation:

| Action | How |
|---|---|
| **Silent Monitor** | Click the eye icon — observe without the agent or customer knowing |
| **Whisper** | Send a private tip to the agent only (chat channels) |
| **Barge-in** | Join the conversation and speak to the customer directly |

→ Full guide: [Silent Monitoring](../../How-to_Guides/Supervisor_and_QA_Lead/Silent-Monitoring.md)

---

## Step 4: Manage Agent Availability

Open the **Available Agents Detail** dashboard to see every agent's current state.

- Use **Search Agent** to find a specific agent quickly.
- If an agent is stuck in a wrong state, click **Change State → Ready**.
- To remove an agent from the system entirely, use **Force Log Out**.

→ Full guide: [Force Logout Agent](../../How-to_Guides/Supervisor_and_QA_Lead/Force-Logout-Agent.md)

---

## Related Articles

- [Summary Dashboard](../../How-to_Guides/Supervisor_and_QA_Lead/Summary-Dashboard.md)
- [Realtime Detailed Dashboards](../../How-to_Guides/Supervisor_and_QA_Lead/Realtime-Detailed-Dashboards.md)
- [Team Stats Dashboard](../../How-to_Guides/Supervisor_and_QA_Lead/Team-Stats-Dashboard.md)
- [Silent Monitoring](../../How-to_Guides/Supervisor_and_QA_Lead/Silent-Monitoring.md)
- [As a Supervisor](../../How-to_Guides/Supervisor_and_QA_Lead/As-a-Supervisor.md)
