---
title: "Kubernetes Distributions"
summary: "Reference guide for Kubernetes distributions supported by ExpertFlow CX — covering RKE2 (recommended), K8s/kubeadm, Tanzu Kubernetes Grid, K3s, and MicroK8s, with guidance on when to use each."
audience: [hosting-partner]
product-area: [platform]
doc-type: explanation
difficulty: beginner
keywords: ["Kubernetes distribution CX", "RKE2 CX", "K3s CX", "Tanzu Kubernetes CX", "supported Kubernetes CX", "MicroK8s CX", "Kubernetes for ExpertFlow"]
aliases: ["CX Kubernetes distributions", "supported K8s CX", "RKE2 ExpertFlow"]
last-updated: 2026-03-10
---

# Kubernetes Distributions

ExpertFlow CX requires a Kubernetes distribution for its core solution components. Any [CNCF-certified Kubernetes distribution](https://landscape.cncf.io) is supported. The ExpertFlow team uses and recommends **RKE2**.

> All ExpertFlow CX product releases are tested on RKE2 unless stated otherwise in release documentation.

---

## Supported Distributions

| Distribution | Recommendation | Use Case |
|---|---|---|
| **RKE2** | **Recommended** | On-premise production deployments. RKE2 (also known as RKE Government) is Rancher's next-generation CNCF-certified Kubernetes distribution. All CX releases are tested on RKE2 by default. |
| **K8s (kubeadm)** | Supported | On-premises, cloud, and hybrid deployments requiring a high-availability Kubernetes cluster. Maintained by Google. |
| **Tanzu Kubernetes Grid** | Supported (Enterprise) | Enterprise-class production deployments on VMware vSphere with vSAN storage. Provided by VMware with commercial support. |
| **K3s** | Supported (Non-production) | Lightweight, single-node, or testing deployments. Packaged as a single binary under 70 MB, with minimal dependencies and simplified installation. Not recommended for production HA deployments. |
| **MicroK8s** | Supported | Low-ops, minimal-footprint production deployments. Lightweight distribution from Canonical. |

---

## Getting Started

To set up RKE2 for an ExpertFlow CX deployment, see [RKE2 Control Plane Deployment](Deploying-the-RKE2-Control-Plane.md).

To learn more about Kubernetes concepts, see the [Kubernetes overview](https://kubernetes.io/docs/concepts/overview/).

---

## Related Articles

- [Deploying the RKE2 Control Plane](Deploying-the-RKE2-Control-Plane.md)
- [RKE2 Uninstallation](RKE2-Uninstallation.md)
- [Helm-Based Application Deployment](Helm-Based-Application-Deployment.md)
