---
title: "Managing Outbound Campaigns"
summary: "End-to-end guide for creating, managing, and optimizing multi-channel outbound campaigns for voice and digital channels."
audience: [admin]
product-area: [campaigns, outbound]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Managing Outbound Campaigns

ExpertFlow CX Campaigns empower you to automate customer outreach across Voice, SMS, and WhatsApp. As a Campaign Manager, you transform business objectives (lead gen, collections) into automated logic using our visual Flow Builder.

## 1. Preparing Your Audience
Before building a flow, you must define your target list.
1.  **Upload Contacts:** Import customer data via CSV. Ensure headers match system attributes (e.g., `Phone 1`, `AccountID`).
2.  **Create Filters:** Use the Filter module to segment your database (e.g., "Overdue Accounts"). Filters are dynamic; new customers matching the criteria are added automatically.

## 2. Campaign Lifecycle
Manage your activities from the **Campaigns** dashboard.
- **Unpublished:** Draft mode. No interactions are sent.
- **Published:** Active and running according to the flow logic.
- **Stopped:** Permanently archived. Note: Stopped campaigns cannot be republished.

## 3. Designing the Flow
The **Flow Builder** uses nodes to define logic. Every campaign must start with a **Start Node**.

### Core Flow Nodes:
- **Start Node:** Defines the "pulse" interval (e.g., every 10s) and the allowed time/day windows.
- **Check Undelivered:** (Best Practice) Prevents duplicate dialing by checking if a contact has already been processed.
- **Seize Agent:** Used in Agent-Based campaigns to reserve a human resource before dialing the customer.
- **Init Node:** Triggers the actual contact attempt (Dial for voice, Send for digital).

## 4. Dialing Strategies
- **Power Dialing:** Dials a fixed ratio of contacts per available agent.
- **Predictive Dialing:** Uses PROMQL formulas to "over-dial" based on live metrics, minimizing agent idle time.
- **Digital Messaging:** A "Fire and Forget" flow for SMS/WhatsApp notifications.

---

*For performance analysis, see the [Campaign Performance Reports](../Supervisor/Campaign-Performance-Reports.md).*
