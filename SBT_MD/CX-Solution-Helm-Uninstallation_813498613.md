# CX Knowledgebase : CX Solution Helm Uninstallation

  * Teardown
    * CX core
    * CX Channels
    * CX AgentDesk
    * CX Reporting
    * CX Surveys
    * CX-Campaigns
    * CX Eleveo
    * CX CiscoScheduler
    * CX Transflux
    * Delete the namespace
    * Externals
      * Delete Persistent Volumes Claims
      * delete the ef-external namespace
    * Rasa-x
      * delete the rasa-x namespace
    * Superset
      * delete the ef-bi namespace
    * Grafana
      * delete Supervisor and Agent dashboard
      * delete dashboard provider
      * delete datasource



## Teardown 

WARNING 

This procedure will delete all the EF-CX components both external and internals. Proceed with caution, as all the charts and their associated Persistent volumes will also be deleted, resulting in data lost irrecoverably.

#### CX core
[code] 
    helm -n expertflow uninstall ef-cx
[/code]

#### CX Channels
[code] 
    helm -n expertflow uninstall cx-channels
[/code]

#### CX AgentDesk
[code] 
    helm -n expertflow uninstall cx-agent-desk
[/code]

#### CX Reporting
[code] 
    helm -n expertflow uninstall cx-reporting
[/code]

#### CX Surveys
[code] 
    helm -n expertflow uninstall cx-surveys
[/code]

#### CX-Campaigns
[code] 
    helm -n expertflow uninstall cx-campaigns
[/code]

#### CX Eleveo
[code] 
    helm -n expertflow uninstall cx-eleveo
[/code]

#### CX CiscoScheduler
[code] 
    helm -n expertflow uninstall cx-ciscoscheduler
[/code]

#### CX Transflux
[code] 
    helm -n expertflow uninstall cx-transflux
[/code]

Delete all the ConfigMaps and Secrets created in expertflow namespace.
[code] 
    kubectl -n expertflow get secrets,cm
[/code]
[code] 
    kubectl -n expertflow delete cm <CM-NAME>
[/code]
[code] 
    kubectl -n expertflow delete secret <SECRET_NAME>
[/code]

#### Delete the namespace
[code] 
    kubectl delete ns expertflow
[/code]

#### Externals
[code] 
    helm -n ef-external uninstall $(helm list -n ef-external 2>/dev/null | awk '! /NAME/ {print $1 }')
[/code]

##### Delete Persistent Volumes Claims
[code] 
    kubectl -n ef-external delete pvc -l app.kubernetes.io/instance=mongo
[/code]
[code] 
    kubectl -n ef-external delete pvc -l app.kubernetes.io/instance=redis 
[/code]
[code] 
    kubectl -n ef-external delete pvc -l app.kubernetes.io/instance=minio
[/code]
[code] 
    kubectl -n ef-external delete pvc -l app.kubernetes.io/instance=ef-postgresql
[/code]

##### delete the ef-external namespace
[code] 
    kubectl delete namespace ef-external
[/code]

#### Rasa-x
[code] 
    helm -n rasa-x uninstall rasa-x
[/code]

##### delete the rasa-x namespace
[code] 
    kubectl delete namespace rasa-x
[/code]

#### Superset 
[code] 
    helm -n ef-bi uninstall superset
[/code]

##### delete the ef-bi namespace
[code] 
    kubectl delete namespace ef-bi
[/code]

#### Grafana 

##### delete Supervisor and Agent dashboard
[code] 
    kubectl -n expertflow delete configmap ef-grafana-supervisor-dashboard
    kubectl -n expertflow delete configmap ef-grafana-agent-dashboard
[/code]

##### delete dashboard provider
[code] 
    kubectl -n expertflow delete cm ef-grafana-dashboard-provider-cm
[/code]

##### delete datasource 
[code] 
    kubectl -n expertflow  delete secret ef-grafana-datasource-secret
[/code]
