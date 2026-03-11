---
title: "Interaction Model: Rooms, Actors, and Events"
summary: "Technical reference defining the ExpertFlow CX interaction model — covering the Room abstraction, Actor roles, stateless CIMEvents, and stateful CIMActivities."
audience: [developer, integrator]
product-area: [platform, sdk, api]
doc-type: reference
difficulty: advanced
last-updated: 2026-03-11
---

# Interaction Model: Rooms, Actors, and Events

The ExpertFlow CX platform utilizes a unified interaction model to track and manage customer journeys. This model is built on three core abstractions: **Rooms**, **Actors**, and **Events**.

## 1. Core Abstractions

### **The Room (Container)**
A **Room** is the logical container for all interactions associated with a specific customer journey. It persists throughout the customer's lifetime, aggregating multiple sessions, messages, and system events into a single, searchable context.

### **The Actor (Participants)**
An **Actor** is any entity that performs an action within a Room.
*   **Customer:** The external party initiating the request.
*   **Agent (Human):** A contact center user handling the interaction.
*   **Bot (AI Agent):** An automated NLU engine (e.g., Rasa).
*   **Application:** A system component (e.g., Scheduler or Campaign Manager) triggering automated events.

### **CIMEvent (The Atomic Unit)**
A **CIMEvent** is the smallest stateless unit of change within an interaction. Every message, state change, or system notification is emitted as a CIMEvent. These events are consumed by various platform components for:
*   **Real-time Delivery:** Sending messages to the Agent Desk.
*   **Analytics:** Tracking SLAs and response times.
*   **Audit Trail:** Maintaining an immutable log of administrative and interaction changes.

---

## 2. Events vs. Activities
While Events are stateless and atomic, **CIMActivities** represent the stateful aggregation of events.

| Entity | State | Nature | Example |
| :--- | :--- | :--- | :--- |
| **CIMEvent** | Stateless | Atomic | `CUSTOMER_MESSAGE` received. |
| **CIMActivity** | Stateful | Aggregate | A "Call Leg" consisting of ringing, answered, and hang-up events. |

---

## 3. Master Conversation Events Table
The following table defines the primary events used across the platform's microservices (CCM, Bot-Framework, Agent-Manager).

| Event Name | Type | Description |
| :--- | :--- | :--- |
| `CUSTOMER_MESSAGE` | ACTIVITY | Fired when a message is received from the customer. |
| `AGENT_MESSAGE` | ACTIVITY | Fired when an agent sends a message. |
| `BOT_MESSAGE` | ACTIVITY | Fired when a bot engine sends a response. |
| `CHANNEL_SESSION_STARTED` | NOTIFICATION | Fired when a new customer presence is detected on a channel. |
| `CHANNEL_SESSION_ENDED` | NOTIFICATION | Fired when a customer closes the chat or the inactivity timer expires. |
| `AGENT_RESERVED` | NOTIFICATION | Fired when the Routing Engine offers a task to an agent. |
| `AGENT_SUBSCRIBED` | NOTIFICATION | Fired when an agent successfully joins a conversation. |
| `FIND_AGENT` | NOTIFICATION | Fired when a bot or system component requests a human agent. |
| `WRAPUP_APPLIED` | ACTIVITY | Fired when an agent submits a wrap-up form. |
| `CALL_HOLD` / `CALL_RESUME` | NOTIFICATION | Fired during voice interactions to signal CTI state changes. |

---

## 4. Interaction Lifecycle Workflow
1.  **Session Start:** `CHANNEL_SESSION_STARTED` event creates or identifies the **Room**.
2.  **Customer Action:** `CUSTOMER_MESSAGE` (Event) is converted into an Interaction (Activity).
3.  **Routing:** `FIND_AGENT` triggers the Routing Engine to locate a `CCUser` (Actor).
4.  **Engagement:** `AGENT_SUBSCRIBED` joins the agent to the Room.
5.  **Completion:** `CHANNEL_SESSION_ENDED` archives the activity while keeping the Room context for the next customer visit.

---

## Related Guides
*   [Platform Objects and Data Model](./Platform-Objects-and-Data-Model.md)
*   [CIM Message Schema Master](./CIM-Message-Schema/CIM-Messages.md)
*   [Socket Events Reference](./Socket_Events/index.md)
