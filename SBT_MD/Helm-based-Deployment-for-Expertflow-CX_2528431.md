# CX Knowledgebase : Helm-based Deployment for Expertflow CX

**Important!!!**  
This guide is not to add information for**Multitenancy**. Refer to [this guide](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=kb&title=Deployment%20Guide%20-%205.0-Dev&linkCreation=true&fromPageId=2528431) if you are adding deployment scripts for the upcoming Multitenancy release.

## Requirements

The following table describes the prerequisites for using Helm for deployment. 

**Item**| **Description**| **When changed**  
---|---|---  
Kubernetes Setup| a standard and compatible release of kubernetes is available| A clean installed Kubernetes Engine . This can be performed using guide  [RKE2 Control plane Deployment](RKE2-Control-plane-Deployment_2528874.html)  
FQDN| A valid FQDN is required to deploy the solution for example “devops.ef.com”| by default there is no FQDN associated, and the helm chart(s) will exit with failure if the default value is used.  
TLS/SSL certificate| It is mandatory to have a valid SSL certificate already create in both expertflow and ef-external namespaces. Default Ingress certificate name is “`ef-ingress-tls-secret`"| It is by default required and must be created before the actual helm chart deployment .  
  
## Add helm repository
[code] 
    helm repo add expertflow https://expertflow.github.io/charts/
[/code]

update helm repo
[code] 
    helm repo update expertflow
[/code]

### Helm chart functional groups

CX helm charts are divided into functional groups. Refer to [this document](https://expertflow-docs.atlassian.net/wiki/pages/resumedraft.action?draftId=2528431) to understand how these charts are structured.

**Group**| **Description**| **Dependency**  
---|---|---  
CX| serves the basic and core functionality of the CX Solution.| External Components  
Web Channels| Provides CX enhancements for digital Channels| CX  
AgentDesk| Provides separate deployment for customers where AgentDesk is optional| CX  
Survey| Functional group provides Surveying Collaborations| CX  
Campaigns| Functional group provides Campaigns Collaborations.| CX  
Reporting| Reporting related to the CX| CX  
Eleveo| Eleveo functional group| CX  
CiscoScheduler| Cisco functional group| CX  
  
# Prepare for CX Deployment

### Step 1: Clone the Expertflow CX repository
[code] 
    git clone -b CX-4.10  https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git CX-4.10
[/code]
[code] 
    cd CX-4.10/kubernetes
[/code]

### Step 2: Create Namespaces

  1. Create a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) `expertflow` for all Expertflow components




Run the following command on the control-plane node.
[code] 
    kubectl create namespace expertflow
[/code]

Create a namespace `ef-external` for all the external elements of the Expertflow CX solution such as Mongo, Redis, MinIO, etc.

Run the following command on the control-plane node.
[code] 
    kubectl create namespace ef-external
[/code]

### Ingress Controller Selection

  * Default ingressClass is set to “nginx” in all helm charts' global section. if you prefer to use other ingress controller, please update the ingressClassName to appropriate value.

  * All helm charts served at expertflow helm repository ( CX groups/components and external components ) by default are compatible with ingress-nginx ingress controller using ingress-nginx annotations. Should there be requirement for any other ingress controller like traefik, HA-Proxy or contour etc, please adjust the annotations for all components accordingly. A coordinated guide for using Traefik as Ingress Controller is available for CX solution’s compatibility at [https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/749437259](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=kb&title=Using%20Traefik%20as%20Ingress%20Controller-5.0&linkCreation=true&fromPageId=2528431)




Add TLS Certificates 

  * For Self Signed please use this guide [https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/48400625](Create-self-signed-Certificates-for-Ingress_48400625.html) in both `ef-external` and `expertflow` namespaces

  * For Commercial Certificates, please import them as `tls.crt` and `tls.key` and create secret with the name of `ef-ingress-tls-secret` in both `ef-external` and `expertflow` namespaces

  * For LetsEncrypt based TLS Certificates please consult [https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/32538676](LetsEncrypt-SSL-for-EF-CX_32538676.html)




NOTE: 

