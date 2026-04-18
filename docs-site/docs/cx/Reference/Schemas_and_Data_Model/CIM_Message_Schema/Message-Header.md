---
title: "CIM Message Header Reference"
summary: "Technical reference for the CIM Message Header, defining sender information, timestamps, and conversation metadata."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# CIM Message Header Reference

The **Header** object contains the metadata required to route and process a CIM message. It identifies who sent the message, which conversation it belongs to, and what the sender's intent is.

## 1. Header Properties
| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **sender** | Object | Yes | Identifies the originator (Agent, Bot, Customer, or System). |
| **channelData** | Object | Yes* | Metadata for the communication medium. *Required for outbound.* |
| **conversationId**| String | Yes | The system-generated UUID for the interaction session. |
| **timestamp** | Number | No | The Unix timestamp when the message was sent. |
| **intent** | Enum | No | Specific action request (e.g., `REPLY_TO`). Only for bots. |
| **customer** | Object | Yes* | Link to the CX-Customer profile. *Required for outbound.* |
| **roomID** | String | No | The ID of the permanent room container. |

## 2. The Sender Object
Defines the actor initiating the communication.
```json
"sender": {
  "id": "uuid-string",
  "type": "AGENT | BOT | CONNECTOR | APP | SYSTEM",
  "senderName": "Amy Agent",
  "additionalDetail": {} 
}
```

## 3. Intent and Entities
For virtual agents and automated flows, the `intent` field describes the "Why" behind the message.
- **Normal Messages:** Intent is typically `null`.
- **Action Requests:** Intent may be `FIND_AGENT` or `START_SURVEY`.
- **Entities:** A Map containing data associated with the intent (e.g., `queueName`).

---

*For content-specific properties, see the [Message Body Reference](Message-Body.md).*
