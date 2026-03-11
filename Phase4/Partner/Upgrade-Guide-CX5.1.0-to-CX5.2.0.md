---
title: "Upgrade Guide: CX 5.1.0 to CX 5.2.0"
summary: "Step-by-step upgrade guide for ExpertFlow CX from version 5.1.0 to 5.2.0 — covering the ActiveMQ Classic to ActiveMQ Artemis migration, Core, Channels, Campaigns, and QM Helm chart upgrades."
audience: [partner]
product-area: [platform]
doc-type: how-to
difficulty: advanced
keywords: ["CX 5.2.0 upgrade", "ExpertFlow upgrade 5.1.0 5.2.0", "ActiveMQ Artemis migration CX", "Helm upgrade CX 5.2.0", "upgrade guide CX 5.2.0"]
aliases: ["upgrade CX 5.2.0", "5.1.0 to 5.2.0 CX upgrade", "ActiveMQ Artemis CX upgrade"]
last-updated: 2026-03-10
---

# Upgrade Guide: CX 5.1.0 to CX 5.2.0

> Before upgrading, ensure the system is idle — all agents must be logged out from the Agent Desk.

For guidelines on custom `values.yaml` layering, refer to the **CX Helm Chart Custom Configuration Strategy** guide.

> **Breaking change**: This release replaces **ActiveMQ Classic** with **ActiveMQ Artemis**. The existing ActiveMQ deployment must be uninstalled and replaced before upgrading the core CX charts.

---

## Step 1: Update Helm Repository

```bash
helm repo update expertflow
```

---

## Step 2: Uninstall ActiveMQ Classic

```bash
helm uninstall -n ef-external activemq
kubectl delete pvc -n ef-external activemq-activemq-0
```

---

## Step 3: Deploy ActiveMQ Artemis

Deploy ActiveMQ Artemis following the Apache ActiveMQ Artemis deployment guide (latest stable version as a system service).

---

## Step 4: Deploy Core

Update the ActiveMQ connection variables in `helm-values/ef-cx-custom-values.yaml`:

```yaml
efConnectionVars:
  ACTIVEMQ_PRIMARY_URL: "<Artemis-IP-Address>"     # Use IP address, not service name
  ACTIVEMQ_SECONDARY_URL: "<Artemis-IP-Address>"   # Use IP address, not service name
```

Deploy:

```bash
helm upgrade --install --namespace expertflow --create-namespace ef-cx \
  --debug --values helm-values/ef-cx-custom-values.yaml \
  expertflow/cx --version 5.2.0-rc.1
```

---

## Step 5: Deploy Channels

```bash
helm upgrade --install --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" --debug \
  cx-channels --values helm-values/cx-channels-custom-values.yaml \
  expertflow/channels --version 5.2.0-rc.1
```

---

## Step 6: Deploy Campaigns

```bash
helm upgrade --install --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" cx-campaigns --debug \
  --values helm-values/cx-campaigns-custom-values.yaml \
  expertflow/campaigns --version 5.2.0-rc.1
```

---

## Step 7: Deploy QM

```bash
helm upgrade --install --namespace=expertflow \
  --set global.efCxReleaseName="ef-cx" qm --debug \
  --values=helm-values/cx-qm-custom-values.yaml \
  expertflow/qm --version 5.2.0-rc.1
```

---

## Related Articles

- [Upgrade Guide: CX 5.0.2 to CX 5.1.0](Upgrade-Guide-CX5.0.2-to-CX5.1.0.md)
- [Change Default ActiveMQ Passwords Using ConfigMap](../Solution_Admin/Change-Default-ActiveMQ-Passwords.md)
- [Vault Dynamic Credentials — ActiveMQ](../Solution_Admin/Vault-Dynamic-Credentials-ActiveMQ.md)
