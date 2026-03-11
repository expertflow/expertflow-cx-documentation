---
title: "Encryption at Rest Configuration Guide"
summary: "How-to guide for enabling AES256-GCM96 encryption at rest in ExpertFlow CX — covering Vault AppRole setup, Transit secrets engine configuration, Conversation Manager environment variables, key rotation, and Vault backup/restore."
audience: [solution-admin]
product-area: [security]
doc-type: how-to
difficulty: advanced
keywords: ["encryption at rest CX", "AES256 CX", "Vault transit CX", "ENABLE_ENCRYPTION CX", "Conversation Manager encryption", "Vault AppRole CX", "encrypt conversation data CX", "key rotation CX"]
aliases: ["CX encryption at rest", "data encryption CX", "Vault encryption CX"]
last-updated: 2026-03-10
---

# Encryption at Rest Configuration Guide

ExpertFlow CX supports AES256-GCM96 encryption at rest for conversation data. When enabled, the **Conversation Manager** microservice encrypts stored conversation content using HashiCorp Vault's Transit secrets engine.

> **Critical warning**: Once encryption is enabled and data is stored, **do not disable `ENABLE_ENCRYPTION`**. Disabling it after encrypted data exists makes all previously encrypted conversations unreadable.

---

## Architecture Overview

| Component | Role |
|---|---|
| **Conversation Manager** | CX microservice that stores conversation data. Handles encrypt/decrypt operations. |
| **HashiCorp Vault** | External secrets manager. Provides the Transit encryption engine and AppRole authentication. |
| **Transit Secrets Engine** | Vault engine that performs encryption without storing the plaintext. Key never leaves Vault. |
| **AppRole** | Authentication method Vault uses to identify Conversation Manager. |

---

## Prerequisites

- HashiCorp Vault deployed and accessible from the ExpertFlow CX namespace.
- Vault CLI (`vault`) available, or access to the Vault UI.
- `kubectl` access to the ExpertFlow namespace.
- Helm access to update Conversation Manager values.

---

## Step 1: Configure Vault

### 1a. Enable the Transit Secrets Engine

```bash
vault secrets enable transit
```

### 1b. Create the Encryption Key

```bash
vault write -f transit/keys/ef-encryption
```

### 1c. Enable AppRole Authentication

```bash
vault auth enable approle
```

### 1d. Create a Policy for Conversation Manager

Create a file `ef-cx-policy.hcl`:

```hcl
path "transit/encrypt/ef-encryption" {
  capabilities = ["update"]
}

path "transit/decrypt/ef-encryption" {
  capabilities = ["update"]
}

path "transit/keys/ef-encryption" {
  capabilities = ["read"]
}
```

Apply the policy:

```bash
vault policy write ef-cx-policy ef-cx-policy.hcl
```

### 1e. Create the AppRole

```bash
vault write auth/approle/role/ef-cx-role \
  token_policies="ef-cx-policy" \
  token_ttl=1h \
  token_max_ttl=4h
```

### 1f. Retrieve AppRole Credentials

```bash
# Get Role ID
vault read auth/approle/role/ef-cx-role/role-id

# Get Secret ID
vault write -f auth/approle/role/ef-cx-role/secret-id
```

Save the `role_id` and `secret_id` values — you will need them in Step 2.

---

## Step 2: Configure Conversation Manager

Update the Conversation Manager Helm values to enable encryption and mount the Vault credentials.

### 2a. Set Environment Variables

In your Conversation Manager custom values file, add:

```yaml
env:
  - name: ENABLE_ENCRYPTION
    value: "true"
  - name: VAULT_ADDR
    value: "http://vault.vault.svc.cluster.local:8200"
  - name: VAULT_ROLE_ID
    value: "<your-role-id>"
  - name: VAULT_SECRET_ID
    value: "<your-secret-id>"
  - name: VAULT_TRANSIT_KEY
    value: "ef-encryption"
```

### 2b. Mount Vault Token Volume (if using Kubernetes Vault agent)

If your deployment uses the Vault Agent sidecar, configure `extraVolumes` and `extraVolumeMounts`:

```yaml
extraVolumes:
  - name: vault-token
    emptyDir:
      medium: Memory

extraVolumeMounts:
  - name: vault-token
    mountPath: /vault/secrets
    readOnly: true
```

### 2c. Apply the Changes

```bash
helm upgrade --install conversation-manager \
  --namespace=expertflow \
  --values=conversation-manager-custom-values.yaml \
  expertflow/conversation-manager
```

---

## Key Rotation

Rotate the encryption key periodically or after a suspected compromise. Rotation adds a new key version; Vault automatically uses the latest version for new encryptions while retaining old versions for decryption.

```bash
vault write -f transit/keys/ef-encryption/rotate
```

After rotation, trigger a reload in Conversation Manager so it picks up the new key version:

```bash
curl -X POST http://<conversation-manager-svc>/api/reload-keys
```

> Old key versions are retained by default. To prevent decryption with old versions, set a minimum decryptable version:
> ```bash
> vault write transit/keys/ef-encryption/config min_decryption_version=<version>
> ```

---

## Vault Backup and Restore

### Backup

Take a snapshot of the Vault Raft storage:

```bash
kubectl exec -n vault vault-0 -- vault operator raft snapshot save /tmp/vault-backup.snap
kubectl cp vault/vault-0:/tmp/vault-backup.snap ./vault-backup.snap
```

### Restore

```bash
kubectl cp ./vault-backup.snap vault/vault-0:/tmp/vault-backup.snap
kubectl exec -n vault vault-0 -- vault operator raft snapshot restore /tmp/vault-backup.snap
```

> After restore, unseal Vault and verify that the Transit engine and AppRole are functional before restarting Conversation Manager.

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---|---|---|
| Conversations show garbled/unreadable text | Encryption enabled but Vault unavailable | Verify Vault is reachable; check AppRole credentials |
| Conversation Manager fails to start | Invalid `VAULT_ROLE_ID` or `VAULT_SECRET_ID` | Re-generate AppRole secret ID and update values |
| Key rotation appears to have no effect | `reload-keys` API not called after rotation | Call the reload-keys endpoint on Conversation Manager |
| Data unreadable after disabling encryption | `ENABLE_ENCRYPTION` was set to `false` after data was encrypted | Re-enable encryption; data cannot be recovered without decryption key |

---

## Related Articles

- [Accessing Kubernetes Logs](Accessing-Kubernetes-Logs.md)
- [IAM Keycloak Configuration](IAM-Keycloak-Configuration.md)
- [Sizing Guidelines](Sizing-Guidelines.md)
