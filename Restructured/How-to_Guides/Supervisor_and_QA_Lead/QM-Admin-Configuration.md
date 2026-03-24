---
title: "QM Admin Configuration"
summary: "Reference for the QM Admin role in ExpertFlow CX — covering how to configure quality management alert thresholds and alert delivery modes for low-scoring evaluation notifications."
audience: [supervisor-qa]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["QM admin CX", "quality management admin", "alert threshold QM", "evaluation alert CX", "QM notification CX", "low score alert CX", "quality manager notification", "bulk alert QM CX"]
aliases: ["QM admin guide CX", "quality management configuration CX", "QM alert setup CX"]
last-updated: 2026-03-10
---

# QM Admin Configuration

The **QM Admin** role in ExpertFlow CX is responsible for configuring the notification and alerting system for Quality Management. QM Admins define how and when Quality Managers are notified about low-scoring evaluations.

> To assign a user the QM Admin role, contact your administrator for IAM/Keycloak role configuration.

---

## QM Admin Workflow

### Step 1: Configure Alert Threshold

Define the performance score threshold that triggers low-scoring evaluation alerts.

- Set the minimum acceptable score for evaluations.
- Any evaluation scoring below the threshold will trigger an alert to the Quality Manager.
- This ensures Quality Managers are promptly informed of interactions that require immediate attention, coaching, or escalation.

### Step 2: Configure Alert Delivery

Control how low-scoring evaluation alerts are delivered to Quality Managers. Two delivery modes are available:

| Mode | Description |
|---|---|
| **Real-time** | Alerts are sent immediately when an individual evaluation falls below the threshold score. Best for urgent quality concerns. |
| **Bulk summary** | Alerts are batched and sent at a configured interval (e.g., hourly, daily). Best for high-volume environments where real-time alerts would create noise. |

Alert delivery configuration is accessible via a dedicated configuration tab in the QM Admin section of Unified Admin.

---

## Related Articles

- [As a Quality Manager](As-a-Quality-Manager.md)
- [AI-Driven Quality Management](AI-Driven-Quality-Management.md)
- [Designing Evaluation Forms](Designing-Evaluation-Forms.md)
- [Auditing and Scoring Conversations](Auditing-and-Scoring-Conversations.md)
