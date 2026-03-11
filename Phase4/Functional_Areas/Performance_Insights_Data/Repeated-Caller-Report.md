---
title: "Repeated Caller Report"
summary: "Reference for the Repeated Caller Report, which identifies customers who contacted the center multiple times within defined timeframes — a key indicator of unresolved first-contact issues."
audience: [supervisor, admin]
product-area: [reporting]
doc-type: reference
difficulty: beginner
keywords: ["repeated caller", "repeat contact", "FCR", "first contact resolution", "re-contact", "queue report", "historical report"]
aliases: ["repeat contact report", "re-contact report", "FCR report"]
last-updated: 2026-03-10
---

# Repeated Caller Report

The **Repeated Caller Report** identifies customers who initiated more than one conversation within a defined timeframe. High repeat-contact rates indicate unresolved issues — making this report a key input for First Contact Resolution (FCR) analysis and process improvement.

## Report Summary

| Attribute | Detail |
|---|---|
| **Report type** | Historical |
| **Primary audience** | Supervisor, Quality Manager |
| **Key use case** | Identify FCR failures; target repeat-contact queues for process improvement |

## Report Columns

| Field | Description |
|---|---|
| **Customer ID** | Unique identifier of the customer who initiated the repeated conversation. |
| **Queue Name** | The queue(s) on which the repeated conversation landed. |
| **MRD Name** | The Media Routing Domain associated with the queue (e.g., `CHAT`, `VOICE`). |
| **Repeated Chat Date Time** | Date and time when the repeated conversation started. |
| **Date & Time for First Chat** | Date and time of the customer's first conversation in the reporting period. |
| **Repeated — 24h** | Count of conversations repeated within 24 hours of the first contact. |
| **Repeated — 48h** | Count of conversations repeated between 24 and 48 hours after the first contact. |
| **Repeated — 72h** | Count of conversations repeated between 48 and 72 hours after the first contact. |
| **Repeated — over 72h** | Count of conversations repeated more than 72 hours after the first contact. |

## Report Filters

| Filter | Description |
|---|---|
| **Date / Time** | Filter by a specific date or date range. |
| **Queue Name** | Filter by one or more queue names. |
| **MRD Name** | Filter by one or more Media Routing Domains. |

## How to Read This Report

Focus first on the **Repeated — 24h** column. Customers who call back within 24 hours almost certainly did not have their issue resolved on the first contact. A high count in this column points to a specific queue, channel, or agent group that warrants investigation.

The 48h and 72h buckets capture delayed re-contacts — often customers who tried a workaround that failed, or who received a resolution that did not hold.

**Typical actions based on this report:**

- Identify the queues with the highest 24h repeat rates and review the wrap-up codes on those interactions
- Cross-reference with [QA QM Forms Evaluation](../../Supervisor/QA-QM-Forms-Evaluation.md) to identify whether agent behaviour is driving re-contacts
- Adjust routing or escalation rules for the interaction types generating the most re-contacts

## Related Articles

- [Key Reporting Metrics](Key-Reporting-Metrics.md)
- [Historical Reports Reference](../../Supervisor/Historical-Reports-Reference.md)
- [Queue Productivity Report](../../Supervisor/Queue-Productivity-Report.md)
- [QA QM Forms Evaluation](../../Supervisor/QA-QM-Forms-Evaluation.md)
