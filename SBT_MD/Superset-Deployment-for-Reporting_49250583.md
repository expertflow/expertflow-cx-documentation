# CX Knowledgebase : Superset Deployment for Reporting

Deprecated. Use CX Analyzer.   
  
Reporting server

Superset will be deployed in `ef-bi` namespace. Run the following command on the master node.
[code] 
    kubectl create namespace ef-bi
[/code]

Create image pull secret for `ef-bi` namespace.
[code] 
    kubectl apply -f pre-deployment/registryCredits/ef-imagePullSecret-ef-bi.yaml
[/code]

Add the charts repository
[code] 
    helm repo add expertflow https://expertflow.github.io/charts
[/code]

update the repository
[code] 
    helm repo update expertflow
[/code]

clone the values file and update the parameters
[code] 
    mkdir helm-values
[/code]

clone the values file for elasticsearch
[code] 
    helm show values expertflow/superset > helm-values/superset-custom-values.yaml
[/code]

Edit the `helm-values/superset-custom-values.yaml` file and update

By default superset is exposed using node port ( default port 30808 ). Use [http://nodeport:30808](https://nodeport:30808) for accessing superset over insecure http

  * If superset is required to be accessible over internet using FQDN using https

    * Add TLS Certificates in `ef-bi`namespace by following any of the below methods

      * For Self-Signed please use this guide [Create self-signed certificates](Create-self-signed-Certificates-for-Ingress_48400625.html)

      * For Commercial Certificates, please import them as `tls.crt` and `tls.key` and create secret with the name of `ef-ingress-tls-secret` in `ef-bi` namespace

      * For LetsEncrypt(LE) based TLS Certificates please consult guide [LetsEncrypt SSL for EF-CX](LetsEncrypt-SSL-for-EF-CX_32538676.html)

    * enable ingress to true in `helm-values/superset-custom-values.yaml` . By default ingress nginx is supported, however for other ingress controllers change the ingress → annotations




Superset for reporting requires a dedicated FQDN ( separate sub-domain from EF-CX ) when using ingress. Please setup accordingly.

Deploy the superset 
[code] 
    helm upgrade --install --namespace ef-bi --create-namespace --values=helm-values/superset-custom-values.yaml superset expertflow/superset
[/code]

wait for the deployments to complete. the superset shall be available via either nodeport 30808 or <https://FQDN/> depending upon the configuration made in values file.
