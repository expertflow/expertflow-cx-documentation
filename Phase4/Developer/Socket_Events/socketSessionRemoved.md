---
title: "socketSessionRemoved"
summary: "Reference for the socketSessionRemoved Socket.IO event in ExpertFlow CX — triggered by Agent Manager when an agent switches browser tabs, causing the Agent Desk to remove the agent from the previous session."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: intermediate
keywords: ["socketSessionRemoved CX", "agent session removed CX", "browser tab switch CX", "agent logout socket CX", "socket session event CX"]
aliases: ["CX socketSessionRemoved reference", "session removed event CX"]
last-updated: 2026-03-10
---

# socketSessionRemoved

| Property | Value |
|---|---|
| **Event Name** | `socketSessionRemoved` |
| **Emitter** | Agent Manager |
| **Listener** | Agent Desk |

Triggered when an agent opens a new browser tab (establishing a second socket session). Agent Manager notifies the previous tab's Agent Desk to remove the agent from the old session — effectively logging the agent out of the previous session automatically.

---

## Payload Properties

| Name | Type | Description |
|---|---|---|
| `agentId` | String | UUID of the agent whose previous session was removed |

---

## Example Payload

```json
{
  "agentId": "cc76c196-912d-4a47-a9dd-8a2357f54399"
}
```

---

## Agent Desk Behavior

When the Agent Desk receives this event, it should:

1. Recognize that the current session has been superseded by a new tab.
2. Clear local session state.
3. Display a message to the user (e.g., *"You have been logged out because you opened a new session in another tab."*).
4. Redirect the agent to the login screen or a disconnected state.

---

## Related Articles

- [Socket Events](Socket-Events.md)
- [onCimEvent](onCimEvent.md)
- [AgentManager SDK Integration Guide](AgentManager-SDK-Integration-Guide.md)
