---
title: "Quick Start for Administrators"
summary: "Foundational guide for Solution Admins to provision the system, manage teams, and configure routing logic."
audience: [administrator]
product-area: [platform, routing]
doc-type: tutorial
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Quick Start for Administrators

As a Solution Admin, your primary workspace is the **Unified Admin** console. This guide walks you through the foundational setup required to get your contact center operational — from routing configuration and user management through to channel onboarding and agent desk settings.

Work through the sections in order on a fresh deployment.

## 1. Configure Routing

Define how interactions are classified and matched to agents.

1. **Media Routing Domains (MRDs)** — define the interaction types your system handles (e.g., Voice, Chat, SMS). Set **Max Tasks Request** per agent per domain. Voice is typically 1; Chat is 3–5 depending on agent capacity.
2. **Routing Attributes** — create the skills assigned to agents (e.g., "English", "Sales") as either **Proficiency** (1–10) or **Boolean** (True/False).
3. **Precision Queues** — build the matching logic. Add steps with conditions (e.g., "Find agent with English > 8; if none after 30s, widen criteria") and set SLA thresholds per queue for accurate reporting.

→ [Media Routing Domains Overview](../../How-to_Guides/Administrator/Media-Routing-Domains-MRD-Overview.md)
→ [Routing Attributes and Precision Queues](../../How-to_Guides/Administrator/Routing-Attributes-and-Queues.md)
→ [Precision Routing](../../How-to_Guides/Administrator/Precision-Routing.md)

## 2. Create Teams and Users

ExpertFlow CX uses **Keycloak** for user identity and **Unified Admin** for operational grouping.

1. Go to the **Teams** tab and select **New Team**.
2. Assign a Primary Supervisor to the team.
3. Add agents to the team. Changes reflect in real-time dashboards after the agent's next login.

→ [User Management](../../How-to_Guides/Administrator/User-Management.md)

## 3. Connect Channels

Once routing is ready, connect your communication channels.

- **Web Widget** — create a new widget instance, configure pre-chat forms to collect customer data, and set supported languages.
- **Digital Channels** (WhatsApp, Facebook, etc.) — configure channel providers and connectors to link your business accounts to the routing engine.

→ [Channel and Connector Setup](../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
→ [Configuring the Customer Widget](../../How-to_Guides/Administrator/Configuring-the-Customer-Widget.md)

## 4. Configure Agent Desk Settings

Set the operational defaults agents will work with.

- **Reason Codes** — add custom Not Ready codes (e.g., Training, System Issue) and Logout codes for accurate state tracking.
- **Agent Desk Settings** — enable or disable features such as emoji support, file sharing, and message formatting.
- **Wrap-up Forms** — create and assign wrap-up forms to channels and queues.

→ [Configure AgentDesk Settings](../../How-to_Guides/Administrator/Configure-AgentDesk-Settings.md)
→ [Configuring Reason Codes](../../How-to_Guides/Administrator/Configuring-Reason-Codes.md)
→ [Configuring Wrap-up Forms](../../How-to_Guides/Administrator/Configuring-Wrap-up-Forms.md)

## What's next

With core configuration complete, explore the full administrative surface:

→ [Administrator How-to Guides](../../How-to_Guides/Administrator/index.md)
→ [Getting Started for Supervisors & QA Leads](../For_Supervisors_and_QA_Leads/index.md)
