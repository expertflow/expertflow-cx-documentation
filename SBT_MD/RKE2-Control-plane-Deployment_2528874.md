# CX Knowledgebase : RKE2 Control plane Deployment

This guide covers prerequisites and steps to install RKE2 on the control plane of Expertflow CX.

## Checklist

RKE2 supported OS list is subject to frequent updates, to verify whether your OS is supported visit this link at [Official RKE2 Supported Platforms](https://docs.rke2.io/install/requirements#operating-systems)

  * Is Internet access available on the target node? If not available, check RKE2 [Official Air-Gapped install of RKE2](https://docs.rke2.io/install/airgap) or [Air-Gap Install for RKE-2 Kubernetes](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/463077539/Air-Gap+Install+for+RKE-2+Kubernetes) for offline deployment.
  * The node is running RKE2 supported OS. [RKE2 installation requirements](https://docs.rke2.io/install/requirements#prerequisites)
  * FQDN should be mapped to the underlying node IP. 
  * All nodes are synchronizing date/time using NTP.
  * FirewallD or UFW is setup appropriately. We recommend to disable the firewall, however, if this is required, please open all the network port mentioned <https://docs.rke2.io/install/requirements#networking>
  * When using RKE2 in HA , the Virtual-IP is allocatable to all the Control-Plane nodes.
  * If your environment allows internet connectivity through an HTTP proxy, follow [Configure an HTTP proxy](https://docs.rke2.io/advanced#configuring-an-http-proxy) to configure your proxy as per RKE2 recommendations. 



## Environment Preparation

### For Ubuntu based deployments

  1. Disable the firewall
[code] systemctl disable firewalld --now
         systemctl disable apparmor.service
         systemctl disable ufw --now
         reboot
[/code]

  2. update the release to latest revision  (Optional)
[code] apt update
         apt upgrade -y
[/code]




### For RHEL

  1. Disable the firewall
[code] systemctl disable firewalld --now
         systemctl disable nm-cloud-setup.service nm-cloud-setup.timer
         systemctl disable apparmor.service
         reboot
[/code]

  2. Lock the release to the supported version of RHEL 
[code] # The following command set assumes that the supported RHEL version is 8.5
         subscription-manager release --set=8.5; 
         yum clean all;
         subscription-manager release --show;
         rm -rf /var/cache/dnf
[/code]

  3. Update the RHEL packages for supported release (Optional)
[code] yum update -y
[/code]




## Set Hostname

Only when deploying multi-node Cluster with Control-plane HA or Worker-HA 

  * If two or more of your machines have the same hostname ( you can verify the hostname using `hostname ` command on all nodes ), you must do one of the following:

    * Update the hostname to a unique value

    * OR set the `node-name` parameter in the config file to a unique value

    * OR set the `with-node-id` parameter in the config file to `true` to append a randomly generated ID number to the hostname.




To set a hostname, run the following command:-

If you are deploying a multi-node cluster, each node should have a unique hostname.
[code] 
    hostnamectl set-hostname <hostname>
[/code]

To check the hostname, run the following command:-
[code] 
    hostname
[/code]

### Enable Extended TLS/SSL certificates for RKE2 ( mandatory for all node types ) 

Create the directory if it doesn't exist
[code] 
    mkdir -p /usr/local/lib/systemd/system/rke2-server.env.d/
[/code]

Add the variable to the environment file
[code] 
    echo "CATTLE_NEW_SIGNED_CERT_EXPIRATION_DAYS=3650" >> /etc/default/rke2-server
[/code]

### Enable kernel tunning for Kubernetes

Run this code block for all the nodes in all deployment modes for example Worker-HA, Control-Plane HA and single Node deployments
[code] 
    cat << EOF > /etc/sysctl.d/99-expertflow.conf
    # SWAP settings
    vm.swappiness=0
    vm.panic_on_oom=0
    vm.overcommit_memory=1
    kernel.panic=10
    kernel.panic_on_oops=1
    vm.max_map_count = 262144
    # Have a larger connection range available
    net.ipv4.ip_local_port_range=1024 65000
    # Increase max connection
    net.core.somaxconn=10000
    # Reuse closed sockets faster
    net.ipv4.tcp_tw_reuse=1
    net.ipv4.tcp_fin_timeout=15
    # The maximum number of "backlogged sockets".  Default is 128.
    net.core.netdev_max_backlog=10000
    # 16MB per socket - which sounds like a lot,
    # but will virtually never consume that much.
    net.core.rmem_max=16777216
    net.core.wmem_max=16777216
    # Various network tunables
    net.ipv4.tcp_max_syn_backlog=20480
    net.ipv4.tcp_max_tw_buckets=400000
    net.ipv4.tcp_no_metrics_save=1
    net.ipv4.tcp_rmem=4096 87380 16777216
    net.ipv4.tcp_syn_retries=2
    net.ipv4.tcp_synack_retries=2
    net.ipv4.tcp_wmem=4096 65536 16777216
    # ARP cache settings for a highly loaded docker swarm
    net.ipv4.neigh.default.gc_thresh1=8096
    net.ipv4.neigh.default.gc_thresh2=12288
    net.ipv4.neigh.default.gc_thresh3=16384
    # ip_forward and tcp keepalive for iptables
    net.ipv4.tcp_keepalive_time=600
    net.ipv4.ip_forward=1
    # monitor file system events
    fs.inotify.max_user_instances=8192
    fs.inotify.max_user_watches=1048576
    net.netfilter.nf_conntrack_max=1048576
    EOF
    
    sysctl --system > /dev/null 2>&1
[/code]

# Installation Steps

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
