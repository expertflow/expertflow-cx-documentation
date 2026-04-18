---
title: "AgentManager SDK Integration Guide"
summary: "End-to-end integration guide for building custom agent desktops using the AgentManager Socket.io and REST interfaces."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# AgentManager SDK Integration Guide

The AgentManager SDK allows you to build custom, event-driven agent interfaces. It utilizes **Socket.io** for real-time events and **Firebase Cloud Messaging (FCM)** for background notifications.

## 1. Connection & Authentication
Establish a connection to the Agent Manager using the platform FQDN.
- **Base URL:** `https://{AGENT_MANAGER_HOST}/`
- **Socket Version:** `4.4.0`

### Authentication Flow:
1.  Perform a POST request to the **User Login API** to retrieve Keycloak user details.
2.  Initiate the Socket.io handshake using the returned credentials.
3.  Listen for the `connect` event to confirm the session is active.

## 2. Managing Presence
Agents must manage their availability via the `changeAgentState` event.
- **Global State:** Transitions between `READY`, `NOT_READY`, and `LOGOUT`.
- **Reason Codes:** Required for any move out of the `READY` state.
- **MRD Specifics:** You can independently control availability for Voice vs. Digital channels.

## 3. Interaction Lifecycle
Tasks are pushed to the agent interface via the `taskRequest` event.
1.  **Subscription:** When a task is offered, the client must emit `topicSubscription` to accept.
2.  **Interaction:** Exchange messages using `publishCimEvent`.
3.  **Unsubscription:** Emit `topicUnsubscription` to leave the conversation and close the task.

## 4. Notifications (FCM)
For mobile or background desktop applications, integrate with the FCM platform.
- **Setup:** Register your FCM token during the Socket.io handshake.
- **Payload:** The Agent Manager will push `agentPresence` and `taskRequest` payloads to the registered token when the WebSocket is disconnected.

---

*For exhaustive event schemas, see the [Socket Events Schema Reference](../../Reference/Schemas_and_Data_Model/Socket_Events/index.md).*
