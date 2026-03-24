---
title: "Custom Bot Connector Development"
summary: "Guide for bot developers to build and register custom connectors to interface between AI engines and the ExpertFlow CX platform."
audience: [developer-integrator]
product-area: [bots, sdk]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Custom Bot Connector Development

While ExpertFlow CX provides native support for Rasa and Amazon Lex, you can integrate any 3rd-party AI engine by developing a custom bot connector. This connector acts as a translation layer between your bot and the ExpertFlow Bot Framework.

## 1. Technical Architecture
The Custom Connector sits between the Bot Framework and your AI engine.
- **Protocol:** Synchronous or Asynchronous REST APIs.
- **Responsibility:** The connector must translate ExpertFlow **CIM Messages** into the schema understood by your bot, and vice versa.

## 2. Requirements for the Connector
Your custom bot must expose a **Webhook** that the ExpertFlow platform can call.
- **Input:** Receives user messages, intents, and system activities from the Bot Framework.
- **Output:** Returns bot responses, suggested actions, or handover requests.

### Translation Logic:
You may need to develop a **Bot Framework Adapter** if your bot's message format is significantly different from the platform's standard. This adapter should handle:
1.  **Messages:** Text, Media, and Structured content.
2.  **Intents:** Detected customer goals.
3.  **Actions:** Commands like `FIND_AGENT` or `CLOSE_CONVERSATION`.

## 3. Registration Process
Once your connector is developed and hosted:
1.  Go to **Unified Admin > Bot Settings**.
2.  Add a new connector of type **Custom**.
3.  Provide the **Webhook URL** where your connector is listening.

---

*For detailed message schema definitions, see the [CIM Message Schema Master](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md).*
