---
title: "Universal Channel Onboarding Guide"
summary: "Master onboarding guide for Solution Admins to connect Facebook, Instagram, and Web Chat channels to ExpertFlow CX."
audience: [administrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["channel onboarding", "Facebook setup", "Instagram setup", "web chat setup", "channel configuration", "Unified Admin channels"]
aliases: ["add a channel", "connect a channel", "channel setup guide"]
last-updated: 2026-03-21
---

# Universal Channel Onboarding Guide

This guide helps Solution Admins connect a new digital channel to ExpertFlow CX. It covers the three most common channels — **Facebook**, **Instagram**, and **Web Chat** — and points to detailed guides for each.

---

## Common Prerequisites

Before setting up any channel, confirm the following:

- You have **Solution Admin** access to Unified Admin.
- The relevant **connector service** is deployed and running in your environment (confirm with your infrastructure team).
- You have a **tenant** provisioned and active in the system.
- For Meta channels (Facebook, Instagram): you have admin access to a Facebook Developer account and the associated Business Page.

---

## Channel Comparison

| Channel | Integration Method | Key Identifier | Connector Service |
|---|---|---|---|
| Facebook | Meta Graph API + Webhook | Facebook Page ID | `ef-facebook-connector-svc` |
| Instagram | Meta Graph API + Webhook | Instagram User ID | `ef-instagram-connector-svc` |
| Web Chat | Embedded JavaScript widget | Service Identifier | Customer Widget (deployed separately) |

---

## Facebook

Facebook supports both **direct messages (DM)** via Messenger and **social media comments** on your Page posts.

### High-Level Steps

1. **Create a Facebook App** on the Meta Developer Platform, add Messenger and Webhooks products, and request the required permissions (`pages_messaging`, `pages_manage_metadata`, etc.).
2. **Generate a Long-Lived Page Access Token** (never-expiring) using the Graph API Explorer — a short-lived token alone is not sufficient.
3. **Register the webhook** pointing to your CX environment: `https://<YOUR-FQDN>/facebook-connector/webhook/<PAGE-ID>`.
4. **Configure Unified Admin**: create a Channel Type, Channel Connector (with the Page Access Token), and a Channel with the Facebook Page ID as the Service Identifier.

> Full instructions: [Facebook Configuration Guide](../../How-to_Guides/Administrator/Facebook-Configuration-Guide.md)

---

## Instagram

Instagram integration runs through the Meta Graph API, using the same Facebook App infrastructure. A Facebook Page must be linked to the Instagram Professional Account.

### High-Level Steps

1. **Set up a Facebook Business App** and add the **Instagram Messenger** and **Webhooks** products. Link your Facebook Page to your Instagram Professional Account.
2. **Request permissions**: `instagram_basic`, `instagram_manage_messages`, `instagram_manage_comments`, `pages_manage_metadata`.
3. **Register the webhook** pointing to: `https://<YOUR-FQDN>/instagram-connector/webhook/<INSTAGRAM-USER-ID>`.
4. **Configure Unified Admin**: create a Channel Type, Channel Connector (with the Page Access Token), and a Channel with the Instagram User ID as the Service Identifier. Set Mode to `HYBRID`.

> Full instructions: [Instagram Connector Configuration Guide](../../How-to_Guides/Administrator/Instagram-Connector-Configuration-Guide.md)

---

## Web Chat

Web Chat uses an embeddable JavaScript widget hosted by ExpertFlow CX. No third-party developer account is required.

### High-Level Steps

1. **Configure Unified Admin**: create a Web Channel with a Service Identifier and Widget Identifier.
2. **Embed the widget** on your website using Google Tag Manager (recommended) or a direct HTML script tag.

> Full instructions: [Customer Widget Embedding Guide](../../Capabilities/Digital_Channels/Customer-Widget-Embedding-Guide.md)

---

## After Connecting a Channel

Once a channel is live, verify end-to-end message flow by sending a test message from the customer side and confirming it appears in the agent interface. Check that routing rules and queues are assigned to the channel before going live with real customers.

---

## Related Articles

- [Facebook Channel Overview](../../Capabilities/Digital_Channels/Facebook-Channel-Overview.md)
- [Facebook Connector Limitations](../../Capabilities/Digital_Channels/Facebook-Connector-Limitations.md)
- [Customer Widget Features and Capabilities](../../Capabilities/Digital_Channels/Customer-Widget-Features-Capabilities.md)
- [Onboarding a New Tenant](../For_Hosting_Partners/Onboarding-a-New-Tenant.md)
