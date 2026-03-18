---
title: "Solution Admin Guide"
summary: "Guide for solution admins — initial setup, routing, queues, channels, agent desk, security, reporting, voice, and system operations."
doc-type: landing
last-updated: 2026-03-18
---

# Solution Admin Guide

This guide covers the full administrative surface of ExpertFlow CX for a solution admin (Olivia) — from initial platform setup and routing configuration to channel onboarding, security hardening, and ongoing operations.

---

## 1. Initial Setup

| Document | Description |
| :--- | :--- |
| [Channel and Connector Setup](./Channel-and-Connector-Setup.md) | High-level steps for onboarding a new channel and registering its connector |
| [User Management](./User-Management.md) | Creating, editing, and deactivating users; role assignments and team membership |
| [Adding Languages and Timezones](./Languages-Timezones-Settings.md) | Configure supported languages and timezone settings for the platform |
| [Infrastructure Sizing Guidelines](./Sizing-Guidelines.md) | Recommended hardware and resource sizing for different deployment scales |

---

## 2. Identity & Security

| Document | Description |
| :--- | :--- |
| [IAM (Keycloak) Configuration Guide](./IAM-Keycloak-Configuration.md) | Configure Keycloak realms, clients, and SSO for the platform |
| [2FA Email Configuration Guide](./2FA-Email-Configuration-Guide.md) | Set up email-based two-factor authentication for agents and admins |
| [2FA Service Technical Reference](./2FA-Service-Technical-Reference.md) | Technical details of the 2FA service — OTP flow, token lifetime, and configuration parameters |
| [Encryption at Rest Configuration Guide](./Encryption-at-Rest-Configuration-Guide.md) | Configure encryption for data at rest across MongoDB, file storage, and backups |
| [Configuring User Inactivity Logout](./User-Inactivity-Logout-Setup.md) | Automatically log out inactive users after a configurable timeout period |
| [Vault Configuration](./Vault-Configuration.md) | Set up HashiCorp Vault for secrets management |
| [Vault Dynamic Credentials — ActiveMQ](./Vault-Dynamic-Credentials-ActiveMQ.md) | Configure Vault to issue short-lived dynamic credentials for ActiveMQ |
| [Vault Dynamic Credentials — MongoDB](./Vault-Dynamic-Credentials-MongoDB.md) | Configure Vault to issue short-lived dynamic credentials for MongoDB |
| [Vault Dynamic Credentials — Redis](./Vault-Dynamic-Credentials-Redis.md) | Configure Vault to issue short-lived dynamic credentials for Redis |

---

## 3. Routing Configuration

| Document | Description |
| :--- | :--- |
| [Media Routing Domains (MRD) Overview](./Media-Routing-Domains-MRD-Overview.md) | How MRDs logically separate different media types and channel groups |
| [Routing Attributes and Precision Queues](./Routing-Attributes-and-Queues.md) | Define agent skills and attributes for attribute-based routing |
| [Precision Routing](./Precision-Routing.md) | Configure multi-attribute routing rules for precise agent-customer matching |
| [Priority Routing](./Priority-Routing.md) | Set queue priority levels to control how competing interactions are ordered |
| [Queue Priority](./Queue-Priority.md) | Configure per-queue priority weights |
| [Queue Wait Time and Position](./Queue-Wait-Time-and-Position.md) | How queue position and estimated wait time are calculated and surfaced to customers |
| [Routing Strategy: Pull Mode](./Routing-Strategy-Pull-Mode.md) | Configure pull-based routing where agents fetch interactions from a list |
| [Agent and Queue Mapping](./Agent-and-Queue-Mapping.md) | How agents are assigned to queues and how assignments affect routing |
| [Customer Interaction Profiles Overview](./Customer-Interaction-Profiles-Overview.md) | Create customer profiles that drive personalized routing and priority decisions |

---

## 4. Agent Desk Configuration

| Document | Description |
| :--- | :--- |
| [Configure AgentDesk Settings](./Configure-AgentDesk-Settings.md) | Global Agent Desk settings — message formatting, file sharing, and UI behavior |
| [Configuring Reason Codes](./Configuring-Reason-Codes.md) | Define Not Ready and logout reason codes for agent state tracking |
| [Configuring Wrap-up Forms](./Configuring-Wrap-up-Forms.md) | Create and assign wrap-up forms to channels and queues |
| [Form Builder User Guide](./Form-Builder-User-Guide.md) | Use the drag-and-drop form builder to design wrap-up and survey forms |
| [Auto-Sync State Logic](./Auto-Sync-State-Logic.md) | How agent state is automatically synced between ExpertFlow CX and Cisco when integrated |
| [Customer and Agent SLA Implementation Details](./Customer-Agent-SLA-Implementation.md) | Technical details of how customer and agent SLA thresholds are tracked and enforced |

---

## 5. Digital Channel Configuration

