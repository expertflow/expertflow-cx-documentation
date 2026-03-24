---
title: "Outbound Summary Report"
summary: "Reference for the Outbound Summary Report, which shows agent-level outbound session outcomes including connected calls, disconnection reasons, talk time, and conversation duration."

product-area: [reporting]
doc-type: reference
difficulty: beginner
keywords: ["outbound summary report", "outbound calls", "outbound sessions", "talk time", "call outcomes", "dialer", "campaign", "historical report"]
aliases: ["outbound report", "outbound call report", "outbound performance report"]
last-updated: 2026-03-10
---

# Outbound Summary Report

The **Outbound Summary Report** provides a per-agent breakdown of outbound session outcomes for a selected period. Use it to assess outbound productivity, identify connection rate issues, and review how sessions end — whether by agent, customer, network, or timeout.

## Report Summary

| Attribute | Detail |
|---|---|
| **Report type** | Historical |
| **Primary audience** | Supervisor, Campaign Manager |
| **Key use case** | Monitor outbound agent productivity; diagnose low connection rates |

## Report Columns

| Field | Description |
|---|---|
| **Date** | The date of the outbound sessions. |
| **Channel Name** | The channel through which the outbound session was initiated. |
| **Agent Name** | The agent who initiated the outbound sessions. |
| **Total Outbound** | Total number of outbound sessions the agent initiated. |
| **Total Connected** | Number of sessions where a connection was established with the customer. |
| **Normal Clearing** | Sessions that ended with a standard, clean disconnection. |
| **Customer** | Sessions ended by the customer. |
| **Inactivity** | Sessions closed because the customer became inactive during the conversation. |
| **Agent** | Sessions ended by the agent. |
| **User Busy** | Sessions where the customer did not answer (line busy or no pickup). |
| **Forced Closed** | Sessions closed because the agent closed the browser tab while the task was still active. |
| **Network** | Sessions terminated due to a customer-side network failure. |
| **Decline** | Sessions where the customer ended the session before responding. |
| **Unknown** | Sessions with an unclassified disposition. |
| **Total Conversation Duration** | Total time the agent spent on all conversations. Calculated as: `SUM(conversation_end_time − conversation_start_time)`. |
| **Average Talk Time** | Average time the agent spent in active conversation per session. |
| **Total Talk Time** | Total time the agent spent in active conversation across all sessions. |

## Report Filters

| Filter | Description |
|---|---|
| **Date** | Filter by a specific date or date range. |
| **Agent** | Filter by one or more agent names. |
| **Channel** | Filter by one or more channel names. |

## How to Read This Report

**Total Connected ÷ Total Outbound** gives your agent's outbound connection rate. A rate below 40–50% on voice channels typically indicates list quality issues, calling time mismatches, or a high proportion of unreachable numbers.

High **Forced Closed** counts indicate agents are abandoning active tasks by closing their browser — a behaviour worth addressing in coaching, as it leaves customers mid-interaction.

**Unknown** dispositions indicate tasks that closed without a recognisable system reason. A rising Unknown count may signal a platform configuration issue worth investigating.

## Related Articles

- [Managing Outbound Campaigns](../../How-to_Guides/Administrator/Managing-Outbound-Campaigns.md)
- [Campaign Performance Reports](../../How-to_Guides/Supervisor_and_QA_Lead/Campaign-Performance-Reports.md)
- [Dialing Success Rate Campaign Summary](../../How-to_Guides/Supervisor_and_QA_Lead/Dialing-Success-Rate-Campaign-Summary.md)
- [Key Reporting Metrics](Key-Reporting-Metrics.md)
- [Historical Reports Reference](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md)
