# CX Knowledgebase : Configuring Vault for Encryption

Use the following guide to initialize and unseal the vault: [Initializing and unsealing the vault](https://expertflow-docs.atlassian.net/wiki/x/eQCLDw?atlOrigin=eyJpIjoiNDg3YzMwYzIwNzFkNDRiNDk2YWRhN2IzNmFiM2QxOGEiLCJwIjoiYyJ9%5D**)

Below we're using the pod **vault-0** from the cluster as it is usually the active pod in the cluster. Make sure to replace that in the commands with the vault pod that is the active one. To check if the pod is active, use this command:
[code] 
    kubectl exec -it -n vault vault-0 -- vault status
[/code]

**Example output**
[code] 
    Key                     Value
    ---                     -----
    Seal Type               shamir
    Initialized             true
    Sealed                  false
    Total Shares            5
    Threshold               3
    Version                 1.13.3
    Build Date              2023-06-06T18:12:37Z
    Storage Type            raft
    Cluster Name            vault-integrated-storage
    Cluster ID              97a5bd70-2dcb-0457-1bb8-96db310f5c5f
    HA Enabled              true
    HA Cluster              <https://vault-0.vault-internal:8201>
    HA Mode                 active
    Active Since            2025-02-11T10:33:48.686231049Z
    Raft Committed Index    133
    Raft Applied Index      133
[/code]

Here, **HA Mode** is active, and if it is standby then that pod is not the active one. 

  1. **Login into Vault** (Using the password as Initial Root Token that you received along with 5 secret keys in the nested guide mentioned above)



[code] 
    kubectl exec -it -n vault vault-0 -- vault login
[/code]

  2. **Enable Transit Secrets Engine**



[code] 
    kubectl exec -it -n vault vault-0 -- vault secrets enable transit
[/code]

  3. **Create an Encryption Key**



[code] 
    kubectl exec -it -n vault vault-0 -- vault write -f transit/keys/ef-encryption-key exportable=true
[/code]

  4. **Enable AppRole Authentication (if not already enabled)**




Check if AppRole already exists  
kubectl exec -it vault-0 -n vault -- /bin/sh  
vault auth list  
You’ll see something like:

Path Type Accessor Description  
approle/ approle auth_approle_xxxxx n/a  
token/ token auth_token_xxxxx n/a
[code] 
    kubectl exec -it -n vault vault-0 -- vault auth enable approle
[/code]

  5. **Create an AppRole (if not already created)**



[code] 
    kubectl exec -it -n vault vault-0 -- vault write sys/auth/approle/tune max_lease_ttl=87600h
[/code]
[code] 
    kubectl exec -it -n vault vault-0 -- sh -c 'vault write auth/approle/role/expertflow \
        token_ttl=87600h \
        token_max_ttl=87600h'
[/code]

  6. **Create a Policy**



[code] 
    kubectl exec -it -n vault vault-0 -- sh -c 'vault policy write ef-policy - <<EOF
    path "/transit/export/*" {
      capabilities = ["read"]
    }
    EOF'
[/code]

  7. **Attach the Policy to an AppRole**



[code] 
    kubectl exec -it -n vault vault-0 -- vault write auth/approle/role/expertflow policies="ef-policy"
[/code]

  8. **Create secret containing role-id, secret-id, path and encryption-key name**



[code] 
    ROLE_ID=$(kubectl exec -n vault vault-0 -- vault read -field=role_id auth/approle/role/expertflow/role-id) && \
    SECRET_ID=$(kubectl exec -n vault vault-0 -- vault write -f auth/approle/role/expertflow/secret-id | grep "secret_id " | awk '{print $2}') && \
    kubectl create secret generic vault-approle-secret -n expertflow \
      --from-literal=ROLE_ID="$ROLE_ID" \
      --from-literal=SECRET_ID="$SECRET_ID" \
      --from-literal=TRANSIT_PATH="transit" \
      --from-literal=TRANSIT_KEY="ef-encryption-key" \
      --save-config --dry-run=client -o yaml | kubectl apply -f -
[/code]

  9. **Copy Vault TLS secrets to Expertflow namespace**



[code] 
    kubectl get secret tls-ca -n vault  -o yaml | sed 's/namespace: vault/namespace: expertflow/' | kubectl create -f -
    kubectl get secret tls-server-client -n vault  -o yaml | sed 's/namespace: vault/namespace: expertflow/' | kubectl create -f -
[/code]

  10. **Apply Encryption Schema**



[code] 
    kubectl create configmap -n expertflow conversation-manager-encryption-schema --from-file=pre-deployment/conversation-manager/encryption/encryption-schema.json
[/code]

The above encryption schema configmap is applied for the conversation manager. You can change the path and name to apply a different schema to another component.

  10. **Deploy/upgrade the solution**




# Post Configuration Stuff (No need to do right away)

## Key rotation

  11. **Rotate key in vault**



[code] 
    kubectl exec -it -n vault vault-0 -- vault write -f transit/keys/ef-encryption/rotate
[/code]

  12. **Reload keys in the component using API**



[code] 
    GET <https://<FQDN>>/conversation-manager/reload-keys
[/code]

## Taking Backups

  13. **Taking backup snapshot**



[code] 
    kubectl exec -it -n vault vault-0 -- vault operator raft snapshot save /vault/data/raft/snapshots/backup.snap
[/code]

  14. **Copy backup from the vault pod to local machine**



[code] 
    kubectl cp -n vault vault-0:/vault/data/raft/snapshots/backup.snap ~/backups/vault/raft/snapshots/backup.snap
[/code]

## Restoring Backups

  15. **Copy backup from local machine to the vault pod**



[code] 
    kubectl cp -n vault ~/backups/vault/raft/snapshots/backup.snap vault-0:/vault/data/raft/snapshots/backup.snap
[/code]

  16. **Restore backup snapshot**



[code] 
    kubectl exec -it -n vault vault-0 -- vault operator raft snapshot restore /vault/data/raft/snapshots/backup.snap
[/code]
