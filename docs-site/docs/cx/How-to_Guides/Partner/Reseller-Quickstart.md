---
title: "Reseller Quickstart: From Contract to Tenant Live"
summary: "End-to-end sequence for Resellers to move a new customer from contract signed to a fully operational ExpertFlow CX tenant."
audience: [hosting-partner]
product-area: [multi-tenancy, licensing, platform]
doc-type: how-to
difficulty: beginner
last-updated: 2026-03-14
---

# Reseller Quickstart: From Contract to Tenant Live

This guide gives you the complete sequence to onboard a new customer. Each step links to the dedicated guide for full detail.

> **Your role as a Reseller:** ExpertFlow manages all infrastructure. Your responsibility is tenant provisioning, license assignment, and handing off a configured environment to your customer.

---

## The Onboarding Sequence

### Step 1 — Confirm the Subscription

Before provisioning anything, verify the customer's subscription details in the **Master Partner Portal**:

- Subscription tier and concurrent agent count
- Licensed products (e.g., Voice, Outbound Dialer, Conversation Search, WFM)
- Contract start and expiry dates

> See [Subscription Tiers & Capacity Planning](Subscription-Tiers-and-Capacity-Planning.md) for a full breakdown of what each tier includes.

---

### Step 2 — Create the Tenant

Register the new tenant using the **CX Tenant API** (Postman or the `create_tenant.sh` script).

You will need:
- A unique `tenantId` and display name
- The customer's FQDN (e.g., `customername.cx.expertflow.com`)
- Keycloak configuration, Redis & MongoDB credentials

On success, the platform automatically provisions the Keycloak realm, Media Server domain, and storage bucket.

> See [Onboarding a New Tenant](Onboarding-a-New-Tenant.md) for the full API payload and script instructions.

---

### Step 3 — Upload the License Key

1. Log in to the tenant's **Unified Admin** console.
2. Navigate to **General Settings > License Info**.
3. Upload the customer's **Master API Key**.
4. Verify that the concurrent user count, licensed products, and expiry date match the contract.

> See [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md) for cross-tenant license management from the Master Partner Portal.

---

### Step 4 — Configure the Tenant

With the tenant live and licensed, complete the initial configuration:

| Area | What to configure |
|------|-------------------|
| **Identity** | Create agent and supervisor accounts in IAM (Keycloak) |
| **Teams** | Define teams and assign supervisors in Unified Admin |
| **Routing** | Enable MRDs (Voice, Chat, SMS) and create Precision Queues |
| **Channels** | Connect Web Widget, WhatsApp, Voice extensions |
| **Localization** | Set timezone and supported languages |

> The [Getting Started: Onboarding a New Tenant](Onboarding-a-New-Tenant.md) guide covers each of these areas in sequence.

---

### Step 5 — Apply Branding (Optional)

If the customer requires white-labeled branding, configure logos, colors, and the custom domain before handing off.

> See [White-Labeling the Interface](White-Labeling-the-Interface.md).

---

### Step 6 — Hand Off to the Customer

Once the tenant is live and verified:

1. Provide the customer's administrator with their FQDN and initial Unified Admin credentials.
2. Share the [Getting Started](../../Getting_Started/index.md) documentation set.
3. Confirm the customer's Solution Admin has the `unified-admin` role in Keycloak.

---

## Post-Launch: Ongoing Responsibilities

| Task | When | Guide |
|------|------|-------|
| Monitor license consumption across tenants | Monthly / on-demand | [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md) |
| Renew or upgrade a subscription | 30+ days before expiry | [License Renewal & Reactivation](License-Renewal-and-Reactivation.md) |
| Add a new tenant | On new contract | This guide |
| Suspend or offboard a tenant | On contract end | [Tenant Lifecycle Management](Tenant-Lifecycle-Management.md) |

---

## Related Guides

- [Tenant Lifecycle Management](Tenant-Lifecycle-Management.md)
- [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md)
- [Subscription Tiers & Capacity Planning](Subscription-Tiers-and-Capacity-Planning.md)
- [License Renewal & Reactivation](License-Renewal-and-Reactivation.md)
- [White-Labeling the Interface](White-Labeling-the-Interface.md)
