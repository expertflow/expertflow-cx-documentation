---
title: "Tenant Lifecycle Management"
summary: "How Resellers create, suspend, reactivate, and offboard customer tenants in an ExpertFlow CX multi-tenant environment."
audience: [reseller]
product-area: [multi-tenancy, platform]
doc-type: how-to
difficulty: intermediate
last-updated: 2026-03-14
---

# Tenant Lifecycle Management

As a Reseller, you manage the full lifecycle of your customers' tenants — from initial creation through to offboarding. ExpertFlow manages the underlying infrastructure; your role is the logical provisioning and state management of each tenant.

---

## Tenant States

| State | Description | Who triggers it |
|-------|-------------|-----------------|
| **Active** | Tenant is live. Agents can log in and handle interactions. | Reseller (on creation or reactivation) |
| **Suspended** | Tenant is inaccessible. Agents cannot log in. Data is retained. | Reseller or platform (on license expiry) |
| **Decommissioned** | Tenant and all data are permanently removed. | Reseller (on offboarding request to ExpertFlow) |

---

## Creating a New Tenant

See the [Reseller Quickstart](Reseller-Quickstart.md) for the full provisioning sequence. In summary:

1. Register the tenant via the **CX Tenant API** (`tenantId`, FQDN, Keycloak config).
2. Upload the **Master License Key** in Unified Admin > General Settings > License Info.
3. Complete initial configuration (teams, queues, channels).

> Each tenant receives an isolated Keycloak realm, Media Server domain, and storage bucket on creation.

---

## Suspending a Tenant

Suspend a tenant when a customer's subscription lapses or is paused.

**What suspension does:**
- Blocks all agent logins for that tenant.
- Stops all active channel sessions (interactions in progress are terminated).
- Retains all configuration and historical data.

**To suspend a tenant:**
1. Log in to the **Master Partner Portal**.
2. Locate the tenant and set its status to **Suspended**.
3. Notify the customer's administrator — agents will see a login error immediately.

> **Note:** The platform may automatically suspend a tenant if its license key expires and is not renewed. See [License Renewal & Reactivation](License-Renewal-and-Reactivation.md).

---

## Reactivating a Suspended Tenant

1. Ensure the customer has a valid, renewed license key.
2. Upload the new license key in the tenant's **Unified Admin > General Settings > License Info**.
3. Set the tenant status back to **Active** in the Master Partner Portal.
4. Verify agents can log in and that channels are operational.

---

## Offboarding a Tenant (Decommissioning)

Decommissioning permanently deletes the tenant and all associated data. This action is **irreversible**.

**Pre-decommission checklist:**
- [ ] Confirm the customer has exported any reports, recordings, or interaction history they need to retain.
- [ ] Confirm no active integrations (CRMs, ticketing systems) are still pointing to this tenant's FQDN.
- [ ] Obtain written confirmation from the customer that data deletion is approved.

**Process:**
1. Suspend the tenant first (see above).
2. Submit a **Tenant Decommission Request** to ExpertFlow Partner Support, including the `tenantId` and written customer approval.
3. ExpertFlow will remove the Keycloak realm, Media Server domain, and all associated data stores.
4. Confirm the FQDN DNS record is removed by your IT team.

> ExpertFlow typically processes decommission requests within 5 business days.

---

## Managing Multiple Tenants

Use the **Master Partner Portal** to view all tenants across your reseller account:

- Filter by status (Active / Suspended)
- Review license expiry dates across all tenants
- Access individual tenant admin consoles

> For cross-tenant license monitoring, see [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md).

---

## Related Guides

- [Reseller Quickstart](Reseller-Quickstart.md)
- [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md)
- [License Renewal & Reactivation](License-Renewal-and-Reactivation.md)
