---
title: "Superset Deployment for Reporting"
summary: "Procedures for deploying Apache Superset on Kubernetes to serve as the ExpertFlow CX analytics and reporting engine."
audience: [partner]
product-area: [analytics, reports]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# Superset Deployment for Reporting

Apache Superset is the visualization engine used for ExpertFlow CX reports and dashboards. It is typically deployed as part of the `ef-external` or `reporting` namespace.

## 1. Prerequisites
- **PostgreSQL Database:** Superset requires a database to store its metadata (dashboards, charts, users).
- **Redis:** Used for query caching and message brokering.
- **Domain Name:** A dedicated FQDN for the reporting portal (e.g., `reports.expertflow.com`).

## 2. Deployment Steps

### Step 1: Configure Secret for Database Connection
Create a secret containing your PostgreSQL connection string:
```bash
kubectl create secret generic superset-db-conn \
  --from-literal=uri=postgresql://superset:password@postgres-svc:5432/superset
```

### Step 2: Deploy using Helm
```bash
helm upgrade --install superset expertflow/superset \
  --namespace ef-external \
  --values superset-values.yaml
```

### Step 3: Initialize Superset
Once the pods are running, initialize the database and create the admin user:
```bash
kubectl exec -it superset-pod-name -- superset-init
```

## 3. Post-Deployment Verification
Log in to the Superset UI using your admin credentials. Ensure the ExpertFlow reporting database is connected and visible under **Data > Databases**.

---

## Related Guides
*   [Superset Reports Configuration](../Solution_Admin/Superset-Reports-Configuration.md)
*   [Key Reporting Metrics](../Functional_Areas/Performance_Insights_Data/Key-Reporting-Metrics.md)
