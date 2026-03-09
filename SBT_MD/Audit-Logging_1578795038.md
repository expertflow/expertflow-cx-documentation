# CX Knowledgebase : Audit Logging

This document provides Operations Managers with the technical framework required to maintain the health, stability, and security of the contact center solution. It serves as a guide to:

  * Provide clear visibility into how audit logging and tracing are implemented across the CX stack.

  * Enable rapid investigation of agent, supervisor, and system activities (who did what, when, and from where)

  * Support troubleshooting of customer interactions and call flows by correlating logs and traces across services

  * Facilitate compliance, security, and governance checks by ensuring that all critical actions are traceable and verifiable on demand.




CX platform uses **OpenTelemetry Protocol (OTLP)** based logs and traces for real-time observability, secure auditability, and end-to-end traceability utilizing a vendor-agnostic SIEM solution. Expertflow CX works with **OpenSearch** for observability but it can work with other enterprise SIEM solutions.

### Core Objectives

Our logging strategy is built upon the following functional pillars:

  * **Observability:** Deliver real-time insight into application health and operational behavior

  * **Debugging:** Enable fast identification of failures and anomalies

  * **Performance Monitoring:** Analyze latency, throughput, and service bottlenecks

  * **Auditability:** Capture and retain critical actions for security and compliance

  * **Correlation:** Link logs, traces, and metrics using trace and span identifiers




### Key Security and Data Integrity Principles

To maintain evidentiary value and system trust, all audit records adhere to the following mandates:

  * **Immutability:** Records are append-only; once written, they cannot be altered or deleted.

  * **Chronological Integrity:** Events are stored in the order of occurrence

  * **Context Awareness:** Each record contains sufficient metadata for interpretation

  * **Trace Correlation:** Logs and audit records can be linked to execution traces




### Compliance Value

Audit logging creates the forensic paper trail needed to meet global security standards. It converts raw system activity into verifiable evidence of accountability.

**Framework**| **Core Requirement**| **Strategic Value**  
---|---|---  
**SOC 2**|  Trust Service Criteria| Ensures **traceability** of admin actions, **availability** of logs during failures, and **confidentiality** of log storage.  
**ISO 27001**|  Control A.12.4| Enables event **traceability** across all resources and provides empirical evidence for incident analysis.  
**HIPAA**|  §164.312(b)| Mandates recording access to **ePHI** ; essential for detecting unauthorized disclosures and forensic breach notification.  
**GDPR**|  Articles 30 & 33| Demonstrates **accountability** in data processing and facilitates the 72-hour breach reporting window.  
**PCI DSS**|  Requirement 10| Mandates tracking all access to **cardholder data (CHD)** to detect policy violations and suspicious network activity.  
  
### Universal Security Benefits

  * **Incident Response:** Provides the telemetry needed to reconstruct the timeline of a security event.

  * **Non-Repudiation:** Ensures that a user cannot deny performing a specific action within the system.

  * **Anomaly Detection:** Establishes a baseline of "normal" behavior to highlight unauthorized administrative shifts.




## Supporting documents:

  * Architecture document: 

  * Fluentbit deployment: <https://expertflow-docs.atlassian.net/wiki/x/AwD1ag>

  * Guide to set up OpenSearch to view logs: [Logging and Tracing Integration with OpenSearch](Logging-and-Tracing-Integration-with-OpenSearch_1614413879.html)




Operations team can access the logs from Kubernetes Pods using this [guide](Accessing-Logs-from-Kubernetes-Pods_1607237654.html)
