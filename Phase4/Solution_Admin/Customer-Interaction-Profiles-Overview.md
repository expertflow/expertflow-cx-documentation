---
audience: [solution-admin]
doc-type: explanation
difficulty: beginner
aliases: []
---

# Customer Interaction Profiles Overview

The **Customers** component in Expertflow CX maintains complete interaction profiles, ensuring a 360° view of every person engaging with your organization.

## What is a Customer Interaction Profile?
A Customer object unifies multiple channel identities into a single record:
- **Identities**: Phone numbers, emails, social handles, and web widget IDs.
- **Preferences**: Preferred channels, language, and contact time windows.
- **Interaction History**: Links all conversations and activities across all channels.
- **CRM Links**: Connects to external systems like Salesforce or Microsoft Dynamics.

## Key Benefits
- **Personalized Orchestration**: Tailor journeys based on profile data (e.g., VIP routing).
- **Agent Efficiency**: Agents see the "full story" immediately without asking for account numbers.
- **Consistent Treatment**: Recognize a customer on WhatsApp who previously called via phone.

## Key Features

### 1. Extensible Schema
Administrators can add custom attributes (key-value pairs) such as "Renewal Date," "VIP Score," or "Preferred Agent." These can be marked as PII for security compliance.

### 2. Customer Labels
Categorize customers for easy routing or reporting. Labels like "High Priority" or "At Risk" can be synced from CRM or assigned manually by agents.

### 3. Outbound Preferences
Stores DNC (Do Not Call) status and "Best Time to Contact" data, which is automatically respected by CX Outbound Campaigns.

## Identification Process
When a customer contacts the center:
1. The system performs a lookup by channel identifier (e.g., phone number).
2. It returns the existing profile or creates an anonymous record.
3. If an anonymous user later authenticates (e.g., in a web chat), the session can be merged with their existing profile.

## Security & Privacy
- **Encryption**: Data is encrypted at rest and in transit.
- **PII Redaction**: Future support for automated masking of sensitive attributes.
- **MFA**: Access to customer data requires Multi-Factor Authentication for supervisors and admins.
