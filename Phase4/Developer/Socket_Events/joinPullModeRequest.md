---
title: "joinPullModeRequest"
summary: "Emitted by Agent Desk to Agent Manager when an agent joins a chat in pull mode, causing the agent manager to assign the chat to the agent."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["joinPullModeRequest socket event CX", "joinPullModeRequest Agent Manager CX", "Socket.IO CX"]
aliases: ["joinPullModeRequest event ExpertFlow", "joinPullModeRequest socket CX"]
last-updated: 2026-03-12
---

# joinPullModeRequest

Event is emitted when an agent joins a chat. The Agent Desk emits `joinPullModeRequest` to the Agent Manager, which listens to the event and successfully joins the chat for the agent.

| Property | Value |
|---|---|
| **Event Name** | `joinPullModeRequest` |
| **Emitter** | Agent Desk |
| **Direction** | Agent Desk → Agent Manager |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `topicParticipant` | Object | The topic participant object for the agent joining the conversation. |
| `agentId` | String | ID of the agent for whom the event has been emitted. |
| `channelSession` | Object | Contains values of properties related to the session established through a particular channel (e.g., web). |
| `requestId` | String | ID of the task subscribed by the agent. |

## Example Payload

```json
{
  "topicParticipant": {},
  "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
  "channelSession": {},
  "requestId": "a13a49f4-7ec6-436b-91b0-0fd1be205799"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [deletePullModeRequest](./deletePullModeRequest_2531709.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
