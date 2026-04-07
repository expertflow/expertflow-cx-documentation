---
title: "CX-Analyser Infrastructure Setup"
summary: "Technical guide for configuring the reporting connector, TLS certificates, and database schemas for CX-Analyser."
audience: [platform-operator]
product-area: [reporting, infrastructure, mysql]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# CX-Analyser Infrastructure Setup

The CX-Analyser reporting engine requires a specific infrastructure setup to transform real-time MongoDB interaction data into a relational SQL database for visualization.

## 1. TLS and Certificate Management
ExpertFlow requires secure communication between the Reporting Connector and the MySQL/MSSQL database.
- **Keystore Setup:** Acquire the MySQL `.jks` and `.cert` files.
- **ConfigMap:** Create a ConfigMap in the tenant namespace to store the keystore.
```bash
kubectl create configmap ef-reporting-connector-keystore-cm --from-file=mykeystore.jks -n <tenant-ns>
```

## 2. Database Creation
For each tenant, you must initialize a dedicated reporting schema.
1.  Navigate to the `pre-deployment/reportingConnector/dbScripts/` directory.
2.  Run the creation script for your target DBMS (MySQL or MSSQL).
3.  **Privileges:** Ensure the database user has permissions to create tables and execute procedures.

## 3. Reporting Connector Configuration
The Reporting Connector bridge requires a specific configuration file (`reporting-connector.conf`) per tenant.
- **tenant_id:** Must match the tenant's logical ID.
- **Database Details:** IP, Port, Username, and Password for the SQL instance.
- **Service Name:** Link to the historical reports service (e.g., `http://ef-cx-historical-reports-svc:8081`).

## 4. Deployment
Once the ConfigMaps and Databases are ready, deploy the Reporting Scheduler via Helm:
```bash
helm upgrade --install --namespace <tenant-ns> cx-reporting helm/Reporting --values=values.yaml
```

---

*For details on the resulting SQL tables, see the [Reporting Database Schema Reference](../Developer_Integrator/Reporting-Database-Schema-Reference.md).*
