---
title: "GDPR Compliance"
summary: "How ExpertFlow CX meets General Data Protection Regulation requirements for personal data protection."

product-area: [security]
doc-type: reference
difficulty: intermediate
keywords: ["GDPR", "data protection", "personal data", "privacy", "encryption", "RBAC", "PII", "audit logging", "compliance"]
aliases: ["General Data Protection Regulation", "data privacy compliance"]
last-updated: 2026-03-10
---

# GDPR Compliance

ExpertFlow CX is designed to support your obligations under the **General Data Protection Regulation (GDPR)** — the EU framework that governs how personal data is collected, processed, stored, and shared. This reference maps each key GDPR technical requirement to the corresponding ExpertFlow CX control.

## Compliance Matrix

| # | GDPR Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|---|
| 1 | **Data Encryption** — Protect personal data at rest and in transit using strong encryption. | ✅ Compliant | ExpertFlow CX encrypts all data in transit using TLS. Data at rest is encrypted for messages and call recordings. See [Data Encryption](../../How-to_Guides/Administrator/Encryption-at-Rest-Configuration-Guide.md). |
| 2 | **Access Controls** — Enforce role-based access to limit personal data exposure to authorized users only. | ✅ Compliant | Role-based access controls (RBAC) and group-based access controls (GBAC) are enforced across the platform. Only authenticated, authorized agents can access conversation data and customer profiles. |
| 3 | **Anonymization & Pseudonymization** — Implement data masking or tokenization to reduce personal data exposure. | ✅ Compliant | PII data masking is available in two scopes: (1) masking in system logs, and (2) masking of customer attributes in Agent Desk. See [PII Data Masking](../../Reference/Archive-Notice.md). |
| 4 | **Audit Logs** — Record all actions related to personal data access, modification, and deletion. Logs must be tamper-proof. | ⚠️ Partial | Event logging for IAM (Keycloak) is available. Centralized audit logging for all CX components is on the 2025 roadmap. |
| 5 | **Pause-and-Resume Recording** — Allow agents to pause call recordings when sensitive personal data is discussed. | ✅ Compliant | Agents can pause and resume call recordings from Agent Desk during live interactions. |

## Key Definitions

| Term | Meaning in this context |
|---|---|
| **RBAC** | Role-Based Access Control — permissions assigned by role (Agent, Supervisor, Admin) |
| **GBAC** | Group-Based Access Control — permissions scoped to a team or tenant group |
| **PII** | Personally Identifiable Information — data that can identify an individual |
| **ePHI** | Electronic Protected Health Information — relevant to HIPAA; not specific to GDPR |
| **TLS** | Transport Layer Security — protocol used to encrypt data in transit |

## Scope and Limitations

ExpertFlow CX provides the **technical controls** listed above. Your organization remains the **data controller** under GDPR and is responsible for:

- Defining and documenting your lawful basis for processing personal data
- Handling data subject access requests (DSARs)
- Conducting data protection impact assessments (DPIAs)
- Maintaining records of processing activities (Article 30)

Contact your ExpertFlow account team for a Data Processing Agreement (DPA) if required by your legal team.

## Related Articles

- [PII Data Masking](../../Reference/Archive-Notice.md)
- [HIPAA Compliance](HIPAA-Compliance.md)
- [PCI DSS Compliance](PCI-DSS-Compliance.md)
- [Security and Compliance Whitepaper](../../Platform_Overview/Security-and-Compliance-Whitepaper.md)
- [IAM Keycloak Configuration](../../How-to_Guides/Administrator/IAM-Keycloak-Configuration.md)