When using LE based TLS Certificates, you will have to enable correct annotations in all the relevant values file. For example, for CX, after downloading the `<COMPONENT>-custom-values.yaml` file, you can run 

`sed -i -e 's/#cert-manager.io\/cluster-issuer: /cert-manager.io\/cluster-issuer: /g' <COMPONENT>-custom-values.yaml` to enable it.

This procedure is required for both externals and all CX group charts being deployed.

### Step 3: Apply Image Pull secret

  1. Run the following commands for applying ImagePullSecrets of Expertflow CX images.



[code] 
    kubectl apply -f pre-deployment/registryCredits/ef-imagePullSecret-ef-external.yaml
[/code]

Create a directory to hold values files for all the helm charts.
[code] 
    mkdir helm-values
[/code]

### Custom Password Interpolations

Below are the interpolations when using custom or not-default password for mongodb, minio, redis, postgresql and activeMQ

**Component with custom password**| **update required in**  
---|---  
MongoDB| 

  1. Update `CX -> values.yaml -> efConnectionVars -> MONGODB_PASSWORD`

  
PostgreSQL| 

  1. Update `keycloak -> keycloak-custom-values.yaml -> externalDatabase -> password`
  2. Update `CX -> values.yaml -> license-manager -> extraEnvVars-> DB_PASS`

  
minio| 

  1. Update `CX -> values.yaml -> file-engin -> extraEnvVars -> ACCESSKEY,SECRETKEY`

  
Redis| 

  1. Update `CX -> values.yaml -> efConnectionVars ->`
  2. update `ActiveMQ -> active-custom-values.yaml -> extraEnvVars -> REDIS_PASSWORD`

  
keycloak| N/A  
activeMQ| N/A  
  
### Setup SQL Database

Expertflow CX requires any of the following **PostgreSQL** for Expertflow CX deployment for storing configuration data.

If you are deploying external components with provided TLS certificates, you must run the following command before deployment:-
[code] 
    kubectl apply -f pre-deployment/static-tls
[/code]

**PostgreSQL** RECOMMENDED | If you do not have PostgreSQL in your environment, create Config-Map of PostgreSQL to create necessary databases and preload it with bootstrap configurations.
[code] 
    kubectl -n ef-external  create configmap ef-postgresql-license-manager-cm --from-file=./pre-deployment/licensemanager/licensemanager.sql
[/code]

download the values.yaml file locally to customize the parameter values.
[code] 
    helm show values expertflow/postgresql > helm-values/ef-postgresql-custom-values.yaml
[/code]

Update the following values file `helm-values/ef-postgresql-custom-values.yaml` as mentioned below:-
[code] 
    auth:
      password: "<CHANGE_PASSWORD>"
[/code]

For Worker HA deployment, add the following tolerations:-
[code] 
      tolerations: 
        - key: "node.kubernetes.io/unreachable"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being unreachable
        - key: "node.kubernetes.io/not-ready"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being not-ready
[/code]

Deploy the postgresql
[code] 
    helm upgrade --install=true --namespace=ef-external --values=helm-values/ef-postgresql-custom-values.yaml  ef-postgresql expertflow/postgresql
[/code]

For managed Postgresql, see [Using Managed PostgreSQL](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/48269150/Using+Managed+PostgreSQL) for configuring PostgreSQL for Expertflow CX.  
---|---  
  
## Deploy CX External Components

Expertflow CX requires the following 3rd party components.

**Redis**|  Key-Values based Caching engine, used by most of the EF-CX components.  
---|---  
**MongoDB**|  NoSQL Database, maintains and serves as primary back store for EF-CX solution.  
**Minio**|  S3 compliant object storage.  
**KeyCloak**|  Realm based auth management tool.  
  
You may use them from your existing environment or from a cloud provider .

### Setup KeyCloak

#### Prerequisites

Before proceeding with the keycloak deployment, please update the backend database connection string parameters ( when using non-default passwords )

clone the values file and update the parameter values
[code] 
    helm show values expertflow/keycloak > helm-values/ef-keycloak-custom-values.yaml
[/code]

