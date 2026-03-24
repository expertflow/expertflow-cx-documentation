---
title: "Google Play Store Configuration Guide"
summary: "Technical steps for administrators to configure the Google Play Store channel in Unified Admin."

product-area: [channels, google-play]
doc-type: how-to
difficulty: advanced
last-updated: 2026-03-13
---

# Google Play Store Configuration Guide

This guide describes how to configure the Google Play Store channel within the Expertflow CX **Unified Admin** console.

## 1. Prerequisites
- Completion of the **[Google Play Store: Account Onboarding](./Google-Play-Store-Account-Onboarding.md)**.
- **JSON Key File** content from your Google Service Account.
- Your app's **Package Name** (e.g., `com.example.myapp`).
- EFCX administrative access.

## 2. Channel Configuration Steps

### A. Setup Channel Type
1. Log in to **Unified Admin**.
2. Navigate to **Channel Manager > Channel Types**.
3. Verify that `PLAY_STORE` exists. If not, click **Add New** and select `CHAT` as the MRD.
4. Save the configuration.

### B. Setup Channel Provider
1. Navigate to **Channel Manager > Channel Providers**.
2. Click **Add New** and enter a name (e.g., `Google Play Store Provider`).
3. Select `PLAY_STORE` as the Channel Type.
4. Enter the **Provider Webhook**: `http://cx-channels-google-playstore-connector-svc:8080` (verify port in your deployment).
5. Add the required **Custom Attributes** for the Google Service Account (e.g., `GOOGLE_SA_PROJECT_ID`, `GOOGLE_SA_PRIVATE_KEY`, etc.).
6. Save the provider.

### C. Setup Channel Connector
1. Navigate to **Channel Manager > Channel Connectors**.
2. Click **Add New** and select the provider created above.
3. Fill in the values for all custom attributes using the content of your **JSON key file**.
   - Ensure the `GOOGLE_SA_PRIVATE_KEY` includes the full text (Begin/End tags).
   - Enter your `GOOGLE_PLAY_PACKAGE_NAME`.
4. Set permission flags:
   - `COMMENT_REPLY_SUPPORT_SM`: `true`
   - `ALLOW_VIEW_FULL_POST_SM`: `true`
5. Save the connector.

### D. Create the Channel
1. Navigate to **Channel Manager > Channels**.
2. Click **Add New Channel** under the `PLAY_STORE` section.
3. Set the **Service Identifier** to your app's package name.
4. Select the **Connector** and **Bot** (if applicable).
5. Set **Routing Mode** to `PULL` and **Channel Mode** to `HYBRID`.
6. Configure the **Queue** and **Agent Selection Policy**.
7. Save.

## 3. Post-Configuration
The connector uses an automatic discovery mechanism. Once the channel is saved, the connector will detect it during the next polling cycle and begin fetching reviews from the Play Store.

No additional webhook setup is required for this channel.
