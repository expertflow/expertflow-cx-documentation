# CX Knowledgebase : High Availability using External Load Balancer

You may use any external load balancer for high availability of your Kubernetes cluster. This document covers the configuration of an NGINX as an external load balancer for an RKE2 Kubernetes cluster.

## Load Balancer Hardware Requirements

**Type**| **RAM (GiB)**| **vCPU**| **DISK (GiB)**| **Scalability**| **Network Ports**| **Minimum Nodes**  
---|---|---|---|---|---|---  
Load-Balancer| 2| 1| 100| Single-Node| 6443, 9345,80,443 to all CP/Worker Nodes nodes| 1  
  
Load Balancer without HA is the single point of failure in the cluster setup and customers are required to set up either of the above in a failover cluster.

# Configuration Steps

## 1\. DNS configurations

In your DNS, map your FQDN to a record or a CNAME pointing to the load balancer IP or hostname. Given below is a sample configuration for NGINX as an ELB. 

## 2\. Deploy an ELB

[Deploy NGINX as an ELB](Deploy-NGINX-as-an-ELB_75860951.html)

[Deploy HAProxy as an ELB](Deploy-HAProxy-as-an-ELB_76021764.html)

##   
3\. Deploy the cluster in HA using LoadBalancer

### 3.1. Deploy RKE2 on the first control plane

  1. Create a deployment manifest called `config.yaml` for the RKE2 cluster and replace the IP address. 




Assuming that the Load balancer is running on `1.1.1.1` with the FQDN `cx.customer-x.com`. 
[code] 
    cat<<EOF|tee /etc/rancher/rke2/config.yaml
    tls-san:
      - cx.customer-x.com
      - 1.1.1.1
    write-kubeconfig-mode: "0600"
    etcd-expose-metrics: true
    cni:
      - canal
    
    EOF
[/code]

  2. For the first control plane setup, install RKE2 [RKE2 Control plane Deployment](RKE2-Control-plane-Deployment_2528874.html)

  3. Retrieve the joining token from the control plane you need to use to install the remaining control plane nodes.
[code] cat /var/lib/rancher/rke2/server/node-token
[/code]




### 3.2. Deploy RKE2 on remaining control plane nodes

  1. Create a deployment manifest called `config.yaml`




Assuming that the Load balancer is running on `1.1.1.1` with the FQDN `cx.customer-x.com`. 
[code] 
    cat<<EOF|tee /etc/rancher/rke2/config.yaml
    server: https://1.1.1.1:9345
    # speicfy the token as retrieved in the first control plane deployment
    token: [token-string]
    tls-san:
      - cx.customer-x.com
    write-kubeconfig-mode: "0644"
    etcd-expose-metrics: true
    cni:
      - canal
    
    EOF
[/code]

  2. Install RKE2 [RKE2 Control plane Deployment](RKE2-Control-plane-Deployment_2528874.html)**** on all the remaining control plane nodes.




## 4\. Deploy Worker Nodes

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




At this point, you have the RKE2 Kubernetes cluster ready using a load balancer.

## 5\. Verify the cluster setup

On the control-plane node run the following command to verify that the worker(s) have been added.
[code] 
    kubectl get nodes -o wide
[/code]

## Next Steps

  1. Choose and install a cloud-native storage. See [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started) for choosing the right storage solution for your deployment.

  2. Deploy Expertflow CX following [Expertflow CX Deployment on Kubernetes](https://docs.expertflow.com/display/CX/Expertflow+CX+Deployment+on+Kubernetes)




  


  


  


  

