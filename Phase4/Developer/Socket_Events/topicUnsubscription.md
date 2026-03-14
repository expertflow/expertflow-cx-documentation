---
title: "topicUnsubscription_"
summary: "Emitted by Agent Desk to Agent Manager when an agent requests to unsubscribe from a conversation topic."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["topicUnsubscription_ socket event CX", "topicUnsubscription_ Agent Manager CX", "Socket.IO CX"]
aliases: ["topicUnsubscription_ event ExpertFlow", "topicUnsubscription_ socket CX"]
last-updated: 2026-03-12
---

# topicUnsubscription_

Agent requests the Agent Manager to unsubscribe from a conversation topic by emitting this event.

| Property | Value |
|---|---|
| **Event Name** | `topicUnsubscription` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `conversationId` | String | ID of the conversation to unsubscribe from. |
| `agentId` | String | ID of the agent for whom the event has been emitted. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode). |

## Example Payload

```json
{
    "conversationId": "261c271a-58e6-4571-9d25-77ad26d745d6",
    "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
    "roomInfo": {
      "id": "65a625609487373651365bfb",
      "mode": "CONTACT_CENTER"
    }
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [topicSubscription](./topicSubscription.md)
- [topicUnsubscription](./topicUnsubscription.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
