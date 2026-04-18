---
title: "Notification Message"
summary: "CIM schema reference for the Notification message type — used to notify system components when CIM events occur, covering event types, required properties, and an example payload."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["notification message CIM", "CIM notification schema", "CIM event notification CX", "channel session notification CX", "agent subscribed notification CIM", "NOTIFICATION type CIM", "typing notification CX"]
aliases: ["notification message CIM", "CIM NOTIFICATION type", "CIM event message CX"]
last-updated: 2026-03-10
---

# Notification Message

The Notification message is sent by the system to notify components within ExpertFlow CX when CIM events are emitted. It is not a customer-facing message but a system-to-component signal.

## Events That Trigger Notification Messages

| Event | Description |
|---|---|
| `SYSTEM_ERROR` | Internal system error notification. |
| `CHANNEL_SESSION_STARTED` | A new channel session has been provisioned by Channel Manager. |
| `CHANNEL_SESSION_EXPIRED` | A channel session expired due to `CUSTOMER_INACTIVITY_TIMEOUT`. |
| `CHANNEL_SESSION_ENDED` | A channel session was deprovisioned by Channel Manager. |
| `AGENT_SUBSCRIBED` | An agent joined a conversation (push or pull mode). |
| `AGENT_UNSUBSCRIBED` | An agent left a conversation. |
| `CONSULT_TRANSFER` | A consult transfer was initiated. |
| `CONSULT_CONFERENCE` | An agent requested another agent to join an active conversation. |
| `DIRECT_TRANSFER` | An agent transferred the conversation to another agent or queue. |
| `NO_AGENT_AVAILABLE` | All agents are busy; no agent could be assigned. |
| `TYPING_STARTED` | Typing indicator — bidirectional between connector and Channel Manager. |
| `TYPING_STOPPED` | Typing indicator — bidirectional between connector and Channel Manager. |
| `AGENT_RESERVED` | An agent has been reserved for the conversation. |

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"NOTIFICATION"` |
| `markdownText` | String | No | Optional plain text accompanying the notification. |
| `notificationType` | Enum | Yes | One of the event values listed in the table above. |

## Example

```json
"body": {
  "type": "NOTIFICATION",
  "markdownText": "Optional",
  "notificationType": "TYPING_STARTED"
}
```

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Delivery Notification Message](Delivery-Notification-Message.md)
- [Message Body](Message-Body.md)
