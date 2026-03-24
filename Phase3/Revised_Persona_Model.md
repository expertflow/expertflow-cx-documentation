# Revised Persona Model: ExpertFlow CX Documentation

**Replaces:** `Final_12_Persona_Model.md` (12-persona model)
**Status:** Proposed — for review and validation

---

## Why the 12-Persona Model Needed Revision

The original model drew vertical role lines (job titles) through horizontal system layers. This caused:

- Overlapping golden paths (e.g., hardware sizing appeared for both CTO and Host)
- Personas that aren't documentation users (Decision Maker / CTO = pre-sales evaluation, not task-based use)
- Real-world role collapse ignored (in most deployments, 1 person covers 2–3 theoretical personas)
- Operational support content (monitoring, upgrades, maintenance) had no persona home

The revised model organises personas around **what people are trying to do**, not org chart titles.

---

## The Core Structure: 3 Clusters + Deployment Context

```
┌──────────────────────────────────────────────────────────┐
│  CLUSTER 1: Contact Center Users                         │
│  People who run the daily operation                      │
│  ├── Agent                                               │
│  └── Supervisor / QA Lead                                │
├──────────────────────────────────────────────────────────┤
│  CLUSTER 2: Platform People                              │
│  People who configure, operate, and host the platform    │
│                                                          │
│  Split by deployment type:                               │
│                                                          │
│  Single-Tenant           Multi-Tenant                    │
│  ─────────────           ───────────                     │
│  Administrator           Hosting Partner                 │
│  (config + infra         (infra + tenant lifecycle       │
│   + ops for one           + commercial for N tenants)    │
│   installation)                                          │
│                                                          │
│  Shared sub-path (both deployment types):                │
│  └── Platform Operator  (monitoring, upgrades,           │
│                          maintenance, backup/restore)    │
├──────────────────────────────────────────────────────────┤
│  CLUSTER 3: Builders                                     │
│  People who build on top of the platform                 │
│  ├── Conversation Designer / AI Specialist               │
│  └── Developer / Integrator                              │
└──────────────────────────────────────────────────────────┘
```

---

## Cluster 1: Contact Center Users

### 1.1 The Agent

*Goal: Handle customer interactions efficiently and accurately.*

Distinct persona — kept separate. Agents have a narrow, well-defined interface (Agent Desktop only) and very specific documentation needs.

**Golden Path:**
1. **Tutorial:** Agent Quick-Start Guide (Ref: `Agent-Quick-Start-Guide.md`)
2. **How-to:** Managing Presence & Breaks (Ref: `Change-Agent-State_2524603`)
3. **How-to:** Accepting & Handling Conversations (Ref: `Accept-a-Conversation_2527849`)
4. **How-to:** Applying Wrap-up & Notes (Ref: `Apply-Wrap-up-and-Add-Notes_2528747`)
5. **How-to:** Using Agent Co-Pilot (Ref: `Agent-Co-Pilot.md`)

---

### 1.2 The Supervisor / QA Lead

*Goal: Monitor team performance, maintain quality, manage the operation.*

**Merges:** Supervisor (Sam) + Human Evaluator (Eva) + Quality Manager (Quentin)

**Why merged:** In most deployments these roles overlap significantly. A supervisor monitors real-time performance and assigns QA; a QA lead scores transcripts and sets rubrics. Smaller organisations have one person doing all three. Splitting them creates three partial pictures of the same operational function.

Sub-paths within this persona for larger orgs that do split roles:
- **Monitoring track** — real-time dashboards, barge-in, availability management
- **Quality track** — evaluation forms, audit assignment, transcript review
- **Reporting track** — historical reports, KPI trend analysis

**Golden Path:**
1. **How-to:** Monitoring Your Team in Real-Time (Ref: `Monitoring-Your-Team-in-Real-Time.md`)
2. **How-to:** Managing the QA Workflow (Ref: `Managing-the-Quality-Assurance-Workflow.md`)
3. **How-to:** Reviewing Conversation Transcripts (Ref: `Review-Screen_819593222`)
4. **How-to:** Designing Evaluation Rubrics (Ref: `Create-an-evaluation-form_819232775`)
5. **Reference:** Key Reporting Metrics (Ref: `Key-Reporting-Metrics_2526622`)

