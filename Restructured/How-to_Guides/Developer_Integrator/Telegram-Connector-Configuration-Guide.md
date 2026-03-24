---
title: "Telegram Connector Configuration Guide"
summary: "Step-by-step guide for configuring the Telegram connector in ExpertFlow CX Unified Admin — covering channel type, channel provider, channel connector, channel configuration, and webhook registration."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["telegram connector CX", "telegram configuration unified admin", "telegram bot token CX", "telegram channel setup CX", "telegram webhook CX", "telegram CIM connector", "telegram channel provider CX", "BOT-TOKEN CX"]
aliases: ["telegram connector setup CX", "configure telegram CX", "telegram integration CX"]
last-updated: 2026-03-10
---

# Telegram Connector Configuration Guide

This guide covers the configuration of the Telegram connector in Unified Admin. It assumes you have already created a Telegram bot and have your **BOT-TOKEN** ready.

> If you have not yet created a Telegram bot, visit the Telegram BotFather documentation to create your bot and retrieve the token.

## Prerequisites

Before configuring the Telegram channel:

1. Set up an **MRD**, **Routing Attribute**, and **Queue** specifically for Telegram in Unified Admin.
2. Assign the MRD to the agent and configure agent attributes.
3. Ensure the Telegram connector is deployed in your environment.

These steps follow the same process as any other channel setup in Unified Admin.

---

## Step 1: Channel Type Configuration

The Telegram channel type is bootstrapped automatically by the system.

1. In **Channel Manager → Channel Type**, locate the TELEGRAM channel type.
2. Select the associated **MRD** for Telegram.
3. The Telegram icon is automatically bootstrapped — you can upload a custom icon if desired.

---

## Step 2: Channel Provider Configuration

1. Navigate to **Channel Manager → Channel Provider** and click **Add new channel provider**.
2. Set a name (e.g., `Telegram Channel Provider`).
3. Select **Channel Type**: `TELEGRAM`.
4. In **Provider Webhook**, enter the Telegram connector service URL:
   - K3s: `http://ef-telegram-connector-svc:8080`
   - Helm: `http://cx-channels-telegram-connector-svc:8664`
5. Click **Add Custom Attribute** and add the following attribute:

   | Attribute Name | Description | Type | Required |
   |---|---|---|---|
   | `BOT-TOKEN` | Unique key identifying your Telegram bot. | String(100) | Yes |

6. Click **Save**.

---

## Step 3: Channel Connector Configuration

1. Navigate to **Channel Manager → Channel Connector** and add a new connector.
2. Set a name (e.g., `Telegram Channel Connector`).
3. Select the **Telegram Channel Provider** created in Step 2.
4. Enter the **BOT-TOKEN** value from your Telegram bot.
5. Click **Save**.

---

## Step 4: Channel Configuration

1. Navigate to **Channel Manager → Channel**, find the TELEGRAM channel, and click **Add new channel**.
2. Fill in the channel settings:

   | Field | Value |
   |---|---|
   | **Name** | e.g., `Telegram DM` |
   | **Service Identifier** | Your bot's ID (see below for how to retrieve it) |
   | **Bot ID** | Select your bot (e.g., `EF-Bot`) |
   | **Channel Connector** | `Telegram Channel Connector` |
   | **Customer Activity Timeout** | `180` seconds |
   | **Channel Mode** | `HYBRID` |
   | **Agent Selection Policy** | `LONGEST AVAILABLE` |
   | **Agent Request TTL** | `100` seconds |
   | **Routing Mode** | `PUSH` or `PULL` |
   | **Queue / List** | Select based on Routing Mode |

3. Click **Save**.

### Retrieving the Service Identifier (Bot ID)

Make a GET request to:
```
GET https://api.telegram.org/bot{YOUR-BOT-TOKEN}/getMe
```

The response contains your bot's numeric ID:
```json
{
  "ok": true,
  "result": {
    "id": 7747304660,
    "is_bot": true,
    "first_name": "MyBot",
    "username": "my_cx_bot"
  }
}
```

Use the `id` value (e.g., `7747304660`) as the **Service Identifier**.

---

## Step 5: Register the Webhook

After completing channel configuration, register the webhook to enable message delivery:

**Endpoint:**
```
POST https://{FQDN}/telegram-connector/register-webhook
```

**Request body:**
```json
{
  "botToken": "4892363233:WEMWDEfwefwe43New9-qghSwA",
  "url": "https://your-cx-instance.example.com"
}
```

> Only HTTPS URLs are supported for the `url` field.

**Success response:**
```json
{
  "ok": true,
  "result": true,
  "description": "Success",
  "errorCode": null,
  "status": "OK"
}
```

Once webhook registration is complete, the Telegram connector can receive and send messages. You can test by searching for your bot in the Telegram app and starting a conversation.

---

## Related Articles

- [Telegram Connector Limitations](Telegram-Connector-Limitations.md)
- [Channel and Connector Setup](../Administrator/Channel-and-Connector-Setup.md)
- [Viber Connector Configuration Guide](../Administrator/Viber-Connector-Configuration-Guide.md)
- [WhatsApp Cloud API Configuration](../Administrator/WhatsApp-Cloud-API-Configuration.md)
