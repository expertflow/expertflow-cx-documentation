---
title: "License Renewal & Reactivation"
summary: "How Resellers renew expiring customer licenses, reactivate suspended tenants, and handle the impact of a license lapse on service continuity."
audience: [reseller]
product-area: [licensing, platform]
doc-type: how-to
difficulty: beginner
last-updated: 2026-03-14
---

# License Renewal & Reactivation

License expiry is one of the most common causes of unplanned service disruption for your customers. This guide covers the renewal process, what happens when a license lapses, and how to restore service quickly.

---

## Renewal Timeline

| Days Before Expiry | Platform Behaviour | Recommended Action |
|--------------------|-------------------|-------------------|
| 30 days | Orange warning banner in Unified Admin. Email alert to Reseller contact. | Initiate renewal request with ExpertFlow. |
| 7 days | Red warning banner. Second email alert to Reseller contact. | Confirm new license key is ready to upload. |
| 0 (Expiry date) | Tenant is automatically **suspended**. Agents cannot log in. | Upload new key immediately to restore service. |
| Post-expiry | All active channel sessions are terminated. Data is retained. | Follow reactivation steps below. |

> You can configure the warning threshold (30–180 days) per tenant in **Unified Admin > General Settings**. The default is 30 days.

---

## Renewing Before Expiry (Recommended)

Renewing before the expiry date ensures zero service disruption.

1. **Initiate the renewal** — Submit a renewal request via the **EF Partner Portal** or contact your ExpertFlow account manager at least 30 days before expiry.
2. **Receive the new key** — ExpertFlow issues a new **Master License Key** with an updated expiry date.
3. **Upload the key** — In the tenant's **Unified Admin > General Settings > License Info**, upload the new key.
4. **Verify** — Confirm the new expiry date and product activations are correct on the License Info screen and in the [Master Partner Portal](Managing-Licenses-Across-Tenants.md).

> Uploading a new key before expiry extends the license without any gap in service. Agents do not need to log out or restart.

---

## Reactivating After Expiry (Service Restoration)

If a tenant has already been suspended due to expiry:

1. **Obtain the renewed license key** from ExpertFlow (follow the renewal request process above).
2. **Log in as a Reseller admin** — You retain access to the suspended tenant's Unified Admin console even when the tenant is suspended.
3. **Upload the new key** in **Unified Admin > General Settings > License Info**.
4. **Set the tenant status to Active** in the **Master Partner Portal**.
5. **Notify the customer** — Agents can now log back in. Active channel sessions do not automatically resume; customers must reopen interactions.

> Reactivation is typically immediate once the key is uploaded. If the tenant status does not update within 5 minutes, contact ExpertFlow Partner Support.

---

## What Happens to Data During Suspension

| Data Type | Retained? |
|-----------|-----------|
| Agent accounts and roles | Yes |
| Tenant configuration (queues, channels, routing) | Yes |
| Historical interaction records | Yes |
| Recordings and transcripts | Yes |
| Active (in-progress) interactions | No — terminated on suspension |
| Agent login sessions | No — terminated on suspension |

---

## Handling a Customer Who Does Not Renew

If a customer decides not to renew and wants to end service:

1. Allow the license to expire naturally (tenant auto-suspends), or manually suspend via the Master Partner Portal.
2. Advise the customer to export any data they need to retain before the decommission window.
3. After the customer confirms data export is complete, proceed with the offboarding process.

> See [Tenant Lifecycle Management — Offboarding](Tenant-Lifecycle-Management.md#offboarding-a-tenant-decommissioning) for the full decommission process. ExpertFlow retains suspended tenant data for 90 days before permanent deletion unless a decommission request is submitted earlier.

---

## Related Guides

- [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md)
- [Subscription Tiers & Capacity Planning](Subscription-Tiers-and-Capacity-Planning.md)
- [Tenant Lifecycle Management](Tenant-Lifecycle-Management.md)
