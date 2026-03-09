# CX Knowledgebase : Tenant Creation for Multi-tenant CX- To be removed

**Non-MTT Components (Per Tenant)**  
To deploy **CX Campaigns Studio, Conversation Studio, and QM Backend** for the new tenant, use the `mtt-single`**** Helm chart.  
You have to disable Campaigns Studio, Conversation Studio & QM-Backend from existing charts or custom values, by first setting the `enabled` key to `false` for these components in their respective charts.
[code] 
    enabled : false
[/code]

For QM Backend, we need to manually create the PostgreSQL database first. The steps to create the database are mentioned in this [guide](PostgresQL-DB-Creation-Guide_955154451.html).

First you need to create the namespace for new tenant
[code] 
    kubectl create namespace <tenant-name>
[/code]

You have to transfer the Mongo, Redis, PostgreSQL Certificates from the ef-external namespace to newly created tenant namespace.   
please change <namespace> with the specific tenant namespace.
[code] 
    kubectl get secret mongo-mongodb-ca -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: <namespace>/' | kubectl create -f -
    kubectl get secret redis-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: <namespace>/' | kubectl create -f -
    kubectl get secret ef-postgresql-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: <namespace>/' | kubectl create -f -
    kubectl get configmap ef-logback-cm -n expertflow  -o yaml | sed 's/namespace: expertflow/namespace: <namespace>/' | kubectl create -f -
    kubectl get configmap ef-cx-efconnections-cm -n expertflow  -o yaml | sed 's/namespace: expertflow/namespace: <namespace>/' | kubectl create -f -
    kubectl get secret ef-gitlab-secret -n expertflow  -o yaml | sed 's/namespace: expertflow/namespace: <namespace>/' | kubectl create -f -
[/code]

### Customise `values.yaml`

![](images/icons/grey_arrow_down.png)Customise values.yaml

You must first edit `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to edit a new file:
[code] 
    vi helm/MTT-single/values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

Update namespace and apply MTT-single helm chart
[code] 
    helm upgrade --install --namespace <tenant-ns>  --debug  <tenant-id> --values=helm/MTT-single/values.yaml  helm/MTT-single
[/code]

### CX Reporting

#### Configure TLS connection for MySQL

Each tenant has their dedicated namespace where the respective commands will be deployed.

Get the MySQL `key-store (.jsk)` & `certificate(.cert)` files for mysql. The `.jsk` file is required for configuration of the reporting connector, whereas the `.cert` file is required for Apache Superset SSL configuration. Skeleton Project (cim-solution) already contains the default .jks files in the keystore directory. Replace the` mykeystore.jks `file acquired with the actual file in `cim-solution/kubernetes/pre-deployment/reportingConnector/keystore/ `directory.

Create `keystore.jks` used for MySQL TLS 
[code] 
    kubectl create configmap -n <tenant-namespace> ef-reporting-connector-keystore-cm --from-file=pre-deployment/reportingConnector/keystore/mykeystore.jks
[/code]

Create directory with <`tenant_config_directory`> in `pre-deployment/reportingConnector/<tenant_config_directory>` and place `reporting-connector.conf` specific to each tenant and set the `mysql_dbms_additional_params`**** value as shown below.
[code] 
    mkdir pre-deployment/reportingConnector/<tenant_config_directory>
[/code]
[code] 
    mysql_dbms_additional_params=noDatetimeStringSync=true&useSSL=true&requireSSL=true&trustServerCertificate=true&clientCertificateKeyStoreUrl=file:///root/config/certs/mykeystore.jks&clientCertificateKeyStorePassword={KEYSTORE_PASSWORD}
     
    # Replace the {KEYSTORE_PASSWORD} with your original keystore password. Use "changeit" in case of default password.
[/code]

#### Reporting Connector Config-Map Setup

For database creation on MTT, refer to the pre-requisite of [EF Data Platform Guide](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/1283588097/Data+Platform+CX)

Create the database in target Database Management System using the scripts from `CX-4.10/kubernetes/pre-deployment/reportingConnector/dbScripts/dbcreation` directory. Name of each database will be varied from tenant to tenant.

Update the config present in `pre-deployment/reportingConnector/<tenant_config_directory>/reporting-connector.conf` as per the below mentioned parameters 

**Parameter**| **Requirement**  
---|---  
fqdn| Use (FQDN) of the CX Solution specific to each tenant.  
svc_name| <http://ef-cx-historical-reports-svc.expertflow.svc.cluster.local:8081>  
tenant_id| unique identifier for each tenantIn case of MTT, the tenant_id will be the name of tenant, for on-prem, tenant_id will be expertflow  
browser_language|  en-US or ar  
connection_type|  mysql or mssql  
sql_dbms_server_ip| mysql.ef-mysql.svc.cluster.local  
sql_dbms_port| for mysql 3306 / for msql 1433  
sql_dbms_username| <username>  
sql_dbms_password| <password>  
sql_database_name| <database name specific to each tenant>  
**In case of MTT, Update the following parameters as well**|   
conversation_manager_db_name| <tenant_id>  
bot_framework_db_name| <tenant_id>  
ccm_db_name| <tenant_id>  
routing_engine_db_name| <tenant_id>  
cim_customer_db_name| <tenant_id>  
business_calendars_db_name| <tenant_id>  
state_events_logger_db_name| <tenant_id>  
admin_panel_db_name| <tenant_id>  
  
#### Apply configuration for Reporting-Connector on the desired tenant’s namespace  
  
please create a directory for each tenant for MTT
[code] 
    mkdir -p pre-deployment/reportingConnector/<tenant_config_directory>
[/code]

Please copy this file in this directory
[code] 
    cp -r pre-deployment/reportingConnector/reporting-connector.conf  pre-deployment/reportingConnector/<tenant_config_directory>/reporting-connector.conf
[/code]

Edit this file according to your configuration
[code] 
    vi pre-deployment/reportingConnector/<tenant_config_directory>/reporting-connector.conf
[/code]

Apply this file after updating <tenant_config_directory> and namespace
[code] 
    kubectl -n <tenant-namespace> create configmap ef-reporting-connector-conf-cm --from-file=pre-deployment/reportingConnector/<tenant_config_directory>/reporting-connector.conf
[/code]

### Customise `values.yaml`

![](images/icons/grey_arrow_down.png)Customise values.yaml

You must first edit `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to edit a new file:
[code] 
    vi helm/Reporting/values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

