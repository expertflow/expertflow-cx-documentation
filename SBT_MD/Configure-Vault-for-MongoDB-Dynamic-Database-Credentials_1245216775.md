# CX Knowledgebase : Configure Vault for MongoDB Dynamic Database Credentials

Check if all the vault pods are unsealed
[code] 
    kubectl -n vault exec -it vault-0 -- vault status
    kubectl -n vault exec -it vault-1 -- vault status
    kubectl -n vault exec -it vault-2 -- vault status
    kubectl -n vault exec -it vault-3 -- vault status
    kubectl -n vault exec -it vault-4 -- vault status
[/code]

If the output says `Sealed true` then unseal them using [this guide](https://expertflow-docs.atlassian.net/wiki/x/eQCLDw). Do not follow the initialization steps, as those are required only for the first time when the vault is deployed.

Check if **mongo-mongodb-ca** is present in vault namespace
[code] 
    kubectl get secrets -n vault
[/code]

If it’s not present, run the following command to copy it from ef-external namespace
[code] 
    kubectl get secret mongo-mongodb-ca -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
[/code]

Exec into the vault pod
[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

Login using root token
[code] 
    vault login
[/code]

Enable database engine
[code] 
    vault secrets enable database
[/code]

Configure mongoDB database plugin
[code] 
    vault write database/config/mongodb-database \
      plugin_name="mongodb-database-plugin" \
      allowed_roles="mongodb-role" \
      username="root" \
      password="Expertflow123" \
      connection_url="mongodb://{{username}}:{{password}}@mongo-mongodb.ef-external.svc.cluster.local:27017/?authSource=admin&tls=true&tlsCAFile=/vault/userconfig/mongo-mongodb-ca/mongodb-ca-cert&tlsCertificateKeyFile=/vault/userconfig/mongo-mongodb-ca/client-pem&tlsAllowInvalidHostnames=true"
[/code]

Set TTLs for database engine (by default they are at 768h), if you want the role TTLs to be greater than **768h**.
[code] 
    vault secrets tune -default-lease-ttl=87600h -max-lease-ttl=87600h database/
[/code]

Configure role for mongoDB
[code] 
    vault write database/roles/mongodb-role \
        db_name=mongodb-database \
        creation_statements='{ "db": "admin", "roles": [{ "role": "root", "db": "admin" }] }' \
        default_ttl="87600h" \
        max_ttl="87600h"
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
    EOF
[/code]

Attach policy to the role
[code] 
    vault write auth/approle/role/expertflow policies="ef-policy"
[/code]
[code] 
    exit
[/code]

##   
How to change TTL of credentials

Exec into the vault pod
[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

Set TTLs for database engine (by default they are at 768h), if you want the role TTLs to be greater than **768h**.
[code] 
    vault secrets tune -default-lease-ttl=87600h -max-lease-ttl=87600h database/
[/code]

Change **default_ttl** and **max_ttl** for the role**** in the below command:
[code] 
    vault write database/roles/mongodb-role \
        db_name=mongodb-database \
        creation_statements='{ "db": "admin", "roles": [{ "role": "root", "db": "admin" }] }' \
        default_ttl="87600h" \
        max_ttl="87600h"
[/code]
