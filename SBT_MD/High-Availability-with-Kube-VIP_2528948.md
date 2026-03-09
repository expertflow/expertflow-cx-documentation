# CX Knowledgebase : High Availability with Kube-VIP

The purpose of this document is to describe steps to deploy an RKE2 Kubernetes cluster in High Availability using Kube-VIP.  
  
# Prerequisites 

The prerequisites and cluster topologies are describe in the [Singe Node Deployment](RKE2-Control-plane-Deployment_2528874.html). Please review the document before proceeding with installation in High Availability mode.

**Nodes / VMs**| | **vCPU**| **vRAM**| **vDisk (GiB)**| **Comments**  
---|---|---|---|---|---  
**CX A**|  Control Plane + CX Core + Channels + StatefulSets| 4| 8| 250| This setup assumes three digital channels. Hardware requirements will increase with each additional channel, requiring approximately 0.5 CPU and 1 GB RAM per channel.  
**CX B**|  Control Plane + CX Core + Channels + StatefulSets| 4| 8| 250| This setup assumes three digital channels. Hardware requirements will increase with each additional channel, requiring approximately 0.5 CPU and 0.5 GB RAM per channel.  
**DiChannels**| | | | |   
**Arbiter**|  Control Plane + Arbiter|  2|  4|  10| The arbiter node ensures quorum during failover scenarios but does not store data or handle traffic  
**Reporting**|  Control Plane + Reporting + ETL| 8| 16| 250| This for Apache Superset and expert flow ETL. HA is not supported for reporting.  
**Voice**|  Media Server|  8|  16|  150| HA is not supported for voice.  
  
## Preparing for Deployment

#### Kube-VIP Requirements

