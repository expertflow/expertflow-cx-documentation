---
title: "Platform Objects and Data Model"
summary: "Clinical technical reference defining the core entities, actors, and state objects that drive the ExpertFlow CX interaction engine."
audience: [developer-integrator]
product-area: [platform, sdk]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Platform Objects and Data Model

The ExpertFlow CX platform is built on a structured data model where every interaction, user, and system state is defined by a set of core entities. These objects are common across all REST and WebSocket interfaces.

## 1. CCUser (Agent)
Defines the identity and routing capabilities of a contact center user.
| Property | Type | Description |
| :--- | :--- | :--- |
| **id** | UUID | System-generated unique identifier. |
| **participantType** | String | Always set to `CCUser`. |
| **keycloakUser** | Object | Linked identity from the IAM provider (Roles, Realm, Scopes). |
| **routingAttributes** | Array | List of skills assigned to the user for precision routing. |

## 2. AgentPresence
Tracks the real-time availability and channel states of a CCUser.
```json
{
  "CCUser": { "id": "uuid" },
  "state": { "name": "READY | NOT_READY", "reasonCode": "id" },
  "stateChangeTime": 1651434965139,
  "agentMrdStates": [ ... ] 
}
```

## 3. Participant
Defines an actor within a specific conversation.
- **JoiningTime:** Timestamp when the participant entered the conversation.
- **isActive:** Boolean flag indicating if the participant is currently connected.
- **state:** The specific conversation state (e.g., `STARTED`, `LEFT`).
- **conversationId:** UUID of the active interaction session.

## 4. Tenant
The top-level organizational container.
- **id:** Unique ID assigned by Keycloak.
- **name:** The display name of the business unit or company.

## 5. Channel & ChannelConfig
- **Channel:** Represents a specific entry point (e.g., a specific WhatsApp number).
- **ChannelConfig:** Defines the behavior of that channel (e.g., Routing Mode, Max Tasks, Inactivity Timeouts).

---

*For interaction data schemas, see the [CIM Message Schema Master](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md).*
