---
audience: [developer]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Upgrade Guide: Postgres and Vault for Cisco Connector

This guide details the database and security configuration required for upgrading to CX 5.1.0, specifically for the Cisco Connector component.

## 1. Postgres Database Setup

### Create the Database
Access the Postgres pod and create the `ciscoConnector` database.
```bash
kubectl exec -it -n ef-external ef-postgresql-0 -- psql -U postgres
CREATE DATABASE "ciscoConnector";
\connect "ciscoConnector"
```

### Create Schema
Manually create the required tables (due to Vault datasource initialization timing, Hibernate cannot auto-create these on first start).
```sql
CREATE TABLE call_legs ( ... );
CREATE TABLE jtapi_events ( ... );
CREATE TABLE call_leg_history ( ... );
```

### Grant Permissions
Grant access to the `app_users` role for Vault dynamic user support.
```sql
GRANT USAGE, CREATE ON SCHEMA public TO app_users;
GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA public TO app_users;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON TABLES TO app_users;
```

## 2. HashiCorp Vault Configuration
Provision service-based accounts for Vault-enabled components using the provided script.
```bash
cd pre-deployment/service-based-accounts
chmod +x service-accounts.sh
./service-accounts.sh
```

## 3. Deployment
Once the database and Vault are provisioned, proceed with the Helm deployment of the Cisco Connector.
