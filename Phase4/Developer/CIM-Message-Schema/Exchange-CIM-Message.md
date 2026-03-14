---
title: "Exchange CIM Message"
summary: "Explanation of CIM message exchange in ExpertFlow CX — how Agent Desk, Channel Connectors, and Bot Connectors send and receive CIMMessage objects via Socket.IO and REST API."
audience: [developer]
product-area: [sdk, channels]
doc-type: explanation
difficulty: intermediate
keywords: ["exchange CIM message CX", "send receive CIM message CX", "CIM message exchange CX", "Agent Desk message CX", "channel connector message exchange CX"]
aliases: ["CX CIM message exchange", "send CIM message CX"]
last-updated: 2026-03-10
---

# Exchange CIM Message

All messages exchanged to and from Agent Desk, Channel Connectors, and Bot Connectors use the `CIMMessage` format. A CIM message has three parts: a unique identifier (ID), a header, and a body.

---

## Message Structure

| Part | Description |
|---|---|
| **ID** | UUID that uniquely identifies the message |
| **Header** | Generic metadata — sender, channel session, timestamp. See [Message Header](Message-Header.md). |
| **Body** | Type-specific content. The body structure changes based on the message type. See [Message Body](Message-Body.md) and individual message type pages. |

---

## How Messages Are Exchanged

### Agent Desk ↔ Agent Manager (WebSocket)

Agent Desk applications communicate with Agent Manager via Socket.IO:

- **Agent Desk → Agent Manager**: Use the `publishCimEvent` socket event to send messages.
- **Agent Manager → Agent Desk**: Use the `onCimEvent` socket event to receive messages.

See [Socket Events](../Socket_Events/index.md) for the full event list.

### Channel Connector ↔ CCM (REST API)

Channel connectors communicate with the Customer Channel Manager (CCM) via REST:

- **Connector → CCM**: `POST /cim-messages` with a `CIMMessage` payload.
- **CCM → Connector**: CCM POSTs CIM-formatted messages to the connector's registered **Provider Webhook**.

See [Channel Connector Developer Guide](../../Integrator/Channel-Connector-Developer-Guide.md).

### Bot Connector ↔ CCM (REST API)

Bot connectors also use REST:

- **Bot → CCM**: `POST /cim-messages` with a `CIMMessage` payload.
- **CCM → Bot**: CCM POSTs messages to the bot's webhook.

---

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Message Header](Message-Header.md)
- [Message Body](Message-Body.md)
- [Socket Events](../Socket_Events/index.md)
- [publishCimEvent](../Socket_Events/publishCimEvent.md)
- [onCimEvent](../Socket_Events/onCimEvent.md)
- [Channel Connector Developer Guide](../../Integrator/Channel-Connector-Developer-Guide.md)
