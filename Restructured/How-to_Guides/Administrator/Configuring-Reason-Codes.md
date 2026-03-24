---
title: "Configuring Reason Codes"
summary: "Guide for Solution Admins to define custom codes for agent unavailability and logout events."
audience: [administrator]
product-area: [platform, reporting]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Configuring Reason Codes

As a Solution Admin (Olivia), you must define the reasons why agents are unavailable for work. These "Reason Codes" are essential for accurately tracking agent adherence and payroll.

## 1. Types of Reason Codes
ExpertFlow CX categorizes reason codes into two main types:
- **NOT READY:** Used when an agent is logged in but cannot take new interactions (e.g., Break, Lunch, Training, Meeting).
- **LOGOUT:** Used when an agent is signing off for the day (e.g., Shift Ended, System Issue).

## 2. Creating a Reason Code
1.  Go to the **Reason Codes** section in Unified Admin.
2.  Click **Create New Reason** and fill out the following:
    - **Label:** The name visible to agents (e.g., "Team Meeting").
    - **Type:** Select either **Not Ready** or **Logout**.
    - **Description:** An optional internal note for administrative tracking.
3.  Click **Save**.

## 3. Mandatory Usage
- **Force Selection:** When an agent attempts to move to a "Not Ready" or "Logout" state, the system automatically presents the list of codes you've created.
- **Reporting Sync:** These labels appear directly in the **Agent Adherence Report**, allowing supervisors to see exactly how much time was spent in each state.

### Best Practices for Olivia:
- **Standardization:** Keep labels short and descriptive.
- **Relevance:** Periodically review which codes are being used. If a code like "System Issue" is spiking, it may indicate a technical problem that needs investigation.

---

*To see how these codes appear in reports, check the [Agent Adherence Report](../Supervisor_and_QA_Lead/Agent-Adherence-Report.md).*
