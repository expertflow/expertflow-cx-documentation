---
title: "Email Configuration — MS Exchange (EWS)"
summary: "How-to guide for configuring the ExpertFlow CX Email channel connector using Microsoft Exchange Web Services (EWS) — covering prerequisites, required Exchange credentials, full Unified Admin setup, and webhook registration."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["MS Exchange email configuration", "Exchange EWS email connector", "Exchange email CX", "email channel Exchange", "EWS configuration", "Unified Admin Exchange email", "Exchange email setup"]
aliases: ["Exchange email connector", "configure MS Exchange email", "EWS email setup CX"]
last-updated: 2026-03-10
---

# Email Configuration — MS Exchange (EWS)

This guide covers configuring the ExpertFlow CX Email channel connector using **Microsoft Exchange Web Services (EWS)** with an on-premises MS Exchange server (primarily Exchange 2019). For Gmail or other IMAP/SMTP mailboxes, see [Email Configuration — IMAP/SMTP](Email-Configuration-IMAP-SMTP.md).

## Prerequisites

- An on-premises MS Exchange (2019 recommended) account designated as the business email channel.
- **EWS enabled** on the Exchange server and accessible from external applications (or accessible within the network where CX is deployed).
- The MS Exchange Email connector deployed in your CX environment.
- An MRD of type **EMAIL** created in Unified Admin.

## Required Information from Your IT Administrator

Before configuring the connector, collect the following from your Exchange IT admin:

| Item | Description | Example |
|---|---|---|
| **Exchange URI** | EWS endpoint of the Exchange server | `https://mail.company.com/EWS/Exchange.asmx` |
| **Username** | Email address / username of the account | `support@company.com` |
| **Password** | Password for the account | — |
| **Public Email ID** | Publicly visible email address (may differ from internal) | `support@company.com` |
| **Domain Part** | Domain portion of the internal Exchange email address | `mailhost.company.com` |

> The **Domain Part** is the section after `@` in the internal Exchange email address. For `ef.demo@mailhost.company.com`, the domain part is `mailhost.company.com`. It is used by the connector when sending email through Exchange.

## Unified Admin Configuration

### Step 1: Configure MRD

1. Navigate to **Unified Admin → Routing Engine → MRD**.
2. Create a new MRD:
   - **Name**: e.g., `Email MRD`
   - **MRD Type**: EMAIL
   - **Max Task Request**: 5 (adjust as needed)
3. Click **Save**.

### Step 2: Configure Channel Type

1. Navigate to **Channel Manager → Channel Type**.
2. The Email channel type is bootstrapped by default — it should already appear in the list.
3. Select the **EMAIL** MRD created in Step 1.
4. Upload the email channel icon if not already present.
5. Click **Save**.

### Step 3: Configure Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Create a new Channel Provider (e.g., **MS Exchange Email Provider**).
3. Select **EMAIL** as the Channel Type.
4. In the **Provider Webhook** field, enter the MS Exchange Email connector service URL:
   - K3s: `http://cx-channels-ms-email-connector-svc:8080`
   - _(Use `kubectl get svc -n expertflow` to confirm the service name in your environment.)_
5. Add the following **5 custom attributes**:

| Attribute Name | Type |
|---|---|
| `USERNAME` | String100 |
| `PASSWORD` | Password |
| `EXCHANGE-URI` | String2000 |
| `PUBLIC-EMAIL-ID` | String2000 |
| `DOMAIN-PART` | String100 |

6. Click **Save**.

### Step 4: Configure Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Create a new Channel Connector (e.g., **MS Exchange Email Connector**).
3. Select the Channel Provider created in Step 3 (MS Exchange Email Provider).
4. Fill in the attribute values:

| Attribute | Value |
|---|---|
| `USERNAME` | The username / email address received from your IT admin |
| `PASSWORD` | The password for the above account |
| `EXCHANGE-URI` | The Exchange EWS endpoint, e.g., `https://mail.company.com/EWS/Exchange.asmx` |
| `PUBLIC-EMAIL-ID` | The publicly visible email address for this channel |
| `DOMAIN-PART` | The domain part of the internal Exchange email, e.g., `mailhost.company.com` |

5. Click **Save**.

### Step 5: Configure Channel

1. Navigate to **Channel Manager → Channel**.
2. Click **Add new channel** under the **Email** channel type.
3. Fill in the channel details:
   - **Name**: e.g., `MS Exchange Email Channel`
   - **Service Identifier**: The email address used in `USERNAME`
   - **Bot**: Select from the dropdown list
   - **Channel Connector**: Select **MS Exchange Email Connector**
   - **Customer Activity Timeout**: 300 seconds (adjust as needed)
   - **Channel Mode**: HYBRID
   - **Routing Mode**: PULL _(recommended for Exchange-based deployments)_
   - **Queue or List**: Select based on routing mode
   - **Agent Selection Policy**: LONGEST AVAILABLE
   - **Agent Request TTL**: 300 seconds
4. Click **Save**.

## Register the Webhook

After completing Unified Admin configuration, register the webhook to activate the connector:

**POST** `https://<YOUR-FQDN>/ms-email-connector/channel-type-configurations`

**Request body:**
```json
{
  "channelTypeId": "<EMAIL-CHANNEL-TYPE-ID>"
}
```

> Retrieve the `channelTypeId` by calling the channels list API and locating the EMAIL channel type entry.

**Expected response**: HTTP 200 with confirmation that the MS Exchange email channel type configuration was applied.

## Verify the Setup

1. Send a test email from an external account to the configured Exchange address.
2. Wait for the polling interval to complete.
3. Confirm the email appears as an incoming request in the Agent Desk.
4. Accept, reply, and confirm the reply reaches the original sender.

## Related Articles

- [Email Channel Overview](Email-Channel-Overview.md)
- [Email Configuration — IMAP/SMTP](Email-Configuration-IMAP-SMTP.md)
- [Email Limitations](Email-Limitations.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
