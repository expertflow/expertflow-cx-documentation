---
title: "Telegram Connector Media Types Support"
summary: "Reference table for supported media file types in the ExpertFlow CX Telegram connector — covering audio, documents, video, image, location, and emoji support for both Telegram-to-agent and agent-to-Telegram directions."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["telegram media types CX", "telegram file support CX", "telegram connector media CX", "telegram audio CX", "telegram image support CX", "telegram document support CX", "telegram video CX", "agent desk telegram media"]
aliases: ["telegram file types CX", "telegram supported formats CX", "telegram media matrix CX"]
last-updated: 2026-03-10
---

# Telegram Connector Media Types Support

This reference documents which media file formats are supported when messages are sent from Telegram to the agent (inbound) and from the agent to Telegram (outbound).

> File size limit for Agent Desk: **5 MB maximum** for attachments sent from Agent Desk to Telegram.

## Inbound: From Telegram to Agent Desk

| Media Type | Format | Sent from Telegram | Received by Agent |
|---|---|---|---|
| **Audio** | OGG | Yes | Yes |
| | WAV | Yes | No |
| | MP3 | Yes | Yes |
| **Documents** | CSV | Yes | No |
| | DOC | Yes | Yes |
| | DXF | Yes | No |
| | SVG | Yes | Yes |
| | PPT | Yes | Yes |
| | PDF | Yes | Yes |
| | TXT | Yes | Yes |
| | SQL | Yes | No |
| | PSD | Yes | No |
| | XLS | Yes | Yes |
| | ZIP | Yes | No |
| | CSS | Yes | Yes |
| | DOCX | Yes | Yes |
| | PPTX | Yes | Yes |
| | XLSX | Yes | Yes |
| | RTF | Yes | No |
| **Voice** | Voice recording | Yes | Yes |
| **Video** | 3GP | Yes | No |
| | FLV | Yes | No |
| | MKV | Yes | No |
| | MP4 | Yes | Yes |
| | MPEG/MPGA | Yes | No |
| **Images** | GIF | Yes | Yes |
| | JPG | Yes | Yes |
| | PNG | Yes | Yes |
| | JPEG | Yes | Yes |
| | WEBP | Yes | Yes |
| **Location** | — | Yes | Yes |
| **Emojis** | — | Yes | Yes |

## Outbound: From Agent Desk to Telegram

| Media Type | Format | Sent from Agent | Received from Telegram |
|---|---|---|---|
| **Audio** | MP3 | No (bug) | No |
| | WAV | Not Supported | — |
| | OGG | Not Supported | — |
| **Documents** | DOC | Yes | Yes |
| | PDF | Yes | Yes |
| | PPT | Yes | Yes |
| | TXT | Yes | Yes |
| | XLS | Yes | Yes |
| | DOCX | Yes | Yes |
| | XLSX | Yes | Yes |
| | CSV | Not Supported | — |
| | DXF | Not Supported | — |
| | PSD | Not Supported | — |
| | SQL | Not Supported | — |
| | ZIP | Not Supported | — |
| | SVG | Not Supported | — |
| | CSS | Not Supported | — |
| | PPTX | Not Supported | — |
| | RTF | No (bug) | — |
| **Video** | MP4 | Yes | Yes |
| | 3GP | Not Supported | — |
| | MKV | Not Supported | — |
| | FLV | Not Supported | — |
| | AVI | Not Supported | — |
| | MOV | Not Supported | — |
| | MPEG | Not Supported | — |
| **Images** | JPG | Yes | Yes |
| | PNG | Yes | Yes |
| | GIF | Not Supported | — |
| | JPEG | No (bug) | — |
| | WEBP | Not Supported | — |

## Related Articles

- [Telegram Connector Limitations](Telegram-Connector-Limitations.md)
- [Telegram Connector Configuration Guide](Telegram-Connector-Configuration-Guide.md)
