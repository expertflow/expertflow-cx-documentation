---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Viber Connector Configuration & Deployment

The Viber Connector allows businesses to interact with customers via a Viber Bot (Admin account).

## 1. Viber Setup
1. Download the Viber Mobile App and sign up.
2. Visit the [Viber Admin Portal](https://partners.viber.com) and log in.
3. **Create Bot Account**: Fill in the details. The **URI** must be unique across all of Viber.
4. **Token**: Copy the unique token assigned upon creation.
5. **Publish**: In the mobile app, scan your bot's QR code and select the "Publish" icon.

## 2. Unified Admin Configuration

### Channel Provider
- **Provider Webhook**: `http://ef-viber-connector-svc:8080` (K3s).
- **Custom Attributes**:
  - `VIBER-TOKEN` (String 2000)
  - `VIBER-ACCOUNT-NAME` (String 2000)

### Channel Connector
- **VIBER-TOKEN**: Paste the token from the Viber Admin Portal.
- **VIBER-ACCOUNT-NAME**: The name assigned to your bot.

### Channel
- **Service Identifier**: The **Account URI** from the Viber Admin Portal (case-sensitive).
- **Mode**: `HYBRID`.
- **Routing**: `PUSH` or `PULL`.

## 3. Webhook Registration
After configuring Unified Admin, you must register the webhook with Viber using a POST request to `https://chatapi.viber.com/pa/set_webhook`.

**Header**: `X-Viber-Auth-Token: {Your-Token}`

**Body**:
```json
{
  "url": "https://{FQDN}/viber-connector/webhook/{Account-URI}",
  "event_types": ["delivered", "seen", "failed", "subscribed", "unsubscribed", "conversation_started"]
}
```
A response status of `0` indicates success.

For more details, refer to the [official Viber REST API documentation](https://developers.viber.com/docs/api/rest-bot-api/).
