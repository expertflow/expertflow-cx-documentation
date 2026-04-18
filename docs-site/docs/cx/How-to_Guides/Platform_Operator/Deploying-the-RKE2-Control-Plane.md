---
title: "Deploying the RKE2 Control Plane"
summary: "Technical guide for Multi-tenant Partners to prepare the environment and install the RKE2 Kubernetes control plane."
audience: [platform-operator]
product-area: [infrastructure, kubernetes]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Deploying the RKE2 Control Plane

This guide covers the prerequisites and step-by-step commands to install RKE2 on the control plane of ExpertFlow CX. RKE2 is the foundational Kubernetes distribution required for high-availability multi-tenant deployments.

## 1. Pre-Deployment Checklist
- **OS Support:** Ensure nodes are running a supported OS (Ubuntu or RHEL).
- **Network:** FQDN must be mapped to node IP; all nodes must synchronize time via NTP.
- **Firewall:** We recommend disabling `firewalld` or `ufw` initially to ensure smooth cluster bootstrapping.
- **SSL:** Ensure directories for extended certificate expiration are ready.

## 2. Environment Preparation
### For Ubuntu Nodes:
```bash
systemctl disable firewalld --now
systemctl disable apparmor.service
systemctl disable ufw --now
reboot
```

### Enable Kernel Tuning:
Run this on all nodes to optimize performance for high-load interaction engine traffic:
```bash
cat << EOF > /etc/sysctl.d/99-expertflow.conf
vm.max_map_count = 262144
net.ipv4.ip_local_port_range = 1024 65000
net.core.somaxconn = 10000
net.ipv4.tcp_tw_reuse = 1
EOF
sysctl --system
```

## 3. Installation Steps
1.  **Create Manifests:** Prepare the directories for RKE2 bootstrapping.
    ```bash
    mkdir -p /etc/rancher/rke2/
    mkdir -p /var/lib/rancher/rke2/server/manifests/
    ```
2.  **Bootstrap Ingress:** Generate the `rke2-ingress-nginx-config.yaml` to allow customized ingress routing for multi-tenant subdomains.
3.  **Launch Server:** Install the RKE2 server and start the service.
    ```bash
    curl -sfL https://get.rke2.io | sh -
    systemctl enable rke2-server.service
    systemctl start rke2-server.service
    ```

---

*Once the cluster is active, proceed to [Helm-Based Application Deployment](Helm-Based-Application-Deployment.md).*
