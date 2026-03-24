---
title: "SLA Calculations"
summary: "Reference explaining how ExpertFlow CX calculates Service Level metrics for queue conversations — covering all scenarios including answered within threshold, abandoned before/after threshold, RONA, and no agents available."
audience: [supervisor-qa]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["SLA calculations", "service level", "chats offered", "chats answered", "chats abandoned", "RONA SLA", "SLA threshold", "service level calculation CX", "contact center SLA"]
aliases: ["service level CX", "SLA formula", "SL calculation contact center"]
last-updated: 2026-03-10
---

# SLA Calculations

ExpertFlow CX tracks Service Level (SL) metrics for queue conversations. The table below explains how each metric is counted across the eight key conversation scenarios, based on whether the conversation was answered, abandoned, or timed out relative to the SL threshold.

## SLA Metric Definitions

| Metric | Description |
|---|---|
| `chats_offered` | Total conversations offered to the queue. |
| `chats_answered` | Conversations accepted by an agent. |
| `chats_abandoned` | Conversations where the customer left before connecting to an agent. |
| `chats_rona` | Conversations where an agent was assigned but did not accept (Redirect on No Answer). |
| `NoAgentAvailable` | Conversations where no agent was available in the queue. |
| `service_level_offered` | Conversations offered within the SL threshold window. |
| `service_level_answered` | Conversations answered within the SL threshold. |
| `service_level_abandoned` | Conversations abandoned within the SL threshold window. |
| `service_level_rona` | RONA events that occurred within the SL threshold. |

## Calculation by Scenario

| # | Scenario | offered | answered | abandoned | rona | NoAgent | sl_offered | sl_answered | sl_abandoned | sl_rona |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Routed to agent **within SL threshold** — agent accepts | 1 | 1 | 0 | — | — | 1 | 1 | 0 | — |
| 2 | Customer **abandons before routing**, before SL threshold expires | 1 | 0 | 1 | — | — | 1 | 0 | 1 | — |
| 3 | Routed to agent **within SL threshold** — customer abandons before agent accepts | 1 | 0 | 1 | — | — | 1 | 0 | 1 | — |
| 4 | Routed to agent **after SL threshold** — customer abandons before agent accepts | 1 | 0 | 1 | — | — | 0 | 0 | 0 | — |
| 5 | Routed to agent **after SL threshold** — agent accepts | 1 | 1 | 0 | — | — | 0 | 0 | 0 | — |
| 6 | Routed to agent **after SL threshold** — agent does not accept (RONA) | 1 | 0 | 0 | 1 | — | 0 | 0 | 0 | 0 |
| 7 | Routed to agent **within SL threshold** — agent does not accept (RONA) | 1 | 0 | 0 | 1 | — | 1 | 0 | 0 | 1 |
| 8 | Conversation queued — **no agents available** | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |

## Key Observations

- **Scenario 1** is the ideal outcome — offered and answered within threshold, SL achieved.
- **Scenario 2 and 3** count as abandoned within the SL window — the customer left while still eligible for service.
- **Scenario 4** — abandonment after the threshold has expired — does not contribute to SL metrics at all.
- **Scenario 5** — answered after the threshold — counts as answered but not within service level.
- **Scenario 7** — RONA within threshold — counts as an SL-offered RONA event.
- **Scenario 8** — no agent available — is tracked separately via `NoAgentAvailable` and does not count toward SL metrics.

## Related Articles

- [Customer Inactivity SLA](Customer-Inactivity-SLA.md)
- [Queue Productivity Report](Queue-Productivity-Report.md)
- [Key Reporting Metrics](../../Capabilities/Reporting_and_Analytics/Key-Reporting-Metrics.md)
- [Historical Reports Reference](Historical-Reports-Reference.md)
