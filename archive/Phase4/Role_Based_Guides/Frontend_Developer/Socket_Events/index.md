---
title: "Socket Events"
slug: Socket-Events-Index
summary: "Reference for all Socket.IO events in ExpertFlow CX — covering events emitted by the Agent Desk (changeAgentState, publishCimEvent, transfer/conference requests, pull-mode events) and events emitted by Agent Manager (taskRequest, onCimEvent, agentPresence, revokeTask, and more)."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["socket events CX", "Socket.IO events CX", "Agent Manager events CX", "Agent Desk socket events CX", "onCimEvent CX", "publishCimEvent CX", "taskRequest CX", "WebSocket events CX"]
aliases: ["CX socket events reference", "agent manager socket events CX", "socket event list CX"]
last-updated: 2026-03-12
---

# Socket Events

ExpertFlow CX uses Socket.IO for real-time bidirectional communication between a custom Agent Desk and the Agent Manager. This page lists all socket events, their triggers, and the emitting component.

---

## Agent Desk as Emitter

These events are **emitted by the Agent Desk** and listened to by Agent Manager.

| Event | Description |
|---|---|
| [`publishCimEvent`](publishCimEvent.md) | Emitted when an agent sends an in-conversation message — plain text, media, contact, location, URL, or WrapUp type. |
| [`directConferenceRequest`](./directConferenceRequest.md) | Emitted when an agent requests another agent (from a queue) to join the active conversation. The Routing Engine finds an available agent until TTL expires. |
| [`consultTransferRequest`](./consultTransferRequest.md) | Emitted when an agent wants to leave the conversation and transfer it to another agent. The Routing Engine finds an available agent until TTL expires. |
| [`consultConferenceRequest`](./consultConferenceRequest.md) | Emitted when an agent requests another agent to join as a consult (not taking over). |
| [`consultRequest`](./consultRequest.md) | Emitted when an agent initiates a consult with another agent during an active conversation. |
| [`directTransferRequest`](./directTransferRequest.md) | Emitted when an agent wants to leave the conversation and directly transfer it to another agent (no consult phase). |
| [`closeWrapup`](./closeWrapup.md) | Emitted when an agent completes the wrap-up phase. |
| [`pauseConversation`](./pauseConversation.md) | Emitted when an agent pauses an active conversation. |
| [`resumeConversation`](./resumeConversation.md) | Emitted when an agent resumes a previously paused conversation. |
| [`JoinAsSilentMonitor`](./joinAsSilentMonitor.md) | Emitted when a supervisor joins an active conversation as a silent monitor. |
| [`joinAsWhisper`](./joinAsWhisper.md) | Emitted when a supervisor joins an active conversation in whisper mode (can speak to agent only). |
| [`JoinAsBargeIn`](./joinAsBargeIn.md) | Emitted when a supervisor barges into an active conversation (full participant). |
| [`subscribePullModeList`](./subscribePullModeList.md) | Emitted when an agent subscribes to a pull-mode list. Agent Manager subscribes the agent and returns existing conversations in the list. |
| [`unsubscribePullModeList`](./unsubscribePullModeList.md) | Emitted when an agent unsubscribes from a pull-mode list. |
| [`joinPullModeRequest`](./joinPullModeRequest.md) | Emitted when an agent joins a specific chat from the pull-mode list. |
| [`deletePullModeRequest`](./deletePullModeRequest.md) | Emitted when an agent ends a chat in pull mode. |
| [`topicSubscription`](./topicSubscription.md) | Emitted when an agent subscribes to a conversation topic. |
| [`topicUnsubscription_`](./topicUnsubscription.md) | Emitted when an agent unsubscribes from a conversation topic. |

---

## Agent Manager as Emitter

These events are **emitted by Agent Manager** and listened to by the Agent Desk.

| Event | Description |
|---|---|
| [`taskRequest`](./taskRequest.md) | Triggered on a new incoming conversation request assigned to the agent. |
| [`revokeTask`](./revokeTask.md) | Triggered to revoke a task request that the agent did not accept within the configured TTL. |
| [`onCimEvent`](onCimEvent.md) | Delivers real-time CIM Events (messages) to the agent. |
| [`agentPresence_`](./agentPresence.md) | Triggered to update agent state information (MRD states, availability). |
| [`onChannelTypes`](./onChannelTypes.md) | Triggered once a socket connection is established — delivers the available channel types. |
| [`topicClosed`](./topicClosed.md) | Triggered to notify the agent when a conversation topic is closed. |
| [`topicUnsubscription`](./topicUnsubscription.md) | Triggered when an agent successfully leaves a conversation. Returns a success message. |
| [`onTopicData`](./onTopicData.md) | Triggered when an agent subscribes to a topic — delivers the topic's current data. |
| [`socketSessionRemoved`](socketSessionRemoved.md) | Triggered when the agent switches to another browser tab. The Agent Desk should log the agent out of the previous session. |
| [`wrapupTimerStarted`](./wrapupTimerStarted.md) | Triggered to start the wrap-up timer for the agent. |
| [`agentAssistanceRequestPlaced`](./agentAssistanceRequestPlaced.md) | Triggered in response to a `directConferenceRequest` or `directTransferRequest`. |
| [`agentAssignedForAssistance`](./agentAssignedForAssistance.md) | Triggered when an agent is assigned in response to a consult or direct transfer request. |
| [`consulTransferRequestSuccess`](./consulTransferRequestSuccess.md) | Triggered when an agent is successfully assigned to a conversation in response to a `consultTransferRequest`. |
| [`addPullModeSubscribedListRequests`](./addPullModeSubscribedListRequests.md) | Triggered when an agent subscribes to a pull-mode list. Returns existing conversations in the list if any. |
| [`removePullModeSubscribedListRequests`](./removePullModeSubscribedListRequests.md) | Triggered when an agent unsubscribes from a pull-mode list. |
| [`onPullModeSubscribedList`](./onPullModeSubscribedList.md) | Triggered when an agent subscribes or unsubscribes from a list. |
| [`onPullModeSubscribedListRequest`](./onPullModeSubscribedListRequest.md) | Triggered when a new customer chat arrives in a subscribed list, or when an agent leaves a chat. |
| [`pullModeSubscribedListRequests`](./pullModeSubscribedListRequests.md) | Triggered if there are existing chat requests in a list the agent just subscribed to. |
| [`errors`](./errors.md) | Triggered to notify the agent of any system or request error. |
| [`connect_error`](./connectError.md) | Triggered when an error occurs during the Socket.IO handshake (e.g., unauthorized user, invalid data). |

---

## Related Articles

### SDK & Integration
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
- [JavaScript SDK](../JavaScript-SDK.md)
- [Customer-Facing SDK](../Customer-Facing-SDK.md)

### Data Model & Objects
- [CIM Message Schema](../CIM-Message-Schema/CIM-Messages.md)
- [Platform Objects and Data Model](../Platform-Objects-and-Data-Model.md)
- [Conversation Life Cycle Objects](../Conversation-Life-Cycle-Objects.md)
- [Interaction Model Overview](../Interaction-Model-Overview.md)

### Routing & Lifecycle
- [Agent Task Routing Lifecycle](../Agent-Task-Routing-Lifecycle.md)
- [Routing Engine Developer Guide](../Routing-Engine-Developer-Guide.md)
