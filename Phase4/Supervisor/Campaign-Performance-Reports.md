---
title: "Campaign Performance Reports"
summary: "Reference guide for Supervisors to analyze the outcome and efficiency of outbound voice and digital campaigns."
audience: [supervisor]
product-area: [campaigns, reporting]
doc-type: reference
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Campaign Performance Reports

As a Supervisor (Sam), you must track the results of your outbound campaigns to ensure your outreach is effective. The **Campaign Performance Reports** provide a high-level summary and detailed call-by-call data for every campaign in the system.

## 1. The Campaign Summary Report
This report provides a consolidated view of your campaign contact list and their final outcomes.

### Core Metrics:
- **Total Loaded:** The number of unique contacts uploaded to the campaign.
- **Dialed (Attempts):** The total number of contact attempts made, including re-dials for busy or no-answer results.
- **Connected:** The number of calls that successfully reached a person.
- **Not Connected:** Contacts where the system failed to reach a person for any reason (Voice only).

### Detailed Call Results:
- **Busy / No Answer:** The contact was dialed but did not connect.
- **Problem:** Technical failures during the attempt.
- **Dialer Abandoned:** The call connected to a customer, but no agent was available to pick up the call (for predictive dialing).

## 2. Campaign Calls Detail Report
This granular report provides a line-by-line log of every contact attempt.

### Report Columns:
| Field | Description | Format |
| :--- | :--- | :--- |
| **Campaign** | The name of the campaign. | Text |
| **DateTime** | The exact timestamp of the attempt. | YYYY-MM-DD HH:MM:SS |
| **Number Called** | The dialed phone number of the customer. | Numeric |
| **Call Result** | The outcome as returned by the dialer (e.g., Connected, Abandoned). | Text |

## 3. Using Filters for Analysis
- **Campaign Name:** Filter to see the results of a specific campaign (e.g., "Q1 Sales Blast").
- **Reporting Intervals:** Choose to see data summarized by **Hourly, Daily, Weekly, or Monthly** intervals to see performance over time.

### Pro-Tips for Sam:
- **Optimizing Results:** If your "No Answer" rate is high, consider changing the [Campaign Start Node Node](../Solution_Admin/Managing-Outbound-Campaigns.md) to a different time window when your customers are more likely to answer.
- **Dialer Abandoned:** If this count is high, it means you are over-dialing. Ask your Campaign Manager (Olivia) to adjust the [Predictive Dialing Formulas](../Solution_Admin/Managing-Outbound-Campaigns.md).

---

*For help on designing the campaigns these reports track, see [Managing Outbound Campaigns](../Solution_Admin/Managing-Outbound-Campaigns.md).*
