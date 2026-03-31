---
title: "Presence and State Technical Reference"
summary: "Detailed technical reference for the agentPresence event and the underlying state logic in the Agent Desk."
audience: [agent, developer]
product-area: [platform, sdk]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Presence and State Technical Reference

The **agentPresence** event is the heart of state management in ExpertFlow CX. It is emitted by the **Agent Manager** to synchronize an agent's status across all platform components.

## 1. The agentPresence Object
This object contains the complete state profile for an agent, including their identity, global state, and channel-specific availability.

### Key Payload Properties:
- **agent.id:** The system-generated UUID for the user.
- **state.name:** The agent's current Global State (`READY`, `NOT_READY`, `LOGOUT`).
- **state.reasonCode:** The ID of the reason code selected (if in `NOT_READY` or `LOGOUT` state).
- **agentMrdStates:** An array containing the individual states for every Media Routing Domain (MRD) assigned to the agent.
- **stateChangeTime:** The Unix timestamp of the last state transition.
- **action:**
    - `AGENT_STATE_UNCHANGED`: Emitted during periodic synchronization.
    - `AGENT_STATE_CHANGED`: Emitted when a manual or system-triggered state transition occurs.

## 2. Global vs. MRD States
An agent's availability is a layered logic:
1.  **Global State:** If the global state is `NOT_READY`, the agent cannot receive any "Push" tasks, regardless of their MRD settings.
2.  **MRD State:** If the global state is `READY`, the routing engine then checks the `agentMrdStates` array for individual channel availability.

### Example JSON Payload:
```json
{
  "agent": {
    "participantType": "CCUser",
    "id": "uuid-12345",
    "username": "amy_agent"
  },
  "state": {
    "name": "READY",
    "reasonCode": null
  },
  "agentMrdStates": [
    {
      "mrd": { "name": "VOICE", "maxRequests": 1 },
      "state": "NOT_READY"
    },
    {
      "mrd": { "name": "CHAT", "maxRequests": 5 },
      "state": "READY"
    }
  ]
}
```

## 3. Important Implementation Notes
- **Auto-Sync:** If enabled, changing the Global State to `READY` will automatically transition all compatible MRDs to `READY`.
- **System Transitions:** The state can be changed by the system (e.g., setting an agent to `BUSY` when their task limit is reached) or by a supervisor.
- **RONA:** If an agent fails to answer a task (Ring On No Answer), the system may automatically set their state to `NOT_READY`.

---

*For an operational guide on managing these states, see [Managing Your Presence and States](Managing-Your-Presence-and-States.md).*
