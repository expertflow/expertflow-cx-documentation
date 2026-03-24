---
title: "Agent States"
summary: "Reference for all global and channel category state transitions an agent can go through in ExpertFlow CX."
audience: [agent]
product-area: [agent-desk, platform]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-14
---

# Agent States

After logging in, agents default to the **Not Ready** state. Switching to **Ready** makes them eligible to receive routed interactions from their assigned Channel Categories.

There are two levels of state management in the Agent Desk:

- **Global State** — the top-level availability status. Changes here cascade to all assigned Channel Categories.
- **Channel Category State** — per-channel availability (e.g., Ready for Chat, Not Ready for Voice). Fine-tunes routing within a specific channel.

> **Push vs. Pull:** Global and Channel Category states only affect **Push Mode** routing. In **Pull Mode**, an agent can pick up requests from a subscribed list regardless of their state, as long as they are logged in.

---

## 1. Global State Transitions

| From | To | Description |
| :--- | :--- | :--- |
| `LOGOUT` | `LOGIN` | `LOGIN` is a transient state — the agent passes through it automatically and transitions to `NOT_READY` within seconds. |
| `LOGIN` | `NOT_READY` | Default state after login. All Channel Category toggles turn off. The Routing Engine will not route new requests to this agent. No reason code is assigned on this automatic transition. |
| `NOT_READY` | `READY` | The agent is now available. Requests may be routed depending on individual Channel Category states. The state dropdown turns active. |
| `READY` | `NOT_READY` | The agent manually steps away. A not-ready reason code (defined by the administrator in Unified Admin) can be selected. |
| `NOT_READY` / `READY` | `LOGOUT` | The system waits for the Agent Disconnect timer to expire, re-routes all active tasks to available agents, then logs the agent out. |
| — | `UNKNOWN` | Rare failover scenario where state cannot be determined. The agent can recover by switching to `READY` or `NOT_READY`. |

A real-time **state timer** is displayed on the agent desk, counting time spent in the current global state. The timer resets on every global state change.

---

## 2. Channel Category State Transitions

| From | To | Routable | Description |
| :--- | :--- | :---: | :--- |
| — | `LOGIN` | No | Transient state immediately after sign-in. No tasks are assigned. Automatically transitions to `NOT_READY`. |
| `LOGIN` | `NOT_READY` | No | Default state after login. The Channel Category toggle turns **grey (OFF)**. No new tasks are assigned for this channel. |
| `NOT_READY` | `READY` | Yes | The agent is available for this channel. The toggle turns **green (ON)**. |
| `READY` | `RESERVED` | Yes | A task is actively being offered to the agent (ringing). System-triggered. The agent has not yet accepted it. |
| `RESERVED` | `ACTIVE` | Yes | The agent accepts the offered task. Transitions automatically. |
| `RESERVED` | `READY` | Yes | The agent declines or the task times out (RONA). The agent returns to `READY`. |
| `READY` | `ACTIVE` | Yes | The agent is handling at least one task in this channel. System-triggered. The toggle turns **orange (ON)**. |
| `ACTIVE` | `BUSY` | No | The agent has reached the **Max Tasks** limit configured by the administrator. No new tasks are routed from this channel. The toggle turns **red (ON)**. |
| `READY` / `ACTIVE` | `INTERRUPTED` | No | A higher-priority interaction (typically a voice call) is active. The channel is temporarily blocked from receiving new tasks. Reverts automatically when the priority interaction ends. |
| `ACTIVE` | `READY` | Yes | The agent's last task in this channel is closed. The agent automatically returns to `READY`. |
| `ACTIVE` | `PENDING_NOT_READY` | No | The agent switches off a Channel Category while still active on tasks. The system waits for active tasks to clear before turning the channel off. The toggle turns **purple (OFF)**. |
| `BUSY` | `PENDING_NOT_READY` | No | The agent switches off a Channel Category while at the max task limit. Same clearing behaviour as above. |
| `PENDING_NOT_READY` | `NOT_READY` | No | Automatic transition once all active tasks are cleared. The channel toggle turns off. |
| `READY` | `NOT_READY` | No | The agent manually toggles off the channel (optionally with a reason). |
| — | `UNKNOWN` | No | Failover scenario. The agent can recover by switching to `READY` or `NOT_READY`. |

> The state timer does **not** apply to Channel Category state changes — only to global state changes.

---

*Related: [Managing Your Presence and States](Managing-Your-Presence-and-States.md) · [Presence and State Technical Reference](Presence-and-State-Technical-Reference.md)*
