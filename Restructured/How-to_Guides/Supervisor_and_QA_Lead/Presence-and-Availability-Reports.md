---
title: "Presence and Availability Reports"
summary: "Detailed reference for Supervisors to monitor agent state durations, adherence to breaks, and MRD-wise availability."
audience: [supervisor-qa]
product-area: [reporting, analytics]
doc-type: reference
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Presence and Availability Reports

The **Presence and Availability Reports** provide a historical audit of how your agents spend their time. As a Supervisor (Sam), use these to track adherence to schedules and calculate the actual capacity of your team across different channels.

## 1. Agent State Analysis (Global)
This report summarizes the total time spent in global states (Ready vs. Not Ready).

### Core Audit Columns:
- **Login/Logout Time:** Exact timestamps of the agent's work day.
- **Login Duration:** The total time the agent was connected to the system.
- **Ready Duration:** Cumulative time the agent was available for "Push" tasks.
- **Not Ready Duration:** Total time spent on breaks, meetings, or other non-productive states.

## 2. MRD Availability Detail
Because an agent can be ready for Chat but busy on Voice, this report breaks down availability by **Media Routing Domain (MRD).**

| Metric | Description | Format |
| :--- | :--- | :--- |
| **Active Duration** | Time spent handling at least one task in that MRD. | HH:MM:SS |
| **Busy Duration** | Time the agent reached their "Max Tasks" limit. | HH:MM:SS |
| **Total Talk Duration** | Combined Active and Busy time (Calculated as actual workload). | HH:MM:SS |
| **Availability %** | (Ready Time + Active Time) / Total Logged-in Time. | % |

## 3. Performance Insights for Sam
- **Availability Benchmarking:** Aim for an Availability % between 80-90%. If it's higher, your agents may be idle; if it's lower, they may be overwhelmed.
- **Adherence Auditing:** Filter by **Agent Name** to see if a specific person is consistently spending too much time in a "Not Ready" state compared to their peers.

---

*For real-time monitoring of these states, check the [Agent Performance Dashboard Reference](Agent-Performance-Dashboard-Reference.md).*
