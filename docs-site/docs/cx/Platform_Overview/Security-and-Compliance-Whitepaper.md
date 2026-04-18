---
title: "Security & Compliance Overview"
summary: "Security architecture, data privacy controls, compliance frameworks, deployment trust boundaries, and operational SLAs for ExpertFlow CX — designed for IT decision makers and procurement."
audience: [platform-overview]
product-area: [security]
doc-type: explanation
difficulty: beginner
aliases: []
last-updated: 2026-03-30
---

ExpertFlow CX is built on a security-first architecture designed to protect sensitive personal, financial, and healthcare data across contact center environments. This page covers the key security controls, compliance commitments, and operational practices relevant to IT leadership and procurement teams evaluating the platform.

> **At a glance**
>
> - Compliance: GDPR, HIPAA, PCI DSS
> - Encryption: TLS 1.3 in transit, AES-256 at rest
> - Authentication: Keycloak-based SSO with MFA for all admin roles
> - Deployment: On-premises, private cloud, or ExpertFlow-hosted (SaaS)
> - Vulnerability disclosure: Critical CVEs patched within 7 days
> - Breach notification: Within 72 hours per GDPR Article 33

---

## 1. Deployment Models & Trust Boundaries

Understanding the deployment model is foundational to the security evaluation, as it determines who controls the infrastructure and where data resides.

### On-Premises / Private Cloud

- The customer controls the infrastructure, network perimeter, and data residency.
- ExpertFlow has no access to customer data unless explicitly granted for a support session.
- All credentials and secrets remain within the customer's Kubernetes cluster.
- This model is preferred for organizations with strict data sovereignty requirements (e.g., healthcare, government, financial services).

### ExpertFlow-Hosted (SaaS)

- Infrastructure is managed by ExpertFlow in a dedicated tenant environment (no multi-tenant data mixing).
- Customer data is logically isolated at the database and storage layer.
- Access to production infrastructure is restricted to a named list of ExpertFlow SREs and requires MFA + VPN.

---

## 2. Compliance Frameworks

ExpertFlow CX maintains active alignment with the following regulatory frameworks:

- **GDPR:** Data privacy through right-to-erasure workflows, localized data residency options, and breach notification within 72 hours (Article 33).
- **HIPAA:** Specialized controls for healthcare data, including audit trails, PHI protection, and selective recording pause during sensitive interactions.
- **PCI DSS:** Secure handling of payment information via tokenization and non-storage policies, with PII masking in logs and the agent interface.

> **Third-party assurance:** ExpertFlow commissions independent penetration tests as part of each major release cycle. Contact your account team for the latest report. Customers with specific certification requirements (ISO 27001, SOC 2) should discuss roadmap alignment with the account team.

---

## 3. Technical Security Pillars

### Data Encryption

- **In transit:** All communication via HTTPS/TLS 1.3.
- **At rest:** Databases and file storage encrypted using AES-256.
- Sensitive data (credentials, tokens) is never written to application logs.

### Identity & Access Management (IAM)

- **Unified authentication:** Centralized identity management via Keycloak (an open-source enterprise IAM platform), supporting SSO integration with your existing identity provider.
- **Role-Based Access Control (RBAC):** Granular permissions scoped to each platform role — from agents and supervisors through to system administrators.
- **Multi-Factor Authentication (MFA):** Native 2FA support via Email, SMS, and Authenticator apps; mandatory for all administrative roles.

### Data Privacy Controls

- **PII masking:** Automatic masking of sensitive fields (e.g., credit card numbers) in logs and the Agent Desk interface.
- **Selective recording:** Rules-based logic pauses voice and screen recording during sensitive interaction segments to prevent inadvertent capture of payment or health data.

---

## 4. Network Security

ExpertFlow CX runs on Kubernetes (RKE2) and enforces network-level isolation by default:

- **Namespace isolation:** Each tenant's workloads run in a dedicated Kubernetes namespace with NetworkPolicies restricting east-west traffic between services.
- **Ingress control:** All external traffic routes through a single ingress controller (NGINX). Direct access to internal services is blocked at the cluster level.
- **Firewall rules:** Only ports 80, 443, and deployment-specific management ports are exposed. All other ports are closed by default.
- **Internal service communication:** Service-to-service calls within the cluster use internal DNS and never traverse the public internet.

---

## 5. OWASP Top 10 Posture

ExpertFlow CX is evaluated against the OWASP Top 10 as part of each major release cycle.

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

---

## 6. Operational Transparency

- **Audit trails:** Centralised logging of all administrative actions and data access events, available for customer review.
- **Vulnerability management:** Continuous scanning (Trivy) and remediation of core components and dependencies, tracked against the SLAs below.

---

## 7. Vulnerability Disclosure & Patch SLA

ExpertFlow operates a responsible disclosure programme. To report a vulnerability, contact **[security@expertflow.com](mailto:security@expertflow.com)** — reports are acknowledged within one business day.

| Severity | Response SLA | Patch SLA |
| --- | --- | --- |
| Critical (CVSS ≥ 9.0) | 24 hours | 7 days |
| High (CVSS 7.0–8.9) | 48 hours | 30 days |
| Medium (CVSS 4.0–6.9) | 5 business days | 90 days |
| Low (CVSS < 4.0) | Next release cycle | Next release cycle |

---

## 8. Incident Response

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
