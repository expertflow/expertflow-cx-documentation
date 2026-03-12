---
title: "wrapupTimerStarted"
summary: "Emitted by Agent Manager to start the wrapup timer after a conversation ends."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["wrapupTimerStarted socket event CX", "wrapupTimerStarted Agent Manager CX", "Socket.IO CX"]
aliases: ["wrapupTimerStarted event ExpertFlow", "wrapupTimerStarted socket CX"]
last-updated: 2026-03-12
---

# wrapupTimerStarted

Event is triggered to start the wrapup timer after a conversation concludes.

| Property | Value |
|---|---|
| **Event Name** | `wrapupTimerStarted` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `task` | String | Value is `wrapupTimerStarted` for this event. |
| `duration` | Timestamp | Duration in milliseconds for the wrapup timer. |
| `conversationId` | String | ID of the conversation associated with the wrapup. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode). |
| `statusCode` | Numeric | Return code `200` indicating success. |

## Example Payload

```json
{
  "task": "wrapupTimerStarted",
  "duration": "600000",
  "conversationId": "cc76c196-912d-4a47-a9dd-8a2357f54399",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  },
  "statusCode": 200
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [closeWrapup](./closeWrapup.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
