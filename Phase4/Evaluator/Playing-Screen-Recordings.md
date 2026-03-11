---
title: "Playing Screen Recordings in Quality Management"
summary: "How-to guide for quality evaluators and Quality Managers to access and play synchronized screen and audio recordings of agent-customer interactions in ExpertFlow CX — covering prerequisites, access steps, and troubleshooting."
audience: [evaluator, quality-manager, supervisor]
product-area: [voice]
doc-type: how-to
difficulty: intermediate
keywords: ["screen recording CX", "play screen recording QM", "synchronized recording CX", "video recording QM", "screen recording evaluator CX", "VRS screen recording", "quality management screen recording", "CX 4.10.5 screen recording"]
aliases: ["screen recording QM CX", "play video recording CX", "audio video QM CX"]
last-updated: 2026-03-10
---

# Playing Screen Recordings in Quality Management

Available from **CX 4.10.5** and **CX 5.1.0** onwards.

Screen recordings allow quality evaluators, supervisors, and compliance officers to review synchronized audio and agent screen recordings of interactions — providing full context for quality assessments, coaching, and compliance verification.

## Key Capabilities

| Capability | Description |
|---|---|
| **Synchronized playback** | Screen and audio recordings play with a unified, time-aligned timeline. |
| **Hold period handling** | Screen recording continues during hold periods; audio shows silence gaps for timeline alignment. |
| **Multi-monitor support** | Both agent screens are captured side-by-side in a single video file. |
| **Evaluator access** | Quality Managers access via **Conversation List**; Evaluators access via **Reviews**. |

## Prerequisites

Before screen recordings appear in Quality Management:

1. **VRS** (Voice Recording Solution) must have screen recording enabled and operational.
2. **QM Connector** must be configured to push screen recordings to CX.
3. **Agent workstations** must have screen recording permissions configured correctly per the deployment guide.

Contact your administrator to verify all three prerequisites are in place.

## Supported Call Types

Screen recording is currently available for:
- Simple **inbound** calls (first leg only)
- Simple **outbound** calls (first leg only)

**Not yet supported:**
- Consult calls
- Consult transfer calls
- Direct transfer calls
- Conference calls
- Subsequent legs after a transfer

## How to Play Screen Recordings

### Quality Manager Access

1. Log in to Unified Admin using your Quality Manager credentials.
2. Navigate to **Quality Management → Conversation List**.
3. Find the target conversation. If it has multiple legs, expand the conversation to view all legs.
4. For Cisco-handled calls, media icons appear per leg:
   - Click the **Video** icon to play synchronized screen + audio recording.
   - Click the **Audio** icon to play audio only.

### Evaluator Access

1. Log in to Unified Admin using your Evaluator credentials.
2. Navigate to **Quality Management → Reviews**.
3. Hover over an incomplete review and click **Start**.
4. If the conversation has multiple legs, expand to see all legs and media icons.
5. Click the **Video** icon for synchronized playback, or the **Audio** icon for audio only.

## Troubleshooting

| Issue | Possible Cause | Resolution |
|---|---|---|
| Video icon not visible | Call type not supported (transfer, consult, conference) | Screen recording is only available for simple inbound/outbound first-leg calls. |
| Video icon not visible | Screen recording not enabled | Contact your administrator to verify VRS screen recording is enabled. |
| Recording won't play | Browser compatibility issue | Use the latest version of Chrome or Firefox. Edge is not tested. |
| Audio/video out of sync | Known limitation | Minor drift may occur on long calls; will be improved in future releases. |

## Related Articles

- [Handle Voice Recordings](Handle-Voice-Recording.md)
- [Auditing and Scoring Conversations](Auditing-and-Scoring-Conversations.md)
- [As an Evaluator](As-an-Evaluator.md)
- [Compatibility Guide — Media Recording](Compatibility-Guide-Media-Recording.md)
