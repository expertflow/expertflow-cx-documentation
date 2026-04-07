---
title: "PCI DSS Compliance"
summary: "How ExpertFlow CX addresses Payment Card Industry Data Security Standard requirements for protecting cardholder data in contact center environments."

product-area: [security]
doc-type: reference
difficulty: intermediate
keywords: ["PCI DSS", "cardholder data", "payment security", "encryption", "RBAC", "vulnerability scanning", "compliance", "contact center"]
aliases: ["Payment Card Industry Data Security Standard", "PCI compliance", "card data security"]
last-updated: 2026-03-10
---

# PCI DSS Compliance

The **Payment Card Industry Data Security Standard (PCI DSS)** defines technical and operational requirements to protect cardholder data and reduce fraud risk. This reference maps each PCI DSS requirement domain to ExpertFlow CX's compliance posture.

> **Important:** ExpertFlow CX processes communications, not payment transactions. Cardholder data may enter the platform only if a customer communicates it verbally or via message. Your organization is responsible for scoping which channels and queues are in-scope for PCI DSS.

## Compliance Matrix

### 1. Build and Maintain a Secure Network and Systems

| Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|
| Install and maintain a firewall to protect cardholder data. | ✅ Compliant | ExpertFlow CX can be deployed behind your network firewall. Kubernetes network policies can be applied to restrict inter-service traffic. |
| Do not use vendor-supplied default passwords or security parameters. | ✅ Compliant | All system passwords are configurable and enforced by a configurable password policy via Keycloak. |

### 2. Protect Cardholder Data

| Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|
| Protect stored cardholder data. | ⚠️ Partial | Message content is encrypted at rest. Call recordings are encrypted at rest. **Note:** Call transcripts do not automatically redact cardholder data spoken during a call. Use pause-and-resume recording to prevent recording of sensitive verbal disclosures. |
| Encrypt transmission of cardholder data across open, public networks. | ✅ Compliant | All data in transit is encrypted via TLS. |

### 3. Maintain a Vulnerability Management Program

| Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|
| Protect systems against malware and update antivirus software. | ➡️ Not Applicable | Customer and partner responsibility. ExpertFlow does not manage host-level antivirus on your infrastructure. |
| Develop and maintain secure systems and applications. | ✅ Compliant | Security checks are applied throughout the CI/CD pipeline. Each packaged release is scanned with a vulnerability scanner. Security maintenance releases are issued for newly discovered vulnerabilities. |

### 4. Implement Strong Access Control Measures

| Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|
| Restrict access to cardholder data by business need. | ✅ Compliant | RBAC and GBAC enforce least-privilege access. Agents access only the conversations and customer data relevant to their queue and team. |
| Identify and authenticate access to system components. | ✅ Compliant | All users authenticate through Keycloak. 2FA is available for an additional authentication layer. |
| Restrict physical access to cardholder data. | ➡️ Not Applicable | Partner and customer responsibility for the physical hosting environment. |

### 5. Regularly Monitor and Test Networks

| Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|
| Track and monitor all access to network resources and cardholder data. | ➡️ Not Applicable | Customer and partner responsibility for network-level monitoring. IAM event logging is available via Keycloak. |
| Regularly test security systems and processes. | ✅ Compliant | Packaged releases are periodically scanned. Security maintenance releases address newly identified vulnerabilities. |

### 6. Maintain an Information Security Policy

| Requirement | Status | ExpertFlow CX Implementation |
|---|---|---|
| Maintain an information security policy for all personnel. | ✅ Compliant | ExpertFlow maintains an Information Security Policy. See [expertflow.com/information-security-policy](https://www.expertflow.com/information-security-policy/). |

## Reducing PCI DSS Scope

To reduce the number of systems in-scope for your PCI DSS assessment:

1. **Use pause-and-resume recording** during interactions where customers verbally provide card data.
2. **Enable PII masking** to prevent cardholder data from appearing in agent UI fields and system logs.
3. **Segment your network** — place ExpertFlow CX components handling cardholder-data channels in a dedicated network segment.
4. **Use a DTMF payment collection integration** — route card number capture to a payment IVR so digits never pass through the agent desktop.

## Related Articles

- [GDPR Compliance](GDPR-Compliance.md)
- [HIPAA Compliance](HIPAA-Compliance.md)
- [VRS PCI DSS Compliance](VRS-PCI-DSS-Compliance.md)
- [Security and Compliance Whitepaper](../../Platform_Overview/Security-and-Compliance-Whitepaper.md)