Deploy the Reporting Scheduler
[code] 
    helm upgrade --install --namespace <tenant-namespace> --set global.efCxReleaseName="ef-cx"   cx-reporting --debug --values helm/Reporting/values.yaml  helm/Reporting   
[/code]

**Expertflow ETL**

Follow the below steps to configure a new tenant for data platform

**Database Setup**

  1. For MYSQL

     1. Edit the file `kubernetes/pre-deployment/reportingConnector/dbScripts/dbcreation/_historical_reports_db_creation_script_MySQL.sql` and update the following then execute
[code] -- ----------------------------------------------------------------------------
            -- NOTE : CX-4.9 creation script  
            -- ----------------------------------------------------------------------------
            SET FOREIGN_KEY_CHECKS = 0;
            
            -- ----------------------------------------------------------------------------
            -- ----------------------------------------------------------------------------
            CREATE SCHEMA IF NOT EXISTS `<tenant-name>`;
            USE `<tenant-name>`;
            
            -- In case of username other then 'root', update the following with current database username (at line 396)
            
            CREATE DEFINER=<username>@%  PROCEDURE InsertWeekDays(IN start_year INT, IN end_year INT ,IN week_start_day VARCHAR(10))
[/code]

  2. For MSSQL

     1. Edit the file `kubernetes/pre-deployment/reportingConnector/dbScripts/dbcreation/_historical_reports_db_creation_script_MSSQL.sql` and update the following then execute
[code] USE master
            GO
            IF NOT EXISTS (
                SELECT [name]
                    FROM sys.databases
                    WHERE [name] = N'<tenant-name>'
            )
            CREATE DATABASE "<tenant-name>"
            COLLATE SQL_Latin1_General_CP1_CI_AS
            GO
            
            USE "<tenant-name>"
            GO
[/code]

  3. Ensure that the executing user has sufficient privileges to create databases and tables.




### Transflux

Edit the file `transflux/config/tenants/tenants.yaml` and add the following configuration

  1. In order to register new tenants, replicate the previous tenant configuration and append the new settings afterwards, set the `TARGET_TYPE` as per the dedicated target database and configure the database credentials accordingly. You can also update the existing tenant's information as per the following setup
[code] <tenant_name>:
         
             mongodb:
             
               SOURCE_HOST: "mongo-mongodb.ef-external.svc"
               SOURCE_PORT: "27017"
               SOURCE_USERNAME: "root"
               SOURCE_PASSWORD: "Expertflow123"
               SOURCE_TLS_ENABLED: true
               SOURCE_DATABASE: "<tenant_name>"
         
             postgre:
         
               SOURCE_HOST: "ef-postgresql.ef-external.svc"
               SOURCE_PORT: "5432"
               SOURCE_USERNAME: "sa"
               SOURCE_PASSWORD: "Expertflow123"
               SOURCE_DATABASE: "<tenant_name>"
         
             api:
             
               FQDN_URL: "https://<tenant_name>.expertflow.com"
               REALM: "<tenant_name>"
         
             TARGET_TYPE: "mysql"
         
             MYSQL:
               TARGET_HOST: "82.208.20.221"
               TARGET_PORT: "30801"
               TARGET_USERNAME: "root"
               TARGET_PASSWORD: "Expertflow123$#"
               TARGET_SSL_ENABLED: false
               TARGET_DATABASE: "<tenant_name>"
         
             MSSQL:
               TARGET_HOST: "192.168.1.77"
               TARGET_PORT: "1433"
               TARGET_USERNAME: "sa"
               TARGET_PASSWORD: "Expertflow464"
               TARGET_SSL_ENABLED: false
               TARGET_DATABASE: "<tenant_name>"
[/code]




Create configuration ConfigMaps for CX-Transflux pipelines with multi-tenancy configurations.
[code] 
    kubectl -n expertflow delete configmap ef-transflux-config-cm
    kubectl -n expertflow create configmap ef-transflux-config-cm --from-file=config/tenants
[/code]
[code] 
    helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-transflux --debug --values helm-values/cx-transflux-custom-values.yaml  expertflow/transflux 
[/code]

**Rasa**  
For Rasa Multitenancy deployment use [this](Deploy-Rasa-for-Multitenancy_1226113282.html) guide

### **Tenant Onboarding**

This section provides the required steps and references for onboarding new tenants after completing the CX deployment.

[Tenant-Onboarding](Tenant-Onboarding--To-be-removed_1015775291.html)
