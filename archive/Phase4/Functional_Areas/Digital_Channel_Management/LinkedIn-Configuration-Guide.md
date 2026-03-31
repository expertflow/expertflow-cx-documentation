---
title: "LinkedIn Configuration Guide"
summary: "How-to guide for configuring the LinkedIn connector in ExpertFlow CX — covering LinkedIn App prerequisites, Access Token generation, Unified Admin setup, and webhook registration for real-time comment notifications."
audience: [solution-admin]
product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["LinkedIn configuration", "LinkedIn connector setup", "LinkedIn App", "LinkedIn Access Token", "LinkedIn webhook", "Unified Admin LinkedIn", "Community Management API"]
aliases: ["LinkedIn connector configuration", "LinkedIn channel setup", "configure LinkedIn"]
last-updated: 2026-03-10
---

# LinkedIn Configuration Guide

This guide walks through the complete configuration of the LinkedIn connector in ExpertFlow CX Unified Admin.

## Prerequisites

- A LinkedIn App created in the [LinkedIn Developer Portal](https://www.linkedin.com/developers/) with **Community Management API** access (Standard tier or higher).
- If your app does not have Community Management API access, complete [LinkedIn Account Onboarding](LinkedIn-Account-Onboarding.md) before proceeding.
- The LinkedIn connector deployed in your CX environment.
- Your organisation's LinkedIn Page ID (available from the page dashboard URL: `https://www.linkedin.com/company/<ORGANIZATION-ID>/admin/dashboard/`).

## Part 1: Generate a LinkedIn Access Token

1. Navigate to the [LinkedIn OAuth Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator).
2. Log in with your LinkedIn account if not already logged in.
3. Select your LinkedIn app from the dropdown (if you have multiple apps).
4. Under **Select OAuth 2.0 Scopes**, choose all permissions required for your app.
5. Check the acknowledgement: *"I understand this tool will update my app's redirect URL settings."*
6. Click **Request access token**.
7. Authorize the app when prompted and copy the generated Access Token.

> The generated token is used as the **Refresh Token** in the CX connector configuration.

## Part 2: Unified Admin Configuration

### 2.1 Channel Type

1. In Unified Admin, go to **Channel Manager → Channel Type**.
2. Create a new Channel Type (if it doesn't exist). Name it **LinkedIn**.
3. Select **Chat** as the MRD type.
4. Click **Save**.

### 2.2 Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Click **Add new Channel Provider** and name it **LinkedIn Provider**.
3. In the **Provider Webhook** field, enter the LinkedIn connector service URL:
   - K3s: `http://ef-linkedin-connector-svc:<PORT>/comments`
   - Helm: `http://cx-channels-linkedin-connector-svc:<PORT>/comments`
4. Add the following custom attributes:

| Attribute Name | Type | Description |
|---|---|---|
| `Organizational-ID` | PositiveNumber | Your LinkedIn organisation ID (from page dashboard URL) |
| `Refresh-Token` | String2000 | Access token from the OAuth Token Generator |
| `Comments-Batch-Size` | PositiveNumber | Number of comments fetched per poll cycle (default: 20) |
| `API-Version` | PositiveNumber | LinkedIn API version (see LinkedIn marketing versioning docs) |
| `Host-Url` | String100 | LinkedIn API base URL |
| `Client-ID` | String100 | App Client ID from the developer portal Auth tab |
| `Client-Secret` | String100 | App Client Secret from the developer portal Auth tab |
| `Start-Time` | AlphanumSpecial200 | Timestamp — comments from this time onward will be routed to agents |
| `EDIT_MESSAGE_SUPPORT_DM` | Boolean | Enable DM comment editing (not currently available) |
| `EDIT_MESSAGE_SUPPORT_SM` | Boolean | Enable Social Media comment editing on Agent Desk |
| `Nested-Comments-Batch-Size` | PositiveNumber | Number of nested comments fetched per cycle (default: 20) |

5. Click **Save**.

### 2.3 Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Click **Add new Channel Connector** and name it **LinkedIn Connector**.
3. Select **LinkedIn Provider** as the Channel Provider Interface.
4. Fill in the connector attribute values:

| Property | Value / Source |
|---|---|
| `Organizational-ID` | From your LinkedIn company page URL |
| `Refresh-Token` | Access token from Part 1 |
| `Comments-Batch-Size` | 20 (recommended default) |
| `API-Version` | Current LinkedIn API version |
| `Host-Url` | LinkedIn API URL |
| `Client-ID` | From developer portal → Auth tab |
| `Client-Secret` | From developer portal → Auth tab |
| `Start-Time` | ISO timestamp for the earliest comment date to retrieve |
| `EDIT_MESSAGE_SUPPORT_SM` | `true` to enable comment editing |
| `Nested-Comments-Batch-Size` | 20 (recommended default) |

5. Click **Save**.

### 2.4 Channel

1. Navigate to **Channel Manager → Channel** and click **Add new channel** under the LinkedIn channel type.
2. Fill in the channel details:
   - **Name**: e.g., `LinkedIn`
   - **Service Identifier**: Your LinkedIn organisation ID
   - **Bot ID**: Select the available Rasa bot from the dropdown
   - **Channel Connector**: Select **LinkedIn Connector**
   - **Customer Activity Timeout**: 300 seconds
   - **Channel Mode**: HYBRID
   - **Routing Mode**: PUSH or PULL (as required)
   - **Queue**: Select the queue for LinkedIn conversations
   - **Agent Selection Policy**: LONGEST AVAILABLE
   - **Agent Response Time**: 300 seconds
3. Click **Save**.

> **Important**: Restart the LinkedIn connector after saving the channel configuration in Unified Admin.

## Part 3: Webhook Registration (Optional — Standard Tier Only)

Webhooks provide real-time comment notifications instead of polling. Webhooks are only available if your LinkedIn app has **Standard tier access** and are supported from **CX version 4.10.3+**.

> Before enabling webhooks, disable the polling scheduler using the [Scheduler Control APIs](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/folder/21457238-7322ad81-0764-4901-a643-482bf705851b).

### 3.1 Register Webhook in LinkedIn Developer Portal

1. Open your app in the [LinkedIn Developer Portal](https://www.linkedin.com/developers/) and go to the **Webhooks** tab.
2. Click **Create new** and add your webhook URL:
   `https://<YOUR-FQDN>/linkedin-connector/linkedin/webhook/<organizationId>`
3. Check the **Social Action** checkbox.
4. Click **Test this URL** to validate (requires valid Client ID and Client Secret).
5. Click **Save webhook**.

> **Note**: Ngrok URLs are not supported. The webhook endpoint must be a public HTTPS FQDN. Both GET and POST requests must be allowed on the endpoint.

### 3.2 Subscribe to Events

After registering the webhook, subscribe using the LinkedIn Subscriptions API:

```
PUT https://api.linkedin.com/v2/eventSubscriptions/(
  developerApplication:urn%3Ali%3AdeveloperApplication%3A{APP-ID},
  user:urn%3Ali%3Aperson%3A{MEMBER-ID},
  entity:urn%3Ali%3Aorganization%3A{ORG-ID},
  eventType:ORGANIZATION_SOCIAL_ACTION_NOTIFICATIONS
)
```

**Body:**
```json
{
  "webhook": "https://<YOUR-FQDN>/linkedin-connector/linkedin/webhook/<organizationId>"
}
```

> Subscriptions are valid as long as the member's authorisation grant is valid. If the grant expires or is revoked, subscriptions are removed.

### Webhook Re-validation

LinkedIn re-validates endpoints every 2 hours. If re-validation fails 3 times in a row, the endpoint is blocked and events stop being delivered. Resolve any connectivity issues and manually trigger re-validation from the developer portal.

## Related Articles

- [LinkedIn Channel Overview](LinkedIn-Channel-Overview.md)
- [LinkedIn Account Onboarding](LinkedIn-Account-Onboarding.md)
- [Channel and Connector Setup](../../Solution_Admin/Channel-and-Connector-Setup.md)
