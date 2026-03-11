---
title: "Voice and Video Overview"
summary: "Explanation of ExpertFlow CX voice and video channel types, capabilities, and architecture — covering both SIP-based telephony and browser-based WebRTC calling."
audience: [decision-maker, solution-admin, supervisor]
product-area: [voice, video]
doc-type: explanation
difficulty: beginner
keywords: ["voice channel", "video channel", "WebRTC", "SIP", "CX Voice", "browser-based calling", "voice overview", "video support"]
aliases: ["voice and video capabilities", "CX voice overview", "voice channel overview"]
last-updated: 2026-03-10
---

# Voice and Video Overview

ExpertFlow CX supports two distinct channel types for real-time audio and video communication with customers: **CX Voice** (SIP-based telephony) and **WebRTC** (browser-based calling). Both are unified under the same agent desk and routing engine, but they differ in infrastructure, deployment requirements, and use cases.

## Channel Types

### CX Voice

CX Voice is the platform's SIP-based telephony channel. It integrates with your existing telephony infrastructure — including Cisco Unified Communications Manager (CUCM), CX SIP Proxy, or third-party SIP trunks — and routes inbound and outbound calls through the platform's Media Routing Domain (MRD) framework.

CX Voice is suited for contact centres that:
- Already operate SIP-based telephony infrastructure
- Require compliance recording with court-admissible audio
- Need to support agent extensions on physical or soft phones
- Run high-volume outbound dialing campaigns

### WebRTC (Browser-Based Calling)

WebRTC enables customers to initiate audio or video calls directly from a web browser — no app download or phone line required. The call connects through the platform's WebRTC-to-SIP gateway and is routed to an agent in the same way as any other inbound task.

WebRTC is suited for:
- Digital-first customer journeys where customers are already on your website
- Video support use cases (screen sharing, visual troubleshooting)
- Click-to-call and chat-to-call escalation flows

## Architecture Overview

```
Customer (Browser / Phone)
         │
         ▼
  [WebRTC Gateway / SIP Trunk]
         │
         ▼
  [CX Voice Media Server]
         │
         ▼
  [Routing Engine → Queue → Agent Desk]
```

Both channel types terminate at the agent desk. The agent experience is consistent — audio controls, call recording, wrap-up, and transfer functions behave the same regardless of whether the call originated from a SIP line or a browser.

## Capabilities by Channel Type

| Capability | CX Voice (SIP) | WebRTC |
|---|---|---|
| Inbound calls | Yes | Yes |
| Outbound calls | Yes | No (link-based only) |
| Outbound campaigns (Dialer) | Yes | No |
| Video calls | No | Yes |
| Call recording | Yes | Yes (audio only) |
| Call forking | Yes | No |
| Agent extensions (hard/soft phone) | Yes | No |
| No additional infrastructure | No | Yes (browser native) |
| Screen sharing | No | Yes |

## Voice and Video in the Contact Centre

From a routing perspective, voice and video tasks follow the same lifecycle as digital interactions: they are created as CIM (Customer Interaction Management) objects, assigned to queues, routed to agents based on skills and availability, and closed with a wrap-up reason.

Supervisors monitor voice and video interactions through the same real-time dashboards used for digital channels. Historical reporting for voice is available in the [Connected Calls Detail Report](Connected-Calls-Detail-Report.md) and the [WebRTC Summary Report](../Performance_Insights_Data/WebRTC-Summary-Report.md).

## Related Articles

- [Inbound Calls](Inbound-Calls.md)
- [Outbound Calls](Outbound-Calls.md)
- [Browser-Based Calling](Browser-Based-Calling.md)
- [WebRTC for CX](WebRTC-for-CX.md)
- [Video Customer Support](Video-Customer-Support.md)
- [CX Voice Limitations](CX-Voice-Limitations.md)
- [Web App Calls Overview](../../Solution_Admin/Web-App-Calls-Overview.md)
