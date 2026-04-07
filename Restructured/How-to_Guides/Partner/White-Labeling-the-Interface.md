---
title: "White-Labeling the Interface"
summary: "How Resellers apply custom branding — logos, color schemes, and domain names — to ExpertFlow CX for their customers."
audience: [hosting-partner]
product-area: [platform, multi-tenancy]
doc-type: how-to
difficulty: intermediate
last-updated: 2026-03-14
---

# White-Labeling the Interface

ExpertFlow CX supports per-tenant branding customization. As a Reseller, you can present the platform under your own brand or your customer's brand, covering the logo, color scheme, and the customer-facing domain name.

> White-labeling is configured per tenant. Each tenant can have its own independent branding.

---

## What Can Be Customized

| Element | Scope | Where Configured |
|---------|-------|-----------------|
| **Logo** | Agent Desk, Unified Admin header, login page | Unified Admin > General Settings > Branding |
| **Favicon** | Browser tab icon | Unified Admin > General Settings > Branding |
| **Primary color** | Button accents, active state highlights | Unified Admin > General Settings > Branding |
| **Platform name** | Page title and browser tab label | Unified Admin > General Settings > Branding |
| **Custom domain (FQDN)** | The URL agents and admins use to access the platform | DNS + Tenant registration |
| **Tenant logo (registration)** | Uploaded as part of the CX 5.0.1+ tenant API payload | CX Tenant API |

---

## Step 1 — Configure a Custom Domain (FQDN)

The FQDN is set at tenant creation and cannot be changed after provisioning without re-creating the tenant.

- **Standard subdomain:** `customername.cx.expertflow.com` (ExpertFlow managed domain)
- **Customer-owned domain:** `cx.customername.com` (requires customer's DNS team to create a CNAME record pointing to the ExpertFlow ingress controller)

Provide the desired FQDN in the `tenantId.root-domain` format when registering the tenant via the CX Tenant API. See [Onboarding a New Tenant](../../How-to_Guides/Partner/Onboarding-a-New-Tenant.md) for the registration payload.

---

## Step 2 — Upload the Tenant Logo (CX 5.0.1+)

From CX version 5.0.1 onward, a tenant logo must be uploaded as part of the tenant registration API call. It cannot be skipped.

- **Supported formats:** PNG, SVG
- **Recommended size:** 200 × 60 px (horizontal layout)
- Include the logo file in the Postman collection request or the `create_tenant.sh` script payload.

> If you are on CX 5.0.0 or earlier, logo upload is done post-registration via the Branding settings in Unified Admin.

---

## Step 3 — Apply Branding in Unified Admin

Once the tenant is live:

1. Log in to **Unified Admin** for the target tenant.
2. Navigate to **General Settings > Branding**.
3. Configure the following:

**Logo & Favicon**
- Upload the customer's logo (PNG/SVG, max 2 MB).
- Upload the favicon (ICO or 32×32 PNG).

**Platform Name**
- Set the name that appears in the browser tab and login page header (e.g., `Acme Contact Center`).

**Primary Color**
- Enter a hex color code for the UI accent color (e.g., `#0057B7`).
- The preview panel updates in real time.

4. Click **Save**. Changes take effect immediately — no page reload required for users already logged in.

---

## Branding Checklist

Before handing off to the customer, verify:

- [ ] Logo renders correctly on both the login page and the Agent Desk header
- [ ] Favicon is visible in the browser tab
- [ ] Primary color matches the customer's brand guidelines
- [ ] Platform name reflects the agreed branding (not "ExpertFlow CX")
- [ ] FQDN is accessible and SSL certificate is valid (green padlock)
- [ ] Login page shows no ExpertFlow branding if full white-label was requested

---

## SSL Certificates

If the customer is using their own domain (e.g., `cx.customername.com`), an SSL certificate must be in place:

- **ExpertFlow-managed subdomain** (`*.cx.expertflow.com`): SSL is managed by ExpertFlow. No action required.
- **Customer-owned domain:** The customer's IT team must provide an SSL certificate for the subdomain. Coordinate with ExpertFlow Partner Support to install it on the ingress controller.

---

## Limitations

- **Email notifications** sent by the platform (e.g., password reset) use ExpertFlow's email infrastructure by default. Custom email sender domains require a separate configuration request to ExpertFlow Partner Support.
- **Mobile apps** (if applicable) require a separate build for full white-label branding and are subject to the customer's app store agreements.

---

## Related Guides

- [Reseller Quickstart](Reseller-Quickstart.md)
- [Onboarding a New Tenant](../../How-to_Guides/Partner/Onboarding-a-New-Tenant.md)
- [Tenant Lifecycle Management](Tenant-Lifecycle-Management.md)
