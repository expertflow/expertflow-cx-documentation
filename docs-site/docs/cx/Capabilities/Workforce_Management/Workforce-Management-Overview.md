---
title: "Workforce Management Overview"
summary: "How ExpertFlow CX Workforce Management optimizes contact center staffing through interaction forecasting, scheduling, and performance tracking."

product-area: [wfm]
doc-type: explanation
difficulty: beginner
keywords: ["WFM", "workforce management", "forecasting", "scheduling", "staffing", "contact center", "resource planning", "adherence"]
aliases: ["WFM", "workforce planning", "staff scheduling"]
last-updated: 2026-03-10
---

# Workforce Management Overview

**Workforce Management (WFM)** is an optional add-on to ExpertFlow CX that helps contact centers forecast interaction volumes, schedule the right number of agents at the right time, and track adherence to those schedules in real time.

Without WFM, staffing decisions are made manually — often based on gut feel or spreadsheets. With WFM, those decisions are driven by historical data and predictive models, reducing both overstaffing costs and understaffing risks.

## What WFM Solves

| Problem | How WFM Addresses It |
|---|---|
| Unpredictable interaction spikes | Demand forecasting uses historical data to predict volume by time of day, day of week, and channel. |
| Manual scheduling overhead | Automated schedule generation assigns agents to shifts based on forecast demand and agent availability. |
| No visibility into schedule adherence | Real-time adherence tracking shows which agents are on schedule, late, or in the wrong state. |
| Siloed workforce data | Integration with ExpertFlow CX pulls actual interaction data — AHT, volume, queue wait times — directly into WFM calculations. |

## Key Capabilities

### Forecasting

WFM analyzes historical interaction data to predict future demand. Forecasts are generated per queue, per channel, and per time interval (typically 15 or 30 minutes). This allows Workforce Managers to staff precisely for expected peaks rather than applying a flat headcount across the day.

### Scheduling

Based on the forecast, WFM generates agent schedules that satisfy:

- Target service levels (e.g., answer 80% of calls within 20 seconds)
- Agent availability and shift preferences
- Contract constraints (minimum/maximum hours, days off)
- Skill requirements per queue

### Adherence Monitoring

Supervisors can view real-time adherence — comparing each agent's current activity against their scheduled activity. Agents who are late to a shift, taking an unscheduled break, or logged into the wrong queue appear as adherence exceptions.

### Reporting

WFM provides historical performance reports covering:

- Schedule adherence rates by agent and team
- Forecast accuracy (planned vs. actual volume)
- Shrinkage analysis (training, breaks, absences)

## How WFM Integrates with ExpertFlow CX

WFM is deployed as a separate Kubernetes-based service alongside ExpertFlow CX. It consumes interaction data from the CX platform — including queue statistics, agent state data, and AHT — via the platform's reporting and analytics layer.

Agents and supervisors see WFM schedule information embedded in their existing tools. No separate login is required for day-to-day schedule viewing.

## Deployment Model

WFM is available as a **CX add-on** for both on-premise and cloud-hosted deployments. Before deploying, verify that your infrastructure meets the minimum hardware and software requirements.

See [WFM Prerequisites](../../Reference/Architecture_and_Infrastructure/WFM-Prerequisites.md) for full hardware, software, and network requirements.

## Related Articles

- [WFM Prerequisites](../../Reference/Architecture_and_Infrastructure/WFM-Prerequisites.md)
- [WFM Admin and Supervisor Guide](../../How-to_Guides/Supervisor_and_QA_Lead/WFM-Admin-Supervisor-Guide.md)
- [WFM FAQs](../../How-to_Guides/Supervisor_and_QA_Lead/WFM-FAQs.md)
- [WFM Compatibility Guide](../../Reference/WFM-Compatibility-Guide.md)
- [Review Scheduler](../../How-to_Guides/Supervisor_and_QA_Lead/Review-Scheduler.md)
