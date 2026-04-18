---
audience: [supervisor-qa]
doc-type: reference
difficulty: beginner
aliases: []
---

# Dialing & Success Rate Campaign Summary

This report provides a comprehensive summary of dial and success rates for outbound campaigns.

## Metrics Overview
- **Total Dial Attempts**: The sum of all dialing attempts across all contacts.
- **Successful Attempts**: Calls where a customer connection was established.
- **Unsuccessful Attempts**: Calls that failed to connect.
- **Failure Reasons**: Granular breakdown of attempts based on specific failure results.

## Report Columns

| Field Name | Description |
| :--- | :--- |
| Campaign Name | The identifier for the campaign. |
| Total Uploaded Contacts | Total customer records successfully imported for the campaign. |
| Total Dialed Contacts | Number of unique contacts dialed at least once. |
| Total Connected (IVR) | Contacts successfully connected to an IVR flow. |
| Total Connected (Agent) | Contacts successfully connected to a live agent. |
| Total Dialed Attempts | The total number of calls placed (includes retries). |
| Dial Rate % | (Total Dialed Unique Contacts / Total Uploaded) * 100 |
| Success Rate % | (Total Connected / Total Dialed Unique Contacts) * 100 |

## Report Filters
- **Date Range**: Filter data by specific time periods.
- **Campaign Name**: Select one or more campaigns to analyze.
