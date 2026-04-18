---
title: "Interval Performance Report"
summary: "Detailed reference for Supervisors to monitor queue performance and interaction volume in 15 or 30-minute intervals."
audience: [supervisor-qa]
product-area: [reporting, analytics]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Interval Performance Report

The **Interval Performance Report** enables you to identify traffic spikes and service level fluctuations throughout the day. By breaking data down into 15 or 30-minute intervals, you can see exactly when your team is most stressed.

## 1. Key Performance Metrics
This report focuses on the efficiency of your queues at a granular level.

### Queue Volume Metrics:
- **Total Answered:** Total interactions successfully picked up by agents within the interval.
- **Total Abandoned:** Customers who left the queue before an agent responded.
- **Longest Queued:** The maximum wait time a customer experienced during the interval.
- **MAX Queued:** The total number of interactions that entered the queue.

### Speed & Efficiency Metrics:
- **Average Speed of Answer:** The mean time a customer waited before being connected to an agent.
- **Average Abandoned Time:** The mean time a customer waited before hanging up.
- **Answered in Threshold (60s, 120s, 180s, 240s):** A count of interactions answered within specific time buckets to visualize SLA compliance.

## 2. Report Columns Reference
| Field | Description | Format |
| :--- | :--- | :--- |
| **Queue** | The name of the specific queue being analyzed. | Text |
| **DateTime** | The timestamp for the start of the interval. | YYYY-MM-DD HH:MM |
| **Interval (60 SEC)** | Static bucket for interactions answered within 60 seconds. | Count |
| **Abandoned OVER 240 SEC** | Interactions where the customer hung up after waiting for more than 4 minutes. | Count |

## 3. Using Filters for Trend Analysis
- **Date/Time Range:** Review performance for a specific peak period (e.g., "Monday Morning Rush").
- **Queue Filter:** Compare two queues (e.g., "Voice" vs. "WhatsApp") to see which channel has higher abandonment rates.

### Pro-Tips for Sam:
- **Spotting Spikes:** Use this report to justify additional staffing during specific hours of the day. 
- **Abandonment Analysis:** If your "Average Abandoned Time" is low, it means customers are hanging up almost immediately, which could indicate a technical issue with the initial greeting.

---

*For real-time queue data, check the [Agent Performance Dashboard Reference](Agent-Performance-Dashboard-Reference.md).*
