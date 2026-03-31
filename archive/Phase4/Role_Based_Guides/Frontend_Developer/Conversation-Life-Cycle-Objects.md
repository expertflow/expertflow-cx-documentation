---
title: "Conversation Life-Cycle Objects"
summary: "Technical reference for developers defining the core actors and objects that drive the interaction engine."
audience: [developer, designer]
product-area: [platform, sdk]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Conversation Life-Cycle Objects

ExpertFlow CX is an actor-based conversation platform. Every interaction is governed by a set of core objects that define the state, the participants, and the routing logic.

## 1. Primary Actors (Participants)
A conversation can have multiple participants, each assigned a specific role.

- **Customer:** The external user reaching out via a media channel. They are identified via the CX-Customer APIs.
- **Agent:** The human participant handling the request on behalf of the business.
- **Conversation Bot:** A virtual agent (Rasa, Lex) that provides self-service or assists the agent.
- **App:** A technical participant representing an API-based system.
- **Controller:** The background system actor that manages the conversation flow, invites bots/agents, and enforces timeouts.

## 2. Structural Objects
| Object | Description |
| :--- | :--- |
| **Room** | The master container for a customer's lifetime journey. Stores all related conversations and events. |
| **Conversation** | A specific interaction session between a customer and the business. |
| **ChannelSession** | Tracks the customer's presence on a specific media channel (e.g., a specific WhatsApp session). |
| **AgentTask** | The specific unit of work assigned to an agent when they are invited to a conversation. |

## 3. The Object Relationship
1.  **Detection:** A `ChannelSession` is created when customer presence is detected.
2.  **Creation:** The `Controller` creates a `Conversation` object if no active one exists.
3.  **Invitation:** The `Controller` invites a `Bot` or an `Agent` to the conversation.
4.  **Assignment:** If an agent is invited, the interaction is encapsulated as an `AgentTask` for tracking and reporting.

---

*For detailed schema definitions of these objects, see [Platform Objects & Data Model](Platform-Objects-and-Data-Model.md).*
