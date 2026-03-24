---
audience: [developer-integrator]
title: "Integration Specialist Guide"
summary: "Guide for integration specialists — Cisco UCCE/X, Finesse, channel connectors, bot connectors, CRM, Telegram, LinkedIn, reporting schema, and observability."
doc-type: landing
last-updated: 2026-03-18
---


This guide covers the full integration surface of ExpertFlow CX — connecting to Cisco voice infrastructure, registering channel and bot connectors, integrating CRM systems, and setting up observability.

---

## 1. Getting Started

| Document | Description |
| :--- | :--- |
| [Integrations Overview](./Integrations.md) | Overview of all supported integration types and how they fit into the platform architecture |

---

## 2. Cisco Integration

| Document | Description |
| :--- | :--- |
| [Finesse Integration Prerequisites](./Finesse-Integration-Prerequisites.md) | Network, license, and configuration requirements before starting a Cisco Finesse integration |
| [Environment Configurations for Cisco](./Environment-Configurations-for-Cisco.md) | All environment variables and settings required for the Cisco connector |
| [Cisco Voice Channel Configuration](./Cisco-Voice-Channel-Configuration.md) | Step-by-step configuration of the Cisco UCCE/X voice channel in Unified Admin |
| [Synchronizing Cisco Users and Teams](./Synchronizing-Cisco-Users-and-Teams.md) | How to sync agent and team data between Cisco and ExpertFlow CX |
| [Deploying Finesse Gadget](./Deploying-Finesse-Gadget.md) | Deploy the ExpertFlow CX gadget inside the Cisco Finesse desktop |
| [QM Connector for Cisco](./QM-Connector-for-Cisco.md) | Connecting the ExpertFlow QM module to Cisco call recording and quality infrastructure |
| [Cisco Integration Known Limitations](./Cisco-Integration-Known-Limitations.md) | Known constraints, version compatibility notes, and workarounds for Cisco integrations |

---

## 3. Channel Connectors

| Document | Description |
| :--- | :--- |
| [Channel Connector Developer Guide](./Channel-Connector-Developer-Guide.md) | Build a custom channel connector to bridge any external message source into ExpertFlow CX |
| [Channel Connector Configuration API](./Channel-Connector-Configuration.md) | API reference for registering and managing channel connectors programmatically |
| [Register Channel Connector](./Register-Channel-Connector.md) | How to register a new channel connector in Unified Admin |

---

## 4. Bot Connectors

| Document | Description |
| :--- | :--- |
| [Add Bot Connector](./Add-Bot-Connector.md) | Register and configure a bot connector in Unified Admin |
| [Bot Connector Developer Guide](./Bot-Connector-Developer-Guide.md) | Build a custom bot connector to connect any NLU engine to ExpertFlow CX |
| [Custom Connector-Bot Communication](./Custom-Connector-Bot-Communication.md) | Event protocol and message format for communication between custom connectors and bots |

---

## 5. Social & Third-Party Connectors

| Document | Description |
| :--- | :--- |
| [Telegram Connector Configuration Guide](./Telegram-Connector-Configuration-Guide.md) | Configure and deploy the Telegram bot connector |
| [Telegram Connector Limitations](./Telegram-Connector-Limitations.md) | Known constraints and unsupported features for the Telegram connector |
| [Telegram Connector Media Types Support](./Telegram-Connector-Media-Types-Support.md) | Supported inbound and outbound media types for the Telegram connector |
| [Facebook Connector Limitations](./Facebook-Connector-Limitations.md) | Known constraints for the Facebook/Instagram connector |
| [LinkedIn Standard Tier Upgrade Guide](./LinkedIn-Standard-Tier-Upgrade.md) | How to upgrade a LinkedIn app to Standard tier to unlock full connector functionality |

---

## 6. CRM & Data

| Document | Description |
| :--- | :--- |
| [CRM Connectors](./CRM-Connectors.md) | Overview of supported CRM integrations and how to configure them |
| [Reporting Database Schema Reference](./Reporting-Database-Schema-Reference.md) | Full schema reference for the ExpertFlow CX reporting database — tables, fields, and relationships |

---

## 7. Observability & Scheduling

| Document | Description |
| :--- | :--- |
| [Logging and Tracing Integration with OpenSearch](./Logging-and-Tracing-OpenSearch.md) | How to ship logs and distributed traces to an OpenSearch cluster |
| [Scheduled Activities](./Scheduled-Activities.md) | How the platform scheduler works and how to configure recurring integration jobs |
