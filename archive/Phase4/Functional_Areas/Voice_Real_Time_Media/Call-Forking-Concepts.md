---
title: "Call Forking Concepts"
summary: "Explanation of call forking in ExpertFlow CX — how a single incoming call is split into parallel sessions to simultaneously serve voice biometrics, agent assist, and call recording use cases."
audience: [solution-admin, developer, decision-maker]
product-area: [voice]
doc-type: explanation
difficulty: intermediate
keywords: ["call forking", "SIPREC", "voice biometrics", "agent assist", "call recording", "parallel call processing", "media server", "CX Voice"]
aliases: ["call forking overview", "SIPREC forking", "parallel call sessions"]
last-updated: 2026-03-10
---

# Call Forking Concepts

**Call forking** is the process of splitting a single incoming call into multiple parallel sessions and routing each copy to a different destination simultaneously. In ExpertFlow CX, call forking enables the Media Server to serve multiple real-time services from a single customer call — such as live transcription, biometric authentication, and call recording — without interrupting the conversation.

## How Call Forking Works

When a call is received by the CX Media Server, it can be forked into duplicate copies. Each copy is independently routed to a different endpoint or application, where it is processed in parallel.

**Call forking process:**

1. **Incoming call**: The customer's call arrives at the CX Media Server as a media stream.
2. **Duplication**: The system creates identical copies of the call's audio stream.
3. **Routing to endpoints**: Each copy is routed to a separate destination (e.g., recording server, AI engine, biometrics service).
4. **Parallel processing**: All downstream systems receive and process the call simultaneously without any copy affecting the others.

## Media Stream Sources

The CX Media Server can receive the media stream via SIPREC (Session Recording Protocol) from:
- A third-party gateway such as Cisco CUBE
- CX SIP Proxy
- Forking at the phone level (e.g., Cisco Built-in Bridge — BIB)

## Use Cases

### 1. Voice Biometrics and Authentication

The original call is sent to an IVR for user authentication, while a forked copy is simultaneously directed to a voice biometrics engine. The engine verifies the caller's identity in real time based on their voice pattern — without adding any delay to the primary IVR interaction.

### 2. Agent Assist and Transcription

A copy of the call is sent to a Voice AI service that:
- Transcribes the conversation in real time
- Translates speech (for multilingual support scenarios)
- Provides suggestions or next-best-action prompts to the agent on their Agent Desk

The agent receives live AI assistance during the call without the customer being aware of the parallel processing.

### 3. Recording and Quality Monitoring

One copy of the call leg is routed to the recording server (VRS — Voice Recording System) for storage. The recording is captured in parallel to the live conversation, enabling quality management review, compliance auditing, and dispute resolution without impacting call quality.

## Architecture Context

```
Customer Call
     │
     ▼
CX Media Server (SIPREC from CUBE / SIP Proxy / BIB)
     │
     ├──► Recording Server (VRS) — for QM and compliance
     ├──► Voice AI Engine — for transcription / agent assist
     └──► Voice Biometrics Engine — for caller authentication
```

Each fork operates independently. A failure or latency in one fork does not affect the others or the primary call.

## Related Articles

- [Voice and Video Overview](Voice-and-Video-Overview.md)
- [Inbound Calls](Inbound-Calls.md)
- [Media Server Configuration CX Voice](../../Solution_Admin/Media-Server-Configuration-CX-Voice.md)
- [Media Server Azure Transcription Setup](../../Solution_Admin/Media-Server-Azure-Transcription-Setup.md)
- [Media Server Google Transcription Setup](../../Solution_Admin/Media-Server-Google-Transcription-Setup.md)