A VIP is a virtual IP Address that remains available and traverses between all the Control-Plane nodes seamlessly with 1 Control-Plane node active to Kube-VIP. Kube-VIP works exactly as keepalive except that it has some additional flexibilities to configure depending upon the environment for example Kube-VIP can work using 

  * ARP – When using ARP or [Layer 2](https://osi-model.com/data-link-layer/) it will use [leader election](https://godoc.org/k8s.io/client-go/tools/leaderelection).




##### Other modes that can also be used such as [BGP](https://kube-vip.io/#bgp), [Routing Table](https://kube-vip.io/#routing-table) and [Wireguard](https://kube-vip.io/#wireguard)

  * In ARP mode same subnet VIP for all the control plane nodes is required

  * Kube-VIP deployment is dependent on the atleast one working RKE2 Control Plane node before we can deploy other nodes ( both CP and Workers ) . 




#### Installation Steps

#### **Step 1: Prepare First Control Plane**

  * <FQDN> is the Kube-VIP FQDN  





**RKE2 Control plane Deployment**

This step is required for the Nginx Ingress controller to allow customized configurations.

### Step 1. Create Manifests

  1. Create necessary directories for RKE2 deployment



[code] 
    mkdir -p /etc/rancher/rke2/
    mkdir -p  /var/lib/rancher/rke2/server/manifests/
[/code]

  1. Generate the ingress-nginx controller config file so that the RKE2 server bootstraps it accordingly.



[code] 
    cat << EOF | tee /var/lib/rancher/rke2/server/manifests/rke2-ingress-nginx-config.yaml
    ---
    apiVersion: helm.cattle.io/v1
    kind: HelmChartConfig
    metadata:
      name: rke2-ingress-nginx
      namespace: kube-system
    spec:
      valuesContent: |-
        controller:
          extraInitContainers:
            - name: ef-set-sysctl
              image: busybox
              securityContext:
                privileged: true
              command:
              - sh
              - -c
              - |
                sysctl -w net.core.somaxconn=65535
                sysctl -w net.ipv4.ip_local_port_range="1024 65535"
          metrics:
            #  DO not enable at the cluster install, enable when monitoring is deployed.
            enabled: false
            service:
              annotations:
                prometheus.io/scrape: "true"
                prometheus.io/port: "10254"
            serviceMonitor:
               #  DO not enable at the cluster install, enable when monitoring is deployed.
               enabled: false
            prometheusRule:
              enabled: false
          config:
            use-forwarded-headers: "true"
            keep-alive-requests: "10000"
            upstream-keepalive-requests: "1000"
            worker-processes: "auto"
            max-worker-connections: "65535"
            use-gzip: "true"
            allow-snippet-annotations: true
            enable-vts-status: true
            annotations-risk-level: "Critical"
            ssl-ciphers: "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:DHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA:ECDHE-RSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES256-SHA256:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:DES-CBC3-SHA"
            ssl-protocols: "TLSv1.2 TLSv1.3"
          extraArgs:
            ## Configures the external IP address used to publish the Ingress status. DO NOT ENABLE/EDIT
            #publish-status-address: "11.22.33.44"
            ## Sets the default SSL certificate for HTTPS traffic. Useful when no specific certificate is defined in the Ingress resource. DO NOT ENABLE/EDIT
            #default-ssl-certificate: "kube-system/wildcard-tls"
            ## Allows encrypted traffic (HTTPS) to be passed directly to the backend without termination at the Ingress. DO NOT ENABLE/EDIT
            #enable-ssl-passthrough: true
            ## Enables HTTP status code breakdowns in metrics. For example, you can see 2XX, 3XX, 4XX, and 5XX response counts grouped together instead individual status codes. DO NOT EDIT
            report-status-classes: true
            ## Prevents requests without matching Ingress rules from being routed to the default backend, improving security and performance DO NOT ENABLE/EDIT
            #disable-catch-all: true
          # Enables fine-grained customizations for specific Ingress resources using annotations.
          allowSnippetAnnotations: "true"
          # Optimizes traffic distribution by routing requests based on topology, such as geographic proximity or network distance.
          enableTopologyAwareRouting: true
    EOF
    
[/code]

Create a deployment manifest called `config.yaml` for RKE2 Cluster and replace the IP addresses and corresponding FQDNS according.

**NOTE:**

  * add any other fields from the Extra Options sections in `config.yaml` at this point . 

  * entry of tls-san can have FQDN and IP addresses of control-plane nodes and worker nodes as well.

  * If you deploying worker HA, uncomment to disable rke2 ingress.



[code] 
    cat<<EOF|tee /etc/rancher/rke2/config.yaml
    #Uncomment for Control-Plane HA    tls-san and its kid entry <FQDN>
    #tls-san:
    #  - <FQDN>
    write-kubeconfig-mode: "0644"
    etcd-expose-metrics: true
    etcd-snapshot-schedule-cron: "0 */6 * * *"
    # Keep 56 etcd snapshorts (equals to 2 weeks with 6 a day)
    etcd-snapshot-retention: 56
    cni:
      - canal
      
    #Uncomment for Worker HA Deployment ONLY
    #disable: 
    #  - rke2-ingress-nginx
    #kube-controller-manager-arg:
    #  - "node-monitor-grace-period=20s"
    
    #Uncoment the following to retain logs for any component without integrating with ELK stack
    #kubelet-arg:                               
    #  - "container-log-max-files=5"            
    #  - "container-log-max-size=10Mi"
    
    # See hostname section above or https://docs.rke2.io/install/requirements#prerequisites
    # node-name
    # with-node-id
      
    EOF
[/code]

In above mentioned template manifest,

  * <FQDN> must be pointing towards the first control plane




### Step 2. Download the RKE2 binaries and start Installation

Following are some defaults that RKE2 uses while installing RKE2. You may change the following defaults as needed by specifying the switches mentioned.

| Switch| Default| Description  
---|---|---|---  
To change the default deployment directory of RKE2| `--data-dir OR -d` | `/var/lib/rancher/rke2` | Important Note: Moving the default destination folder to another location is not recommended. However, if there is need for storing the containers in different partition, it is recommended to deploy the containerd separately and change its destination to the partition where you have space available using `--root` flag in containerd.server manifest, and subsequently adding `#container-runtime-endpoint: "/path/to/containerd.sock"` switch in RKE2 config.yaml file.   
Default POD IP Assignment Range| `--cluster-cidr`| `"10.42.0.0/16"`| IPv4/ network CIDRs to use for pod IPs  
Default Service IP Assignment Range| `--service-cidr` | `"10.43.0.0/16"`| IPv4 network CIDRs to use for service IPs  
  
cluster-cidr and service-cidr are independently evaluated. Decide wisely well before the the cluster deployment. This option is not configurable once the cluster is deployed and workload is running.

Run the following command to install RKE2.
[code] 
    curl -sfL https://get.rke2.io |INSTALL_RKE2_TYPE=server  sh - 
[/code]

  1. Enable the rke2-server service



[code] 
    systemctl enable rke2-server.service
[/code]

  1. Start the service



[code] 
    systemctl start rke2-server.service
[/code]

RKE2 server requires 10-15 minutes (at least) to bootstrap completely You can check the status of the RKE2 Server using` systemctl status rke2-server`; Only procced once everything is up and running or configurational issues might occur requiring redo of all the installation steps.

### Step 3. Kubectl Profile setup

By default, RKE2 deploys all the binaries in 

`/var/lib/rancher/rke2/bin` path. Add this path to the system's default PATH for kubectl utility to work appropriately.
[code] 
    echo "export PATH=$PATH:/var/lib/rancher/rke2/bin" >> $HOME/.bashrc
    echo "export KUBECONFIG=/etc/rancher/rke2/rke2.yaml"  >> $HOME/.bashrc
    source ~/.bashrc
[/code]

### Step 4. Bash Completion for kubectl

  1. Install bash-completion package




####  For Ubuntu:- 
[code] 
    apt install bash-completion -y   
[/code]

####  For RHEL:-
[code] 
    yum install bash-completion -y
[/code]

  2. Set-up autocomplete in bash into the current shell, Also, add alias for short notation of kubectl



[code] 
    kubectl completion bash > /etc/bash_completion.d/kubectl
    echo "source /etc/bash_completion.d/kubectl" >> ~/.bashrc 
    echo "alias k=kubectl"  >> ~/.bashrc 
    echo "complete -o default -F __start_kubectl k"  >> ~/.bashrc 
    source ~/.bashrc
[/code]

### Step 5. Install helm

  1. Helm is a super tool to deploy external components. In order to install helm on cluster, execute the following command: 



[code] 
    curl -fsSL https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3|bash
[/code]

In case the above mentioned command does not work, follow the below mentioned commands:-

#### For Ubuntu:-
[code] 
    curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
    apt-get install apt-transport-https --yes
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
    apt-get update
    apt-get install helm
[/code]

#### For RHEL:-
[code] 
    curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm
    chmod +x /usr/local/bin/helm
    helm version
[/code]

### Step 6. Enable bash completion for helm

  1. Generate the scripts for help bash completion



[code] 
    helm completion bash > /etc/bash_completion.d/helm
[/code]

create link for crictl to work properly.
[code] 
    ln -s /var/lib/rancher/rke2/agent/etc/crictl.yaml /etc/crictl.yaml
[/code]

#### **Step 4: Deploy Kube-VIP**

1\. Decide the IP and the interface on all nodes for Kube-VIP and setup these as environment variables. This step must be completed before deploying any other node in the cluster (both CP and Workers).
[code] 
    export VIP=<FQDN>
    export INTERFACE=<Interface>
[/code]

2\. Import the RBAC manifest for Kube-VIP
[code] 
    curl https://kube-vip.io/manifests/rbac.yaml > /var/lib/rancher/rke2/server/manifests/kube-vip-rbac.yaml
[/code]

3\. Fetch the kube-vip image 
[code] 
    /var/lib/rancher/rke2/bin/crictl -r "unix:///run/k3s/containerd/containerd.sock"  pull ghcr.io/kube-vip/kube-vip:latest
[/code]

4\. Deploy the Kube-VIP 
[code] 
    CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock  ctr -n k8s.io run \
    --rm \
    --net-host \
    ghcr.io/kube-vip/kube-vip:latest vip /kube-vip manifest daemonset --arp --interface $INTERFACE --address $VIP --controlplane  --leaderElection --taint --services --inCluster | tee /var/lib/rancher/rke2/server/manifests/kube-vip.yaml
[/code]

5\. Wait for the kube-vip to complete bootstrapping 
[code] 
    kubectl rollout status daemonset   kube-vip-ds    -n kube-system   --timeout=650s
[/code]

6\. Once the condition is met, you can check the daemonset by kube-vip is running 1 pod 
[code] 
    kubectl  get ds -n kube-system  kube-vip-ds
[/code]

Once the cluster has more control-plane nodes added, the count will be equal to the total number of CP nodes.

#### **Step 5: Remaining Control-Plane Nodes**

Perform these steps on remaining control-plane nodes.

1\. Create required directories for RKE2 configurations.
[code] 
    mkdir -p /etc/rancher/rke2/
    mkdir -p  /var/lib/rancher/rke2/server/manifests/
[/code]

2\. Create a deployment manifest called `config.yaml` for RKE2 Cluster and replace the IP addresses and corresponding FQDNS according (add any other fields from the Extra Options sections in `config.yaml` at this point).
[code] 
    cat<<EOF|tee /etc/rancher/rke2/config.yaml
    server: https://<FQDN>:9345
    token: [token from /var/lib/rancher/rke2/server/node-token on server node 1]
    write-kubeconfig-mode: "0644" 
    tls-san:
      - <FQDN>
    write-kubeconfig-mode: "0644"
    etcd-expose-metrics: true
    cni:
      - canal
    
    EOF
[/code]

  


In above mentioned template manifest, 

  * <FQDN> is the Kube-VIP FQDN




#### Ingress-Nginx config for RKE2

By default RKE-2 based ingress controller doesn't allow additional snippet information in ingress manifests, create this config before starting the deployment of RKE2 
[code] 
    cat<<EOF| tee /var/lib/rancher/rke2/server/manifests/rke2-ingress-nginx-config.yaml
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

#### **Step 6: Begin the RKE2 Deployment**

1\. Begin the RKE2 Deployment
[code] 
    curl -sfL https://get.rke2.io | INSTALL_RKE2_TYPE=server sh -
[/code]

2\. Start the RKE2 service. Starting the Service will take approx. 10-15 minutes based on the network connection
[code] 
    systemctl start rke2-server
[/code]

3\. Enable the RKE2 Service
[code] 
    systemctl enable rke2-server
[/code]

4\. By default, RKE2 deploys all the binaries in `/var/lib/rancher/rke2/bin` path. Add this path to system's default PATH for kubectl utility to work appropriately.
[code] 
    export PATH=$PATH:/var/lib/rancher/rke2/bin
    export KUBECONFIG=/etc/rancher/rke2/rke2.yaml
[/code]

5\. Also, append these lines into current user's `.bashrc` file
[code] 
    echo "export PATH=$PATH:/var/lib/rancher/rke2/bin" >> $HOME/.bashrc
    echo "export KUBECONFIG=/etc/rancher/rke2/rke2.yaml"  >> $HOME/.bashrc 
[/code]

#### **Step 7: Deploy Worker Nodes**

On each worker node,

  1. Run the following command to install RKE2 agent on the worker.
[code] curl -sfL https://get.rke2.io | INSTALL_RKE2_TYPE="agent" sh -
[/code]

  2. Enable the `rke2-agent` service by using the following command.
[code] systemctl enable rke2-agent.service
[/code]

  3. Create a directory by running the following commands.
[code] mkdir -p /etc/rancher/rke2/
[/code]

  4. Add/edit `/etc/rancher/rke2/config.yaml` and update the following fields.

     1. `<Control-Plane-IP>` This is the IP for the control-plane node.

     2. `<Control-Plane-TOKEN>` This is the token which can be extracted from first control-plane by running `cat /var/lib/rancher/rke2/server/node-token`
[code] server: https://<Control-Plane-IP>:9345
            token: <Control-Plane-TOKEN>
[/code]

  5. Start the service by using follow command.
[code] systemctl start rke2-agent.service
[/code]



  1. Choose storage - See [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started)

  2. [CX-Core deployment on Kubernetes](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528385)




  


  


  


  

