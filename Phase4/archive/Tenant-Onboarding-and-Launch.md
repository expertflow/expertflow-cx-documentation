---
title: "Tenant Onboarding and Launch"
summary: "Lifecycle guide for Resellers to register a new tenant, configure external access, and prepare for customer launch."
audience: [reseller, admin]
product-area: [platform, licensing]
doc-type: how-to
difficulty: intermediate
last-updated: 2026-03-08
---

# Tenant Onboarding and Launch

As a Reseller, your goal is to move a new customer from "Contract Signed" to "Platform Live" as quickly as possible. This process involves registering the tenant, configuring their FQDN, and initializing their data stores.

## 1. Registering a New Tenant
Use the **CX Tenant API** to create the customer's logical environment.
- **Payload Requirements:**
    - `tenantId` & `tenantName`.
    - Keycloak configuration object.
    - Subdomain information (e.g., `customer1.cx.example.com`).
    - Campaign and Survey URLs.
- **Automation:** You can use Postman or the provided `create_tenant.sh` script in the post-deployment folder.

## 2. Infrastructure Initialization
Upon registration, the CX Tenant service automatically:
1.  Creates a dedicated **Keycloak Realm**.
2.  Initializes a **Media Server Domain**.
3.  Uploads default channel icons to the tenant's private storage bucket.

## 3. External Access Configuration
- **FQDN Registration:** Register the tenant's unique FQDN on the **Grafana allowedHosts** list to enable dashboard visualization.
- **DNS:** Ensure your IT team has created the CNAME record pointing the tenant subdomain to the master ingress controller.

## 4. Final Handoff
Once the bootstrap events are triggered, the tenant is **LIVE.**
- Proceed with [Standard CX Configuration](../Solution_Admin/Unified-Admin-Core-Configuration.md) (Teams, Queues, Channels).
- Upload the customer's [Master License Key](Monitoring-License-and-Renewals.md).

---

*To track the usage across your new tenant, see [Monitoring License and Renewals](Monitoring-License-and-Renewals.md).*
