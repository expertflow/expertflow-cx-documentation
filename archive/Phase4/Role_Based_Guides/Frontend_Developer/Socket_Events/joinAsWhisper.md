---
title: "joinAsWhisper"
summary: "Emitted by Agent Desk when a supervisor requests to whisper into an active conversation rather than being a silent monitor."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["joinAsWhisper socket event CX", "joinAsWhisper Agent Manager CX", "Socket.IO CX"]
aliases: ["joinAsWhisper event ExpertFlow", "joinAsWhisper socket CX"]
last-updated: 2026-03-12
---

# joinAsWhisper

Event is emitted when a supervisor requests the Agent Manager to whisper into an active conversation instead of being a silent monitor.

| Property | Value |
|---|---|
| **Event Name** | `joinAsWhisper` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `participantId` | String | ID of the supervisor for whom the event has been emitted. |
| `conversationId` | String | ID of the conversation for whom the event has been emitted. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode, e.g., `CONTACT_CENTER`). |

## Example Payload

```json
{
  "participantId": "65a63fee6a264c3b8edece8a",
  "conversationId": "65b3acaec94e6061e70a0ef5",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  }
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [JoinAsSilentMonitor](./JoinAsSilentMonitor.md)
- [JoinAsBargeIn](./JoinAsBargeIn.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
