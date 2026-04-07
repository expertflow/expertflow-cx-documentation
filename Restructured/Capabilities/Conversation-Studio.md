---
title: "Conversation Studio"
summary: "Overview of the low-code authoring environment for building interaction flows in ExpertFlow CX."
audience: [decision-maker, conversation-designer]
product-area: [ivr, studio]
doc-type: explanation
difficulty: beginner
aliases: []
last-updated: 2026-03-30
---

# Conversation Studio

Conversation Studio is the low-code, event-driven authoring environment in ExpertFlow CX. It enables Conversation Designers to build and manage interaction flows for IVR, chatbots, and outbound campaigns using a visual, node-based interface — without writing code.

## Core Concepts

Logic in Conversation Studio is organized into **Flows** and **Nodes**.

- **Flows** — a collection of nodes defining a specific business process (e.g., "Main Inbound Greeting")
- **Nodes** — individual logic blocks that perform actions (e.g., Transfer to Queue, Send Message, Request API)
- **Events** — flows are triggered by platform events such as `Participant Role Changed` or `New Message Received`

Conversation Studio is powered by Node-RED and is accessible at `https://<FQDN>/conversation-studio`. Authoring requires the `conversation-studio-admin` role in Keycloak; read-only access is available for auditing.

---

*To start building flows, see the [Conversation Designer how-to guides](/docs/cx/How-to_Guides/Conversation_Designer).*
