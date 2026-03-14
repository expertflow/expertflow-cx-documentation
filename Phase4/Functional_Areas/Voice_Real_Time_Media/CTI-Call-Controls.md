---
title: "CTI Call Controls"
summary: "Reference for the CTI toolbar call controls available to agents in the Agent Desk during active CX Voice calls, including Answer, Hold, Resume, End, Mute, DTMF dialpad, and Consult/Transfer."
audience: [agent, supervisor]
product-area: [voice]
doc-type: reference
difficulty: beginner
keywords: ["CTI call controls", "CTI toolbar", "call controls", "hold call", "mute call", "DTMF dialpad", "consult transfer", "voice controls", "agent desk voice"]
aliases: ["call controls reference", "agent CTI toolbar", "voice call controls"]
last-updated: 2026-03-10
---

# CTI Call Controls

The **CTI toolbar** in the Agent Desk provides call control functions for managing active CX Voice interactions. The toolbar appears automatically when an agent answers an incoming call and can be repositioned or pinned to the conversation view.

## Toolbar Overview

When an agent answers a call, the CTI toolbar appears with a clear active call status indicator. The toolbar can be:
- **Floating**: Draggable to any position on the screen using the pop-out icon on the left.
- **Fixed**: Pinned to the right-hand side of the conversation view using the Minimise button.

## Call Controls Reference

| Control | Description |
|---|---|
| **Answer Call** | Accept an incoming call alert and connect to the customer. |
| **Mute / Unmute** | Toggle the agent's microphone on or off during an active call. The customer hears silence while muted. |
| **Hold / Resume** | Place the customer on hold (hold timer starts); click again to resume (hold timer stops). A single button toggles between the two states. |
| **End Call** | End the active call leg between the agent and the customer. |
| **DTMF Dialpad** | Send Dual-Tone Multi-Frequency tones during a call — for interacting with external IVR systems, conference bridges, or third-party telephony services. |
| **Consult / Conference** | Initiate a private consult call with another agent, escalate to a three-way conference, or perform a consult-transfer. |
| **Popout / Minimise** | Toggle the toolbar between a floating draggable view and a fixed panel on the conversation view side. |

## Control Details

### Answer Call

When an inbound call arrives, the agent sees an incoming call notification. Clicking **Accept** (or answering the physical/soft phone extension) triggers the CTI toolbar to appear with full call controls active.

### Hold and Resume

Placing a call on hold starts the hold timer. The customer hears hold music defined in the queue configuration. Clicking **Resume** reconnects the customer and stops the hold timer.

> One button toggles between Hold and Resume — the button label updates based on the current call state.

### DTMF Dialpad

The dialpad is available during active calls. Use it to:
- Navigate external IVR menus reached via transfer.
- Interact with conference bridge access codes.
- Send tone signals required by third-party telephony integrations.

The dialpad is accessible in both minimised and maximised toolbar views.

### Consult and Conference

| Action | Description |
|---|---|
| **Consult** | Place the current customer on hold and initiate a private call to another agent or queue. The original customer does not hear the consult conversation. |
| **Conference** | Add the consulted agent to the active call, creating a three-way conversation including the customer. |
| **Consult Transfer** | Transfer the customer to the consulted agent and disconnect from the call. |

> Failover is not supported for Consult and Consult Transfer. See [CX Voice Limitations](CX-Voice-Limitations.md).

## Known Limitations

- Consult, Consult Transfer, and Silent Monitoring are not supported in failover scenarios.
- WebRTC calls (browser-based) do not support Consult, Conference, or Transfer from the CTI toolbar. See [Handle WebRTC Calls](Handle-WebRTC-Calls.md).
- For additional open issues affecting call controls, refer to [CX Voice Limitations](CX-Voice-Limitations.md).

## Related Articles

- [Inbound Calls](Inbound-Calls.md)
- [Handle WebRTC Calls](Handle-WebRTC-Calls.md)
- [CX Voice Limitations](CX-Voice-Limitations.md)
- [Adding Agent Extensions for CX Voice](Adding-Agent-Extensions-CX-Voice.md)
- [Managing Your Presence and States](../../Agent/Managing-Your-Presence-and-States.md)
