---
title: "pauseConversation"
summary: "Emitted by Agent Desk when an agent requests to hold or pause the active conversation."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["pauseConversation socket event CX", "pauseConversation Agent Manager CX", "Socket.IO CX"]
aliases: ["pauseConversation event ExpertFlow", "pauseConversation socket CX"]
last-updated: 2026-03-12
---

# pauseConversation

Event is emitted when an agent requests the Agent Manager to hold or pause the conversation.

| Property | Value |
|---|---|
| **Event Name** | `pauseConversation` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `participantId` | String | ID of the agent initiating the hold. |
| `conversationId` | String | ID of the conversation to be paused. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode). |
| `duration` | Timestamp | Duration in seconds for which the conversation can remain on hold. |
| `state` | String | The target state for the conversation. Value: `"ON_HOLD"`. |

## Example Payload

```json
{
  "participantId": "65a63fee6a264c3b8edece8a",
  "conversationId": "65b3acaec94e6061e70a0ef5",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  },
  "duration": "1740715196",
  "state": "ON_HOLD"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [resumeConversation](./resumeConversation.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
