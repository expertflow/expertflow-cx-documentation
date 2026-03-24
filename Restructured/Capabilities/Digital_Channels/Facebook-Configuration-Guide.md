---
title: "Facebook Configuration Guide"
summary: "How-to guide for configuring the Facebook channel connector in ExpertFlow CX — covering Facebook App creation, Page Access Token generation, Unified Admin setup, and webhook registration."

product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["Facebook configuration", "Facebook connector setup", "Facebook App", "Page Access Token", "Facebook webhook", "Unified Admin Facebook", "Facebook Messenger setup"]
aliases: ["Facebook connector configuration", "Facebook channel setup", "configure Facebook"]
last-updated: 2026-03-10
---

# Facebook Configuration Guide

This guide walks through the complete setup of the Facebook channel connector in ExpertFlow CX, from creating the Facebook App to configuring channels in Unified Admin.

## Prerequisites

- A Facebook account with admin access to the business Facebook Page.
- The Facebook connector deployed in your CX environment (confirm the service name and port with your deployment team).
- Basic familiarity with the Facebook Developer Platform.

## Part 1: Create the Facebook App

### 1.1 Create a Developer Account

Register at [https://developers.facebook.com](https://developers.facebook.com). You must have an existing Facebook account to create a developer account.

### 1.2 Create a Facebook App

1. Navigate to the **Apps** panel at https://developers.facebook.com/apps and click **Create App**.
2. Select **Other** and click **Next**.
3. Select **App Type: Business** and click **Next**.
4. Enter the **App Name** and a notification email address.
5. Optionally link a Facebook Business Manager account.
6. Click **Create App**.

### 1.3 Add Webhook and Messenger Products

> **Important**: Complete this step only after the Facebook connector is deployed in your environment.

#### A. Webhook (for Social Media Comments)

1. On the App Dashboard, click **Add Product** and select **Webhooks**.
2. In the left navigation, select **Webhooks**, then select **Page** as the object type.
3. Click **Subscribe to this object** and provide:
   - **Webhook URL**: `https://<YOUR-FQDN>/facebook-connector/webhook/<PAGE-ID>`
   - **Verify Token**: Use the same value you will set as `FACEBOOK-PAGE-ACCESS-TOKEN` in Unified Admin (see Part 3).
4. Click **Verify & Save**.
5. On the App Dashboard, subscribe to the **feed** field.

#### B. Messenger (for Direct Messages)

1. On the App Dashboard, click **Add Product** and select **Messenger**.
2. In the left navigation, select **Messenger**, then find the **Access Token** section.
3. Click **Add or remove Page** and select **Opt in to current Pages only**.
4. Select your Facebook Page and click **Continue**, then **Save**.
5. Click **Add subscriptions** and select the **messages** field.

### 1.4 Request App Permissions

To receive content from public users (not just page admins), your app requires Facebook review and approval for the following permissions:

**For Messenger (DM):**
- `pages_messaging`

**For Social Media Comments:**
- `pages_manage_metadata`
- `pages_read_user_content`
- `pages_manage_engagement`

**Approval process:**
1. Go to **App Review → Permissions and Features** in the developer portal.
2. For each permission, click **Get advanced access** and complete the review form.
3. Submit the form with: your privacy policy URL, app category (Messaging), a step-by-step test procedure for reviewers, and a screencast demonstration.
4. Repeat for each permission.
5. Once all permissions are approved, switch your App to **Live Mode** to access public content.

## Part 2: Generate a Long-Lived Page Access Token

The Facebook connector requires a permanent (non-expiring) Page Access Token. Generate it in three stages:

### 2.1 Generate a Short-Lived User Access Token

1. Open the [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Change the query from `me?fields=id,name` to `me/accounts`.
3. Select your app in the **Meta App** dropdown.
4. Click **Get User Access Token** and select the required permissions.
5. Click **Generate Access Token** and copy the token. Also copy the **Page ID** (`id`) from the response.

### 2.2 Exchange for a Long-Lived User Access Token (60 days)

Use the Graph API to exchange the short-lived token:
- `GET https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=<APP-ID>&client_secret=<APP-SECRET>&fb_exchange_token=<SHORT-LIVED-TOKEN>`
- Copy the returned access token.

### 2.3 Generate the Long-Lived Page Access Token (never expires)

- `GET https://graph.facebook.com/<PAGE-ID>/accounts?access_token=<LONG-LIVED-USER-TOKEN>`
- The `access_token` value in the response is your **Long-Lived Page Access Token**. Store it securely.

## Part 3: Unified Admin Configuration

### 3.1 Channel Type

1. In Unified Admin, go to **Channel Manager → Channel Type**.
2. Create a new Channel Type named **Facebook** (if it does not already exist).
3. In the **Provider Webhook** field, enter the Facebook connector service URL:
   - K3s: `http://ef-facebook-connector-svc:8080`
   - Helm: `http://cx-channels-facebook-connector-svc:8080`
4. Add the following custom attributes:

| Attribute Name | Type | Purpose |
|---|---|---|
| `FACEBOOK-HOST-URL` | URL | Facebook Graph API base URL |
| `FACEBOOK-API-KEY` | String 2000 | Long-Lived Page Access Token |
| `FACEBOOK-PAGE-ACCESS-TOKEN` | String 2000 | Verify token for webhook registration |
| `EDIT_MESSAGE_SUPPORT_SM` | Boolean | Enable/disable comment editing for Social Media |

5. Click **Save**.

### 3.2 Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Create a new connector and provide a name (e.g., **Facebook Connector**).
3. Select the Channel Provider Interface created in the previous step.
4. Fill in the attribute values:
   - **FACEBOOK-HOST-URL**: `https://graph.facebook.com/v15.0/` (note the trailing slash)
   - **FACEBOOK-API-KEY**: The Long-Lived Page Access Token from Part 2
   - **FACEBOOK-PAGE-ACCESS-TOKEN**: The Verify Token used in Step 1.3.A
   - **EDIT_MESSAGE_SUPPORT_SM**: `true` to enable comment editing
5. Click **Save**.

### 3.3 Channel

1. Navigate to **Channel Manager → Channel**.
2. Create a new channel under the Facebook channel type.
3. **Service Identifier**: Enter the **Facebook Page ID** obtained in Step 2.1.
4. Fill in the remaining fields (Queue, Routing Mode, etc.) and click **Save**.

## Part 4: Verify Webhook Subscriptions (Optional)

If you are not receiving events for comments but receive DM events:

1. In the Graph API Explorer, run: `GET <page-id>/subscribed_apps`
2. Check that both `messages` and `feed` appear in the subscribed fields.
3. If `feed` is missing, run: `POST <page-id>/subscribed_apps?subscribed_fields=feed,messages`
4. Both event types should now be delivered to your webhook.

## Related Articles

- [Facebook Channel Overview](Facebook-Channel-Overview.md)
- [Facebook Connector Limitations](Facebook-Connector-Limitations.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
