# CX Knowledgebase : Upgrade Guide CX5.0.2 to CX5.1.0

Before upgrading, ensure that the system is idle, i.e, all agents are logged out from the AgentDesk.

## Custom Configuration Strategy

For detailed guidelines on applying environment-specific configurations using custom `values.yaml` layering,

Refer to the **CX Helm Chart Custom Configuration Strategy** [_guide_](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/1238565784/4.10+Customizing+CX+Helm+Chart+Deployments).

  1. **Update Helm repo**
[code] helm repo update expertflow
[/code]

  2. **Clone the CX repository on the target server**
[code] # Create CX-5.1.0 directory from root
           mkdir CX-5.1.0
         # Navigate to CX-5.1.0
           cd CX-5.1.0
         # Clone the CX-5.1.0 branch of the cim-solution repository
           git clone -b CX-4.10.x_MergedInto-CX-5.0 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git $HOME/CX-5.1.0
         # Navigate to root(previous) directory
           cd ../
[/code]

  3. **Setup Transflux**

     1. Setup transflux using the guide: <https://expertflow-docs.atlassian.net/wiki/x/IQALZQ>

  4. **Setup Apisix**
[code] # Clone the latest version apisixi custom values
         helm show values expertflow/apisix --version 5.1.0-rc.1  > helm-values/apisix-custom-values.yaml
         
         # update the helm-values/apisix-custom-values.yaml file for given parameters
         global:
           ingressRouter: "*.expertflow.com"   # * for MTT & for prem replace FQDN
           ingressClassName: "nginx"
           ingressTlsCertName: "ef-ingress-tls-secret"
         
         # Deploy the apisix using updated custom-values.yaml file
         helm upgrade --install --namespace ef-external --values helm-values/apisix-custom-values.yaml apisix expertflow/apisix --version 5.1.0-rc.1
         
         #Verify the deployment of the apisix
         kubectl -n ef-external get deploy
         
[/code]

  5. **Vault Configuration**
[code] # Create secrets related to vault
           kubectl get secret tls-ca -n vault -o yaml | sed 's/namespace: vault/namespace: ef-external/' | kubectl create -f -
           kubectl get secret tls-server-client -n vault -o yaml | sed 's/namespace: vault/namespace: ef-external/' | kubectl create -f -
           kubectl get secret tls-server-vault -n vault -o yaml | sed 's/namespace: vault/namespace: ef-external/' | kubectl create -f -
           kubectl get secret expertflow-reg-cred -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
           kubectl get secret redis-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
           kubectl get secret ef-postgresql-crt -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
           kubectl get secret activemq-tls -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: vault/' | kubectl create -f -
         
         # Copy activemq-vault directory 
           Copy From CX-5.1.0/kubernetes/pre-deployment/activemq-vault To ./kubernetes/pre-deployment
         # Copy service-based-accounts directory 
           Copy From CX-5.1.0/kubernetes/pre-deployment/service-based-accounts To ./kubernetes/pre-deployment
         # Copy keycloak-spc.yaml
           Copy From CX-5.1.0/kubernetes/pre-deployment/keycloak/keycloak-spc.yaml To ./kubernetes/pre-deployment/keycloak
[/code]

  6. **Deploy Redis Helm Chart**



[code] 
    helm show values expertflow/redis --version 5.1.0-rc.1 > helm-values/ef-redis-custom-values.yaml
[/code]

Update the following values `helm-values/ef-redis-custom-values.yaml` as mentioned below
[code] 
      acl:
        users:
             password: "Expertflow464" # Change this to match the requirements  
[/code]
[code] 
    helm upgrade --install=true  --namespace=ef-external --values=helm-values/ef-redis-custom-values.yaml  redis expertflow/redis --version 5.1.0-rc.1
[/code]

  5. **Deploy Vault Helm Chart**



[code] 
    helm uninstall -n vault vault
[/code]
[code] 
    helm show values expertflow/vault --version 5.1.0-rc.1 > helm-values/ef-vault-custom-values.yaml
[/code]
[code] 
    helm upgrade --install --namespace vault --create-namespace vault --debug --values helm-values/ef-vault-custom-values.yaml expertflow/vault --version 5.1.0-rc.1
