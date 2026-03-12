---
title: "Managing the Quality Assurance Workflow"
summary: "Guide for Quality Managers to orchestrate human and AI evaluation processes, set thresholds, and manage alerts."
audience: [qm]
product-area: [quality-management]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Managing the Quality Assurance Workflow

As a Quality Manager (Quentin), your role is to design the quality strategy and ensure the evaluation team (Eva) and the AI Evaluator are aligned. This guide covers how to set performance thresholds and orchestrate the audit flow.

## 1. Defining Quality Standards
Your first task is to define what constitutes a "Passed" interaction. This is done through the **Evaluation Score Threshold**.

### How to set the Threshold:
1. Navigate to **QM Configuration**.
2. Locate the **Define Threshold (%)** field.
3. Enter the minimum score required for compliance (e.g., 70%).
4. **Impact:** Any evaluation (Human or AI) that falls below this percentage will be automatically flagged for your review.

## 2. Orchestrating the Audit Workflow
ExpertFlow allows you to choose how your team receives alerts about poor-quality interactions.

### Configuration Options:
| Notification Type | Workflow Impact | Best For |
|-------------------|-----------------|----------|
| **Individual** | Real-time alerts for every failed audit. | Critical industries (Finance/Health). |
| **Bulk** | Consolidates failures into a scheduled summary. | High-volume environments. |

### Setting the Notification Logic:
1. In **QM Configuration**, select your preferred **Notification Type**.
2. If using **Bulk**, set the **Bulk Notification Interval (mins)**. 
   - *Example:* A 60-minute interval sends you a summary of all quality failures once per hour.

## 3. Human vs. AI Workload Assignment
To balance efficiency with accuracy, you can distribute audits between your human team and the AI engine.

- **AI Audits:** Use for 100% coverage of standard interactions.
- **Human Audits:** Use for complex, high-value, or flagged "Calibration" interactions.
- *For technical AI setup, see the [Configuring AI-Powered Quality Audits](../AI_Specialist/Configuring-AI-Powered-Quality-Audits.md) guide.*

## 4. Closing the Loop: Feedback & Coaching
Once an evaluation is complete:
1. **Low Scores:** Review the failed interactions in the **Review Queue**.
2. **Coaching:** Use the integrated feedback tool to send the evaluation results directly to the **Agent (Amy)**.
3. **Calibration:** If the AI Evaluator's score was incorrect, use the **Override** function to maintain model accuracy.

---

*Next Step: Learn how to analyze long-term quality trends in the [Quality Performance Dashboard](../Supervisor/Monitoring-Your-Team-in-Real-Time.md).*
