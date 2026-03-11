---
title: "IVR Detail Report"
summary: "Reference guide for the IVR Detail Report in ExpertFlow CX — covering all report columns (Call ID, Conversation ID, ANI, language, menu/sub-menu selections, journey path, disposition, duration) and available filters."
audience: [designer, supervisor]
product-area: [voice]
doc-type: reference
difficulty: beginner
keywords: ["IVR detail report CX", "IVR journey report CX", "IVR call report CX", "IVR disposition CX", "ExpertFlow IVR report"]
aliases: ["IVR detail CX", "call IVR report CX"]
last-updated: 2026-03-10
---

# IVR Detail Report

The IVR Detail Report shows the complete IVR journey for each individual call — including the menu path the customer navigated, the outcome (disposition), and the time spent in the IVR.

---

## Report Columns

| Field | Description |
|---|---|
| **Start Date & Time** | Date and time the IVR session started |
| **Call ID** | Unique identifier of the call |
| **Conversation ID** | Unique identifier of the customer conversation |
| **ANI** | Calling number of the customer |
| **Language** | Language selected by the customer in the IVR |
| **End Date & Time** | Date and time the IVR session ended |
| **Menu** | Main menu option selected by the customer |
| **Sub Menu** | Sub-menu option selected by the customer |
| **Journey** | Complete sequence of menu selections made by the customer (e.g., Main Menu → Sub-Menu → Sales) |
| **Disposition** | Final outcome of the IVR session (e.g., `DIALOG_ENDED`, `TRANSFER`) |
| **Duration (S)** | Total IVR session duration in seconds |

---

## Report Filters

| Filter | Description |
|---|---|
| **Date** | Filter by the date of the IVR session |
| **Conversation ID** | Filter to a specific conversation |
| **Call ID** | Filter to a specific call |
| **Disposition** | Filter by IVR outcome (e.g., show only `TRANSFER` records) |

---

## Related Articles

- [IVR Summary Report](IVR-Summary-Report.md)
- [Historical Reports Reference](../Supervisor/Historical-Reports-Reference.md)
