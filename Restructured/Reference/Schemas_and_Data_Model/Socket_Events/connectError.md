---
title: "connect_error"
summary: "Emitted by Agent Manager to notify the agent whenever any error occurs during the handshake of socket connection establishment."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["connect_error socket event CX", "connect_error Agent Manager CX", "Socket.IO CX"]
aliases: ["connect_error event ExpertFlow", "connect_error socket CX"]
last-updated: 2026-03-12
---

# connect_error

Event is triggered to notify the agent whenever any error occurs during the handshake of socket connection establishment (e.g., unauthorized user, invalid data).

| Property | Value |
|---|---|
| **Event Name** | `connect_error` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

This event carries no structured payload properties. The error object is passed directly as the event data, containing the error message from the Socket.IO handshake failure.

## Related Articles

- [Socket Events Overview](./index.md)
- [errors](./errors.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
