# CX Knowledgebase : Encryption at Rest - Configuration Guide

This guide helps operational admins to enable, maintain, or troubleshoot the **Encryption at Rest** feature on Expertflow CX.****

Our system uses **AES256-GCM96** encryption to protect sensitive data when it's stored (at rest). The integrated encryption library handles **both the encryption and decryption** of data based on the defined schema.

Currently, the****`Conversation Manager` microservice is the primary component with integrated support for this encryption at rest mechanism. This guide focuses specifically on configuring the `Conversation Manager` to utilize this security feature.

## **Encryption Scope (Conversation Manager)**

For the `Conversation Manager`, encryption at rest applies to specific fields within the following MongoDB collections:

  * `CustomerTopicEvents` Collection:

    * `cimEvent.data.body.markdownText`

    * `cimEvent.data.body.jsonNode`

    * (Encryption applies only if `cimEvent.name` is "BOT_MESSAGE", "CUSTOMER_MESSAGE", or "AGENT_MESSAGE")

  * `ConversationActivities` Collection:

    * `activity.data.body.markdownText`

    * `cimEvent.data.body.jsonNode`

    * (Encryption applies only if `activity.name` is "BOT_MESSAGE", "CUSTOMER_MESSAGE", or "AGENT_MESSAGE")




For a detailed explanation of the encryption schema and its logic, refer to the [Encryption Schema Guide](https://expertflow-docs.atlassian.net/wiki/x/EgBJPQ).

## **Prerequisites**

Before enabling encryption for the `Conversation Manager`, ensure the following are already in place:

  * **Vault Configuration:** Vault must be fully configured for encryption. This includes setting up an **AppRole** for the `Conversation Manager` and defining the necessary **Transit secrets engine paths** within Vault. For detailed instructions, refer to the [Configuring Vault for Encryption](https://expertflow-docs.atlassian.net/wiki/x/ZoDJOQ)

  * **Encryption Schema Applied:** A specific encryption schema for the `Conversation Manager` must be defined and applied to Vault as a `configMap`. The name of this `configMap` is critical and must match the configuration in the service's deployment.

  * **TLS Certificates:** The required TLS certificates for secure communication with Vault must be available as Kubernetes `secrets` (typically `tls-ca` and `tls-server-client`).




## **1\. Core Configuration for Conversation Manager (Verification)**

Enabling encryption for the `Conversation Manager` requires verifying that its deployment configuration (e.g., in `values.yaml`) has the correct environment variables and mounted volumes in place.

### **Environment Variables (Verify Existing)**

These variables control the encryption functionality and Vault authentication.

Environment Variable| Action for Operations  
---|---  
`ENABLE_ENCRYPTION`| **Set to**`"true"` to activate encryption. This is the main switch.  
`VAULT_ROLE_ID`| Ensure this fetches its value from the `vault-approle-secret` (key: `ROLE_ID`).  
`VAULT_SECRET_ID`| Ensure this fetches its value from the `vault-approle-secret` (key: `SECRET_ID`).  
`VAULT_TRANSIT_PATH`| Verify this fetches its value from the `vault-approle-secret` (key: `TRANSIT_PATH`).  
`VAULT_TRANSIT_KEY`| Verify this fetches its value from the `vault-approle-secret` (key: `TRANSIT_KEY`).  
`ENCRYPTION_SCHEMA_PATH`| Set its value to `"file:/encryption/encryption-schema.json"`.  
  
### **Mounted Volumes (Verify Existing)**

These Kubernetes volumes provide certificates and the encryption schema to the `Conversation Manager` pod.

**Example extraVolumes section:**

(Defines the sources of the volumes)
[code] 
    extraVolumes:
      - name: tls-ca
        secret:
          secretName: tls-ca
      - name: tls-server-client
        secret:
          secretName: tls-server-client
      - name: conversation-manager-encryption-schema # Must match the applied ConfigMap name
        configMap:
          name: conversation-manager-encryption-schema
[/code]

**Example extraVolumeMounts section:**

(Defines where these volumes are mounted inside the container)
[code] 
    extraVolumeMounts:
      - name: tls-ca
        mountPath: /tls-ca
      - name: tls-server-client
        mountPath: /tls-server-client
      - name: conversation-manager-encryption-schema
        mountPath: /encryption # The encryption schema will be available at /encryption/encryption-schema.json
[/code]

### **Vault Connection Variables (**`efConnectionVars`) **(Verify Existing)**

These define the internal connection details for Vault. Ensure these are correctly set in your `Conversation Manager`'s configuration:

  * `VAULT_URI: https://vault.vault.svc.cluster.local:8200`

  * `VAULT_CLIENT_CERT: /tls-server-client/tls.crt`

  * `VAULT_CLIENT_KEY: /tls-server-client/tls.key`

  * `VAULT_CA_CERT: /tls-ca/tls.crt`




* * *

## **2\. Enabling and Disabling Encryption**

### **To Enable Encryption for Conversation Manager**

  1. **Review Prerequisites:** Confirm all listed prerequisites are met.

  2. **Edit Deployment:** Access the `Conversation Manager`'s deployment configuration (e.g., in `values.yaml`).

  3. **Set Encryption Toggle:** Change the `ENABLE_ENCRYPTION` environment variable's value from `"false"` to `"true"`.

  4. **Apply Changes:** Apply the updated deployment configuration. This will trigger a rolling update of the `Conversation Manager` pods.

  5. **Monitor:** After the update, closely monitor the `Conversation Manager`'s logs and health metrics to ensure successful startup and operation.




### **To Disable Encryption for Conversation Manager**

  1. **Edit Deployment:** Access the `Conversation Manager`'s deployment configuration.

  2. **Set Encryption Toggle:** Change the `ENABLE_ENCRYPTION` environment variable's value from `"true"` back to `"false"`.

  3. **Apply Changes:** Apply the updated configuration.




**Important:** Setting `ENABLE_ENCRYPTION` to `"false"` will disable _both_ encryption for new data and decryption for existing encrypted data. This will result in the inability to read previously encrypted information. Only disable if absolutely necessary and with full understanding of the impact on data readability.

* * *

## **3\. Post-Enablement Operations and Maintenance**

These procedures are crucial for ongoing security and disaster recovery when encryption is enabled.

### **Key Rotation**

Regular key rotation is a security best practice. This process involves generating a new version of the encryption key in Vault and instructing the `Conversation Manager` to reload the new key for future encryption operations.

  1. **Rotate Key in Vault:**

Execute the following command on a Vault pod to rotate the encryption key. This creates a new version of the key.
[code] kubectl exec -it -n vault vault-0 -- vault write -f transit/keys/ef-encryption/rotate
[/code]

  2. **Reload Keys in Conversation Manager:**

After rotating the key in Vault, instruct the Conversation Manager to reload the new key version using its API. This ensures the service uses the latest key for new encryption/decryption operations.
[code] GET https://<FQDN>/conversation-manager/reload-keys
[/code]

_Replace_`<FQDN>`_with the fully qualified domain name or service endpoint of your Conversation Manager._




### **Vault Backup and Restore**

**Strongly Recommended:** Regularly take snapshots of your Vault data. These backups are critical for disaster recovery and restoring access to your encryption keys, which are essential for decrypting your data.

**CRITICAL WARNING:** **If Vault snapshots, their associated unseal keys, and critical access tokens (like the root token) are permanently lost, any encrypted data will become permanently unrecoverable and inaccessible.**

### **Taking Backups**

  1. **Take Backup Snapshot:**

Execute this command on a Vault pod to create a snapshot of Vault's Raft storage.
[code] kubectl exec -it -n vault vault-0 -- vault operator raft snapshot save /vault/data/raft/snapshots/backup.snap
[/code]

  2. **Copy Backup to Local Machine:**

After creating the snapshot, immediately copy it from the Vault pod to a secure local or remote backup location.
[code] kubectl cp -n vault vault-0:/vault/data/raft/snapshots/backup.snap ~/backups/vault/raft/snapshots/backup.snap
[/code]




### **Restoring Backups**

**Caution:** Restoring a Vault snapshot is a critical operation that should only be performed in a disaster recovery scenario and with extreme care. It will overwrite Vault's current state.

**Important Note on Restore:** After restoring a snapshot, Vault will revert to using its **original unseal keys and root token** that were active when the snapshot was taken. Ensure you have access to these credentials to unseal Vault and regain full access.

  1. **Copy Backup from Local Machine to Vault Pod:**

Copy the .snap file from your local backup location back to the Vault pod.
[code] kubectl cp -n vault ~/backups/vault/raft/snapshots/backup.snap vault-0:/vault/data/raft/snapshots/backup.snap
[/code]

  2. **Restore Backup Snapshot:**

Execute this command on the Vault pod to restore from the copied snapshot.
[code] kubectl exec -it -n vault vault-0 -- vault operator raft snapshot restore /vault/data/raft/snapshots/backup.snap
[/code]




## **4\. Troubleshooting**

  * `Conversation Manager` fails to start:

    * Check `Conversation Manager` logs for Vault connectivity errors (e.g., certificate issues, AppRole authentication failures).

    * Verify the `VAULT_ROLE_ID`, `VAULT_SECRET_ID`, `VAULT_TRANSIT_PATH`, and `VAULT_TRANSIT_KEY` are correctly configured and have the necessary Vault permissions.

    * Ensure the `conversation-manager-encryption-schema` `configMap` and TLS `secrets` (and their corresponding mounts) are correctly named and accessible.

  * **Data not encrypting:** Confirm `ENABLE_ENCRYPTION` is explicitly set to `"true"`.

  * **Decryption errors:** If the `Conversation Manager` cannot decrypt existing data (and `ENABLE_ENCRYPTION` is `"true"`), **immediately escalate to the development and security teams.** This is a critical issue indicating potential key or schema problems in Vault.



