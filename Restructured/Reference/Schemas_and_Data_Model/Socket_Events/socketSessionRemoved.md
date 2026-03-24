---
title: "socketSessionRemoved"
summary: "Emitted by Agent Manager when an agent switches to another tab, triggering automatic logout from the previous session."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["socketSessionRemoved socket event CX", "socketSessionRemoved Agent Manager CX", "Socket.IO CX"]
aliases: ["socketSessionRemoved event ExpertFlow", "socketSessionRemoved socket CX"]
last-updated: 2026-03-12
---

# socketSessionRemoved

Event is triggered when an agent switches to another tab. The Agent Desk listens to the event and removes the agent from the previous session, automatically logging them out.

| Property | Value |
|---|---|
| **Event Name** | `socketSessionRemoved` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `agentId` | String | ID of the agent whose previous socket session has been removed. |

## Example Payload

```json
{
    "agentId": "cc76c196-912d-4a47-a9dd-8a2357f54399"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