---

## Cluster 2: Platform People

The key insight: **deployment type determines responsibilities more than job title.**

In single-tenant deployments, one administrator may own infrastructure, configuration, and day-to-day operations. In multi-tenant deployments, the Hosting Partner owns infrastructure and tenant lifecycle, while each tenant has its own administrator for business configuration.

### Deployment Context Decision Tree

```
How is ExpertFlow deployed in your organisation?

├── Single installation for one organisation
│     └── → Administrator path
│
└── Hosted platform serving multiple tenants
      └── → Hosting Partner path
            (both if you manage infrastructure AND onboard tenants)
```

---

### 2.1 The Administrator (Single-Tenant)

*Goal: Configure and maintain the platform for one organisation.*

**Merges:** Solution Admin (Olivia) — but now also owns operational support content for single-tenant installations.

**Covers:**
- Business configuration (queues, routing, teams, skills, channels)
- User and license management
- Platform health monitoring and alerting
- Upgrade and maintenance operations (single-node scope)

**Golden Path:**
1. **How-to:** Unified Admin Overview (Ref: `Unified-Admin-Guide_2524407`)
2. **How-to:** Configuring Routing & Queues (Ref: `Manage-Queues-and-Routing-Attributes_1567719455`)
3. **How-to:** Setting Up Channels (WhatsApp, Facebook, Email) (Ref: `Manage-Channels-and-Channel-Categories_1562411043`)
4. **How-to:** Managing Teams & Agents (Ref: `Manage-Teams_1602027529`)
5. **Reference:** License Consumption & Monitoring (Ref: `License-Consumption-Status_985595918`)

**Then → Platform Operator sub-path** for monitoring, upgrades, backup

---

### 2.2 The Hosting Partner (Multi-Tenant)

*Goal: Deploy, operate, and commercially manage a multi-tenant ExpertFlow installation.*

**Merges:** Multi-tenant Host + Reseller

**Why merged:** The Host deploys and manages the cluster; the Reseller creates and manages tenants commercially. In almost all real deployments, this is the same company (an ISP, SI, or MSP). Splitting them creates two partial views of one end-to-end responsibility: cluster → tenant provisioning → billing → tenant lifecycle → support.

**Covers:**
- Cluster infrastructure (RKE2, Helm, networking, SSL)
- Multi-tenant provisioning (tenant creation, onboarding, configuration templates)
- Tenant lifecycle management (suspend, upgrade, decommission)
- Commercial management (license tiers, renewal, white-labeling)
- Platform-wide operational support (monitoring, upgrades, HA)

**Golden Path:**
1. **How-to:** Deploying the RKE2 Control Plane (Ref: `Deploying-the-RKE2-Control-Plane.md`)
2. **How-to:** Onboarding a New Tenant (Ref: `Tenant-Onboarding--To-be-removed_1015775291`)
3. **How-to:** Configuring Multi-tenant Provisioning (Ref: `Tenant-Creation-for-Multi-tenant-CX--To-be-removed_1372029057`)
4. **How-to:** Managing SSL with LetsEncrypt (Ref: `LetsEncrypt-SSL-for-EF-CX_32538676`)
5. **Reference:** Hardware Sizing for Large Scale Clusters

**Then → Platform Operator sub-path** for monitoring, upgrades, backup

---

### 2.3 Platform Operator (Sub-path, shared)

*Goal: Keep the running installation healthy.*

**This is new — previously had no persona home.** Operational support content was scattered across Host and Admin personas, or simply missing. This sub-path surfaces it for whoever owns operations in a given deployment.

**Not a separate persona entry point** — reached from either Administrator or Hosting Partner path.

**Covers:**
- System health monitoring (dashboards, alerting, logs)
- Version upgrades and patch procedures
- Backup and restore
- Troubleshooting infrastructure issues
- Performance tuning

