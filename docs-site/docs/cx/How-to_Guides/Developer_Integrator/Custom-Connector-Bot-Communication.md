---
title: "Custom Connector-Bot Communication"
summary: "Reference guide for the message and intent exchange format between a custom bot connector and ExpertFlow CX — covering CIM request types (message vs intent), the intent table, bot response structure (message, suggestion, action), and the Bot Actions reference table."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: advanced
keywords: ["custom bot connector communication CX", "CIM bot request CX", "bot intent CX", "bot message format CX", "CHANNEL_SESSION_STARTED CX", "bot action CX", "FIND_AGENT CX"]
aliases: ["bot connector message format CX", "CIM bot communication CX", "bot framework message CX"]
last-updated: 2026-03-10
---

# Custom Connector-Bot Communication

This reference covers the request/response message format between the **custom bot connector** and ExpertFlow CX's Bot Framework. The connector sends messages and intents to the bot, and the bot responds with messages, suggestions, or actions.

---

## Request Types

The connector sends two types of requests to the bot:

| Type | When Used |
|---|---|
| `message` | A customer message that the bot should respond to |
| `intent` | A system event notifying the bot of conversation state changes |

---

## Send a Message to the Bot

When a `CUSTOMER_MESSAGE` CIM event is received, the connector sends a request with `type = "message"`.

- `entities` is `null` for message requests
- `metadata` contains the CIM Message object

```json
{
  "conversation": "1234",
  "type": "message",
  "message": "Hello how are you",
  "entities": null,
  "metadata": {<CimMessage>}
}
```

---

## Send an Intent to the Bot

For system events, the connector sends a request with `type = "intent"`.

- `entities` contains the data payload for the intent (e.g., a channelSession object)
- `metadata` is `null` for intent requests

```json
{
  "conversation": "1234",
  "type": "intent",
  "message": "CHANNEL_SESSION_STARTED",
  "entities": {
    "channelSession": {}
  },
  "metadata": null
}
```

### Intent Reference

| Intent Name | Intent Data | Fired When |
|---|---|---|
| `CHANNEL_SESSION_STARTED` | channelSession object | Customer starts a conversation on a channel |
| `CHANNEL_SESSION_ENDED` | channelSession object | Chat ended on a channel |
| `END_CONVERSATION` | channelSession object | Conversation is ended |
| `AGENT_RESERVED` | — | An agent is reserved and will be added to the conversation |
| `AGENT_SUBSCRIBED` | CcUser object | An agent joins the conversation |
| `AGENT_UNSUBSCRIBED` | CcUser object | An agent leaves the conversation |

---

## Bot Response Structure

The bot can respond with three types of responses:

1. **Message** — a response to send to the customer
2. **Suggestion** — a message shown only to the agent as a recommendation
3. **Action** — a system instruction for the Bot Framework to execute

All responses share the same structure:

| Property | Type | Required | Description |
|---|---|---|---|
| `intent` | Object | Optional | `name` (String) — event/intent name; `confidence` (Numeric) — confidence level (1.0 for system events) |
| `mode` | String | Optional | `"message"` or `"suggestion"` — specifies whether this is a customer-facing message or an agent-side suggestion |
| `body` | Object | Required | `type` (String) — message type (e.g., `PLAIN`, `ACTION`); `markdownText` (String) — message text; `name` (String) — action name (e.g., `FIND_AGENT`) |

### Response: Message or Suggestion

```json
{
  "intent": {
    "name": "Greet",
    "confidence": 0.92
  },
  "mode": "message",
  "body": {
    "type": "PLAIN",
    "markdownText": "Welcome"
  }
}
```

### Response: Action

```json
{
  "intent": {
    "name": "TALK_TO_AGENT",
    "confidence": 0.92
  },
  "mode": null,
  "body": {
    "type": "ACTION",
    "markdownText": "",
    "name": "FIND_AGENT",
    "data": {}
  }
}
```

---

## Bot Actions Reference

| Action Name | Data | Description |
|---|---|---|
| `END_CONVERSATION` | — | End the conversation |
| `FIND_AGENT` | — | Request agent routing |
| `ASSIGN_AGENT` | — | Assign a specific agent |
| `CANCEL_RESOURCE` | `reasonCode: CANCELLED` | Cancel a resource request |
| `REVOKE_REQUEST` | `reasonCode: CANCELLED` | Revoke a pending request |

> Actions marked with strikethrough in the source (`CUSTOMER_RESPONSE_TIMEOUT`, `AGENT_RESPONSE_TIMEOUT`, `END_CHANNEL_SESSION`, `CHANNEL_SESSION_EXPIRED`, `ACCEPT_TIMEOUT`) are deprecated and should not be used.

---

## Related Articles

- [Bot Connector Developer Guide](Bot-Connector-Developer-Guide.md)
- [Add Bot Connector](Add-Bot-Connector.md)
- [Channel Connector Developer Guide](Channel-Connector-Developer-Guide.md)
