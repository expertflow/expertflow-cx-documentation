# CX Knowledgebase : Deploy Rasa for Multitenancy

**Overview**  
The **MTT Rasa Deployment** is designed to support multiple customers by deploying separate Rasa instances for each tenant. Since Rasa does not natively support multi-tenancy, each customer’s chatbot is deployed in its own Kubernetes namespace with a dedicated Rasa server, action server, and configuration. A single MinIO instance is deployed once and acts as centralized storage, where each tenant has its own bucket to store and manage trained Rasa models. This setup ensures complete isolation of data, models, and configurations for every customer while allowing easy scalability and management through Helm-based deployments.  
  
****  
C**lone**
[code] 
    git clone https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/bot/rasa/rasa-deployment.git -b 3.6.20 /home/rasa && cd /home/rasa
[/code]

#### Pull Images
[code] 
    CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock /var/lib/rancher/rke2/bin/ctr -n k8s.io i pull -u efcx:RecRpsuH34yqp56YRFUb gitimages.expertflow.com/general/minio:2022.10.5-debian-11-r1
    CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock /var/lib/rancher/rke2/bin/ctr -n k8s.io i pull -u efcx:RecRpsuH34yqp56YRFUb gitimages.expertflow.com/bot/rasa/rasa:3.6.20
    CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock /var/lib/rancher/rke2/bin/ctr -n k8s.io i pull -u efcx:RecRpsuH34yqp56YRFUb gitimages.expertflow.com/general/redis:7.4.2-debian-12-k8s
    CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock /var/lib/rancher/rke2/bin/ctr -n k8s.io i pull -u efcx:RecRpsuH34yqp56YRFUb gitimages.expertflow.com/bot/rasa/rasa-action-server:3.6.2-rich
[/code]

**Deploy Minio**  
Do not need to deploy Minio for every time just need to deploy once
[code] 
    helm install minio chart/minio --create-namespace -f chart/minio/values.yaml -n <tenant-name>
[/code]

  * Once deployed access through [https://{IP}:30901/](https://83.171.249.11:30901/buckets)

  * Login Minio with Default creds  
username: `minioadmin`  
Password: `minioadmin`

  * Create buckets with tenant name & upload the specific model file


![image-20250805-143818.png](attachments/1226113282/1227292733.png?width=936)

**Deploy Rasa**  
first copy the existing rasa folder with the new tenant name
[code] 
    cd /home
    cp rasa <tenant-name>
    cd <tenant-name>
[/code]

  * Edit the file rasa.yaml

  * set the model name & bucket name accordingly  



![image-20250805-144319.png](attachments/1226113282/1227325492.png?width=465)

  * For every new tenant you have to copy the existing folder with new tenant name and change the bucket & model name in `rasa.yaml` file accordingly  


![image-20250805-144554.png](attachments/1226113282/1227227175.png?width=208)

  * Update you custom actions (If any)

    * Delete existing action files in the `actions` directory and place you custom action files

    * Update the volume path of actions  
Open the `actions.yaml` file and update the `hostPath > path` according to your tenant `(/home/<tenant-name>/actions)`

![image-20251124-132009.png](attachments/1226113282/1480687892.png?width=729)



  * Update the port (If required)  
By default, the Rasa service is configured to expose port****`30505`. If this port is already in use or if network requirements dictate a specific port assignment, you can modify the configuration in the deployment manifest.

    * Open the `rasa.yml` configuration file.

    * Navigate to the `Service` section.

    * Locate the `nodePort` field under `ports`.

    * Update the value to your desired port number (ensuring it is within the valid range from 30000 to 32767).




#### installation
[code] 
    helm install rasa chart/rasa --create-namespace -f rasa.yaml -n <tenant-name>
    helm install rasa-action-server chart/rasa-action-server --create-namespace -f actions.yaml -n <tenant-name>
[/code]

## Uninstallation

#### Rasa
[code] 
    helm uninstall rasa -n <tenant-name>
    helm uninstall rasa-action-server -n <tenant-name>
[/code]

#### Minio
[code] 
    helm uninstall minio -n <tenant-name>
[/code]
