---
title: "Configuring Wrap-up Forms"
summary: "Guide for Solution Admins to design the outcome codes and notes fields that agents use to summarize customer interactions."
audience: [admin]
product-area: [platform, form-builder]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Configuring Wrap-up Forms

As a Solution Admin (Olivia), you define the data agents must provide at the end of a conversation. This data is critical for accurate performance reporting and identifying customer trends.

## 1. Accessing the Wrap-Up Form
ExpertFlow CX provides a **Default Wrap-Up** form that is used across all channels.
1.  Go to the **Forms** page in Unified Admin.
2.  Locate the **Wrap-Up** form and click **Edit**.

## 2. Designing Outcome Categories
To keep data organized, wrap-up codes are grouped into categories.
- **Add Category:** Create a high-level bucket (e.g., "Sales", "Support").
- **Add Options:** Inside each category, list the specific outcomes (e.g., "Order Placed", "Escalated to Tier 2").
- **Checkboxes:** Enable "Multiple Choice" if you want agents to be able to select more than one outcome for a single conversation.

## 3. Mandatory Fields & Notes
By default, the Wrap-Up form includes a **Notes** field for agents to provide a narrative summary.
- **Instruction:** Inform your agents that notes are vital for future interaction context.
- **Timer Correlation:** Ensure your wrap-up codes match the time given in the **Wrap-up Timer** settings.

### Best Practices for Olivia:
- **Keep it Lean:** Avoid adding too many categories. If an agent has to scroll through 50 options, they are more likely to pick the first one just to close the timer.
- **Reporting Sync:** Periodically review the [Historical Reports](../Supervisor/Historical-Reports-Reference.md) to see which wrap-up codes are being used most frequently.

---

*Need to configure agent-specific logout reasons? See [Configuring Reason Codes](Configuring-Reason-Codes.md).*
