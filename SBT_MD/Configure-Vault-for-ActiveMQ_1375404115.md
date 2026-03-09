# CX Knowledgebase : Configure Vault for ActiveMQ

This deployment requires redeployment of ActiveMQ

## **1\. Vault Setup**
[code] 
    cd CX-4.10.5/kubernetes
[/code]
[code] 
    helm repo add secrets-store-csi-driver https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts
    helm install csi-secrets-store secrets-store-csi-driver/secrets-store-csi-driver --namespace vault
[/code]
[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

Create a KV-v2 secret in Vault: 

Note: If its not already exists, then create path using below command.
[code] 
    vault secrets enable -path=kv kv-v2
[/code]
[code] 
    vault kv put kv/activemq/broker \
        activemq.username=admin \
        activemq.password=Expertflow123
[/code]

Verify:
[code] 
    vault kv get kv/activemq/broker
[/code]

Write policy for the role
[code] 
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
[/code]

Attach policy to the role
[code] 
    vault write auth/approle/role/expertflow policies="ef-policy"
[/code]

## **2\. Vault Role for Kubernetes Authentication**

Create a policy for Kubernetes role in Vault:
[code] 
    vault policy write activemq-kv - <<EOF
    path "kv/data/activemq/broker" {
      capabilities = ["read"]
    }
    EOF
[/code]

Create a Kubernetes role in Vault:
[code] 
    vault auth enable kubernetes
[/code]
[code] 
    vault write auth/kubernetes/config \
        token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
        kubernetes_host="https://kubernetes.default.svc:443" \
        kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
[/code]
[code] 
    vault write auth/kubernetes/role/expertflow \
        bound_service_account_names=default \
        bound_service_account_namespaces=ef-external \
        policies=activemq-kv \
        ttl=87600h
[/code]
[code] 
    exit
[/code]

## 3\. Apply SecretProviderClass, ClusterRole and ClusterRoleBinding
[code] 
    kubectl apply -f pre-deployment/activemq-vault
[/code]

## 4\. Deploy / Restart Pods
[code] 
    kubectl delete pod -n vault <vault-csi-provider-pod>
[/code]
[code] 
    # Restart ActiveMQ pod 
    kubectl delete pod -n ef-external <activemq-pod>
[/code]
