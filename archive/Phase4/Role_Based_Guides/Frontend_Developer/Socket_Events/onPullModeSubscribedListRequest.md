---
title: "onPullModeSubscribedListRequest"
summary: "Emitted by Agent Manager when a new chat is initiated in one of an agent's subscribed pull-mode lists, or when an agent leaves a chat."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["onPullModeSubscribedListRequest socket event CX", "onPullModeSubscribedListRequest Agent Manager CX", "Socket.IO CX"]
aliases: ["onPullModeSubscribedListRequest event ExpertFlow", "onPullModeSubscribedListRequest socket CX"]
last-updated: 2026-03-12
---

# onPullModeSubscribedListRequest

Event is triggered when a new chat is initiated by the customer in one of the agent's subscribed lists. It is also triggered when an agent leaves a chat.

| Property | Value |
|---|---|
| **Event Name** | `onPullModeSubscribedListRequest` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

**Possible `type` values:**

- `PULL_MODE_LIST_REQUEST_RECEIVED` — a new chat request has been received in the subscribed list.
- `PULL_MODE_LIST_REQUEST_STATE_CHANGED` — the state of an existing request in the list has changed.

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `pullModeEvent` | String | JSON-serialized string describing the properties of the chat session. Contains: `id` (String, system-generated channel session ID), `channelSession` (Channel Object, conversation session details), `status` (String), `listId` (String, ID of the subscribed list), `time` (epoch timestamp). |
| `type` | String | Action of the event: `PULL_MODE_LIST_REQUEST_RECEIVED` or `PULL_MODE_LIST_REQUEST_STATE_CHANGED`. |
| `conversationId` | String | ID of the associated conversation (or list ID). |

## Example Payload

```json
{
    "pullModeEvent": "{\"id\":\"67c58d36956d765cfc278e0f\",\"channelSession\":{\"participantType\":\"ChannelSession\",\"id\":\"67c58d36d9244213fbf321d0\",\"channel\":{\"id\":\"6737304a7f433c0c29ee93b2\",\"name\":\"pull\",\"serviceIdentifier\":\"1133\",\"defaultOutbound\":false,\"tenant\":{\"id\":\"678f7e30f718dd632e3090b4\",\"name\":null},\"channelConfig\":{\"id\":\"678f7e30f718dd632e3090b5\",\"channelMode\":\"HYBRID\",\"conversationBot\":\"\",\"responseSla\":0,\"customerActivityTimeout\":6000,\"customerSla\":{\"totalDuration\":null,\"action\":null,\"startTime\":null},\"customerIdentificationCriteria\":{\"value\":null},\"routingPolicy\":{\"agentSelectionPolicy\":\"LONGEST_AVAILABLE\",\"routeToLastAgent\":true,\"routingMode\":\"PULL\",\"routingObjectId\":\"67372f8d58db250027b8e917\",\"agentRequestTtl\":6000},\"botId\":\"6712cf4bfb156449bb04ce99\"}},\"status\":\"CREATED\",\"listId\":\"67372f8d58db250027b8e917\",\"time\":1740999990727}",
    "type": "PULL_MODE_LIST_REQUEST_RECEIVED",
    "conversationId": "67372f8d58db250027b8e917"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [pullModeSubscribedListRequests](./pullModeSubscribedListRequests.md)
- [subscribePullModeList](./subscribePullModeList.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
