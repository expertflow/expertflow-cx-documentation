---
title: "SMS Channel Overview"
summary: "Overview of the SMS channel in ExpertFlow CX — how customers can start SMS conversations with agents from any mobile phone."
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["SMS channel", "SMS support", "text messaging", "mobile SMS", "digital channels"]
aliases: ["SMS channel overview", "text messaging channel"]
last-updated: 2026-03-10
---

# SMS Channel Overview

The SMS channel in ExpertFlow CX lets customers start a conversation with an agent by sending a text message to the business number from any mobile phone. Incoming messages are routed as chat requests and delivered to an available agent in the Agent Desk. The agent replies from the same interface used for all other chat channels.

## How It Works

1. A customer sends an SMS to the business number.
2. The CX platform receives the message and routes it through the standard queue and routing engine.
3. An available agent receives the conversation in the Agent Desk and replies.
4. The customer receives the agent's reply as an SMS on their phone.

The agent experience is identical to any other chat channel — no special interface is required.

## Routing Modes

The SMS channel supports both **Push** and **Pull** routing modes, configured per channel in Unified Admin.

## Use Cases

- **Inbound SMS support**: Customers text a business number; agents respond in the Agent Desk.
- **SMS campaigns with reply handling**: After sending outbound SMS notifications, incoming replies are routed to agents.
- **Bot-assisted SMS**: A bot handles initial customer queries and escalates to an agent when needed.

## Configuration

SMS channel setup requires connection details from your SMS gateway provider. For full configuration steps, see the [SMPP Configuration Guide](../../../How-to_Guides/Administrator/SMPP-Configuration-Guide.md) in the Administrator guides.

## Related Articles

- [Post-Call SMS Survey](./Post-Call-SMS-Survey.md)
- [SMPP Configuration Guide](../../../How-to_Guides/Administrator/SMPP-Configuration-Guide.md)
- [Twilio SMS/MMS Configuration Guide](../../../How-to_Guides/Administrator/Twilio-SMS-MMS-Configuration-Guide.md)
- [Channel and Connector Setup](../../../How-to_Guides/Administrator/Channel-and-Connector-Setup.md)
