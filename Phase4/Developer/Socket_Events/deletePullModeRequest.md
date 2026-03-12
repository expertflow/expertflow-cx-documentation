---
title: "deletePullModeRequest"
summary: "Emitted by Agent Desk to Agent Manager when an agent ends a chat, instructing the platform to remove the pull-mode request."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["deletePullModeRequest socket event CX", "deletePullModeRequest Agent Manager CX", "Socket.IO CX"]
aliases: ["deletePullModeRequest event ExpertFlow", "deletePullModeRequest socket CX"]
last-updated: 2026-03-12
---

# deletePullModeRequest

Event is emitted when an agent ends a chat. The Agent Desk emits `deletePullModeRequest` to the Agent Manager, which listens to the event and successfully ends the chat for the agent.

| Property | Value |
|---|---|
| **Event Name** | `deletePullModeRequest` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `id` | String | ID of the chat request that needs to end. Example: `"9d7a1b83-e2c3-47c5-899b-3820a768b6b8"`. |

## Related Articles

- [Socket Events Overview](./index.md)
- [joinPullModeRequest](./joinPullModeRequest_2531724.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
