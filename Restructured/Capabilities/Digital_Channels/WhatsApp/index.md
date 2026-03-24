---
title: "WhatsApp Channel Overview"
summary: "High-level overview of WhatsApp channel integration, supporting WhatsApp Cloud API as the primary connectivity method and 360dialog as an alternative BSP for ExpertFlow CX."

product-area: [channels, whatsapp]
doc-type: explanation
difficulty: beginner
last-updated: 2026-03-17
---

# WhatsApp Channel Overview

WhatsApp is a core digital channel in ExpertFlow CX, enabling businesses to communicate with customers through the world's most popular messaging app. The platform supports rich media, templates, and automated bot-to-human handovers.

## Integration Options

ExpertFlow CX supports two WhatsApp integration paths:

| Integration | Description | Best For |
| :--- | :--- | :--- |
| **[WhatsApp Cloud API](./WhatsApp-Cloud-API.md)** | Direct Meta integration — no third-party BSP fees | Most customers; new deployments |
| **[360dialog Integration](./360dialog-WhatsApp-Overview.md)** | Third-party BSP via 360dialog | Legacy deployments; BSP contract already in place |

---

## Key Features

*   **Two-Way Messaging:** Agents can handle incoming customer queries and initiate outbound notifications using approved templates.
*   **Rich Media Support:** Send and receive images, documents (PDF), and audio files.
*   **Interactive Messages:** Use buttons and list pickers to guide customer journeys (requires [Conversation Studio](../../../Getting_Started/For_Conversation_Designers/Conversation-Studio-Configuration-Guide.md)).
*   **Verified Profiles:** Support for the official WhatsApp "Green Tick" for verified business accounts.

---

## Deployment Considerations

### Data Sovereignty
All WhatsApp interaction data is stored within your private ExpertFlow CX instance (on-premise or private cloud).

### Routing Logic
Incoming WhatsApp messages can be routed based on keywords, sentiment, or customer priority using the [Universal Routing Engine](../../../How-to_Guides/Developer_Integrator/Agent-Task-Routing-Lifecycle.md).

### Migrating from a Legacy BSP
The flexible connector architecture allows businesses to transition from legacy providers (like 360dialog or Twilio) to the native Cloud API without losing historical interaction data.

---

## Operational View for Supervisors

Supervisors can monitor real-time WhatsApp interactions through the **Team Dashboard**. Key metrics include:
*   **Average Response Time (ART):** Speed of agent replies on WhatsApp.
*   **Resolution Rate:** Percentage of WhatsApp queries closed within the first interaction.
*   **Sentiment Analysis:** Automatic detection of customer mood during the chat.

---

## In This Section

- [WhatsApp Cloud API](./WhatsApp-Cloud-API.md) — Supported message types, media specs, and getting started with Meta's native integration.
- [360dialog Integration](./360dialog-WhatsApp-Overview.md) — Overview of the 360dialog BSP connector and its configuration.
