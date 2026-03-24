---
title: "RKE2 Uninstallation"
summary: "How-to guide for completely uninstalling RKE2 from control plane and worker nodes — including the uninstall script, data cleanup, and system reboot."
audience: [hosting-partner, platform-operator]
product-area: [platform]
doc-type: how-to
difficulty: intermediate
keywords: ["RKE2 uninstall CX", "remove RKE2 CX", "uninstall Kubernetes CX", "RKE2 cleanup CX", "rke2-uninstall.sh"]
aliases: ["remove RKE2 CX", "RKE2 teardown CX", "uninstall K8s CX"]
last-updated: 2026-03-10
---

# RKE2 Uninstallation

This guide removes RKE2 and all associated data from a node. Run these steps on **every control plane and worker node** individually.

> **Warning**: This procedure is destructive and irreversible. All cluster data, volumes, and configuration stored on the node will be permanently deleted.

---

## Step 1: Run the Uninstall Script

```bash
cd /usr/bin/
rke2-uninstall.sh
```

This stops all RKE2 services and removes RKE2 binaries.

---

## Step 2: Remove Residual Data

```bash
rm -rf /var/lib/rancher /etc/rancher /var/lib/longhorn/ /etc/cni /opt/cni /var/openebs/
```

This cleans up all cluster data, CNI configuration, and storage volumes (including Longhorn and OpenEBS data).

---

## Step 3: Reboot

```bash
reboot
```

Reboot the node to clear any remaining kernel-level network state.

---

## Related Articles

- [Kubernetes Distributions](Kubernetes-Distributions.md)
- [Deploying the RKE2 Control Plane](../../Getting_Started/For_Hosting_Partners/Deploying-the-RKE2-Control-Plane.md)
- [CX Solution Helm Uninstallation](Helm-Based-Application-Deployment.md)
