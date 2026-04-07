---
title: "Helm Chart Customization Guide"
summary: "Advanced instructions for customizing ExpertFlow CX Helm charts, covering replica counts, resource limits, and custom image tags."
audience: [hosting-partner]
product-area: [platform, infrastructure]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# Helm Chart Customization Guide

The ExpertFlow CX platform is deployed using a master Helm chart. For production environments, the default values must be customized to align with your infrastructure requirements.

## 1. Extracting Default Values

Always start by extracting the current default configuration from the chart:

```bash
helm show values expertflow/ef-cx > custom-values.yaml
```

## 2. Common Customizations

### Scaling Microservices (Replica Count)
To increase the availability of critical services like the `conversation-manager`:

```yaml
conversation-manager:
  replicaCount: 3
  resources:
    limits:
      cpu: 500m
      memory: 1024Mi
```

### Resource Limits and Requests
Set limits to prevent any single microservice from consuming all node resources:

```yaml
global:
  resources:
    limits:
      cpu: 1
      memory: 2Gi
    requests:
      cpu: 100m
      memory: 512Mi
```

### Custom Image Tags
If you are deploying a specific patch release or a customized image:

```yaml
customer-manager:
  image:
    repository: gitimages.expertflow.com/core/customer-manager
    tag: v5.2.1-patch1
```

---

## 3. Applying the Custom Configuration

Apply your changes to the cluster using the following command:

```bash
helm upgrade --install ef-cx expertflow/ef-cx \
  --namespace expertflow \
  --values custom-values.yaml
```

### Verification
Monitor the rollout of your customized services:

```bash
kubectl -n expertflow get pods -w
```

---

## Related Guides
*   [Helm-Based Application Deployment](Helm-Based-Application-Deployment.md)
*   [Deploying the RKE2 Control Plane](Deploying-the-RKE2-Control-Plane.md)
