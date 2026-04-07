---
title: "Deploying MongoDB with Replica Sets"
summary: "Guide for configuring MongoDB in Replica Set mode on Kubernetes to achieve high availability, redundancy, and read/write isolation."
audience: [platform-operator]
product-area: [platform, database]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# Deploying MongoDB with Replica Sets

Deploying MongoDB in **Replica Set** mode is the recommended configuration for production ExpertFlow CX environments. This setup provides high availability (HA), data redundancy, and improved performance by isolating read and write workloads.

## 1. Benefits of Replica Sets
*   **High Availability:** Automatic failover if the primary node becomes unavailable.
*   **Read Isolation:** Secondary nodes can handle read queries, reducing the load on the primary node.
*   **Non-Disruptive Backups:** Backups can be taken from secondary nodes without impacting client requests on the primary node.

---

## 2. Resource Considerations

For a resilient deployment, replica members should be spread across different physical nodes in a multi-node Kubernetes cluster.

| Entity | Specification |
| :--- | :--- |
| **Replica Count** | 2 (1 Primary, 1 Secondary) |
| **RAM** | 4 GB per replica |
| **CPU Cores** | 1 CPU Core per replica |
| **Storage** | Persistent Volume (PV) per replica |

---

## 3. Deployment Steps

The MongoDB HA stack is deployed using the ExpertFlow Helm chart.

### Step 1: Extract Default Values
Clone the values file from the ExpertFlow repository to customize your deployment:
```bash
helm show values expertflow/mongodb-ha > helm-values/mongo-db-ha-custom-values.yaml
```

### Step 2: Configure Authentication
Edit `helm-values/mongo-db-ha-custom-values.yaml` and update the root password under the `auth` section:
```yaml
auth:
  rootPassword: "YourSecurePassword"
```

### Step 3: Execute Deployment
Deploy the chart into the `ef-external` namespace:
```bash
helm upgrade --install \
  --namespace ef-external \
  --values helm-values/mongo-db-ha-custom-values.yaml \
  mongo expertflow/mongodb
```

### Step 4: Verify Status
Monitor the rollout to ensure all replicas are ready:
```bash
kubectl -n ef-external rollout status sts mongo-mongodb
```

Check the pod status:
```bash
kubectl -n ef-external get pods -l app.kubernetes.io/name=mongodb
```
*Expected Output:*
```text
NAME              READY   STATUS    RESTARTS   AGE
mongo-mongodb-0   1/1     Running   0          8m
mongo-mongodb-1   1/1     Running   0          6m
```

---

## Related Guides
*   [Upgrade to MongoDB Version 8.x](Upgrade-to-MongoDB-Version-8.x.md)
*   [Database Backup and Restore](../../Reference/Archive-Notice.md)
