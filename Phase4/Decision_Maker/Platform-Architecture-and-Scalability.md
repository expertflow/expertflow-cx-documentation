---
title: "Platform Architecture & Scalability"
summary: "A technical deep-dive into ExpertFlow CX's microservices topology, multi-tenancy isolation model, data tier design, and horizontal scaling capabilities."
audience: [decision-maker, partner]
product-area: [platform, strategic]
doc-type: explanation
difficulty: intermediate
aliases: []
last-updated: 2026-03-13
---

# Platform Architecture & Scalability

ExpertFlow CX is built as a cloud-native, microservices platform running on **Kubernetes (RKE2)**. This article explains the architectural decisions that give the platform its resilience, multi-tenancy, and horizontal scalability — the properties that matter most when evaluating it for enterprise or multi-tenant deployment.

---

## 1. Microservices Topology

The platform is composed of loosely coupled services, each owning a specific domain:

| Service | Responsibility |
|---------|---------------|
| **CIM (Customer Interaction Manager)** | Central message broker. All interaction events (incoming, transferred, closed) flow through CIM as structured event objects. |
| **Routing Engine** | Evaluates routing rules, skill matching, and queue priorities. Operates in push (precision) or pull (list) mode. |
| **Agent Desk / AgentManager** | WebSocket-based real-time UI server. Maintains per-agent session state and pushes events to browser clients. |
| **AI Orchestrator** | Decoupled reasoning layer. Receives conversation context from CIM and dispatches to configured LLM/NLU providers. Returns enriched results without blocking the interaction flow. |
| **Keycloak (IAM)** | Identity and access management. Issues JWTs for all service-to-service and user authentication. Each tenant gets an isolated realm. |
| **Unified Admin** | Configuration service. Manages queues, skills, channels, teams, and license assignments. Writes directly to MongoDB config collections. |
| **Quality Management** | Evaluation pipeline. Receives transcripts from CIM, assigns to human evaluators or AI audit jobs. |
| **Reporting / CX Analyser** | Reads from MongoDB replica sets and/or OpenSearch indexes to serve real-time dashboards and historical aggregations. |

Services communicate over **REST** (synchronous) and **Redis Pub/Sub** (asynchronous event streams). There is no shared database between services — each owns its own collection namespace within MongoDB.

---

## 2. Multi-Tenancy Isolation Model

ExpertFlow CX supports **logical multi-tenancy**: multiple tenants on shared infrastructure, with strict data and configuration isolation.

### What is isolated per tenant:
- **Keycloak realm** — separate identity store, roles, and SSO configuration
- **MongoDB namespace** — all documents are partitioned by `tenantId`
- **Redis keyspace** — tenant-prefixed keys prevent cross-tenant event leakage
- **Minio bucket** — separate storage bucket per tenant for recordings, attachments, and channel icons
- **Ingress routing** — subdomain-based routing (`tenantId.root-domain`) directs traffic to the correct Keycloak realm and tenant context before it reaches any application service

### What is shared:
- Kubernetes node pool and cluster control plane
- Core microservice deployments (one instance set serves all tenants, differentiating via `tenantId` in each request)
- Ingress controller and TLS termination layer

This model gives operators the cost efficiency of a shared cluster while providing tenants the security guarantees of isolated namespaces.

---

## 3. Data Tier Architecture

```
┌─────────────────────────────────────────┐
│              MongoDB (Primary Data)      │
│  - Config (queues, skills, channels)    │
│  - Interaction records & transcripts    │
│  - Audit & QM results                   │
│  - Replica set recommended for HA       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│         Redis (Real-time State)          │
│  - Agent presence & availability        │
│  - Active interaction state             │
│  - Pub/Sub event bus between services   │
│  - Supports Redis Cluster for HA        │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│      Minio / Blob Storage (Objects)      │
│  - Call recordings                      │
│  - Screen recordings                    │
│  - Channel icons, tenant logos          │
│  - Compatible with AWS S3 API           │
└─────────────────────────────────────────┘
```

