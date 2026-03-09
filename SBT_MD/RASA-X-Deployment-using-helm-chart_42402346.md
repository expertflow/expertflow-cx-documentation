# CX Knowledgebase : RASA-X Deployment using helm chart

# Deployment prerequisites  
  
**Type**| **RAM (GB)**| **CPU**| **DISK**| **Scalability**| **Network Ports**| **Minimum Nodes**  
---|---|---|---|---|---|---  
**Single-Node**| **Multi-Node**| **Single-Node**| **Multi-Node**| **Single-Node**| **Multi-Node**  
RKE21| 8| 8| 250 GiB | 250GiB (preferably on /var)| No| High| 

  * 6443/TCP and 9345 to be accessible by all nodes
  * 8472/UDP for CNI
  * 10250/TCP for metrics-server
  * 2379-2380/TCP for Cluster HA (Ports info can be found [here](https://docs.rke2.io/install/requirements))

| 1| 2+  
  
### RASA-X 

Rasa-X deployment on same node is not recommended . Install it on a separate node to deploy a production ready system. Deploying on the same node severely degrades the overall performance

  1. Create the rasa-x namespace using
[code] kubectl create namespace rasa-x
[/code]

  2. Add the image pull secrets for rasa-x
[code] kubectl apply -f pre-deployment/registryCredits/ef-imagePullSecret-rasa-x.yaml
[/code]

  3. Add the Nginx customized config for RASA-X as Confirg-Map
[code] kubectl create -f pre-deployment/rasa-x-1.1.2/ef-rasa-x-nginx-standard-conf.yaml
[/code]




### Update the FQDN parameter for RASA-X

  1. Change the <CIM-FQDN> with your actual FQDN for CIM Solution.
[code] sed -i -e 's@value: http://devops.ef.com/bot-framework@value: https://<CIM-FQDN>/bot-framework@' external/rasa-x/values-small.yaml
[/code]

  2. And
[code] sed -i -e 's@value: https://devops.ef.com@value: https://<CIM-FQDN>@' external/rasa-x/values-small.yaml
[/code]

  3. Install the rasa-x using helm command
[code] helm  upgrade --install=true --wait=true --timeout=10m0s --debug   rasa-x    --namespace rasa-x     --values external/rasa-x/values-small.yaml  external/rasa-x
[/code]




Rasa-x deployment may take longer than expected due to dependency on huge image sizes and may throw warning like `Error: timed out waiting for the condition` , however the deployment continues. You can check the status of the deployment by running ` kubectl get pods -n rasa-x ` which shall give more recent information.

  4. You RASA-X service is available through HTTP **30800** NodePort on all the nodes' IP Addresses in your Cluster.



