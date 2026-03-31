---
title: "WFM Prerequisites"
summary: "Hardware, software, network, and database requirements for deploying CX Workforce Management as an add-on to ExpertFlow CX."
audience: [admin, partner]
product-area: [wfm, platform]
doc-type: reference
difficulty: advanced
keywords: ["WFM", "prerequisites", "hardware requirements", "Kubernetes", "Docker", "Helm", "PostgreSQL", "sizing", "deployment"]
aliases: ["WFM requirements", "workforce management installation requirements", "WFM sizing"]
last-updated: 2026-03-10
---

# WFM Prerequisites

Before deploying **CX Workforce Management (WFM)** as a CX add-on, verify that your environment meets the requirements below. WFM runs on Kubernetes and requires dedicated compute resources separate from your core CX deployment.

## Frontend Requirements

### Hardware

Minimum specifications vary by agent count:

| Attribute | 50 Agents | 300 Agents | 1000 Agents |
|---|---|---|---|
| **CPU** | 3 vCPUs | 6 vCPUs | 16 vCPUs |
| **RAM** | 6 GB | 8 GB | 32 GB |
| **Storage** | 50 GB SSD | 75 GB SSD | 150 GB SSD |

### Supported Browsers

| Agent Count | Supported Browsers |
|---|---|
| Up to 50 | Google Chrome 127.0.6533.73 (64-bit), Microsoft Edge 127.0.2651.105 (64-bit) |
| 300–1000 | Google Chrome 128.0.6613.85 (64-bit), Microsoft Edge 128.0.2739.42 (64-bit) |

### Software

| Component | Requirement |
|---|---|
| **Operating System** | Minimum: Ubuntu 20.04 LTS. Recommended: Ubuntu 22.04 LTS |
| **Kubernetes** | Version 1.22 or higher |
| **Docker** | Version 20.10 or higher |
| **Helm** | Version 3.0 or higher |
| **Kubeadm** | Required for Kubernetes cluster setup |

## Backend Requirements

WFM's backend runs on Kubernetes. You need at least one master node and one or more worker nodes.

### Master Node

| Component | Minimum | Recommended |
|---|---|---|
| **CPU** | 6 vCPUs (e.g., Intel Core i5) | 8 vCPUs (e.g., Intel Xeon) |
| **RAM** | 16 GB | 32 GB or more |
| **Storage** | 500 GB SSD | 800 GB NVMe SSD |
| **Network** | 1 Gbps Ethernet | 10 Gbps Ethernet |

### Worker Nodes

| Component | Minimum | Recommended |
|---|---|---|
| **CPU** | Quad-core (e.g., Intel Core i5) | Octa-core (e.g., Intel Xeon) |
| **RAM** | 8 GB | 16 GB or more |
| **Storage** | 100 GB SSD | 500 GB NVMe SSD |
| **Network** | 1 Gbps Ethernet | 10 Gbps Ethernet |

### Software

| Component | Requirement |
|---|---|
| **Operating System** | Minimum: Ubuntu 20.04 LTS. Recommended: Ubuntu 22.04 LTS |
| **Kubernetes** | Version 1.22 or higher |
| **Docker** | Version 20.10 or higher |
| **Helm** | Version 3.0 or higher |
| **Kubeadm** | Required for cluster configuration |

## Network Requirements

### Internal Networking

- Stable, low-latency connection between master and worker nodes
- A Kubernetes network plugin such as **Calico**, **Flannel**, or **Weave** for pod-to-pod networking

### External Access

- Load balancer configuration (e.g., Nginx or HAProxy) for ingress traffic
- HTTPS enforced for all external-facing endpoints
- VPN or private network recommended for administrative access

## Database Requirements

WFM uses **PostgreSQL** for persistent data storage:

| Requirement | Detail |
|---|---|
| **Version** | PostgreSQL 16 or higher |
| **Instance model** | Each WFM microservice requires its own dedicated PostgreSQL instance |
| **Cross-service access** | Secure and configure cross-service database credentials separately |
| **Storage** | Use Kubernetes **Persistent Volume Claims (PVCs)** for all database storage |

## Environment Configuration

| Area | Requirement |
|---|---|
| **Kubernetes cluster** | Minimum one master node and one worker node |
| **Container runtime** | Docker or a compatible container runtime (e.g., containerd) |
| **Namespaces** | Use separate Kubernetes namespaces for development, staging, and production |

## Related Articles

- [Workforce Management Overview](Workforce-Management-Overview.md)
- [WFM Admin and Supervisor Guide](../../Supervisor/WFM-Admin-Supervisor-Guide.md)
- [Sizing Guidelines](../../Solution_Admin/Sizing-Guidelines.md)
- [Deploying the RKE2 Control Plane](../../Getting_Started/Deploying-the-RKE2-Control-Plane.md)
