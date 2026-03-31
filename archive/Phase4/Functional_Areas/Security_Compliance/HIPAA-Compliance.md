---
title: "HIPAA Compliance"
summary: "How ExpertFlow CX meets HIPAA Technical Safeguard requirements for protecting electronic protected health information (ePHI)."
audience: [decision-maker, admin]
product-area: [security]
doc-type: reference
difficulty: intermediate
keywords: ["HIPAA", "ePHI", "health information", "access control", "audit controls", "transmission security", "authentication", "compliance"]
aliases: ["Health Insurance Portability and Accountability Act", "healthcare compliance", "ePHI protection"]
last-updated: 2026-03-10
---

# HIPAA Compliance

The **Health Insurance Portability and Accountability Act (HIPAA)** establishes standards to protect sensitive patient health information (ePHI) from unauthorized disclosure. This reference maps the HIPAA Technical Safeguards to ExpertFlow CX's implementation.

> **Note:** This article covers Technical Safeguards only. Physical and Administrative Safeguards are the responsibility of your organization as the covered entity.

## HIPAA Technical Safeguards — Compliance Matrix

| Safeguard | Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|---|
| **Access Control** | Implement technical policies to allow only authorized persons to access ePHI in electronic information systems. | ✅ Compliant | Role-based access controls (RBAC) and group-based access controls (GBAC) ensure only authorized agents access conversation and customer data. PII masking further limits data exposure within the UI. See [PII Data Masking](../../Archive-Notice.md). |
| **Authentication** | Implement procedures to verify the identity of any person seeking access to ePHI. | ✅ Compliant | All users authenticate via Keycloak (IAM). Two-Factor Authentication (2FA) is available as an additional verification layer. See [2FA Email Configuration Guide](../../Solution_Admin/2FA-Email-Configuration-Guide.md). |
| **Transmission Security** | Implement technical security measures to guard against unauthorized access to ePHI transmitted over electronic networks. | ✅ Compliant | ExpertFlow CX uses TLS for all data in transit. API communications and channel connectors enforce encrypted transport. |
| **Audit Controls** | Implement hardware, software, or procedural mechanisms to record and examine activity in systems that contain or use ePHI. | ⚠️ Partial | IAM event logging is available via Keycloak. Centralized audit logging for all CX components (conversation access, data queries) is on the platform roadmap. OpenSearch integration is available for partners who require audit trails now. |

## Scope and Organizational Responsibility

ExpertFlow CX operates as a **Business Associate** when processing ePHI on behalf of a covered entity. Your organization must:

- Execute a **Business Associate Agreement (BAA)** with ExpertFlow before processing ePHI through the platform
- Define which agents and queues handle ePHI interactions
- Configure pause-and-resume recording for interactions where ePHI is verbally disclosed
- Implement workforce training as required under HIPAA Administrative Safeguards

Contact your ExpertFlow account team to obtain a BAA.

## Related Articles

- [GDPR Compliance](GDPR-Compliance.md)
- [PCI DSS Compliance](PCI-DSS-Compliance.md)
- [2FA Email Configuration Guide](../../Solution_Admin/2FA-Email-Configuration-Guide.md)
- [IAM Keycloak Configuration](../../Solution_Admin/IAM-Keycloak-Configuration.md)
- [Security and Compliance Whitepaper](../../Getting_Started/Security-and-Compliance-Whitepaper.md)
