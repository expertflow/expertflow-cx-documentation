---
title: "Managing Licenses Across Tenants"
summary: "Reference guide for Resellers to monitor and manage license consumption, capacity, and status across all customer tenants from the Master Partner Portal."
audience: [hosting-partner]
product-area: [licensing, platform]
doc-type: reference
difficulty: beginner
last-updated: 2026-03-14
---

# Managing Licenses Across Tenants

As a Reseller, you have visibility into license usage across all your customer tenants through the **Master Partner Portal**. This is distinct from the per-tenant view available to Solution Admins — you can see the full picture across your entire customer portfolio.

> **Solution Admins** can only see their own tenant's license data. See [Monitoring Tenant License Consumption](../Administrator/Monitoring-Tenant-License-Consumption.md) for that view.

---

## Accessing the Master Partner Portal

1. Log in to the **Master Partner Portal** using your Reseller credentials (provided by ExpertFlow on account activation).
2. The **License Overview** dashboard loads by default, showing all tenants under your account.

---

## License Overview Dashboard

The dashboard presents a row per tenant with the following fields:

| Column | Description |
|--------|-------------|
| **Tenant Name** | Display name and `tenantId` |
| **Subscription Tier** | The customer's current plan (e.g., Starter, Professional, Enterprise) |
| **Purchased Licenses** | Total concurrent agent slots allocated |
| **Consumed Licenses** | Agents currently logged in across all MRDs |
| **Utilization %** | Consumed ÷ Purchased, expressed as a percentage |
| **Licensed Products** | Which products are active (Voice, Outbound, WFM, etc.) |
| **Expiry Date** | Date the current license key expires |
| **Status** | `ACTIVE`, `SUSPENDED`, or `EXPIRING SOON` |

---

## Expiry Alerts

The portal flags tenants approaching expiry:

- **Orange** — Expiry within 30 days
- **Red** — Expiry within 7 days or already expired

ExpertFlow also sends automated email alerts to your registered Reseller contact at 30-day and 7-day thresholds.

> To manage a renewal, see [License Renewal & Reactivation](License-Renewal-and-Reactivation.md).

---

## Upgrading a Tenant's Capacity

If a customer needs more concurrent agent slots or additional licensed products:

1. Raise an upgrade request via the **EF Partner Portal** or contact your ExpertFlow account manager.
2. ExpertFlow generates a new **Master License Key** with the updated capacity.
3. Upload the new key in the tenant's **Unified Admin > General Settings > License Info**.
4. Verify the updated concurrent user count is reflected on the License Overview dashboard.

> Capacity upgrades take effect immediately upon key upload — no restart required.

---

## Viewing a Single Tenant's Detail

From the License Overview dashboard, click any tenant row to open its detail view:

- Full product activation list with per-product license counts
- Historical consumption chart (last 30 days)
- Audit log of license key uploads and status changes

---

## Common Scenarios

**A tenant hits 100% utilization:**
- Agents beyond the licensed count cannot log in.
- Raise a capacity upgrade request immediately or ask the customer to log out inactive agents.

**A tenant's status shows SUSPENDED unexpectedly:**
- Check the expiry date — automatic suspension occurs on the day of expiry.
- Follow the [License Renewal & Reactivation](License-Renewal-and-Reactivation.md) guide to restore service.

**A licensed product doesn't appear active for a tenant:**
- The product only registers as consumed after an agent logs into it for the first time.
- Ask the customer's admin to have one agent log in to that product to trigger activation.

---

## Related Guides

- [Subscription Tiers & Capacity Planning](Subscription-Tiers-and-Capacity-Planning.md)
- [License Renewal & Reactivation](License-Renewal-and-Reactivation.md)
- [Tenant Lifecycle Management](Tenant-Lifecycle-Management.md)
- [Monitoring Tenant License Consumption](../Administrator/Monitoring-Tenant-License-Consumption.md) *(Admin view)*
