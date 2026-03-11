---
title: "Silent Monitoring"
summary: "How-to guide for supervisors using Silent Monitoring in ExpertFlow CX — how to join an ongoing conversation invisibly, send whisper messages to agents, escalate to barge-in, and known limitations."
audience: [supervisor]
product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["silent monitoring", "supervisor monitoring", "monitor agent conversation", "whisper message supervisor", "barge-in monitoring", "ongoing conversation monitoring", "CX supervisor tools"]
aliases: ["supervisor silent monitor", "monitor agent chat", "CX monitor conversation"]
last-updated: 2026-03-10
---

# Silent Monitoring

Silent Monitoring lets supervisors join an ongoing customer-agent conversation invisibly. The supervisor can observe the interaction in real time and send whisper messages to the agent — without the customer being aware of the supervisor's presence.

## Prerequisites

- The supervisor must be assigned to a team in Keycloak, with their name included in the group attributes for that team.

## How to Silently Monitor a Conversation

1. Navigate to the **Ongoing Conversations Detail** dashboard from the Supervisor interface.
2. The dashboard displays all active conversations and their channel sessions.
3. Locate the conversation to monitor.
4. Click the **Monitor** icon (eye icon) next to the conversation.
5. The supervisor joins the conversation as a Silent Monitor.

In the **Conversation View**, active conversations are listed on the left-hand side. Monitored conversations are distinguished by an **eye icon** in the conversation list and dashboard.

## What Supervisors Can Do During Monitoring

| Action | Available |
|---|---|
| View the full conversation in real time | Yes |
| Send a **Whisper message** to the agent | Yes (chat only) |
| **Barge in** to the conversation | Yes (chat only — from the Barge-in button) |
| Leave the conversation | Yes |
| Send a message directly to the customer | No |
| Transfer the conversation | No |
| Start a conference | No |

## Escalating to Barge-in

While in Silent Monitoring mode, supervisors can escalate their involvement at any time:
- Click the **Barge-in** button in the Conversation View to switch from Silent Monitor to an active participant who can message the customer directly.

See [Barge-in and Intervention](Barge-in-and-Intervention.md) for full details on barge-in mode.

## Notes

- When the **primary agent leaves** a conversation, the silent monitor is automatically removed from the conversation.
- The monitored conversation's status is shown in the Ongoing Conversations Detail dashboard with a monitoring indicator.

## Limitations

- Only **one Silent Monitor supervisor** can monitor a given conversation at any time.
- If Silent Monitoring is active on a chat session and a CX Voice session becomes active in the same conversation, Silent Monitoring is limited to the chat channel only.
- Keycloak role changes require the supervisor (and affected agents) to **re-login** before the changes take effect.
- The **Whisper** option is available for **chat only** — not for voice sessions.
- Silent Monitoring does not work when **Outbound**, **Direct Named Agent Transfer**, or **Consult Transfer** are in progress due to technical constraints.
- If Agent A places a Named Agent Consult request and Agent B accepts, the Ongoing Conversations Detail dashboard does not display Agent B's name for the supervisor.
- If the customer or agent ends a call while the supervisor is initiating silent monitoring, the call may remain visible on the CTI toolbar; clicking End displays an "_invalid action releaseCall_" error.

## Related Articles

- [Barge-in and Intervention](Barge-in-and-Intervention.md)
- [Agent Hand Raise](../Functional_Areas/Digital_Channel_Management/Agent-Hand-Raise.md)
- [Monitoring Your Team in Real Time](Monitoring-Your-Team-in-Real-Time.md)
