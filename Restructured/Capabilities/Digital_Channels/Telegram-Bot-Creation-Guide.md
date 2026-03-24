---
title: "Telegram Bot Creation Guide"
summary: "How-to guide for creating a Telegram bot using BotFather and obtaining the Bot Token required to connect the Telegram channel to ExpertFlow CX."

product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["Telegram bot creation", "BotFather", "Telegram Bot Token", "create Telegram bot", "Telegram setup"]
aliases: ["create Telegram bot", "Telegram BotFather guide", "Telegram bot token setup"]
last-updated: 2026-03-10
---

# Telegram Bot Creation Guide

This guide explains how to create a Telegram bot using BotFather and retrieve the Bot Token needed to configure the Telegram connector in ExpertFlow CX.

## Prerequisites

- An active Telegram account. If you don't have one, register at [https://telegram.org](https://telegram.org) and log in from any device.

## What Is a Telegram Bot?

Telegram bots are special accounts that act as interfaces for server-side applications. The Telegram connector in ExpertFlow CX uses a bot account as the customer-facing endpoint — customers message your business bot, and the message is routed to an agent through the CX platform.

## Steps to Create a Telegram Bot

### Step 1: Open BotFather in Telegram

Search for **@BotFather** in the Telegram app and open the chat.

> **Important**: Verify that the BotFather account shows the **verified tick icon** — this confirms you are using the official Telegram BotFather and not an impersonator.

### Step 2: Send the /newbot Command

Send the following command to BotFather:

```
/newbot
```

### Step 3: Set the Bot Name

BotFather will ask for a name for your bot. Enter your **business name** or any descriptive name — this is the display name customers will see (e.g., `ExpertFlow Support`).

### Step 4: Choose a Username

BotFather will ask for a **username** for the bot.

> **Rules:**
> - The username must be **globally unique** across all Telegram bots.
> - It must end with `bot` (e.g., `expertflow_bot` or `ExpertflowBot`).

### Step 5: Copy the Bot Token

After a successful bot creation, BotFather sends a **Congratulations** message that includes your **Bot Token**.

Example format: `1234567890:ABCDefGhIJklMnopQRSTUvwxyz`

**Store this token securely.** You will need it when configuring the Telegram connector in Unified Admin. See [Telegram Configuration Guide](Telegram-Configuration-Guide.md).

## Retrieve a Lost Bot Token

If you lose your Bot Token, send `/mybots` to BotFather, select your bot, then click **API Token**.

## Customise Your Bot (Optional)

You can edit your bot's profile using BotFather commands:
- `/setdescription` — Update the bot's description
- `/setabouttext` — Update the "About" section
- `/setuserpic` — Upload a profile photo
- `/setname` — Change the display name

## Next Step

After creating the bot, proceed to [Telegram Configuration Guide](Telegram-Configuration-Guide.md) to connect it to ExpertFlow CX through Unified Admin.

## Related Articles

- [Telegram Channel Overview](Telegram-Channel-Overview.md)
- [Telegram Configuration Guide](Telegram-Configuration-Guide.md)
- [Telegram Connector Limitations](Telegram-Connector-Limitations.md)
