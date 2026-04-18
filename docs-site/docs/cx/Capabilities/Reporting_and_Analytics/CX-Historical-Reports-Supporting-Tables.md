---
title: "CX Historical Reports — Supporting Tables"
summary: "Reference for the three database tables that underpin ExpertFlow CX historical reports: report_configs, reports_offset, and weekdays."

product-area: [reporting]
doc-type: reference
difficulty: advanced
keywords: ["historical reports", "reporting database", "report_configs", "reports_offset", "weekdays", "ETL", "Superset", "database tables"]
aliases: ["reporting database tables", "historical reports schema", "reporting DB reference"]
last-updated: 2026-03-10
---

# CX Historical Reports — Supporting Tables

ExpertFlow CX historical reports rely on three supporting database tables that store configuration, timezone offsets, and calendar data. This reference describes each table's purpose, structure, and usage rules.

## Tables Overview

| Table | Purpose |
|---|---|
| `report_configs` | Stores universal configuration key-value pairs used across reports |
| `reports_offset` | Stores the UTC offset applied to all timestamps in historical reports |
| `weekdays` | Stores week number, year, and week start/end dates for weekly report grouping |

---

## `report_configs`

This table acts as a universal configuration store for report-level settings. It has two columns:

| Column | Type | Description |
|---|---|---|
| `config_key` | string | The name of the configuration setting |
| `config_value` | string | The value for that setting |

**Current usage:** Two configurations are active. Values are updated automatically by the ETL job (`configs` step).

**Extending the table:** If a future report requires an additional configuration parameter, add a new row with the relevant key and value. Reports automatically use the latest value for each key.

> Do not modify `config_key` names that existing reports depend on — this will break report queries.

---

## `reports_offset`

This table stores the UTC offset that is added to (or subtracted from) all timestamps when generating historical report data. Because all interaction timestamps are recorded in UTC+0, the offset converts them to your contact center's local time for display in Superset.

| Column | Type | Description |
|---|---|---|
| `offset_in_minutes` | integer | The UTC offset expressed in minutes. Positive = ahead of UTC; negative = behind UTC. |

**Example values:**

| Timezone | `offset_in_minutes` |
|---|---|
| UTC+0 (London, no offset) | `0` |
| UTC+2 (South Africa) | `120` |
| UTC+5:30 (India) | `330` |
| UTC-5 (Eastern US) | `-300` |

> **Critical:** This table must contain exactly **one row**. Multiple rows produce undefined behavior in reports. If you need to change the offset, run `UPDATE reports_offset SET offset_in_minutes = [value]` — do not insert a new row.

For configuration steps, see [Configure UTC Offset for Reports](UTC-Offset-Reports.md).

---

## `weekdays`

This table provides the mapping between week numbers and calendar dates. Multiple historical reports — including the Queue-wise Stats Summary Report and Historical Conversation Summary Report — use this table to group data by week.

| Column | Description |
|---|---|
| `week_number` | ISO week number within the year |
| `year` | Calendar year |
| `week_start_date` | The date on which the week begins |
| `week_end_date` | The date on which the week ends |

**Data generation:** A stored procedure populates this table. When running the procedure, pass the correct **week start day** for your country. This varies by locale:

| Region | Week starts on |
|---|---|
| Most of Europe, South Africa | Monday |
| United States, Canada | Sunday |
| Middle East | Saturday or Sunday (varies by country) |

> Passing the wrong week start day causes weekly report groupings to misalign with your business calendar. Verify the correct day before running the stored procedure.

## Related Articles

- [Configure UTC Offset for Reports](UTC-Offset-Reports.md)
- [Historical Reports Reference](../../How-to_Guides/Supervisor_and_QA_Lead/Historical-Reports-Reference.md)
- [Superset Reports Configuration](../../How-to_Guides/Administrator/Superset-Reports-Configuration.md)
- [Key Reporting Metrics](Key-Reporting-Metrics.md)
