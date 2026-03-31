---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Instagram Connector Configuration & Deployment

Integrating Instagram with Expertflow CX is achieved via the Meta Graph API. This guide covers the setup of the Facebook App, Webhooks, and Connector settings.

## 1. Facebook App Setup
1. Create a **Business App** on the [Facebook Developer Platform](https://developers.facebook.com).
2. Add the **Instagram Messenger** and **Webhooks** products.
3. Link your **Facebook Page** to your **Instagram Professional Account** (Business or Creator).

## 2. Webhook Configuration
- **Callback URL**: `https://{SERVER-FQDN}/instagram-connector/webhook/{INSTAGRAM-USER-ID}`
- **Verify Token**: Must match the `INSTAGRAM-PAGE-ACCESS-TOKEN` in Unified Admin.
- **Subscriptions**: Subscribe to `messages` and `comments`.

## 3. Permissions & Approval
To access public user content, your app must be approved for the following permissions:
- `instagram_basic`
- `instagram_manage_messages`
- `instagram_manage_comments`
- `pages_manage_metadata`

## 4. Page Access Token
Generate a **Long-Lived Page Access Token** (never expires) using the Graph API Explorer:
1. Get a short-lived User Token.
2. Exchange it for a long-lived User Token (60 days).
3. Use the long-lived User Token to request the non-expiring Page Access Token for your specific page.

## 5. Unified Admin Settings
### Channel Provider
- **Provider Webhook**: `http://ef-instagram-connector-svc:8080` (K3s).
- **Custom Attributes**: `INSTAGRAM-HOST-URL` (URL), `INSTAGRAM-API-KEY` (String 2000), `INSTAGRAM-PAGE-ACCESS-TOKEN` (String 100).

### Channel Connector
- **INSTAGRAM-HOST-URL**: `https://graph.facebook.com/v15.0/`
- **INSTAGRAM-API-KEY**: Your Long-Lived Page Access Token.
- **INSTAGRAM-PAGE-ACCESS-TOKEN**: Your Webhook Verify Token.

### Channel
- **Service Identifier**: Your **Instagram User ID**.
- **Mode**: `HYBRID`.
- **Routing**: `PUSH` or `PULL`.
