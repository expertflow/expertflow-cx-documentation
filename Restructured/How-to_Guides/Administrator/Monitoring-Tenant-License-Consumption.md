---
title: "Monitoring Tenant License Consumption"
summary: "Reference guide for Solution Admins to track concurrent agent usage, product activation status, and license expiry within a single tenant."
audience: [administrator]
product-area: [licensing, platform]
doc-type: reference
difficulty: beginner
last-updated: 2026-03-11
---

# Monitoring Tenant License Consumption

As a Solution Admin (Olivia), you can monitor the real-time consumption of concurrent agent licenses for your specific tenant. This ensuring your team remains within its purchased capacity and avoids service degradation during peak hours.

## 1. Accessing the License Dashboard
1.  Log in to the **Unified Admin** console.
2.  Navigate to **General Settings > License Info.**
3.  The table will display all products currently active for your instance.

> **Note for Partners:** Reseller-level license management across multiple tenants is currently performed via the **Master Partner Portal**. Documentation for the partner-level view is currently under development.

---

## 2. License Monitoring Metrics

| Metric | Definition | Admin Action Required |
| :--- | :--- | :--- |
| **Purchased Licenses** | The total number of concurrent agent slots allocated to your tenant. | If this is too low, contact your Reseller to increase capacity. |
| **Consumed Licenses** | The current number of agents logged into the system across all Media Routing Domains. | Monitor this during peak hours to ensure you don't hit the ceiling. |
| **Expiry Date** | The date your current license key will deactivate. | Ensure renewal is processed at least 30 days before this date. |
| **Activation Status** | Shows if a product is `ACTIVE` or `SUSPENDED`. | If suspended, check your subscription status with your provider. |

---

## 3. Automated Warnings
The system provides visual indicators within the Unified Admin UI to prevent accidental downtime:

*   **Utilization Alerts:** A yellow banner appears when consumption reaching 90% of your purchased limit.
*   **Expiry Countdown:** The dashboard displays a "Days Remaining" counter starting 30 days before the expiry date.

---

## 4. Troubleshooting Product Availability
If a newly purchased product (e.g., *Conversation Search* or *Outbound Dialer*) does not appear in your list:
1.  Verify that at least one agent has successfully logged into that specific product once.
2.  Refresh the **License Info** page manually to sync with the License Engine.
3.  If the issue persists, verify the **Master License Key** in your platform configuration.

---

## Related Guides
*   [Unified Admin Core Configuration](../../Getting_Started/For_Administrators/Unified-Admin-Guide.md)
*   [Agent Performance Dashboard](../Supervisor_and_QA_Lead/Agent-Performance-Dashboard-Reference.md)
