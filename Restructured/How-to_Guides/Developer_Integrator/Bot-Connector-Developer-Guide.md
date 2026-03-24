---
title: "Bot Connector Developer Guide"
summary: "Developer guide for building a custom bot connector to integrate a third-party bot with ExpertFlow CX — covering the connector's role in the Bot Framework, webhook registration, message translation, and links to the message/intent format reference."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: explanation
difficulty: advanced
keywords: ["bot connector developer guide CX", "custom bot connector CX", "bot framework CX", "bot webhook CX", "custom bot integration CX"]
aliases: ["custom bot connector CX", "bot developer guide CX", "bot framework integration CX"]
last-updated: 2026-03-10
---

# Bot Connector Developer Guide

This guide is for developers building a **custom bot connector** to integrate a third-party bot with ExpertFlow CX. Built-in connectors exist for Rasa and Dialogflow. For any other bot platform, a custom connector must be developed to handle communication between the CX Bot Framework and the external bot.

**Intended audience**: Developers familiar with bot frameworks and synchronous/asynchronous REST APIs.

---

## What Is a Bot Connector?

The Bot Framework in ExpertFlow CX manages all aspects of conversation flow with bots. The **custom bot connector** is the communication interface between the Bot Framework and a third-party bot.

A connector sits between:

```
CX Bot Framework  ←→  Custom Bot Connector  ←→  Third-party Bot
```

The connector is responsible for:

1. **Receiving messages and intents** from the Bot Framework and forwarding them to the custom bot via REST.
2. **Receiving responses** from the bot (messages, suggestions, or actions) and translating them back into the format the Bot Framework expects.
3. **Translation/adaptation** — a Bot Framework adapter may be developed to convert CX message formats into the language understood by the custom bot, and vice versa.

> The internal architecture and development of the bot/adapter is at the developer's discretion. This guide covers the CX-side interface only.

---

## Connector Requirements

| Requirement | Detail |
|---|---|
| **Webhook exposure** | The custom bot must expose a webhook URL. This URL is registered in Unified Admin when setting up the bot connector. |
| **Message handling** | The connector must handle CIM message events (`CUSTOMER_MESSAGE`) and compose outbound requests to the bot. |
| **Intent handling** | The connector must send system intents (`CHANNEL_SESSION_STARTED`, `AGENT_SUBSCRIBED`, etc.) to the bot. |
| **Response translation** | Bot responses (messages, suggestions, actions) must be translated back into the CIM message format for the Bot Framework. |

---

## Development Steps

| Step | Action |
|---|---|
| 1 | **Register the custom bot** — Expose a webhook on your bot and register the bot name and webhook URL in Unified Admin. See [Add Bot Connector](Add-Bot-Connector.md). |
| 2 | **Implement the connector** — Handle inbound CIM events and compose requests to the bot. Handle bot responses and translate them back. See [Custom Connector-Bot Communication](Custom-Connector-Bot-Communication.md) for the full message, intent, and action format reference. |

---

## Related Articles

- [Custom Connector-Bot Communication](Custom-Connector-Bot-Communication.md)
- [Add Bot Connector](Add-Bot-Connector.md)
- [Register Channel Connector](Register-Channel-Connector.md)
- [Channel Connector Developer Guide](Channel-Connector-Developer-Guide.md)
