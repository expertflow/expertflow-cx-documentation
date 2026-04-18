---
title: "consulTransferRequestSuccess"
summary: "Emitted by Agent Manager when an agent has been successfully assigned to a conversation in response to a consult transfer request."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["consulTransferRequestSuccess socket event CX", "consulTransferRequestSuccess Agent Manager CX", "Socket.IO CX"]
aliases: ["consulTransferRequestSuccess event ExpertFlow", "consulTransferRequestSuccess socket CX"]
last-updated: 2026-03-12
---

# consulTransferRequestSuccess

Event is triggered when an agent is assigned to the conversation in response to a consult transfer request.

| Property | Value |
|---|---|
| **Event Name** | `consulTransferRequestSuccess` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `conversationId` | String | ID of the conversation. |
| `newTask` | String | The new task object created for the assigned agent. |
| `agentId` | String | ID of the agent assigned to the conversation. |

## Example Payload

```json
{
    "conversationId": "67c1cb75956d765cfc275754",
    "task": {},
    "agentId": "7dcdf513-da75-4667-968b-94b8098bc689"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [consultTransferRequest](./consultTransferRequest.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
