---
title: "Video Customer Support"
summary: "Explanation of video customer support capabilities in ExpertFlow CX — covering use cases by industry, the agent and customer experience, technical requirements, security and compliance, and adoption guidance."

product-area: [video, voice]
doc-type: explanation
difficulty: beginner
keywords: ["video customer support", "video calls", "WebRTC video", "face to face support", "video use cases", "browser video", "telemedicine", "insurance video"]
aliases: ["video support", "video contact center", "face to face support"]
last-updated: 2026-03-10
---

# Video Customer Support

Video customer support adds face-to-face interaction to your contact centre without requiring customers to install apps, download software, or use a separate platform. Customers click a button in their browser, grant camera and microphone permission, and are connected to an agent — all within your website.

## When Video Makes Sense

Not every interaction benefits from video. Voice and chat handle most routine inquiries efficiently. Video provides the most value in the following scenarios:

| Use Case | Why Video Helps |
|---|---|
| **Technical troubleshooting** | Customers show the issue directly rather than describing it — eliminates back-and-forth, reduces resolution time |
| **Product demonstrations** | Showing how something works is more effective than describing it |
| **Personalized advisory services** | Industries where trust matters (banking, insurance, healthcare) benefit from face-to-face even when in-person isn't practical |
| **Visual verification** | Claims (show us the damage), document checks, product issues — situations where seeing is deciding |
| **High-value customer retention** | Personal video attention changes the outcome when a valuable customer is considering leaving |

## Industry Use Cases

**Insurance**: Claims processing with real-time damage assessment; policy sales with document walkthroughs; visual identity verification for sensitive account changes.

**Financial services**: Wealth management portfolio reviews with screen sharing; mortgage applications with document guidance; fraud resolution through video verification.

**Healthcare**: Telemedicine consultations for non-emergency conditions; patient education on device use; mental health sessions requiring a personal connection.

**Technical support**: Device setup where customers show the problem; software support where agents see errors directly; complex installation walkthroughs.

**Retail and e-commerce**: Personal shopping with live product demonstrations; virtual fitting assistance; detailed consultation on complex purchases.

## Customer Experience

1. Customer visits a support page or clicks a video support button.
2. The browser requests camera and microphone permission (one-time prompt per browser).
3. Within seconds, the customer is connected to an agent.
4. The video window shows the agent (if agent has video enabled) and the customer's own feed.
5. If the agent needs to see the customer's screen, the browser prompts for screen share permission — the customer selects which screen or window to share and retains control at all times.
6. Privacy is always customer-controlled: they can disable video, end screen sharing, or drop to audio-only at any point.

## Agent Experience

Agents handle video calls through the same Agent Desk they use for voice — no separate interface or application.

On an incoming video call, agents see an incoming request notification. On acceptance:
- The customer's video stream appears as the main view.
- The agent's local video stream appears as a picture-in-picture overlay.
- Standard call controls (Hold, Mute, End) are available.
- The agent has full access to CRM data and knowledge base tools alongside the video view.

Wrap-up, conversation notes, and quality review work the same way as for voice calls.

## Security and Compliance

WebRTC video connections are encrypted end-to-end by default. Media streams are transmitted over SRTP; signalling uses DTLS. There is no mechanism to create an unencrypted WebRTC connection.

| Compliance Area | Consideration |
|---|---|
| **HIPAA** | Browser-based video meets HIPAA requirements when properly configured. No PHI is stored on the customer's device. Recording and retention occur on your compliant infrastructure. |
| **PCI-DSS** | Payment card data should never be shown on video. Guide customers to enter sensitive data through secure form fields, not on camera. |
| **Financial services (KYC)** | Video identity verification is increasingly accepted for Know Your Customer requirements, particularly when combined with document verification. |
| **Data residency** | You control where video traffic is processed and recorded, which matters for regions with strict data localisation requirements. |

## Recording and Quality Management

Video calls can be recorded alongside voice calls, capturing both audio and video streams. Quality managers can:
- Review agent presentation and professionalism.
- Verify that visual information was correctly interpreted.
- Identify training opportunities specific to video interactions.
- Ensure compliance with visual verification procedures.

Video recordings are stored in the same recording infrastructure as voice. Retention policies, access controls, and QM workflows are the same. Note that video recordings require more storage than voice — approximately 5–10× more per minute of interaction.

## Technical Requirements

| For Customers | For Agents |
|---|---|
| Modern browser (Chrome, Firefox, Edge, Safari) | Same as customers, plus: |
| Webcam (built-in laptop camera is sufficient) | USB webcam recommended for better quality |
| 2–3 Mbps broadband internet | Headset for better audio quality |
| Microphone (built-in or headset) | Professional or virtual background |

No apps, accounts, or special configuration are required on the customer side.

**Network**: Video uses approximately 2–3 Mbps per call, compared to ~100 kbps for voice. For contact centres with significant video volume, factor this into internet capacity planning. Video quality automatically adjusts downward on slower connections while preserving audio.

## Adoption Approach

| Phase | Action |
|---|---|
| **Pilot** | Start with 1–2 use cases where video clearly reduces resolution time or increases satisfaction. Train a small agent group. |
| **Expand** | Based on pilot results, identify additional teams and scenarios where video adds measurable value. Not every team needs video. |
| **Market** | Once agents are comfortable and processes are refined, promote video support on your website and in customer communications. |
| **Measure and optimise** | Track first-contact resolution, handle time, and CSAT for video vs voice. Optimise routing, staffing, and training based on results. |

## Related Articles

- [WebRTC for CX](WebRTC-for-CX.md)
- [Handle WebRTC Calls](Handle-WebRTC-Calls.md)
- [Website Click-to-Call](Website-Click-to-Call.md)
- [Browser-Based Calling](Browser-Based-Calling.md)
- [Voice and Video Overview](Voice-and-Video-Overview.md)
- [Customer Widget](../Digital_Channels/Customer-Widget-Features-Capabilities.md)
