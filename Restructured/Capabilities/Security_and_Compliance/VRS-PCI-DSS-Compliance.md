---
title: "VRS PCI DSS Compliance"
summary: "PCI DSS compliance posture for the ExpertFlow Voice Recording System (VRS), covering password management, transmission security, access controls, and vulnerability management."

product-area: [security]
doc-type: reference
difficulty: advanced
keywords: ["VRS", "voice recording", "PCI DSS", "password management", "TLS", "RBAC", "Keycloak", "compliance", "Cisco Finesse"]
aliases: ["Voice Recording System compliance", "VRS security", "recording PCI compliance"]
last-updated: 2026-03-10
---

# VRS PCI DSS Compliance

This reference covers the PCI DSS compliance posture of the **ExpertFlow Voice Recording System (VRS)** — the component responsible for recording, storing, and replaying agent-customer voice interactions.

For the broader platform compliance posture, see [PCI DSS Compliance](PCI-DSS-Compliance.md).

## Compliance Matrix

### Password Management

| Requirement | Status | VRS Implementation |
|---|---|---|
| Force users to change admin-assigned passwords on first login. | ✅ Compliant | Enforced via Keycloak password policies. |
| Enforce password complexity (length 4–16 characters, mixed case, numbers, symbols; first character must be uppercase). | ✅ Compliant | Keycloak password policy rules are configurable and applied at authentication. |
| Prevent reuse of the last 4 passwords. | ✅ Compliant | Keycloak password history policy prevents reuse. |
| Lock accounts after 4 failed login attempts; lockout duration configurable up to 30–60 minutes. | ⚠️ Partial | Keycloak brute-force protection is configurable for standard user accounts. **Note:** When VRS is integrated with Cisco Finesse, agent credentials are synchronized with Finesse, and Keycloak password policies do not apply to the Finesse-side authentication. |

### Transmission Security

| Requirement | Status | VRS Implementation |
|---|---|---|
| Use strong cryptography (SSL/TLS, SSH, or IPSec) to protect data in transit over public networks. | ✅ Compliant | All web-based access to VRS is secured via SSL/TLS. |
| Encrypt all non-console administrative access (browser/web-based management tools). | ✅ Compliant | Administrative access is served over HTTPS. |

### Access Control

| Requirement | Status | VRS Implementation |
|---|---|---|
| Limit system access to users whose role requires it; default-deny for all others. | ✅ Compliant | Role-based security is applied to VRS users. Access is scoped by role assignment. |
| Protect stored recordings from unauthorized access. | ⚠️ Partial | Recordings stored on disk require the system administrator to configure OS-level access controls on the storage volume. VRS does not enforce host-level filesystem permissions independently. |
| Implement two-factor authentication for remote access. | ⚠️ Not Tested | 2FA for the Cisco integration path has not been validated. Standard VRS login supports 2FA via Keycloak. |
| Render passwords unreadable during storage and transmission using strong cryptography. | ✅ Compliant | SSL/TLS is used for transport. Keycloak handles credential storage securely. |
| Ensure proper user identification and authentication management. | ✅ Compliant | User identity is managed through Keycloak. |

### Vulnerability Management

| Requirement | Status | VRS Implementation |
|---|---|---|
| Establish a process to identify and rank security vulnerabilities. | ⚠️ Partial | VRS components are not currently included in the automated vulnerability scanning process that covers other CX components. Manual review applies. |
| Develop software applications securely in accordance with PCI DSS. | ⚠️ Partial | Secure development practices are applied but formal PCI DSS-aligned secure development documentation for VRS is not published. |

## Known Gaps and Mitigations

| Gap | Risk Level | Recommended Mitigation |
|---|---|---|
| Cisco Finesse integration bypasses Keycloak password policies | Medium | Enforce password policies directly in Cisco CUCM/Finesse administration console. |
| OS-level storage access controls are admin-managed | Medium | Apply filesystem permissions to the recording storage volume. Restrict access to the VRS service account only. |
| 2FA not tested on Cisco integration path | Low–Medium | Test and validate 2FA for remote administrative access to VRS on Cisco-integrated deployments. |
| VRS not in automated vulnerability scan scope | Medium | Include VRS containers/services in your periodic vulnerability scanning process. |

## Related Articles

- [PCI DSS Compliance](PCI-DSS-Compliance.md)
- [GDPR Compliance](GDPR-Compliance.md)
- [Security and Compliance Whitepaper](../../Platform_Overview/Security-and-Compliance-Whitepaper.md)
- [IAM Keycloak Configuration](../../How-to_Guides/Administrator/IAM-Keycloak-Configuration.md)
- [Cisco Voice Channel Configuration](../../How-to_Guides/Developer_Integrator/Cisco-Voice-Channel-Configuration.md)