| Document | Description |
| :--- | :--- |
| [WhatsApp Cloud API Configuration](./WhatsApp-Cloud-API-Configuration.md) | Configure the Meta WhatsApp Cloud API channel |
| [WhatsApp Cloud API Limitations](./WhatsApp-Cloud-API-Limitations.md) | Known constraints and supported media formats for the WhatsApp Cloud API connector |
| [360-Connector Configuration Guide](./360-Connector-Configuration-Guide.md) | Configure the 360dialog WhatsApp BSP connector |
| [Email Channel Configuration Guide (IMAP/SMTP)](./Email-IMAP-SMTP-Configuration-Guide.md) | Connect an email account via IMAP/SMTP |
| [Facebook Channel Configuration Guide](./Facebook-Configuration-Guide.md) | Configure the Facebook/Instagram channel connector |
| [Instagram Connector Configuration & Deployment](./Instagram-Connector-Configuration-Guide.md) | Deploy and configure the Instagram connector |
| [Viber Connector Configuration & Deployment](./Viber-Connector-Configuration-Guide.md) | Deploy and configure the Viber connector |
| [Twilio SMS / MMS Connector Configuration](./Twilio-SMS-MMS-Configuration-Guide.md) | Configure the Twilio SMS/MMS connector |
| [SMPP Configuration Guide](./SMPP-Configuration-Guide.md) | Configure SMS delivery via direct SMPP protocol |
| [Twitter Connector Limitations & Highlights](./Twitter-Connector-Limitations.md) | Known constraints and key behaviors of the Twitter (X) connector |
| [YouTube Connector Limitations & Highlights](./YouTube-Connector-Limitations.md) | Known constraints and key behaviors of the YouTube comment connector |

---

## 6. Customer Widget

| Document | Description |
| :--- | :--- |
| [Configuring the Customer Widget](./Configuring-the-Customer-Widget.md) | Customize and deploy the embeddable web chat widget |
| [Customer Widget Features & Capabilities](./Customer-Widget-Features-Capabilities.md) | Full feature reference for the customer-facing web widget |

---

## 7. Voice Configuration

| Document | Description |
| :--- | :--- |
| [Accessing CX Voice Components](./Accessing-CX-Voice-Components.md) | How to access and manage the FreeSWITCH/EFSwitch voice server |
| [WebRTC Channel Configuration Guide](./WebRTC-Configuration-Guide.md) | Configure browser-based voice and video using WebRTC |
| [Media Server Configuration for CX Voice](./Media-Server-Configuration-CX-Voice.md) | Set up the media server for voice call recording and processing |
| [Media Server: Azure Transcription Setup](./Media-Server-Azure-Transcription-Setup.md) | Configure Azure Cognitive Services for real-time voice transcription |
| [Media Server: Google Transcription Setup](./Media-Server-Google-Transcription-Setup.md) | Configure Google Speech-to-Text for real-time voice transcription |
| [Voice Channel Configuration: Limitations](./Voice-Channel-Configuration-Limitations.md) | Known constraints and proposed solutions for voice channel configuration |

---

## 8. Outbound & Campaigns

| Document | Description |
| :--- | :--- |
| [Managing Outbound Campaigns](./Managing-Outbound-Campaigns.md) | Create, schedule, and manage outbound dialing campaigns |
| [Do Not Contact (DNC) Lists](./DNC-Lists.md) | Configure and maintain DNC lists to ensure regulatory compliance |

---

## 9. AI Configuration

| Document | Description |
| :--- | :--- |
| [AI-powered Customer Experience](./AI-powered-Customer-Experience.md) | Enable and configure AI features — Co-Pilot, sentiment analysis, and auto-scoring |

---

## 10. Reporting & Analytics

| Document | Description |
| :--- | :--- |
| [EFCX Reports Configuration (Superset)](./Superset-Reports-Configuration.md) | Configure Apache Superset for ExpertFlow CX reporting |
| [Superset Reports Configuration (Import & SSL)](./Superset-Reports-Import-Config.md) | Import report definitions and configure SSL for Superset |
| [Superset Alerts & Reports Feature Enablement](./Superset-Alerts-Reports-Enablement.md) | Enable the Superset alerts and scheduled reports feature |
| [Deleting Reports from Superset 2.0](./Superset-Report-Deletion-Guide.md) | How to safely delete custom reports in Superset 2.0 |
| [Monitoring Tenant License Consumption](./Monitoring-Tenant-License-Consumption.md) | Monitor per-tenant license usage and enforce consumption limits |

---

## 11. System Operations

| Document | Description |
| :--- | :--- |
| [Archival Configuration](./Archival-Configuration.md) | Configure interaction archival — retention policies, storage targets, and triggers |
| [Migrate EF IAM Users to Different Instances or Realms](./Migrate-EF-IAM-Users.md) | Move users between Keycloak instances or realms without data loss |
| [Migrating Keycloak Groups to CX Teams](./Migrate-Keycloak-Groups-to-CX-Teams.md) | Migrate legacy Keycloak groups to ExpertFlow CX team structures |
| [Extending RKE2 SSL Certificate Expiry](./RKE2-SSL-Certificate-Extension.md) | Renew or extend SSL certificates on the RKE2 cluster |
| [Change Default ActiveMQ Passwords Using ConfigMap](./Change-Default-ActiveMQ-Passwords.md) | Rotate default ActiveMQ credentials via Kubernetes ConfigMap |
| [Accessing Kubernetes Logs](./Accessing-Kubernetes-Logs.md) | How to access pod and component logs in the RKE2 cluster |
| [MongoDB Slow Query Logs](./MongoDB-Slow-Query-Logs.md) | Enable and interpret MongoDB slow query logging for performance troubleshooting |
| [Redis Log Monitoring via Slowlogs](./Redis-Slowlogs.md) | Use Redis SLOWLOG to identify and diagnose slow commands |

---

## 12. Security Advisories

| Document | Description |
| :--- | :--- |
| [Vulnerability Report — Release 4.10.4](./Vulnerability-Report-4.10.4.md) | CVE disclosures and mitigations for ExpertFlow CX 4.10.4 |
| [Vulnerability Report — Release 4.10](./Vulnerability-Report-4.10.md) | CVE disclosures and mitigations for ExpertFlow CX 4.10 |
| [Vulnerability Report — Release 4.9.4](./Vulnerability-Report-4.9.4.md) | CVE disclosures and mitigations for ExpertFlow CX 4.9.4 |
