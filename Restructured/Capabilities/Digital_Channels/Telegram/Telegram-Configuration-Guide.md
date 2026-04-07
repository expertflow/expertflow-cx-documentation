---
title: "Telegram Configuration Guide"
summary: "How-to guide for configuring the Telegram connector in ExpertFlow CX Unified Admin — including Channel Type, Channel Provider, Channel Connector, Channel setup, and webhook registration."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["Telegram configuration", "Telegram connector setup", "Telegram Unified Admin", "Telegram webhook", "BOT-TOKEN", "Telegram channel setup"]
aliases: ["Telegram connector configuration", "configure Telegram channel", "Telegram Unified Admin setup"]
last-updated: 2026-03-10
---

# Telegram Configuration Guide

This guide walks through configuring the Telegram channel connector in ExpertFlow CX Unified Admin. Complete [Telegram Bot Creation](Telegram-Bot-Creation-Guide.md) first — you will need the Bot Token before proceeding.

## Prerequisites

- A Telegram Bot Token obtained from BotFather. See [Telegram Bot Creation Guide](Telegram-Bot-Creation-Guide.md).
- The Telegram connector deployed in your CX environment.
- An MRD, Queue, and routing attributes configured for the Telegram channel in Unified Admin.

## Step 1: Configure Channel Type

The Telegram channel type is automatically bootstrapped by the system. To verify and configure it:

1. In Unified Admin, go to **Channel Manager → Channel Type**.
2. Find the **TELEGRAM** channel type in the list.
3. Select the **MRD** associated with Telegram interactions.
4. The Telegram icon is auto-loaded, but you can upload a custom icon if needed.
5. Click **Save**.

## Step 2: Configure Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Click **Add new Channel Provider** and name it (e.g., **Telegram Channel Provider**).
3. Select **TELEGRAM** as the Channel Type.
4. In the **Provider Webhook** field, enter the Telegram connector service URL:
   - K3s: `http://ef-telegram-connector-svc:8080`
   - Helm: `http://cx-channels-telegram-connector-svc:8664`
5. Click **Add Custom Attribute** and add the following attribute:

| Attribute Name | Type | Required | Description |
|---|---|---|---|
| `BOT-TOKEN` | String100 | Yes | The unique Bot Token from BotFather that identifies your Telegram bot |

6. Click **Save**.

## Step 3: Configure Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Click **Add new Channel Connector** and name it (e.g., **Telegram Channel Connector**).
3. Select the **Channel Provider Interface** created in Step 2 (e.g., Telegram Channel Provider).
4. The custom attribute fields from Step 2 will appear. Enter:
   - **BOT-TOKEN**: Your Telegram bot token from BotFather.
5. Click **Save**.

## Step 4: Configure Channel

1. Navigate to **Channel Manager → Channel**.
2. Find the **TELEGRAM** channel type and click **Add new channel**.
3. Fill in the channel details:
   - **Name**: e.g., `Telegram DM`
   - **Service Identifier**: Your Telegram bot's numeric ID, retrieved by calling the Telegram API:
     ```
     GET https://api.telegram.org/bot<YOUR-BOT-TOKEN>/getMe
     ```
     The `id` field in the response is your Service Identifier.
   - **Bot ID**: Select the default bot (e.g., `EF-Bot`) from the dropdown.
   - **Channel Connector**: Select the connector created in Step 3.
   - **Customer Activity Timeout**: 180 seconds (recommended)
   - **Channel Mode**: HYBRID
   - **Agent Selection Policy**: LONGEST AVAILABLE
   - **Agent Request TTL**: 100 seconds
   - **Routing Mode**: PUSH (queue-based) or PULL (agent-selected)
4. Click **Save**.

## Step 5: Register the Webhook

After completing the Unified Admin configuration, register the Telegram webhook to start receiving messages:

**POST** `https://<YOUR-FQDN>/telegram-connector/register-webhook`

**Request body:**
```json
{
  "botToken": "<YOUR-BOT-TOKEN>",
  "url": "https://<YOUR-FQDN>"
}
```

> **Note**: Only HTTPS URLs are supported. The `url` field must use a valid public domain. Ngrok URLs are not supported.

**Expected response (success):**
```json
{
  "ok": true,
  "result": true,
  "description": "Success",
  "errorCode": null,
  "status": "OK"
}
```

After successful webhook registration, customers can search for your bot by name in Telegram and begin chatting.

## Verify the Setup

1. Search for your bot name in the Telegram app.
2. Send a test message.
3. Confirm the message appears as an incoming request in the Agent Desk.
4. Accept and reply — confirm the reply reaches the Telegram customer.

## Related Articles

- [Telegram Bot Creation Guide](Telegram-Bot-Creation-Guide.md)
- [Telegram Channel Overview](index.md)
- [Telegram Connector Limitations](Telegram-Connector-Limitations.md)
- [Telegram Media Types Support](Telegram-Media-Types.md)
- [Channel and Connector Setup](../../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
