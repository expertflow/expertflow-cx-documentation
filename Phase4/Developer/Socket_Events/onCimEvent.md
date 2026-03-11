---
title: "onCimEvent"
summary: "Reference for the onCimEvent Socket.IO event in ExpertFlow CX — emitted by Agent Manager to deliver real-time CIM events (messages, suggestions, and notifications) to the Agent Desk."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["onCimEvent CX", "socket event CX", "Agent Manager event CX", "real-time messages CX", "CIM event socket CX", "onCimEvent payload"]
aliases: ["CX onCimEvent reference", "onCimEvent socket"]
last-updated: 2026-03-10
---

# onCimEvent

| Property | Value |
|---|---|
| **Event Name** | `onCimEvent` |
| **Emitter** | Agent Manager |
| **Listener** | Agent Desk |

The Agent Manager sends real-time CIM Events to the Agent Desk through this event. This includes messages from customers, bots, and system notifications.

---

## Payload Properties

| Name | Type | Description |
|---|---|---|
| `cimEvent.id` | String | System-generated ID of the event |
| `cimEvent.name` | String | Event name (e.g., `BOT_SUGGESTION`, `AGENT_MESSAGE`) |
| `cimEvent.type` | String | Event type (e.g., `SUGGESTION`, `MESSAGE`) |
| `cimEvent.timestamp` | Epoch | Timestamp when the event was generated |
| `cimEvent.data` | CIMMessage | Full CIM message object (header + body) |
| `conversationId` | String | UUID of the conversation |

---

## Example Payload

```json
{
  "cimEvent": {
    "id": "e8ced09f-50b9-4721-bcfd-80ca07994cfd",
    "name": "BOT_SUGGESTION",
    "type": "SUGGESTION",
    "timestamp": 1651938185572,
    "data": {
      "id": "bcc62bd4-e021-4ca0-b285-a5b200192f81",
      "header": {
        "sender": {
          "type": "BOT",
          "role": "ASSISTANT"
        },
        "channelData": {
          "channelCustomerIdentifier": "113377701",
          "serviceIdentifier": "1111",
          "channelTypeCode": "webChannel"
        },
        "timestamp": 1651938185571
      },
      "suggestions": [
        {
          "messageBody": {
            "type": "PLAIN",
            "markdownText": "Bot could not understand your message. An agent will join you shortly."
          },
          "confidenceLevel": 0
        }
      ]
    }
  },
  "conversationId": "9a8d8480-3df6-494b-90cc-b324fe5c5224"
}
```

---

## Related Articles

- [Socket Events](Socket-Events.md)
- [publishCimEvent](publishCimEvent.md)
- [CIM Messages](CIM-Message-Schema/CIM-Messages.md)
- [AgentManager SDK Integration Guide](AgentManager-SDK-Integration-Guide.md)
