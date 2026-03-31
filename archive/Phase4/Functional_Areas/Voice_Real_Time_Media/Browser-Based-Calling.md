---
title: "Browser-Based Calling"
summary: "Explanation of how browser-based calling works in ExpertFlow CX using WebRTC — covering the value proposition, how it differs from traditional telephony, use cases, and common questions."
audience: [decision-maker, solution-admin, supervisor]
product-area: [voice, video]
doc-type: explanation
difficulty: beginner
keywords: ["browser-based calling", "WebRTC", "click to call", "remote agents", "no softphone", "web calling", "voice in browser", "Opus codec"]
aliases: ["web calling overview", "WebRTC calling overview", "browser voice"]
last-updated: 2026-03-10
---

# Browser-Based Calling

Browser-based calling uses **WebRTC** technology to deliver HD voice and video communication directly through a web browser — without plugins, downloads, or hardware phones. It enables both agents to handle calls from any browser-equipped device and customers to reach support directly from your website.

## The Problem with Traditional Telephony

Most contact centres still rely on softphones or hardware phones for agent voice. This creates friction at multiple levels:

- **Deployment**: Remote agents need hardware phones shipped or VPN access to reach the softphone server.
- **IT overhead**: Codec conflicts, firewall rules, softphone installation failures, and device-specific issues consume IT resources.
- **Cost**: Hardware phones cost $100–300 per agent. Toll-free infrastructure adds to the bill.
- **Customer experience**: Customers must leave your website to find a phone number, losing all browsing context before they even reach an agent.

## How Browser-Based Calling Works

WebRTC (Web Real-Time Communication) is a browser-native technology supported by Chrome, Firefox, Safari, and Edge. It enables encrypted, real-time voice and video streams directly between a browser and the platform — without any additional software.

**For agents**: Agents log into the Agent Desk through their browser. Within seconds, they are ready to handle calls. All standard controls — Hold, Transfer, Conference, Mute — work as expected within the same interface.

**For customers**: A "Click to Call" or video call button on your website connects customers instantly to a waiting agent. No phone number to dial, no app to install.

**Behind the scenes**: ExpertFlow's WebRTC-to-SIP gateway handles bridging between the browser-based audio stream and your existing telephony infrastructure (Cisco CCE, CCX, CUCM, or any SIP provider).

## Key Benefits

| Audience | Benefit |
|---|---|
| **Operations** | Deploy remote agents in hours, not weeks — no hardware to ship or VPN to configure. |
| **IT** | Eliminate softphone installation and codec troubleshooting; the browser handles it. |
| **Finance** | Remove per-agent hardware costs; support Chromebooks and BYOD devices. |
| **Customers** | One-click access to support directly from your website, with context preserved. |

## Audio and Video Support

| Channel | Supported |
|---|---|
| Audio calls (browser-to-agent) | Yes |
| Video calls (browser-to-agent) | Yes |
| Screen sharing (agent-initiated) | Yes |
| Outbound campaigns via WebRTC | No — outbound dialing uses SIP-based CX Dialer |

WebRTC calls are always **multichannel** interactions: the web chat session initialises first, and the customer then escalates to audio or video from the customer widget.

## Security

WebRTC connections are encrypted by default — both the media streams (SRTP) and the signalling (DTLS). There is no mechanism to create an unencrypted WebRTC connection. This makes browser-based calling suitable for regulated environments including healthcare and financial services.

## Frequently Asked Questions

**Will call quality be good enough?**
WebRTC uses the Opus codec, which delivers excellent voice quality even on modest broadband connections. Quality meets or exceeds traditional hardware desk phones in typical deployments.

**Does it work with Cisco infrastructure?**
Yes. ExpertFlow CX integrates with Cisco CCE, CCX, and CUCM. Browser-based calling adds WebRTC capability alongside — not instead of — your existing investment.

**What happens if the agent's internet drops?**
The call drops, as it would with any VoIP solution. When connectivity returns, the agent refreshes their browser and is immediately back in service. No reconnection procedure is needed.

**Can we use Chromebooks?**
Yes. Chromebooks are fully supported. Browser-based calling enables low-cost agent workstations without any additional software.

## Common Use Cases

- Remote and hybrid agent deployments
- Rapid expansion to new contact centre locations
- Click-to-call from website pages
- Video customer support (technical troubleshooting, remote demos)
- BYOD contact centre environments
- Replacement of aging hardware phone infrastructure

## Related Articles

- [WebRTC for CX](WebRTC-for-CX.md)
- [Handle WebRTC Calls](Handle-WebRTC-Calls.md)
- [WebRTC to SIP](WebRTC-to-SIP.md)
- [Website Click-to-Call](Website-Click-to-Call.md)
- [Video Customer Support](Video-Customer-Support.md)
- [Voice and Video Overview](Voice-and-Video-Overview.md)
