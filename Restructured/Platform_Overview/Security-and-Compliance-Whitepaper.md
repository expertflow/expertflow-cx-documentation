---
title: "Security & Compliance Whitepaper"
summary: "High-level overview of ExpertFlow CX security architecture, data privacy measures, and global compliance adherence."
audience: [platform-overview]
product-area: [security]
doc-type: explanation
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Security & Compliance Whitepaper

ExpertFlow CX is designed with a "Security-First" architecture to protect sensitive personal, financial, and healthcare data. This document outlines our adherence to global standards and the technical measures we take to ensure data sovereignty.

## 1. Compliance Frameworks
We maintain active alignment with the following regulatory frameworks:

- **GDPR:** We ensure data privacy through right-to-erasure workflows and localized data residency options.
- **HIPAA:** Specialized controls for healthcare data, including audit trails and PHI protection.
- **PCI DSS:** Secure handling of payment information via tokenization and non-storage policies.

## 2. Technical Security Pillars

### Data Encryption
ExpertFlow employs industry-standard encryption protocols:
- **In-Transit:** All communication via HTTPS/TLS 1.3.
- **At-Rest:** Encryption of databases and file storage using AES-256.

### Identity & Access Management (IAM)
- **Unified Authentication:** Centralized management via Keycloak.
- **Role-Based Access Control (RBAC):** Granular permissions for the 12 platform personas.
- **Multi-Factor Authentication (MFA):** Native support for 2FA via Email, SMS, and Authenticator apps.

## 3. Data Privacy Measures
To mitigate the risk of data leakage, ExpertFlow provides:
- **PII Masking:** Automatic masking of sensitive fields (e.g., Credit Card numbers) in logs and the Agent Desk.
- **Selective Recording:** Rules-based logic to pause voice/screen recording during sensitive interaction segments.

## 4. Operational Transparency
- **Audit Trails:** Centralized logging of all administrative actions and data access.
- **Vulnerability Management:** Continuous scanning and remediation of our core components and dependencies.

---

## 5. Network Security

ExpertFlow CX is deployed on Kubernetes (RKE2) and enforces network-level isolation by default:

- **Namespace isolation:** Each tenant's workloads run in a dedicated namespace with Kubernetes NetworkPolicies restricting east-west traffic.
- **Ingress control:** All external traffic routes through a single ingress controller (NGINX). Direct access to internal services is blocked at the cluster level.
- **Firewall rules:** Only ports 80, 443, and deployment-specific management ports are exposed. All other ports are closed by default.
- **Internal service communication:** Service-to-service calls within the cluster use internal DNS and never traverse the public internet.

---

## 6. OWASP Top 10 Posture

ExpertFlow CX is evaluated against the OWASP Top 10 as part of each major release cycle. The table below reflects the current posture:

| OWASP Risk | Mitigation |
| --- | --- |
| A01 Broken Access Control | RBAC enforced via Keycloak; all API endpoints require a valid JWT |
| A02 Cryptographic Failures | TLS 1.3 in transit; AES-256 at rest; no sensitive data in logs |
| A03 Injection | Parameterised queries throughout; input validation at API boundaries |
| A04 Insecure Design | Threat modelling performed during architecture review for each feature |
| A05 Security Misconfiguration | Hardened Helm charts; default credentials disabled; secrets managed via Kubernetes Secrets |
| A06 Vulnerable Components | Automated dependency scanning (Trivy) on every build; CVEs tracked and remediated per SLA |
| A07 Auth & Session Failures | Session tokens are short-lived JWTs; MFA available for all admin roles |
| A08 Software & Data Integrity | Container images are signed and verified at deploy time |
| A09 Logging & Monitoring Failures | Centralised audit log; alerting on anomalous admin actions |
| A10 SSRF | Outbound HTTP from connectors is allowlisted; arbitrary URL calls are blocked |

> **Note:** Items marked as in-progress in previous assessments have been remediated. Contact your ExpertFlow account team for the latest third-party penetration test report.

---

## 7. Deployment Model & Trust Boundaries

ExpertFlow CX supports two deployment models, each with distinct trust boundaries:

### On-Premises / Private Cloud

- Customer controls the infrastructure, network perimeter, and data residency.
- ExpertFlow has no access to customer data unless explicitly granted for support purposes.
- All credentials and secrets remain within the customer's Kubernetes cluster.

### ExpertFlow-Hosted (SaaS)

- Infrastructure is managed by ExpertFlow in a dedicated tenant environment.
- Customer data is logically isolated at the database and storage layer.
- Access to production infrastructure is restricted to a named list of ExpertFlow SREs and requires MFA + VPN.

---

## 8. Vulnerability Disclosure & Patch SLA

ExpertFlow operates a responsible disclosure programme:

| Severity | Response SLA | Patch SLA |
| --- | --- | --- |
| Critical (CVSS ≥ 9.0) | 24 hours | 7 days |
| High (CVSS 7.0–8.9) | 48 hours | 30 days |
| Medium (CVSS 4.0–6.9) | 5 business days | 90 days |
| Low (CVSS < 4.0) | Next release cycle | Next release cycle |

To report a vulnerability, contact **[security@expertflow.com](mailto:security@expertflow.com)**. Reports are acknowledged within one business day.

---

## 9. Incident Response

In the event of a confirmed security incident:

1. **Detection & triage** — automated alerts via the monitoring stack trigger an on-call page within minutes.
2. **Containment** — affected workloads are isolated at the network layer without waiting for root-cause analysis.
3. **Customer notification** — affected customers are notified within 72 hours of a confirmed breach, in line with GDPR Article 33.
4. **Post-incident review** — a root-cause analysis and remediation plan are shared with affected customers within 14 days.

---

## Related Articles

- [GDPR Compliance](../Capabilities/Security_and_Compliance/GDPR-Compliance.md)
- [HIPAA Compliance](../Capabilities/Security_and_Compliance/HIPAA-Compliance.md)
- [PCI DSS Compliance](../Capabilities/Security_and_Compliance/PCI-DSS-Compliance.md)
- [Voice Recording and Compliance Features](Voice-Recording-and-Compliance-Features.md)
