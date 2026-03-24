---
title: "Email Channel Configuration Guide (IMAP/SMTP)"
summary: "Step-by-step guide for configuring an IMAP/SMTP-based email channel in ExpertFlow CX — covering Gmail App Password generation, Unified Admin setup for MRD, Channel Type, Channel Provider, Channel Connector, Channel, and webhook registration."
audience: [administrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["email channel CX", "IMAP SMTP configuration", "gmail email connector CX", "email channel setup unified admin", "email MRD CX", "CX email integration", "IMAP connector setup", "SMTP connector CX"]
aliases: ["email connector setup CX", "IMAP SMTP email CX", "configure email channel CX"]
last-updated: 2026-03-10
---

# Email Channel Configuration Guide (IMAP/SMTP)

This guide explains how to set up an IMAP/SMTP-based email channel in ExpertFlow CX. The email connector uses **IMAP** for receiving and **SMTP** for sending, with a pull-mode mechanism that polls the mailbox at a configured interval.

> The currently supported mailbox is **Gmail**. IMAP and SMTP support are enabled by default in Gmail accounts.

## Prerequisites

- A Gmail account to use as the email channel inbox
- 2-Step Verification enabled on the Gmail account
- An App Password generated for the Gmail account (see Step 1)

---

## Step 1: Generate a Gmail App Password

Standard Gmail passwords do not work with IMAP/SMTP connectors. You must generate an App Password.

1. Go to your [Google Account](https://myaccount.google.com/) and open the **Security** tab.
2. Under **2-Step Verification**, scroll down and click **App passwords**.
3. Enter an app name (e.g., `CX Email Connector`) and click **Create**.
4. Copy and save the generated App Password — you will need it during connector setup.

> IMAP and SMTP settings are enabled by default on Gmail. No additional Google-side configuration is required.

---

## Step 2: Create an MRD in Unified Admin

1. Navigate to **Unified Admin → Routing Engine → MRD**.
2. Click **Add** and set:
   - **Name**: e.g., `Email MRD`
   - **MRD Type**: `EMAIL`
   - **Max Task Request**: `5`
3. Click **Save**.

---

## Step 3: Create a Channel Type

1. Navigate to **Channel Manager → Channel Type**.
2. Check if an Email channel type already exists. If not, create one.
3. Set the **MRD** to `EMAIL`.
4. Upload a channel icon if not already present.
5. Click **Save**.

---

## Step 4: Create a Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Set a name, e.g., `Email Provider`.
3. Select **Channel Type**: `EMAIL`.
4. In **Provider Webhook**, enter the email connector service URL:
   ```
   http://cx-channels-email-connector-svc:8080
   ```
5. Add the following **11 custom attributes**:

   | Attribute | Data Type |
   |---|---|
   | `IMAP-HOST` | String(100) |
   | `IMAP-USERNAME` | String(100) |
   | `IMAP-PORT` | PositiveNumber |
   | `IMAP-PASSWORD` | String(100) |
   | `IMAP-SSL-ENABLED` | Boolean |
   | `SMTP-HOST` | String(100) |
   | `SMTP-USERNAME` | String(100) |
   | `SMTP-PASSWORD` | String(100) |
   | `SMTP-PORT` | PositiveNumber |
   | `SMTP-AUTH` | Boolean |
   | `SMTP-TTLS-ENABLE` | Boolean |

6. Click **Save**.

---

## Step 5: Create a Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Set a name, e.g., `Email Connector`.
3. Select **Channel Provider**: `Email Provider`.
4. Fill in the connector values:

   | Field | Value |
   |---|---|
   | `IMAP-HOST` | `imap.gmail.com` |
   | `IMAP-USERNAME` | Your business email address |
   | `IMAP-PORT` | `993` |
   | `IMAP-PASSWORD` | App Password generated in Step 1 |
   | `IMAP-SSL-ENABLED` | `true` |
   | `SMTP-HOST` | `smtp.gmail.com` |
   | `SMTP-USERNAME` | Same email as IMAP-USERNAME |
   | `SMTP-PASSWORD` | Same App Password as IMAP-PASSWORD |
   | `SMTP-PORT` | `587` |
   | `SMTP-AUTH` | `true` |
   | `SMTP-TTLS-ENABLE` | `true` |

5. Click **Save**.

---

## Step 6: Create a Channel

1. Navigate to **Channel Manager → Channel** and expand the Email section.
2. Click **Add new Channel**.
3. Fill in the channel settings:

   | Field | Value |
   |---|---|
   | **Name** | e.g., `Email Channel` |
   | **Service Identifier** | The email address used in SMTP-USERNAME and IMAP-USERNAME |
   | **Bot** | Select from the dropdown |
   | **Channel Connector** | `Email Connector` |
   | **Customer Activity Timeout (sec)** | `300` (5 minutes, adjust as needed) |
   | **Channel Mode** | `HYBRID` |
   | **Routing Mode** | `PULL` |
   | **Agent Selection Policy** | `LONGEST AVAILABLE` |
   | **Agent Request TTL (sec)** | `300` (adjust as needed) |

4. Click **Save**.

---

## Step 7: Register the Webhook

After completing Unified Admin configuration, register the email connector by making a POST request to the webhook endpoint.

**Endpoint:**
```
POST https://{FQDN}/email-connector/channel-type-configurations
```

**Request body:**
```json
{
  "channelTypeId": "<id-of-email-channel-type>"
}
```

> Retrieve the `channelTypeId` from the Channels List API by searching for the EMAIL channel type entry.

A successful response confirms the email connector is active and ready to receive emails.

---

## Related Articles

- [Email Configuration Guide — MS Exchange](../../Capabilities/Digital_Channels/Email-Configuration-MS-Exchange.md)
- [Channel and Connector Setup](Channel-and-Connector-Setup.md)
- [Media Routing Domains (MRD) Overview](Media-Routing-Domains-MRD-Overview.md)
- [Managing Outbound Campaigns](Managing-Outbound-Campaigns.md)
