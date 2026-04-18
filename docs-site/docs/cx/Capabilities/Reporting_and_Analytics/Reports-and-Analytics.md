---
title: "Reports and Analytics"
summary: "Reference overview of the ExpertFlow CX reporting and analytics suite — covering all report categories including conversation, quality, agent, queue, outbound campaign, IVR, WebRTC, and survey reports."

product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["CX reports", "analytics overview", "ExpertFlow reporting", "contact center reports", "historical reports", "real-time analytics", "Superset reporting", "CX dashboards", "report categories"]
aliases: ["reporting overview", "CX analytics", "all reports CX"]
last-updated: 2026-03-10
---

# Reports and Analytics

ExpertFlow CX provides a comprehensive suite of reports and analytics built on a unified data platform. All interaction data from voice, digital, and social media channels is consolidated into a single data lake with an ETL layer, giving a complete view of contact center performance, agent behaviour, and customer trends.

Reports are delivered through **Apache Superset** (historical reports and dashboards) and **real-time dashboards** embedded in the supervisor interface.

---

## Report Categories

### Conversation and Channel Reports

Detailed insights into the customer journey from first interaction to outcome.

| Report | Summary |
|---|---|
| **Channel Stats Summary** | Summarises all conversations opened for a particular channel during a selected period. |
| **Channel Stats Graph** | Shows the percentage of channel sessions closed due to each disposition type. |
| **Repeated Caller Report** | Identifies customers who have made multiple contacts within a specified timeframe. |
| **Outbound Summary Report** | Provides a summary of all outbound conversations. |
| **Conversation Detail** | Detailed record per conversation: direction, queue, start/end time, duration, agent, customer, routing mode, transfer counts, bot participation %, transcript, and disposition. |
| **Historical Conversation Summary** | Summarises all conversations over a period regardless of channel type or queue. |
| **Multichannel Session Detail** | Details of multiple channel sessions within a single conversation. |
| **Channel Session Detail** | Details of each individual channel session in a conversation. |
| **Conversation Volume by Disposition** | Bar chart of conversations handled by Agent, Bot, and Network. |
| **Wrap-up Summary** | Count of conversations grouped by wrap-up category and reason. |

---

### Quality and Performance Reports

Evaluate agent quality scores and QM outcomes.

| Report | Summary |
|---|---|
| **Team Comparison** | Visual and tabular comparison of team-level evaluation scores across a selected time range, with filters by team, form, section, and question. |
| **Agent & Team Leaderboard** | Ranked performance data based on evaluation results — shows reviews, average scores, and score variance. |
| **Evaluator Comparison** | Compares how multiple evaluators scored the same agent using the same form — supports calibration. |
| **Evaluation Volume** | Counts of evaluations by status (planned, in progress, completed) in tabular and graphical views. |
| **Skills Assessment** | Agent or team performance based on evaluation form scores, with graphical and tabular output. |

---

### Agent and Queue Reports

Historical and real-time data on agent activity and queue performance.

| Report | Summary |
|---|---|
| **Agent Availability Report** | MRD-wise availability statistics per agent: logged-in, ready, not-ready, active, busy durations, and availability %. |
| **Agent Task Detail** | All conversation tasks handled by the agent including RONA (Redirect on No Answer) events. |
| **Agent Not Ready Detail** | Details of each not-ready reason per agent. |
| **Agent Not-Ready Summary** | Summary of not-ready reason durations per agent. |
| **Agent Performance Report** | Agent KPIs in 15-minute intervals. |
| **Agent Productivity By Queue** | Concise summary of agent productivity per queue with total tasks assigned. |
| **Agent State Analysis Report** | Time in each agent state (ready, not-ready and reason) for visualization and monitoring. |
| **Answered Chats in Time Intervals** | Tasks answered by agents in 15-minute interval buckets. |
| **Queue Stats Today** | Queue statistics for the current day since midnight. |
| **Queue-wise Stats Summary** | Count of requests per queue: offered, done, cancelled, transferred, and more. |
| **Transferred Tasks per Queue** | Bar chart of tasks transferred out from each queue. |
| **Queue Flushed Conversation Count** | Count of conversations forcefully closed per queue by administrator or supervisor. |

---

### Outbound Campaign Reports

Performance, efficiency, and effectiveness of proactive outbound calling.

| Report | Summary |
|---|---|
| **Campaign Summary** | Campaign contact status grouped by call result. |
| **Connected Calls Detail** | Details of successfully connected calls — excludes abandoned calls. |
| **Dialing & Success Rate Summary** | Dial and success rate per campaign. |
| **Campaign Calls Detail Report** | All calls attempted by the dialer but not connected, including agent-based and IVR-based attempts. |

---

### IVR Reports

Insights into customer self-service interactions with the IVR system.

| Report | Summary |
|---|---|
| **IVR Summary Report** | Summarises IVR activity journey per day. |
| **IVR Detail Report** | Detailed IVR journey per call for each customer. |

---

### WebRTC Reports

Quality and volume of browser-based communications.

| Report | Summary |
|---|---|
| **WebRTC Summary Report** | Summary of WebRTC generated links and sessions. |
| **WebRTC Detail Report** | Detailed view of each WebRTC link and session. |

---

### Survey Reports

Customer feedback and satisfaction data collected via CX Surveys.

| Report | Summary |
|---|---|
| **Agents' Summary Report** | Agent performance based on customer survey ratings per agent. |
| **Questions' Summary Report** | Overview of customer responses to each survey question across all interactions. |

---

## Data Freshness

All historical reports update **after a conversation or channel session is closed and processed**. By default, the ETL pipeline runs at 5-minute intervals. Live conversations do not appear in historical reports until finalized.

For real-time data, use the [Real-time Contact Center Analytics](Real-time-Contact-Center-Analytics.md) dashboards.

---

## Related Articles

- [Real-time Contact Center Analytics](Real-time-Contact-Center-Analytics.md)
- [Key Reporting Metrics](Key-Reporting-Metrics.md)
- [Historical Reports Reference](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md)
- [Superset Reports Configuration](../../How-to_Guides/Administrator/Superset-Reports-Configuration.md)
