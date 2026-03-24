---
title: "Twitter Configuration Guide"
summary: "How-to guide for setting up a Twitter Developer Account with API v2 credentials and configuring the Twitter channel connector in ExpertFlow CX Unified Admin."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["Twitter configuration", "Twitter connector setup", "Twitter Developer Portal", "Twitter API v2", "Twitter Unified Admin", "CONSUMER-KEY", "BEARER-TOKEN", "Twitter channel setup"]
aliases: ["configure Twitter connector", "Twitter CX setup", "Twitter API configuration"]
last-updated: 2026-03-10
---

# Twitter Configuration Guide

This guide walks through creating a Twitter Developer Account with API v2 credentials and configuring the Twitter channel connector in ExpertFlow CX Unified Admin.

## Prerequisites

- A Twitter account for your business or brand.
- Access to Unified Admin with Channel Manager permissions.
- The Twitter connector deployed in your CX environment.

---

## Part 1: Set Up a Twitter Developer Account

### Step 1: Sign In to Twitter

Go to [twitter.com](https://twitter.com) and sign in with your business Twitter account. If you do not have one, create a new account first.

### Step 2: Apply for a Developer Account

1. Navigate to the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard).
2. Log in with your Twitter credentials.
3. Click **Apply** and complete the developer account application, describing your intended use case.
4. Wait for the email confirmation that your developer account has been approved.

### Step 3: Create a Project and Enable API v2

1. In the Developer Portal, navigate to **Projects & Apps → Overview**.
2. Click **+ New Project** (or **Set up Project** if prompted).
3. Enter a project name and describe the intended use (e.g., "ExpertFlow CX Twitter Integration").
4. Complete the project creation wizard.

### Step 4: Create an App and Generate Credentials

1. Inside your project, click **+ Create App**.
2. Fill in the app details: name, description, and use case.
3. Once the app is created, go to the **Keys and Tokens** tab.
4. Generate and securely store the following five credentials:

| Credential | Description |
|---|---|
| **API Key** (`CONSUMER-KEY`) | Identifies your app to the Twitter API |
| **API Secret Key** (`CONSUMER-SECRET`) | Secret paired with the API Key |
| **Bearer Token** (`BEARER-TOKEN`) | App-only authentication token for read access |
| **Access Token** (`TOKEN-KEY`) | Identifies the Twitter account the app acts on behalf of |
| **Access Token Secret** (`TOKEN-SECRET`) | Secret paired with the Access Token |

> **Important**: Store all five credentials securely. The Bearer Token and Access Token Secret are displayed only once during generation.

---

## Part 2: Unified Admin Configuration

### Step 1: Initial Setup

Before configuring the channel, create the required routing objects in Unified Admin:

1. Navigate to **Unified Admin → Routing Engine → MRD** and create an MRD for Twitter (type: **CHAT** or the applicable type).
2. Create a **Routing Attribute** for Twitter agents.
3. Create a **Queue** dedicated to Twitter interactions.
4. Assign the MRD to the relevant agents and define their routing attributes.

### Step 2: Configure Channel Type

1. Navigate to **Channel Manager → Channel Type**.
2. The Twitter channel type (`TWITTER`) is bootstrapped automatically during connector deployment. Confirm it appears in the list.
3. If not present, create it manually with MRD type set to **CHAT**.

### Step 3: Configure Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Create a new Channel Provider (e.g., **Twitter Channel Provider**).
3. Select **TWITTER** as the Channel Type.
4. In the **Provider Webhook** field, enter the Twitter connector service URL:
   - K3s: `http://ef-twitter-connector-svc:8080`
   - Helm: `http://cx-channels-twitter-connector-svc:8080`
5. Add the following **5 custom attributes** (all type `String2000`, marked as **Required**):

| Attribute Name | Description |
|---|---|
| `CONSUMER-KEY` | Twitter API Key |
| `CONSUMER-SECRET` | Twitter API Secret Key |
| `TOKEN-KEY` | Access Token |
| `TOKEN-SECRET` | Access Token Secret |
| `BEARER-TOKEN` | Bearer Token |

6. Click **Save**.

### Step 4: Configure Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Create a new Channel Connector (e.g., **Twitter Channel Connector**).
3. Select the Channel Provider created in Step 3 (Twitter Channel Provider).
4. Enter the five API credentials generated in Part 1 into their respective fields.
5. Click **Save**.

### Step 5: Configure Channel

1. Navigate to **Channel Manager → Channel**.
2. Expand the **TWITTER** section and click **Add new channel**.
3. Fill in the channel details:
   - **Name**: e.g., `Twitter`
   - **Service Identifier**: Your Twitter Account ID (numeric ID)
   - **Bot**: Select EF-Bot or your configured default bot
   - **Channel Connector**: Select **Twitter Channel Connector**
   - **Customer Activity Timeout**: 180 seconds (adjust as needed)
   - **Channel Mode**: HYBRID
   - **Routing Mode**: PUSH or PULL
   - **Queue or List**: Select based on routing mode
   - **Agent Selection Policy**: LONGEST AVAILABLE
   - **Agent Request TTL**: 100 seconds
4. Click **Save**.

---

## Part 3: Register the Channel Type

After completing Unified Admin configuration, activate the connector by registering the channel type:

1. Fetch the `channelTypeId` for TWITTER by calling the channels list API.
2. Send a POST request to register the channel type:

**POST** `https://<YOUR-FQDN>/twitter-connector/channel-type-configurations`

**Request body:**
```json
{
  "channelTypeId": "<TWITTER-CHANNEL-TYPE-ID>"
}
```

**Expected response**: HTTP 200 confirming the Twitter channel type configuration was applied.

---

## Runtime Behaviour

After registration, the Twitter connector runs in **PULL MODE**:

- The connector periodically polls Twitter's API to fetch new messages, replies, and mentions.
- Poll frequency is governed by Twitter API rate limits and the connector's scheduled interval.
- New messages appear as incoming interaction requests in the Agent Desk.

---

## Related Articles

- [Twitter Channel Overview](Twitter-Channel-Overview.md)
- [Twitter Connector Limitations](../../How-to_Guides/Administrator/Twitter-Connector-Limitations.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
