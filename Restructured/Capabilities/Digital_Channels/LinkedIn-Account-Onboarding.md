---
title: "LinkedIn Account Onboarding"
summary: "How-to guide for setting up a LinkedIn Developer Portal account, creating a LinkedIn App, verifying your LinkedIn Page, and requesting Community Management API access required for the ExpertFlow CX LinkedIn connector."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["LinkedIn onboarding", "LinkedIn Developer Portal", "LinkedIn App creation", "LinkedIn Community Management API", "LinkedIn page verification", "Standard tier LinkedIn"]
aliases: ["LinkedIn setup", "LinkedIn developer account", "LinkedIn API access"]
last-updated: 2026-03-10
---

# LinkedIn Account Onboarding

This guide walks through setting up a LinkedIn App with Community Management API access — a prerequisite for the ExpertFlow CX LinkedIn connector. If you already have a LinkedIn App with Community Management API (developer or standard tier), you can skip this guide and proceed directly to the [LinkedIn Configuration Guide](LinkedIn-Configuration-Guide.md).

## Prerequisites

- Admin access to the LinkedIn Page you want to integrate.
- A LinkedIn account for the Page admin.

## Step 1: Create a LinkedIn Developer Portal Account

1. Open the [LinkedIn Developer Portal](https://www.linkedin.com/developers/) in your browser.
2. Log in using the LinkedIn credentials of the Page admin. If you don't have a developer account, create one using the same LinkedIn admin account.
3. Complete the required profile information to finish account setup.
4. Once completed, you will be directed to the Developer Portal dashboard.

## Step 2: Create a LinkedIn Application

1. In the Developer Portal, navigate to **My Apps → Create App**.
2. Fill in the required application details:
   - **App name**: e.g., `ExpertFlow CX LinkedIn Connector`
   - **LinkedIn Page association**: Link to your company LinkedIn page
   - **Privacy policy URL**: Your company's privacy policy (must be publicly accessible)
   - **Business logo**: Upload your company logo
3. Submit the form. Your application will be created with **Default Tier** access.

## Step 3: Verify Your LinkedIn Page

Page verification links your LinkedIn App to your company page, allowing the app to manage page content.

1. In the Developer Portal, navigate to your app's settings and find the page verification section.
2. Send a verification request to the administrator of the associated LinkedIn Page.
3. The page admin will receive a verification link via LinkedIn notifications.
4. The page admin clicks the link to complete verification.
5. Once verified, the Developer Portal reflects the page's verified status in your app settings.

## Step 4: Request Community Management API Access

The Community Management API provides access to LinkedIn social actions (comments, reactions) needed by the ExpertFlow connector.

1. In your app's Developer Portal, go to the **Products** tab.
2. Locate **Community Management** and click **Request Access**.
3. Complete the Community Access Form with details about your integration use case.
4. Submit the form. The status changes to **Review in Progress**.
5. Once LinkedIn approves, your app gains **Developer Tier** access.
6. Approved permissions will be visible in the **Auth** tab of your app.

## Step 5: Upgrade to Standard Tier (Optional — For Webhooks)

Standard tier access is required for real-time webhook notifications in the LinkedIn connector (available from CX version 4.10.3+). The upgrade requires a review by LinkedIn.

**Requirements for the standard tier upgrade:**

1. **Demo video**: Upload a video (e.g., on Google Drive) demonstrating your application's functionality.
   - Must include audio commentary in US English explaining how the application works.
2. **OAuth consent screen**: Configure an OAuth consent screen that shows which LinkedIn permissions the app requests from members.
3. **Use case demonstration**: Show in the video:
   - How member information (name, comment) is displayed to the page admin when a user interacts with a post.
   - How comments or reactions appear in your application.
4. **Post publishing demo**: Show how a post published from your app appears on the LinkedIn company page.

Submit the standard tier request through the Developer Portal and wait for LinkedIn's review response.

> **Note**: If you only need polling-based integration (no real-time webhooks), Developer Tier access is sufficient. See [LinkedIn Configuration Guide](LinkedIn-Configuration-Guide.md) for webhook vs. scheduler trade-offs.

## Next Step

Once your LinkedIn App has Community Management API access, proceed to [LinkedIn Configuration Guide](LinkedIn-Configuration-Guide.md) to connect it to ExpertFlow CX via Unified Admin.

## Related Articles

- [LinkedIn Channel Overview](LinkedIn-Channel-Overview.md)
- [LinkedIn Configuration Guide](LinkedIn-Configuration-Guide.md)
- [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
