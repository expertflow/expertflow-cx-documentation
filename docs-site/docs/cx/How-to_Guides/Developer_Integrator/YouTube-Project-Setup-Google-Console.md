---
audience: [developer-integrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# YouTube Project Setup in Google Developers Console

To integrate YouTube with Expertflow CX, you must first set up a project in the Google Developers Console.

## 1. Create a New Project
- Go to the [Google Developers Console](https://console.cloud.google.com/).
- Create a new project by selecting **"New Project"** in the project drop-down.

## 2. Enable the YouTube Data API v3
- In your project, navigate to: `APIs & Services > Library`.
- Search for **YouTube Data API v3** and enable it.

## 3. Obtaining API Credentials

### Step 1: Creating Credentials
- Navigate to: `APIs & Services > Credentials`.
- Click on **Create Credentials** and select **OAuth 2.0 Client ID**.

### Step 2: Configuring the OAuth Consent Screen
- Click **Configure Consent Screen**.
- Select **User Type** (Internal for testing, External for production).
- Fill in the required fields (App Name, Support Email, etc.).
- In the **Scopes** section, add:
  - `https://www.googleapis.com/auth/youtube.readonly`
  - `https://www.googleapis.com/auth/youtube.force-ssl`
- For production, you must submit the app for verification with a video demo and screenshots.

### Step 3: Securing Your Credentials
- Go to the **Credentials** tab and click **Create Credentials** -> **Web Application**.
- Name it `expertflow`.
- Set the Redirect URI:
  - **Testing:** `https://oauth.pstmn.io/v1/callback`
  - **Production:** `https://yourdomain.com/oauth/callback`
- **IMPORTANT:** Store your **Client ID** and **Client Secret** securely.

## 4. Grant Developer Access in Google Cloud IAM
- Navigate to: `IAM & Admin > IAM`.
- Click **Grant Access** and add the developer's email.
- Assign a role such as `Editor` or `Cloud Functions Developer`.

## 5. Obtain Authorization Code
Use the following URL structure to initiate the OAuth flow:
`https://accounts.google.com/o/oauth2/auth?client_id=YOUR_CLIENT_ID&redirect_uri=https://yourdomain.com/oauth/callback&response_type=code&scope=https://www.googleapis.com/auth/youtube.force-ssl&access_type=offline&prompt=consent`

## 6. Exchange Authorization Code for Tokens
Send a POST request to `https://oauth2.googleapis.com/token` with the following body:
`code=AUTHORIZATION_CODE&client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&redirect_uri=YOUR_REDIRECT_URI&grant_type=authorization_code`

## 7. Use Tokens to Access YouTube API
- Use the `access_token` for API calls.
- Store the `refresh_token` securely for long-term access.

## 8. Request Quota Increase
If you exceed 10,000 units/day, request an increase via `IAM & Admin > Quotas` for the **YouTube Data API v3**.
