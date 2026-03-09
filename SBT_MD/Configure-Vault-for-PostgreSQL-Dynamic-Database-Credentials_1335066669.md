# CX Knowledgebase : Configure Vault for PostgreSQL Dynamic Database Credentials

### Create role in postgres
[code] 
    k exec -it -n ef-external ef-postgresql-0 -- psql -U postgres
[/code]

You’ll be prompted to enter `the `password for the `postgres` user. The default password is `secretpassword`
[code] 
    \connect licenseManager
[/code]
[code] 
    -- 1. Ensure the group role exists
    DO $$
    BEGIN
       IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'app_users') THEN
          CREATE ROLE app_users;
       END IF;
    END
    $$;
    
    -- 2. Grant USAGE on the schema. This is the most likely missing piece.
    --    It allows the role to "see" objects inside the schema.
    GRANT USAGE ON SCHEMA public TO app_users;
    
    -- 3. Grant table permissions for the app_users role.
    --    This covers all tables that CURRENTLY exist in the schema.
    GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA public TO app_users;
    
    -- 4. IMPORTANT: Set default permissions for FUTURE tables.
    --    This ensures that if you create new tables later, app_users automatically gets access.
    --    NOTE: This only applies to tables created by the user running this command (postgres).
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE, TRUNCATE ON TABLES TO app_users;
    
    -- 5. (Optional but good practice) Grant permissions on sequences for future objects.
    ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT USAGE, SELECT ON SEQUENCES TO app_users;
    GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_users;
[/code]
[code] 
    exit
[/code]

### Exec into the vault pod  

[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

### Enable database engine

**Note:** Execute this below command only if it’s not executed already in Mongo guide, otherwise we can skip it.
[code] 
    vault secrets enable database
[/code]

### Configure PostgreSQL database plugin  

[code] 
    vault write database/config/postgres-database \
      plugin_name="postgresql-database-plugin" \
      allowed_roles="postgres-role" \
      connection_url="postgresql://{{username}}:{{password}}@ef-postgresql.ef-external.svc.cluster.local:5432/postgres?sslmode=verify-ca&sslrootcert=/vault/userconfig/postgres-ca/ca.crt&sslcert=/vault/userconfig/postgres-ca/tls.crt&sslkey=/vault/userconfig/postgres-ca/tls.key" \
      username="postgres" \
      password="secretpassword"
[/code]

### Set TTLs for database engine  

[code] 
    vault secrets tune -default-lease-ttl=87600h -max-lease-ttl=87600h database/
[/code]

### Configure role for PostgreSQL  

[code] 
    vault write database/roles/postgres-role \
        db_name=postgres-database \
        creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
                             GRANT app_users TO \"{{name}}\";" \
        revocation_statements="DROP ROLE IF EXISTS \"{{name}}\";" \
        default_ttl="87600h" \
        max_ttl="87600h"
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

## Configure PostgreSQL credentials in KV Secret for Keycloak:-  


Keycloak does not allow user credentials to be dynamically injected. So, as a workaround, we need to configure the default credentials of PostgreSQL in KV secret.

Run the following command to store the credentials in KV secret:-
[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

Enable kv path:-
[code] 
    vault secrets enable -path=secret kv
[/code]

Create a policy for Keycloak to access the secret:-
[code] 
    vault policy write keycloak-kv - <<EOF
    path "secret/vault-keycloak" {
      capabilities = ["read"]
    }
    EOF
[/code]

Attach the policy:-
[code] 
    vault write auth/kubernetes/role/database \
        bound_service_account_names=default \
        bound_service_account_namespaces=ef-external \
        policies=keycloak-kv \
        ttl=87600h
[/code]
[code] 
    vault kv put secret/vault-keycloak admin-password=<password for Keycloak admin user> sa-password=<password for postgresql sa user>
[/code]

exit the vault pod:-
[code] 
    exit
[/code]

Now run the following command in `kubernetes` directory:-
[code] 
    k apply -f pre-deployment/keycloak/keycloak-spc.yaml
[/code]

Once the SecretProviderClass is applied, restart the Keycloak pod using the following command:-
[code] 
    k delete pods -n ef-external <keycloak-pod>
[/code]

  


If you want to change the TTL value, you can follow the below steps

### How to change the TTL of credentials   
  
Exec into the vault pod
[code] 
    kubectl -n vault exec -it vault-0 -- sh
[/code]

### Update TTLs for engine
[code] 
    vault secrets tune -default-lease-ttl=87600h -max-lease-ttl=87600h database/
[/code]

### Update TTLs for PostgreSQL role
[code] 
    vault write database/roles/postgres-role \
        db_name=postgres-database \
        creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; \
                             GRANT app_users TO \"{{name}}\";" \
        revocation_statements="DROP ROLE IF EXISTS \"{{name}}\";" \
        default_ttl="87600h" \
        max_ttl="87600h"
[/code]
