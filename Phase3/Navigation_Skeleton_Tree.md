# Navigation Skeleton Tree — ExpertFlow CX Docs

**Status:** Proposed skeleton (2 levels deep, representative examples only)
**Based on:** Revised Persona Model + Phase4 content inventory (~346 files)
**Next step:** Validate structure, then map all files

---

## Structure at a Glance

```
1. Getting Started
2. Platform Overview
3. Capabilities
4. How-to Guides
5. Reference
```

---

## 1. Getting Started

*Entry point for new users. One path per persona cluster. Tutorial-type content.*

```
Getting Started
  ├── For Agents
  │     └── e.g. Agent-Quick-Start-Guide.md
  ├── For Supervisors & QA Leads
  │     └── e.g. Monitoring-Your-Team-in-Real-Time.md, Evaluator-Guide.md
  ├── For Administrators
  │     └── e.g. Unified-Admin-Guide.md, Channel-Onboarding-Guide.md
  ├── For Hosting Partners
  │     └── e.g. Deploying-the-RKE2-Control-Plane.md, Onboarding-a-New-Tenant.md
  ├── For Conversation Designers
  │     └── e.g. Conversation-Studio-Configuration-Guide.md
  └── For Developers & Integrators
        └── e.g. Agent-Desk-Developer-Guide.md
```

**Source:** `Getting_Started/` (16 files — most stay here, 2–3 move out, see notes)

---

## 2. Platform Overview

*Orientation and evaluation content. Not a persona path. Replaces Decision_Maker/ folder.*

```
Platform Overview
  ├── What is ExpertFlow CX?
  │     └── e.g. Expertflow-CX-Platform-Overview.md
  ├── Platform Architecture
  │     └── e.g. Platform-Architecture.md, cx_architecture.svg
  │           (summary only — detailed diagrams link to Reference)
  ├── Security & Compliance
  │     └── e.g. Security-and-Compliance-Whitepaper.md
  │           (overview only — detailed compliance guides live in Capabilities)
  ├── AI & Automation Capabilities
  │     └── e.g. AI-Self-Service-Capabilities.md, Customer-Journey-Orchestration.md
  ├── Supported Integrations & Compatibility
  │     └── e.g. WFM-Compatibility-Guide.md, Hybrid-Chat-to-CX-Migration-Comparison.md
  └── Release & Versioning
        └── e.g. Release-Lifecycle-and-Versioning.md
```

**Source:** `Role_Based_Guides/Decision_Maker/` (11 files — entire folder repurposed here)
**+ from Getting_Started:** Expertflow-CX-Platform-Overview.md, Security-and-Compliance-Whitepaper.md

---

## 3. Capabilities

*Topic-based browsing — what the platform can do. Replaces "Functional Areas" naming.*

```
Capabilities
  ├── Digital Channels
  │     ├── WhatsApp, Facebook, Email, Telegram, LinkedIn, Twitter, YouTube, SMPP
  │     └── Customer Widget
  ├── Voice & Video
  │     ├── Inbound / Outbound Calls
  │     ├── WebRTC & Browser-Based Calling
  │     └── Dialer & Outbound Campaigns
  ├── Reporting & Analytics
  │     ├── Real-time Dashboards
  │     ├── Historical Reports
  │     └── Conversation Analytics
  ├── Quality Management
  │     ├── Evaluation & Scoring
  │     ├── AI-Powered QA
  │     └── Screen & Audio Recording
  ├── Workforce Management
  │     ├── Scheduling
  │     └── Adherence & Forecasting
  └── Security & Compliance
        ├── GDPR, HIPAA, PCI-DSS
        └── Audit Logging
```

**Source:** `Functional_Areas/` (86 files — rename section, content stays largely intact)
**+ Quality Management content** pulled in from `Role_Based_Guides/Quality_Manager/` and `Role_Based_Guides/Human_Evaluator/` (concept/overview docs only; task docs stay in How-to Guides)

---

## 4. How-to Guides

*Task-based guides, organised by persona cluster. Bulk of the content.*

