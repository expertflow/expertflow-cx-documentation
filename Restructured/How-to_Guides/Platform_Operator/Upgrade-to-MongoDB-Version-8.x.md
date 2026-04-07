---
title: "Upgrading MongoDB to Version 8.x"
summary: "Comprehensive procedure for upgrading MongoDB from version 6.x to 8.x, including the mandatory intermediate step through version 7.x and feature compatibility updates."
audience: [platform-operator]
product-area: [platform, database]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# Upgrading MongoDB to Version 8.x

This guide outlines the mandatory upgrade path for ExpertFlow CX MongoDB from version 6.x to 8.x. This procedure ensures data integrity by following the official version-by-version compatibility path.

## 1. Prerequisites & Backup

### Important Compatibility Note
This guide is valid for **ExpertFlow CX 4.6 and higher**, where AUTH and TLS capabilities are already enabled. Older versions must be updated to the standard security baseline before attempting this upgrade.

### Mandatory Backup
Before starting, perform a full backup of your MongoDB data. Choose the method appropriate for your environment:
*   **Small Datasets:** [Manual PostgreSQL/MongoDB Backup](../../Reference/Archive-Notice.md)
*   **Large Datasets:** [Velero Kubernetes Backup/Restore](../../Reference/Archive-Notice.md)

---

## 2. Upgrade Path Overview

MongoDB requires a sequential upgrade of the **Feature Compatibility Version (FCV)**. You cannot skip major versions.

1.  **Current State:** MongoDB 6.x (FCV 6.0)
2.  **Intermediate State:** Upgrade to MongoDB 7.x and set FCV to 7.0.
3.  **Target State:** Upgrade to MongoDB 8.x and set FCV to 8.0.

---

## 3. Phase 1: Upgrade to MongoDB 7.x

### Step 1: Pull the v7 Helm Chart
```bash
mkdir -p mongodb-v7 && cd mongodb-v7
helm pull --untar oci://registry-1.docker.io/bitnamicharts/mongodb --version 15.6.9
cd mongodb
```

### Step 2: Configure `values.yaml`
Update your existing `values.yaml` with your current root password and TLS secrets. Ensure `useStatefulSet: true` is set.

### Step 3: Execute v7 Upgrade
```bash
helm upgrade --install --namespace ef-external --values ./values.yaml mongo .
```

### Step 4: Update Feature Compatibility (FCV 7.0)
1.  Launch a temporary MongoDB 7 client pod.
2.  Connect to the primary node using `mongosh`.
3.  Run the FCV update command:
    ```javascript
    db.adminCommand( { setFeatureCompatibilityVersion: "7.0", confirm: true } )
    ```
4.  Verify with: `db.adminCommand( { getParameter: 1, featureCompatibilityVersion: 1 } )`.

---

## 4. Phase 2: Upgrade to MongoDB 8.x

### Step 1: Pull the v8 Helm Chart
```bash
mkdir -p mongodb-v8 && cd mongodb-v8
helm pull --untar oci://registry-1.docker.io/bitnamicharts/mongodb --version 16.4.4
cd mongodb
```

### Step 2: Execute v8 Upgrade
Using your updated `values.yaml` (ensure the version tags are updated to 8.x):
```bash
helm upgrade --install --namespace ef-external --values ./values.yaml mongo .
```

### Step 3: Update Feature Compatibility (FCV 8.0)
1.  Launch a temporary MongoDB 8 client pod.
2.  Connect to the primary node.
3.  Run the FCV update command:
    ```javascript
    db.adminCommand( { setFeatureCompatibilityVersion: "8.0", confirm: true } )
    ```

---

## 5. Post-Upgrade Verification

### Client Re-authentication
After the upgrade, the CX microservices must reconnect. If you updated TLS certificates during the process, ensure the new secrets are distributed to the `expertflow` namespace:

```bash
kubectl -n expertflow rollout restart deploy
```

Verify that the logs for `conversation-manager` and `customer-manager` show successful connections to the upgraded MongoDB instance.

---

## Related Guides
*   [Deploying MongoDB with Replica Sets](Deployment-of-Mongo-using-ReplicaSet.md)
*   [Vault Dynamic Credentials — MongoDB](../Administrator/Vault-Dynamic-Credentials-MongoDB.md)
