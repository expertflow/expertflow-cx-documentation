# CX Knowledgebase : Configure Vault for Redis Database Credentials

Check if **redis-crt** is present in vault namespace
[code] 
    kubectl get secrets -n vault
[/code]

If it’s not present, run the following command to copy it from ef-external namespace
[code] 
    kubectl get secret redis-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
[/code]

### Exec into the vault pod
[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

### Enable kv engine
[code] 
    vault secrets enable -path=kv kv-v2
[/code]

### Store Redis Credentials
[code] 
    vault kv put kv/redis \
        redis.username=superuser \
        redis.password=Expertflow464
[/code]

Verify
[code] 
    vault kv get kv/redis
[/code]

### Write policy for the role
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

### Attach policy to the role
[code] 
    vault write auth/approle/role/expertflow policies="ef-policy"
[/code]

### Exit pod
[code] 
    exit
[/code]
