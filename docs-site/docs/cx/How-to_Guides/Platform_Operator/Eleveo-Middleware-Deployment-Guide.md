---
title: "Eleveo Middleware Deployment Guide"
summary: "How-to guide for deploying the Eleveo Recording Middleware for ExpertFlow CX using Helm — covering custom values files for both the middleware and cronjob charts, all environment variable definitions, Keycloak authentication, and deployment commands."
audience: [platform-operator]
product-area: [voice, platform]
doc-type: how-to
difficulty: intermediate
keywords: ["Eleveo middleware deployment CX", "Eleveo recording CX", "cx-middleware Helm CX", "middleware-cronjob Helm CX", "Eleveo integration CX"]
aliases: ["Eleveo CX deployment", "Eleveo middleware Helm CX", "recording middleware CX"]
last-updated: 2026-03-10
---

# Eleveo Middleware Deployment Guide

This guide deploys the **Eleveo Recording Middleware** for ExpertFlow CX using Helm. The middleware bridges CX voice recordings with the Eleveo recording platform.

> **Single tenant only**: Eleveo Middleware supports single-tenant deployments in CX 5.0. Do not add authentication variables (`AUTH_ENABLED`, `API_USERNAME`, etc.) if ExpertFlow CX is multi-tenant.

---

## Prerequisites

- ExpertFlow CX deployed via Helm. See the CX Helm deployment guide.
- Eleveo deployment accessible from the CX cluster.
- Expertflow Helm charts repository added:

```bash
helm repo add expertflow https://expertflow.github.io/charts
helm repo update expertflow
```

---

## Step 1: Navigate to the Deployment Directory

```bash
cd <CX-Folder>/kubernetes/
```

---

## Step 2: Create Custom Values Files

Two Helm charts are deployed: the **middleware** (real-time recording relay) and the **cronjob** (backfill of past recordings).

### 2a. Create `cx-middleware-custom-values.yaml`

```bash
vi helm-values/cx-middleware-custom-values.yaml
```

Minimum required configuration:

```yaml
global:
  ingressRouter: <CUSTOM-FQDN>
```

To view all available configuration options:

```bash
helm show values expertflow/eleveo-middleware --version 4.10.0
```

Update the following under `siteEnvVars`:

| Variable | Description |
|---|---|
| `RECORDING_BACKEND` | Recording mechanism — leave at default `ELEVEO` |
| `LOG_LEVEL` | `INFO` (default) or `DEBUG` |
| `ELEVEO_ADMIN` | Eleveo administrator username |
| `ELEVEO_PASSWORD` | Eleveo administrator password |
| `ELEVEO_URL` | Eleveo server URL — format: `http://IP-address` |
| `ELEVEO_ADMIN_PASSWORD` | Eleveo administrator password (duplicate field) |
| `ELEVEO_USERNAME` | Eleveo username |
| `CX_FQDN` | Set automatically via `https://{{ .Values.global.ingressRouter }}` |

If APISIX authentication is enabled (`AUTH_ENABLED=true`), also set:

| Variable | Description |
|---|---|
| `AUTH_ENABLED` | `true` or `false` |
| `API_USERNAME` | Keycloak user with `admin` and `default` roles, Email-Verified enabled, non-temporary password |
| `API_PASS` | Password for the Keycloak API user |
| `CLIENT_ID` | Always `cim` |
| `CLIENT_SECRET` | Found in Keycloak under the `cim` client |

### 2b. Create `cx-middleware-cronjob-custom-values.yaml`

```bash
vi helm-values/cx-middleware-cronjob-custom-values.yaml
```

Minimum required configuration:

```yaml
global:
  ingressRouter: <CUSTOM-FQDN>
```

To view all available configuration options:

```bash
helm show values expertflow/middleware-cronjob --version 4.10.0
```

Update the following under `siteEnvVars`:

| Variable | Description |
|---|---|
| `RECORDING_BACKEND` | Leave at default `ELEVEO` |
| `LOG_LEVEL` | `INFO` (default) or `DEBUG` |
| `CX_FQDN` | Set automatically |
| `CX_CONVERSATION_MANAGER` | `https://EFCX-FQDN/conversation-manager` |
| `MIDDLEWARE_API` | Set automatically — format: `http://EFCX-FQDN/recording-middleware` |
| `RETRIEVAL_INTERVAL` | Number of past days to push recording links for on startup |
| `ELEVEO_MAX_CALL_TIME` | Maximum assumed call duration in minutes |
| `ELEVEO_PASSWORD` | Eleveo administrator password |
| `ELEVEO_PROCESSING_TIME` | Minutes after a call ends before it appears in Eleveo |
| `ELEVEO_TIMEZONE` | Eleveo deployment timezone (e.g., `Asia/Karachi`) |
| `ELEVEO_URL` | Eleveo server URL — format: `http://IP-address` |
| `ELEVEO_USERNAME` | Eleveo username |
| `TRUST_STORE_PASSWORD` | From `CX-<version>/cim-solution/kubernetes/helm/Core/values.yml` under `efConnectionVars` |
| `KEY_STORE_PASSWORD` | From the same file under `efConnectionVars` |

---

## Step 3: Deploy the Eleveo Middleware Helm Chart

```bash
helm upgrade --install \
  --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" \
  eleveo-middleware \
  --values helm-values/cx-middleware-custom-values.yaml \
  expertflow/eleveo-middleware \
  --version <cx-version>
```

Verify pods are running:

```bash
kubectl get pods -n expertflow | grep eleveo-middleware
```

---

## Step 4: Deploy the Eleveo Middleware Cronjob Helm Chart

```bash
helm upgrade --install \
  --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" \
  middleware-cronjob \
  --debug \
  --values helm-values/cx-middleware-cronjob-custom-values.yaml \
  expertflow/middleware-cronjob \
  --version <cx-version>
```

---

## Related Articles

- [Helm-Based Application Deployment](Helm-Based-Application-Deployment.md)
- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
