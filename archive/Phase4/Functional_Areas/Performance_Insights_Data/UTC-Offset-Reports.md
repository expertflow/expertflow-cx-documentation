---
title: "Configure UTC Offset for Reports"
summary: "Set the timezone offset in the reporting database so that historical report timestamps display in your local time instead of UTC."
audience: [admin]
product-area: [reporting]
doc-type: how-to
difficulty: intermediate
keywords: ["UTC offset", "timezone", "reports", "Superset", "reports_offset", "local time", "historical reports", "SQL"]
aliases: ["timezone offset", "report timezone configuration", "UTC to local time"]
last-updated: 2026-03-10
---

# Configure UTC Offset for Reports

ExpertFlow CX stores all interaction timestamps in the reporting database as **UTC+0**. If your contact center operates in a different timezone, you must configure a UTC offset so that historical reports in Superset display timestamps in your local time.

## Prerequisites

- Database administrator access to the reporting database
- Your contact center's UTC offset value (e.g., UTC+2, UTC-5:30)

## Steps

### 1. Find Your UTC Offset

Search for your city or country's current UTC offset.

1. Open a browser and search: `UTC offset for [your city or country]`
2. Note the offset value including its sign — for example, `UTC+2` or `UTC-1.5`.

### 2. Convert the Offset to Minutes

The `reports_offset` table stores the offset as an integer number of minutes.

**Formula:** `offset_hours × 60 = offset_in_minutes`

| Example | Calculation | Value to store |
|---|---|---|
| UTC+2 (South Africa) | 2 × 60 | `120` |
| UTC+5:30 (India) | 5.5 × 60 | `330` |
| UTC-1:30 | -1.5 × 60 | `-90` |

> **Important:** Preserve the sign. Positive offsets add time to UTC; negative offsets subtract.

### 3. Update the Offset in the Reporting Database

Run the following SQL query against the reporting database, replacing `-120` with your calculated offset in minutes:

```sql
UPDATE reports_offset SET offset_in_minutes = 120;
```

**Example for UTC-2:**

```sql
UPDATE reports_offset SET offset_in_minutes = -120;
```

### 4. Verify the Update

Confirm that the table contains exactly one record with your new offset:

```sql
SELECT * FROM reports_offset;
```

The result should show a single row with your `offset_in_minutes` value.

> **Warning:** The `reports_offset` table must contain only **one record**. Do not insert additional rows — multiple rows will cause unpredictable report behavior.

### 5. Refresh Superset Reports

After updating the offset, open Superset and refresh your historical reports. All timestamps now display in local time based on your configured offset.

## Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| Reports still show UTC time | Cache not cleared | Refresh the Superset dashboard or clear browser cache |
| Timestamps shifted by wrong amount | Incorrect sign or calculation | Re-check your offset and rerun the `UPDATE` query |
| Multiple rows in `reports_offset` | Extra records inserted | Delete all rows and insert a single correct record |

## Related Articles

- [CX Historical Reports Supporting Tables](CX-Historical-Reports-Supporting-Tables.md)
- [Historical Reports Reference](../../Supervisor/Historical-Reports-Reference.md)
- [Superset Reports Configuration](../../Solution_Admin/Superset-Reports-Configuration.md)
- [Languages and Timezones Settings](../../Solution_Admin/Languages-Timezones-Settings.md)