edit `helm-values/ef-keycloak-custom-values.yaml` and update the password for postgresql database
[code] 
    global:
      ingressRouter: <DEFAULT-FQDN>
    externalDatabase:
      password: "Expertflow123"
[/code]

Default keycloak deployment uses postgresql running inside the same kubernetes cluster. When using managed postgresql database instance, update above parameters with relevant information 

For Worker HA deployments, add the following tolerations:-
[code] 
    tolerations:
        - key: "node.kubernetes.io/unreachable"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being unreachable
        - key: "node.kubernetes.io/not-ready"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being not-ready
[/code]

#### Keycloak Deployment

Keycloak is used as the centralized authentication and authorization component for Expertflow CX. Follow these steps to setup KeyCloak.

Now, deploy KeyCloak by running the following command
[code] 
    helm upgrade --install=true  --debug --namespace=ef-external  --values=helm-values/ef-keycloak-custom-values.yaml keycloak expertflow/keycloak
[/code]

Check the KeyCloak installation status. You can check the status of deployment by using the following command:
[code] 
    kubectl -n ef-external rollout status sts keycloak
[/code]

### Setup MongoDB

Expertflow CX using MongoDB for storing all CX events, activities, and some configuration data as well.

Skip this step if you already have MongoDB in your environment that can be used by Expertflow CX. For using MongoDB from a managed environment, see [Using Managed MongoDB](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/49217904/Using+Managed+MongoDB) for necessary configurations.

Clone the values file to update the parameter values
[code] 
    helm show values expertflow/mongodb > helm-values/ef-mongodb-custom-values.yaml
[/code]

Update the following values file `helm-values/ef-mongodb-custom-values.yaml` as mentioned below
[code] 
    auth:
      rootPassword: "Expertflow123"
[/code]

For Worker HA deployments, add the following tolerations:-
[code] 
    tolerations:
        - key: "node.kubernetes.io/unreachable"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being unreachable
        - key: "node.kubernetes.io/not-ready"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being not-ready
[/code]

Deploy MongoDB by running the following command.
[code] 
    helm upgrade --install=true --namespace=ef-external --values=helm-values/ef-mongodb-custom-values.yaml mongo expertflow/mongodb
[/code]

Check the MongoDB deployment status by running the following command:
[code] 
    kubectl -n ef-external rollout status sts mongo-mongodb
[/code]

### Setup MinIO as S3 Storage

Expertflow CX using MinIO for storing files exchanged between agents, customers, and/or bots. Install using Helm using following command:

Clone the values file for updating the parameter values
[code] 
    helm show values expertflow/minio > helm-values/ef-minio-custom-values.yaml
[/code]

update the minio helm chart `helm-values/ef-minio-custom-values.yaml` files with the required ACCESSKEY and PASSKEY values
[code] 
    auth:
      rootUser: minioadmin
      rootPassword: "minioadmin"
[/code]

Deploy the minio helm chart
[code] 
    helm upgrade --install=true --namespace=ef-external --values=helm-values/ef-minio-custom-values.yaml minio expertflow/minio
[/code]

Wait for the minio deployment to get ready
[code] 
    kubectl -n ef-external  rollout status deployment  minio --timeout=5m
[/code]

#### Digital Channel Icons Bootstrapping

proceed with icons bootstrapping.
[code] 
    kubectl apply -f scripts/minio-helper.yaml
[/code]
[code] 
    kubectl -n ef-external --timeout=90s wait --for=condition=ready pod minio-helper
[/code]
[code] 
    kubectl -n ef-external cp post-deployment/data/minio/bucket/default minio-helper:/tmp/
[/code]
[code] 
    kubectl -n ef-external cp scripts/icon-helper.sh minio-helper:/tmp/
[/code]
[code] 
    kubectl -n ef-external exec -it minio-helper -- /bin/sh /tmp/icon-helper.sh
[/code]
[code] 
    kubectl delete -f scripts/minio-helper.yaml
[/code]

### Setup Redis

CX uses Redis for storing active system state of most of the CX objects.

