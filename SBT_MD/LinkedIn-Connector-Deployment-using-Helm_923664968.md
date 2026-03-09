# CX Knowledgebase : LinkedIn Connector Deployment using Helm

### Requirements

  * Kubernetes. [Deployment Planning](/wiki/pages/createpage.action?spaceKey=SBT&title=Deployment%20Planning&linkCreation=true&fromPageId=923664968)
  * Storage Solution [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started)
  * CX Deployement <https://expertflow-docs.atlassian.net/wiki/x/r5Qm>



### Deployment

Add the Expertflow Helm charts repository.
[code] 
    helm repo add expertflow https://expertflow.github.io/charts
[/code]

Update the charts repository
[code] 
    helm repo update expertflow
[/code]

Clone linkdin-connector Repository
[code] 
    git clone -b CX-4.9.5 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git  CX-4.9.5
[/code]
[code] 
    cd CX-4.9.5/kubernetes/
[/code]

### CX Channels

Customise the deployment by fetching the values.yaml file and edit it as per requirements.
[code] 
    vi helm/Channels/values.yaml
[/code]

Edit/update the values file `with`
[code] 
    global:
      ingressRouter: <DEFAULT-FQDN>
[/code]

Deploy the Channels helm chart by
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"   --debug   cx-channels --values  helm-values/cx-channels-custom-values.yaml  helm/Channels
[/code]
