---
title: "revokeTask"
summary: "Emitted by Agent Manager to revoke a new task request from an agent if it was not accepted within the configured acceptance time."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["revokeTask socket event CX", "revokeTask Agent Manager CX", "Socket.IO CX"]
aliases: ["revokeTask event ExpertFlow", "revokeTask socket CX"]
last-updated: 2026-03-12
---

# revokeTask

Event is triggered to revoke a new task request from the agent if not accepted within the configured accept time.

| Property | Value |
|---|---|
| **Event Name** | `revokeTask` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `conversationId` | String | ID of the conversation whose task request is being revoked. |

## Example Payload

```json
{
    "conversationId": "cc76c196-912d-4a47-a9dd-8a2357f54399"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [taskRequest](./taskRequest.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
