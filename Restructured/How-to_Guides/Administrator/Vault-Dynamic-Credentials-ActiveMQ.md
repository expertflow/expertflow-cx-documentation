---
title: "Vault Dynamic Credentials — ActiveMQ"
summary: "How-to guide for configuring HashiCorp Vault to manage ActiveMQ credentials using the KV-v2 secrets engine — covering the CSI secrets store driver, Kubernetes authentication role, SecretProviderClass, and ActiveMQ pod redeployment."
audience: [administrator]
product-area: [platform]
doc-type: how-to
difficulty: advanced
keywords: ["Vault ActiveMQ credentials CX", "Vault KV ActiveMQ CX", "secrets-store-csi-driver CX", "SecretProviderClass ActiveMQ CX", "Vault Kubernetes auth ActiveMQ CX"]
aliases: ["Vault ActiveMQ CX", "ActiveMQ credentials Vault CX", "CSI secrets ActiveMQ CX"]
last-updated: 2026-03-10
---

# Vault Dynamic Credentials — ActiveMQ

This guide configures HashiCorp Vault to supply ActiveMQ credentials to the CX deployment using the **KV-v2 secrets engine** and the **Secrets Store CSI Driver**. This approach injects Vault secrets directly into the ActiveMQ pod at startup.

> This procedure requires redeploying the ActiveMQ pod.

> For an overview of Vault credential management across all CX components, see [Vault Configuration](Vault-Configuration.md).

---

## Prerequisites

- Vault deployed, initialized, and all pods unsealed in the `vault` namespace.
- `kubectl` access to the cluster with permissions on `vault` and `ef-external` namespaces.
- CX Helm chart files available locally (the `pre-deployment/activemq-vault` directory is required in Step 3).

---

## Step 1: Install the Secrets Store CSI Driver

```bash
cd CX-4.10.5/kubernetes

helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver --namespace vault
```

---

## Step 2: Configure Vault

Exec into the Vault pod:

```bash
kubectl -n vault exec -it vault-0 -- sh
```

### Create the KV-v2 secret path (if not already enabled)

```bash
vault secrets enable -path=kv kv-v2
```

### Store ActiveMQ credentials

```bash
vault kv put kv/activemq/broker \
    activemq.username=admin \
    activemq.password=Expertflow123
```

Replace `admin` and `Expertflow123` with your actual ActiveMQ credentials.

Verify:

```bash
vault kv get kv/activemq/broker
```

### Write the AppRole policy

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

vault write auth/approle/role/expertflow policies="ef-policy"
```

### Configure Kubernetes authentication

Create a dedicated policy for the Kubernetes role:

```bash
vault policy write activemq-kv - <<EOF
path "kv/data/activemq/broker" {
  capabilities = ["read"]
}
EOF
```

Enable Kubernetes auth and configure it:

```bash
vault auth enable kubernetes

vault write auth/kubernetes/config \
    token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
    kubernetes_host="https://kubernetes.default.svc:443" \
    kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
```

Create the Kubernetes role binding:

```bash
vault write auth/kubernetes/role/expertflow \
    bound_service_account_names=default \
    bound_service_account_namespaces=ef-external \
    policies=activemq-kv \
    ttl=87600h

exit
```

---

## Step 3: Apply SecretProviderClass, ClusterRole, and ClusterRoleBinding

Apply the pre-deployment Vault resources for ActiveMQ:

```bash
kubectl apply -f pre-deployment/activemq-vault
```

This creates the `SecretProviderClass` that tells the CSI driver how to fetch the ActiveMQ credentials from Vault, along with the required RBAC resources.

---

## Step 4: Restart Pods

Restart the Vault CSI provider pod to pick up the new SecretProviderClass:

```bash
kubectl delete pod -n vault <vault-csi-provider-pod>
```

Then restart the ActiveMQ pod to inject the new credentials:

```bash
kubectl delete pod -n ef-external <activemq-pod>
```

Replace `<vault-csi-provider-pod>` and `<activemq-pod>` with the actual pod names from `kubectl get pods`.

---

## Related Articles

- [Vault Configuration](Vault-Configuration.md)
- [Vault Dynamic Credentials — MongoDB](Vault-Dynamic-Credentials-MongoDB.md)
- [Vault Dynamic Credentials — Redis](Vault-Dynamic-Credentials-Redis.md)
- [Change Default ActiveMQ Passwords Using ConfigMap](Change-Default-ActiveMQ-Passwords.md)
