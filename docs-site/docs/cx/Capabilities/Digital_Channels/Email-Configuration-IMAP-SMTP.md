---
title: "Email Configuration — IMAP/SMTP"
summary: "How-to guide for configuring the Email channel connector using IMAP and SMTP protocols in ExpertFlow CX — covering Gmail app password setup and full Unified Admin configuration."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["Email IMAP SMTP configuration", "Gmail email connector", "email channel setup", "IMAP configuration", "SMTP configuration", "Unified Admin email", "email connector setup"]
aliases: ["email IMAP setup", "Gmail email connector", "configure email IMAP SMTP"]
last-updated: 2026-03-10
---

# Email Configuration — IMAP/SMTP

This guide covers configuring the Email channel connector using **IMAP** (for receiving emails) and **SMTP** (for sending emails) protocols. The current primary supported mailbox is **Gmail**. Other IMAP/SMTP-compatible mailboxes may work with appropriate server settings.

## Prerequisites

- A Gmail account (or IMAP/SMTP-compatible mailbox) designated as the business email channel.
- The Email connector deployed in your CX environment.
- An MRD of type **EMAIL** created in Unified Admin.

## Part 1: Generate a Gmail App Password

Gmail requires an App Password for third-party IMAP/SMTP access when using 2-Step Verification.

1. Sign in to your Google account and navigate to **Security**.
2. Scroll to **2-Step Verification** and open it. _(Enable 2-Step Verification if not already active.)_
3. Scroll to **App passwords** and click it.
4. Enter an app name (e.g., `ExpertFlow CX Email`) and click **Create**.
5. Copy the generated 16-character app password. **Store it securely** — you will need it in Part 2.

> **Note**: IMAP and SMTP are enabled by default in Gmail accounts.

## Part 2: Unified Admin Configuration

### Step 1: Configure MRD

1. Navigate to **Unified Admin → Routing Engine → MRD**.
2. Create a new MRD:
   - **Name**: e.g., `Email MRD`
   - **MRD Type**: EMAIL
   - **Max Task Request**: 5 (adjust as needed)
3. Click **Save**.

### Step 2: Configure Channel Type

1. Navigate to **Channel Manager → Channel Type**.
2. The Email channel type should already be present in the list (bootstrapped by default).
3. Select the **EMAIL** MRD created in Step 1.
4. Upload the email channel icon if not already present.
5. Click **Save**.

### Step 3: Configure Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Create a new Channel Provider (e.g., **Email Provider**).
3. Select **EMAIL** as the Channel Type.
4. In the **Provider Webhook** field, enter the Email connector service URL:
   - Example: `http://cx-channels-email-connector-svc:8080`
5. Add the following custom attributes:

| Attribute Name | Type |
|---|---|
| `IMAP-HOST` | String100 |
| `IMAP-USERNAME` | String100 |
| `IMAP-PORT` | PositiveNumber |
| `IMAP-PASSWORD` | String100 |
| `IMAP-SSL-ENABLED` | Boolean |
| `SMTP-HOST` | String100 |
| `SMTP-USERNAME` | String100 |
| `SMTP-PASSWORD` | String100 |
| `SMTP-PORT` | PositiveNumber |
| `SMTP-AUTH` | Boolean |
| `SMTP-TTLS-ENABLE` | Boolean |

6. Click **Save**.

### Step 4: Configure Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Create a new Channel Connector (e.g., **Email Connector**).
3. Select the Channel Provider created in Step 3 (Email Provider).
4. Fill in the attribute values for Gmail:

| Attribute | Value |
|---|---|
| `IMAP-HOST` | `imap.gmail.com` |
| `IMAP-USERNAME` | Your business Gmail address |
| `IMAP-PORT` | `993` |
| `IMAP-PASSWORD` | App Password generated in Part 1 _(not your regular Gmail password)_ |
| `IMAP-SSL-ENABLED` | `true` |
| `SMTP-HOST` | `smtp.gmail.com` |
| `SMTP-USERNAME` | Same Gmail address as IMAP-USERNAME |
| `SMTP-PASSWORD` | Same App Password |
| `SMTP-PORT` | `587` |
| `SMTP-AUTH` | `true` |
| `SMTP-TTLS-ENABLE` | `true` |

5. Click **Save**.

### Step 5: Configure Channel

1. Navigate to **Channel Manager → Channel**.
2. Click **Add new channel** under the **Email** channel type.
3. Fill in the channel details:
   - **Name**: e.g., `Email Channel`
   - **Service Identifier**: The exact Gmail address used in `IMAP-USERNAME` and `SMTP-USERNAME`
   - **Bot**: Select from the dropdown list
   - **Channel Connector**: Select **Email Connector**
   - **Customer Activity Timeout**: 300 seconds (5 minutes; adjust as needed)
   - **Channel Mode**: HYBRID
   - **Routing Mode**: PULL _(works best in PULL mode for email)_
   - **Queue or List**: Select based on routing mode
   - **Agent Selection Policy**: LONGEST AVAILABLE
   - **Agent Request TTL**: 300 seconds
4. Click **Save**.

## Part 3: Register the Webhook

After completing Unified Admin configuration, register the webhook to activate the email connector:

**POST** `https://<YOUR-FQDN>/email-connector/channel-type-configurations`

**Request body:**
```json
{
  "channelTypeId": "<EMAIL-CHANNEL-TYPE-ID>"
}
```

> Retrieve the `channelTypeId` by calling the channels list API and locating the EMAIL channel type entry.

**Expected response**: HTTP 200 with confirmation that the email channel type configuration was applied.

## Verify the Setup

1. Send a test email to the configured Gmail address from an external account.
2. Wait for the polling interval to complete (or trigger manually if APIs allow).
3. Confirm the email appears as an incoming request in the Agent Desk.
4. Accept, reply, and confirm the reply reaches the original sender.

## Related Articles

- [Email Channel Overview](Email/index.md)
- [Email Limitations](Email-Limitations.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
