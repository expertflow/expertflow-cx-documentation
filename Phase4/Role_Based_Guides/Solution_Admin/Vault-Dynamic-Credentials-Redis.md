---
title: "Vault Dynamic Credentials — Redis"
summary: "How-to guide for storing Redis credentials in HashiCorp Vault using the KV-v2 secrets engine — covering secret storage, policy creation, and AppRole attachment for ExpertFlow CX."
audience: [solution-admin, partner]
product-area: [platform]
doc-type: how-to
difficulty: advanced
keywords: ["Vault Redis credentials CX", "Vault KV Redis CX", "Redis Vault secret CX", "Vault AppRole Redis CX", "ExpertFlow Redis Vault"]
aliases: ["Vault Redis CX", "Redis credentials Vault CX", "KV Redis Vault CX"]
last-updated: 2026-03-10
---

# Vault Dynamic Credentials — Redis

This guide stores Redis credentials in HashiCorp Vault using the **KV-v2 secrets engine**. CX services retrieve credentials from Vault at startup, eliminating hardcoded Redis passwords.

> For an overview of Vault credential management across all CX components, see [Vault Configuration](Vault-Configuration.md).

---

## Prerequisites

- Vault deployed, initialized, and all pods unsealed in the `vault` namespace.
- Redis TLS certificate secret (`redis-crt`) present in the `vault` namespace. Check:

```bash
kubectl get secrets -n vault
```

If missing, copy it from the `ef-external` namespace:

```bash
kubectl get secret redis-crt -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: vault/' \
  | kubectl create -f -
```

---

## Step 1: Exec into Vault

```bash
kubectl -n vault exec -it vault-0 -- sh
```

---

## Step 2: Enable the KV-v2 Secrets Engine

If not already enabled:

```bash
vault secrets enable -path=kv kv-v2
```

---

## Step 3: Store Redis Credentials

```bash
vault kv put kv/redis \
    redis.username=superuser \
    redis.password=Expertflow464
```

Replace `superuser` and `Expertflow464` with your actual Redis credentials.

Verify the stored secret:

```bash
vault kv get kv/redis
```

---

## Step 4: Write and Attach the Vault Policy

The `ef-policy` policy grants CX services read access to Redis, ActiveMQ, database credentials, and Transit secrets. If the policy already exists (e.g., from the MongoDB setup), update it to include the Redis path:

```bash
vault policy write ef-policy - <<EOF
path "/transit/export/*" {
  capabilities = ["read"]
}
path "database/creds/*" {
  capabilities = ["read"]
}
path "kv/data/activemq/broker" {
  capabilities = ["read"]
}
path "kv/data/redis" {
  capabilities = ["read"]
}
EOF
```

Attach the policy to the AppRole:

```bash
vault write auth/approle/role/expertflow policies="ef-policy"
```

---

## Step 5: Exit the Pod

```bash
exit
```

---

## Related Articles

- [Vault Configuration](Vault-Configuration.md)
- [Vault Dynamic Credentials — MongoDB](Vault-Dynamic-Credentials-MongoDB.md)
- [Vault Dynamic Credentials — ActiveMQ](Vault-Dynamic-Credentials-ActiveMQ.md)
