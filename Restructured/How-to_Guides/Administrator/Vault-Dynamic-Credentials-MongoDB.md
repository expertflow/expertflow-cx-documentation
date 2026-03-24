---
title: "Vault Dynamic Credentials — MongoDB"
summary: "How-to guide for configuring HashiCorp Vault to generate dynamic database credentials for MongoDB — covering the database secrets engine, connection plugin config, role creation, TTL tuning, and AppRole policy attachment."
audience: [administrator]
product-area: [platform]
doc-type: how-to
difficulty: advanced
keywords: ["Vault MongoDB dynamic credentials CX", "Vault database engine MongoDB CX", "mongodb-database-plugin CX", "Vault AppRole MongoDB CX", "dynamic credentials ExpertFlow CX"]
aliases: ["Vault MongoDB CX", "dynamic MongoDB credentials CX", "Vault database credentials MongoDB CX"]
last-updated: 2026-03-10
---

# Vault Dynamic Credentials — MongoDB

This guide configures HashiCorp Vault to generate dynamic credentials for MongoDB using the **database secrets engine**. Vault creates short-lived MongoDB users on demand, eliminating hardcoded credentials in CX service configuration.

> For an overview of Vault credential management across all CX components, see [Vault Configuration](Vault-Configuration.md).

---

## Prerequisites

- Vault deployed and initialized in the `vault` namespace.
- All Vault pods unsealed. Check status:

```bash
kubectl -n vault exec -it vault-0 -- vault status
kubectl -n vault exec -it vault-1 -- vault status
kubectl -n vault exec -it vault-2 -- vault status
```

If any pod shows `Sealed: true`, unseal it using your Vault unseal keys before continuing.

- MongoDB TLS CA secret (`mongo-mongodb-ca`) must be present in the `vault` namespace. Check:

```bash
kubectl get secrets -n vault
```

If missing, copy it from the `ef-external` namespace:

```bash
kubectl get secret mongo-mongodb-ca -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: vault/' \
  | kubectl create -f -
```

---

## Step 1: Exec into Vault and Log In

```bash
kubectl -n vault exec -it vault-0 -- sh
vault login
```

Enter your root token when prompted.

---

## Step 2: Enable the Database Secrets Engine

```bash
vault secrets enable database
```

---

## Step 3: Configure the MongoDB Database Plugin

```bash
vault write database/config/mongodb-database \
  plugin_name="mongodb-database-plugin" \
  allowed_roles="mongodb-role" \
  username="root" \
  password="Expertflow123" \
  connection_url="mongodb://{{username}}:{{password}}@mongo-mongodb.ef-external.svc.cluster.local:27017/?authSource=admin&tls=true&tlsCAFile=/vault/userconfig/mongo-mongodb-ca/mongodb-ca-cert&tlsCertificateKeyFile=/vault/userconfig/mongo-mongodb-ca/client-pem&tlsAllowInvalidHostnames=true"
```

Replace `username` and `password` with your MongoDB root credentials.

---

## Step 4: Set TTLs for the Database Engine

By default, Vault caps lease TTLs at 768 hours. For long-lived dynamic credentials (to avoid frequent pod restarts), increase the TTL to 87600 hours (10 years):

```bash
vault secrets tune -default-lease-ttl=87600h -max-lease-ttl=87600h database/
```

---

## Step 5: Create a Role for MongoDB

```bash
vault write database/roles/mongodb-role \
    db_name=mongodb-database \
    creation_statements='{ "db": "admin", "roles": [{ "role": "root", "db": "admin" }] }' \
    default_ttl="87600h" \
    max_ttl="87600h"
```

---

## Step 6: Write and Attach the Vault Policy

Write the `ef-policy` policy granting access to database credentials and Transit secrets:

```bash
vault policy write ef-policy - <<EOF
path "/transit/export/*" {
  capabilities = ["read"]
}
path "database/creds/*" {
  capabilities = ["read"]
}
EOF
```

Attach the policy to the AppRole:

```bash
vault write auth/approle/role/expertflow policies="ef-policy"
exit
```

---

## Changing TTLs Later

If you need to update credential TTLs after the initial setup:

```bash
kubectl -n vault exec -it vault-0 -- sh
vault login

# Update the engine-level TTL cap
vault secrets tune -default-lease-ttl=87600h -max-lease-ttl=87600h database/

# Update the role TTLs
vault write database/roles/mongodb-role \
    db_name=mongodb-database \
    creation_statements='{ "db": "admin", "roles": [{ "role": "root", "db": "admin" }] }' \
    default_ttl="87600h" \
    max_ttl="87600h"

exit
```

---

## Related Articles

- [Vault Configuration](Vault-Configuration.md)
- [Vault Dynamic Credentials — Redis](Vault-Dynamic-Credentials-Redis.md)
- [Vault Dynamic Credentials — ActiveMQ](Vault-Dynamic-Credentials-ActiveMQ.md)
