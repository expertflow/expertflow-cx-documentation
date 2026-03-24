---
title: "Handle Voice Recordings"
summary: "How-to guide for agents and evaluators accessing, playing, and navigating call recordings in ExpertFlow CX — covering the recording player controls, seek bar, per-leg recording structure, and permissions."
audience: [supervisor-qa]
product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["voice recording CX", "call recording playback", "handle voice recording", "call recording agent desk", "seek bar recording", "play call recording", "recording player CX", "interaction history recording"]
aliases: ["play call recording", "voice recording playback CX", "call recording agent"]
last-updated: 2026-03-10
---

# Handle Voice Recordings

Call recordings in ExpertFlow CX are accessible from the **Customer Interaction History** in the Conversation View. Each call leg has its own recording, accessible based on the user's permissions. Recordings can be played back with full seeking and navigation controls.

## Accessing a Recording

1. Open the **Customer Interaction History** for a conversation.
2. Navigate to the **Voice Activities** section.
3. Each call leg displays a separate **Play** button.
4. Click the **Play** button for the recording you want to review.

The recording player opens as a **floating player** that stays visible while you navigate to other screens. The player remains active until you explicitly close it.

## Recording Player Controls

| Control | Description |
|---|---|
| **Play / Pause** | Start or pause playback. |
| **Seek bar** | Click or drag to jump to any timestamp in the recording. |
| **Mute / Unmute** | Toggle audio on or off. |
| **Close** | Close the floating player and stop playback. |

The seek bar also displays:
- **Total recording duration**
- **Current playback position**

Tooltips are shown on all player controls for clarity.

## Per-Leg Recording Structure

Each recording corresponds to a specific **call leg**. In multi-agent conversations (consult, conference), each agent's leg has its own recording. You can play each leg independently to review different parts of the call.

## Permissions

Access to specific call recordings depends on the user's role and permissions configured in Keycloak. Not all users may have access to all call legs. Contact your administrator if a recording is expected but not visible.

## Limitations for Cisco-Integrated Environments

When CX is integrated with Cisco contact center (Eleveo recordings), specific limitations apply to recording access and playback. Refer to the Cisco integration documentation for details.

## Related Articles

- [As an Evaluator](../../Getting_Started/For_Supervisors_and_QA_Leads/Evaluator-Guide.md)
- [Conversation View](../../Capabilities/Digital_Channels/Conversation-View.md)
- [Voice Recording and Compliance Features](../../Platform_Overview/Voice-Recording-and-Compliance-Features.md)
- [Auditing and Scoring Conversations](Auditing-and-Scoring-Conversations.md)
