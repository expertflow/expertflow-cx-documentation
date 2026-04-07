---
title: "Review Scheduler"
summary: "Configure one-time or recurring automated evaluation schedules to assign quality reviews to evaluators based on interaction filters, deadlines, and reminders."

product-area: [wfm]
doc-type: how-to
difficulty: intermediate
keywords: ["review scheduler", "QA automation", "evaluation schedule", "quality management", "recurring evaluations", "interaction filters", "evaluator assignment"]
aliases: ["evaluation scheduler", "automated QA scheduling", "scheduled evaluations"]
last-updated: 2026-03-10
---

# Review Scheduler

The **Review Scheduler** lets Quality Managers automate the assignment of evaluations — removing the need to manually select conversations for review. You define the rules once; the scheduler assigns matching conversations to evaluators on your chosen cadence.

## Prerequisites

- Quality Manager role or equivalent admin access
- At least one evaluation form created in Quality Management
- At least one evaluator assigned to the relevant team

## Steps

### 1. Link an Evaluation Form to the Schedule

Select the evaluation form that evaluators will use to score interactions. The form you choose determines which scoring criteria apply to this schedule.

1. Open **Quality Management** from the main navigation.
2. Navigate to **Review Scheduler**.
3. Click **New Schedule**.
4. In the **Evaluation Form** field, select the form to apply.

### 2. Assign Evaluators

Designate which evaluators are responsible for completing reviews under this schedule.

1. In the **Evaluators** field, select one or more evaluators by name.
2. Evaluators assigned here will receive conversation assignments automatically when the schedule runs.

### 3. Select Agents or Teams for Evaluation

Choose whose interactions this schedule will evaluate.

1. In the **Agents / Teams** field, select individual agents or entire teams.
2. The scheduler will pull conversations only from the agents or teams you specify.

### 4. Apply Interaction Filters

Narrow the pool of conversations assigned for review using one or more filters:

| Filter | Description |
|---|---|
| **Date-Time Range** | Limit to conversations that occurred within a specific window. |
| **Agent or Team** | Further restrict to a subset within the agents/teams selected above. |
| **Call Direction** | Filter by Inbound or Outbound. |
| **Wrap-up Code** | Assign evaluations only to conversations with specific wrap-up codes (e.g., "Complaint", "Escalation"). |
| **Duration** | Target short or long interactions by minimum/maximum duration. |

Combining filters reduces the evaluation pool to the highest-value conversations for your QA programme.

### 5. Set Review Deadlines

Define how long evaluators have to complete their assigned reviews.

1. In the **Deadline** field, enter the number of days after assignment by which the review must be completed.
2. The scheduler tracks this deadline and marks overdue evaluations.

### 6. Configure Reminders

Set automated reminders to prompt evaluators before deadlines pass.

1. In the **Reminders** section, enable reminders and set how many days before the deadline each reminder fires.
2. Evaluators receive a notification at each reminder interval.

### 7. Enable Recurring Evaluations (Optional)

For ongoing QA programmes, enable recurring mode so the schedule runs automatically on a defined cadence.

1. Toggle **Recurring** to **On**.
2. Set the recurrence interval (daily, weekly, or monthly).
3. When the schedule runs, it automatically selects new conversations matching your filters from the relevant period and assigns them to evaluators.

### 8. Save and Activate

1. Review all settings.
2. Click **Save** to activate the schedule.

Once active, the scheduler runs at the defined interval, assigns matching conversations, and sends reminders without further manual input.

## Related Articles

- [Designing Evaluation Forms](../../How-to_Guides/Supervisor_and_QA_Lead/Designing-Evaluation-Forms.md)
- [Managing the Quality Assurance Workflow](../../Getting_Started/For_Supervisors_and_QA_Leads/Managing-the-Quality-Assurance-Workflow.md)
- [Quality Assurance Reports](../../How-to_Guides/Supervisor_and_QA_Lead/Quality-Assurance-Reports.md)
- [Auditing and Scoring Conversations](../../How-to_Guides/Supervisor_and_QA_Lead/Auditing-and-Scoring-Conversations.md)
- [Workforce Management Overview](../../Capabilities/Workforce_Management/Workforce-Management-Overview.md)
