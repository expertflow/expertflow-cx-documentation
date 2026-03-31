---
title: "Infrastructure & Hosting (Partner) Guide"
summary: "Full golden path for multi-tenant partners — Kubernetes setup, component deployment, SIP proxy, HA, upgrades, and Day 2 operations."
audience: [partner]
doc-type: landing
last-updated: 2026-03-14
---

As an Infrastructure & Hosting Partner, you are responsible for deploying and operating the ExpertFlow CX platform on behalf of your customers. This guide covers everything from initial Kubernetes setup through to upgrades and operational reliability.

---

## Platform Foundation

Start here if you are setting up a new environment.

- [Hardware Sizing Calculator](Hardware-Sizing-Calculator.md) — CPU/RAM/storage tables for CX Core, Voice, Database, and connectors by agent count and concurrent calls
- [Kubernetes Distributions](Kubernetes-Distributions.md) — supported distributions (RKE2 recommended), K8s/kubeadm, Tanzu, K3s, MicroK8s
- [Helm-Based Application Deployment](Helm-Based-Application-Deployment.md) — deploying CX application layers using Helm charts and custom values files
- [Helm Deployment Customization](Helm-Deployment-Customization.md) — replica counts, resource limits, custom image tags

---

## Core Component Deployment

- [CX Voice Deployment](CX-Voice-Deployment.md) — voice architecture overview and deployment sequence
- [CX Dialer Deployment Guide](CX-Dialer-Deployment-Guide.md) — Outbound Dialer using Docker Compose
- [LiveKit Deployment Guide](LiveKit-Deployment-Guide.md) — AI voice agent integration (LiveKit on Docker Compose)
- [WFM Component Deployment](WFM-Component-Deployment.md) — Workforce Management microservices on Kubernetes
- [Superset Deployment](Superset-Deployment.md) — analytics and reporting engine on Kubernetes
- [CX Analyser Infrastructure Setup](CX-Analyser-Infrastructure-Setup.md) — reporting connector, TLS, and database schemas
- [CX Analyser Reports Setup](CX-Analyser-Reports-Setup.md) — importing report definitions and configuring the scheduler
- [RASA-X Deployment](RASA-X-Deployment.md) — NLU model management and training via Helm
- [Eleveo Middleware Deployment Guide](Eleveo-Middleware-Deployment-Guide.md) — Eleveo recording middleware via Helm
- [Customer Widget Deployment Guide](Customer-Widget-Deployment-Guide.md) — Live Chat widget deployment via Google Tag Manager

---

## SIP Proxy & Voice Infrastructure

- [SIP Proxy Architecture](SIP-Proxy-Architecture.md) — reference: signal flow, load balancing, and HA overview
- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md) — single-node and HA deployment modes, hardware prerequisites, port reference
- [CX SIP Proxy Installation Guide](CX-SIP-Proxy-Installation-Guide.md) — OpenSIPS 3.4 installation on Debian 12 with MariaDB and opensips-cp
- [Configuring Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md) — Set IDs for CVP, CUBE, VVB, CUCM, and Dialer
- [Configuring Load Balancer in CX SIP Proxy](Configuring-Load-Balancer-in-CX-SIP-Proxy.md) — Group IDs, channel resource limits, and probe modes
- [Load Balancing Dispatcher Module](Load-Balancing-Dispatcher-Module.md) — advanced opensips.cfg configuration for load balancing
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md) — OpenSIPS clustering, Keepalived/VRRP virtual IP, and failover configuration
- [Voice Connector Deployment Guide](Voice-Connector-Deployment-Guide.md) — Unified Voice Connector via Docker Compose
- [Voice Recording Components Deployment](Voice-Recording-Components-Deployment.md) — Recording Link Uploader and Middleware for call recording playback
- [EasySIPp Deployment Guide](EasySIPp-Deployment-Guide.md) — SIP load testing tool via Docker Compose

---

## Connectors & Integrations

- [Cisco Outbound Connector — Docker Deployment](Cisco-Outbound-Connector-Docker-Deployment.md) — Docker Compose deployment for CCX and CCE
- [Cisco Outbound Connector — Kubernetes Deployment](Cisco-Outbound-Connector-Kubernetes-Deployment.md) — RKE2/Kubernetes deployment with APISIX authentication
- [LinkedIn Connector Deployment](LinkedIn-Connector-Deployment.md) — LinkedIn channel connector via Helm

---

## Data & Storage

- [MongoDB Replica Set Deployment](Deployment-of-Mongo-using-ReplicaSet.md) — HA MongoDB configuration on Kubernetes
- [Audit Trail Implementation (OpenSearch)](Audit-Trail-Implementation-OpenSearch.md) — centralized audit trail using OpenSearch or equivalent SIEM

---

## High Availability & Reliability

- [System Behaviour in Failover](System-Behaviour-in-Failover.md) — reference: failover behavior across Email and Web channels, session recovery, and known limitations

---

## Upgrades & Maintenance

- [Upgrade to MongoDB 8.x](Upgrade-to-MongoDB-Version-8.x.md) — mandatory intermediate step through MongoDB 7.x with feature compatibility updates
- [RKE2 Uninstallation](RKE2-Uninstallation.md) — full RKE2 removal from control plane and worker nodes
