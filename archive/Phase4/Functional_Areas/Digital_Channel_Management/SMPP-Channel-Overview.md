---
title: "SMPP Channel Overview"
summary: "Explanation of the SMPP SMS channel integration in ExpertFlow CX — how customers can start SMS conversations with agents using any mobile messaging app via the SMPP protocol."
audience: [solution-admin, supervisor, decision-maker]
product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["SMPP", "SMS channel", "SMPP integration", "SMS to chat", "SMPP connector", "mobile SMS", "digital channels"]
aliases: ["SMPP channel", "SMS SMPP overview", "SMPP connector overview"]
last-updated: 2026-03-10
---

# SMPP Channel Overview

The **SMPP (Short Message Peer-to-Peer) channel** in ExpertFlow CX enables customers to start SMS-to-chat conversations with agents from any mobile SMS messaging application. When a customer sends an SMS to the business number, the message is received by the CX SMPP connector, routed as a chat request, and delivered to an available agent in the Agent Desk.

## How It Works

SMPP is a telecommunications protocol used by mobile carriers and SMS aggregators to exchange SMS messages. The ExpertFlow CX SMPP connector:
1. Connects to an SMPP gateway provided by a mobile carrier or SMS aggregator.
2. Listens for inbound SMS messages on a configured phone number.
3. Routes incoming SMS messages as chat requests through the standard CX queue and routing engine.
4. Delivers agent replies back to the customer as SMS via the SMPP gateway.

The agent experiences the conversation as a standard chat interaction — no special interface is required.

## Routing Modes

The SMPP channel supports both **PUSH** and **PULL** routing modes, configured per channel in Unified Admin.

## Key Characteristics

| Aspect | Detail |
|---|---|
| **Protocol** | SMPP (Short Message Peer-to-Peer) |
| **Encryption** | Configurable (`SMPP-SECURE` flag) |
| **Bind type** | TX (transmitter), RX (receiver), or TRX (transceiver) |
| **Number format** | Numeric or alphanumeric, configurable |
| **Delivery receipts** | Configurable via `PUBLISHER-ENABLE` flag |
| **Interaction type** | SMS-to-chat (agent desk handles it as chat) |
| **Outbound** | Agents reply to ongoing customer SMS sessions; bot can also handle the chat |

## Use Cases

- **Inbound SMS support**: Customers text a business number; agents respond in the Agent Desk.
- **SMS campaigns with reply handling**: After sending outbound SMS notifications, incoming replies are routed to agents.
- **Bot-assisted SMS**: A bot handles initial customer queries and escalates to an agent when needed.

## Configuration

SMPP requires connection parameters from your SMS gateway provider (IP, port, system ID, password, bind type). For full configuration steps, see [SMPP Configuration Guide](../../Solution_Admin/SMPP-Configuration-Guide.md).

## Related Articles

- [SMPP Configuration Guide](../../Solution_Admin/SMPP-Configuration-Guide.md)
- [Channel and Connector Setup](../../Solution_Admin/Channel-and-Connector-Setup.md)
- [Twilio SMS/MMS Configuration Guide](../../Solution_Admin/Twilio-SMS-MMS-Configuration-Guide.md)
