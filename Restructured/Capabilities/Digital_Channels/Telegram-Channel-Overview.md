---
title: "Telegram Channel Overview"
summary: "Explanation of the Telegram channel integration in ExpertFlow CX — how it works, supported message types, and what agents and customers can do over Telegram."

product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["Telegram channel", "Telegram bot", "Telegram integration", "Telegram messaging", "digital channels", "CX Telegram"]
aliases: ["Telegram connector overview", "Telegram channel", "Telegram for CX"]
last-updated: 2026-03-10
---

# Telegram Channel Overview

The Telegram channel integration in ExpertFlow CX enables customers to initiate conversations with agents through a business-owned Telegram bot. Customers message the bot using the standard Telegram app; the message is routed through the platform and delivered to an available agent in the Agent Desk.

## How It Works

The integration uses a **Telegram Bot** as the customer-facing interface. The bot is created and registered through Telegram's BotFather and connected to ExpertFlow CX via a Bot Token and webhook.

When a customer sends a message to the bot:
1. The message is received by the CX Telegram Connector.
2. The connector routes the message to the CX platform, creating a conversation request.
3. The request is routed to an available agent based on queue and routing configuration.
4. The agent responds through the Agent Desk; the reply is delivered to the customer via the Telegram bot.

> **Note**: All Telegram interactions are one-to-one DM conversations. Group messaging and channels are not supported.

## Supported Message Types

### Customer to Agent (Telegram → Agent Desk)

| Type | Support |
|---|---|
| Text messages | Yes |
| Images (jpg, png, jpeg, webp) | Yes |
| Video (mp4) | Yes |
| Audio (Ogg) | Yes |
| Voice recordings | Yes |
| Documents (doc, pdf, ppt, txt, xls, docx, xlsx) | Yes |
| GIFs | Yes (displayed as video) |
| Location | Yes |
| Emojis | Yes |

### Agent to Customer (Agent Desk → Telegram)

| Type | Support |
|---|---|
| Text messages | Yes |
| Images (JPG, PNG, JPEG) | Yes |
| Video (mp4) | Yes |
| Documents (doc, pdf, ppt, txt, xls, docx, xlsx) | Yes |
| Audio (Mp3) | Bug — currently not working |

For the full media compatibility matrix, see [Telegram Media Types Support](Telegram-Media-Types.md).

## Routing Modes

The Telegram channel supports both **PUSH** (automatic routing to agents from a queue) and **PULL** (agents pick from a list). Configure this in the Channel settings in Unified Admin.

## Agent Experience

Agents see incoming Telegram messages as standard chat requests in the Agent Desk. The Telegram channel type icon identifies the source channel. The conversation view displays the customer's Telegram username (if public) and all messages exchanged.

## Known Limitations Summary

- No delivery notifications for messages.
- Agents cannot see the typing indicator when a customer is typing.
- Quoted (threaded) replies are not supported for agents responding to Telegram conversations.
- Emojis are not supported in the agent desk interface.
- Some media formats are not supported on the agent desk (mp3 audio, rtf documents, jpeg images — known bugs).

For the full list, see [Telegram Connector Limitations](Telegram-Connector-Limitations.md).

## Related Articles

- [Telegram Bot Creation Guide](Telegram-Bot-Creation-Guide.md)
- [Telegram Configuration Guide](Telegram-Configuration-Guide.md)
- [Telegram Connector Limitations](Telegram-Connector-Limitations.md)
- [Telegram Media Types Support](Telegram-Media-Types.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
