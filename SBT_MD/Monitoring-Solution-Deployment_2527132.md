# CX Knowledgebase : Monitoring Solution Deployment

## Requirements

**vCPU**| **vRAM**| **vDisk (GiB)**| **Comments**  
---|---|---|---  
2| 4| 150| Dedicated Node is recommended for the monitoring solution.   
  
This document covers the process of deploying the Monitoring solution stack for CX. This stack consists of the following components.

  1. Prometheus

  2. Grafana

  3. Alertmanager

  4. Node Exporter




The Prometheus operator includes the following features:

  * **Kubernetes Custom Resources** : Use Kubernetes custom resources to deploy and manage Prometheus, Alertmanager, and related components.

  * **Simplified Deployment Configuration** : Configure the fundamentals of Prometheus like versions, persistence, retention policies, and replicas from a native Kubernetes resource.

  * **Prometheus Target Configuration** : Automatically generate monitoring target configurations based on familiar Kubernetes label queries; no need to learn a Prometheus-specific configuration language.




## Deployment

Monitoring stack helm chart is customized to accommodate the monitoring requirements of the CX Solution monitoring.

add the helm repository
[code] 
    helm repo add expertflow https://expertflow.github.io/charts
[/code]

update the repository
[code] 
    helm repo update expertflow
[/code]

make the directory
[code] 
    mkdir helm-values
[/code]

customize the parameters by cloning the values file
[code] 
    helm show values expertflow/kube-prometheus-stack > helm-values/kube-prometheus-stack-values.yaml
[/code]

  * create monitoring namespace 
[code] kubectl create namespace monitoring
[/code]

  * Alert Manager Ingress (Optional)

    * alert-manager ingress is disabled by default as it can be explored publicly by anyone without any authentication, exposing potentially critical information . However if this is required, please follow these steps

      * Create an apache2 pod by running 
[code] kubectl run apache2 --image=bitnami/apache2 
[/code]

      * Create secret using. Change the password placeholder <CHANGE_ME> with the required value.
[code] kubectl -n monitornig create secret generic  basic-auth  --from-literal=auth="$(kubectl exec -ti apache2 -- bash -c 'echo <CHANGE_ME>|htpasswd -i -n monitoring')" 
[/code]

      * Delete the apache2 pod 
[code] kubectl delete pod apache2
[/code]

  * Prometheus Ingress (Optional)

    * Prometheus ingress is disabled by default as it can be explored publicly by anyone without any authentication, exposing potentially critical information . However if this is required ( skip these steps if already completed for alert-manager as both ingresses use same auth token and credentials as kubernetes secret.)

      * Create an apache2 pod by running 
[code] kubectl run apache2 --image=bitnami/apache2 
[/code]

      * Create secret using. Change the password placeholder <CHANGE_ME> with the required value.
[code] kubectl -n monitornig create secret generic  basic-auth  --from-literal=auth="$(kubectl exec -ti apache2 -- bash -c 'echo <CHANGE_ME>|htpasswd -i -n monitoring')" 
[/code]

      * Delete the apache2 pod
[code] kubectl delete pod apache2
[/code]

  * EFSwitch Monitoring Dashboards (Optional)

    * Please Update the EFSwitch IP in `additionalScrapeConfigs:` section in `helm-values/kube-prometheus-stack-values.yaml`, for Prometheus to start fetching statistics from exporters running on EFSwitch node .

      * 
[code]- job_name: "node"
                      static_configs:
                        - targets: ["<IP>:9100"]
            
                    - job_name: 'freeswitch'
                      static_configs:
                        - targets: ["<IP>:9282"]
            
                    - job_name: 'fusionpbx'
                      scrape_interval: 60s
                      static_configs:
                        - targets: ['<IP>:8080']
[/code]




Considerations to cater for when changing values file `helm-values/kube-prometheus-stack-values.yaml`

  * Replace all occurrences of `devops.ef.com` to FQDN. You can use `sed -i -e 's/devops.ef.com/<FQDN>/g' helm-values/kube-prometheus-stack-values.yaml`

  * change the default password for grafana admin user under grafana section. optionally command `sed -i -e 's/Expertflow123/<CUSTOM_PASSWORD>/g' helm-values/kube-prometheus-stack-values.yaml` can also be used 

  * change the retention period for prometheus. default 30 days. command to substitute this parameter can be `sed -i -e 's/^retention: 30d/retention: <NUMBER_OF_DAYS>d' helm-values/kube-prometheus-stack-values.yaml`

  * If the monitoring solution is to be deployed on a specific node in cluster, update the `nodeSelector` term for Alert-Manager, Grafana and Prometheus or use appropriate `nodeAffinity` terms for proper placement plan of monitoring solution.

  * Create secret containing TLS certificates in `monitoring` namespace. All ingress resources use `ef-ingress-tls-secret` as secret name for TLS encryption.

    * For Self Signed please use this guide [Create self-signed certificates for ingress](Create-self-signed-Certificates-for-Ingress_48400625.html)

    * For commercial SSL/TLS certificates, please import them as `tls.crt` and `tls.key` and create secret with the name of `ef-ingress-tls-secret` in both ef-external and expertflow namespaces

    * For LetsEncrypt based SSL/TLS Certificates please consult [LetsEncrypt SSL for EF-CX](LetsEncrypt-SSL-for-EF-CX_32538676.html)

  * update the Grafana password (adminPassword) . The default password is Expertflow123 




Deploy the monitoring Solution stack helm chart.
[code] 
    helm upgrade --namespace monitoring --install=true kube-stack-prometheus --values=helm-values/kube-prometheus-stack-values.yaml  expertflow/kube-prometheus-stack
[/code]

after all the pods created successfully, you can access the monitoring solution using <https://FQDN>>/monitoring with these credentials

Username: admin

Password: `Password set in helm-values/kube-prometheus-stack-values.yaml` Default Password is Expertflow123

#### Teardown 

These steps will remove the monitoring solution along with its persistent volumes

Uninstall the monitoring solution 
[code] 
    helm --namespace monitoring uninstall  kube-stack-prometheus 
[/code]

list all the Persistent Volumes Claims
[code] 
    kubectl -n monitoring get pvc
[/code]

delete pvc pairs by executing
[code] 
    kubectl -n monitoring  delete pv <PVC_NAME>
[/code]

delete all the CRDs related to monitoring solution
[code] 
    kubectl delete crd alertmanagerconfigs.monitoring.coreos.com
    kubectl delete crd alertmanagers.monitoring.coreos.com
    kubectl delete crd podmonitors.monitoring.coreos.com
    kubectl delete crd probes.monitoring.coreos.com
    kubectl delete crd prometheusagents.monitoring.coreos.com
    kubectl delete crd prometheuses.monitoring.coreos.com
    kubectl delete crd prometheusrules.monitoring.coreos.com
    kubectl delete crd scrapeconfigs.monitoring.coreos.com
    kubectl delete crd servicemonitors.monitoring.coreos.com
    kubectl delete crd thanosrulers.monitoring.coreos.com
[/code]

finally delete the namespace
[code] 
    kubectl delete namespace monitoring
[/code]

IMPORTANT: if you have metrics enabled for any components like mongo, redis etc, disable the metric section in their corresponding helm chart’s values file. 
