---
audience: [administrator]
doc-type: reference
difficulty: beginner
aliases: []
---

# Customer and Agent SLA Implementation Details

This document outlines the logic for Service Level Agreement (SLA) timers based on conversation events in Expertflow CX.

## SLA Logic by Event

| Event | Agent SLA Action | Customer SLA Action |
| :--- | :--- | :--- |
| **SESSION_STARTED** | Stop if Voice session. | Start if Non-Voice; Start for current if Voice. |
| **TASK_ENQUEUED** | - | Stop for the specific channel. |
| **AGENT_SUBSCRIBE** | Reset for all if Primary exists; Start if first agent. | Stop for Non-Voice sessions. |
| **AGENT_MESSAGE** | Stop timer (except for wrap-up). | Start for all channels (if no Voice session). |
| **CUSTOMER_MESSAGE** | Start if agent exists and not on hold. | Start for all other channels if not on hold. |
| **BOT_MESSAGE** | - | Start if not on hold. |
| **PAUSED** | - | Stop for all sessions. |
| **NO_AGENT** | - | Start timer for latest session. |

## Common Scenarios

### Web Chat with Available Agent
1. **Started**: Customer SLA starts.
2. **Customer Message**: Customer SLA stops.
3. **Agent Reserved/Joined**: Agent SLA starts; Customer SLA stops.

### Voice Escalation
When a customer initiates a voice session during an active chat:
1. The running Agent SLA for the chat is stopped.
2. A new Voice session SLA is started.

### Conversation Pause
When an agent puts a conversation on hold (Pause), the Customer SLA timer is stopped for all sessions until the conversation is resumed.
