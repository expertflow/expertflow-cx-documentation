# CX Knowledgebase : Vault Configuration

To configure Vault for MongoDB Dynamic Database Credentials, please see this [guide](Configure-Vault-for-MongoDB-Dynamic-Database-Credentials_1245216775.html).  
  
To configure Vault for Redis Dynamic Database Credentials, please see this [guide](Configure-Vault-for-Redis-Database-Credentials_1369505803.html).

To configure Vault for PostgreSQL Dynamic Database Credentials, please see this [guide](Configure-Vault-for-PostgreSQL-Dynamic-Database-Credentials_1335066669.html).

To configure Vault for ActiveMQ, please see this [guide](Configure-Vault-for-ActiveMQ_1375404115.html).

For MongoDB, Redis, and PostgreSQL, credentials rotate according to the TTL configured in Vault. The default TTL is currently set to **10 years** to avoid frequent restarts of CX‑Core components, as each rotation requires a component restart and therefore incurs some expected downtime.
