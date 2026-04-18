---
sidebar_position: 2
title: "Managing the Quality Assurance Workflow"
summary: "Getting started guide for Quality Managers — the 6-step QM workflow covering form design, scheduling, assignment, evaluation, and reporting."
audience: [supervisor-qa]
product-area: [quality-management]
doc-type: tutorial
difficulty: beginner
keywords: ["quality management", "QA workflow", "evaluation forms", "review scheduler", "quality manager", "QM configuration", "AI quality management"]
aliases: ["QA workflow guide", "quality manager getting started", "QM workflow CX"]
last-updated: 2026-03-27
---

# Managing the Quality Assurance Workflow

As a Quality Manager, you design the evaluation strategy and orchestrate both human and AI-driven audits. The workflow has six steps.

---

## Step 1: Design Evaluation Forms

Create the rubrics your Evaluators will use to score agent interactions.

1. Go to **Quality Management → Evaluation Forms**.
2. Add sections (e.g., Communication, Compliance, Problem Solving) and assign each a percentage weight — all sections must sum to 100%.
3. Add questions inside each section with their own weights.
4. Use **Weighted Single Select** questions (Yes/No, 1–5 scale) for scored criteria; use text inputs for coaching notes.
5. Click **Save** once the form validates.

→ Full guide: [Designing Evaluation Forms](../../How-to_Guides/Supervisor_and_QA_Lead/Designing-Evaluation-Forms.md)

---

## Step 2: Configure QM Settings

Before running evaluations, set your pass/fail threshold and notification preferences.

1. Go to **QM Configuration**.
2. Set **Define Threshold (%)** — e.g., 70%. Evaluations scoring below this are flagged automatically.
3. Choose a notification mode:

| Mode | When to use |
|---|---|
| **Individual** | Real-time alert per failed audit — best for critical industries |
| **Bulk** | Scheduled summary of failures — best for high-volume environments |

---

## Step 3: Schedule Bulk Evaluations

Assign batches of conversations to Evaluators automatically.

1. Go to **Quality Management → Review Scheduler**.
2. Filter by agent, team, Evaluator, channel, or call properties.
3. Set a **one-time** or **recurring** schedule with a completion deadline.

→ Full guide: [Review Scheduler](../../How-to_Guides/Supervisor_and_QA_Lead/Review-Scheduler.md)

---

## Step 4: Assign Individual Evaluations

For ad-hoc reviews, assign specific conversations manually.

1. Go to **Quality Management → Conversation List**.
2. Find the target conversation and assign it to an Evaluator.

---

## Step 5: Use AI for Full Coverage

Instead of relying solely on human evaluators, enable AI-driven evaluation to cover 100% of interactions.

| Mode | Description |
|---|---|
| **Full Automation** | AI evaluates every closed interaction |
| **Hybrid** | A configured percentage goes to AI; the rest to human Evaluators |

AI scores appear in the same interface as human scores. You can override any AI score to keep the model calibrated.

→ Full guide: [AI-Driven Quality Management](../../How-to_Guides/Supervisor_and_QA_Lead/AI-Driven-Quality-Management.md)

---

## Step 6: Review Results and Close the Loop

1. Open **Quality Management → Review Screen** to track evaluation statuses (Pending, In Progress, Completed).
2. Review failed interactions in the **Review Queue**.
3. Send feedback directly to the agent via the integrated feedback tool.
4. Use **Quality Assurance Reports** to identify trends and coaching opportunities.

→ Full guide: [Quality Assurance Reports](../../How-to_Guides/Supervisor_and_QA_Lead/Quality-Assurance-Reports.md)

---

## Related Articles

- [As a Quality Manager](../../How-to_Guides/Supervisor_and_QA_Lead/As-a-Quality-Manager.md)
- [Designing Evaluation Forms](../../How-to_Guides/Supervisor_and_QA_Lead/Designing-Evaluation-Forms.md)
- [AI-Driven Quality Management](../../How-to_Guides/Supervisor_and_QA_Lead/AI-Driven-Quality-Management.md)
- [Auditing and Scoring Conversations](../../How-to_Guides/Supervisor_and_QA_Lead/Auditing-and-Scoring-Conversations.md)
- [Evaluator Guide](./Evaluator-Guide.md)
