---
title: "Questions' Summary Report"
summary: "Reference for the Questions' Summary Report, which aggregates customer survey responses per question to track satisfaction trends and NPS scores across all interactions."

product-area: [reporting]
doc-type: reference
difficulty: beginner
keywords: ["questions summary report", "survey report", "NPS", "CSAT", "satisfaction", "survey questions", "response breakdown", "historical report"]
aliases: ["survey summary report", "question response report", "NPS summary"]
last-updated: 2026-03-10
---

# Questions' Summary Report

The **Questions' Summary Report** provides an aggregate view of how customers responded to each survey question across all interactions in the selected period. While the [Agents' Summary Report](Agents-Summary-Report.md) focuses on individual agent scores, this report focuses on the survey itself — revealing which questions drive satisfaction or dissatisfaction at a program level.

## Report Summary

| Attribute | Detail |
|---|---|
| **Report type** | Historical |
| **Primary audience** | Supervisor, Quality Manager, Decision Maker |
| **Key use case** | Assess overall survey effectiveness; identify satisfaction drivers and problem areas |

## Report Columns

| Field | Description |
|---|---|
| **Total Surveys Offered** | The total number of surveys presented to customers in the selected period. |
| **Total Responses** | The total number of responses received across all survey questions. |
| **Survey Questions** | Each question listed with its type (NPS, 5-star rating, multiple choice) and total responses received per answer option. |
| **Response Breakdown** | For each question, the count of responses per answer option. For example, a 5-star question shows the count of 5-star, 4-star, 3-star, 2-star, and 1-star responses. |
| **NPS Calculation** | For NPS questions, the report calculates the NPS score based on the distribution of Promoters (9–10), Passives (7–8), and Detractors (0–6). Formula: `% Promoters − % Detractors`. |
| **Average Scores** | For numerical rating questions (NPS, 5-star), the average score across all responses — useful for tracking trend movement over time. |

## Report Views

| View | Description |
|---|---|
| **Daily** | Response volumes and scores per day — useful for identifying post-incident sentiment dips. |
| **Weekly** | Week-on-week comparison of scores and response rates. |
| **Monthly** | Month-on-month trend tracking for executive reporting. |

## How to Read This Report

Start with **Total Surveys Offered vs. Total Responses** to assess your survey completion rate. A low completion rate (under 30%) suggests the survey is too long, poorly timed, or not well-presented to customers.

For each question, review the **Response Breakdown** to understand distribution. An NPS question with a bimodal distribution (many 10s and many 0s) signals a polarised customer experience that warrants deeper investigation — likely tied to specific agents, channels, or interaction types.

## Related Articles

- [Agents' Summary Report](Agents-Summary-Report.md)
- [Creating Survey Forms and Flows](../../How-to_Guides/Conversation_Designer/Creating-Survey-Forms-and-Flows.md)
- [Historical Reports Reference](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md)
- [Key Reporting Metrics](Key-Reporting-Metrics.md)
