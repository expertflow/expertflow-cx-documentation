---
audience: [administrator]
doc-type: reference
difficulty: beginner
aliases: []
---

# WhatsApp Cloud API Limitations & Highlights

This document outlines the supported formats and key limitations for the WhatsApp Cloud API integration within Expertflow CX (EFCX).

## Supported Media Formats

| Media Type | WhatsApp Cloud API Formats | EFCX Supported Formats |
| :--- | :--- | :--- |
| **Audio** | `.aac`, `.amr`, `.mp3`, `.m4a`, `.ogg` | `.mp3` only |
| **Image** | `.jpeg`, `.png` (max 5MB) | `.jpg`, `.png` |
| **Video** | `.mp4`, `.3gp` (H.264/AAC; max 16MB) | `.mp4` only |
| **Document** | `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt` | `.pdf`, `.doc`, `.docx`, `.ppt`, `.txt` |
| **Sticker** | `.webp` | Not supported |

## Key Limitations

1. **Sticker Messages**: Outbound sticker messages are not supported.
2. **Emoji Support**: Emojis are currently not supported by the connector.
3. **Interactive Messages**: Only **Button-type** interactive messages are supported from bots.
4. **File Sharing**: Disabled by default. Enable via `Unified Admin → AgentDesk → Enable File Sharing`.

For further details, refer to the [official WhatsApp Cloud API documentation](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/media).
