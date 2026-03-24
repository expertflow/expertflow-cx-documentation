---
title: "Telegram Media Types Support"
summary: "Reference table for media file format support across the Telegram connector — showing which formats are supported for messages sent from Telegram and received on the Agent Desk, and vice versa."

product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["Telegram media types", "Telegram file formats", "Telegram supported formats", "Telegram audio video images", "Telegram connector media"]
aliases: ["Telegram media support", "Telegram file support matrix", "Telegram format compatibility"]
last-updated: 2026-03-10
---

# Telegram Media Types Support

This reference lists media file format support for the Telegram connector. Formats marked with `*` in the source are noted as agent-supported types.

> **Size limit**: Files sent via Agent Desk must be **less than 5 MB**.

## Telegram → Agent Desk (Customer Sends to Agent)

| Media Type | Format | Sent from Telegram | Received on Agent Desk |
|---|---|---|---|
| **Audio** | Ogg | Yes | Yes |
| | Wav | Yes | No |
| | Mp3 | Yes | Yes |
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
| **Videos** | 3GP | Yes | No |
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

## Agent Desk → Telegram (Agent Sends to Customer)

| Media Type | Format | Sent from Agent | Received from Telegram |
|---|---|---|---|
| **Audio** | Mp3 | No (bug) | No |
| | Wav | Not Supported | — |
| | OGG | Not Supported | — |
| **Documents** | DOC | Yes | Yes |
| | PDF | Yes | Yes |
| | PPT | Yes | Yes |
| | TXT | Yes | Yes |
| | XLS | Yes | Yes |
| | DOCX | Yes | Yes |
| | XLSX | Yes | Yes |
| | RTF | No (bug) | — |
| | CSV, DXF, PSD, SQL, ZIP, SVG, CSS, PPTX | Not Supported | — |
| **Videos** | MP4 | Yes | Yes |
| | 3GP, MKV, FLV, AVI, MOV, MPEG | Not Supported | — |
| **Images** | JPG | Yes | Yes |
| | PNG | Yes | Yes |
| | JPEG | No (bug) | Yes |
| | GIF | Not Supported | — |
| | WEBP | Not Supported | — |

## Notes

- **Bug** entries indicate formats where support is expected but currently broken.
- **Not Supported** entries indicate formats that are explicitly not implemented.
- Voice recordings from Telegram are received and playable; seek functionality is not available.

## Related Articles

- [Telegram Connector Limitations](Telegram-Connector-Limitations.md)
- [Telegram Channel Overview](Telegram-Channel-Overview.md)
- [Telegram Configuration Guide](Telegram-Configuration-Guide.md)
