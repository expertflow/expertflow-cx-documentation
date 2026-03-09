# CX Knowledgebase : WFM as a CX add-on - Prerequisites

This document outlines the hardware and software requirements for deploying CX Workforce Management as a CX add-on. 

To deploy CX WFM for Cisco & EFCX, follow ![\(blue star\)](images/icons/emoticons/72/2753.png)

## Frontend Requirements

#### **Hardware Requirement**

**Attribute**| | |   
---|---|---|---  
Agents| 50| 300| 1000  
Processor| 3 vCPUs| 6 vCPUs| 16 vCPU  
Memory (RAM)| 6 GB| 8 GB| 32 GB  
Storage| SSD with at least 50 GB of free space| 75 GB of free space| 150GB  
Supported Browsers| Google Chrome 127.0.6533.73 (64-bit)Microsoft Edge 127.0.2651.105 (64-bit) | Google Chrome 128.0.6613.85 (64-bit)Microsoft Edge 128.0.2739.42 (64-bit)| Google Chrome 128.0.6613.85 (64-bit)Microsoft Edge 128.0.2739.42 (64-bit)  
  
#### **Software Requirement**

**Software Component**| **Requirement**  
---|---  
**Operating System**|  Minimum: Ubuntu 20.04 LTS or equivalentRecommended: Ubuntu 22.04 LTS or equivalent  
**Kubernetes**|  Version 1.22 or higher  
**Docker**|  Version 20.10 or higher  
**Helm**|  Version 3.0 or higher  
**Kubeadm**|  For setting up the Kubernetes cluster  
  
## Backend Requirements

#### **Hardware Requirements for Kubernetes Deployment**

There are two kinds of nodes requirement; Master Node(s) and Worker Node(s).

**Master Node(s):**

**Component**| **Minimum Requirements**| **Recommended Requirements**  
---|---|---  
**Agents**|  50| 300  
**Processor**|  6 vCPUs (e.g., Intel Core i5 or equivalent)| 8 vCPUs Octa-core processor (e.g., Intel Xeon or equivalent)  
**RAM**|  16 GB| 32 GB or more  
**Storage**|  500 GB SSD| 800 GB SSD with NVMe  
**Network**|  1 Gbps Ethernet| 10 Gbps Ethernet  
  
**Worker Node(s):**

**Component**| **Minimum Requirements**| **Recommended Requirements**  
---|---|---  
**CPU**|  Quad-core processor (e.g., Intel Core i5 or equivalent)| Octa-core processor (e.g., Intel Xeon or equivalent)  
**RAM**|  8 GB| 16 GB or more  
**Storage**|  100 GB SSD| 500 GB SSD with NVMe  
**Network**|  1 Gbps Ethernet| 10 Gbps Ethernet  
  
#### **Software Requirements**

**Software Component**| **Requirement**  
---|---  
**Operating System**|  Minimum: Ubuntu 20.04 LTS or equivalentRecommended: Ubuntu 22.04 LTS or equivalent  
**Kubernetes**|  Version 1.22 or higher  
**Docker**|  Version 20.10 or higher  
**Helm**|  Version 3.0 or higher  
**Kubeadm**|  For setting up the Kubernetes cluster  
  
#### **Network Requirements**

  * **Internal Networking:**

    * Secure and stable network connection between master and worker nodes

    * Network plugins such as Calico, Flannel, or Weave for pod networking.

  * **External Access:**

    * Configurations for load balancing (e.g., Nginx, HAProxy).

    * Secure communication channels (e.g., HTTPS, VPN).




#### **Database Configuration**

  * **PostgreSQL:** Version 16+ for each microservice.

  * Each microservice should have its own PostgreSQL instance.

  * Secure and configure cross-service database access.

  * Persistent Storage: Use Persistent Volume Claims **(PVC) in Kubernetes** for database storage.




## **Environment Setup**

  * **Container Orchestration:**

    * Kubernetes cluster with at least one master node and multiple worker nodes

  * **Containerization:**

    * Docker or similar container runtime

  * **Namespace Configuration:**

    * Separate namespaces for different environments (e.g., development, staging, production)



