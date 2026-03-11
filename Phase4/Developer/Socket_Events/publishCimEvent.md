---
title: "publishCimEvent"
summary: "Reference for the publishCimEvent Socket.IO event in ExpertFlow CX — emitted by the Agent Desk to send in-conversation messages (plain text, media, contact, location, URL, WrapUp) to Agent Manager."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["publishCimEvent CX", "agent sends message socket CX", "Agent Desk emit event CX", "CIM event publish CX", "socket send message CX"]
aliases: ["CX publishCimEvent reference", "publish CIM event CX"]
last-updated: 2026-03-10
---

# publishCimEvent

| Property | Value |
|---|---|
| **Event Name** | `publishCimEvent` |
| **Emitter** | Agent Desk |
| **Listener** | Agent Manager |

Emitted by the Agent Desk when an agent sends a message during an active conversation. Supported message types include plain text, media, contact, location, URL, and WrapUp.

---

## Payload Properties

| Name | Type | Description |
|---|---|---|
| `cimEvent` | Object | The CIM event object being published |
| `cimEvent.id` | String | System-generated event ID |
| `cimEvent.name` | String | Always `"AGENT_MESSAGE"` for agent-sent messages |
| `cimEvent.type` | String | Always `"MESSAGE"` for conversation messages |
| `cimEvent.timestamp` | Epoch | System-generated timestamp |
| `cimEvent.data` | CIMMessage | CIM message with header and body |
| `cimEvent.data.header` | MessageHeader | Sender, channel session, and routing metadata |
| `cimEvent.data.body` | MessageBody | Message content (type-specific) |
| `agentId` | String | ID of the agent emitting the event |
| `conversationId` | String | ID of the conversation |
| `roomInfo.id` | String | ID of the conversation room |
| `roomInfo.mode` | String | Room mode (e.g., `"CONTACT_CENTER"`) |

---

## Example Payload (Plain Text Message)

```json
{
  "cimEvent": {
    "id": "c65bb9da-f596-48a2-bef5-bd47f0732dbe",
    "name": "AGENT_MESSAGE",
    "type": "MESSAGE",
    "timestamp": 1653888665578,
    "data": {
      "id": "142ad3a6-6ab8-4cf7-9553-959e2c3605c2",
      "header": {
        "timestamp": 1653888665578,
        "sender": {
          "id": "688ef131-9cd6-4108-893e-033943eb2be0",
          "type": "AGENT",
          "role": "PRIMARY",
          "state": "SUBSCRIBED"
        },
        "channelSession": {
          "id": "7f570b41-1d5d-4932-bffe-fcdabcec1f3d",
          "state": "STARTED"
        }
      },
      "body": {
        "type": "PLAIN",
        "markdownText": "How can I help you today?"
      }
    }
  },
  "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
  "conversationId": "261c271a-58e6-4571-9d25-77ad26d745d6",
  "roomInfo": {
    "id": "65a625609487373651365bfb",
    "mode": "CONTACT_CENTER"
  }
}
```

---

## Related Articles

- [Socket Events](Socket-Events.md)
- [onCimEvent](onCimEvent.md)
- [CIM Messages](CIM-Message-Schema/CIM-Messages.md)
- [Message Header](CIM-Message-Schema/Message-Header.md)
- [Message Body](CIM-Message-Schema/Message-Body.md)
