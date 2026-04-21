---
title: "PII Data Masking"
summary: "How ExpertFlow CX masks Personally Identifiable Information in application logs and Agent Desk."
product-area: [security]
doc-type: reference
difficulty: intermediate
keywords: ["PII", "data masking", "privacy", "logs", "Agent Desk", "customer schema", "GDPR", "personal data"]
aliases: ["PII masking", "data privacy", "personal data masking"]
last-updated: 2026-04-21
---

# PII Data Masking

ExpertFlow CX uses advanced data masking techniques to ensure that your customers' personal and confidential details remain secure during every interaction. Data masking conceals Personally Identifiable Information (PII) while still enabling agents to assist customers effectively.

## What is PII?

PII refers to any data that can identify an individual, including:

- Full names
- Email addresses
- Telephone numbers

## Masking Scopes

ExpertFlow CX applies PII masking in two distinct scopes:

### 1. PII Data Masking in Logs

To safeguard PII including email addresses, telephone numbers, and full names during the debugging process, ExpertFlow CX masks sensitive data in all application logs. This ensures that even technical staff accessing logs cannot inadvertently expose customer data.


### 2. PII Data Masking of Customer Attributes in Agent Desk

Supervisors can enable PII masking on any customer schema attribute in Agent Desk. Once enabled:

- All agents see the attribute value in masked form by default.
- Only authorized agents can view the unmasked data.
- This reduces the risk of unauthorized exposure of sensitive customer information.


## Related Articles

- [GDPR Compliance](GDPR-Compliance.md)
- [HIPAA Compliance](HIPAA-Compliance.md)
- [PCI DSS Compliance](PCI-DSS-Compliance.md)
- [Audit Logging](Audit-Logging.md)
- [Customer Interaction Profiles Overview](../../How-to_Guides/Administrator/Customer-Interaction-Profiles-Overview.md)
