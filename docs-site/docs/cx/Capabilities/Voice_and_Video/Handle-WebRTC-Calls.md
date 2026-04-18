---
title: "Handle WebRTC Calls"
summary: "How-to guide for agents handling customer-initiated WebRTC audio and video calls in the Agent Desk, including prerequisites, acceptance steps, call controls, and known limitations."

product-area: [voice, video]
doc-type: how-to
difficulty: beginner
keywords: ["handle WebRTC calls", "agent WebRTC", "accept audio call", "accept video call", "WebRTC agent guide", "call controls", "video call agent"]
aliases: ["agent WebRTC guide", "respond to WebRTC calls", "accept browser calls"]
last-updated: 2026-03-10
---

# Handle WebRTC Calls

This guide explains how to accept and manage customer-initiated WebRTC audio and video calls from the Agent Desk.

## Prerequisites

- Your **Global State** is set to **Ready**.
- Your **CX Voice MRD** state is set to **Ready**.
- **Browser microphone permission** is enabled for the Agent Desk. For video calls, **camera permission** must also be enabled.

> WebRTC calls are multichannel interactions — the customer's web session is always active alongside the audio or video call. You will see both the WEB and WebRTC sessions in the conversation view.

## Handling Audio Calls

### Accept an Incoming Audio Call

1. When a customer initiates a WebRTC audio call, an **incoming call notification** appears on your Agent Desk. The notification shows:
   - Customer details (name, if provided in the pre-chat form)
   - Channel type icon indicating the call is WebRTC/Web

2. Click **Accept** in the notification.

3. The conversation view opens with two active channel sessions: **WebRTC** (audio) and **WEB** (chat session). The Active Channels dropdown in the conversation view shows both.

4. Use the call controls to manage the interaction:
   - **Hold**: Place the customer on hold.
   - **Resume**: Return the customer from hold.
   - **End**: End the call.

5. When the call ends, the audio session closes. Note that the **wrap-up window does not appear** after a WebRTC audio call. You cannot submit wrap-up codes or notes for this interaction type.

## Handling Video Calls

### Accept an Incoming Video Call

1. When a customer initiates a WebRTC video call, an **incoming call notification** appears. The notification indicates the call is a video request via the channel type icon.

2. Click **Accept** in the notification.

3. The Agent Desk opens the video view:
   - **Main view**: Customer's video stream.
   - **Picture-in-picture**: Your local video stream.

4. The conversation view shows both the **WebRTC** (video) and **WEB** sessions as active.

5. Use the available call controls to manage the video interaction.

6. When either party ends the call, the video session closes. The WEB session may remain open if the customer is still connected through chat.

## Current Limitations for Agents

| Limitation | Impact |
|---|---|
| **Wrap-up codes not available** | After WebRTC audio calls end, there is no wrap-up window. You cannot log reason codes or notes for the interaction. |
| **No Consult, Conference, or Transfer** | You cannot consult another agent, create a conference, or transfer a WebRTC call to another agent or queue. |
| **No Silent Monitoring or Barge-in** | Supervisors cannot silently monitor or barge into your WebRTC calls. |
| **Video hold — black screen** | If you put a video call on hold and the customer stops/restarts their video, they will see a black screen. Advise customers to avoid toggling video while on hold. `CCC-1806` |
| **Call timer may freeze** | If you navigate away while the video call is in minimised mode, the call timer may freeze on the maximised view. The call itself continues normally. |

## Related Articles

- [WebRTC for CX](WebRTC-for-CX.md)
- [Browser-Based Calling](Browser-Based-Calling.md)
- [CTI Call Controls](CTI-Call-Controls.md)
- [Managing Your Presence and States](../../How-to_Guides/Agent/Managing-Your-Presence-and-States.md)
- [CX Voice Limitations](CX-Voice-Limitations.md)
