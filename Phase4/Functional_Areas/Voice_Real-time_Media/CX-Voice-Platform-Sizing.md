---
title: "CX Voice Platform Sizing"
summary: "Reference for CX Voice on-premise hardware requirements, deployment scenarios (baseline, AI-powered, WebRTC), SIP trunking, and high availability configurations."
audience: [solution-admin, decision-maker]
product-area: [voice]
doc-type: reference
difficulty: intermediate
keywords: ["CX Voice sizing", "voice platform hardware", "concurrent calls", "deployment scenarios", "high availability", "SIP trunking", "on-premise deployment", "media server"]
aliases: ["voice hardware requirements", "CX Voice deployment", "voice platform prerequisites"]
last-updated: 2026-03-10
---

# CX Voice Platform Sizing

This reference covers on-premise deployment options for the CX Voice Platform, including hardware requirements, deployment scenarios, SIP trunking considerations, and high availability configuration.

## Hardware Requirements

Size the Voice Platform based on the expected number of concurrent calls:

| Category | < 100 Concurrent Calls | < 300 Concurrent Calls | < 500 Concurrent Calls | > 1000 Concurrent Calls |
|---|---|---|---|---|
| **CPU** | 4 cores | 8 cores | 12 cores | 16 cores |
| **RAM** | 8 GB | 16 GB | 24 GB | 32 GB |
| **Storage** | 100 GB SSD | 200 GB SSD | 300 GB SSD | 500 GB SSD |

> These figures cover the Media Server component. CX Core Platform hardware is sized separately. See [Sizing Guidelines](../../Solution_Admin/Sizing-Guidelines.md).

## Software Prerequisites

- Operating System: **Debian 12+**

## Deployment Scenarios

### Scenario 1: Baseline Voice (CX Voice with Legacy IVR)

**Purpose**: Standard voice platform for inbound and outbound calls with DTMF IVR menus, queue announcements, conferencing, and voice recording.

**Required Components**:
- CX Core Platform (mandatory foundation for all CX Voice deployments)
- Media Server (handles RTP streams, IVR prompts, conferencing, and voice recording)

**Notes**:
- Voice Recording (VRS) is part of the Media Server — no additional server is required.
- This scenario does not support conversational AI or speech recognition.

---

### Scenario 2: AI-Powered Voice (Voicebots, Transcription, Translation)

**Purpose**: Advanced AI-driven voice experience with conversational IVR, voicebots, speech-to-text transcription, and text-to-speech responses.

**Required Components**:
- CX Core Platform
- Media Server
- Jambonz (SIP application server for AI integration)
- AI Engines

**Additional AI Services** (hardware/software prerequisites vary by provider):
- ASR — Automatic Speech Recognition
- NLU — Natural Language Understanding
- TTS — Text-to-Speech
- LLM / AI connectors (optional for advanced language use cases)

---

### Scenario 3: WebRTC Voice and Video

**Purpose**: Enables customers to make voice and video calls directly from web or mobile browsers without requiring a SIP hard phone or soft phone.

**Required Components**:
- CX Core Platform
- Media Server (handles RTP streams for voice and video)
- Customer Widget (provides the WebRTC client embedded in the browser or mobile app)

**Additional Considerations**:
- Requires TURN/STUN server configuration for NAT traversal.
- SIP trunking is still required if WebRTC calls need to connect to the PSTN.
- Validate bandwidth requirements in video-heavy deployments.

## Deployment Summary

| Deployment Type | Required Components | Notes |
|---|---|---|
| **Baseline Voice** | CX Core + Media Server | Includes legacy DTMF IVR and Voice Recording |
| **AI-Powered Voice** | CX Core + Media Server + Jambonz + AI Engines | Conversational IVR, voicebots, transcription/translation |
| **WebRTC Voice and Video** | CX Core + Media Server + Customer Widget | Browser-based calling; TURN/STUN required |
| **High Availability** | CX Core Cluster + Media Server HA + CX SIP Proxy HA | Redundancy and failover for mission-critical environments |

## SIP Trunking

CX Voice integrates with SIP trunks to connect with the PSTN or the customer's telephony provider.

| Option | Description |
|---|---|
| **Customer-provided SIP trunks** | Customer contracts with their own SIP provider; ExpertFlow integrates the trunk into CX Voice. |
| **ExpertFlow-provided SIP trunks** | Available in selected geographies. Confirm availability per deployment opportunity. |

When sizing `MAX_CONCURRENT_CALLS` in the CX Dialer, always confirm the maximum concurrent calls allowed by the SIP trunk with the provider. Exceeding trunk limits causes calls to get stuck. See [CX Dialer Reference](CX-Dialer-Reference.md).

## High Availability (HA)

For mission-critical deployments, CX Voice supports HA configurations:

| Component | HA Option |
|---|---|
| **CX Core** | Redundant application server cluster |
| **Media Server** | Active-passive or active-active clustering |
| **CX SIP Proxy (OpenSIPS)** | Load balancing and failover for SIP signalling |
| **Database** | Clustering for data consistency and failover |

## Related Articles

- [CX Voice Limitations](CX-Voice-Limitations.md)
- [CX Dialer Benchmarks](CX-Dialer-Benchmarks.md)
- [CX Dialer Reference](CX-Dialer-Reference.md)
- [Sizing Guidelines](../../Solution_Admin/Sizing-Guidelines.md)
- [Media Server Configuration CX Voice](../../Solution_Admin/Media-Server-Configuration-CX-Voice.md)
- [WebRTC to SIP](WebRTC-to-SIP.md)
