---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Migrate EF IAM Users to Different Instances or Realms

This guide provides step-by-step instructions for exporting users from a source EF IAM (Keycloak) instance and importing them into a target realm.

## Overview
The migration process involves extracting user data from the source Kubernetes environment, cleaning the JSON data for compatibility, and performing a partial import at the destination.

## Prerequisites
- Access to the source and target EF IAM (Keycloak) deployments.
- `kubectl` configured for the source cluster.
- Administrative privileges on the local machine and target Keycloak instance.
- `jq` installed for JSON processing.

## Step 1: Install jq
Ensure `jq` is installed on your processing machine:
- **Ubuntu/Debian**: `sudo apt-get install jq`
- **CentOS/RHEL**: `sudo yum install epel-release && sudo yum install jq`

## Step 2: Export Users from Source
Connect to the Keycloak pod and run the export command:
```bash
kubectl exec -it -n <Namespace> <Keycloak-Pod> -- /bin/bash
/opt/bitnami/keycloak/bin/kc.sh export --realm <Realm-Name> --users different_files --users-per-file 10000 --dir /tmp/
```
Verify that `<realm-name>-users-0.json` exists in `/tmp/`.

## Step 3: Copy and Clean User Data
Copy the file to your local machine:
```bash
kubectl cp -n <Namespace> <Pod-Name>:/tmp/<realm-name>-users-0.json ./users-export.json
```

Use `jq` to remove incompatible fields (IDs, timestamps, and credential dates):
```bash
jq '.users |= map(del(.id, .createdTimestamp) | if has("credentials") then .credentials |= map(del(.id, .createdDate)) else . end) | del(.realm)' users-export.json > cleaned-users.json
```

## Step 4: Import to Target Realm
1. Log in to the **Target Keycloak Admin Console**.
2. Select your target **Realm**.
3. Go to **Realm Settings** -> **Action** (top-right) -> **Partial Import**.
4. Upload `cleaned-users.json`.
5. Select **Overwrite** if users already exist.
6. Click **Import**.

## Step 5: Verification
- Navigate to **Users** and verify the list.
- Test login functionality for a few imported accounts to ensure data integrity.
