---
title: "Unified Admin: Core Platform Configuration"
summary: "Foundational guide for Solution Admins to provision the system, manage teams, and configure routing logic."
audience: [administrator]
product-area: [platform, routing]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Unified Admin: Core Platform Configuration

As a Solution Admin (Olivia), your primary workspace is the **Unified Admin** console. This guide walks you through the foundational setup required to get your contact center operational.

## 1. Initial System Provisioning
Follow these steps in sequence to configure the core interaction engine.

### Step 1: Media Routing Domains (MRD)
Define the types of interactions your system will handle (e.g., Voice, Chat, SMS).
1. Go to **Routing Engine > MRDs**.
2. Set the **Max Tasks Request** per agent for each domain. 
3. **Pro-tip:** Set Voice to 1 and Chat to 3-5 based on agent proficiency.

### Step 2: Routing Attributes (Skills)
Attributes are the "Skills" assigned to agents (e.g., "English", "Sales").
1. Go to **Routing Engine > Routing Attributes**.
2. Create attributes as either **Proficiency** (1-10) or **Boolean** (True/False).

### Step 3: Precision Queues
Queues use logical expressions to find the right agent for a request.
1. Go to **Routing Engine > Queues**.
2. **Add Steps:** Define the logic (e.g., "Step 1: Find Agent with English > 8. If none found after 30s, go to Step 2").
3. **SLA Thresholds:** Set the target answer time for each queue to enable accurate reporting.

## 2. Managing Teams & Users
ExpertFlow uses **Keycloak** for user identity and **Unified Admin** for operational grouping.

### Creating a Team:
1. Click the **Teams** tab.
2. Select **New Team** and assign a **Primary Supervisor (Sam)**.
3. Add **Agents (Amy)** to the team. 
4. **Note:** Changes made here reflect in the real-time dashboards immediately after the next agent login.

## 3. Channel & Widget Management
Once the routing is ready, you must connect your communication channels.

### Web Widget Setup:
1. Go to **Web Widget** and create a new instance.
2. Configure **Pre-chat Forms** to collect customer data before the chat begins.
3. **Localization:** Select the languages your widget should support.

### Digital Channels:
- **WhatsApp/Facebook:** Configure your **Channel Providers** and **Connectors** to link your business accounts to the routing engine.
- *For detailed channel setup, see [Digital Channels](../../Capabilities/Digital_Channels/index.md).*

## 4. Operational Settings
- **Reason Codes:** Add custom codes for "Not Ready" (e.g., Training, System Issue) and "Logout."
- **Agent Desk Settings:** Enable or disable features like Emoji support, File Sharing, and Message Formatting.

---

*Looking for specialized guides? Check out [Managing Campaigns](../../How-to_Guides/Administrator/Managing-Outbound-Campaigns.md) or [Managing the QA Workflow](../For_Supervisors_and_QA_Leads/Managing-the-Quality-Assurance-Workflow.md).*
