---
sidebar_position: 0
title: "Quick Start for Supervisors & QA Leads"
summary: "Entry point for Supervisors, Quality Managers, and Evaluators — covers real-time monitoring, QA workflow orchestration, and evaluation tasks."
audience: [supervisor-qa]
product-area: [reporting, quality-management]
doc-type: tutorial
difficulty: beginner
keywords: ["supervisor", "quality manager", "evaluator", "real-time monitoring", "QA workflow", "quick start"]
aliases: ["supervisor quick start", "QA lead guide", "evaluator getting started"]
last-updated: 2026-03-27
---

# Quick Start for Supervisors & QA Leads

This path covers three related roles that monitor and evaluate contact center performance. Find your role below.

---

## I am a Supervisor

You monitor live queues and manage agent availability in real-time.

### Check queue health
Open the **Summary Dashboard** to get an instant snapshot of performance:
- **Service Level (SL%)** — is the queue meeting its target (e.g., 80/20)?
- **Oldest in Queue** — who has been waiting the longest?
- **Average Wait Time** — do you need to move agents between skills?

Filter by **Team Name** and **Queues** at the top of the dashboard to scope your view.

### Monitor active conversations
Go to **Ongoing Conversations Detail** to see live interactions. From here you can:
- **Silent Monitor** — read or listen along without the agent or customer knowing
- **Whisper Coach** — send a tip to the agent only
- **Barge-in** — join the conversation and speak to the customer directly

### Manage agent availability
Use **Available Agents Detail** to fix stuck agent states:
1. Find the agent in the list
2. Click **Change State** → select **Ready** or **Log Out**

### KPI alerts
If a threshold (e.g., Wait Time) is breached, an alert appears in the **Alerts Tab** — review it to identify conversations needing immediate attention.

→ Next: [Historical Reports Reference](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md)

---

## I am a Quality Manager

You design the quality strategy and orchestrate human and AI evaluation workflows.

### Set the pass/fail threshold
1. Go to **QM Configuration**
2. Set **Define Threshold (%)** — e.g., 70%. Any evaluation scoring below this is automatically flagged for your review.

### Choose your notification mode

| Mode | When to use |
|---|---|
| **Individual** | Real-time alert for every failed audit — best for critical industries |
| **Bulk** | Scheduled summary of failures — best for high-volume environments |

Set **Bulk Notification Interval (mins)** if using Bulk mode.

### Split work between human and AI
- **AI audits** — use for 100% coverage of standard interactions
- **Human audits** — use for complex, high-value, or flagged calibration interactions

→ See: [Configuring AI-Powered Quality Audits](../../How-to_Guides/Conversation_Designer/Configuring-AI-Powered-Quality-Audits.md)

### Close the feedback loop
After evaluations complete:
1. Review failed interactions in the **Review Queue**
2. Send results directly to the agent via the integrated feedback tool
3. Use **Override** if an AI score was incorrect — this keeps the model calibrated

→ Next: [Auditing and Scoring Conversations](../../How-to_Guides/Supervisor_and_QA_Lead/Auditing-and-Scoring-Conversations.md) · [Designing Evaluation Forms](../../How-to_Guides/Supervisor_and_QA_Lead/Designing-Evaluation-Forms.md)

---

## I am an Evaluator

You review assigned conversations and submit scored evaluations by their deadlines.

### Find your assigned evaluations
Open the **Review Screen** — evaluations are grouped by status:

| Status | Meaning |
|---|---|
| **Pending** | Assigned, not yet started |
| **In Progress** | Opened but not yet submitted |
| **Completed** | Submitted |

### Review and score
1. Click an evaluation to open the **Conversation View**
2. Review the full interaction (chat history or call recording)
3. Answer each weighted question in the evaluation form alongside the conversation
4. Add written feedback where required — all mandatory fields must be filled
5. Click **Submit** before the due date

> You can only access conversations explicitly assigned to you. Modifying evaluation form templates and assigning evaluations are Quality Manager responsibilities.

→ Next: [Quality Assurance Reports](../../How-to_Guides/Supervisor_and_QA_Lead/Quality-Assurance-Reports.md)
