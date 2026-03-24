---
title: "Add Bot Connector"
summary: "How-to guide for adding a bot connector in ExpertFlow CX Unified Admin — covering bot type selection (Rasa or Custom), required fields, API URL configuration, and deletion restrictions."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["add bot connector CX", "bot connector CX", "Rasa bot CX", "custom bot CX", "bot unified admin CX", "configure bot CX", "bot API URL CX", "CX bot setup"]
aliases: ["bot connector setup CX", "configure bot connector CX", "add bot CX"]
last-updated: 2026-03-10
---

# Add Bot Connector

Before creating channels in ExpertFlow CX, you must have at least one bot configured in the system. The bot handles self-service customer requests before routing to a human agent.

> Ensure your bot is trained with the required data (or using the default bot training) before adding it as a connector. Untrained bots will not handle customer requests correctly.

## Prerequisites

- Bot software (Rasa or custom connector) deployed and accessible via HTTP.
- Access to Unified Admin.

## Steps

1. Navigate to **Unified Admin → Bot Connectors**.
2. Expand the **Rasa** type (or the relevant bot type).
3. Click **Add Bot**.
4. Fill in the required fields:

   | Field | Description |
   |---|---|
   | **Bot Name** | A name to identify this bot in Unified Admin. |
   | **API URL** | The URL where the bot connector is running. Only applicable for **Rasa** or **Custom** bot types. Example: `http://server-ip:30800` |

5. Click **Save**.

## Notes

- A bot connector that is associated with a Channel or another component **cannot be deleted** until the association is removed.
- The **API URL** field appears only when the Bot Type is **Rasa** or **Custom**.

## Related Articles

- [Custom Bot Connector Development](Custom-Bot-Connector-Development.md)
- [Channel and Connector Setup](../Administrator/Channel-and-Connector-Setup.md)
- [NLU Digital Bots Concepts](../Conversation_Designer/NLU-Digital-Bots-Concepts.md)
- [Registering Bot Connectors](../Conversation_Designer/Registering-Bot-Connectors.md)
