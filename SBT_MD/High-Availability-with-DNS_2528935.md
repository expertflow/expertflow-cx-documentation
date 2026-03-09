# CX Knowledgebase : High Availability with DNS

The purpose of this document is to describe the steps to deploy an RKE2 Kubernetes distribution in high availability with DNS.

## Prerequisites

**Nodes / VMs**| | **vCPU**| **vRAM**| **vDisk (GiB)**| **Comments**  
---|---|---|---|---|---  
**CX A**|  Control Plane + CX Core + Channels + StatefulSets| 4| 8| 250| This setup assumes three digital channels. Hardware requirements will increase with each additional channel, requiring approximately 0.5 CPU and 1 GB RAM per channel.  
**CX B**|  Control Plane + CX Core + Channels + StatefulSets| 4| 8| 250| This setup assumes three digital channels. Hardware requirements will increase with each additional channel, requiring approximately 0.5 CPU and 0.5 GB RAM per channel.  
**DiChannels**| | | | |   
**Arbiter**|  Control Plane + Arbiter|  2|  4|  10| The arbiter node ensures quorum during failover scenarios but does not store data or handle traffic  
**Reporting**|  Control Plane + Reporting + ETL| 8| 16| 250| This for Apache Superset and expert flow ETL. HA is not supported for reporting.  
**Voice**|  Media Server|  8|  16|  150| HA is not supported for voice.  
  
## Preparing for Deployment

All control-plane nodes must be ready as per the environment preparation mentioned in [https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528874/RKE2+Control+plane+Deployment#Environment-Preparation](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2528874/RKE2+Control+plane+Deployment#Environment-Preparation).

## Installation and Configuration Steps

### 1\. Setup DNS Configurations

For DNS-based load balancing you need to set up a virtual FQDN that can point to all control plane nodes. Contact your network administrator to do that. 

  * The DNS server should perform health checks on the Control-Plane nodes' availability on ports `6443`, `9345`, `80,` and `443`. Otherwise routing to control-plane nodes will have to be managed manually.




### Step 2. Create the first Control Plane node

Follow [RKE2 Control plane Deployment](RKE2-Control-plane-Deployment_2528874.html) to create the first control-plane node. 

Get the server node token from the first control plane. This is required for adding the remaining control plane and worker nodes.
[code] 
    cat /var/lib/rancher/rke2/server/node-token
[/code]

### Step 3. Adding Remaining Control Plane Nodes

Before proceeding, make sure your control plane environment is ready following [https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528874/RKE2+Control+plane+Deployment#Environment-Preparation](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2528874/RKE2+Control+plane+Deployment#Environment-Preparation)

  1. Create the directories as listed below in the control plane nodes to be added.
[code] mkdir -p /etc/rancher/rke2/
         mkdir -p  /var/lib/rancher/rke2/server/manifests/
[/code]

  2. Create a deployment manifest called `config.yaml` and replace <FQDN> with the FQDN/IP of the first control plane. Kid entry of tls-san can have FQDN and IP addresses of control-plane nodes and worker nodes as well.
[code] cat<<EOF|tee /etc/rancher/rke2/config.yaml
         server: https://<FQDN>:9345
         token: [token from /var/lib/rancher/rke2/server/node-token on server node 1]
         write-kubeconfig-mode: "0644" 
         tls-san:
           - <FQDN>
         etcd-expose-metrics: true
         # Make a etcd snapshot every 6 hours
         etcd-snapshot-schedule-cron: "0 */6 * * *"
         # Keep 56 etcd snapshorts (equals to 2 weeks with 6 a day)
         etcd-snapshot-retention: 56
         cni:
           - canal
         
         EOF
[/code]



  3. Ingress-Nginx config for RKE2 \- By default the RKE-2-based ingress controller does not allow additional snippet information in ingress manifests, create this config before starting the deployment of RKE2.
[code] cat<<EOF| tee /var/lib/rancher/rke2/server/manifests/rke2-ingress-nginx-config.yaml
         ---
         apiVersion: helm.cattle.io/v1
         kind: HelmChartConfig
         metadata:
           name: rke2-ingress-nginx
           namespace: kube-system
         spec:
           valuesContent: |-
             controller:
               metrics:
                 service:
                   annotations:
                     prometheus.io/scrape: "true"
                     prometheus.io/port: "10254"
               config:
                 use-forwarded-headers: "true"
               allowSnippetAnnotations: "true"
         EOF
[/code]




### Step 4. Install RKE2 HA with DNS

  1. Begin the RKE2 Deployment. Starting the Service will take approx. 10-15 minutes based on the network connection
[code] curl -sfL https://get.rke2.io |INSTALL_RKE2_TYPE=server  sh - 
[/code]

  2. Start the RKE2 service
[code] systemctl start rke2-server
[/code]

  3. Enable the RKE2 Service
[code] systemctl enable rke2-server
[/code]

  4. By default, RKE2 deploys all the binaries in`/var/lib/rancher/rke2/bin` path, add this path to the system's default PATH for kubectl utility to work appropriately
[code] export PATH=$PATH:/var/lib/rancher/rke2/bin
         export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
[/code]

  5. Append these lines to the current user's `.bashrc` file.
[code] echo "export PATH=$PATH:/var/lib/rancher/rke2/bin" >> $HOME/.bashrc
         echo "export KUBECONFIG=/etc/rancher/rke2/rke2.yaml"  >> $HOME/.bashrc 
[/code]




### Step 5. Deploy Worker Nodes

Follow the Deployment Prerequisites from [(4.5) RKE2 Control plane Deployment](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/155222298/4.5+RKE2+Control+plane+Deployment) for each worker node before deployment i.e disable firewall on all worker nodes.

On each worker node, make sure a unique hostname is set beforehand.

To set a hostname, run the following command:-
[code] 
    hostnamectl set-hostname <hostname>
[/code]

To check the hostname, run the following command:-
[code] 
    hostname
[/code]

Once hostnames are set, follow these commands on each node to deploy worker nodes.

  1. Run the following command to install the RKE2 agent on the worker.
[code] curl -sfL https://get.rke2.io | INSTALL_RKE2_TYPE="agent" sh -
[/code]

  2. Enable the `rke2-agent` service by using the following command.
[code] systemctl enable rke2-agent.service
[/code]

  3. Create a directory by running the following commands.
[code] mkdir -p /etc/rancher/rke2/
[/code]

  4. Add/edit `/etc/rancher/rke2/config.yaml` and update the following fields.

     1. `<Control-Plane-IP>` This is the IP for the first control-plane node.

     2. `<Control-Plane-TOKEN>` This is the token from Step 2.
[code] server: https://<Control-Plane-IP>:9345
            token: <Control-Plane-TOKEN>
[/code]

  5. Start the service by using the following command.
[code] systemctl start rke2-agent.service
[/code]




### Next Steps

  1. Choose storage - See [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started)

  2. [CX-Core deployment on Kubernetes](/wiki/pages/createpage.action?spaceKey=SBT&title=CX%20Deployment%20on%20Kubernetes&linkCreation=true&fromPageId=2528935)




.

  


  

