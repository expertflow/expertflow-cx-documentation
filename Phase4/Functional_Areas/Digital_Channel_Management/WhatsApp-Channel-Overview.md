---
title: "WhatsApp Channel Overview"
summary: "High-level overview of WhatsApp channel integration, supporting WhatsApp Cloud API as the primary connectivity method for ExpertFlow CX."
audience: [admin, supervisor]
product-area: [channels, whatsapp]
doc-type: explanation
difficulty: beginner
last-updated: 2026-03-11
---

# WhatsApp Channel Overview

WhatsApp is a core digital channel in ExpertFlow CX, enabling businesses to communicate with customers through the world's most popular messaging app. The platform supports rich media, templates, and automated bot-to-human handovers.

## 1. Primary Connectivity: WhatsApp Cloud API
ExpertFlow CX fully supports the **WhatsApp Cloud API** from Meta. This is the recommended integration method for most customers as it offers:
*   **Direct Meta Integration:** No third-party BSP (Business Solution Provider) fees.
*   **High Performance:** Lower latency for message delivery and media processing.
*   **Scalability:** Support for high-volume messaging and automated notifications.

> For technical setup steps, see the [WhatsApp Cloud API Configuration Guide](./WhatsApp-Cloud-API-Configuration.md).

---

## 2. Key Features
*   **Two-Way Messaging:** Agents can handle incoming customer queries and initiate outbound notifications using approved templates.
*   **Rich Media Support:** Send and receive images, documents (PDF), and audio files.
*   **Interactive Messages:** Use buttons and list pickers to guide customer journeys (requires [Conversation Studio](../Designer/Conversation-Studio-Fundamentals.md)).
*   **Verified Profiles:** Support for the official WhatsApp "Green Tick" for verified business accounts.

---

## 3. Deployment Models
While the WhatsApp Cloud API is the standard, ExpertFlow CX maintains a flexible connector architecture. This allows businesses to transition from legacy providers (like 360dialog or Twilio) to the native Cloud API without losing historical interaction data.

### **Enterprise Considerations**
*   **Data Sovereignty:** All WhatsApp interaction data is stored within your private ExpertFlow CX instance (on-premise or private cloud).
*   **Routing Logic:** Incoming WhatsApp messages can be routed based on keywords, sentiment, or customer priority using the [Universal Routing Engine](../Developer/Agent-Task-Routing-Lifecycle.md).

---

## 4. Operational View for Supervisors
Supervisors can monitor real-time WhatsApp interactions through the **Team Dashboard**. Key metrics include:
*   **Average Response Time (ART):** Speed of agent replies on WhatsApp.
*   **Resolution Rate:** Percentage of WhatsApp queries closed within the first interaction.
*   **Sentiment Analysis:** Automatic detection of customer mood during the chat.

---

## Related Guides
*   [WhatsApp Cloud API Configuration](./WhatsApp-Cloud-API-Configuration.md)
*   [Managing WhatsApp Message Templates](../Solution_Admin/Managing-Message-Templates.md)
*   [WhatsApp Integration Limitations](./WhatsApp-Cloud-API-Limitations.md)
