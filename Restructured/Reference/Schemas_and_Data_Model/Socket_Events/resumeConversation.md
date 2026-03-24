---
title: "resumeConversation"
summary: "Emitted by Agent Desk when an agent requests to resume a paused or held conversation."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["resumeConversation socket event CX", "resumeConversation Agent Manager CX", "Socket.IO CX"]
aliases: ["resumeConversation event ExpertFlow", "resumeConversation socket CX"]
last-updated: 2026-03-12
---

# resumeConversation

Event is emitted when an agent requests the Agent Manager to resume a paused or held conversation.

| Property | Value |
|---|---|
| **Event Name** | `resumeConversation` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `participantId` | String | ID of the agent initiating the resume. |
| `conversationId` | String | ID of the conversation to be resumed. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode). |
| `state` | String | The target state for the conversation. Value: `"ACTIVE"`. |

## Example Payload

```json
{
  "participantId": "65a63fee6a264c3b8edece8a",
  "conversationId": "65b3acaec94e6061e70a0ef5",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  },
  "state": "ACTIVE"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [pauseConversation](./pauseConversation.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
