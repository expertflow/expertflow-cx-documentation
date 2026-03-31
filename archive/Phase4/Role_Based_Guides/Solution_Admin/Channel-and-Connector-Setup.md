---
title: "Channel and Connector Setup"
summary: "Guide for Solution Admins to configure digital channels, providers, and connectors to link customer touchpoints to the routing engine."
audience: [admin, integrator]
product-area: [channels, platform]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Channel and Connector Setup

As a Solution Admin (Olivia), you must bridge the gap between your customer's communication apps (WhatsApp, Facebook, Web) and your internal routing engine. This is done through a hierarchy of Providers, Connectors, and Channels.

## 1. Defining Channel Categories (MRD)
Before adding a channel, you must have a category defined.
1.  Go to **Routing Engine > Channel Categories**.
2.  Set the **Max Tasks Request**: This determines how many interactions of this type an agent can handle at once (e.g., 3 for Chat, 1 for Voice).

## 2. Configuring Providers & Connectors
These are the technical links to 3rd-party services.
1.  **Channel Providers:** Navigate to **Channel Manager > Channel Providers**. Add your vendor (e.g., Dialog 360 for WhatsApp, Meta for Facebook).
2.  **Channel Connectors:** Navigate to **Channel Manager > Channel Connectors**. Link a specific connector to your provider and enter the required API keys or URLs provided by the vendor.

## 3. Launching a New Channel
The Channel is the specific "Point of Entry" for customers.
1.  Go to the **Channel** section in Unified Admin.
2.  **Service Identifier:** Enter the unique ID for the channel (e.g., the WhatsApp Phone Number or the Website URL).
3.  **Routing Mode:**
    - **Push:** Interactions are assigned to agents via queues.
    - **Pull:** Interactions land in a "List" for agents to manually pick up.
4.  **Bot Association:** Every channel requires a **Bot ID** to handle initial intents and session timeouts.

## 4. Social Media Permissions
For Facebook and Instagram, you can control what agents are allowed to do.
- Navigate to the **Connector Provider** configuration.
- Add attributes like `LIKE_SUPPORT_SM` or `DELETE_SUPPORT_SM` and set them to `True` or `False` to manage agent capabilities.

---

*Need to configure the visual interface for web users? See [Configuring the Customer Widget](Configuring-the-Customer-Widget.md).*
