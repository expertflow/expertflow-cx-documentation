# CX Knowledgebase : CX SIP Proxy Deployment Guide

# Overview

CX SIP Proxy is required for voice and video calls. It can be integrated with CISCO voice solutions as well as core Expertflow CX solutions. It is deployed on-premises. The solution consists of various modules that may be configured as required.

As a deployment engineer, you need to be well-versed in the concept of VOIP and SIP Platforms.

# Deployment Modes

CX SIP Proxy requires one or multiple on-premises servers depending upon the deployed mode as described.

| **Single Node Deployment**| **High Availability Deployment**  
---|---|---  
| In single node (non-HA) mode, CX SIP Proxy operates as a single-instance server handling SIP (Session Initiation Protocol) traffic independently. It acts as the central point of communication, facilitating interactions between SIP clients, SIP providers, and other SIP entities. | In high availability mode, CX SIP Proxy is deployed in a redundant and fault-tolerant configuration to ensure continuous operation and minimize downtime. It typically involves multiple instances of CX SIP Proxy distributed across multiple servers or nodes, forming a cluster or failover system.   
**Suitable when**| 

  * The standalone mode in SIP proxy deployment is suitable for scenarios where high availability is not a critical requirement. It can be appropriate for non-critical communication systems where occasional downtime or service interruptions are tolerable.
  * Also, if end users are registered in CX SIP Proxy.

| The High Availability (HA) mode is essential where uninterrupted service is paramount. This mode provides redundancy and fault tolerance, minimizing the risk of downtime due to hardware failures, software issues, or network problems.   
**Limitations**| 

  * In case of server failure, the service will be interrupted. 

| 

  * Service will be interrupted if none of the nodes is live.

  
**Deployment Guide**|  ….| ….  
  
## Deployment Prerequisites

The following are the prerequisites for setting up CX SIP Proxy for up to 1000 concurrent requests :

| **Single Node Deployment**| **High Availability Deployment**  
---|---|---  
**Hardware requirements**| 

  * 4 CPU, 8 GB RAM, 500 GB HDD

| 

  * Each server with 4 CPU, 8GB RAM, 500GB HDD 

  
**Software requirements**| 

  * A server with a Linux-based operating system -Debian 12 
  * PHP 7.4 is necessary as the control panel is most compatible with this version of PHP.

| 

  * Multiple servers with Linux-based operating system - Debian 12 in the same network/subnet
  * PHP 7.4 is necessary on all servers as the control panel is most compatible with this version of PHP.
  * One Virtual IP in the same network

  
**System Access Requirements**| 

  * Administrative privileges (root) on the host machine are required to proceed with installation.

| 

  * Administrative privileges (root) on all the host machines are required to proceed with installation.

  
  
## Port Utilization

The local security policy and firewall should allow open communication on the following ports.

**Type/Protocol**| **Source Host**| **Port**| **Destination**  
---|---|---|---  
TCP| CX SIP Proxy| 5060| any  
UDP| CX SIP Proxy| 5060| any  
BIN (binary)| CX SIP Proxy| 5555| any  
  
## Deploy SIP Proxy

This method for deploying SIP Proxy is currently being defined. Keep watching this space for further developments on this.

Once the pre-requisites are complete, we can proceed to the steps of deploying SIP Proxy.

For **_single node deployment_** , the steps given as follows:

  1. [CX SIP Proxy installation](CX-SIP-Proxy-Installation-Guide_229539941.html)

  2. [Dialplan implementation ](https://expertflow-docs.atlassian.net/wiki/spaces/CT/pages/168460320/Dialplan+implementation+in+EF+SIP+Proxy) to add the media servers

  3. To implement CX SIP Proxy using the [dispatcher module](Load-balancing-in-EF-SIP-Proxy-through-the-dispatcher-module_178684103.html)

  4. Or to implement CX SIP Proxy using the load balancer module( doc remaining)




For **_high availability_** , we need to follow the mentioned processes for each node:

  1. [CX SIP Proxy installation](CX-SIP-Proxy-Installation-Guide_229539941.html)

  2. [Dialplan implementation ](https://expertflow-docs.atlassian.net/wiki/spaces/CT/pages/168460320/Dialplan+implementation+in+EF+SIP+Proxy) to add the media servers

  3. [Dialog and profile replication](Dialog-and-Profile-replication-in-a-cluster-in-EF-SIP-Proxy_176947233.html) in a cluster

  4. [Clustering configuration](HA-in-EF-SIP-Proxy_173670574.html) to make CX SIP Proxy redundant

  5. To implement CX SIP Proxy using the [dispatcher module](Load-balancing-in-EF-SIP-Proxy-through-the-dispatcher-module_178684103.html)

  6. Or to implement CX SIP Proxy using the load balancer module( doc remaining)



