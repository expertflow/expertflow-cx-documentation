---
title: "Agent Adherence Report"
summary: "Reference guide for Supervisors to analyze agent state transitions and adherence to schedules through reason code tracking."
audience: [supervisor]
product-area: [reporting, analytics]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Agent Adherence Report

The **Agent Adherence Report** provides a detailed record of every state transition an agent makes during their shift. As a Supervisor (Sam), you use this to monitor compliance with breaks and ensure that agents are using the correct **Reason Codes.**

## 1. Key Performance Insights
This report allows you to audit the non-productive time of your team.
- **Login Tracking:** Verify when agents actually start their shift.
- **Reason Code Auditing:** See exactly why agents are in a "Not Ready" state (e.g., Break, Lunch, Training).
- **Duration Tracking:** Identify agents who are spending more than the allocated time on breaks or in meetings.

## 2. Report Columns Reference
| Field | Description | Format |
| :--- | :--- | :--- |
| **Agent Name** | The name of the team member. | Text |
| **Login Time** | The timestamp of the initial sign-in for the shift. | YYYY-MM-DD HH:MM:SS |
| **Not Ready Reason** | The label of the reason code selected by the agent. | Text |
| **State Change Time** | The timestamp when the agent entered the specific state. | YYYY-MM-DD HH:MM:SS |
| **Duration** | The total time spent in that state before the next transition. | HH:MM:SS |

## 3. Using Filters for Compliance
- **Agent Filter:** Investigate the daily activity of a single agent.
- **Date/Time Range:** Review performance for a specific shift or a custom range (e.g., Last Month).
- **Adherence Auditing:** Compare the "Duration" of a "Lunch" reason code against your company's policy (e.g., 60 minutes).

### Pro-Tips for Sam:
- **Identifying "Ghosting":** If an agent has a high number of "Not Ready" states with a null or generic reason code, it may indicate they are using the system incorrectly to avoid tasks.
- **Dashboard Correlation:** Compare this report with the [Agent Performance Dashboard](Agent-Performance-Dashboard-Reference.md) to see if high "Not Ready" time is negatively impacting service levels.

---

*To configure the reason codes shown in this report, see [Configuring Reason Codes](../Solution_Admin/Configuring-Reason-Codes.md).*
