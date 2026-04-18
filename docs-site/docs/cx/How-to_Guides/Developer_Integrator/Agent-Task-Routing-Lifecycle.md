---
audience: [developer-integrator]
doc-type: reference
difficulty: beginner
aliases: []
---

# Agent Task and Routing Lifecycle

An **Agent Task** (or Routing Task) tracks a conversation between an agent and a customer. This document details how tasks are created, assigned, and closed across different routing modes.

## 1. PUSH Mode (Queue-Based)
Used when a request is parked in a queue to find an available agent.

| Event | Task/Media State Change |
| :--- | :--- |
| **New Request** | Task created as `QUEUED` / `ACTIVE`. |
| **Agent Reserved** | Media state changes to `RESERVED`. |
| **Agent Accepts** | Media state changes to `ACTIVE`. |
| **RONA (No Answer)** | Current task is deleted; a new task is created and re-queued. |
| **TTL Expires** | Task closed with `NO_AGENT_AVAILABLE`. |

## 2. PULL Mode (Direct Assignment)
Used when the agent is known beforehand (e.g., sticky routing).
- A new task is created directly with `MediaState = ACTIVE`.
- If a task already exists for the agent and the MRD is "Auto Join-able", the existing task is returned.

## 3. Transfer and Conference

### Queue Transfer
- A new task is created in `QUEUED` state.
- The original agent's task moves to `WRAP_UP` (Reason: `TRANSFERRED`) and then `CLOSED`.

### Named Agent Transfer
- A new task is created in `RESERVED` state for the specific target agent.
- If the agent accepts, it moves to `ACTIVE`. If they decline, it closes as `RONA`.

## Task and Media States

### Task States
- **ACTIVE**: The task is currently being handled or routed.
- **WRAP_UP**: The post-interaction phase (if enabled).
- **CLOSED**: The task is finalized.

### Media States
- **QUEUED**: Waiting for an agent.
- **RESERVED**: An agent is being alerted.
- **ACTIVE**: Agent is participating in the conversation.

For a full list of termination codes, see the [Task Reason Codes](../Administrator/Configuring-Reason-Codes.md) reference.
