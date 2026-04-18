---
title: "LinkedIn Connector Deployment using Helm"
summary: "How-to guide for deploying the ExpertFlow CX LinkedIn Connector using Helm — covering repository setup, values.yaml customization with FQDN, and Channels Helm chart deployment."
audience: [platform-operator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["LinkedIn connector Helm CX", "LinkedIn connector deployment CX", "LinkedIn Helm chart CX", "cx-channels Helm CX", "LinkedIn CX deployment"]
aliases: ["LinkedIn connector deploy CX", "Helm LinkedIn CX", "LinkedIn channel Helm CX"]
last-updated: 2026-03-10
---

# LinkedIn Connector Deployment using Helm

This guide deploys the ExpertFlow CX LinkedIn Connector using the Helm-based CX deployment.

## Prerequisites

- Kubernetes cluster with ExpertFlow CX deployed. See the CX Helm deployment guide.
- Persistent storage solution configured for the cluster.
- LinkedIn Standard Tier access for the Community Management API. See [LinkedIn Standard Tier Upgrade Guide](../Developer_Integrator/LinkedIn-Standard-Tier-Upgrade.md).

---

## Step 1: Add and Update the Helm Repository

```bash
helm repo add expertflow https://expertflow.github.io/charts
helm repo update expertflow
```

---

## Step 2: Clone the CX Solution Repository

```bash
git clone -b CX-4.9.5 \
  https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git CX-4.9.5

cd CX-4.9.5/kubernetes/
```

---

## Step 3: Configure the Channels Values File

Open the values file:

```bash
vi helm/Channels/values.yaml
```

Set your deployment FQDN:

```yaml
global:
  ingressRouter: <DEFAULT-FQDN>
```

Replace `<DEFAULT-FQDN>` with your actual deployment FQDN.

---

## Step 4: Deploy the Channels Helm Chart

```bash
helm upgrade --install \
  --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" \
  --debug \
  cx-channels \
  --values helm-values/cx-channels-custom-values.yaml \
  helm/Channels
```

---

## Related Articles

- [LinkedIn Standard Tier Upgrade Guide](../Developer_Integrator/LinkedIn-Standard-Tier-Upgrade.md)
- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [Helm-Based Application Deployment](Helm-Based-Application-Deployment.md)
