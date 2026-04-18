---
title: "agentAssistanceRequestPlaced"
summary: "Emitted by Agent Manager in response to a direct conference or direct transfer request, notifying the agent desk that the request has been placed."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["agentAssistanceRequestPlaced socket event CX", "agentAssistanceRequestPlaced Agent Manager CX", "Socket.IO CX"]
aliases: ["agentAssistanceRequestPlaced event ExpertFlow", "agentAssistanceRequestPlaced socket CX"]
last-updated: 2026-03-12
---

# agentAssistanceRequestPlaced

Event is triggered in response to a direct conference and direct transfer request.

| Property | Value |
|---|---|
| **Event Name** | `agentAssistanceRequestPlaced` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `requestAction` | String | The type of action requested. Value could be `transfer` or `conference`. |
| `mode` | String | The routing mode. Value is `queue`. |

## Example Payload

```json
{
    "requestAction": "transfer",
    "mode": "queue"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)