---
title: "Managing Your Presence and States"
summary: "Guide for agents to manage global and channel-specific availability states to receive customer interactions."
audience: [agent]
product-area: [agent-desk]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Managing Your Presence and States

As an Agent (Amy), your **State** determines whether the system can route new customer interactions to you. You can manage your availability at two levels: **Global State** and **Channel Category (MRD) State**.

## 1. Global Presence States
The Global State is your master availability. It sets the baseline for all individual channels.

- **NOT READY:** Your default state upon login. You will not receive any new "Push" interactions. 
- **READY:** Signals that you are available for work. Individual channels will now follow their own specific settings.
- **LOGOUT:** Completely removes you from the routing engine. 

### Global State Transitions:
| From | To | Description |
| :--- | :--- | :--- |
| **Login** | **Not Ready** | Automatic transition upon signing in. |
| **Not Ready** | **Ready** | You become eligible for task assignment. |
| **Ready** | **Not Ready** | Requires a **Reason Code** (e.g., Break, Training). |
| **Any** | **Logout** | System clears your active tasks before finalizing the logout. |

## 2. Channel Category (MRD) States
You can fine-tune your availability for specific channels (e.g., being Ready for Chat but Not Ready for Voice).

- **READY (Green):** You are available for this specific channel.
- **ACTIVE (Orange):** You are currently handling at least one task in this channel.
- **BUSY (Red):** You have reached your "Max Tasks" limit for this channel.
- **PENDING NOT READY (Purple):** You have switched the channel off, but the system is waiting for you to finish your active tasks.

### Pro-Tips for Amy:
1. **State Timer:** Watch the timer at the top of your screen to track how long you've been in your current state—this is a key metric for your supervisor.
2. **Push vs. Pull:** Your state primarily affects **Push** routing (where tasks are assigned to you). You can still engage in **Pull** requests (picking from a list) regardless of your global state, provided you are logged in.

---

*New to the platform? Start with the [Agent Quick-Start Guide](../../Getting_Started/For_Agents/Agent-Quick-Start-Guide.md).*
