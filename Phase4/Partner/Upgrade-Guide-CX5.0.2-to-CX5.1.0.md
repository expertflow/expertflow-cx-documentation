---
title: "Upgrade Guide: CX 5.0.2 to CX 5.1.0"
summary: "Step-by-step upgrade guide for ExpertFlow CX from version 5.0.2 to 5.1.0 — covering Helm repo update, CX 5.1.0 repository clone, Transflux setup, APISIX, Vault reconfiguration, Redis, ActiveMQ, Keycloak, AgentDesk, Core, Channels, QM, Campaigns, and Fluent-Bit chart deployments."
audience: [partner]
product-area: [platform]
doc-type: how-to
difficulty: advanced
keywords: ["CX 5.1.0 upgrade", "ExpertFlow upgrade 5.0.2 5.1.0", "CX upgrade Helm 5.1.0", "upgrade guide CX 5.1.0", "Helm upgrade CX 5.1.0"]
aliases: ["upgrade CX 5.1.0", "5.0.2 to 5.1.0 CX upgrade", "CX 5.1.0 deployment upgrade"]
last-updated: 2026-03-10
---

# Upgrade Guide: CX 5.0.2 to CX 5.1.0

> Before upgrading, ensure the system is idle — all agents must be logged out from the Agent Desk.

For guidelines on custom `values.yaml` layering, refer to the **CX Helm Chart Custom Configuration Strategy** guide.

---

## Step 1: Update Helm Repository

```bash
helm repo update expertflow
```

---

## Step 2: Clone the CX 5.1.0 Repository

```bash
mkdir CX-5.1.0
cd CX-5.1.0
git clone -b CX-4.10.x_MergedInto-CX-5.0 \
  https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git $HOME/CX-5.1.0
cd ../
```

---

## Step 3: Set Up Transflux

Follow the Transflux setup guide for this release before proceeding.

---

## Step 4: Deploy APISIX

```bash
helm show values expertflow/apisix --version 5.1.0-rc.1 > helm-values/apisix-custom-values.yaml
```

Edit `helm-values/apisix-custom-values.yaml`:

```yaml
global:
  ingressRouter: "*.expertflow.com"   # Use * for MTT; replace with FQDN for on-premise
  ingressClassName: "nginx"
  ingressTlsCertName: "ef-ingress-tls-secret"
```

Deploy:

```bash
helm upgrade --install --namespace ef-external \
  --values helm-values/apisix-custom-values.yaml \
  apisix expertflow/apisix --version 5.1.0-rc.1

kubectl -n ef-external get deploy
```

---

## Step 5: Configure Vault Secrets

Copy TLS secrets between namespaces:

```bash
kubectl get secret tls-ca -n vault -o yaml \
  | sed 's/namespace: vault/namespace: ef-external/' | kubectl create -f -
kubectl get secret tls-server-client -n vault -o yaml \
  | sed 's/namespace: vault/namespace: ef-external/' | kubectl create -f -
kubectl get secret tls-server-vault -n vault -o yaml \
  | sed 's/namespace: vault/namespace: ef-external/' | kubectl create -f -
kubectl get secret expertflow-reg-cred -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
kubectl get secret redis-crt -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
kubectl get secret ef-postgresql-crt -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
kubectl get secret activemq-tls -n ef-external -o yaml \
  | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
```

Copy pre-deployment resources from the new release:

```bash
# Copy activemq-vault directory
cp -r CX-5.1.0/kubernetes/pre-deployment/activemq-vault ./kubernetes/pre-deployment/

# Copy service-based-accounts directory
cp -r CX-5.1.0/kubernetes/pre-deployment/service-based-accounts ./kubernetes/pre-deployment/

# Copy keycloak-spc.yaml
cp CX-5.1.0/kubernetes/pre-deployment/keycloak/keycloak-spc.yaml ./kubernetes/pre-deployment/keycloak/
```

### Verify MongoDB Vault TTL

Check the current MongoDB role TTL:

```bash
kubectl -n vault exec -it vault-0 -- vault read database/roles/mongodb-role
```

If `default_ttl` is less than `87600h`, update it. See [Vault Dynamic Credentials — MongoDB](../Solution_Admin/Vault-Dynamic-Credentials-MongoDB.md).

### Configure Vault for all components

Follow the Vault configuration guides for:
- **MongoDB** — [Vault Dynamic Credentials — MongoDB](../Solution_Admin/Vault-Dynamic-Credentials-MongoDB.md)
- **Redis** — [Vault Dynamic Credentials — Redis](../Solution_Admin/Vault-Dynamic-Credentials-Redis.md)
- **ActiveMQ** — [Vault Dynamic Credentials — ActiveMQ](../Solution_Admin/Vault-Dynamic-Credentials-ActiveMQ.md)

---

## Step 6: Deploy Redis

```bash
helm show values expertflow/redis --version 5.1.0-rc.1 > helm-values/ef-redis-custom-values.yaml
```

Edit `helm-values/ef-redis-custom-values.yaml`:

```yaml
acl:
  users:
    password: "Expertflow464"   # Update to match your requirements
```

Deploy:

```bash
helm upgrade --install=true --namespace=ef-external \
  --values=helm-values/ef-redis-custom-values.yaml \
  redis expertflow/redis --version 5.1.0-rc.1
```

---

## Step 7: Deploy Vault

```bash
helm uninstall -n vault vault

helm show values expertflow/vault --version 5.1.0-rc.1 > helm-values/ef-vault-custom-values.yaml

helm upgrade --install --namespace vault --create-namespace vault \
  --debug --values helm-values/ef-vault-custom-values.yaml \
  expertflow/vault --version 5.1.0-rc.1
```

