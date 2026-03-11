---
title: "Agents' Summary Report"
summary: "Reference for the Agents' Summary Report, which shows customer survey ratings and NPS scores per agent to assess individual performance and identify coaching opportunities."
audience: [supervisor, admin]
product-area: [reporting]
doc-type: reference
difficulty: beginner
keywords: ["agents summary report", "agent performance", "survey responses", "NPS", "CSAT", "satisfaction score", "agent rating", "historical report"]
aliases: ["agent survey report", "agent satisfaction report", "agent NPS report"]
last-updated: 2026-03-10
---

# Agents' Summary Report

The **Agents' Summary Report** shows how customers rated individual agents through post-interaction surveys. It aggregates survey responses, NPS scores, and satisfaction ratings per agent — making it the primary report for assessing agent-level customer experience performance.

## Report Summary

| Attribute | Detail |
|---|---|
| **Report type** | Historical |
| **Primary audience** | Supervisor, Quality Manager |
| **Key use case** | Identify top and bottom performers; target coaching based on customer feedback |

## Report Columns

| Field | Description |
|---|---|
| **Agent Name** | The name of the agent who handled the interaction. |
| **Survey Responses** | Customer responses to each survey question. Includes a note if a question was skipped and the reason for skipping, where available. |
| **NPS and Satisfaction Scores** | Calculated Net Promoter Score (NPS) and satisfaction ratings for each agent, showing overall customer sentiment toward that individual. |
| **Average Scores per Agent** | For rating questions (e.g., 5-star ratings), the average score the agent received across all surveyed interactions. |
| **Response Count** | The total number of customers who provided feedback for each agent, along with the breakdown of rating values. |

## Report Views

The report supports the following time-based views:

| View | Description |
|---|---|
| **Weekly** | Performance aggregated by week, useful for spotting short-term trends or the impact of coaching sessions. |
| **Monthly** | Performance aggregated by month, useful for performance reviews and target tracking. |

## How to Read This Report

Use **Average Scores per Agent** as your primary ranking metric. Agents with consistently low average scores across multiple periods warrant a coaching conversation — compare their scores against [Questions' Summary Report](Questions-Summary-Report.md) to identify which survey questions they score lowest on.

A high **skipped question** rate may indicate that agents are ending interactions before the survey completes, or that the survey flow has a configuration issue worth investigating.

## Related Articles

- [Questions' Summary Report](Questions-Summary-Report.md)
- [Historical Reports Reference](../../Supervisor/Historical-Reports-Reference.md)
- [QA QM Forms Evaluation](../../Supervisor/QA-QM-Forms-Evaluation.md)
- [Agent Performance Dashboard Reference](../../Supervisor/Agent-Performance-Dashboard-Reference.md)
- [Creating Survey Forms and Flows](../../Designer/Creating-Survey-Forms-and-Flows.md)