**Content to create or consolidate:**
- Upgrade runbooks
- Health check procedures
- Log monitoring reference
- Backup/restore guide
- Common operational issues and resolution

---

## Cluster 3: Builders

### 3.1 Conversation Designer / AI Specialist

*Goal: Design conversation flows and tune AI/NLU models.*

**Merges:** Conversation Designer (Dave) + AI QA & NLU Specialist

**Why merged:** Both work primarily in Conversation Studio. Flow logic and NLU/bot tuning are deeply intertwined — you cannot design effective flows without understanding the AI models, and you cannot tune AI effectively without understanding the flow design. In practice, one person or team owns the entire "bot and flow" domain.

**Golden Path:**
1. **Explanation:** Conversation Studio Fundamentals (Ref: `Configuration-Guide---Conversation-Studio_1017118849`)
2. **How-to:** Building Your First Studio Flow (Ref: `Conversation-Flow-for-Outbound-Dialing-Modes---to-be-reviewed_1132265580`)
3. **How-to:** Registering Bot Connectors (Ref: `Registering-Bot-Connectors.md`)
4. **How-to:** Configuring AI-Powered Quality Audits (Ref: `Configuring-AI-Powered-Quality-Audits.md`)
5. **Tutorial:** Handover Logic: AI to Human (Ref: `AI-Assistant-handover-to-human-agent_1324417085`)

---

### 3.2 Developer / Integrator

*Goal: Build custom UIs, integrate external systems, and extend the platform.*

**Merges:** Frontend Developer (Dev) + Integration Specialist (Ian)

**Why merged:** Both require deep technical knowledge of the platform's APIs and data model. Frontend developers use the AgentManager SDK and WebChannel SDK; Integration Specialists use the same CIM message schemas, webhook events, and REST APIs. The technical boundary between "building a custom UI" and "connecting an external system" is thin — both require understanding platform objects, socket events, and message schemas.

**Sub-paths for teams with dedicated specialists:**
- **UI / SDK track** — AgentManager SDK, WebChannel SDK, Widget embedding
- **Integration track** — CRM connectors, Webhooks, Third-party Activity API

**Golden Path:**
1. **Reference:** Platform Objects & Data Model (Ref: `Platform-Objects-and-Data-Model.md`)
2. **Reference:** AgentManager SDK Reference (Ref: `Agent-Desk-Developer-Guide_2523754`)
3. **Reference:** CIM Message Schema Overview (Ref: `CIM-Messages_2530195`)
4. **How-to:** Setting Up CRM Connectors (Ref: `CRM-Connectors_28410275`)
5. **Reference:** Socket Events Reference (Ref: `Socket-Events_2530728`)

---

## What Happened to the Decision Maker / CTO

The CTO is a **pre-sales evaluation persona**, not a documentation user. They need to assess platform suitability, not complete tasks.

**Resolution:** Remove as a persona entry point. Content moves to the **Platform Overview** top-level nav section (see Navigation Structure below). A CTO searching "ExpertFlow security compliance" lands directly on the relevant page — they don't navigate through a persona selector.

---

## Migration Map: 12 Personas → Revised Model

| Original Persona | Maps To |
|---|---|
| Agent (Amy) | Cluster 1: Agent |
| Supervisor (Sam) | Cluster 1: Supervisor / QA Lead |
| Human Evaluator (Eva) | Cluster 1: Supervisor / QA Lead |
| Quality Manager (Quentin) | Cluster 1: Supervisor / QA Lead |
| Solution Admin (Olivia) | Cluster 2: Administrator |
| Decision Maker (CTO) | → Platform Overview section (not a persona) |
| Frontend Developer (Dev) | Cluster 3: Developer / Integrator |
| Conversation Designer (Dave) | Cluster 3: Conversation Designer / AI Specialist |
| Integration Specialist (Ian) | Cluster 3: Developer / Integrator |
| AI QA & NLU Specialist | Cluster 3: Conversation Designer / AI Specialist |
| Multi-tenant Partner (Host) | Cluster 2: Hosting Partner |
| Reseller (Cloud) | Cluster 2: Hosting Partner |

