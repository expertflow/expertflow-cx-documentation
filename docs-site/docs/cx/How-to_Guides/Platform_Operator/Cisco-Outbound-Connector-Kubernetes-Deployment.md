---
title: "Cisco Outbound Connector — Kubernetes Deployment"
summary: "How-to guide for deploying the Cisco Outbound Connector on an RKE2 Kubernetes cluster — covering Redis setup, artifact cloning, ConfigMap configuration, Unified Admin channel setup, and Keycloak authentication for APISIX-enabled deployments."
audience: [platform-operator]
product-area: [voice, channels]
doc-type: how-to
difficulty: intermediate
keywords: ["Cisco outbound connector Kubernetes CX", "Cisco outbound K8s deployment CX", "UCCX Kubernetes connector CX", "cisco-outbound-connector ConfigMap CX", "Cisco CCX CCE Kubernetes CX"]
aliases: ["Cisco outbound K8s CX", "UCCX Kubernetes connector CX", "Cisco connector K8s deployment CX"]
last-updated: 2026-03-10
---

# Cisco Outbound Connector — Kubernetes Deployment

This guide deploys the Cisco Outbound Connector in a Kubernetes cluster running ExpertFlow CX. The connector integrates Cisco UCCE or UCCX outbound campaigns with the CX platform.

---

## Prerequisites

- ExpertFlow CX deployed in the cluster.
- Redis installed on a server accessible to the cluster.
- Cisco UCCE or UCCX with API-created campaigns configured.

---

## Redis Setup

On the Redis host server:

```bash
systemctl enable redis
systemctl enable redis-server
systemctl start redis
systemctl start redis-server

# Set a password (replace PASSWORD)
sed -i '/# requirepass/c\requirepass PASSWORD' /etc/redis/redis.conf

# Allow external connections
sed -i '/protected-mode/c\protected-mode no' /etc/redis/redis.conf
sed -i '/bind 127.0.0.1 -::1/c\# bind 127.0.0.1 -::1' /etc/redis/redis.conf
sed -i '/bind 127.0.0.1 ::1/c\# bind 127.0.0.1 ::1' /etc/redis/redis.conf

systemctl restart redis
systemctl restart redis-server
```

---

## Deploy Kubernetes Artifacts

SSH to the EF CX server and navigate to the root folder.

### Step 1: Clone the connector repository and create namespace

```bash
git clone -b deploy_artifacts_4.9.1 \
  https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/cisco-outbound-connector.git

cd cisco-outbound-connector

kubectl create namespace cisco-voice

# Copy ActiveMQ TLS certificate to the cisco-voice namespace
kubectl get secret activemq-tls -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: cisco-voice/' \
  | kubectl create -f -

# Pull the connector image
CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock \
  /var/lib/rancher/rke2/bin/ctr -n k8s.io i pull \
  -u efcx:RecRpsuH34yqp56YRFUb \
  gitimages.expertflow.com/rtc/cisco-outbound-connector:4.9.1
```

### Step 2: Set your FQDN

Replace `<FQDN>` with your actual deployment FQDN:

```bash
sed -i 's/devops[0-9]*.ef.com/<FQDN>/g' ./*
```

### Step 3: Configure the ConfigMap

```bash
vi ef-cisco-outbound-connector-cm.yml
```

Update the following values:

| Variable | Description |
|---|---|
| `CISCO_FQDN` | URL of the Cisco UCCX/UCCE deployment |
| `CISCO_USERNAME` | Admin username for Cisco |
| `CISCO_PASS` | Admin password for Cisco |
| `CISCO_TYPE` | `CCX` or `CCE` |
| `CX_FQDN` | ExpertFlow CX URL (`https://FQDN`) |
| `DB_NAME` | CCX default: `db_cra`; CCE: database containing `Dialer_Detail` |
| `DB_IP` | IP address of the Cisco database server |
| `DB_PASS` | Cisco database password |
| `DB_PORT` | CCX default: `1504`; CCE default: `1433` |
| `DB_USERNAME` | CCX default: `uccxhruser`; CCE default: `sa` |
| `LOG_LEVEL` | `INFO` (default) or `DEBUG` |
| `REDIS_DB` | Redis database index (0–16) for call ID storage |
| `REDIS_HOST` | Redis server IP |
| `REDIS_PASS` | Redis password |
| `REDIS_PORT` | Redis port (default: `6379`) |
| `REDIS_DELAY` | Minutes between Redis call result checks |
| `SERVICE_ID` | Service Identifier from EF CX Unified Admin channel settings |
| `AUTH_ENABLED` | `true` if APISIX authentication is enabled in EFCX, otherwise `false` |
| `API_USERNAME` | Keycloak user for API authentication (see note below) |
| `API_PASS` | Password for the Keycloak API user |
| `CLIENT_ID` | Always `cim` |
| `CLIENT_SECRET` | Found in Keycloak under the `cim` client |

> **Keycloak API user setup** (required when `AUTH_ENABLED=true`): Create a user in the Expertflow Keycloak realm. Assign the `admin` and `default` roles with **Email-Verified** enabled. Set a non-temporary password.

### Step 4: Apply Kubernetes manifests

```bash
kubectl apply -f ef-cisco-outbound-connector-cm.yml
kubectl apply -f ef-cisco-outbound-connector-service.yml
kubectl apply -f ef-cisco-outbound-connector-deployment.yml
kubectl apply -f ef-cisco-outbound-connector-ingress.yml
```

---

## Configure Unified Admin

1. Open Unified Admin and navigate to **Channel Provider**.
2. Add a new provider:
   - **Supported Channel Type**: `CISCO_CC`
   - **Provider Webhook**: `http://cx-cisco-outbound-connector-svc.cisco-voice.svc:8080/ccm-msg/receive`
3. Add a new **Channel Connector** using this provider.
4. Create a new **Channel** of type `CISCO_CC`, setting the **Service Identifier** to match the `SERVICE_ID` value in your ConfigMap.

---

## Related Articles

- [Cisco Outbound Connector — Docker Deployment](Cisco-Outbound-Connector-Docker-Deployment.md)
- [Cisco Voice Channel Configuration](../Developer_Integrator/Cisco-Voice-Channel-Configuration.md)
