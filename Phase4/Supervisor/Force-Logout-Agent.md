---
title: "Force Logout Agent"
summary: "How-to reference for supervisors force-logging out agents in ExpertFlow CX — covering the impact on ongoing conversations in each agent state including normal chat, consult, conference, and silent monitoring scenarios."
audience: [supervisor]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["force logout agent", "forced logout supervisor", "FORCED_LOGOUT_BY_SUPERVISOR", "supervisor agent logout", "agent logout CX", "force remove agent"]
aliases: ["forced agent logout", "supervisor logout agent", "remove agent from CX"]
last-updated: 2026-03-10
---

# Force Logout Agent

Supervisors can force-log out any agent regardless of their current state — including Ready, Not Ready, Active, Busy, in Consult, or in Conference. The Force Logout action is available from the **Available Agents Detail Dashboard** in the Supervisor interface.

Logged-out agents receive the reason code **FORCED_LOGOUT_BY_SUPERVISOR**.

---

## Impact by Agent State

### Ready or Not Ready (No Active Conversation)

The agent is immediately logged out with reason code `FORCED_LOGOUT_BY_SUPERVISOR`. No impact on any conversation.

### Active — Normal Chat (Customer + Agent A)

- All of Agent A's active chats are **re-routed to the same queue with Highest Priority (11)**.
- Agent A is logged out with reason code `FORCED_LOGOUT_BY_SUPERVISOR`.

### Consult (Customer + Agent A Primary + Agent B Secondary)

**Logout request for Agent A (Primary):**
- Agent A is logged out with reason code `FORCED_LOGOUT_BY_SUPERVISOR`.
- Agent B is automatically removed from the conversation.
- The conversation is re-routed to the same queue with Highest Priority (11).

**Logout request for Agent B (Secondary/Consulted):**
- Agent B is logged out with reason code `FORCED_LOGOUT_BY_SUPERVISOR`.
- Agent A receives a notification: _"Agent B left the conversation."_
- No impact on the current conversation — it continues with Agent A.

### Conference (Customer + Agent A + Agent B, both Primary)

- The agent receiving the logout request is logged out with `FORCED_LOGOUT_BY_SUPERVISOR`.
- The remaining agent receives a notification that the other agent has left.
- No impact on the current conversation — it continues with the remaining agent.

### Conference with Supervisor Monitoring (Customer + Agent A + Supervisor X)

**Supervisor X in Silent Monitoring mode:**
- Agent A is logged out with `FORCED_LOGOUT_BY_SUPERVISOR`.
- Supervisor X is automatically removed from the conversation.
- The conversation is re-routed to the same queue with Highest Priority (11).

**Supervisor X in Whisper mode:**
- Agent A is logged out with `FORCED_LOGOUT_BY_SUPERVISOR`.
- Supervisor X is automatically removed from the conversation.
- The conversation is re-routed to the same queue with Highest Priority (11).

**Supervisor X in Barge-in mode:**
- Agent A is logged out with `FORCED_LOGOUT_BY_SUPERVISOR`.
- Supervisor X remains in the conversation and can continue handling the customer directly.

---

## Key Behaviour Summary

| Scenario | Conversation Outcome |
|---|---|
| Ready/Not Ready agent | No conversation impact |
| Active in normal chat | Conversation re-routed to queue at Highest Priority |
| Primary agent in Consult | Secondary removed; conversation re-routed |
| Secondary agent in Consult | Primary continues; no conversation impact |
| Conference participant | Other agent continues; no conversation impact |
| Primary agent, Supervisor in Silent/Whisper mode | Supervisor removed; conversation re-routed |
| Primary agent, Supervisor in Barge-in mode | Supervisor takes over conversation |

---

## Related Articles

- [Silent Monitoring](Silent-Monitoring.md)
- [Barge-in and Intervention](Barge-in-and-Intervention.md)
- [Managing Teams and Members](Managing-Teams-and-Members.md)
- [Monitoring Your Team in Real Time](../Getting_Started/Monitoring-Your-Team-in-Real-Time.md)
