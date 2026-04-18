---
title: "CIM Message Schema Master"
summary: "Technical reference for the Customer Interaction Model (CIM), the universal data format for all ExpertFlow CX interactions."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# CIM Message Schema Master

The **Customer Interaction Model (CIM)** is the standardized JSON format used for all communication within the ExpertFlow CX ecosystem. Every actor—including Agents, Bots, and 3rd-party Connectors—must adhere to this schema when exchanging messages.

## 1. Interaction Protocols
CIM messages are exchanged via two primary protocols depending on the actor's role:
- **REST API:** Used by **Channel Connectors** and **Bot Connectors** for stateless request/response transmission.
- **WebSocket (Socket.io):** Used by the **Agent Desk** for real-time, bidirectional event streaming.

## 2. Global Object Structure
Every CIM message consists of three mandatory top-level components:

| Component | Description | Requirement |
| :--- | :--- | :--- |
| **ID** | A universally unique identifier (UUID) for the specific message. | Required |
| **Header** | Metadata including sender info, timestamps, and conversation IDs. | Required |
| **Body** | The actual content payload (Text, Media, Action, etc.). | Required |

### Common Base Schema:
```json
{
  "id": "uuid-v4-string",
  "header": { ... },
  "body": { ... }
}
```

## 3. Core Schema Definitions
Navigate to the specialized references below for granular property definitions:
- **[Message Header](Message-Header.md):** Defines sender identity, channel data, and intent logic.
- **[Message Body](Message-Body.md):** Defines the various content types (Plain, Media, Carousel, Location).
- **[Message Exchange Handshake](Message-Exchange-Handshake.md):** Explains how messages are acknowledged and sequenced.

---

*Looking for real-time events? See the [AgentManager SDK Reference](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md).*