```
How-to Guides
  ├── Agent
  │     └── e.g. Accept-a-Conversation.md, Wrap-up-and-Follow-up-Work.md,
  │           Agent-Co-Pilot.md, Pause-Resume-Conversation.md
  │     Source: Role_Based_Guides/Agent/ (17 files)
  │
  ├── Supervisor & QA Lead          ← merged cluster
  │     ├── Monitoring & Intervention
  │     │     └── e.g. Silent-Monitoring.md, Barge-in-and-Intervention.md,
  │     │           Realtime-Detailed-Dashboards.md
  │     ├── Quality Evaluation
  │     │     └── e.g. Auditing-and-Scoring-Conversations.md,
  │     │           Designing-Evaluation-Forms.md, Finding-Conversations-for-Audit.md
  │     └── Reporting & Team Management
  │           └── e.g. Agent-Performance-Dashboard-Reference.md, Managing-Teams-and-Members.md
  │     Source: Role_Based_Guides/Supervisor/ (36) + Human_Evaluator/ (5) + Quality_Manager/ (7)
  │
  ├── Administrator
  │     ├── Routing & Queues
  │     ├── Channel Setup
  │     ├── User & Team Management
  │     ├── Security Configuration
  │     └── Platform Operator ↓ (sub-path, see below)
  │     Source: Role_Based_Guides/Solution_Admin/ (67 files — largest single group)
  │
  ├── Hosting Partner               ← merged cluster
  │     ├── Infrastructure Deployment
  │     │     └── e.g. Helm-Based-Application-Deployment.md, CX-Voice-Deployment.md
  │     ├── Tenant Management
  │     │     └── e.g. Tenant-Lifecycle-Management.md, Managing-Licenses-Across-Tenants.md
  │     ├── Commercial Management
  │     │     └── e.g. Subscription-Tiers-and-Capacity-Planning.md, White-Labeling-the-Interface.md
  │     └── Platform Operator ↓ (sub-path, see below)
  │     Source: Role_Based_Guides/Infrastructure_Hosting_Partner/ (33) + Reseller/ (7)
  │
  ├── [Platform Operator sub-path]  ← shared, reached from Admin or Hosting Partner
  │     ├── Monitoring System Health
  │     ├── Upgrades & Patching
  │     ├── Backup & Restore
  │     └── Troubleshooting
  │     Source: scattered across Solution_Admin/ and Infrastructure_Hosting_Partner/
  │             ⚠ content gap — several guides need to be created
  │
  ├── Conversation Designer / AI Specialist   ← merged cluster
  │     ├── Building Flows
  │     │     └── e.g. Conversation-Flow-for-Outbound-Dialing-Modes.md,
  │     │           Creating-Survey-Forms-and-Flows.md
  │     ├── Bot & NLU Configuration
  │     │     └── e.g. Registering-Bot-Connectors.md, NLU-Digital-Bots-Concepts.md
  │     └── AI Quality Tuning
  │           └── e.g. AI-Orchestration-and-LLM-Logic.md, AI-Powered-Quality-Assurance.md
  │     Source: Role_Based_Guides/Conversation_Designer/ (11) + AI_Quality_NLU_Specialist/ (5)
  │
  └── Developer / Integrator        ← merged cluster
        ├── Agent UI Development
        │     └── e.g. AgentManager-SDK-Integration-Guide.md, CRM-Agent-Desk-Post-Message-Events.md
        ├── Customer-Facing Channels
        │     └── e.g. Customer-Facing-SDK.md, Custom-Bot-Connector-Development.md
        └── System Integrations
              └── e.g. CRM-Connectors.md, Channel-Connector-Developer-Guide.md,
                    Cisco-Voice-Channel-Configuration.md
        Source: Role_Based_Guides/Frontend_Developer/ (how-to files only) +
                Role_Based_Guides/Integration_Specialist/ (24 files)
        ⚠ CIM-Message-Schema/ and Socket_Events/ move to Reference (see below)
```

---

## 5. Reference

*Look-up content. Single home for technical specs. Linked from How-to Guides and Platform Overview.*