MongoDB replica sets (minimum 3 nodes: 1 primary, 2 secondaries) are the recommended production configuration. Redis Cluster mode with sentinel is supported for environments requiring sub-second failover on the real-time event bus.

---

## 4. AI Orchestration Architecture

The AI layer is intentionally **decoupled from the interaction path**. This means a slow or unavailable AI provider never delays or blocks a live customer conversation.

```
Customer Interaction
       │
       ▼
    CIM Service  ──► (async) ──► AI Orchestrator
       │                              │
       ▼                              ▼
  Agent Desk               LLM Router (configurable)
  (real-time)             ┌──────────────────────────┐
                          │  OpenAI  │ Gemini │ Ollama│
                          │  Rasa    │Dialogflow│ etc. │
                          └──────────────────────────┘
```

The AI Orchestrator exposes a provider-agnostic interface. Operators configure which LLM or NLU engine to use per use case (agent assist, bot routing, quality scoring) without modifying any other service. This is the "Bring Your Own AI" capability referenced in product documentation.

---

## 5. Scalability Patterns

### Horizontal Pod Autoscaling (HPA)
All stateless services (CIM, Routing Engine, AI Orchestrator, Unified Admin) support Kubernetes HPA. Under high load, additional pods are scheduled automatically within the cluster's available node capacity.

### Services that require careful scaling:
- **AgentManager** — maintains WebSocket state per agent. Requires a sticky-session ingress rule (or a shared Redis session store) when running multiple replicas.
- **Keycloak** — scales horizontally but requires an external database (PostgreSQL) and shared Infinispan cache configuration for session replication.

### Typical sizing reference:
| Deployment Size | Concurrent Agents | Recommended Nodes |
|----------------|------------------|-------------------|
| Small (single-tenant) | up to 50 | 3 nodes (8 vCPU / 16 GB each) |
| Medium (multi-tenant, 5–10 tenants) | up to 300 | 5–6 nodes (16 vCPU / 32 GB each) |
| Large (multi-tenant, 20+ tenants) | 500+ | 8+ nodes, separate DB node pool |

> For detailed sizing, see [Hardware Sizing & Resource Requirements](../Solution_Admin/Sizing-Guidelines.md).

---

## 6. High Availability & Failover

- **Control Plane HA:** RKE2 supports a 3-node etcd cluster for control plane fault tolerance.
- **Ingress:** MetalLB or cloud load balancer in front of NGINX ingress. DNS failover supported via TTL management.
- **Database:** MongoDB replica set with automatic primary election. Redis Sentinel or Cluster for cache/event bus HA.
- **Stateless Services:** Any pod failure triggers Kubernetes self-healing (pod restart or rescheduling) within seconds.
- **RTO/RPO:** With a properly configured replica set and daily MongoDB snapshots, Recovery Time Objective (RTO) is under 5 minutes; Recovery Point Objective (RPO) depends on snapshot frequency (default: 24 hours, configurable to near-zero with oplog shipping).

---

## 7. Security Architecture

- **Network:** All inter-service communication is TLS-encrypted. mTLS is supported for sensitive service-to-service paths.
- **Identity:** Keycloak enforces OAuth 2.0 / OIDC for all user sessions. Service accounts use client credential grants with short-lived JWTs.
- **Data at rest:** MongoDB and Minio support AES-256 encryption at rest. Encryption keys managed via Kubernetes Secrets (or external KMS such as Vault).
- **Tenant boundary enforcement:** `tenantId` is extracted from the Keycloak JWT on every API request and enforced at the application layer — no cross-tenant data access is possible even from within the cluster.

---

*Related: [Security & Compliance Whitepaper](../Getting_Started/Security-and-Compliance-Whitepaper.md) · [Hardware Sizing & Resource Requirements](../Solution_Admin/Sizing-Guidelines.md)*
