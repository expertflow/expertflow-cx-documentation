---
title: "WebRTC for CX"
summary: "Explanation of WebRTC capabilities in ExpertFlow CX — covering how customers initiate audio and video calls through the customer widget, and known limitations."
audience: [solution-admin, agent, supervisor]
product-area: [voice, video]
doc-type: explanation
difficulty: beginner
keywords: ["WebRTC", "audio calls", "video calls", "customer widget", "browser calling", "WebRTC capabilities", "multichannel call"]
aliases: ["WebRTC capabilities", "customer WebRTC", "voice video from widget"]
last-updated: 2026-03-10
---

# WebRTC for CX

WebRTC functionality in ExpertFlow CX enables customers to initiate direct voice and video communication with agents from a standard web browser using the Customer Widget — no phone number required, no app to download.

## How WebRTC Calls Work

> **Important**: A WebRTC call is always a **multichannel** interaction. The web chat session is initiated first when the customer opens the Customer Widget. From within that web session, the customer can then escalate to an audio or video call.

### Audio Calls

Audio WebRTC calls allow customers to initiate a voice conversation with a business contact centre directly from the Customer Widget. The call can enter an IVR flow (traditional DTMF menu or conversational bot) and be routed to the appropriate agent based on the inquiry.

**Customer steps to initiate an audio call:**

1. Customer opens the Customer Widget on the website.
2. Customer fills in the pre-conversation form (name, topic, etc.) and clicks **Start Chat**.
3. After the bot welcome message appears, the customer sees two icons in the widget toolbar: one for text chat and one for a voice call.
4. **Browser microphone permission must be granted** before initiating the call. The browser will prompt for this permission if not already granted.
5. Customer clicks the call icon to initiate the audio call.
6. The call is routed through the platform IVR and then to a ready agent.

### Video Calls

Video WebRTC calls add a camera feed to the audio experience, enabling face-to-face support, remote demos, or visual troubleshooting.

**Customer steps to initiate a video call:**

1. Customer opens the Customer Widget and fills in the pre-conversation form, then clicks **Start Chat**.
2. After the bot welcome message, the customer sees two icons: one for text chat and one for video.
3. **Both browser microphone and camera permissions must be granted** before the call begins.
4. Customer clicks the video icon to initiate the video call.
5. The call is routed to an agent who accepts from the Agent Desk. Both parties' video streams appear: the remote video as the main view and the local stream as a picture-in-picture.

## Agent-Side Experience

When a customer initiates a WebRTC call, the agent receives an incoming call notification in the Agent Desk. The agent must be in **Global State: Ready** and **CX Voice MRD: Ready** to receive the call.

- The conversation view opens showing the **WebRTC** and **WEB** sessions both active.
- For audio calls: call controls (Answer, Hold, Resume, End) appear in the interface.
- For video calls: the customer's video stream appears as the main view; the agent's local video stream appears as a small overlay.

See [Handle WebRTC Calls](Handle-WebRTC-Calls.md) for the full agent guide.

## Known Limitations

| Limitation | Details |
|---|---|
| **Wrap-up not available after audio calls** | The wrap-up window does not appear when a WebRTC audio call ends. Agents cannot submit wrap-up codes or notes for WebRTC audio interactions. |
| **Silent Monitoring and Barge-in not supported** | Supervisors cannot monitor or join active WebRTC conversations. |
| **Consult, Conference, and Transfer not supported** | Assistance controls for WebRTC calls are not currently available. |
| **Video hold — black screen issue** | If the agent puts a video call on hold and the customer stops and restarts their video, the customer sees a black screen instead of the remote video feed. `CCC-1806` |
| **Camera permission removed mid-call** | If camera permission is revoked during an active video call: both parties' video stops, voice continues, and a console error is logged without UI feedback. Granting permission again does not auto-resume video — the user must click the camera icon twice. |
| **Call timer freeze on maximised view** | The call timer freezes on the maximised Agent Desk view when navigating away during a WebRTC video call in minimised mode. |

## Related Articles

- [Browser-Based Calling](Browser-Based-Calling.md)
- [Handle WebRTC Calls](Handle-WebRTC-Calls.md)
- [WebRTC to SIP](WebRTC-to-SIP.md)
- [Website Click-to-Call](Website-Click-to-Call.md)
- [Video Customer Support](Video-Customer-Support.md)
- [Customer Widget Features and Capabilities](../../Solution_Admin/Customer-Widget-Features-Capabilities.md)
