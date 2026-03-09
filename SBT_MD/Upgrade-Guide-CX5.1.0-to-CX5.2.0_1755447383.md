# CX Knowledgebase : Upgrade Guide CX5.1.0 to CX5.2.0

Before upgrading, ensure that the system is idle, i.e, all agents are logged out from the AgentDesk.

## Custom Configuration Strategy

For detailed guidelines on applying environment-specific configurations using custom `values.yaml` layering,

Refer to the **CX Helm Chart Custom Configuration Strategy** [_guide_](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/1238565784/4.10+Customizing+CX+Helm+Chart+Deployments).

In this release, ActiveMQ Classic is being replaced by ActiveMQ Artemis

  1. **Update Helm repo**
[code] helm repo update expertflow
[/code]

  2. **Uninstall the ActiveMQ**
[code] # Uninstall the ActiveMQ chart
           helm uninstall -n ef-external activemq
         # Remove the ActiveMQ PVC
           kubectl delete pvc -n ef-external activemq-activemq-0 
[/code]

  3. **Deploy the Artemis using the following**[**guide**](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/1268056065/Apache+ActiveMQ+Artemis+Deployment+Latest+Stable+Version+as+a+System+Service)**.**

  4. **Deploy the Core helm chart**



[code] 
    # Update the following variables in the helm-values/ef-cx-custom-values.yaml 
      efConnectionVars:
          ACTIVEMQ_PRIMARY_URL: "<10.192.11.18>" → #Not using svc name anymore, use the respective IP Address
          ACTIVEMQ_SECONDARY_URL: "<10.192.11.18>" → #Not using svc name anymore, use the respective IP Address
    
    # Deploy the new chart version using the helm-values/ef-cx-custom-values.yaml 
      helm upgrade --install --namespace expertflow --create-namespace   ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx --version 5.2.0-rc.1
[/code]

  8. **Deploy the Channels helm chart**
[code] # Deploy the new chart version using the helm-values/cx-channels-custom-values.yaml
           helm upgrade --install --namespace expertflow --set global.efCxReleaseName="ef-cx" --debug cx-channels --values helm-values/cx-channels-custom-values.yaml  expertflow/channels --version 5.2.0-rc.1
[/code]

  9. **Deploy the Campaigns helm chart**
[code] # Deploy the new chart version using the helm-values/cx-campaigns-custom-values.yaml
         helm upgrade --install --namespace expertflow   --set global.efCxReleaseName="ef-cx"  cx-campaigns --debug --values helm-values/cx-campaigns-custom-values.yaml expertflow/campaigns --version 5.2.0-rc.1
[/code]

  10. **Deploy the QM helm chart**
[code] # Deploy the new chart version using the helm-values/cx-qm-custom-values.yaml
           helm upgrade --install --namespace=expertflow --set global.efCxReleaseName="ef-cx" qm  --debug --values=helm-values/cx-qm-custom-values.yaml expertflow/qm --version 5.2.0-rc.1
[/code]



