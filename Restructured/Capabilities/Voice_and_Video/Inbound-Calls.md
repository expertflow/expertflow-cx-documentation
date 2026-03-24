---
title: "Inbound Calls"
summary: "How-to guide for understanding and managing the inbound call flow in ExpertFlow CX — from IVR routing through queue assignment to agent handling and wrap-up."

product-area: [voice]
doc-type: how-to
difficulty: intermediate
keywords: ["inbound calls", "inbound routing", "IVR", "queue", "skills-based routing", "voice routing", "call flow", "CX Voice"]
aliases: ["inbound call routing", "incoming calls", "inbound voice flow"]
last-updated: 2026-03-10
---

# Inbound Calls

This guide explains how inbound calls flow through ExpertFlow CX from the moment a customer dials your number to the point the agent wraps up. Understanding this flow helps you configure routing correctly and diagnose issues when calls are not reaching the right agents.

## Prerequisites

- CX Voice channel is configured and SIP trunk or CUCM integration is active.
- At least one queue and one MRD (Media Routing Domain) is configured for voice.
- Agents are assigned to the queue and their extensions are registered.

## Inbound Call Flow

### Step 1: Customer Dials the Number

The customer dials a DNIS (Dialled Number Identification Service) number. The call arrives at the platform through the configured SIP trunk or CUCM integration.

### Step 2: IVR Processing

The call enters the IVR (Interactive Voice Response) flow associated with that DNIS. The IVR can:
- Play prompts and collect DTMF input (touch-tone keypad responses)
- Route calls to different queues based on customer input (e.g., "Press 1 for Sales, Press 2 for Support")
- Perform data dips (API calls to external systems to retrieve caller information before routing)
- Announce estimated wait time and offer callback options

### Step 3: Queue Assignment

Based on IVR logic, the call is placed in the appropriate queue. The queue applies:
- **Priority rules**: High-priority customers or queues can skip ahead.
- **Overflow rules**: If the primary queue is full or wait time exceeds a threshold, the call is routed to an overflow queue or transferred out.
- **Business calendar checks**: Calls arriving outside of business hours follow the after-hours routing defined in the queue configuration.

### Step 4: Skills-Based Routing

The routing engine selects an available agent based on:
- Agent skills matching the requirements tagged in the IVR flow
- Agent availability state (must be in a Ready state to receive calls)
- Longest-idle selection within matching agents

If no agent is available, the call waits in queue. Queue position announcements can be played at configurable intervals.

### Step 5: Agent Ring and Answer

When an agent is selected, the platform rings the agent's registered extension. The agent sees the incoming call in their Agent Desk with:
- Queue name and wait time
- Customer phone number (ANI — Automatic Number Identification)
- Any data retrieved during the IVR data dip (e.g., customer name, account number)

The agent clicks **Answer** (or answers their physical/soft phone) to accept the call.

### Step 6: Active Call Handling

During the call, agents have access to:
- **Hold / Resume**: Place the customer on hold while consulting internally.
- **Consult**: Initiate a private call to another agent or supervisor.
- **Transfer**: Blind transfer (immediate handoff) or consultative transfer (speak to the destination first).
- **DTMF dialpad**: Send tones to IVR systems during the call (e.g., for conference bridges or third-party systems).

### Step 7: Wrap-up

When the call ends, the agent enters wrap-up state. During wrap-up, the agent:
- Selects a wrap-up reason (e.g., "Resolved", "Escalated", "Follow-up Required")
- Adds notes if configured
- Completes any post-call tasks

Wrap-up duration is configurable per queue. When wrap-up is complete, the agent's availability state returns to Ready and they can receive the next call.

## Call Transfer Options

| Transfer Type | Description |
|---|---|
| **Blind Transfer** | Immediately routes the call to the destination. The transferring agent disconnects. |
| **Consultative Transfer** | The agent speaks with the destination before completing the transfer. Customer is on hold during consultation. |
| **Transfer to Queue** | Returns the call to a different queue for re-routing. |
| **Transfer to External** | Routes the call to an external PSTN number via SIP trunk. |

## Troubleshooting Common Issues

| Symptom | Likely Cause | Action |
|---|---|---|
| Call not reaching queue | DNIS not mapped to IVR flow | Verify DNIS mapping in Voice Channel configuration |
| Agent not receiving ring | Extension not registered | Check agent extension configuration in Keycloak |
| Long queue wait despite available agents | Agent state not set to Ready | Verify agent presence state in Agent Desk |
| Call drops during hold | SIP session timeout | Check SIP timer configuration on your trunk |

## Related Articles

- [Outbound Calls](Outbound-Calls.md)
- [CTI Call Controls](CTI-Call-Controls.md)
- [Adding Agent Extensions for CX Voice](Adding-Agent-Extensions-CX-Voice.md)
- [CX Voice Limitations](CX-Voice-Limitations.md)
- [Troubleshooting CX Voice](Troubleshooting-CX-Voice.md)
- [Media Routing Domains (MRD) Overview](../../How-to_Guides/Administrator/Media-Routing-Domains-MRD-Overview.md)
