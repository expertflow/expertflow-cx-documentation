---
title: "topicUnsubscription"
summary: "Emitted by Agent Manager when an agent leaves a conversation, returning a success message upon successful unsubscription."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["topicUnsubscription socket event CX", "topicUnsubscription Agent Manager CX", "Socket.IO CX"]
aliases: ["topicUnsubscription event ExpertFlow", "topicUnsubscription socket CX"]
last-updated: 2026-03-12
---

# topicUnsubscription

Event is triggered when an agent leaves the conversation. Returns a success message in case of success.

| Property | Value |
|---|---|
| **Event Name** | `topicUnsubscription` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `task` | String | Value is `topicUnsubscription` for this event. |
| `conversationId` | String | ID of the conversation that was unsubscribed. |
| `statusCode` | Numeric | Return value `200` in case of successful unsubscription. |
| `roomInfo` | Object | (Optional) Contains `id` (room ID) and `mode` (room mode). |
| `reason` | String | (Optional) Reason for unsubscription. |

## Example Payload

```json
{
    "task": "topicUnsubscription",
    "conversationId": "5d37c884-8495-49fd-b6d3-8ef43fe53dc7",
    "statusCode": 200
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [topicSubscription](./topicSubscription.md)
- [topicClosed](./topicClosed.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
