---
title: "Plain Text Message Schema"
summary: "Technical reference for the PLAIN message body type, the fundamental building block for text-based interactions."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Plain Text Message Schema

The **PLAIN** message type is the simplest and most widely supported interaction format in ExpertFlow CX. It is used for standard chat, SMS, and system notifications.

## 1. Schema Definition
The body for a plain text message must include the `type` and `markdownText` properties.

| Property | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| **type** | String | Yes | Must be set to `"PLAIN"`. |
| **markdownText**| String | Yes* | The actual text content. Supports Markdown syntax. |

## 2. JSON Example
```json
{
  "body": {
    "type": "PLAIN",
    "markdownText": "Hello! How can I assist you today?"
  }
}
```

## 3. Implementation Notes
- **Markdown Support:** The ExpertFlow Agent Desk and Web Widget render standard Markdown (Bold, Italics, Lists, Links). 
- **Channel Fallback:** If a 3rd-party channel (e.g., SMS) does not support Markdown, the platform will attempt to strip the formatting before delivery to ensure the text remains readable.
- **Empty Messages:** Sending a message with an empty `markdownText` string is permitted for system "typing" indicators but should be avoided for standard user interactions.

---

*For sending files or images, see the [Multimedia Message Schema](CIM-Messages.md).*
