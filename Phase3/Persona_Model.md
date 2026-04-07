# Persona Model: ExpertFlow CX Documentation

| Field | Value |
|---|---|
| **Version** | 2.0 |
| **Status** | Proposed — for review and validation |
| **Owner** | *(assign)* |
| **Created** | *(date)* |
| **Last Updated** | *(date)* |
| **Review By** | *(date)* |
| **Change History** | See `Persona_Model_History.md` |

---

## The Core Structure: 3 Clusters

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
│  ├── Administrator    (business configuration —          │
│  │                    queues, routing, channels,         │
│  │                    users, teams)                      │
│  │                                                       │
│  ├── Platform Operator (deployment-agnostic infra & ops  │
│  │                    — installation, upgrades,          │
│  │                    RKE2/Helm/SSL/networking,           │
│  │                    health monitoring, alerting,       │
│  │                    backup/restore)                    │
│  │                                                       │
│  └── Partner          (tenant management, onboarding,   │
│                        tenant lifecycle, subscriptions,  │
│                        billing, white-labeling)          │
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

**Merges:** Supervisor + Human Evaluator + Quality Manager

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

**Function determines responsibilities, not deployment type.**

Administrator owns business configuration. Platform Operator owns infrastructure and operations. Partner owns tenant management and commercial functions. These three responsibilities are distinct regardless of whether the deployment is single-tenant or multi-tenant.

### 2.1 The Administrator

*Goal: Configure and manage the business operations of the platform. Works primarily in **Unified Admin** — setting up queues, routing, channels, users, and teams.*

**Covers:**
- Business configuration (queues, routing, teams, skills, channels)
- User and license management
- Agent desk configuration

**Golden Path:**

1. **How-to:** Unified Admin Overview (Ref: `Unified-Admin-Guide_2524407`)
2. **How-to:** Configuring Routing & Queues (Ref: `Manage-Queues-and-Routing-Attributes_1567719455`)
3. **How-to:** Setting Up Channels (WhatsApp, Facebook, Email) (Ref: `Manage-Channels-and-Channel-Categories_1562411043`)
4. **How-to:** Managing Teams & Agents (Ref: `Manage-Teams_1602027529`)
5. **Reference:** License Consumption & Monitoring (Ref: `License-Consumption-Status_985595918`)

---

### 2.2 Platform Operator

*Goal: Install, operate, and maintain the platform infrastructure.*

**Deployment-agnostic** — this function is identical whether the deployment is single-tenant or multi-tenant. The Platform Operator owns all infrastructure and operational concerns.

**Covers:**
- Installation and initial deployment (RKE2, Helm, networking, SSL)
- Version upgrades and patch procedures
- Platform health monitoring and alerting
- Backup and restore
- Troubleshooting infrastructure issues
- Performance tuning

**Golden Path:**

1. **Explanation:** Platform Architecture Overview (Ref: `Platform-Architecture-Overview.md`) ⚠️ *Placeholder — content not yet written*
2. **How-to:** Deploying the RKE2 Control Plane (Ref: `Deploying-the-RKE2-Control-Plane.md`) ⚠️ *Placeholder — content not yet written*
3. **How-to:** Helm-Based Application Deployment (Ref: `Helm-Based-Application-Deployment.md`) ⚠️ *Placeholder — content not yet written*
4. **How-to:** Monitoring the Platform (Ref: `Monitoring-the-Platform.md`) ⚠️ *Placeholder — content not yet written*
5. **How-to:** Upgrading the Platform (Ref: `Upgrading-the-Platform.md`) ⚠️ *Placeholder — content not yet written*
6. **How-to:** Backup and Restore (Ref: `Backup-and-Restore.md`) ⚠️ *Placeholder — content not yet written*

---

### 2.3 Partner

*Goal: Manage tenants and the commercial relationship on a hosted ExpertFlow installation.*

**Applies to:** Multi-tenant and hosted deployments only. In a single-tenant self-hosted deployment this function does not exist — the Administrator owns all configuration directly.

**Covers:**
- Tenant onboarding and provisioning
- Tenant lifecycle management (suspend, upgrade, decommission)
- Subscription tiers and capacity planning
- License management across tenants
- White-labeling the interface

**Golden Path:**

1. **How-to:** Onboarding a New Tenant (Ref: `Onboarding-a-New-Tenant.md`) ⚠️ *Placeholder — content not yet written*
2. **How-to:** Tenant Lifecycle Management (Ref: `Tenant-Lifecycle-Management.md`) ⚠️ *Placeholder — content not yet written*
3. **How-to:** Managing Licenses Across Tenants (Ref: `Managing-Licenses-Across-Tenants.md`) ⚠️ *Placeholder — content not yet written*
4. **How-to:** Subscription Tiers and Capacity Planning (Ref: `Subscription-Tiers-and-Capacity-Planning.md`) ⚠️ *Placeholder — content not yet written*
5. **How-to:** White-Labeling the Interface (Ref: `White-Labeling-the-Interface.md`) ⚠️ *Placeholder — content not yet written*

---

## Cluster 3: Builders

### 3.1 Conversation Designer / AI Specialist

*Goal: Design conversation flows and tune AI/NLU models.*

**Merges:** Conversation Designer + AI QA & NLU Specialist

**Why merged:** Both work primarily in Conversation Studio. Flow logic and NLU/bot tuning are deeply intertwined — you cannot design effective flows without understanding the AI models, and you cannot tune AI effectively without understanding the flow design. In practice, one person or team owns the entire "bot and flow" domain.

Sub-paths within this persona for larger orgs that do split roles:

