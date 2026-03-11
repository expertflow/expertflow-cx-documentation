---
title: "WebRTC to SIP Gateway"
summary: "Reference for the ExpertFlow WebRTC-to-SIP gateway — covering communication flow, hardware and software prerequisites, port requirements, and integration with Cisco CUBE."
audience: [solution-admin, developer]
product-area: [voice, video]
doc-type: reference
difficulty: advanced
keywords: ["WebRTC to SIP", "WebRTC SIP gateway", "Cisco CUBE", "SIP TLS", "WebRTC gateway", "port requirements", "SIPREC", "video gateway"]
aliases: ["WebRTC SIP bridge", "WebRTC gateway reference", "WebRTC to Cisco"]
last-updated: 2026-03-10
---

# WebRTC to SIP Gateway

The **ExpertFlow WebRTC-to-SIP Gateway** bridges browser-based WebRTC audio/video calls to SIP-based telephony infrastructure. It enables web users to initiate calls to Cisco Contact Center agents (CCX or CCE) during a web chat session without installing any software.

## Communication Flow

1. A web user initiates an audio or video call from their browser during a web chat session.
2. The browser requests microphone (and optionally camera) permission from the user.
3. Upon permission grant, the WebRTC media stream is established from the browser to the EF WebRTC Server.
4. The WebRTC Server converts the browser call to a SIP call.
5. The SIP call is routed to Cisco CUBE (or another SIP gateway), which handles the onward routing to the Cisco Contact Center.

**Encryption**: The connection from the customer's browser to the WebRTC Server is encrypted via WebRTC (DTLS/SRTP). The SIP leg from the WebRTC Server to Cisco CUBE uses SIP with TLS.

## Hardware Requirements

These requirements cover deployments of up to 50 concurrent agents:

| Component | Minimum Requirement |
|---|---|
| **CPU** | 8 cores |
| **RAM** | 8 GB |
| **Disk** | 250 GB |

## Software Requirements

| Component | Requirement |
|---|---|
| **Operating System** | Debian 10+ |
| **Node.js** | Latest stable version |
| **TLS Certificate** | Certificate from a valid signing authority or domain-signed certificate (required for HTTPS) |

## Port Requirements

### Public-Facing Ports (Customer Browser to WebRTC Server)

| Source | Destination | Destination Port | Protocol | Description |
|---|---|---|---|---|
| Web Audio/Video Call | WebRTC Server | 7443 | WSS | WebRTC WebSocket Secure |
| Web Audio/Video Call | WebRTC Server | 8021 | TCP | ESL (Event Socket Layer) |
| Web Audio/Video Call | WebRTC Server | 3000 | HTTPS | Application API |

### WebRTC Server to Cisco CUBE

| Port | Protocol | Application Protocol | Destination |
|---|---|---|---|
| 1719 | UDP | H.323 Gatekeeper RAS | Cisco CUBE |
| 1720 | TCP | H.323 Call Signalling | Cisco CUBE |
| 2855–2856 | TCP | MSRP | Cisco CUBE |
| 3478 | UDP | STUN service | Cisco CUBE |
| 3479 | UDP | STUN service | Cisco CUBE |
| 5002 | TCP | MLP protocol server | — |
| 5003 | UDP | Neighbourhood service | — |
| 5060 | UDP/TCP | SIP UAS | Cisco CUBE |
| 5066 | TCP | WebSocket | — |
| 5070 | UDP/TCP | SIP UAS | — |
| 5080 | UDP/TCP | SIP UAS | Cisco CUBE |
| 7443 | TCP | WebSocket Secure | — |
| 8021 | TCP | ESL | — |
| 8081–8082 | TCP | WebSocket | — |
| 16384–32768 | UDP | RTP/RTCP (media streaming) | Cisco CUBE |

## Website Integration

ExpertFlow provides a JavaScript/HTML snippet that the website owner embeds in the website header to enable click-to-call from web pages. A sample HTML reference page is also provided to guide development teams on implementation.

The website must have **HTTPS enabled** — WebRTC requires a secure browsing context and will not function over HTTP.

## Supported Video Codecs

The WebRTC-to-SIP gateway supports the following video codecs for passthrough:
- H.261 (passthru via `mod_h26x`)
- H.263 (passthru via `mod_h26x`)
- H.263+ (passthru via `mod_h26x`)
- H.263++ (passthru via `mod_h26x`)
- H.264 (passthru via `mod_h26x`)

## Related Articles

- [Browser-Based Calling](Browser-Based-Calling.md)
- [WebRTC for CX](WebRTC-for-CX.md)
- [Website Click-to-Call](Website-Click-to-Call.md)
- [Video Customer Support](Video-Customer-Support.md)
- [CX Voice Platform Sizing](CX-Voice-Platform-Sizing.md)
- [Cisco Voice Channel Configuration](../../Integrator/Cisco-Voice-Channel-Configuration.md)
