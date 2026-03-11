---
audience: [developer]
doc-type: reference
difficulty: beginner
aliases: []
---

# CRM & Agent Desk Post Message Events

When CRM integration is enabled in Agent Desk, Expertflow CX emits JavaScript `postMessage` events to the parent CRM window. These allow the CRM to react to agent state changes and conversation events in real-time.

## Key Events

### 1. Agent State Change (`AGENT_STATE_CHANGE`)
Emitted whenever an agent's global state or specific MRD state changes.

**Example Payload Snippet:**
```json
{
  "eventName": "AGENT_STATE_CHANGE",
  "agentData": {
    "action": "AGENT_STATE_CHANGED",
    "agentPresence": {
      "state": { "name": "READY" },
      "agentMrdStates": [
        { "mrd": { "name": "CHAT" }, "state": "NOT_READY" }
      ]
    }
  }
}
```
- **States**: `READY`, `NOT_READY`, `LOGIN`, `LOGOUT`.

### 2. Agent Login (`AGENT_LOGIN`)
Sent upon successful login, containing the agent's profile, roles, and assigned team.

### 3. Agent Task State (`AGENT_TASK_STATE`)
Emitted during the lifecycle of a specific task (e.g., a chat or call).

- **RESERVED**: Triggered when a task is ringing/reserved for the agent.
- **ANSWERED**: Triggered when the agent accepts the conversation.

**Reserved State Attributes:**
- `conversationId`: Unique ID for the interaction.
- `channelCustomerIdentifier`: The customer's phone number or ID.
- `queue`: The name and ID of the queue the task came from.

## Integration Note
The CRM should listen for these events using a standard window event listener:
```javascript
window.addEventListener("message", (event) => {
  if (event.data.eventName === "AGENT_STATE_CHANGE") {
    console.log("Agent is now:", event.data.agentData.agentPresence.state.name);
  }
});
```
