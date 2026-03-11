---
title: "Routing Engine Developer Guide"
summary: "Technical reference for the ExpertFlow CX Routing Engine — covering routing attributes, Media Routing Domains (MRDs), precision queues, queue steps, agent global and MRD states, tasks, and routing policies (Push and Pull)."
audience: [developer]
product-area: [channels, digital]
doc-type: reference
difficulty: advanced
keywords: ["routing engine CX", "routing engine developer guide", "MRD routing CX", "precision queue developer", "agent MRD state CX", "push pull routing CX", "routing attribute developer", "task state routing CX"]
aliases: ["routing engine API CX", "routing engine reference CX", "CX routing developer guide"]
last-updated: 2026-03-10
---

# Routing Engine Developer Guide

The Routing Engine is the core microservice responsible for matching customer requests to agents. Beyond routing, it manages agent and agent-MRD states, task lifecycle, routing attribute configurations, and both push-based and pull-based routing policies.

## Core Sub-Components

- Push-mode automatic routing
- Agent and Agent-MRD state manager
- Task state manager (Push and Pull)
- Routing Attributes, MRD, and Queue configuration backend

---

## Key Concepts

### Routing Attributes

A Routing Attribute is a skill assigned to an agent or supervisor. Agents can have an unlimited number of unique routing attributes.

| Type | Description | Value Range |
|---|---|---|
| **Proficiency** | How skilled the agent is on a particular topic. | `1` (lowest) to `10` (highest) |
| **Boolean** | Whether the agent has a skill or not. | `true` or `false` |

**Routing Attribute fields:**

| Field | Description |
|---|---|
| `Id` | Unique identifier (auto-assigned). |
| `Name` | Name of the routing attribute. |
| `Description` | Short description. |
| `Type` | `Boolean` or `Proficiency`. |
| `Default-value` | Value used when the attribute is assigned to an agent without an explicit value. `0` or `1` for Boolean; `1–10` for Proficiency. |

Routing attributes are configured in Unified Admin. Administrators assign attributes to agents and can override default values per assignment.

---

### Media Routing Domains (MRD)

An MRD is a collection of precision queues grouped by a common media class (e.g., Chat, Voice, Email). MRDs control which types of requests agents can receive.

**Key relationships:**
- A precision queue belongs to **one** MRD; one MRD can have **many** queues.
- A channel type is linked to **one** MRD; one MRD can have **many** channel types.

**Agent-MRD association:** Agents have independent states per MRD. An agent can be `READY` on a Chat MRD and `NOT_READY` on a Voice MRD simultaneously.

**MRD fields:**

| Field | Description |
|---|---|
| `Id` | Unique identifier (auto-assigned). |
| `Name` | Name of the MRD. |
| `Description` | Short description. |
| `Interruptible` | Boolean — whether a conversation in this MRD can be interrupted by a higher-priority MRD task. (Not yet implemented.) |

---

### Routing Queues (Precision Queues)

A precision queue hosts customer requests and determines which agents are eligible to receive them based on routing attribute criteria.

**Queue Steps** define the routing logic:
- A queue can have **at most 10 steps**.
- Each step contains one or more **expressions** (combinations of **terms**).
- A **term** compares an attribute to a value: `English == true`, `Broadband >= 7`.
- An **expression** is multiple terms combined with `AND`/`OR`.
- Steps have a **step timeout (seconds)** — if no matching agent is found, the engine moves to the next step.

**Example queue logic:**

```
Step 1: (English == true) AND (Los Angeles == true) AND (Broadband >= 7)
Step 2: (English == true) AND (Broadband >= 5)
Step 3: (English == true)
```

Steps are evaluated left-to-right. If no agent is found in Step 1, the engine moves to Step 2, and so on.

---

### Lists (Pull Routing)

A **List** is a broadcast queue used in pull-mode routing. Incoming requests are parked on the List rather than pushed to a specific agent.

**Request states on a List:**

