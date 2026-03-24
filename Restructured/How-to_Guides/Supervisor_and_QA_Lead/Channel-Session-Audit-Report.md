---
title: "Channel Session Audit Report"
summary: "Detailed reference for Supervisors to audit individual customer sessions across all digital and voice channels."
audience: [supervisor-qa]
product-area: [reporting, channels]
doc-type: reference
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Channel Session Audit Report

The **Channel Session Audit Report** provides a granular view of every individual session within a customer conversation. Use this report to troubleshoot connectivity issues, verify customer device data, and analyze session closure reasons.

## 1. Key Audit Columns
| Field | Description | Format |
| :--- | :--- | :--- |
| **Session ID** | The unique system identifier for this specific interaction leg. | UUID |
| **Channel Type** | The medium used (e.g., WhatsApp, Webchat, Facebook). | Text |
| **Session Data** | Metadata including Browser Type, Device (iOS/Android), and Language. | Text |
| **Start/End Time** | The exact timestamps of the session's activity. | YYYY-MM-DD HH:MM:SS |
| **Duration** | The total active time of the session. | HH:MM:SS |

## 2. Understanding Session Dispositions
The **Disposition** field tells you why and how a session ended.

- **AGENT:** Handled by a human and closed manually (typical for Pull-mode).
- **CUSTOMER:** The customer closed their browser or chat app.
- **INACTIVITY:** Closed automatically because the customer stopped responding (based on Admin timeout settings).
- **NETWORK:** Terminated due to a connection failure on the customer's side.
- **FORCE_CLOSED:** An agent closed their browser tab without ending the task properly.

## 3. Reporting Filters
- **Conversation ID:** Enter a specific ID to see all related sessions (e.g., if a customer moved from Webchat to WhatsApp).
- **Channel Name:** Filter by specific business lines (e.g., "Sales-Queue" vs "Support-Queue").
- **Date Range:** Audit sessions from a specific incident window.

---

*For high-level traffic trends, see the [Digital Channel Traffic Analysis](Digital-Channel-Traffic-Analysis.md).*