Clone the values file to update the parameter values
[code] 
    helm show values expertflow/redis > helm-values/ef-redis-custom-values.yaml
[/code]

Update the following values `helm-values/ef-redis-custom-values.yaml` as mentioned below:-
[code] 
    auth:
      password: "Expertflow123"  # Change this to match the requirements  
[/code]

For Worker HA deployments, add the following tolerations:-
[code] 
    tolerations:
        - key: "node.kubernetes.io/unreachable"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being unreachable
        - key: "node.kubernetes.io/not-ready"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 60 # Evict after 60 seconds of being not-ready 
[/code]

Run the following command to deploy Redis.
[code] 
    helm upgrade --install=true  --namespace=ef-external --values=helm-values/ef-redis-custom-values.yaml  redis expertflow/redis
[/code]

### Setup APISIX

Clone the apisix values.yaml file
[code] 
    helm show values expertflow/apisix --version 2.10.0  > helm-values/apisix-custom-values.yaml
[/code]

update the `apisix-custom-values.yaml` file for given parameters
[code] 
    global:
      ingressRouter: "devops.ef.com"   
      ingressClassName: "nginx"
      ingressTlsCertName: "ef-ingress-tls-secret"
[/code]

deploy the apisix using updated custom-values.yaml file
[code] 
    helm upgrade --install --namespace ef-external --values helm-values/apisix-custom-values.yaml apisix expertflow/apisix --version 2.10.0 
[/code]

Verify the deployment of the apisix
[code] 
    kubectl -n ef-external get deploy
[/code]

API authentication is disabled by default. To enable it, follow this [guide](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/1166770877/API+Gateway+Enablement+Guide). Additionally, ensure that Keycloak is properly configured by referring to the Keycloak Configuration [Guide](/wiki/pages/createpage.action?spaceKey=SBT&title=Keycloak%20Configurations%20for%20APISIX-Proxy%20Enablement&linkCreation=true&fromPageId=2528431).

### Setup ActiveMQ

Clone the values file to update the parameters required
[code] 
    helm show values expertflow/activemq --version 4.10.0 > helm-values/ef-activemq-custom-values.yaml
[/code]
[code] 
    helm upgrade --install=true  --namespace=ef-external --values=helm-values/ef-activemq-custom-values.yaml activemq expertflow/activemq --version 4.10.0
[/code]

### CX Clamav

Clamav is an optional scanning service to scan the files before uploading to the file engine. You can enable/disable the scanning in the file engine’s environment variable `IS_SCAN_ENABLED`; by default, it’s enabled.

Customise the deployment by fetching the values.yaml file and edit it as per the requirements.
[code] 
    helm show values expertflow/clamav --version 4.9.0   > helm-values/cx-clamav-values.yaml
[/code]

Edit/update the values file `helm-values/cx-clamav-values.yaml` with
[code] 
    global:
      ingressRouter: <DEFAULT-FQDN>
[/code]

Deploy the Clamav helm chart by 
[code] 
    helm upgrade --install --namespace ef-external --set global.efCxReleaseName="ef-cx"  clamav --debug --values helm-values/cx-clamav-values.yaml   helm/clamav --version 4.9.0 
[/code]

### Setup Vault

Clone the values file to update the parameters required
[code] 
    helm show values expertflow/vault --version 0.28.0 > helm-values/ef-vault-custom-values.yaml
[/code]
[code] 
    helm upgrade --install --namespace vault --create-namespace vault --debug --values helm-values/ef-vault-custom-values.yaml expertflow/vault
[/code]

