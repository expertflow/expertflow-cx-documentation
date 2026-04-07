---
sidebar_position: 0
title: "Quick Start for Platform Operators"
summary: "Entry point for platform operators and hosting partners — covers infrastructure setup, first deployment, tenant onboarding, and day-to-day platform operations."
audience: [hosting-partner, platform-operator]
doc-type: tutorial
difficulty: intermediate
keywords: ["platform operator", "hosting partner", "deployment", "RKE2", "tenant onboarding", "operations", "quick start"]
aliases: ["hosting partner quick start", "platform operator guide", "deployment quick start"]
last-updated: 2026-03-27
---

# Quick Start for Platform Operators

You deploy, host, and operate ExpertFlow CX environments for one or more tenants. You own the infrastructure — from the Kubernetes cluster to ongoing platform health.

---

## Step 1 — Plan your infrastructure

Before deploying, establish your infrastructure baseline:

- Review [Kubernetes Distributions](../../How-to_Guides/Platform_Operator/Kubernetes-Distributions.md) to choose the right cluster type
- Use the [Hardware Sizing Calculator](../../Reference/Architecture_and_Infrastructure/Hardware-Sizing-Calculator.md) to size nodes for your expected tenant load
- Understand high-availability requirements: [System Behaviour in Failover](../../How-to_Guides/Platform_Operator/System-Behaviour-in-Failover.md)

---

## Step 2 — Deploy the platform

1. **Stand up the cluster** — [Deploying the RKE2 Control Plane](../../How-to_Guides/Platform_Operator/Deploying-the-RKE2-Control-Plane.md)
2. **Install ExpertFlow CX** — [Helm-Based Application Deployment](../../How-to_Guides/Platform_Operator/Helm-Based-Application-Deployment.md)
3. **Customise your deployment** — [Helm Deployment Customization](../../How-to_Guides/Platform_Operator/Helm-Deployment-Customization.md)

For voice infrastructure, also see [CX Voice Deployment](../../How-to_Guides/Platform_Operator/CX-Voice-Deployment.md) and [CX SIP Proxy Deployment Guide](../../How-to_Guides/Platform_Operator/CX-SIP-Proxy-Deployment-Guide.md).

---

## Step 3 — Onboard your first tenant

Once the platform is running, provision the first tenant:

- [Onboarding a New Tenant](../../How-to_Guides/Partner/Onboarding-a-New-Tenant.md)

Hand the tenant credentials to the Solution Admin — their path continues in [Getting Started for Administrators](../For_Administrators/).

---

## Step 4 — Operate the platform day-to-day

With tenants live, your ongoing responsibilities are:

| Task | Guide |
|---|---|
| Monitor platform health | [Monitoring the Platform](../../How-to_Guides/Platform_Operator/Monitoring-the-Platform.md) |
| Back up and restore data | [Backup and Restore](../../How-to_Guides/Platform_Operator/Backup-and-Restore.md) |
| Upgrade ExpertFlow CX | [Upgrading the Platform](../../How-to_Guides/Platform_Operator/Upgrading-the-Platform.md) |
| Review audit trails | [Audit Trail Implementation](../../How-to_Guides/Platform_Operator/Audit-Trail-Implementation-OpenSearch.md) |

→ Full reference: [How-to Guides — Hosting Partner](../../How-to_Guides/Platform_Operator/index.md)
