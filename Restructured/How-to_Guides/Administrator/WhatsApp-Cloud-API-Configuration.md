---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# WhatsApp Cloud API Configuration & Deployment

WhatsApp is a supported customer channel in Expertflow CX, allowing seamless interaction between bots, agents, and customers.

## Getting Started

### 1. Meta Developer Setup
- Register as a [Meta Developer](https://developers.facebook.com/docs/development/register).
- Create a **Business App** in the Meta App Dashboard.
- Add the **WhatsApp** product to your app.

### 2. Recipient and Test Messaging
- Under **WhatsApp > API Setup**, add a valid WhatsApp number to the "To" field for testing.
- Send the `hello_world` template message to verify the connection.

### 3. Webhook Configuration
- In the Meta App Dashboard, go to **Webhooks**.
- Select **WhatsApp Business Account** and click **Subscribe**.
- **Callback URL**: `https://{{SERVER-FQDN}}/whatsapp-connector/webhook/{{Phone-Number-ID}}`
- **Verify Token**: Must match the `WHATSAPP-PAGE-ACCESS-TOKEN` in your Unified Admin configuration.
- Subscribe to the **messages** field.

### 4. Page Access Token
- Generate a **Short-Lived Token** via the Graph API Explorer.
- Extend it to a **Long-Lived Token** (no expiry) using the [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken).

## Unified Admin Configuration

### Channel Provider
1. Create a provider named "WhatsApp Provider".
2. **Provider Webhook**: `http://{SERVICE-NAME}:{SERVICE-PORT}`.
3. Add Custom Attributes:
   - `WHATSAPP-HOST-URL` (URL)
   - `WHATSAPP-API-KEY` (String 2000)
   - `WHATSAPP-PAGE-ACCESS-TOKEN` (String 100)

### Channel Connector
1. **WHATSAPP-HOST-URL**: `https://graph.facebook.com/v19.0/` (Include trailing slash).
2. **WHATSAPP-API-KEY**: Your Long-Lived Page Access Token.
3. **WHATSAPP-PAGE-ACCESS-TOKEN**: Your Webhook Verify Token.

### Channel Setup
1. **Service Identifier**: Your WhatsApp Phone Number ID.
2. **Channel Mode**: `HYBRID`.
3. **Routing Mode**: `PUSH` or `PULL` as required.
4. **Queue**: Select the target chat queue.

For more details on Meta features, visit the [WhatsApp Cloud API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api).
