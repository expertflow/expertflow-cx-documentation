---
title: "Channel Connector Developer Guide"
summary: "Developer guide for building a custom channel connector in ExpertFlow CX — covering the connector communication model, REST API and webhook requirements, and the 5-step registration process in Unified Admin."
audience: [developer, integrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["channel connector developer guide CX", "custom channel connector CX", "build channel connector CX", "CCM REST API CX", "connector webhook CX", "register channel connector CX", "channel connector developer CX"]
aliases: ["custom connector guide CX", "channel connector development CX", "build connector CX"]
last-updated: 2026-03-10
---

# Channel Connector Developer Guide

This guide explains how to build a custom channel connector that integrates a media channel with ExpertFlow CX (CCM — Customer Channel Manager) for customer interactions.

ExpertFlow CX is **channel-agnostic** — developers can connect any chat or voice media channel. The integration between the external channel and your connector is left to the developer's discretion and is not covered here.

## Communication Model

A Channel Connector communicates with ExpertFlow CX over **REST APIs**:

| Component | Role |
|---|---|
| **CCM** | Customer Channel Manager — the ExpertFlow CX core. |
| **Channel Connector** | Bridges external media channels with CCM. Sends and receives CIM messages. |
| **Customer Channels** | External media platforms (WhatsApp, Facebook, custom channels, etc.). |

The connector must:
1. **Expose a webhook** to receive events (messages, notifications) from CCM.
2. **Call the `cim-messages` endpoint** on CCM to send messages.

---

## Development Steps

### Step 1: Register the Channel Connector in Unified Admin

Follow the [Register Channel Connector](Register-Channel-Connector.md) guide to define your connector. This covers:
- Creating a Channel Type
- Creating a Channel Provider (with webhook URL pointing to your connector)
- Creating a Channel Connector
- Creating a Channel
- Creating a Customer Schema attribute for channel identification

### Step 2: Handle Configuration Updates

When Unified Admin settings change, your connector must call the **Channel Connector Configuration API** to update its local configuration. This keeps the connector in sync with changes made via the admin console.

### Step 3: Send Messages to CCM

To send a customer message to CCM, call:

```
POST /cim-messages
```

Message payloads follow the **CIM message schema**. See [CIM Messages](../Developer/CIM-Message-Schema/CIM-Messages.md) for the full format reference including message types (Plain Text, Button, Carousel, Location, etc.).

### Step 4: Receive Messages from CCM

Your connector must expose an HTTP webhook. Register the webhook URL in Unified Admin as the **Provider Webhook** in the Channel Provider configuration.

CCM will POST CIM-formatted messages to this webhook when agents or bots send outbound messages to the customer.

---

## Related Articles

- [Register Channel Connector](Register-Channel-Connector.md)
- [CIM Messages](../Developer/CIM-Message-Schema/CIM-Messages.md)
- [Custom Bot Connector Development](../Developer/Custom-Bot-Connector-Development.md)
- [Channel and Connector Setup](../Solution_Admin/Channel-and-Connector-Setup.md)
