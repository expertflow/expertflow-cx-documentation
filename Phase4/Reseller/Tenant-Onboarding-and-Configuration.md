---
title: "Tenant Onboarding and Configuration"
summary: "Lifecycle guide for Resellers to provision, configure, and launch a new customer tenant on the ExpertFlow CX Cloud."
audience: [reseller, admin]
product-area: [platform, licensing]
doc-type: how-to
difficulty: intermediate
last-updated: 2026-03-08
---

# Tenant Onboarding and Configuration

As a Reseller (Cloud), you are responsible for the end-to-end setup of your customers' tenants. This guide provides the checklist and sequence required to transform a fresh instance into a live contact center.

## 1. Initial Access & Licensing
1.  **Credentials:** Log in to **Unified Admin** using the temporary administrator credentials provided by ExpertFlow.
2.  **Licensing:** Navigate to **General > License Info** and upload the customer's **Master API Key**.
3.  **Validation:** Verify the concurrent user count and expiry date match the customer's subscription tier.

## 2. Identity & Team Structure
Before adding channels, you must define *who* will handle the work.
1.  **User Management:** Use the **IAM (Keycloak)** portal to create Agent and Supervisor accounts.
2.  **Teams:** In Unified Admin, create **Teams** and assign a Primary Supervisor (Sam) to each.
3.  **Localization:** Set the **Timezone** and **Supported Languages** in General Settings to ensure the UI matches the customer's locale.

## 3. Routing Logic & Business Rules
Define how customer requests move through the system.
1.  **Media Routing Domains (MRD):** Enable the required domains (Voice, Chat, SMS).
2.  **Precision Queues:** Build queues with logical steps (e.g., "Language == Arabic").
3.  **Reason Codes:** Configure "Not Ready" and "Logout" reasons to enable accurate adherence reporting.

## 4. Channel Connectivity
Connect the customer's communication touchpoints.
- **Web Widget:** Create a widget instance and configure the pre-chat form.
- **WhatsApp:** Configure the Meta Cloud API connector or 3rd-party provider.
- **Voice:** Create extensions on the Media Server and assign them to voice-enabled agents.

## 5. Automation & Flow Design
1.  **Conversation Studio:** Assign the `conversation-studio-admin` role to the customer's Designer (Dave).
2.  **Bot Handover:** Ensure a default bot is registered to handle initial greetings and intent detection.
3.  **Surveys:** Configure post-interaction survey forms to collect customer sentiment.

---

*Need to white-label the interface or set up custom billing? Contact the [ExpertFlow Partner Support Team](https://support.expertflow.com).*
