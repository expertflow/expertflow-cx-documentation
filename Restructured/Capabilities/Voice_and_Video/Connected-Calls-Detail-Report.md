---
title: "Connected Calls Detail Report"
summary: "Reference for the Connected Calls Detail Report, which shows row-level records of successfully connected outbound calls including campaign, duration, agent, team, and wrap-up reason."

product-area: [reporting, voice, dialer]
doc-type: reference
difficulty: beginner
keywords: ["connected calls detail report", "outbound call report", "connected calls", "campaign report", "call duration", "wrap-up", "historical report", "dialer report"]
aliases: ["connected calls report", "outbound call detail", "campaign connected calls"]
last-updated: 2026-03-10
---

# Connected Calls Detail Report

The **Connected Calls Detail Report** shows a row-level record for each outbound call that was successfully connected — that is, calls where the customer answered. Abandoned and unconnected calls are not included.

## Report Summary

| Attribute | Detail |
|---|---|
| **Report type** | Historical |
| **Primary audience** | Supervisor, Campaign Manager |
| **Key use case** | Audit connected outbound calls; verify agent handling and wrap-up accuracy per campaign |

## Report Columns

| Field | Description |
|---|---|
| **Campaign** | Name of the outbound campaign the call belongs to. |
| **DateTime** | Date and time of the call record. |
| **Number Called** | The customer's phone number that was dialled. |
| **Call Duration** | Total duration of the connected call, in seconds. |
| **Agent ID** | Unique identifier of the agent who handled the call. |
| **Agent Name** | Display name of the agent who handled the call. |
| **Agent Team** | Name of the team to which the agent belongs. |
| **Wrap-up** | The wrap-up code selected by the agent at the conclusion of the call. |

## Report Filters

| Filter | Description |
|---|---|
| **DateTime** | Filter by date and time range. |
| **Campaign Name** | Filter by one or more campaign names. |
| **Team(s)** | Filter by one or more agent teams. |
| **Agent(s)** | Filter by one or more specific agents. |

## How to Read This Report

Use **Campaign** grouping to assess outbound campaign performance at the call level. The absence of a record for a contact in this report means the call was not connected — cross-reference with the [Outbound Summary Report](../Reporting_and_Analytics/Outbound-Summary-Report.md) to see how those unconnected calls are classified.

**Call Duration** combined with **Agent Name** reveals whether certain agents have significantly shorter or longer conversations — which may reflect coaching opportunities or differences in contact quality within the same campaign.

**Wrap-up** values that are blank or appear inconsistent can indicate agents closing calls without completing the wrap-up form, or a configuration issue in wrap-up form assignment. See [Configuring Wrap-up Forms](../../How-to_Guides/Administrator/Configuring-Wrap-up-Forms.md).

## Related Articles

- [Outbound Summary Report](../Reporting_and_Analytics/Outbound-Summary-Report.md)
- [Outbound Calls](Outbound-Calls.md)
- [CX Dialer Reference](CX-Dialer-Reference.md)
- [Campaign Performance Reports](../../How-to_Guides/Supervisor_and_QA_Lead/Campaign-Performance-Reports.md)
- [Managing Outbound Campaigns](../../How-to_Guides/Administrator/Managing-Outbound-Campaigns.md)
