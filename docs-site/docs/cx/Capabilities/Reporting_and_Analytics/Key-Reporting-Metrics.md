---
title: "Key Reporting Metrics"
summary: "Definitions of core conversation and queue metrics used across ExpertFlow CX historical and real-time reports, including SLA calculation types."

product-area: [reporting]
doc-type: reference
difficulty: beginner
keywords: ["reporting metrics", "SLA", "service level", "handled conversation", "abandoned conversation", "AHT", "AnsweredWithinSL", "AbandonedWithinSL", "queue metrics"]
aliases: ["reporting glossary", "metric definitions", "SLA calculation", "contact center KPIs"]
last-updated: 2026-03-10
---

# Key Reporting Metrics

This reference defines the core metrics used across ExpertFlow CX historical and real-time reports. Use these definitions to interpret report data consistently and configure queue service level thresholds correctly.

## Conversation State Metrics

| Metric | Definition |
|---|---|
| **Handled Conversation** | A conversation is Handled when the disposition of its last task is set to `CLOSED` with reason code `DONE`. |
| **Abandoned Conversation** | A conversation is Abandoned when the customer disconnects while waiting in the queue or during agent alerting (ringing). The agent task closes with state `CLOSED` and reason code `CANCELLED`. |

## Service Level Metrics

**Service Level (SL%)** measures the percentage of incoming conversations that an agent answers within a defined time threshold. The threshold timer starts the moment the conversation enters a precision queue.

**Example:** If your SL threshold is 120 seconds and your SL target is 80%, you are aiming to answer 80% of conversations within 2 minutes.

| Metric | Definition |
|---|---|
| **AnsweredWithinSL** | A queued conversation accepted by an agent within the SL threshold. |
| **AnsweredAfterSL** | A queued conversation accepted by an agent after the SL threshold has elapsed. |
| **AbandonedWithinSL** | A queued conversation abandoned by the customer before the SL threshold elapsed. |
| **AbandonedAfterSL** | A queued conversation abandoned by the customer after the SL threshold elapsed. |
| **OfferedWithinSL** | `AnsweredWithinSL` + `AbandonedWithinSL` — all conversations that reached the queue within the SL window. |

## Service Level Calculation Types

The SL% formula applied in reports depends on the **Service Level Type** configured per queue. There are three types:

| Type | Name | Formula |
|---|---|---|
| **Type 1** | Ignore Abandoned | `AnsweredWithinSL ÷ (TotalOffered – AbandonedWithinSL)` |
| **Type 2** | Abandoned = Negative Impact | `AnsweredWithinSL ÷ TotalOffered` |
| **Type 3** | Abandoned = Positive Impact | `(AnsweredWithinSL + AbandonedWithinSL) ÷ TotalOffered` |

**Choosing the right type:**

- Use **Type 1** if your team is not responsible for abandoned contacts (e.g., customers who abandon immediately before being answered skew your SLA unfairly).
- Use **Type 2** for the strictest SLA measurement — every abandon counts against you.
- Use **Type 3** if early abandons (customers who hang up quickly) should be treated as self-served successes.

Configure the Service Level Type in the queue settings under **Unified Admin > Queues**.

## Common Derived Metrics

| Metric | Definition |
|---|---|
| **AHT (Average Handle Time)** | The average total duration an agent spends on a conversation, including talk time and wrap-up time. |
| **FCR (First Contact Resolution)** | The percentage of conversations resolved without the customer needing to contact again within a defined period (typically 24–72 hours). See [Repeated Caller Report](Repeated-Caller-Report.md). |
| **Occupancy** | The percentage of logged-in time an agent spends handling interactions (talk + wrap-up), versus idle/available time. |
| **Shrinkage** | The percentage of scheduled time agents are unavailable for interactions (training, breaks, absences, system issues). |

## Related Articles

- [Historical Reports Reference](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md)
- [Queue Productivity Report](../../How-to_Guides/Supervisor_and_QA_Lead/Queue-Productivity-Report.md)
- [Interval Performance Report](../../How-to_Guides/Supervisor_and_QA_Lead/Interval-Performance-Report.md)
- [Repeated Caller Report](Repeated-Caller-Report.md)
- [Routing Attributes and Queues](../../How-to_Guides/Administrator/Routing-Attributes-and-Queues.md)
