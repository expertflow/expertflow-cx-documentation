---
audience: [agent]
doc-type: reference
difficulty: beginner
aliases: []
---

# Agent and MRD States Reference

In Expertflow CX, your availability is managed through two layers: your **Global Agent State** and your specific **Media Routing Domain (MRD) States**.

## 1. Global Agent States
These represent your overall presence in the contact center.

- **LOGIN**: Your initial state upon entering the Agent Desk.
- **NOT_READY**: You are unavailable for all channels. You cannot set an MRD to "Ready" while in this state.
- **READY**: You are generally available and can now enable specific channel (MRD) availability.
- **LOGOUT**: You have signed out and are removed from all routing.

## 2. Media Routing Domain (MRD) States
These represent your availability for specific channels (e.g., Voice, Chat).

- **READY**: You are eligible to receive new requests for this specific channel.
- **RESERVED**: A request is currently being offered to you (ringing).
- **ACTIVE**: You are handling one or more interactions, but have not reached your maximum limit.
- **BUSY**: You have reached the maximum number of concurrent tasks allowed for this MRD.
- **PENDING_NOT_READY**: You have requested to go "Not Ready," but the system is waiting for you to finish your current active tasks. You will automatically transition to Not Ready once the tasks are closed.
- **INTERRUPTED**: You cannot accept new chats because you are currently handling a higher-priority interaction (usually a voice call).
- **LOGOUT**: The MRD state when you sign out of the system.