| State | Description |
|---|---|
| `UNREAD` | No agent has joined the request yet. |
| `ACTIVE` | At least one agent is currently in the conversation. |
| `INACTIVE` | An agent previously joined and left without closing. No new notifications are sent for new customer messages. |
| `CLOSED` | The request was closed and removed from the List. |

Agents can close a request when it is in `ACTIVE`, `INACTIVE`, or `UNREAD` state.

---

### Agent Global States

An agent's global state is independent of any specific MRD.

| From | To | Description |
|---|---|---|
| — | `UNKNOWN` | State cannot be determined. |
| `LOGOUT` | `LOGIN` | Transient state; immediately transitions to `NOT_READY`. |
| `LOGIN` | `NOT_READY` | Default state after login. No requests are routed. |
| `NOT_READY` | `READY` | Agent is available. Requests may be routed based on MRD state. |
| `READY` | `NOT_READY` | All MRD toggles are turned off. |
| `NOT_READY` | `LOGOUT` | All MRDs disabled; active tasks re-routed; agent logged out. |
| any logged-in | `LOGOUT` | Active tasks are re-routed. |

---

### Agent MRD States

Each agent has a separate state per MRD.

| From | To | Description | Routable |
|---|---|---|---|
| — | `LOGIN` | Transient state after sign-in; transitions to `NOT_READY`. | No |
| `LOGIN` | `NOT_READY` | Agent is unavailable on this MRD. MRD toggle is grey/OFF. | No |
| `NOT_READY` | `READY` | Agent is available for requests on this MRD. Toggle is green/ON. | Yes |
| `READY` | `ACTIVE` | Agent is handling at least one task on this MRD. Toggle is orange/ON. | Yes |
| `ACTIVE` | `BUSY` | Agent has reached the maximum tasks for this MRD. Toggle is red/ON. | No |
| `ACTIVE`/`BUSY` | `PENDING_NOT_READY` | Agent turned off this MRD while active. Toggle is purple/OFF. | No |
| `PENDING_NOT_READY` | `NOT_READY` | All active tasks ended; agent transitions to NOT_READY. | No |
| `ACTIVE` | `READY` | Last task for this MRD closed; agent returns to READY. | Yes |
| any | `UNKNOWN` | Failover scenario. Agent can switch to READY or NOT_READY. | No |
| `READY` | `INTERRUPTED` | Higher-priority MRD task interrupted this MRD. System-controlled. | No |

---

### Tasks

The Routing Engine creates a **Task** for each request assigned to an agent. The task lifecycle mirrors the conversation lifecycle.

| Task State | Description |
|---|---|
| `Created` | Task has been created and assigned to an agent. |
| `Active` | Agent is actively handling the task. |
| `Wrap-up` | Agent is applying wrap-up codes/notes after the interaction. |
| `Closed` | All channel sessions closed; agent has left. |

---

## Routing Policies

### Push Routing (Precision Routing)

The system automatically assigns incoming requests to the best-matching available agent based on queue step criteria. The agent cannot refuse the assignment.

**Flow:**
1. Customer sends a message on channel `C1`.
2. Request is enqueued in the default queue `Q1` for that channel.
3. Routing Engine evaluates queue steps and finds the best-matching agent.
4. Agent task is created; agent transitions from `READY` to `ACTIVE`.
5. On conversation close, agent returns to `READY`.

### Pull Routing

Incoming requests are broadcast to a List. Subscribed agents receive notifications and self-select which requests to join.

**Flow:**
1. Customer message arrives on a pull-mode channel.
2. Request is published to the associated List.
3. All subscribed agents see the notification.
4. One or more agents join the request.
5. Conversation is closed by an agent when the interaction completes.

---

## Related Articles

- [Precision Routing](../Solution_Admin/Precision-Routing.md)
- [Pull-Mode Routing](../Solution_Admin/Pull-Mode-Routing.md)
- [Agent Task Routing Lifecycle](Agent-Task-Routing-Lifecycle.md)
- [Agent MRD States Reference](../Agent/Agent-MRD-States-Reference.md)
- [Media Routing Domains (MRD) Overview](../Solution_Admin/Media-Routing-Domains-MRD-Overview.md)
