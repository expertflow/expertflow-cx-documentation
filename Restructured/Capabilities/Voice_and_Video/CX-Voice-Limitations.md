---
title: "CX Voice Limitations"
summary: "Reference listing known limitations of CX Voice, including feature-specific constraints, general edge cases, multichannel conflicts, failover scenarios, and routing issues."

product-area: [voice]
doc-type: reference
difficulty: intermediate
keywords: ["CX Voice limitations", "voice limitations", "failover limitations", "routing issues", "WebRTC limitations", "consult limitations", "known issues", "voice channel"]
aliases: ["voice known issues", "CX Voice known limitations", "voice channel limitations"]
last-updated: 2026-03-10
---

# CX Voice Limitations

This page documents known limitations of the CX Voice channel. Use this reference when evaluating whether CX Voice is suitable for a specific use case, when planning failover procedures, or when diagnosing unexpected behaviour.

## Prerequisites and Environment Requirements

- **Microphone permissions** must be enabled for the Agent Desk in the browser. Denying microphone access will prevent WebRTC audio.
- **Private browser windows** are not supported. The Agent Desk uses browser cache for state maintenance; private browsing clears this cache.
- **Failover** is not supported for Consult, Transfer, and Silent Monitoring features.

## Feature Limitations

| Feature | Limitation |
|---|---|
| **Consult** | Failover not supported. See Consult, Transfer and Conference documentation for details. |
| **Consult Transfer** | Failover not supported. |
| **Direct Agent Transfer** | Failover not supported. |
| **Manual Outbound Call** | See Manual Outbound Call documentation for limitations. |
| **Silent Monitoring** | Failover not supported. |

## General Edge Cases

| Issue | Description |
|---|---|
| **Concurrent login conflict** | If Agent1 is on an active call and another agent logs in with Agent1's credentials, the conversation gets stuck. `CCC-659` |
| **Incoming notification** | Optional note in notifications and requesting agent info is not available for CX Voice incoming requests. |
| **RONA** | CX RONA is not fully integrated with CX Voice (FreeSWITCH). The system leverages FreeSWITCH's native ringing timeout as the RONA mechanism instead. |
| **Hold disconnect error** | If a customer or agent ends a call while the customer is on hold, an "incorrect object for call" error appears on the Agent Desk and the agent's MRD state is set to Not-Ready. `CIM-15531` |
| **Immediate disconnect after reserve** | If a customer disconnects immediately after agent reservation, an "invalid action answerCall" error is thrown and the Voice MRD transitions to Not-Ready, preventing the agent from receiving further calls. `CIM-15904` |
| **Conversation stays open after call ends** | If a customer disconnects immediately after the agent accepts, the voice call ends but the conversation remains open and the MRD stays busy. The agent must manually close the conversation to free the MRD. `CIM-15881` |
| **Queue routing stuck after ringing timeout** | If the customer ends the call while it is ringing on the agent desk and that agent is the only one available, queued customers are not routed to the agent until the Voice MRD is toggled Off/On. `CIM-25994` |
| **"Topic Closed Already" MRD stuck** | When an agent changes their MRD to Ready while a customer ends the call or the agent refreshes, a "Topic Closed Already" error can cause the MRD to become stuck. The agent cannot change MRD state and must log out and log back in to resolve. `CIM-26651` |
| **Microphone removed during consult/transfer** | If microphone permission is revoked while a transfer or consult is in progress, the Voice MRD does not transition to PENDING_NOT_READY as expected. Instead it remains READY or shifts to NOT_READY incorrectly. `CIM-26797` |

## Multichannel Cases

| Issue | Description |
|---|---|
| **MRD mismatch** | The MRD of a queue must match the MRD of the corresponding channel type. A mismatch causes incorrect enqueuing and MRD state update failures. `CIM-13610` |
| **Voice queue + simultaneous web chat** | If a customer is in a voice queue and simultaneously starts a web chat, then leaves the voice call and presses "talk to agent" from the chat, the system incorrectly reports an agent was requested but the chat is not routed. `CIM-13309` |
| **Voice call + web chat concurrent routing** | If a customer with an active web chat also initiates a voice call, and the first agent does not answer, the voice call is not routed back to that agent once they become available — it goes to other agents instead. `CIM-14343` |

## Failover Scenarios

### Network Failure

| Scenario | Behaviour |
|---|---|
| Customer leaves during queue/named agent consult re-connection | Call ends on Agent Desk only after agent manually clicks End Call. A2 call ends cleanly. |
| Queue Transfer button clicked multiple times during network outage | No immediate error shown. When network restores, multiple "Queue Error" pop-ups appear corresponding to the number of clicks made during the outage. |
| VPN disconnect during consult/transfer (when Media Server requires VPN but EFCX does not) | SIPjs throws an error; the reserved agent remains stuck in reserved state until the main call ends and the conversation closes. |

### Refresh Cases

| Scenario | Behaviour |
|---|---|
| Agent refreshes during active call | Call ends for customer; a CALL LEG ENDED event is sent from the Agent Desk. |
| Agent refreshes during ringing | Multiple outcomes possible depending on network speed and timing: (1) FreeSWITCH detects USER_NOT_REGISTERED — customer gets a message and call ends cleanly; (2) FreeSWITCH detects NO_USER_RESPONSE — same clean result; (3) Refresh completes mid-transfer — agent's Voice MRD gets stuck on READY; music stops for customer; after 30 seconds RONA occurs but a second agent will not receive the call either. Manual close of the conversation by the customer is required to free Agent1. |

### Routing Engine Pod Failure

| Scenario | Behaviour |
|---|---|
| RE pod deleted while customer is interacting with IVR | Call gets stuck in queue after pressing 0. Does not route to available agents. Resolved only when customer ends the call. Normal routing resumes on the customer's next call. `CIM-26658` |
| RE pod restarted during agent reservation | Call connects in background without conversation view for the agent. `CIM-26659` |

### General Routing Issues

| Scenario | Behaviour |
|---|---|
| Customer ends call/chat during ringing when one agent is active | Next queued call/chat is not routed to the agent. `CIM-25994`, `CIM-12012` |
| Agent makes consult to own empty queue; customer chat enters that queue | Customer chat is not routed to the only available agent. `CIM-15948` |
| RONA timeout — agent delays setting MRD to Ready | If the agent changes Voice MRD to Ready within 3 seconds of RONA: call is re-routed to them. If the agent waits longer than 3 seconds: call is not routed to them even if they are the only agent. `CIM-14343` |

## Related Articles

- [Inbound Calls](Inbound-Calls.md)
- [Outbound Calls](Outbound-Calls.md)
- [Troubleshooting CX Voice](Troubleshooting-CX-Voice.md)
- [CTI Call Controls](CTI-Call-Controls.md)
- [CX Voice Platform Sizing](CX-Voice-Platform-Sizing.md)
- [Voice Channel Configuration Limitations](../../How-to_Guides/Administrator/Voice-Channel-Configuration-Limitations.md)
