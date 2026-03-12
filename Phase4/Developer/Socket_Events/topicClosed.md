---
title: "topicClosed"
summary: "Emitted by Agent Manager to notify the agent whenever a conversation topic is closed."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["topicClosed socket event CX", "topicClosed Agent Manager CX", "Socket.IO CX"]
aliases: ["topicClosed event ExpertFlow", "topicClosed socket CX"]
last-updated: 2026-03-12
---

# topicClosed

Event is triggered to notify the agent whenever a topic (conversation) is closed.

| Property | Value |
|---|---|
| **Event Name** | `topicClosed` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `task` | String | Value is `topicClosed` for this event. |
| `conversationId` | String | ID of the conversation that was closed. |
| `statusCode` | Numeric | Return value `200` in case of successful topic closure. |

## Example Payload

```json
{
    "task": "topicClosed",
    "conversationId": "97f460f1-42b5-4970-b77b-0985b17e562c",
    "statusCode": 200
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [topicSubscription](./topicSubscription_2531760.md)
- [topicUnsubscription](./topicUnsubscription_2531762.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
