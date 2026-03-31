---
title: "JoinAsSilentMonitor"
summary: "Emitted by Agent Desk when a supervisor requests to join an active conversation of a team member as a silent monitor."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["JoinAsSilentMonitor socket event CX", "JoinAsSilentMonitor Agent Manager CX", "Socket.IO CX"]
aliases: ["JoinAsSilentMonitor event ExpertFlow", "JoinAsSilentMonitor socket CX"]
last-updated: 2026-03-12
---

# JoinAsSilentMonitor

Event is emitted when a supervisor requests the Agent Manager to join an active conversation of a team member (agent) as a silent member.

| Property | Value |
|---|---|
| **Event Name** | `JoinAsSilentMonitor` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `topicParticipant` | Object | Agent details such as `id`, `type`, Keycloak user authentication fields, etc. |
| `agentId` | String | ID of the supervisor who wants to join the chat as a silent monitor. |
| `channelSession` | Object | Contains values of properties related to the session established through a particular channel (e.g., web). |

## Related Articles

- [Socket Events Overview](./index.md)
- [JoinAsBargeIn](./JoinAsBargeIn.md)
- [joinAsWhisper](./joinAsWhisper.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
