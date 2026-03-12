---
title: "Socket Event: joinAsBargeIn"
summary: "Technical reference for the joinAsBargeIn Socket.IO event — emitted by the Agent Desk when a supervisor elevates from a silent monitor to an active participant."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
last-updated: 2026-03-11
---

# Socket Event: joinAsBargeIn

The `joinAsBargeIn` event is emitted by the **Agent Desk** (on behalf of a supervisor) to the **Agent Manager**. It instructs the platform to elevate the supervisor's role in an active conversation from a silent monitor to a full participant.

## Event Metadata
*   **Event Name:** `joinAsBargeIn`
*   **Emitter:** Agent Desk
*   **Listener:** Agent Manager
*   **Trigger:** Supervisor clicks the "Barge-in" button while silent monitoring a call.

---

## Payload Properties

| Property | Type | Description |
| :--- | :--- | :--- |
| `participantId` | String | The unique identifier of the supervisor initiating the barge-in. |
| `conversationId` | String | The unique identifier of the active conversation. |
| `roomInfo` | Object | Metadata about the chat room where the interaction is occurring. |

---

## Example Payload

```json
{
  "participantId": "65a63fee6a264c3b8edece8a",
  "conversationId": "65b3acaec94e6061e70a0ef5",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  }
}
```

---

## Related Events
*   [JoinAsSilentMonitor](./JoinAsSilentMonitor.md)
*   [onCimEvent](./onCimEvent.md)
*   [publishCimEvent](./publishCimEvent.md)
