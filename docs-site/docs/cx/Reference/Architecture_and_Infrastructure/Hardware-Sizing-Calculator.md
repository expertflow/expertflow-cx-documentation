---
title: "Hardware Sizing Calculator"
summary: "Reference sizing tables for Infrastructure & Hosting Partners — CX Core, Voice Media Server, and Digital Channels — mapped to agent count and concurrent call volume."
audience: [platform-operator]
product-area: [infrastructure]
doc-type: reference
difficulty: intermediate
keywords: ["hardware sizing", "capacity planning", "CPU RAM sizing", "agent count", "concurrent calls", "CX Core requirements", "Kubernetes nodes", "infrastructure prerequisites"]
aliases: ["sizing calculator", "hardware requirements", "capacity planning guide", "infrastructure sizing"]
last-updated: 2026-03-21
---

# Hardware Sizing Calculator

Use this reference to size hardware for a new ExpertFlow CX deployment. Tables are organised by component and scaled against the two primary sizing drivers: **concurrent agents** and **concurrent voice calls**.

> All figures are minimum recommended specs for production. Add 20–30% headroom for peak traffic and OS overhead. Development and lab environments may use lower specs.

---

## Sizing Drivers

Before reading the tables, identify your deployment's two key numbers:

| Driver | How to get it |
| --- | --- |
| **Concurrent agents** | Peak agents logged in and handling interactions at the same time |
| **Concurrent voice calls** | Peak simultaneous live voice calls (inbound + outbound combined) |

If the customer cannot provide these, use: **concurrent agents = 60–70% of total licensed agents**, and **concurrent voice calls ≈ concurrent voice agents × 0.8**.

---

## CX Core Platform

The CX Core runs the routing engine, agent desk, Unified Admin, APIs, and all digital channel connectors. Size it based on concurrent agents.

| Concurrent Agents | CPU (cores) | RAM | Storage | Notes |
| --- | --- | --- | --- | --- |
| Up to 50 | 8 | 16 GB | 200 GB SSD | Suitable for SMB or single-tenant deployments |
| Up to 150 | 16 | 32 GB | 500 GB SSD | Standard mid-market deployment |
| Up to 300 | 32 | 64 GB | 1 TB SSD | Large single-tenant or small multi-tenant |
| 300+ | 48+ | 128 GB+ | 2 TB SSD (RAID) | Multi-tenant; consult ExpertFlow pre-sales |

**Kubernetes node recommendation:** Distribute CX Core workloads across a minimum of 3 worker nodes for HA. Each node should meet at least the per-tier CPU/RAM figures above divided by the node count, plus 20% overhead.

---

## Voice Media Server

The Media Server handles RTP streams, IVR prompts, conferencing, and voice recording. Size it based on concurrent voice calls, independently of CX Core.

| Concurrent Voice Calls | CPU (cores) | RAM | Storage | OS |
| --- | --- | --- | --- | --- |
| Up to 100 | 4 | 8 GB | 100 GB SSD | Debian 12+ |
| Up to 300 | 8 | 16 GB | 200 GB SSD | Debian 12+ |
| Up to 500 | 12 | 24 GB | 300 GB SSD | Debian 12+ |
| 500–1000 | 16 | 32 GB | 500 GB SSD | Debian 12+ |
| 1000+ | 16+ (scale out) | 32 GB+ | 500 GB+ SSD | Debian 12+; consider active-active HA |

> Voice Recording (VRS) is included in the Media Server — no separate server is required for recording storage unless retention exceeds 90 days, in which case add a dedicated NAS or object storage tier.

---

## AI-Powered Voice Add-on

Required only when deploying voicebots, speech transcription, or text-to-speech. Run on a dedicated node separate from CX Core.

| Component | CPU (cores) | RAM | GPU | Notes |
| --- | --- | --- | --- | --- |
| Jambonz (SIP app server) | 4 | 8 GB | Not required | Handles SIP-to-AI bridge |
| ASR engine (e.g. Whisper) | 8 | 16 GB | Optional (improves throughput) | Scale with concurrent transcription sessions |
| TTS engine | 4 | 8 GB | Optional | Scale with concurrent synthesis sessions |
| NLU engine (e.g. RASA) | 8 | 16 GB | Recommended for training | Inference can run CPU-only |

---

## Digital Channel Connectors

Each connector (WhatsApp, Facebook, Instagram, etc.) is a lightweight microservice. Run connectors on shared Kubernetes worker nodes — they do not require dedicated hardware unless message volume is very high.

| Channels Active | Additional CPU (cores) | Additional RAM | Notes |
| --- | --- | --- | --- |
| 1–3 channels | 2 | 4 GB | Co-locate with CX Core worker nodes |
| 4–8 channels | 4 | 8 GB | Consider a dedicated connector node |
| 8+ channels or high-volume | 8 | 16 GB | Dedicated node; monitor queue depth per connector |

---

## Database (MongoDB)

| Concurrent Agents | CPU (cores) | RAM | Storage | Replica Set |
| --- | --- | --- | --- | --- |
| Up to 50 | 4 | 8 GB | 200 GB SSD | 1 primary + 1 secondary |
| Up to 150 | 8 | 16 GB | 500 GB SSD | 1 primary + 2 secondaries (recommended) |
| Up to 300 | 16 | 32 GB | 1 TB SSD | 1 primary + 2 secondaries |
| 300+ | 16+ | 64 GB+ | 2 TB SSD | Sharded cluster; consult ExpertFlow pre-sales |

> Storage figures are for operational data. Add a separate backup volume equal to 2× the data volume.

---

## CX SIP Proxy

Required for voice deployments. Handles SIP signalling load balancing and failover.

| Concurrent Voice Calls | CPU (cores) | RAM | HA Mode |
| --- | --- | --- | --- |
| Up to 500 | 4 | 4 GB | Single node acceptable |
| Up to 2000 | 4 | 8 GB | Active-passive (Keepalived/VRRP) |
| 2000+ | 8 | 16 GB | Active-active cluster |

---

## Full Deployment Example

A mid-market deployment with **100 concurrent agents** and **200 concurrent voice calls**:

| Component | Spec |
| --- | --- |
| CX Core (3 worker nodes) | 6 cores / 12 GB RAM each (18 cores / 36 GB total) |
| Voice Media Server | 8 cores / 16 GB RAM / 200 GB SSD |
| MongoDB Replica Set (3 nodes) | 4 cores / 8 GB RAM / 200 GB SSD each |
| CX SIP Proxy | 4 cores / 4 GB RAM |
| Digital connectors (3 channels) | Co-located on CX Core worker nodes |
| **Total (approx.)** | **~44 cores / ~100 GB RAM / ~1.4 TB SSD** |

---

## Related Articles

- [CX Voice Platform Sizing](../../Capabilities/Voice_and_Video/CX-Voice-Platform-Sizing.md)
- [Sizing Guidelines](../../How-to_Guides/Administrator/Sizing-Guidelines.md)
- [Kubernetes Distributions](../../How-to_Guides/Platform_Operator/Kubernetes-Distributions.md)
- [Helm-Based Application Deployment](../../How-to_Guides/Platform_Operator/Helm-Based-Application-Deployment.md)
- [CX Voice Deployment](../../How-to_Guides/Platform_Operator/CX-Voice-Deployment.md)
- [MongoDB Replica Set Deployment](../../How-to_Guides/Platform_Operator/Deployment-of-Mongo-using-ReplicaSet.md)
