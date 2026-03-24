---
title: "agentAssignedForAssistance"
summary: "Emitted by Agent Manager when an agent is assigned to a conversation in response to a consult transfer or direct transfer request."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["agentAssignedForAssistance socket event CX", "agentAssignedForAssistance Agent Manager CX", "Socket.IO CX"]
aliases: ["agentAssignedForAssistance event ExpertFlow", "agentAssignedForAssistance socket CX"]
last-updated: 2026-03-12
---

# agentAssignedForAssistance

Event is triggered when an agent is assigned to the conversation in response to a consult transfer or direct transfer.

| Property | Value |
|---|---|
| **Event Name** | `agentAssignedForAssistance` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `conversationId` | String | ID of the conversation. |
| `task` | String | The task object associated with the assignment. |
| `type` | String | The type of assignment. Value could be `consult` or `direct-transfer`. |

## Example Payload

```json
{
    "conversationId": "67c1cb75956d765cfc275754",
    "task": {},
    "type": "consult"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)