```
Reference
  ├── Architecture & Infrastructure
  │     ├── Platform Architecture (detailed diagrams)
  │     │     └── e.g. SIP-Proxy-Architecture.md, detailed cx_architecture.svg
  │     ├── Deployment Topology
  │     │     └── e.g. Kubernetes-Distributions.md, System-Behaviour-in-Failover.md
  │     └── Hardware Sizing & Requirements
  │           └── e.g. Hardware-Sizing-Calculator.md, Sizing-Guidelines.md,
  │                 CX-Voice-Platform-Sizing.md
  │
  ├── API & SDK
  │     ├── AgentManager SDK
  │     │     └── AgentManager-SDK-Integration-Guide.md (moved from Frontend_Developer/)
  │     ├── WebChannel / Customer-Facing SDK
  │     │     └── JavaScript-SDK.md, Customer-Facing-SDK.md
  │     └── REST APIs
  │           └── e.g. Business-Calendar-API.md, Form-APIs.md,
  │                 Queue-Flushing-API.md, Scheduler-API-Reference.md
  │
  ├── Schemas & Data Model
  │     ├── CIM Message Schema (16 files — moved from Frontend_Developer/)
  │     │     └── Plain-Text-Message.md, Button-Message.md, Email-Message.md …
  │     ├── Socket Events (38 files — moved from Frontend_Developer/)
  │     │     └── onCimEvent.md, taskRequest.md, agentPresence.md …
  │     └── Platform Objects & Data Model
  │           └── Platform-Objects-and-Data-Model.md, Conversation-Life-Cycle-Objects.md
  │
  └── Glossary
        └── Glossary-of-Key-Terms.md (moved from Getting_Started/)
```

**Source:** Pulled from multiple locations:
- `Frontend_Developer/CIM-Message-Schema/` (16 files)
- `Frontend_Developer/Socket_Events/` (38 files)
- `Infrastructure_Hosting_Partner/Hardware-Sizing-Calculator.md`
- `Solution_Admin/Sizing-Guidelines.md`
- `Getting_Started/Glossary-of-Key-Terms.md`
- Selected SDK/API files from `Frontend_Developer/`

---

## Key Structural Changes Summary

| Change | From | To | Impact |
| --- | --- | --- | --- |
| Decision_Maker/ → Platform Overview | Role_Based_Guides/Decision_Maker/ (11 files) | Platform Overview section | Folder renamed/repurposed |
| Supervisor + Evaluator + QM merged | 3 separate folders (48 files) | How-to Guides > Supervisor & QA Lead | Content consolidation |
| Host + Reseller merged | 2 separate folders (40 files) | How-to Guides > Hosting Partner | Content consolidation |
| Conv. Designer + AI/NLU merged | 2 separate folders (16 files) | How-to Guides > Conversation Designer | Content consolidation |
| Frontend Dev + Integration merged | 2 separate folders (45 files) | How-to Guides > Developer / Integrator | Content consolidation |
| CIM Schema + Socket Events → Reference | Frontend_Developer/ subfolders (54 files) | Reference > Schemas & Data Model | Move out of role folder |
| Functional_Areas → Capabilities | Section rename only | No file moves, rename section | Low effort |
| Platform Operator sub-path | Scattered / missing | How-to Guides > Admin + Hosting Partner | Content gap to fill |

---

## Content Gaps Identified

| Gap | Where it should live | Notes |
| --- | --- | --- |
| Platform Operator guides (monitoring, upgrade, backup) | How-to Guides > Platform Operator sub-path | No dedicated content exists; scattered fragments in Solution_Admin/ and Infrastructure_Hosting_Partner/ |
| Getting Started guide for Hosting Partner | Getting Started > For Hosting Partners | Deploying-the-RKE2-Control-Plane.md exists but is a deep-dive, not a true quick-start |
| Getting Started guide for Conversation Designer | Getting Started > For Conversation Designers | Conversation-Studio-Configuration-Guide.md is config reference, not an onboarding tutorial |

---

## Notes for Full Mapping Phase

- **Solution_Admin/ is the largest folder (67 files)** and the least consistent — it mixes pure how-to guides, reference specs, operational runbooks, and security configuration. Will need the most curation effort.
- **Getting_Started/ needs pruning** — Cisco-Contact-Center-Integration-Reference.md and Configuring-AI-Powered-Quality-Audits.md are not entry-point content; they should move to How-to Guides.
- **Security_Compliance/ Functional Area** has an interesting dual home: the overview/compliance briefs belong in Platform Overview; the detailed configuration guides belong in Capabilities or How-to Guides > Administrator. Worth flagging for the full mapping phase.
