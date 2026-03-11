---
title: "Telegram Connector Limitations"
summary: "Reference listing known limitations of the Telegram connector in ExpertFlow CX, including delivery notifications, typing indicators, media format gaps, and agent desk restrictions."
audience: [solution-admin, agent, supervisor]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["Telegram connector limitations", "Telegram known issues", "Telegram media limitations", "Telegram agent desk", "Telegram delivery notifications"]
aliases: ["Telegram limitations", "Telegram connector known issues"]
last-updated: 2026-03-10
---

# Telegram Connector Limitations

This page documents known limitations of the ExpertFlow CX Telegram connector.

## Functionality Limitations

| Limitation | Detail |
|---|---|
| **Delivery notifications** | The Telegram connector does not support message delivery or read receipt notifications. Agents have no confirmation that a sent message was delivered. |
| **Typing indicator (agent to customer)** | Customers can see a typing indicator when the agent is composing. However, agents cannot see when a customer is typing — the Telegram API does not provide this information. |
| **Quoted replies** | Agents cannot use quoted (threaded) reply when responding to a Telegram customer. |
| **Emojis on Agent Desk** | Emojis sent by Telegram customers are not rendered correctly on the Agent Desk interface. |
| **Seeking/navigating audio** | Agents cannot seek or navigate within audio messages received from Telegram. The audio can be played from the start only. |

## Media Format Limitations

When images, videos, or audio files are sent from Telegram **as a file** (rather than their native type), they may not display correctly on the Agent Desk.

Known media issues on Agent Desk:

| Media Type | Issue |
|---|---|
| **MP3 audio (agent send)** | Sending MP3 from agent to Telegram is currently a bug — not working. |
| **JPEG images (agent send)** | Sending JPEG from agent to Telegram is currently a bug — not working. |
| **RTF documents** | RTF files sent from Telegram to agent are not supported on Agent Desk. |
| **GIF** | Not supported for sending from Agent Desk to Telegram. |
| **WEBP images** | Not supported for sending from Agent Desk to Telegram. |

For the full media format compatibility matrix, see [Telegram Media Types Support](Telegram-Media-Types.md).

## Related Articles

- [Telegram Channel Overview](Telegram-Channel-Overview.md)
- [Telegram Media Types Support](Telegram-Media-Types.md)
- [Telegram Configuration Guide](Telegram-Configuration-Guide.md)
