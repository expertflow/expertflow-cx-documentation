---
title: "Onboarding a New Tenant"
summary: "A step-by-step guide for Resellers to register and activate a new tenant in a multi-tenant ExpertFlow CX deployment."
audience: [reseller]
product-area: [multi-tenancy, platform]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-13
---

# Onboarding a New Tenant

This guide walks you through registering a new tenant in an ExpertFlow CX multi-tenant environment and verifying it is ready for configuration.

## Prerequisites

Before you begin, confirm the following:

- You have a valid, available **FQDN** for the new tenant.
  - **Single-tenant / on-prem:** Any valid domain (e.g., `companyname.com`).
  - **Multi-tenant:** Must follow the `tenantId.root-domain` pattern (e.g., `tenant1.expertflow.com`).
- **DNS:** The tenant's subdomain DNS entry points to the multi-tenant ingress controller.
- **Subdomain routing** has been configured manually by the IT team.
- If CX Voice is required for this tenant, confirm it is enabled on the system.

---

## Step 1: Register the Tenant via the CX Tenant API

Use the CX Tenant API to create the tenant. The registration payload must include:

| Field | Description |
|-------|-------------|
| `tenantId` | Unique identifier for the tenant |
| `tenantName` | Display name |
| Keycloak config | Realm and auth settings |
| Subdomain info | The tenant's FQDN |
| Redis & MongoDB credentials | External access credentials |
| Campaign / Survey URLs | Update to match your tenant |

**Option A — Postman**

Use the [ExpertFlow Postman collection](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/request/21457238-193a442d-66f6-4f5c-867d-7d8b736eae32) to send the tenant creation request.

> **CX 5.0.1+:** Use the [updated Tenant API folder](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/folder/21457238-75863354-5ea2-432c-8747-a4ce44f472ee) — tenant logo upload is required as part of registration from this version onward.

**Option B — Shell Script**

If Postman is not available, use the bundled script in the post-deployment folder:

1. Edit the script and set your `tenantId` and `fqdn` values:

```bash
cd post-deployment
vi create_tenant.sh
```

2. Make the script executable and run it:

```bash
chmod +x create_tenant.sh
./create_tenant.sh
```

> **Default tenant:** For on-prem single-tenant deployments, use `tenantId: expertflow`.

**What happens on success:**

- CX Tenant service creates a Keycloak realm for the tenant.
- Media Server domain is provisioned.
- Channel icons are uploaded to Minio/blob storage.
- Bootstrap events are triggered to all registered webhooks.

---

## Step 2: Register the Tenant FQDN on Grafana allowedHosts

Follow the [Register new Tenant FQDN on Grafana allowedHosts](../../Partner/Register-new-Tenants-FQDN-on-Grafana-allowedHosts.md) guide to add the new subdomain to Grafana's allowed hosts list.

---

## Step 3: Verify the Tenant is Live

Once both steps are complete, confirm the tenant is active:

1. Navigate to the tenant's FQDN in a browser — the CX login page should load.
2. Log in with the initial admin credentials.
3. Confirm the Keycloak realm is accessible at `https://<fqdn>/auth/realms/<tenantId>`.

The tenant is now live and ready for standard CX configuration (queues, channels, agents, etc.).

---

*Next step: Hand off to the Solution Admin with the [Unified Admin Guide](../../Solution_Admin/Unified-Admin-Guide_2524407.md) to complete channel and routing configuration.*
