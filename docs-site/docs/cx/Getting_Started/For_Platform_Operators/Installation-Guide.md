---
title: "Installation Guide"
summary: "End-to-end guide for platform operators deploying ExpertFlow CX from scratch — from pre-installation validation through deployment and post-installation verification."
audience: [platform-operator]
doc-type: tutorial
last-updated: 2026-04-08
---

This document sequences a fresh ExpertFlow CX deployment — from validating your environment to a verified, production-ready platform.

For upgrading an existing deployment, see [Upgrade Guide](Upgrade-Guide.md).

---

## Stage 1 — Validate Prerequisites

Before any installation work begins, confirm your environment meets all requirements.

### Hardware sizing

Use the sizing tables to determine node specifications for your expected agent and call volume:

→ [Hardware Sizing Calculator](../../Reference/Architecture_and_Infrastructure/Hardware-Sizing-Calculator.md)

If you are deploying WFM as an add-on, also check:

→ [WFM Prerequisites](../../Reference/Architecture_and_Infrastructure/WFM-Prerequisites.md)

### Cluster and distribution

Review supported Kubernetes distributions and HA topology before provisioning nodes:

→ [Kubernetes Distributions](../../How-to_Guides/Platform_Operator/Kubernetes-Distributions.md)
→ [System Behaviour in Failover](../../How-to_Guides/Platform_Operator/System-Behaviour-in-Failover.md)

### Pre-installation checklist

Proceed only when all of the following pass:

- [ ] Node specs meet or exceed sizing table minimums, with 20–30% headroom for peak traffic
- [ ] Network connectivity verified between all nodes (ports open, low-latency links confirmed)
- [ ] Kubernetes, Helm, and kubectl versions confirmed compatible with the target release
- [ ] SSL certificates obtained or cert-manager strategy decided
- [ ] DNS entries for the platform FQDN prepared
- [ ] Maintenance window agreed and rollback plan documented

---

## Stage 2 — Install the Platform

Follow this sequence. Each step must complete successfully before the next.

1. **Provision the Kubernetes cluster**
   → [Deploying the RKE2 Control Plane](../../How-to_Guides/Platform_Operator/Deploying-the-RKE2-Control-Plane.md)

2. **Deploy ExpertFlow CX via Helm**
   → [Helm-Based Application Deployment](../../How-to_Guides/Platform_Operator/Helm-Based-Application-Deployment.md)

3. **Customise your deployment**
   → [Helm Deployment Customization](../../How-to_Guides/Platform_Operator/Helm-Deployment-Customization.md)

---

## Stage 3 — Deploy Optional Components

Deploy only the components required for your topology:

| Component | Guide |
| --- | --- |
| Voice infrastructure | [CX Voice Deployment](../../How-to_Guides/Platform_Operator/CX-Voice-Deployment.md) |
| SIP proxy | [CX SIP Proxy Deployment](../../How-to_Guides/Platform_Operator/CX-SIP-Proxy-Deployment-Guide.md) |
| Outbound dialer | [CX Dialer Deployment](../../How-to_Guides/Platform_Operator/CX-Dialer-Deployment-Guide.md) |
| LiveKit (WebRTC media) | [LiveKit Deployment](../../How-to_Guides/Platform_Operator/LiveKit-Deployment-Guide.md) |
| Workforce Management | [WFM Component Deployment](../../How-to_Guides/Platform_Operator/WFM-Component-Deployment.md) |
| CX Analyser | [CX Analyser Infrastructure Setup](../../How-to_Guides/Platform_Operator/CX-Analyser-Infrastructure-Setup.md) |
| MongoDB replica set | [MongoDB ReplicaSet Deployment](../../How-to_Guides/Platform_Operator/Deployment-of-Mongo-using-ReplicaSet.md) |

---

## Stage 4 — Post-Installation Verification

Before handing the platform to an administrator, confirm the deployment is healthy.

**Platform health**
- [ ] All pods running and ready — `kubectl get pods -A` shows no CrashLoopBackOff or Pending
- [ ] All Helm releases in `deployed` state — `helm list -A`
- [ ] Ingress resolves and TLS certificate is valid
- [ ] ExpertFlow CX UI loads and admin login succeeds

**Connectivity**
- [ ] Agent Desk accessible from a client browser
- [ ] API health endpoint responds
- [ ] If voice is deployed: SIP registration succeeds from a test device

**Monitoring baseline**

Set up your monitoring stack before go-live:

→ [Monitoring the Platform](../../How-to_Guides/Platform_Operator/Monitoring-the-Platform.md)

---

## What's next

With the platform verified, hand over to your administrator:

→ [Getting Started for Administrators](../For_Administrators/index.md)

When a new version is available:

→ [Upgrade Guide](Upgrade-Guide.md)
