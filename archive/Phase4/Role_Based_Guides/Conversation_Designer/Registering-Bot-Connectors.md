---
title: "Registering Bot Connectors"
summary: "Guide for Conversation Designers to link external AI bots (Rasa, Lex, Custom) to the ExpertFlow CX platform."
audience: [designer, admin]
product-area: [bots, studio, platform]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Registering Bot Connectors

Before you can build automated flows, you must link your AI engine to the ExpertFlow CX platform. Every communication channel requires an associated **Bot Connector** to handle self-service logic and timeouts.

## 1. Prerequisites
- **Trained Bot:** Ensure your bot (e.g., Rasa) is trained and running on a reachable network address.
- **Unified Admin Access:** You must have the appropriate administrative permissions to modify Bot Settings.

## 2. Adding a Connector
1.  Open **Unified Admin** and go to **Bot Settings**.
2.  **Select Type:** Choose from **Rasa**, **Amazon Lex**, or **Custom**.
3.  **Bot Name:** Provide a descriptive name (e.g., `Sales-Support-Bot`).
4.  **API URL:** Enter the endpoint where the bot connector is running (e.g., `http://10.0.0.50:30800`).

## 3. Association Rules
- **Channel Linking:** Once a bot is registered, you can assign it to a digital channel (WhatsApp, Web) in the Channel Management module.
- **Deletion Lock:** The system will not allow you to delete a bot connector if it is currently linked to an active channel. You must remove all associations before deleting the connector.

---

*Once your bot is registered, you can design its handover logic in [AI Sentiment-Based Handover](AI-Sentiment-Based-Handover.md).*
