# CX Knowledgebase : EFSwitch Monitoring Dashboards

This document illustrates deployment of EFSwitch monitoring dashboards in monitoring solution.

# Before you begin, verify

  * Have already set up monitoring solution. If not yet, see [Monitoring Solution Deployment](Monitoring-Solution-Deployment_2527132.html)



## Clone the Expertflow CX repository
[code] 
    git clone -b CX-4.9_f-CCC-1678 https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git CX-4.9_f-CCC-1678
[/code]

#### Create a Namespace 
[code] 
    kubectl create ns monitoring
[/code]
[code] 
    cd cim-solution/kubernetes/monitoring
[/code]

## Adding EFSwitch IP

  * Please Update the EFSwitch IP in `additionalScrapeConfigs:` section in `values.yaml`, for Prometheus to start fetching statistics from exporters running on EFSwitch node .

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




Considerations to cater for when changing values file `values.yaml`

  * Replace all occurrences of `devops.ef.com` to FQDN. You can use `sed -i -e 's/devops.ef.com/<FQDN>/g' values.yaml`




## Upgrading Monitoring Solution

run the following helm command to upgrade the monitoring solution to new version.
[code] 
    helm upgrade --namespace monitoring --install=true kube-stack-prometheus --values=values.yaml  .
[/code]

## Verify Dashboards

Open the following link in the browser to visit Grafana dashboards.

<FQDN>/monitoring

search dashboards with names including “EFswitch“ to verify each dashboard is reflecting data.
