---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# 360-Connector Configuration Guide

This guide provides the necessary endpoints and parameters for setting up WhatsApp messaging via the 360dialog API.

## 1. Webhook Registration
The 360-connector requires a one-time registration of the webhook URL. Send an HTTP POST request to `{FQDN}/configs/webhook`.

| Query Param | Description |
| :--- | :--- |
| **url** | The notification endpoint: `{FQDN}/360notifications` |
| **hostUrl** | `https://waba.360dialog.io` (Production) |
| **apiKey** | Your 360dialog WhatsApp API Key. |
| **authorization** | Your WhatsApp number (e.g., `41762884806`). |

## 2. Unified Admin Configurations

### Channel Provider
- **Provider Webhook**: `http://ef-360-connector-svc:8080` (K3s).
- **Custom Attributes**:
  - `HOST-URL`: The base URL for the API.
  - `API-KEY`: The token provided by 360dialog.

### Channel Connector
- **HOST-URL**: `https://waba.360dialog.io` (Include trailing slash).
- **API-KEY**: Paste your 360dialog token.

## 3. Testing with Sandbox
To use the 360dialog sandbox:
1. Set `HOST-URL` to `https://waba-sandbox.360dialog.io`.
2. Add the sandbox number `4930609859535` to your phone.
3. Send `START` (all caps) to that number to receive your sandbox API key.
