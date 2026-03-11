---
audience: [supervisor]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# WFM Admin and Supervisor Guide

This guide covers the core responsibilities of a WFM Administrator or Supervisor, from defining rules to monitoring real-time adherence.

## 1. Configuration Settings

### Contracts
Define full-time and part-time templates. Set weekly rest periods (e.g., 48:00), nightly rest, and minimum/maximum weekly hours. Toggle the specific days of the week an agent is eligible to work.

### Activities
Create color-coded activities (e.g., "Phone", "Lunch", "Coaching").
- **Flags**: Use flags like `Is Paid Time`, `Requires Skill`, or `Is Ready Time` to control how the scheduler and reporting engines treat the time.

### Leave Types
Configure leave categories (Sick, Vacation). Control whether agents can request these via self-service and whether the details are hidden from peers (Confidential flag).

## 2. Forecasting & Skills
Access via `Forecaster > Voice > Skills`.
- **Skill Targets**: Set Service Level thresholds (e.g., 80% in 20s) and occupancy bounds.
- **Queue Mapping**: Map inbound queues to specific skills. Use `Overflow In/Out` to model volume shared between departments.

## 3. Scheduling
- **Shift Creation**: Define shifts with movable start windows (e.g., 08:00–09:00 start) to allow the optimizer to find the best coverage.
- **Scheduler**: Open a team's schedule, apply forecasts, and click **Generate** to create a optimized roster. **Publish** the schedule to make it visible to agents.

## 4. Adherence Monitoring
- **State Grouping**: Map live platform states (Ready, Talking) to WFM activities.
- **View Adherence**: Use the board to spot agents who are "Out of Adherence" (e.g., on a break when they should be on the phone).

## 5. Reports
Generate and export reports in PDF or Excel format to track coverage, schedule compliance, and historical volume.
