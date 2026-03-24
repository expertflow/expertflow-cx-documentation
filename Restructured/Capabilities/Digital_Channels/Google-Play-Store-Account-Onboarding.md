---
title: "Google Play Store Account Onboarding"
summary: "Detailed steps for obtaining a Google Cloud Service Account and JSON key to enable Expertflow CX to manage app reviews."

product-area: [channels, google-play]
doc-type: how-to
difficulty: intermediate
last-updated: 2026-03-13
---

# Google Play Store Account Onboarding

This guide describes how to connect your Google Play Store app with the **Official Google Play Developer API** (Android Publisher API). Expertflow CX uses this API to pull reviews and post replies on your behalf.

## 1. Prerequisites
- Access to the **Google Cloud Console** with administrator permissions.
- Access to the **Google Play Console** for the target application.
- The **Package Name** (bundle ID) of your Android app (e.g., `com.example.myapp`).

## 2. Step 1: Google Cloud Project Setup
Your Google Play Console must be linked to a Google Cloud Project to manage API access.

1.  Log in to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Select or create a project for your integration.
3.  Ensure the **Android Publisher API** is enabled for this project.

## 3. Step 2: Create a Service Account
You must create a Service Account to authenticate Expertflow CX with Google APIs.

1.  Navigate to **IAM & Admin > Service Accounts**.
2.  Click **Create Service Account**.
3.  Enter a name (e.g., `play-store-integration`) and description.
4.  Assign the role: **Service Account User**.
5.  Click on the newly created Service Account email.
6.  Go to the **Keys** tab, click **Add Key > Create new key**, and select **JSON**.
7.  **Download and save the JSON file securely.** You will need these credentials for the configurational guide.

## 4. Step 3: Link to Google Play Console
You must grant the Service Account permission to manage reviews in the Play Store.

1.  Go to the [Google Play Console](https://play.google.com/apps/publish/).
2.  Navigate to **Users and Permissions**.
3.  Invite a new user using the **Service Account email address** created in Step 2.
4.  Grant the following permissions:
    - **View app information (read-only)**
    - **Reply to reviews** (required for agents to post responses)
5.  Click **Invite User**.

## 5. Next Steps
Once you have the **JSON key file** and have linked the service account in the Play Console, proceed to the [Google Play Store: Configuration Guide](./Google-Play-Store-Configuration-Guide.md) to set up the channel in Expertflow CX.
