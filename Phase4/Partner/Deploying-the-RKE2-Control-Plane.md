---
title: "Deploying the RKE2 Control Plane"
summary: "Technical instructions for Multi-tenant Partners to install and configure the RKE2 Kubernetes control plane."
audience: [partner]
product-area: [platform, infrastructure]
doc-type: how-to
difficulty: advanced
last-updated: 2026-03-08
---

# Deploying the RKE2 Control Plane

This guide provides the step-by-step instructions for Multi-tenant Partners (Hosts) to install RKE2 on the control plane. This is the foundational step for any ExpertFlow CX deployment.

## 1. Pre-Deployment Checklist
Before starting, verify the following on your target nodes:
- **Internet Access:** Required for downloading binaries (or use the [Air-Gapped Guide](Air-Gap-Install-for-RKE-2-Kubernetes.html)).
- **Time Sync:** NTP must be active across all nodes.
- **FQDN:** Fully qualified domain names must map to node IPs.
- **Firewall:** It is recommended to disable the firewall or open [required RKE2 ports](https://docs.rke2.io/install/requirements#networking).

## 2. Environment Preparation

### Ubuntu Nodes:
```bash
systemctl disable firewalld --now
systemctl disable apparmor.service
systemctl disable ufw --now
reboot
```

### RHEL Nodes:
```bash
# Lock to supported RHEL 8.5
subscription-manager release --set=8.5; 
yum clean all;
systemctl disable firewalld --now
reboot
```

## 3. Kernel Tuning for Kubernetes
Run the following to optimize the host for high-volume CX workloads:
```bash
cat << EOF > /etc/sysctl.d/99-expertflow.conf
vm.swappiness=0
vm.overcommit_memory=1
net.core.somaxconn=10000
net.ipv4.ip_local_port_range=1024 65000
net.ipv4.tcp_tw_reuse=1
EOF

sysctl --system
```

## 4. RKE2 Server Installation

### Step 1: Create Configuration
```bash
mkdir -p /etc/rancher/rke2/
cat <<EOF | tee /etc/rancher/rke2/config.yaml
write-kubeconfig-mode: "0644"
etcd-expose-metrics: true
cni:
  - canal
EOF
```

### Step 2: Install and Start Service
```bash
curl -sfL https://get.rke2.io | INSTALL_RKE2_TYPE=server sh - 
systemctl enable rke2-server.service
systemctl start rke2-server.service
```
**Success Indicator:** Run `systemctl status rke2-server`. Do not proceed until the service is `active (running)`. This may take 10-15 minutes.

## 5. CLI Utility Setup
Add `kubectl` and `helm` to your path for easier management.

```bash
# Path Setup
echo "export PATH=\$PATH:/var/lib/rancher/rke2/bin" >> \$HOME/.bashrc
echo "export KUBECONFIG=/etc/rancher/rke2/rke2.yaml" >> \$HOME/.bashrc
source ~/.bashrc

# Bash Completion
apt install bash-completion -y
kubectl completion bash > /etc/bash_completion.d/kubectl
alias k=kubectl
complete -o default -F __start_kubectl k
```

---

*Next Step: Once the control plane is ready, proceed to [Setting Up CX Analyser Reports](../Infrastructure/Setting-Up-CX-Analyser-Reports.md).*
