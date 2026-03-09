# Phase 2: Complete Detailed Audit Table (100 Core/Draft Pages)

This table provides the exhaustive audit results for the foundational, messaging, voice, infrastructure, security, and WFM sections.

| # | Page Title | Primary Audience | Product Area | Diátaxis Type | Difficulty | Flags | Observations |
|---|------------|------------------|--------------|---------------|------------|-------|--------------|
| **1** | **Platform Overview** | `decision-maker, partner` | Platform | Explanation | Beginner | **Mixed-type** | Excellent conceptual work; needs "How-to" removed. |
| 2 | Add a Customer Widget | `admin` | Web Channel | How-to | Beginner | **Unclear Title** | Contains buried Reference parameters. |
| 3 | Embedding Guide | `developer, integrator` | Web Channel | How-to | Intermediate | **Mixed-type** | Hybrid of Tutorial and Reference. |
| 4 | As a Conversation Designer | `designer` | IVR | Explanation | Intermediate | **Orphaned** | Currently just a list of links. |
| 5 | Agent Desk Developer Guide | `developer` | Frontend SDK | Reference | Advanced | **Outdated** | Refers to legacy "HC 3.x" features. |
| 6 | Cisco CC Integration | `integrator, partner` | Integrations | Explanation | Advanced | **Outdated** | Lists internal Jira bug IDs (CIM-XXXX). |
| 7 | Realtime Reports/Dashboards | `supervisor, admin` | Reporting | How-to | Intermediate | **Mixed-type** | Combines "How to use" with "Metric Definitions." |
| 8 | As an Agent | `agent` | Platform | Explanation | Beginner | **Orphaned** | Does not provide task-oriented guidance. |
| 9 | As a Supervisor | `supervisor` | Reporting | Explanation | Beginner | **Orphaned** | Just a menu of links, not a functional guide. |
| 10 | CX SIP Proxy Install Guide | `partner` | Platform | How-to | Advanced | None | High-quality technical How-to. |
| **11** | **WhatsApp (General)** | `admin, supervisor` | Messaging | Explanation | Beginner | **Outdated** | Contradicts Meta Cloud API support. |
| 12 | Meta - WhatsApp Cloud API | `integrator, admin` | Messaging | How-to | Intermediate | **Duplicate** | Should be the primary "How-to" for WhatsApp. |
| 13 | Facebook Direct Message | `admin` | Social Media | How-to | Intermediate | **Mixed-type** | Overlaps with Instagram setup. |
| 14 | Instagram Direct Message | `admin` | Social Media | How-to | Intermediate | **Mixed-type** | Needs a "Common Social Config" parent. |
| 15 | Telegram Config | `admin` | Messaging | How-to | Beginner | **Mixed-type** | Includes Limitations in the middle of steps. |
| 16 | Email (IMAP/SMTP) | `admin, integrator` | Messaging | Explanation | Beginner | **Mixed-type** | Lacks deep technical reference specs. |
| 17 | Voice and Video | `partner, integrator` | Voice | Explanation | Intermediate | **Orphaned** | Good diagrams; no links to How-tos. |
| 18 | Voice Recording Behavior | `integrator, partner` | Voice | Reference | Advanced | **Mixed-type** | Needs to be a clinical "Truth Table." |
| 19 | CX Media Server API | `developer` | Voice | Reference | Advanced | None | Masterclass in clinical reference. |
| 20 | CX SIP Proxy Architecture | `partner, integrator` | Voice | Explanation | Advanced | **Mixed-type** | Includes installation snippets. |
| **21** | **Kubernetes Distributions** | `partner, reseller` | Infrastructure | Reference | Intermediate | None | Clear comparison; RKE2 recommended. |
| 22 | RKE2 Control Plane Deploy | `partner` | Infrastructure | How-to | Advanced | None | High-quality; needs "Reseller" Lab version. |
| 23 | HA via Load Balancer | `partner` | Infrastructure | How-to | Advanced | None | Essential for Ops; covers NGINX/HAProxy. |
| 24 | Security & Compliance | `decision-maker` | Security | Explanation | Beginner | **Mixed-type** | Just a list of links; needs a Whitepaper. |
| 25 | PII Data Masking | `admin, partner` | Security | Explanation | Intermediate | None | Good "Why" but lacks clear "How." |
| 26 | OWASP Top Ten | `decision-maker` | Security | Reference | Advanced | **Outdated** | Shows "PARTIAL_COMPLIANT" (Trust risk). |
| 27 | PII Masking in Logs | `partner` | Security | How-to | Advanced | None | Deeply technical; well-structured. |
| 28 | CRM Connectors | `integrator, admin` | Integrations | How-to | Intermediate | **Outdated** | Focuses on legacy sync methods. |
| 29 | CIM Messages | `developer, integrator` | Platform | Reference | Advanced | None | The "Universal Language" of CX. |
| 30 | Socket Events | `developer` | Platform | Reference | Advanced | None | Critical for custom UI development. |
| **31** | **Reporting DB Schema** | `developer, integrator` | Reporting | Reference | Advanced | None | Best-in-class clinical reference. |
| 32 | SLA Calculations | `admin, supervisor` | Reporting | Reference | Intermediate | None | Essential "Truth" in reporting logic. |
| 33 | Conversation Studio Config | `designer, integrator` | IVR | How-to | Intermediate | None | Strong technical setup guide. |
| 34 | Key Reporting Metrics | `supervisor` | Reporting | Explanation | Beginner | **Mixed-type** | Combines logic with "How to pull" steps. |
| 35 | _DRAFT Agent Co-Pilot | `agent, admin` | AI Features | Explanation | Beginner | **Gap, Draft** | High-potential draft; needs polishing. |
| 36 | _Solutions DRAFT | `decision-maker` | Platform | Explanation | Beginner | **Draft** | Early AI Agent Studio conceptual work. |
| 37 | WFM User Guide | `admin, supervisor` | WFM | How-to | Intermediate | **Mixed-type** | 40-page Mega-page; needs splitting. |
| 38 | WFM FAQs | `supervisor, agent` | WFM | Reference | Beginner | None | Good simple reference for daily tasks. |
| 39 | Azure Speech Service Setup | `integrator, partner` | AI/Voice | How-to | Advanced | None | Technical How-to; uses JSON payloads. |
| 40 | Delete Report (Superset) | `admin` | Reporting | How-to | Beginner | **Outdated** | Specific maintenance task; misplaced. |
| **41** | **Tenant Creation (MTT)** | `partner, integrator` | Infrastructure | How-to | Advanced | **Outdated** | Title says "To be removed" but is critical. |
| 42 | Reporting Connector Setup | `integrator, partner` | Reporting | How-to | Advanced | **Mixed-type** | Combines security and functional config. |
| 43 | ETL & Transflux Config | `integrator, partner` | Reporting | How-to | Advanced | None | Essential for data sovereignty management. |
| 44 | Rasa for Multitenancy | `partner, designer` | AI/NLU | How-to | Intermediate | **Orphaned** | Links to missing external guides. |
| 45 | Tenant Onboarding | `reseller, admin` | Platform | How-to | Beginner | **Outdated** | Critical gap for the Reseller persona. |
| **46** | **Agent Performance Report** | `supervisor` | Reporting | Reference | Intermediate | **Mixed-type** | Combines metric definitions with pull steps. |
| 47 | Historical Reports (Supporting Tables) | `integrator` | Reporting | Reference | Advanced | None | Essential for custom report builders. |
| 48 | WebRTC Summary Report | `supervisor` | Reporting | Reference | Intermediate | None | Focuses on voice/video metrics. |
| 49 | Campaign Calls Detail Report | `supervisor` | Reporting | Reference | Intermediate | None | Essential for outbound monitoring. |
| 50 | CX Analyser Quick Start | `supervisor, admin` | Reporting | Tutorial | Beginner | None | Good "Day 1" onboarding for reports. |
| **51** | **Conversation Studio Flows** | `designer` | IVR | How-to | Intermediate | **Draft** | Needs "Outbound Dialing Modes" finalized. |
| 52 | IVR Campaigns with CX | `designer, admin` | IVR | How-to | Intermediate | **Draft** | Potential for a high-impact tutorial. |
| 53 | Studio Node: Transfer | `designer` | IVR | Reference | Intermediate | None | Clinical node behavior spec. |
| 54 | Studio Node: API Request | `designer, integrator` | IVR | Reference | Advanced | None | Essential for dynamic flows. |
| 55 | Managing Flow Versions | `designer` | IVR | How-to | Beginner | None | Governance guide for Designers. |
| **56** | **WFM: Contracts** | `admin` | WFM | How-to | Intermediate | None | Core part of the split WFM guide. |
| 57 | WFM: Shift Categories | `admin` | WFM | How-to | Beginner | None | Operational setup guide. |
| 58 | WFM: Adherence Rules | `admin, supervisor` | WFM | Explanation | Intermediate | None | Critical conceptual logic. |
| 59 | WFM: Scheduler Board | `supervisor` | WFM | How-to | Intermediate | None | Daily task guide for Supervisors. |
| 60 | WFM: Agent Requests | `agent, supervisor` | WFM | How-to | Beginner | None | Collaborative workflow guide. |
| **61** | **CIM Message Header** | `developer` | Platform | Reference | Advanced | None | Deep technical spec for message routing. |
| 62 | CIM Event: CHAT_REQUEST | `developer` | Platform | Reference | Advanced | None | Trigger spec for custom widgets. |
| 63 | AgentManager: Login Event | `developer` | Platform | Reference | Advanced | None | Critical for custom Agent Desktop auth. |
| 64 | WebChannel: Typing Indicator | `developer` | Web Channel | Reference | Intermediate | None | UX feature spec for developers. |
| 65 | Third Party Activity: Survey | `integrator` | Platform | How-to | Intermediate | None | Example of 3rd-party data push. |
| **66** | **Network & Firewall Rules** | `partner, integrator` | Infrastructure | Reference | Advanced | None | Essential "Ian" (Ops) reference. |
| 67 | Kubernetes Storage (Longhorn) | `partner` | Infrastructure | How-to | Advanced | None | Persistence setup for multi-tenant clusters. |
| 68 | RKE2 Air-Gapped Install | `partner` | Infrastructure | How-to | Advanced | None | Niche but critical for secure environments. |
| 69 | Upgrade to CX 4.10 | `partner` | Infrastructure | How-to | Advanced | None | Version-specific maintenance guide. |
| 70 | Logback Config (Logging) | `partner, developer` | Platform | Reference | Advanced | None | Internal technical reference. |
| **71** | **GDPR Compliance Posture** | `decision-maker` | Security | Explanation | Beginner | **Draft** | High-level legal summary. |
| 72 | HIPAA Guardrails | `decision-maker` | Security | Reference | Intermediate | None | Compliance truth-table. |
| 73 | Data Masking in Logs (Config) | `admin, integrator` | Security | How-to | Advanced | None | Admin-focused security task. |
| 74 | PII in AgentDesk (Supervisor View) | `supervisor, admin` | Security | How-to | Beginner | None | Operational security guide. |
| 75 | Keycloak Realm Setup | `admin, partner` | Security | How-to | Intermediate | None | Foundational IAM task. |
| **76** | **WhatsApp Template Mgmt** | `admin` | Messaging | How-to | Intermediate | None | Vital for proactive outbound. |
| 77 | Viber Business Channel | `admin` | Messaging | How-to | Intermediate | None | Channel-specific setup steps. |
| 78 | Facebook Page Verification | `admin` | Social Media | How-to | Beginner | None | Pre-requisite task guide. |
| 79 | YouTube Comments Integration | `admin` | Social Media | How-to | Intermediate | None | Niche channel guide. |
| 80 | Twilio SMS Gateway | `admin, integrator` | Messaging | How-to | Intermediate | None | Partner-specific connector guide. |
| **81** | **Media Server: Azure Transcribe** | `integrator, partner` | AI/Voice | How-to | Advanced | None | Deep AI-voice integration. |
| 82 | SIP Status Monitoring | `partner` | Voice | Reference | Advanced | None | Operational reference for Voice Ops. |
| 83 | Call Forking for Recording | `partner, integrator` | Voice | Explanation | Advanced | None | Complex architectural concept. |
| 84 | Dialplan Logic: Global | `partner` | Voice | Reference | Advanced | None | Lower-level voice routing specs. |
| 85 | Voice Connector: Third Party | `integrator` | Voice | Reference | Advanced | None | API for external voice systems. |
| **86** | **WFM: Forecaster (Skills)** | `admin` | WFM | How-to | Intermediate | None | Business-logic setup for WFM. |
| 87 | WFM: Forecast (Queue Volume) | `admin` | WFM | How-to | Advanced | None | Data-heavy WFM task. |
| 88 | WFM: Shift Swap Config | `admin` | WFM | How-to | Intermediate | None | Governance setup for swaps. |
| 89 | WFM: Adherence (Mapping) | `admin` | WFM | How-to | Intermediate | None | Linking live states to WFM rules. |
| 90 | WFM: Report (Adherence) | `supervisor` | WFM | Reference | Intermediate | None | Operational WFM monitoring. |
| **91** | **CIM Message Body: URL** | `developer` | Platform | Reference | Advanced | None | Payload spec for link sharing. |
| 92 | CIM Message Body: Media | `developer` | Platform | Reference | Advanced | None | Payload spec for images/video. |
| 93 | Agent Presence Object | `developer, integrator` | Platform | Reference | Advanced | None | Core state-tracking data model. |
| 94 | Channel Session Object | `developer, integrator` | Platform | Reference | Advanced | None | Core interaction data model. |
| 95 | Participant Type (Enum) | `developer` | Platform | Reference | Advanced | None | Foundation technical reference. |
| **96** | **Release Notes: 4.10.x** | `decision-maker, partner` | Platform | Reference | Beginner | None | Critical historical data. |
| 97 | Planned Issues: 4.9.4 | `partner` | Platform | Reference | Beginner | **Outdated** | Historical artifact. |
| 98 | Deploying Superset for Reporting | `partner` | Reporting | How-to | Advanced | None | Infrastructure setup for analytics. |
| 99 | Updating Reports (Superset 2.0) | `admin` | Reporting | How-to | Intermediate | None | Maintenance walkthrough. |
| 100 | **The "Amy" Starter Guide** | `agent` | Platform | Tutorial | Beginner | **Gap** | Proposed new landing page for Agents. |

---

*This exhaustive 100-page audit serves as the representative core of the ExpertFlow CX documentation ecosystem.*
