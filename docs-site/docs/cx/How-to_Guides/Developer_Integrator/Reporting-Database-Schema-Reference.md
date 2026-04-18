---
title: "Reporting Database Schema Reference"
summary: "Technical reference for the relational reporting database, covering tables for conversations, activities, and team performance."
audience: [developer-integrator]
product-area: [reporting, platform]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Reporting Database Schema Reference

The ExpertFlow CX reporting engine transforms real-time event data from MongoDB into a relational schema optimized for SQL queries and BI tools (like Superset or Metabase).

## 1. Core Transactional Tables
These tables track the lifecycle of every interaction.

### `conversation`
The master record for a customer-business interaction session.
- **conversation_id (PK):** Unique identifier.
- **customer_id:** Links to the customer record.
- **state:** Current status (e.g., ACTIVE, CLOSED).
- **start_time / end_time:** Interaction timestamps.

### `agent_task`
Records specific assignments of conversations to agents.
- **task_id (PK):** Unique identifier for the assignment.
- **agent_id:** The agent assigned to the task.
- **disposition:** Outcome of the task (DONE, RONA, CANCELLED).
- **talk_time / wrapup_time:** Performance durations.

## 2. Activity & Event Tables
- **`voice_activities`:** Granular logs for call legs, hold times, and transfers.
- **`messages_bronze`:** Raw interaction logs containing the full CIM message body and header.
- **`conversation_hold_resume`:** Tracks specific hold events for SLA calculation.

## 3. Organizational & Identity Tables
- **`team`:** Maps team names to supervisors.
- **`team_members`:** Links agents and secondary supervisors to their respective teams.
- **`forms_schema`:** Stores the structures and weighting of evaluation forms used by QM.

## 4. Integration Usage
| Use Case | Recommended Table |
| :--- | :--- |
| **SLA Calculation** | `conversation` + `agent_task` |
| **Agent Adherence** | `agent_task` (Disposition: AGENT_LOGOUT) |
| **Audit Trails** | `messages_bronze` (Raw Payloads) |
| **Quality Analysis** | `forms_gold` (Pre-calculated Scores) |

---

*For real-time data objects, see the [Platform Objects and Data Model](Platform-Objects-and-Data-Model.md).*