- **Flow design track** — Conversation Studio, flow builder, handover logic, outbound dialing modes
- **AI / NLU track** — bot connector registration, NLU model tuning, AI-powered quality audits

**Golden Path:**

1. **Explanation:** Conversation Studio Fundamentals (Ref: `Configuration-Guide---Conversation-Studio_1017118849`)
2. **How-to:** Building Your First Studio Flow (Ref: `Conversation-Flow-for-Outbound-Dialing-Modes---to-be-reviewed_1132265580`) ⚠️ *Placeholder — source doc marked for review; replace with stable reference before publishing*
3. **How-to:** Registering Bot Connectors (Ref: `Registering-Bot-Connectors.md`)
4. **How-to:** Configuring AI-Powered Quality Audits (Ref: `Configuring-AI-Powered-Quality-Audits.md`)
5. **Tutorial:** Handover Logic: AI to Human (Ref: `AI-Assistant-handover-to-human-agent_1324417085`)

---

### 3.2 Developer / Integrator

*Goal: Build custom UIs, integrate external systems, and extend the platform.*

**Merges:** Frontend Developer + Integration Specialist

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

## Navigation Structure

### Top-Level Sections

| # | Section | Diátaxis type | Purpose |
| --- | --- | --- | --- |
| 1 | **Getting Started** | Tutorial | Role-based entry points — first steps for each persona cluster |
| 2 | **Platform Overview** | Orientation | High-level summaries for evaluation and orientation — not a persona path |
| 3 | **Capabilities** | Cross-cutting | Topic-based browsing — what the platform can do (replaces "Functional Areas") |
| 4 | **How-to Guides** | How-to | Task-based guides, organised by persona cluster |
| 5 | **Reference** | Reference | Technical specs, APIs, SDKs, schemas, hardware sizing, deployment topology |

### Getting Started Entry Flow

```
What brings you here?

┌─────────────────────────────────────────────────────────┐
│  I work in a contact center                             │
│  (handling interactions, monitoring teams, QA)          │
│  → Agent  |  Supervisor & QA Lead                       │
├─────────────────────────────────────────────────────────┤
│  I manage or run the platform                           │
│  (configuration, hosting, operations)                   │
│  → Administrator  |  Platform Operator  |  Partner      │
├─────────────────────────────────────────────────────────┤
│  I'm building on ExpertFlow                             │
│  (flows, bots, integrations, custom UIs)                │
│  → Conversation Designer  |  Developer / Integrator     │
└─────────────────────────────────────────────────────────┘
```

### Capabilities — Scope Definition

Topic-based browsing — what the platform can do. Organised by feature domain, not by persona. Readers arrive here when they want to understand a capability before deciding which how-to guide to follow.

**What lives here:**
- Omnichannel routing and queue management
- AI & automation (bots, co-pilot, NLU, quality audits)
- Conversation Studio (flow builder overview)
- Reporting & analytics
- Integrations & connectors overview
- Agent Desktop features
- Quality management

**What does NOT live here** (→ How-to Guides or Reference instead):
- Step-by-step task instructions (→ How-to Guides)
- API specs, SDK references, schemas (→ Reference)
- Deployment and infrastructure details (→ Reference)

**Why:** Capabilities is for understanding what the platform does. Once a reader is ready to act, they move to How-to Guides or Reference.

---

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
┌── Reference
│     ├── Architecture & Infrastructure
│     │     ├── Platform Architecture (detailed diagrams)
│     │     ├── Deployment Topology Reference
│     │     └── Hardware Sizing & Requirements
│     ├── API & SDK
│     │     ├── AgentManager SDK
│     │     ├── WebChannel SDK
│     │     └── Third-Party Activity API
│     ├── Schemas & Data Model
│     │     ├── CIM Message Schema
│     │     ├── Socket Events
│     │     └── Platform Objects
│     └── Reporting & Analytics
│           ├── Key Reporting Metrics
│           └── KPI Definitions
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

## Metadata Tagging Rules

```yaml
audience:
  # Cluster 1
  - agent
  - supervisor-qa

  # Cluster 2
  - administrator        # business configuration
  - platform-operator    # infrastructure & ops (deployment-agnostic)
  - partner              # tenant management & commercial

  # Cluster 3
  - conversation-designer
  - developer-integrator

  # Non-persona (no golden path, accessed by topic/search)
  - platform-overview    # evaluation/orientation content → Platform Overview section (NOT a persona — do not assign a golden path)
```

**Tagging rules:**

- A document can carry multiple audience tags. Example — a monitoring guide relevant to both the Platform Operator and the Partner:

  ```yaml
  audience:
    - platform-operator
    - partner
  ```

- `platform-operator` is deployment-agnostic — tag any installation, upgrade, monitoring, backup, or infrastructure content with this value regardless of whether the deployment is single-tenant or multi-tenant
- `partner` covers all tenant management and commercial content — onboarding, lifecycle, subscriptions, billing, white-labeling
- `hosting-partner` is retired — replace with `platform-operator` and/or `partner` as appropriate
- `platform-overview` is not a persona — do not create a golden path for it; content is surfaced via the Platform Overview nav section and direct search
- **Capabilities content** is feature-domain-based, not persona-based. Tag it with the audience tags of every persona that would read it — do not create a `capabilities` tag. Example — an omnichannel routing overview relevant to both Administrator and Supervisor:

  ```yaml
  audience:
    - administrator
    - supervisor-qa
  ```

- Hardware Sizing, deployment topology, and architecture diagrams carry no audience tag — they are Reference content, linked from multiple persona paths