[/code]

Follow only the unsealing steps from [_initializing and unsealing the vault_](https://expertflow-docs.atlassian.net/wiki/x/eQCLDw) guide
[code] 
    kubectl -n vault exec -it vault-0 -- vault login <root-token>
[/code]

Use the **root token** for vault in the above login command

**Follow the below mentioned guides to configure Service based Accounts and Vault in different external components:**

**_For Mongo_**  
Execute below command to see the existing mongo TTL. If the TTL is less than `87600h` then update the TTL using this last part of this guide [_Configure Vault for MongoDB Dynamic Database Credentials_](https://expertflow-docs.atlassian.net/wiki/x/B4A4Sg)   
`kubectl -n vault exec -it vault-0 -- vault read database/roles/mongodb-role`  
**Note:** Make sure vault is login otherwise do vault login after making exec separately into vault if permission is denied on above command.  
  
**_Continue_**  
**For Redis:** [_Configure Vault for Redis Dynamic Database Credentials (non-mtt)_](https://expertflow-docs.atlassian.net/wiki/x/CwChUQ)   
**For ActiveMQ:** [_Configure Vault for ActiveMQ_](https://expertflow-docs.atlassian.net/wiki/x/UwD7UQ)   
**For PostgreSql:** [_Configure Vault for PostgreSQL Dynamic Database Credentials_](https://expertflow-docs.atlassian.net/wiki/x/LYCTTw)   
**For Service Based Accounts:** [_Configure Service Based Accounts using Vault_](https://expertflow-docs.atlassian.net/wiki/x/eYDzTw)

  6. **Move back to** `<active-directory>/kubernetes`

  7. **Deploy the ActiveMQ helm chart**



[code] 
    helm show values expertflow/activemq --version 5.1.0-rc.1 > helm-values/ef-activemq-custom-values.yaml
[/code]
[code] 
    helm upgrade --install=true  --namespace=ef-external --values=helm-values/ef-activemq-custom-values.yaml activemq expertflow/activemq --version 5.1.0-rc.1
[/code]

  7. **Deploy the Keycloak helm chart**



[code] 
    helm show values expertflow/keycloak --version 5.1.0-rc.1 > helm-values/ef-keycloak-custom-values.yaml
[/code]

Edit `helm-values/ef-keycloak-custom-values.yaml`
[code] 
    global:
      ingressRouter: <DEFAULT-FQDN>
[/code]

Now, deploy Keycloak by running the following command
[code] 
    helm upgrade --install=true  --debug --namespace=ef-external  --values=helm-values/ef-keycloak-custom-values.yaml keycloak expertflow/keycloak --version 5.1.0-rc.1
[/code]

  8. **Deploy the AgentDesk helm chart**
[code] # Copy the unified agent translation directory to the current release 
           Copy From CX-5.1.0/kubernetes/pre-deployment/app-translations/unified-agent/i18n/ To pre-deployment/app-translations/unified-agent
         # Delete and Create the ConfigMap of Unified Agent based translations
           kubectl delete cm ef-app-translations-cm -n expertflow
           kubectl -n expertflow create configmap ef-app-translations-cm --from-file=pre-deployment/app-translations/unified-agent/i18n/
         # Copy the customer-widget translation directory to the current release 
           Copy From CX-5.1.0/kubernetes/pre-deployment/app-translations/customer-widget/i18n/ To pre-deployment/app-translations/customer-widget
         # Delete and Create the ConfigMap of Customer Widget based translations
           kubectl delete cm ef-widget-translations-cm -n expertflow
           kubectl -n expertflow  create configmap ef-widget-translations-cm --from-file=pre-deployment/app-translations/customer-widget/i18n/
[/code]
[code] # Deploy the new chart version using the helm-values/cx-agent-desk-custom-values.yaml
           helm upgrade --install --namespace expertflow --set global.efCxReleaseName="ef-cx"  cx-agent-desk  --debug --values helm-values/cx-agent-desk-custom-values.yaml expertflow/agent-desk --version 5.1.0-rc.1
[/code]




**AGENT_STATE_CHANGED Flow Added in Conversation Studio**  
**Note:** Please take backup/export of your existing flow from conversation studio before any change

A new flow for Agent State Change has been added as part of the Conversation Re-Routing on Agent State Change - Not Ready (Callback) [_feature_](Conversation-Rerouting-on-Agent-State-Change-to-Callback_1599766616.html).

**If you are using custom flows for Conversation Studio:**

Please add the flow changes manually. After deploying the Core helm chart, refer to the Conversation Studio default flows [_documentation_](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/1144094757/Default+Flows) (see the 'Agent State Changed' section—17th heading) and update your customized flow accordingly.  


**If you are using default flows for Conversation Studio (This will remove all existing flows, please only follow the below in case you are using default flows):**

Execute the below commands before deploying the Core Helm chart.

a. Delete the Conversation Studio StatefulSet:
[code] 
    kubectl delete -n expertflow statefulset ef-cx-conversation-studio
[/code]

b. Delete the existing Persistent Volume Claim (PVC) for Conversation Studio:
[code] 
    kubectl delete -n expertflow pvc conversation-studio-flow-vol-ef-cx-conversation-studio-0
[/code]

  9. **Deploy the Core helm chart**



[code] 
    # Copy the conversation manager graphql schemas and mongodb rules to the current release directory
      Copy From CX-5.1.0/kubernetes/pre-deployment/conversation-manager/graphql/ To pre-deployment/conversation-manager
    # Delete and Create the Config Maps related to Conversation Manager Graphql schemas and mongodb rules
      kubectl delete configmap -n expertflow conversation-manager-graphql-schemas
      kubectl create configmap -n expertflow conversation-manager-graphql-schemas --from-file=./pre-deployment/conversation-manager/graphql/schemas
      kubectl delete configmap -n expertflow conversation-manager-graphql-mongodb-rules
      kubectl create configmap -n expertflow conversation-manager-graphql-mongodb-rules --from-file=./pre-deployment/conversation-manager/graphql/graphql-mongodb-rules.json
    # Deploy the new chart version using the helm-values/ef-cx-custom-values.yaml 
      helm upgrade --install --namespace expertflow --create-namespace   ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx --version 5.1.0-rc.1
[/code]

  10. **Deploy the Channels helm chart**



[code] 
    # Deploy the new chart version using the helm-values/cx-channels-custom-values.yaml
      helm upgrade --install --namespace expertflow --set global.efCxReleaseName="ef-cx" --debug cx-channels --values helm-values/cx-channels-custom-values.yaml  expertflow/channels --version 5.1.0-rc.1
[/code]

  11. **Deploy the QM helm chart**



[code] 
    # Deploy the new chart version using the helm-values/cx-qm-custom-values.yaml
      helm upgrade --install --namespace=expertflow --set global.efCxReleaseName="ef-cx" qm  --debug --values=helm-values/cx-qm-custom-values.yaml expertflow/qm --version 5.1.0-rc.1
[/code]

  12. **Deploy the Campaign helm chart**



[code] 
    # Deploy the new chart version using the helm-values/cx-campaigns-custom-values.yaml
      helm upgrade --install --namespace expertflow --set global.efCxReleaseName="ef-cx"  cx-campaigns --debug --values helm-values/cx-campaigns-custom-values.yaml expertflow/campaigns --version 5.1.0-rc.1
[/code]

  13. **Deploy the Fluent-Bit helm chart**



[code] 
    # Deploy the new chart version using the helm-values/cx-fluent-bit-custom-values.yaml
      helm show values expertflow/fluent-bit --version 5.1.0-rc.1 > helm-values/cx-fluent-bit-custom-values.yaml
      helm upgrade --install --namespace ef-external --set global.efCxReleaseName="ef-cx"  cx-fluent-bit --debug --values helm-values/cx-fluent-bit-custom-values.yaml expertflow/fluent-bit --version 5.1.0-rc.1
[/code]

**Note:** To setup voice connector, please follow this [_guide_](CX-Voice-Upgrade-to-4.10.X_1215954962.html) with **Voice-Connector** part only using version `5.1.0`

**Configuration Guide(s):**

  1. <https://expertflow-docs.atlassian.net/wiki/x/dAA5Y>



