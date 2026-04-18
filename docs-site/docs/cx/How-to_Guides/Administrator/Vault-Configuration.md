---
title: "Vault Configuration"
summary: "Overview of HashiCorp Vault configuration for ExpertFlow CX — covering dynamic database credentials for MongoDB, Redis, PostgreSQL, and ActiveMQ, with TTL notes and rotation behavior."
audience: [administrator]
product-area: [security]
doc-type: reference
difficulty: advanced
keywords: ["Vault configuration CX", "HashiCorp Vault CX", "dynamic credentials CX", "MongoDB Vault CX", "Redis Vault CX", "PostgreSQL Vault CX", "ActiveMQ Vault CX", "Vault TTL CX"]
aliases: ["CX Vault setup", "Vault dynamic credentials CX", "configure Vault CX"]
last-updated: 2026-03-10
---

# Vault Configuration

ExpertFlow CX uses **HashiCorp Vault** to manage dynamic database credentials for its core data stores. Dynamic credentials are short-lived, auto-rotated credentials that Vault issues to CX components — eliminating the need to store static database passwords in configuration files.

---

## Supported Integrations

| Data Store | Purpose |
|---|---|
| **MongoDB** | Primary document store for conversation and configuration data |
| **Redis** | Cache and session state |
| **PostgreSQL** | Relational data (reporting, QM) |
| **ActiveMQ** | Message broker credentials |

---

## Credential Rotation and TTL

Credentials rotate according to the **TTL** (Time to Live) configured in Vault for each database secrets engine role.

> **Default TTL**: The default TTL for all database credentials in ExpertFlow CX is set to **10 years**. This intentionally long TTL avoids frequent automatic rotations, because each credential rotation requires a restart of the affected CX components, which incurs brief downtime.

Adjust the TTL according to your organization's security policy. Lower TTLs increase security but require planning for scheduled restarts.

---

## Configuration Guides

Configure Vault dynamic credentials for each data store by following the dedicated guides:

- **MongoDB** — [Configure Vault for MongoDB Dynamic Database Credentials](Vault-Dynamic-Credentials-MongoDB.md)
- **Redis** — [Configure Vault for Redis Database Credentials](Vault-Dynamic-Credentials-Redis.md)
- **PostgreSQL** — [Configure Vault for PostgreSQL Dynamic Database Credentials](Vault-Dynamic-Credentials-MongoDB.md)
- **ActiveMQ** — [Configure Vault for ActiveMQ](Vault-Dynamic-Credentials-ActiveMQ.md)

---

## Related Articles

- [Encryption at Rest Configuration Guide](Encryption-at-Rest-Configuration-Guide.md)
- [IAM Keycloak Configuration](IAM-Keycloak-Configuration.md)
- [Accessing Kubernetes Logs](Accessing-Kubernetes-Logs.md)
