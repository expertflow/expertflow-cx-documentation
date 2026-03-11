---
title: "Monitoring License and Renewals"
summary: "Guide for Resellers and Admins to track concurrent user consumption, license expiry, and proactive renewal warnings."
audience: [reseller, admin]
product-area: [licensing, platform]
doc-type: how-to
difficulty: beginner
last-updated: 2026-03-08
---

# Monitoring License and Renewals

ExpertFlow CX provides a centralized dashboard for tracking product licenses and concurrent user consumption. This ensures that Resellers can manage customer subscriptions and avoid service interruptions.

## 1. Accessing License Information
1.  Log in to the **Unified Admin** console.
2.  Navigate to **General Settings > License Info.**
3.  The system displays all products linked to your **Master License Key.**

## 2. Key Monitoring Fields
| Field | Description |
| :--- | :--- |
| **Purchased Licenses** | The total capacity allocated to the tenant (e.g., 100 Concurrent Users). |
| **Consumed Licenses** | The number of licenses currently in use by active agents. |
| **Status** | Current state of the subscription (`ACTIVE`, `PENDING`, `SUSPENDED`). |
| **Expiry Date** | The date when the license will cease to function. |

## 3. Proactive Expiry Warnings
The system displays a warning banner when a license approaches its expiry date.
- **Threshold:** Configurable between 30 and 180 days (default is 30).
- **Banner Message:** *"Your license will expire soon. Please renew to avoid service interruption."*
- **Adjustment:** Solution Admins can change this threshold by updating the `LICENSE_EXPIRY_WARNING_DAYS` variable in the Unified Admin ConfigMap.

## 4. Operational Considerations
- **Activation:** New product licenses only appear on the dashboard **after** an agent logs into that specific product for the first time.
- **Manual Refresh:** Consumption data is not real-time; you must refresh the page to see the latest license status.
- **Renewal:** If a subscription is suspended, the customer must resubscribe via the EF Shop to reactivate the license.

---

*For technical hardware benchmarks associated with high-capacity licensing, see [Dialer Performance Benchmarks](../Decision_Maker/Dialer-Performance-Benchmarks.md).*
