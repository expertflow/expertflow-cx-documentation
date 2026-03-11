---
audience: [developer]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# YouTube Integration Configuration (Developer Access)

This guide provides technical steps for developers to set up the Google Cloud Project and OAuth credentials required for the Expertflow YouTube Connector.

## 1. Google Console Project Setup
1. Create a new project in the [Google Developers Console](https://console.cloud.google.com).
2. Enable the **YouTube Data API v3**.
3. Create **OAuth 2.0 Credentials** (Client ID and Secret).
4. Configure the **OAuth Consent Screen**:
   - Set User Type to **Internal** (testing) or **External** (production).
   - Add scopes: `youtube.readonly` and `youtube.force-ssl`.

## 2. Obtain Authorization Code
Hit the following URL in a browser to authenticate:
`https://accounts.google.com/o/oauth2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=https://oauth.pstmn.io/v1/callback&response_type=code&scope=https://www.googleapis.com/auth/youtube.force-ssl&access_type=offline&prompt=consent`

## 3. Exchange Code for Tokens
Use Postman to POST to `https://oauth2.googleapis.com/token` with:
- `grant_type`: `authorization_code`
- `code`: `{The-code-from-step-2}`
- `client_id` & `client_secret`

**Important**: Securely store the `refresh_token` returned in the response.

## 4. Unified Admin Config
### Channel Connector
- **REFRESH_TOKEN**: Paste the token from Step 3.
- **CLIENT_ID**: Your Google Client ID.
- **CLIENT_SECRET**: Your Google Client Secret.

### Webhook Setup
After saving, register the webhook via a POST request to:
`https://<FQDN>/youtube-connector/channel-type-configurations`
Body: `{"channelTypeId": "your-youtube-type-id"}`
