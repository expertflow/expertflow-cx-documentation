---
audience: [agent]
doc-type: reference
difficulty: beginner
aliases: []
---

# Pause and Resume Conversation: Limitations

This document outlines specific technical and functional constraints of the Pause/Resume (Hold/Resume) feature as of the 4.5 release.

## General Constraints

- **Digital Only**: This feature is exclusively for non-voice sessions (Chat, WhatsApp, etc.). Voice sessions use a separate "Hold" button on the call control bar which does not affect conversation SLA timers.
- **Wrap-up Behavior**: If an agent applies a wrap-up code while a conversation is **ON_HOLD**, the wrap-up is treated as an agent message. This automatically changes the state to **ACTIVE** and triggers the customer inactivity timer.

## Notifications and Timing

- **Customer Alerts**: Currently, the customer is notified via a BOT message (e.g., *"The conversation is resumed now."*) rather than a system notification. This behavior is subject to change in future releases.
- **Inactivity Trigger**: The customer inactivity timer starts immediately upon the conversation being resumed, as the state returns to active.
- **Multiple Agents**: In a multi-agent scenario, if one agent leaves and provides a wrap-up, the conversation state will revert to ACTIVE even if it was previously paused.
