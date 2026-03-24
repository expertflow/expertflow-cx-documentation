---
title: "CIM Message Body Reference"
summary: "Technical reference for all supported CIM Message Body types including Plain Text, Multimedia, and Structured Content."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# CIM Message Body Reference

The **Body** object contains the actual content payload of a message. Its internal structure varies based on the `type` property.

## 1. Supported Message Types
ExpertFlow CX supports a wide range of interaction types to ensure omnichannel consistency.

| Type | Description | Primary Use |
| :--- | :--- | :--- |
| **PLAIN** | Standard text content. | All Channels. |
| **MULTIMEDIA** | Images, Video, Audio, Files, and Stickers. | Digital Channels. |
| **ACTION** | Instruction to the system (e.g., FIND_AGENT). | Bot Handover. |
| **CAROUSEL** | A group of horizontally scrollable images/cards. | Web & Social. |
| **BUTTON** | Pre-defined options for the customer. | Outbound/Bots. |
| **LOCATION** | Geographic coordinates. | Map sharing. |
| **URL** | Web links formatted for action. | Resource sharing. |
| **RECEIPT** | Delivery and read notifications. | System events. |

## 2. Global Requirement
Every body object must include the **`type`** string to allow the platform to parse the subsequent fields correctly.

```json
"body": {
  "type": "PLAIN | MULTIMEDIA | ACTION | ...",
  "data": { ... type-specific payload ... }
}
```

## 3. Deep-Dive Payload Schemas
- **[Plain Text Message](Plain-Text-Message.md):** The simplest schema for text and markdown.
- **Multimedia Schema:** Details for `IMAGE`, `VIDEO`, and `FILE` attachments.
- **Structured Schemas:** Carousel, Button, and Location payloads.

---

*For metadata and sender info, see the [Message Header Reference](Message-Header.md).*
