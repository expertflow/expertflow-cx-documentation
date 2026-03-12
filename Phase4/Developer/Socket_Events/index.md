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
last-updated: 2026-03-10
---

# Socket Events

ExpertFlow CX uses Socket.IO for real-time bidirectional communication between a custom Agent Desk and the Agent Manager. This page lists all socket events, their triggers, and the emitting component.

---

## Agent Desk as Emitter

These events are **emitted by the Agent Desk** and listened to by Agent Manager.

| Event | Description |
|---|---|
| `changeAgentState` | Emitted when an agent changes MRD state (ready/not-ready, with or without a reason code) or logs out. Agent Manager updates the agent's presence accordingly. |
| `publishCimEvent` | Emitted when an agent sends an in-conversation message — plain text, media, contact, location, URL, or WrapUp type. |
| `directConferenceRequest` | Emitted when an agent requests another agent (from a queue) to join the active conversation. The Routing Engine finds an available agent until TTL expires. |
| `consultTransferRequest` | Emitted when an agent wants to leave the conversation and transfer it to another agent. The Routing Engine finds an available agent until TTL expires. |
| `consultConferenceRequest` | Emitted when an agent requests another agent to join as a consult (not taking over). |
| `directTransferRequest` | Emitted when an agent wants to leave the conversation and directly transfer it to another agent (no consult phase). |
| `closeWrapup` | Emitted when an agent completes the wrap-up phase. |
| `JoinAsSilentMonitor` | Emitted when a supervisor joins an active conversation as a silent monitor. |
| `subscribePullModeList` | Emitted when an agent subscribes to a pull-mode list. Agent Manager subscribes the agent and returns existing conversations in the list. |
| `unsubscribePullModeList` | Emitted when an agent unsubscribes from a pull-mode list. |
| `joinPullModeRequest` | Emitted when an agent joins a specific chat from the pull-mode list. |
| `deletePullModeRequest` | Emitted when an agent ends a chat in pull mode. |
| `topicSubscription` | Emitted when an agent subscribes to a conversation topic. |
| `topicUnsubscription_` | Emitted when an agent unsubscribes from a conversation topic. |

---

## Agent Manager as Emitter

These events are **emitted by Agent Manager** and listened to by the Agent Desk.

| Event | Description |
|---|---|
| `taskRequest` | Triggered on a new incoming conversation request assigned to the agent. |
| `revokeTask` | Triggered to revoke a task request that the agent did not accept within the configured TTL. |
| `onCimEvent` | Delivers real-time CIM Events (messages) to the agent. See [onCimEvent](./onCimEvent.md). |
| `agentPresence_` | Triggered to update agent state information (MRD states, availability). |
| `onChannelTypes` | Triggered once a socket connection is established — delivers the available channel types. |
| `topicClosed` | Triggered to notify the agent when a conversation topic is closed. |
| `topicUnsubscription` | Triggered when an agent successfully leaves a conversation. Returns a success message. |
| `onTopicData` | Triggered when an agent subscribes to a topic — delivers the topic's current data. |
| `socketSessionRemoved` | Triggered when the agent switches to another browser tab. The Agent Desk should log the agent out of the previous session. See [socketSessionRemoved](./socketSessionRemoved.md). |
| `wrapupTimerStarted` | Triggered to start the wrap-up timer for the agent. |
| `agentAssistanceRequestPlaced` | Triggered in response to a `directConferenceRequest` or `directTransferRequest`. |
| `agentAssignedForAssistance` | Triggered when an agent is assigned in response to a consult or direct transfer request. |
| `consulTransferRequestSuccess` | Triggered when an agent is successfully assigned to a conversation in response to a `consultTransferRequest`. |
| `addPullModeSubscribedListRequests` | Triggered when an agent subscribes to a pull-mode list. Returns existing conversations in the list if any. |
| `removePullModeSubscribedListRequests` | Triggered when an agent unsubscribes from a pull-mode list. |
| `onPullModeSubscribedList` | Triggered when an agent subscribes or unsubscribes from a list. |
| `onPullModeSubscribedListRequest` | Triggered when a new customer chat arrives in a subscribed list, or when an agent leaves a chat. |
| `pullModeSubscribedListRequests` | Triggered if there are existing chat requests in a list the agent just subscribed to. |
| `errors` | Triggered to notify the agent of any system or request error. |
| `connect_error` | Triggered when an error occurs during the Socket.IO handshake (e.g., unauthorized user, invalid data). |

---

## Related Articles

- [onCimEvent](./onCimEvent.md)
- [publishCimEvent](./publishCimEvent.md)
- [socketSessionRemoved](./socketSessionRemoved.md)
- [Socket Event: joinAsBargeIn](./Socket-Event-joinAsBargeIn.md)
- [CIM Messages](../CIM-Message-Schema/CIM-Messages.md)
- [Agent Task Routing Lifecycle](../Agent-Task-Routing-Lifecycle.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