Use the following vault [configuration guide](https://expertflow-docs.atlassian.net/wiki/x/ZoDJOQ)

## Deploy CX Components

#### Custom Configuration

For detailed guidelines on applying environment-specific configurations using custom `values.yaml` layering, refer to the **CX Helm Chart Custom Configuration Strategy** [guide](https://expertflow-docs.atlassian.net/wiki/x/M4DyS).

### Expertflow ETL 

For CX Transflux deployment, please refer to [EF Data Platform Deployment](https://expertflow-docs.atlassian.net/wiki/spaces/EF/pages/772243470/EF+Data+Platform+Deployment)

It is required to run the following pipeline before deploying the CX Solution. But this `grafana_queries` pipeline requires CX Reporting Connector to be deployed and up.

  * `grafana_queries`




### CX Core

Transfer the Mongo, Redis, PostgreSQL and ActiveMQ Certificates from the ef-external namespace
[code] 
    kubectl get secret mongo-mongodb-ca -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: expertflow/' | kubectl create -f -
    kubectl get secret redis-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: expertflow/' | kubectl create -f -
    kubectl get secret ef-postgresql-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: expertflow/' | kubectl create -f -
    kubectl get secret activemq-tls -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: expertflow/' | kubectl create -f -
    
[/code]

Setup default translation file for customer widget
[code] 
    kubectl -n expertflow  create configmap ef-widget-translations-cm --from-file=pre-deployment/app-translations/customer-widget/i18n/
[/code]

Apply ConfigMap to enable log masking for all components in `expertflow` namespace:-
[code] 
    kubectl apply -f pre-deployment/logback/
    kubectl -n expertflow create configmap ef-logback-cm --from-file=pre-deployment/logback/logback-spring.xml
[/code]

Setup graphql schemas and mongodb rules configmaps 
[code] 
     kubectl create configmap -n expertflow conversation-manager-graphql-schemas --from-file=pre-deployment/conversation-manager/graphql/schemas
[/code]
[code] 
    kubectl create configmap -n expertflow conversation-manager-graphql-mongodb-rules --from-file=pre-deployment/conversation-manager/graphql/graphql-mongodb-rules.json
[/code]

#### Create and Customise `ef-cx-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise ef-cx-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/ef-cx-custom-values.yaml 
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `ef-cx-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/cx --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

In real time reports change the following extraEnvVars as per your reporting DB

  * DATASOURCE_URL

  * DATASOURCE_USERNAME 

  * DATASOURCE_PASSWORD




Deploy the CX Core using default values.
[code] 
    helm upgrade --install --namespace expertflow --create-namespace   ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx --version 4.10.0 
[/code]

“ef-cx” in above command is the release name which will referenced in all subsequent functional groups' deployments.

check the status of CX components
[code] 
    kubectl -n expertflow get pods
[/code]

### CX AgentDesk

Setup default translation file for Agent Desk
[code] 
    kubectl -n expertflow  create configmap ef-app-translations-cm --from-file=pre-deployment/app-translations/unified-agent/i18n
[/code]

Setup default canned messages translations file for Agent Desk
[code] 
    kubectl -n expertflow  create configmap ef-canned-messages-cm --from-file=pre-deployment/app-translations/unified-agent/canned-messages
[/code]

Apply CRM ConfigMap for Agent Desk 
[code] 
    kubectl -n expertflow create configmap ef-crm-service-cm --from-file=pre-deployment/crm-service/
[/code]

Update the **FQDN** of the machine against `url` field in file `post-deployment/config/grafana/supervisor-dashboards/datasource.yml`

Apply the Grafana data-source manifest.
[code] 
    kubectl -n expertflow  create secret generic ef-grafana-datasource-secret --from-file=post-deployment/config/grafana/supervisor-dashboards/datasource.yml
[/code]

Apply Grafana provider manifest.
[code] 
    kubectl -n expertflow create cm ef-grafana-dashboard-provider-cm --from-file=post-deployment/config/grafana/supervisor-dashboards/dashboard.yml
[/code]

##### For Supervisor Dashboard

Apply config-map for the supervisor dashboard files using the steps below.
[code] 
    kubectl -n expertflow create configmap ef-grafana-supervisor-dashboard --from-file=post-deployment/config/grafana/supervisor-dashboards/Supervisor_Dashboard_CIM.json
[/code]

##### For Agent Dashboard
[code] 
    kubectl -n expertflow create configmap ef-grafana-agent-dashboard --from-file=post-deployment/config/grafana/supervisor-dashboards/Agent_Dashboard_CIM.json
[/code]

#### Create and Customise `cx-agent-desk-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-agent-desk-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-agent-desk-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-agent-desk-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/agent-desk --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Install the AgentDesk using helm chart
[code] 
    helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-agent-desk  --debug --values helm-values/cx-agent-desk-custom-values.yaml expertflow/agent-desk --version 4.10.0 
[/code]

### CX Channels

#### Create and Customise `cx-channels-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-channels-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-channels-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-channels-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/channels --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Deploy the Channels helm chart by 
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"   --debug   cx-channels --values  helm-values/cx-channels-custom-values.yaml  expertflow/channels --version 4.10.0 
[/code]

### CX Surveys

#### Create and Customise `cx-surveys-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-surveys-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-surveys-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-surveys-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/surveys --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Deploy the CX Surveys helm chart by 
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"  cx-surveys  --debug --values helm-values/cx-surveys-custom-values.yaml expertflow/surveys --version 4.10.0 
[/code]

Make sure to assign the role _conversation-studio-admin_ to the Keycloak user _admin._  
If you want to create an explicit user for surveys, update the user in the surveys siteEnvVars

### CX Campaigns

#### Create and Customise `cx-campaigns-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-campaigns-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-campaigns-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-campaigns-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/campaigns --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Deploy the CX Campaigns helm chart by 
[code] 
    helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-campaigns --debug --values helm-values/cx-campaigns-custom-values.yaml expertflow/campaigns --version 4.10.0 
[/code]

Make sure to assign the role _conversation-studio-admin_ to the Keycloak user _admin._  
If you want to create an explicit user for campaigns, update the user in the campaigns siteEnvVars

### CX Reporting

#### Configure TLS connection for MySQL

Get the MySQL `key-store (.jsk)` & `certificate(.cert)` files from customer. The `.jsk` file is required for configuration of the reporting connector, whereas the `.cert` file is required for Apache Superset SSL configuration. Skeleton Project (cim-solution) already contains the default .jks files in the keystore directory. Replace the` mykeystore.jks `file acquired from the customer in `cim-solution/kubernetes/pre-deployment/reportingConnector/keystore/ `directory.

Create `keystore.jks` used for MySQL TLS 
[code] 
    kubectl create configmap -n expertflow ef-reporting-connector-keystore-cm --from-file=pre-deployment/reportingConnector/keystore/mykeystore.jks
[/code]

Open the `pre-deployment/reportingConnector/reporting-connector.conf` and set the `mysql_dbms_additional_params`**** value as shown below.
[code] 
    mysql_dbms_additional_params=noDatetimeStringSync=true&useSSL=true&requireSSL=true&trustServerCertificate=true&clientCertificateKeyStoreUrl=file:///root/config/certs/mykeystore.jks&clientCertificateKeyStorePassword={KEYSTORE_PASSWORD}
     
    # Replace the {KEYSTORE_PASSWORD} with your original keystore password. Use "changeit" in case of default password.
[/code]

#### Reporting Connector Config-Map Setup

Create the the database in target Database Management System using the scripts from `CX-4.10/kubernetes/pre-deployment/reportingConnector/SQLScripts/dbcreation` directory.

Update below parameters in the file `pre-deployment/reportingConnector/reporting-connector.conf`

**Parameter**| **Requirement**  
---|---  
fqdn|  FQDN of the CX Solution  
svc_name| k get svc -n expertflow | grep historical http://ef-cx-historical-reports-svc.expertflow.svc:8081  
browser_language|  en or ar  
connection_type|  mysql or mssql  
sql_dbms_server_ip| <IP>  
sql_dbms_port| for mysql 3306 / for msql 1433  
sql_dbms_username| <username>  
sql_dbms_password| <password>  
sql_database_name| <database name>  
  
Apply configuration for Reporting-Connector
[code] 
    kubectl -n expertflow create configmap ef-reporting-connector-conf-cm --from-file=pre-deployment/reportingConnector/reporting-connector.conf
[/code]

#### Create and Customise `cx-reporting-scheduler-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-reporting-scheduler-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-reporting-scheduler-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-reporting-scheduler-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/reporting --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Deploy the Reporting Scheduler
[code] 
    helm upgrade --install --namespace expertflow --set global.efCxReleaseName="ef-cx"   cx-reporting --debug --values helm-values/cx-reporting-scheduler-custom-values.yaml  expertflow/reporting  --version 4.10.0 
[/code]

### CX Eleveo Middleware

#### Create and Customise `cx-middleware-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-middleware-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-middleware-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-middleware-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/eleveo-middleware --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

#### Create and Customise `cx-middleware-cronjob-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-middleware-cronjob-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-middleware-cronjob-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-middleware-cronjob-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/middleware-cronjob --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Open the `helm-values/cx-middleware-custom-values.yaml` and `helm-values/cx-middleware-cronjob-custom-values.yaml` files and update the variables as documented [here](https://expertflow-docs.atlassian.net/wiki/x/OgCFNg).

Run the following commands:
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"  eleveo-middleware  --values helm-values/cx-middleware-custom-values.yaml expertflow/eleveo-middleware --version 4.10.0 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"  middleware-cronjob --debug --values helm-values/cx-middleware-cronjob-custom-values.yaml   expertflow/middleware-cronjob  --version 4.10.0 
[/code]

### **CiscoSyncService**

#### Create and Customise `cx-ciscosyncservice-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-ciscosyncservice-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-ciscosyncservice-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-ciscosyncservice-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/cisco-sync-service --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

Deploy the CiscoSyncService helm chart by 
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"  cisco-sync-service  --values helm-values/cx-ciscosyncservice-custom-values.yaml expertflow/cisco-sync-service --version 4.10.0
[/code]

### Rasa-X deployment

Please refer to [RASA-X Deployment using helm chart](RASA-X-Deployment-using-helm-chart_42402346.html) for deployment of Rasa-x AI Assistant.

### QM 

Deploy QM using the following [guide](https://expertflow-docs.atlassian.net/wiki/x/E4DuO)

### **EFBI Server & Reports**

EFBI for reporting, [Deployment of EFBI](https://expertflow-docs.atlassian.net/wiki/x/F4HvAg) and to configure the Reports follow the below instructions.

For MySQL open the MySQL folder instead of MSSQL

#### For Standard Reports:

Download the reports folder from `kubernetes/post-deployment/supersetReporting/MSSQL/all` reports

####   
QM Reports

Download the reports folder from `kubernetes/post-deployment/supersetReporting/MSSQL/QM` Reports

####   
Campaign Reports

Download the reports folder from `kubernetes/post-deployment/supersetReporting/MySQL/Campaign-Reports`

####   
Survey Reports

Download the reports folder from `kubernetes/post-deployment/supersetReporting/MSSQL/Survey Reports`

  
Compress to Zip file, then update the file on EFBI (superset).

The guide to import the Reports Package into EFBI is [here](1190953015.html).

## Configurations

  1. Import [default keyCloak realm](https://expertflow-docs.atlassian.net/wiki/x/aJsm) for essential KeyCloak resources, permissions, and authentication configurations

  2. Conversation-Studio [configuration guide](https://expertflow-docs.atlassian.net/wiki/x/gQCgP)

  3. Run Expertflow ETL pipelines mentioned [here](https://expertflow-docs.atlassian.net/wiki/x/QoA_SQ)

  4. If you intend to use Apache Superset for reporting, [Deployment of Superset](https://expertflow-docs.atlassian.net/wiki/x/F4HvAg) and [Configure and import historical report templates](https://expertflow-docs.atlassian.net/wiki/x/I4om) to configure the Reporting solution.

  5. For customer channel configuration, see [customer channels](Omnichannel-Engagement_2529366.html). 

  6. For CX-Voice component deployment [this](CX-Voice-Deployment_1344510.html) guide.

  7. For the Surveys [Keycloak Configuration Guide](https://expertflow-docs.atlassian.net/wiki/pages/createpage.action?spaceKey=kb&title=CX%20Surveys%20Deployment%20Guide&linkCreation=true&fromPageId=2528431)

  8. For the Campaigns [Keycloak Configuration Guide](CX-Campaigns-Keycloak-Configuration_474120764.html)



