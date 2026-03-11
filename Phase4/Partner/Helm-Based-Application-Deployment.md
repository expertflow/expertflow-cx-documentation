---
title: "Helm-Based Application Deployment"
summary: "Guide for Multi-tenant Partners to deploy the ExpertFlow CX application layers using Helm charts and customized values.yaml files."
audience: [partner, integrator]
product-area: [infrastructure, helm]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Helm-Based Application Deployment

Once your Kubernetes cluster is active, you must deploy the ExpertFlow CX application services. This is performed using **Helm**, allowing for consistent and version-controlled deployments.

## 1. Environment Configuration
ExpertFlow uses a centralized GitLab repository for its container images and Helm charts.
- **Secret Sync:** Mirror the `ef-gitlab-secret` from the system namespace into your specific tenant or core namespace to allow image pulling.
```bash
kubectl get secret ef-gitlab-secret -n expertflow -o yaml | sed 's/namespace: expertflow/namespace: <target-ns>/' | kubectl create -f -
```

## 2. Customizing values.yaml
You must define your platform settings in a local `values.yaml` file before installation.
- **Ingress Routing:** Define your Master FQDN.
```yaml
global:
  ingressRouter: "cx.example.com"
```

## 3. Installation Sequence
Deploy the core platform components using the Helm CLI:
```bash
helm upgrade --install --namespace <namespace> --debug expertflow-cx --values=values.yaml ./helm-chart
```

## 4. Multi-Tenant Deployment (MTT)
For partners hosting multiple customers:
1.  Create a dedicated namespace for each tenant.
2.  Deploy the **MTT-single** chart into the tenant's namespace using their specific subdomain.
3.  Ensure the `global.ingressRouter` reflects the tenant's unique FQDN (e.g., `customer1.cx.example.com`).

---

*After deployment, you must initialize the reporting layer. See [CX-Analyser Infrastructure Setup](CX-Analyser-Infrastructure-Setup.md).*