Follow only the **unsealing steps** from the Vault initialization guide. Then log in:

```bash
kubectl -n vault exec -it vault-0 -- vault login <root-token>
```

---

## Step 8: Deploy ActiveMQ

```bash
helm show values expertflow/activemq --version 5.1.0-rc.1 > helm-values/ef-activemq-custom-values.yaml

helm upgrade --install=true --namespace=ef-external \
  --values=helm-values/ef-activemq-custom-values.yaml \
  activemq expertflow/activemq --version 5.1.0-rc.1
```

---

## Step 9: Deploy Keycloak

```bash
helm show values expertflow/keycloak --version 5.1.0-rc.1 > helm-values/ef-keycloak-custom-values.yaml
```

Edit `helm-values/ef-keycloak-custom-values.yaml`:

```yaml
global:
  ingressRouter: <DEFAULT-FQDN>
```

Deploy:

```bash
helm upgrade --install=true --debug --namespace=ef-external \
  --values=helm-values/ef-keycloak-custom-values.yaml \
  keycloak expertflow/keycloak --version 5.1.0-rc.1
```

---

## Step 10: Deploy AgentDesk

Update translation ConfigMaps:

```bash
# Unified Agent translations
cp -r CX-5.1.0/kubernetes/pre-deployment/app-translations/unified-agent/i18n/ \
  pre-deployment/app-translations/unified-agent/
kubectl delete cm ef-app-translations-cm -n expertflow
kubectl -n expertflow create configmap ef-app-translations-cm \
  --from-file=pre-deployment/app-translations/unified-agent/i18n/

# Customer Widget translations
cp -r CX-5.1.0/kubernetes/pre-deployment/app-translations/customer-widget/i18n/ \
  pre-deployment/app-translations/customer-widget/
kubectl delete cm ef-widget-translations-cm -n expertflow
kubectl -n expertflow create configmap ef-widget-translations-cm \
  --from-file=pre-deployment/app-translations/customer-widget/i18n/
```

Deploy:

```bash
helm upgrade --install --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" \
  cx-agent-desk --debug \
  --values helm-values/cx-agent-desk-custom-values.yaml \
  expertflow/agent-desk --version 5.1.0-rc.1
```

---

## Step 11: Prepare Conversation Studio

A new **AGENT_STATE_CHANGED** flow has been added for Conversation Re-Routing on Agent State Change.

> **Back up your existing Conversation Studio flows before making any changes.**

**If using custom flows:** Manually add the AGENT_STATE_CHANGED flow changes after deploying the Core chart. Refer to the Conversation Studio Default Flows documentation (section: "Agent State Changed").

**If using default flows only:**

```bash
kubectl delete -n expertflow statefulset ef-cx-conversation-studio
kubectl delete -n expertflow pvc conversation-studio-flow-vol-ef-cx-conversation-studio-0
```

---

## Step 12: Deploy Core

```bash
# Copy Conversation Manager GraphQL schemas
cp -r CX-5.1.0/kubernetes/pre-deployment/conversation-manager/graphql/ \
  pre-deployment/conversation-manager/

kubectl delete configmap -n expertflow conversation-manager-graphql-schemas
kubectl create configmap -n expertflow conversation-manager-graphql-schemas \
  --from-file=./pre-deployment/conversation-manager/graphql/schemas

kubectl delete configmap -n expertflow conversation-manager-graphql-mongodb-rules
kubectl create configmap -n expertflow conversation-manager-graphql-mongodb-rules \
  --from-file=./pre-deployment/conversation-manager/graphql/graphql-mongodb-rules.json

# Deploy Core
helm upgrade --install --namespace expertflow --create-namespace ef-cx \
  --debug --values helm-values/ef-cx-custom-values.yaml \
  expertflow/cx --version 5.1.0-rc.1
```

---

## Step 13: Deploy Channels

```bash
helm upgrade --install --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" --debug \
  cx-channels --values helm-values/cx-channels-custom-values.yaml \
  expertflow/channels --version 5.1.0-rc.1
```

---

## Step 14: Deploy QM

```bash
helm upgrade --install --namespace=expertflow \
  --set global.efCxReleaseName="ef-cx" qm --debug \
  --values=helm-values/cx-qm-custom-values.yaml \
  expertflow/qm --version 5.1.0-rc.1
```

---

## Step 15: Deploy Campaigns

```bash
helm upgrade --install --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" cx-campaigns --debug \
  --values helm-values/cx-campaigns-custom-values.yaml \
  expertflow/campaigns --version 5.1.0-rc.1
```

---

## Step 16: Deploy Fluent-Bit

```bash
helm show values expertflow/fluent-bit --version 5.1.0-rc.1 \
  > helm-values/cx-fluent-bit-custom-values.yaml

helm upgrade --install --namespace ef-external \
  --set global.efCxReleaseName="ef-cx" cx-fluent-bit --debug \
  --values helm-values/cx-fluent-bit-custom-values.yaml \
  expertflow/fluent-bit --version 5.1.0-rc.1
```

---

## Voice Connector

To upgrade the Voice Connector, follow the CX Voice Upgrade guide using version `5.1.0`.

---

## Related Articles

- [Upgrade Guide: CX 5.1.0 to CX 5.2.0](Upgrade-Guide-CX5.1.0-to-CX5.2.0.md)
- [Vault Dynamic Credentials — MongoDB](../Solution_Admin/Vault-Dynamic-Credentials-MongoDB.md)
- [Vault Dynamic Credentials — Redis](../Solution_Admin/Vault-Dynamic-Credentials-Redis.md)
- [Vault Dynamic Credentials — ActiveMQ](../Solution_Admin/Vault-Dynamic-Credentials-ActiveMQ.md)
