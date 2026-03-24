---
title: "Facebook Channel Configuration Guide"
summary: "Step-by-step guide for connecting ExpertFlow CX to Facebook — covering Facebook App creation, webhook setup, Messenger configuration, app permission approval, long-lived Page Access Token generation, and Unified Admin configuration."
audience: [administrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["facebook configuration CX", "facebook connector setup", "facebook app developer portal", "page access token CX", "facebook webhook setup", "facebook messenger CX", "facebook channel unified admin", "facebook graph API CX"]
aliases: ["facebook connector CX", "facebook integration guide", "configure facebook CX"]
last-updated: 2026-03-10
---

# Facebook Channel Configuration Guide

This guide covers the end-to-end process of connecting ExpertFlow CX to a Facebook Page — including Facebook App creation, permission approval, long-lived Page Access Token generation, and Unified Admin configuration.

## Prerequisites

- A Facebook account and a Facebook Developer account
- Admin access to the Facebook Page you intend to connect
- The Facebook connector deployed in your CX environment (required before configuring webhooks)

---

## Part 1: Create a Facebook App on the Developer Platform

### Step 1: Create a Developer Account

Create a Facebook Developer account at [developers.facebook.com](https://developers.facebook.com/). You must have a standard Facebook account first.

### Step 2: Create the Facebook App

1. Go to the [Apps panel](https://developers.facebook.com/apps) and click **Create App**.
2. Select **Other** and click **Next**.
3. Select App Type **Business** and click **Next**.
4. Enter an **App Name** and a developer notification email address.
5. Optionally link a Facebook Business Manager account.
6. Click **Create App**.

Your app dashboard opens where you can configure settings, roles, and products.

### Step 3: Add Webhook and/or Messenger Product

> Complete this step only after the Facebook connector is deployed in your environment.

#### A. Add Webhook (for Page Comments)

1. Go to **Add Product** and select **Webhooks**.
2. Select **Webhooks** from the left navigation menu.
3. Select **Page** as the object and click **Subscribe to this object**.
4. Enter the webhook URL:
   ```
   https://{SERVER-FQDN}/facebook-connector/webhook/{PAGE-ID}
   ```
5. Enter the **Verify Token** — this must match the `FACEBOOK-PAGE-ACCESS-TOKEN` value configured in Unified Admin.
6. Click **Verify & Save**.
7. Subscribe to the **feed** field on the App dashboard.

#### B. Add Messenger (for Direct Messages)

1. Go to **Add Product** and select **Messenger**.
2. Select **Messenger** from the left navigation menu.
3. In the **Access Token** section, click **Add or remove Page**.
4. Select **Opt in to current Pages only**, then select your target Page and click **Continue**.
5. Click **Save**.
6. Find and click **Add subscriptions**.
7. Select the **messages** field and save.

### Step 4: App Permissions and Approval

To receive messages from public users (not just developers/testers), you must request and receive Facebook approval for the required permissions.

| Use Case | Required Permissions |
|---|---|
| **Messenger DM** | `pages_messaging` |
| **Page Comments / Posts** | `pages_manage_metadata`, `pages_read_user_content`, `pages_manage_engagement` |

**Submitting for approval:**

1. Go to **App Review → Permissions and Features**.
2. Find the required permission and click **Get advanced access**.
3. Agree to the Terms and click **Confirm**.
4. Scroll to **Review your app settings** and complete the form:
   - Enter your Privacy Policy URL (must be hosted and publicly accessible).
   - Select **Messaging** as the App Category.
5. Scroll to **Complete App verification** and complete the form:
   - Provide step-by-step testing instructions for the Facebook review team including: test Facebook account, Page URL, AgentDesk credentials, how to send/receive messages, why each permission is needed, and a screencast demonstration.
6. Submit and repeat for each permission.

Once all permissions are approved, switch your App from **Development Mode** to **Live Mode**.

---

## Part 2: Grant User Access to the App

To add another Facebook user as an app administrator or developer:

1. Log in to Facebook with the account that owns the app.
2. Open the [Facebook Developer platform](https://developers.facebook.com/apps) and select the app.
3. Expand **Roles** and click **Roles**.
4. Click **Add** next to the appropriate role (Admin, Developer, or Tester).
5. Search for the user by full name or Facebook username (found at `facebook.com/settings/?tab=profile`).
6. Ask the invited user to accept the invitation via the notification tray in their Facebook Developer account.

---

## Part 3: Generate a Long-Lived Page Access Token

Facebook API calls require a **Long-Lived Page Access Token** (never expires). Generate it using the following three-step process.

### Step 1: Generate a Short-Lived User Access Token (valid 1 hour)

1. Open the [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Change the query from `me?fields=id,name` to `me/accounts`.
3. Select your App from the **Meta App** dropdown.
4. From **User or Page**, select **Get User Access Token**.
5. Select the required permissions and click **Generate Access Token**.
6. Copy and save the short-lived user access token and the **Page ID** (`id`) from the response.

### Step 2: Exchange for a Long-Lived User Access Token (valid 60 days)

Using the Expertflow Postman workspace, call the long-lived user access token endpoint:

- Replace `client_id` with your **App ID** (from App Settings → Basic).
- Replace `client_secret` with your **App Secret**.
- Replace `fb_exchange_token` with the short-lived user access token from Step 1.
- Click **Send** and save the returned long-lived user access token.

### Step 3: Exchange for a Long-Lived Page Access Token (never expires)

Using the Expertflow Postman workspace, call the long-lived page access token endpoint:

- Replace `{PAGE-ID}` in the URL with your Page ID from Step 1.
- Replace `access_token` with the long-lived user access token from Step 2.
- Click **Send** and save the returned **Long-Lived Page Access Token** securely.

---

## Part 4: Unified Admin Configuration

### Step 1: Create Channel Type and Provider

1. Navigate to **Channel Manager → Channel Type**.
2. Create a new Channel Type named **Facebook** (if it does not already exist).
3. In the **Provider Webhook** field, enter the Facebook connector service URL:
   - K3s: `http://ef-facebook-connector-svc:8080`
   - Helm: `http://cx-channels-facebook-connector-svc:8080`
4. Add the following custom attributes:

   | Attribute | Data Type |
   |---|---|
   | `FACEBOOK-HOST-URL` | URL |
   | `FACEBOOK-API-KEY` | String 2000 |
   | `FACEBOOK-PAGE-ACCESS-TOKEN` | String 2000 |
   | `EDIT_MESSAGE_SUPPORT_SM` | Boolean |

5. Click **Save**.

### Step 2: Create Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Enter a name for the connector.
3. Select the **Facebook** Channel Provider Interface.
4. In **FACEBOOK-HOST-URL**, enter: `https://graph.facebook.com/v15.0/` (include the trailing `/`).
5. In **FACEBOOK-API-KEY**, enter the Long-Lived Page Access Token.
6. In **FACEBOOK-PAGE-ACCESS-TOKEN**, enter the Verify Token used during webhook registration.
7. Set **EDIT_MESSAGE_SUPPORT_SM** to `true` to enable message editing for social media comments.
8. Click **Save**.

### Step 3: Create Channel

1. Navigate to **Channel Manager → Channel**.
2. Enter a channel name.
3. In **Service Identifier**, enter the **Facebook Page ID**.
4. Fill in the remaining fields (Queue, Bot, routing settings) and click **Save**.

---

## Optional: Fix Webhook Subscription for Post Comments

If webhook events are received for DMs but not for page comments:

1. Open the [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
2. Run a GET request to `<page-id>/subscribed_apps` and check the fields returned.
3. If both `messages` and `feed` are not present, run a POST request:
   ```
   POST <page-id>/subscribed_apps?subscribed_fields=feed,messages
   ```

## Related Articles

- [Channel and Connector Setup](Channel-and-Connector-Setup.md)
- [Facebook Connector Limitations](../Developer_Integrator/Facebook-Connector-Limitations.md)
- [WhatsApp Cloud API Configuration](WhatsApp-Cloud-API-Configuration.md)
- [Instagram Connector Configuration Guide](Instagram-Connector-Configuration-Guide.md)
