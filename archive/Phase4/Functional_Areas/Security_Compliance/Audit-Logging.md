---
title: "Audit Logging"
summary: "Reference explaining how ExpertFlow CX implements audit logging and distributed tracing using OpenTelemetry Protocol (OTLP) — covering core objectives, data integrity principles, compliance frameworks, and how to access logs."
audience: [solution-admin]
product-area: [channels, digital]
doc-type: reference
difficulty: advanced
keywords: ["audit logging CX", "OpenTelemetry CX", "OTLP audit logs", "OpenSearch logging", "CX observability", "audit trail contact center", "SOC 2 CX", "HIPAA audit logging", "GDPR logging", "CX tracing"]
aliases: ["CX audit logs", "observability CX", "tracing logging CX"]
last-updated: 2026-03-10
---

# Audit Logging

ExpertFlow CX uses **OpenTelemetry Protocol (OTLP)**-based logs and traces for real-time observability, secure auditability, and end-to-end traceability. The platform works with **OpenSearch** as its primary SIEM solution but is compatible with other vendor-agnostic enterprise SIEM products.

Audit logging enables operations teams to:
- Investigate agent, supervisor, and system activities (who did what, when, and from where).
- Troubleshoot customer interaction flows by correlating logs and traces across services.
- Meet compliance and governance requirements by ensuring all critical actions are traceable.

---

## Core Objectives

| Objective | Description |
|---|---|
| **Observability** | Real-time insight into application health and operational behaviour. |
| **Debugging** | Fast identification of failures and anomalies across services. |
| **Performance Monitoring** | Analysis of latency, throughput, and service bottlenecks. |
| **Auditability** | Capture and retention of critical actions for security and compliance. |
| **Correlation** | Linking logs, traces, and metrics using trace and span identifiers. |

---

## Data Integrity Principles

All audit records adhere to the following principles to maintain evidentiary value:

| Principle | Description |
|---|---|
| **Immutability** | Records are append-only — once written they cannot be altered or deleted. |
| **Chronological Integrity** | Events are stored in order of occurrence. |
| **Context Awareness** | Each record contains sufficient metadata for interpretation. |
| **Trace Correlation** | Logs and audit records are linkable to execution traces via trace and span IDs. |

---

## Compliance Framework Coverage

| Framework | Core Requirement | Value for CX |
|---|---|---|
| **SOC 2** | Trust Service Criteria | Ensures traceability of admin actions, availability of logs during failures, and confidentiality of log storage. |
| **ISO 27001** | Control A.12.4 | Enables event traceability across all resources; provides evidence for incident analysis. |
| **HIPAA** | §164.312(b) | Mandates recording access to ePHI; essential for detecting unauthorized disclosures and breach notification. |
| **GDPR** | Articles 30 & 33 | Demonstrates accountability in data processing; facilitates the 72-hour breach reporting window. |
| **PCI DSS** | Requirement 10 | Mandates tracking all access to cardholder data (CHD) to detect policy violations. |

---

## Universal Security Benefits

- **Incident Response**: Provides the telemetry needed to reconstruct the timeline of a security event.
- **Non-Repudiation**: Ensures users cannot deny having performed a specific action within the system.
- **Anomaly Detection**: Establishes a baseline of normal behaviour to highlight unauthorized administrative changes.

---

## Accessing Logs

Operations teams can access logs from two sources:

1. **Kubernetes Pod Logs**: Direct log access from running pods. See [Accessing Kubernetes Logs](../../Solution_Admin/Accessing-Kubernetes-Logs.md).
2. **OpenSearch Dashboard**: Centralized log search and visualization after deploying Fluentbit as a log shipper.

---

## Related Articles

- [Accessing Kubernetes Logs](../../Solution_Admin/Accessing-Kubernetes-Logs.md)
- [GDPR Compliance](GDPR-Compliance.md)
- [HIPAA Compliance](HIPAA-Compliance.md)
- [Platform Security Overview](../../Getting_Started/Security-and-Compliance-Whitepaper.md)

