---
audience: [agent]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Pause and Resume a Conversation

Agents can temporarily pause an active non-voice conversation to stop SLA and inactivity timers. This is useful for handling internal consultations or waiting for a customer without penalizing response metrics.

## How to Pause/Resume

1. **Pause**: Click the **Hold** button at the top of the message composer.
2. **Set Timer**: Select a duration from the drop-down menu and click **Confirm**.
3. **Indicators**:
   - The Agent SLA timer stops.
   - A 'pause' icon and countdown timer appear above the message composer.
   - The customer receives a notification: *"The conversation is currently paused by the agent."*
4. **Resume**: 
   - The conversation resumes automatically when the timer expires.
   - The agent can resume manually by typing a message.
   - The customer is notified: *"The conversation is resumed now."*

## Key Behaviors
- **Notifications**: While paused, browser and sound notifications for new customer messages are suppressed. They resume once the conversation is active again.
- **Inactivity**: The customer inactivity timeout is suspended during the pause.
- **Transfers**: If a paused conversation is transferred, it resumes automatically for the new agent.

## Voice Calls vs. Conversations
- **Voice**: Use the **Hold** button on the call control bar. This only pauses the audio; it does not stop SLA timers for the digital conversation thread.
- **Digital**: Use the **Hold** button on the composer bar to pause SLA and timers.
