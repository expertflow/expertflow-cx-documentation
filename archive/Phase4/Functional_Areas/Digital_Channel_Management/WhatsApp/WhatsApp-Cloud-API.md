---
title: "WhatsApp Cloud API"
summary: "Reference for the WhatsApp Cloud API integration in ExpertFlow CX — supported message types, media specifications, and getting started steps."
audience: [solution-admin, agent]
product-area: [channels, whatsapp]
doc-type: reference
difficulty: beginner
last-updated: 2026-03-17
---

# WhatsApp Cloud API

WhatsApp Cloud API is the recommended integration method for ExpertFlow CX. It provides a direct connection to Meta's platform — no third-party BSP required — with lower latency, no additional per-message fees, and support for the full range of WhatsApp message types.

> For setup instructions, see the [WhatsApp Cloud API Configuration Guide](../../../Role_Based_Guides/Solution_Admin/WhatsApp-Cloud-API-Configuration.md).
> For known constraints, see [WhatsApp Cloud API Limitations](../../../Role_Based_Guides/Solution_Admin/WhatsApp-Cloud-API-Limitations.md).

---

## Getting Started

A business must have a verified WhatsApp Business Account linked to a phone number. This account is integrated into ExpertFlow CX through Unified Admin. Once connected, agents handle WhatsApp conversations like any other channel in the Agent Desk.

---

## Supported Message Types

### Plain Message

A basic text message exchanged between the customer and the agent without attachments.

- **Maximum length:** 4,096 characters
- **Format:** UTF-8 encoded text

Agents reply using the Reply Bar at the bottom of the conversation view.

---

### Audio Message

Voice notes or audio clips sent during chat.

- Audio files play inline with a single click.
- Agents can send voice messages by uploading via the attachment icon in the Reply Bar.
- **Maximum size:** 16 MB

---

### Video Message

Short video files shared for visual explanation or demonstration.

- Videos display as a thumbnail with a play button.
- Agents can upload and send video files from their desktop.
- **Maximum size:** 16 MB

---

### Image Message

Photos or screenshots exchanged for visual context.

- Images display as thumbnails; click to expand.
- Agents can send images via the attachment icon in the Reply Bar.
- **Maximum size:** 5 MB

---

### Stickers

Expressive graphics sent by customers to convey mood or reaction.

- Stickers display as static or animated images.
- **Agents cannot send stickers** — outbound sticker messages are not supported (WhatsApp uses `image/webp` format, which is not supported for outbound).
- **Maximum size:** Static 100 KB, Animated 500 KB

---

### Emoji

> **Limitation:** Emoji support is not currently provided by the connector.

---

### Quoted Reply

A reply linked to a specific previous message for conversational clarity.

- Agents select a message and click **Reply** — the reply carries the original message as a reference.
- Customers can also use quoted replies from their WhatsApp app.

---

### File Message

Document files (PDFs, DOCs, etc.) sent for reference, instructions, or records.

- Files appear in chat with filename, type, and size displayed.
- Click to open or download directly.
- Agents can upload and send files from their desktop (invoices, manuals, forms).
- **This feature must be enabled before use:** `Unified Admin → AgentDesk → Enable File Sharing → Save`
- **Maximum size:** 100 MB

---

### Contact Message

A structured contact card with fields like name, email, phone, and organization.

- Shared contact cards appear as a contact block showing all fields.
- Agents can click to view full details.
- Bots can also send contact cards via button messages.

---

### Location Message

A map location or pin sent for navigation or address confirmation.

- Received locations render as a mini map with a clickable Google Maps link.
- Agents can click to view the place.
- Bots can also send locations via button messages.

---

### Read Notification

A system-generated signal indicating the customer has seen a message.

- When the message is read on WhatsApp, a "read" acknowledgement is reflected in the agent's interface alongside the **Customer's Name**.
- Applies to both incoming and outgoing messages.
- Helps agents confirm delivery and decide whether to follow up.

---

### Interactive / Button Messages

Predefined button options sent by the business to help users respond faster.

- A bot sends a message with buttons.
- Customers tap a button to select their choice.
- The selected option appears in the conversation feed.
- **Note:** Only Button-type interactive messages are supported from bots (not List Messages for outbound bot flows).

---

### URLs

Web links sent within messages to direct users to external resources.

- Links are automatically detected and made clickable.
- Clicking opens the URL in a new browser window.

---

## Related Guides

- [WhatsApp Cloud API Configuration](../../../Role_Based_Guides/Solution_Admin/WhatsApp-Cloud-API-Configuration.md)
- [WhatsApp Cloud API Limitations](../../../Role_Based_Guides/Solution_Admin/WhatsApp-Cloud-API-Limitations.md)
- [360dialog Integration](./360dialog-WhatsApp-Overview.md)
