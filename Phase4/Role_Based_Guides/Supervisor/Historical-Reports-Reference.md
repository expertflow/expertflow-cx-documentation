---
title: "Historical Reports Reference"
summary: "Detailed reference for historical reporting and dashboards to analyze long-term agent and queue performance."
audience: [supervisor]
product-area: [reporting, dashboards]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Historical Reports Reference

The **Historical Reports** enable you to analyze long-term performance trends across your teams and queues. As a Supervisor (Sam), you use these to identify productivity gains and ensure your service levels are being met.

## 1. The Agent Performance Report
This is your most valuable report for tracking individual agent productivity over a specific period.

### Core Report Columns:
| Field | Description | Format |
| :--- | :--- | :--- |
| **Interval** | The time window of the data (default is 15 minutes). | HH:MM |
| **Calls Answered** | Number of interactions successfully picked up by the agent. | Count |
| **Calls Handled** | Interactions answered and completed with a wrap-up. | Count |
| **Talk Time** | Total time spent in active conversation. | HH:MM:SS |
| **Hold Time** | Duration the agent put interactions on hold. | HH:MM:SS |
| **Ring Time** | Time the task offered before being answered (Latency). | HH:MM:SS |
| **Not Ready Time** | Total time spent in an unavailable state. | HH:MM:SS |
| **Wait Time** | Total time the agent spent in a "Ready" state awaiting a task. | HH:MM:SS |
| **External Transfer** | Interactions transferred to an external party. | Count |

## 2. Using Filters for Analysis
Historical reports allow for precise data extraction based on your needs.
- **Date/Time Range:** Select the period you want to analyze (e.g., Yesterday, Last 7 Days, Custom Range).
- **Agent Name:** Filter to see the performance of a specific team member.
- **Queue Name:** Analyze which queues are experiencing the most traffic or the longest wait times.

## 3. Reporting Dashboard Access
To access these reports, navigate to the **Analytics & Reporting** module.
- **Superset Integration:** All historical reports are powered by Superset, providing a robust interface for data visualization. 
- **Timezone:** Always ensure your reports are filtered using the correct **UTC Offset** for your region to maintain data accuracy.

---

*For real-time data, check the [Agent Performance Dashboard Reference](Agent-Performance-Dashboard-Reference.md).*
