---
title: "Agent Hand Raise"
summary: "Explanation of the Agent Hand Raise feature in ExpertFlow CX — how agents signal supervisors for help during live conversations, how supervisors respond, and known limitations."

product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["agent hand raise", "agent assistance request", "supervisor whisper", "hand raise CX", "agent help request", "supervisor notification", "whisper mode"]
aliases: ["hand raise feature", "agent signals supervisor", "CX hand raise"]
last-updated: 2026-03-10
---

# Agent Hand Raise

The Hand Raise feature lets agents discreetly request supervisor assistance during a live customer conversation. Supervisors receive a real-time notification and can join the conversation in Whisper mode without the customer's knowledge.

## How an Agent Raises Their Hand

During an active customer conversation, the agent clicks the **Hand Raise** icon in the conversation toolbar. This sends a push notification to the agent's supervisors. The icon can be toggled again to withdraw the request if help is no longer needed.

## How Supervisors Respond

When an agent raises their hand, supervisors assigned to that agent's team receive a notification with two options:

| Action | Description |
|---|---|
| **Join** | Enter the conversation in **Whisper mode** — the agent can hear/see the supervisor, but the customer cannot. |
| **Dismiss** | Remove the notification without joining. |

Notification behaviour:
- Notifications are sent to both **primary and secondary supervisors** of the agent's team.
- If no action is taken, the notification disappears automatically after **30 seconds**.
- A sound alert plays once for multiple simultaneous hand raise requests. The alert stops when all notifications are cleared or dismissed.
- Once a supervisor joins, their notification is cleared. Other supervisors still see the notification until they dismiss it or join.

## Responding from the Supervisor Dashboard

In the **Ongoing Conversations Detail Dashboard**, an alert icon appears next to any conversation where an agent has raised their hand. Supervisors can:
- Click the alert icon to join directly in **Whisper mode**.
- Enter in **Silent Monitoring mode** first and switch to Whisper mode as needed.

Switching to Whisper mode automatically lowers the hand raise request — the icon is removed from the dashboard and the conversation view, indicating the request has been addressed.

## Limitations

- Hand Raise is only available for **digital chat channels** (web chat, messaging). It is not supported over CX Voice because Whisper over voice is not yet implemented.
- The Hand Raise icon is not displayed if a voice session (CX Voice or Cisco CC) is active in the conversation.
- If a voice session starts after an agent has raised their hand, supervisors still see the request but the icon is disabled for the agent.
- If a supervisor has already joined the conversation, new hand raise requests from the same agent are not visible to that supervisor until they leave and re-enter.
- When one supervisor joins, other supervisors' notifications are **not** dismissed — more than one supervisor can join the same conversation simultaneously.

## Related Articles

- [Barge-in and Intervention](../../How-to_Guides/Supervisor_and_QA_Lead/Barge-in-and-Intervention.md)
- [Consult, Transfer, and Conference](Consult-Transfer-Conference.md)
- [Managing Teams and Members](../../How-to_Guides/Supervisor_and_QA_Lead/Managing-Teams-and-Members.md)
