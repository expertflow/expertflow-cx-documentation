---
title: "AgentManager SDK Reference"
summary: "Technical reference for building custom Agent Desktops using the AgentManager Socket.io and REST interfaces."
audience: [developer]
product-area: [platform, sdk]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# AgentManager SDK Reference

The AgentManager SDK provides the event-driven interfaces required to build custom agent interfaces. It utilizes **Socket.io** for real-time events, **REST APIs** for stateful requests, and **Firebase Cloud Messaging (FCM)** for background notifications.

## 1. Connection & Authentication
Establish a secure Socket.io connection using the Agent Manager FQDN and Keycloak user details.

- **Base URL:** `https://{AGENT_MANAGER_HOST}/`
- **Socket.io Version:** `4.4.0` (Required)

### Handshake Example:
```javascript
import { io } from "socket.io-client";

const socket = io(origin, {
  path: path === "/" ? "" : path + "/socket.io",
  auth: {
    agent: keycloak_User,
    fcm: "" // Optional FCM token for push notifications
  }
});
```

## 2. Agent Presence & State Management
Manage the agent's global and Media Routing Domain (MRD) states.

### State Transitions
| Action | Event Name | Target State |
|--------|------------|--------------|
| Change Global State | `changeAgentState` | `READY`, `NOT_READY`, `LOGOUT` |
| Change MRD State | `changeAgentState` | Set `action: agentMRDState` |

**Rule:** An agent must be in a global `READY` state before any specific MRD can be set to `READY`.

## 3. Interaction Lifecycle (Push Mode)
The Routing Engine pushes tasks to the SDK via the `taskRequest` event.

### Task States
1.  **RESERVED:** The initial state when a task is offered. The **RONA timer** starts.
2.  **ACTIVE:** Set once the agent accepts via `topicSubscription`.
3.  **CLOSED:** Set after the agent leaves or the RONA timer expires.

### Accepting a Task:
```javascript
// Emit to AgentManager
socket.emit("topicSubscription", {
  conversationId: "uuid",
  taskId: "uuid"
});
```

## 4. Messaging & CIM Events
All interaction content (Text, Media, System Activities) follows the **Customer Interaction Model (CIM)**.

### Publishing a Message:
Emit the `publishCimEvent` to send content to the customer.
```json
{
  "header": {
    "intent": "PUBLISH",
    "originalMessageId": null
  },
  "body": {
    "type": "PLAIN",
    "markdownText": "Hello, how can I help you?"
  }
}
```

## 5. Supervisor & Assistance Events
Events for real-time collaboration and monitoring.

- **HAND_RAISED:** Dispatched when an agent requests discreet help.
- **joinAsSilentMonitor:** Allows a supervisor to subscribe to `onTopicData` without notification to the customer.
- **joinAsBargeIn:** Elevates a supervisor to a full participant in the interaction.

---

*For exhaustive payload schemas, see the [Master Socket Events List](../Developer/Socket_Events/index.md) or the [CIM Message Objects Reference](../Developer/CIM-Message-Schema/CIM-Messages.md).*