---

## Navigation Structure

### Top-Level Sections

The site nav has five sections, each with a clear and distinct job:

| # | Section | Diataxis type | Purpose |
| --- | --- | --- | --- |
| 1 | **Getting Started** | Tutorial | Role-based entry points — first steps for each persona cluster |
| 2 | **Platform Overview** | Orientation | High-level summaries for evaluation and orientation — not a persona path |
| 3 | **Capabilities** | Cross-cutting | Topic-based browsing — what the platform can do (replaces "Functional Areas") |
| 4 | **How-to Guides** | How-to | Task-based guides, organised by persona cluster |
| 5 | **Reference** | Reference | Technical specs, APIs, SDKs, schemas, hardware sizing, deployment topology |

### Getting Started Entry Flow

Replace the persona selector ("which of these 12 are you?") with a 3-question entry:

```
What brings you here?

┌─────────────────────────────────────────────────────────┐
│  I work in a contact center                             │
│  (handling interactions, monitoring teams, QA)          │
│  → Agent  |  Supervisor & QA Lead                       │
├─────────────────────────────────────────────────────────┤
│  I manage or run the platform                           │
│  (configuration, hosting, operations)                   │
│  → Single-tenant Admin  |  Hosting Partner              │
├─────────────────────────────────────────────────────────┤
│  I'm building on ExpertFlow                             │
│  (flows, bots, integrations, custom UIs)                │
│  → Conversation Designer  |  Developer / Integrator     │
└─────────────────────────────────────────────────────────┘
```

### Platform Overview — Scope Definition

**What lives here** (orientation-level, no detailed specs):

- Security & Compliance overview
- Platform architecture summary (component diagram, not deployment topology)
- AI & Automation capabilities summary
- Release versioning & support policy

**What does NOT live here** (→ Reference instead):

- Detailed architecture diagrams
- Deployment topology references
- Hardware sizing tables
- Port/network requirements

**Why:** Platform Overview is for orientation and evaluation. Once a reader needs specific numbers or diagrams to act on, they have crossed into Reference territory.

### Reference — Scope Definition

Technical, look-up content. Organised into sub-sections:

```text
Reference
  ├── Architecture & Infrastructure
  │     ├── Platform Architecture (detailed diagrams)
  │     ├── Deployment Topology Reference
  │     └── Hardware Sizing & Requirements
  ├── API & SDK
  │     ├── AgentManager SDK
  │     ├── WebChannel SDK
  │     └── Third-Party Activity API
  └── Schemas & Data Model
        ├── CIM Message Schema
        ├── Socket Events
        └── Platform Objects
```

### Single Source, Multiple Entry Points

Content lives once in Reference. Role paths and Platform Overview link to it contextually.

**Example — Hardware Sizing:**

```text
CTO reading Platform Overview
  └── "What infrastructure do I need?"
        → links to Reference: Hardware Sizing & Requirements

Hosting Partner following their golden path
  └── Step 5: "Hardware Sizing for Large Scale Clusters"
        → links to same Reference: Hardware Sizing & Requirements
```

No duplication. Same page, different arrival path.

---

## Metadata Tagging Rules (Updated)

```yaml
audience:
  # Cluster 1
  - agent
  - supervisor-qa

  # Cluster 2
  - administrator          # single-tenant
  - hosting-partner        # multi-tenant
  - platform-operator      # shared sub-path, used alongside above

  # Cluster 3
  - conversation-designer
  - developer-integrator

  # Non-persona (no golden path, accessed by topic/search)
  - platform-overview      # evaluation/orientation content → Platform Overview section
```

**Tagging rules:**

- A document can carry multiple audience tags
- `platform-operator` should be added to any monitoring, upgrade, backup, or maintenance content currently tagged only `hosting-partner` or `administrator`
- `platform-overview` is not a persona — do not create a golden path for it; content is surfaced via the Platform Overview nav section and direct search
- Hardware Sizing, deployment topology, and architecture diagrams carry no audience tag — they are Reference content, linked from multiple persona paths
