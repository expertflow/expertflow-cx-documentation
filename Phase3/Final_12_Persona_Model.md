# Final 12-Persona Model: ExpertFlow CX Knowledge Base

This document defines the 12 personas used for metadata tagging, navigation design, and content refactoring.

## 1. Business & Operations (Role-Based)

| Persona | Alias | Primary Goal | Key Tools |
|---------|-------|--------------|-----------|
| **Agent** | Amy | Handling daily interactions | Agent Desktop, Wrap-up, Presence |
| **Supervisor** | Sam | Real-time team performance | Real-time Dashboard, Barge-in, Assistance |
| **Human Evaluator** | Eva | Manual quality scoring | Transcript Review, Audio Playback, Forms |
| **Quality Manager** | Quentin | Quality strategy & workflow | Rubric Design, Audit Assignment, Trends |
| **Solution Admin** | Olivia | Business logic config | Unified Admin, Skills, Queues, Routing |
| **Decision Maker** | CTO | Platform value, compliance, & resource planning | Architecture, Security, Hardware Sizing |

## 2. Implementation & Technical

| Persona | Alias | Primary Goal | Key Tools |
|---------|-------|--------------|-----------|
| **Frontend Developer** | Dev | Building custom UIs | AgentManager SDK, WebChannel API |
| **Conversation Designer** | Dave | Designing flow logic | Conversation Studio, Studio Nodes |
| **Integration Specialist** | Ian | Connecting external systems | CRM Connectors, Webhooks, APIs |
| **AI QA & NLU Spec.** | - | Tuning AI/LLM models | AI Evaluator Config, Rasa, Prompt Eng. |

## 3. Infrastructure & Commercial

| Persona | Alias | Primary Goal | Key Tools |
|---------|-------|--------------|-----------|
| **Multi-tenant Partner** | Host | Cluster deployment & HA | RKE2, Helm, Hardware Sizing, SIP Proxy |
| **Reseller** | Cloud | Tenant & billing mgmt | Tenant Onboarding, Subscription Tiers |

---

## Metadata Tagging Rules:
- `audience`: Must map to one or more of these 12 keys.
- `doc-type`: Tutorial | How-to | Reference | Explanation (Diátaxis).
