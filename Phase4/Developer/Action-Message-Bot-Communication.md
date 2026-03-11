---
audience: [developer]
doc-type: reference
difficulty: beginner
aliases: []
---

# Action Message: Bot Communication

Bots can send **Action Messages** to instruct the Expertflow CX system to perform specific operational tasks, such as routing or participant management.

## Message Structure
The body must be in JSON format with `type: "ACTION"`.

**Example:**
```json
{
  "type": "ACTION",
  "name": "FIND_AGENT",
  "data": {
    "queueId": "12345"
  }
}
```

## Supported Actions

| Action Name | Description |
| :--- | :--- |
| **FIND_AGENT** | Triggers the routing engine to look for an available agent. |
| **ASSIGN_AGENT** | Forcefully assigns a specific agent to the conversation. |
| **ASSIGN_BOT** | Handover the conversation to another specialized bot. |
| **REVOKE_BOT** | Removes the bot from the interaction. |
| **CHANGE_PARTICIPANT_ROLE** | Updates the role (e.g., from Whisper to Primary) of a participant. |
| **UPDATE_CONVERSATION_DATA** | Updates metadata associated with the current session. |
| **END_CONVERSATION** | Terminates the interaction and triggers wrap-up. |
| **REMOVE_ALL_AGENTS** | Clears all human participants from the conversation. |

For detailed implementation of bot-to-system communication, refer to the [Custom Connector Bot Guide](../Integrator/Custom-Connector-Bot-Communication.md).
