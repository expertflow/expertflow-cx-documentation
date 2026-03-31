---
title: "LinkedIn Standard Tier Upgrade Guide"
summary: "How-to guide for upgrading a LinkedIn application from Development Tier to Standard Tier — covering the 8-step Community Management API upgrade request form, required field values, compliance answers, and demo submission."
audience: [integrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["LinkedIn standard tier CX", "LinkedIn community management API CX", "LinkedIn developer portal upgrade CX", "LinkedIn connector tier upgrade", "LinkedIn API access CX"]
aliases: ["LinkedIn tier upgrade CX", "LinkedIn standard access CX", "community management API upgrade CX"]
last-updated: 2026-03-10
---

# LinkedIn Standard Tier Upgrade Guide

This guide walks through upgrading a LinkedIn application from **Development Tier** to **Standard Tier** to enable full access to the Community Management API. This is required to use the ExpertFlow CX LinkedIn Connector in production.

## Prerequisites

- Existing LinkedIn Developer application with Development Tier access.
- Verified LinkedIn Page associated with the application.
- Access to the [LinkedIn Developer Portal](https://www.linkedin.com/developers).

---

## Access the Upgrade Form

1. Log in to the [LinkedIn Developer Portal](https://www.linkedin.com/developers).
2. Navigate to your application and open the **Products** tab.
3. Click **Upgrade options** under **Community Management API**.
4. Begin completing the Upgrade Request Form.

---

## Step 1: Company Information

- Enter your company's legal name (include alternative or registered names if applicable).
- Provide your official company website URL.

---

## Step 2: Registered Address

Fill in all address fields:

- Street Address
- City
- State/Province
- Zip/Postal Code
- Country

---

## Step 3: Existing Tier Access

- Select **Yes** if your company already has Standard Tier access for any other LinkedIn applications. Otherwise select **No**.

---

## Step 4: Primary Use Case

- **Platform**: Select *"To integrate LinkedIn into an externalized self-service SaaS platform"*.
- Write a company description in the text field.
- Under **Use Cases Enabled**, select:
  - **Page Management** — Create and manage company posts, comments, reactions, and monitor engagement.
  - **Page Analytics** — Track post analytics and performance.

**Use case description** (copy and paste):

> **Post Creation & Engagement**: An admin posts content on LinkedIn, prompting user interactions.
>
> **Real-Time Detection**: The LinkedIn Connector detects new comments and triggers a chat session with an agent via ExpertFlow EFCX.
>
> **Agent Response**: The agent replies within EFCX. Responses can be: Reply To a Comment, React to a Comment, or Delete a Comment. The response is posted back to LinkedIn through the API.
>
> **Traceability & Reporting**: The conversation is logged with a reason code for analytics and performance tracking.
>
> **Authentication & Deployment**: The connector is deployed on Kubernetes. OAuth 2.0 tokens are generated via the LinkedIn Developer Portal and stored in Connector ConfigMaps.
>
> **Data Management**: The connector tracks Post ID and comment count to detect new interactions. It captures Post ID, Comment ID, and Comment Text, passes them to EFCX for processing, and posts the response back to LinkedIn.

---

## Step 5: Customer Information

Answer the following questions:

- Where are most of your customers based?
- How many clients use the product being integrated with the Community Management API?
- What category best describes your primary customers?
- If your product supports managing individual profiles → select **Others** and enter **N/A**.
- What industries are most common among your customers?

---

## Step 6: Privacy and Compliance

- Paste the ExpertFlow privacy policy URL: `https://www.expertflow.com/privacy-policy/`

Answer the compliance questions as follows:

| Question | Answer |
|---|---|
| Does your organization have a person/team responsible for compliance with privacy regulations? | **Yes** |
| Does your organization have the capability to securely delete all data from Community Management APIs if required by LinkedIn? | **Yes** |
| Is personal data obtained via Community Management APIs used for advertising or sales? | **No** |
| Is personal data shared with other customers for the purpose of managing a specific customer's page? | **No** |
| Do you have partnerships with any other platforms? | Select **Facebook, Twitter and other** |

---

## Step 7: Provide Demonstration Details

- Upload a video demonstrating your application's functionality using the ExpertFlow LinkedIn Connector demo video.
- Provide test login credentials for the reviewer:
  - URL: `https://<your-fqdn>/unified-agent/#/login`
  - Username: `linkedinuser`
  - Password: *(provide your test environment credentials)*

---

## Step 8: Final Review and Submission

1. Review all form fields for accuracy.
2. Click **Submit** to initiate the LinkedIn review process.

**After submission:**

- LinkedIn sends a confirmation email from `developer-access@linkedin.com` requesting a walkthrough video with English commentary.
- Respond with the same details provided in the form.
- Monitor follow-up emails — LinkedIn may ask for clarification on specific use case handling.

---

## Related Articles

- [LinkedIn Connector Deployment using Helm](../Partner/LinkedIn-Connector-Deployment.md)
- [CRM Connectors](CRM-Connectors.md)
