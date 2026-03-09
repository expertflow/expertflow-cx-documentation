# CX Knowledgebase : PostgresQL DB Creation Guide

### 1\. Create the database in Postgres  
  
Follow this guide to create the db in Postgres already deployed in the `ef-external` namespace. Follow the steps below to create one.

  1. `exec` into the `ef-postgresql-0` pod in the `ef-external` namespace



[code] 
    kubectl -n ef-external exec -it ef-postgresql-0 -- bash
[/code]

  2. execute the environment setup for `ef-postgresql-0` ( Only needed when the postgresql is running in non-HA mode , like no pgpool and multiple replicas of postgresql are running )



[code] 
    /opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash
[/code]

  3. Log into Postgres using the following command



[code] 
    psql --host ef-postgresql -U sa postgres -p 5432
[/code]

  4. The system will ask for the password for the user `sa`. Enter the password, configured during deployment of Postgres. You should now be logged into the Postgres shell.

  5. Create the required database and extensions using the following commands.




the name of the db must be same as tenant name.
[code] 
    CREATE DATABASE <DBName>?;
    \c qm_db;
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
[/code]

  6. Then to exit from the shell



[code] 
    \q
    exit
    exit
[/code]
