---
title: "Frontend Developer Guide"
summary: "Guide for frontend developers — AgentManager SDK, WebChannel SDK, CIM message schema, socket events, routing lifecycle, and custom bot/connector development."
doc-type: landing
last-updated: 2026-03-18
---

# Frontend Developer Guide

This guide covers the developer-facing surface of ExpertFlow CX — SDKs, APIs, message schemas, socket events, and the data model underpinning the routing and interaction lifecycle.

---

## 1. SDKs

| Document | Description |
| :--- | :--- |
| [AgentManager SDK Integration Guide](./AgentManager-SDK-Integration-Guide.md) | Embed agent capabilities into custom UIs — authentication, state management, conversation handling |
| [Customer-Facing SDK for Omnichannel Communication](./Customer-Facing-SDK.md) | Build custom customer-facing widgets and apps on top of the CX communication layer |
| [JavaScript SDK for Customer-Facing Channels](./JavaScript-SDK.md) | Lightweight JS SDK for web and mobile customer interfaces |

---

## 2. Core Concepts & Data Model

| Document | Description |
| :--- | :--- |
| [Interaction Model: Rooms, Actors, and Events](./Interaction-Model-Overview.md) | The fundamental model of how conversations, agents, bots, and customers are represented |
| [Platform Objects and Data Model](./Platform-Objects-and-Data-Model.md) | Schema reference for core platform entities — agents, queues, channels, and interactions |
| [Conversation Life-Cycle Objects](./Conversation-Life-Cycle-Objects.md) | State machine and object model for a conversation from creation to closure |
| [Agent Task and Routing Lifecycle](./Agent-Task-Routing-Lifecycle.md) | How a task is created, routed, assigned, and resolved from the developer's perspective |

---

## 3. APIs

| Document | Description |
| :--- | :--- |
| [Action Message: Bot Communication](./Action-Message-Bot-Communication.md) | How bots send action messages to trigger platform behavior (transfer, end session, set attributes) |
| [CRM & Agent Desk Post Message Events](./CRM-Agent-Desk-Post-Message-Events.md) | postMessage events fired by the Agent Desk iframe for CRM embedding and external integrations |
| [Form APIs](./Form-APIs.md) | API reference for programmatically reading and submitting wrap-up and survey forms |
| [Business Calendar API Configurations](./Business-Calendar-API.md) | API for querying business hours, holiday schedules, and timezone settings |
| [Queue Flushing API](./Queue-Flushing-API.md) | API to drain or flush a queue — use cases, request format, and side effects |
| [Scheduler API & Workflow Reference](./Scheduler-API-Reference.md) | Schedule tasks, callbacks, and deferred actions via the platform scheduler |
| [Routing Engine Developer Guide](./Routing-Engine-Developer-Guide.md) | How to interact with and extend the routing engine programmatically |

---

## 4. CIM Message Schema

The CIM (Customer Interaction Message) schema defines the structure of every message exchanged on the platform.

| Document | Description |
| :--- | :--- |
| [Message Header](./CIM-Message-Schema/Message-Header.md) | Standard header fields present on every CIM message |
| [Message Body](./CIM-Message-Schema/Message-Body.md) | Body structure and common fields across message types |
| [Plain Text Message](./CIM-Message-Schema/Plain-Text-Message.md) | Schema for plain text messages |
| [Button Message](./CIM-Message-Schema/Button-Message.md) | Schema for interactive button/list messages |
| [Carousel Message](./CIM-Message-Schema/Carousel-Message.md) | Schema for carousel card messages |
| [Contact Message](./CIM-Message-Schema/Contact-Message.md) | Schema for contact card messages |
| [Location Message](./CIM-Message-Schema/Location-Message.md) | Schema for location pin messages |
| [URL Message](./CIM-Message-Schema/URL-Message.md) | Schema for URL link messages |
| [Email Message](./CIM-Message-Schema/Email-Message.md) | Schema for email-type messages |
| [Notification Message](./CIM-Message-Schema/Notification-Message.md) | Schema for system notification messages |
| [Delivery Notification Message](./CIM-Message-Schema/Delivery-Notification-Message.md) | Schema for message delivery and read receipts |
| [Receipt Message](./CIM-Message-Schema/Receipt-Message.md) | Schema for transaction receipt messages |
| [WrapUp Message](./CIM-Message-Schema/WrapUp-Message.md) | Schema for wrap-up and disposition messages |

---

## 5. Bot & Connector Development

| Document | Description |
| :--- | :--- |
| [Custom Bot Connector Development](./Custom-Bot-Connector-Development.md) | Build a custom bot connector to integrate any NLU or AI engine with ExpertFlow CX |

---

## 6. Channel Integrations

| Document | Description |
| :--- | :--- |
| [YouTube Integration Configuration (Developer)](./YouTube-Integration-Configuration-Developer.md) | Developer-level steps for configuring the YouTube connector and handling comment events |
| [YouTube Project Setup in Google Developers Console](./YouTube-Project-Setup-Google-Console.md) | Setting up OAuth, API keys, and webhook subscriptions in Google Cloud Console |

---

## 7. Maintenance & Upgrades

| Document | Description |
| :--- | :--- |
| [Upgrade Guide: Postgres and Vault for Cisco Connector](./Upgrade-Guide-Postgres-Vault-Cisco.md) | Step-by-step upgrade procedure for Postgres and Vault dependencies in Cisco connector deployments |
