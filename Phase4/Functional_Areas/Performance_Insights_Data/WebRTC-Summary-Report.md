---
title: "WebRTC Summary Report"
summary: "Reference for the WebRTC Summary Report, which shows daily totals for generated, successful, and failed WebRTC links."
audience: [supervisor, admin]
product-area: [reporting]
doc-type: reference
difficulty: beginner
keywords: ["WebRTC summary report", "WebRTC", "web calling", "browser-based calling", "link success rate", "historical report"]
aliases: ["WebRTC link summary", "web call summary report"]
last-updated: 2026-03-10
---

# WebRTC Summary Report

The **WebRTC Summary Report** provides a daily aggregate view of WebRTC link performance — showing how many links were generated, how many connected successfully, and how many failed. Use it to track overall WebRTC channel health over time and spot degradation trends.

## Report Summary

| Attribute | Detail |
|---|---|
| **Report type** | Historical |
| **Primary audience** | Solution Admin, Supervisor |
| **Key use case** | Monitor WebRTC channel success rate; identify days with elevated failure rates |

## Report Columns

| Field | Description |
|---|---|
| **Date** | The date for which the totals are reported. |
| **Total Generated Links** | Total number of WebRTC links generated on that date. |
| **Total Successful** | Number of links that resulted in a successfully connected call. |
| **Total Failure** | Number of links that did not connect successfully. |

## Report Filters

| Filter | Description |
|---|---|
| **Date** | Filter by a specific date or date range. |

## How to Read This Report

**Total Successful ÷ Total Generated Links** gives your daily WebRTC connection rate. A healthy connection rate depends on your use case and customer base, but a sustained rate below 70% warrants investigation.

Compare **Total Failure** spikes against known events (platform releases, network changes, browser updates) to identify root causes. For row-level failure detail, drill into the [WebRTC Detail Report](WebRTC-Detail-Report.md).

## Related Articles

- [WebRTC Detail Report](WebRTC-Detail-Report.md)
- [Web App Calls Overview](../../Solution_Admin/Web-App-Calls-Overview.md)
- [Historical Reports Reference](../../Supervisor/Historical-Reports-Reference.md)
- [Key Reporting Metrics](Key-Reporting-Metrics.md)
