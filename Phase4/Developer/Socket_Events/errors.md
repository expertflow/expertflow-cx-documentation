---
title: "errors"
summary: "Emitted by Agent Manager to notify the agent whenever any error occurs in the system or on any request."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["errors socket event CX", "errors Agent Manager CX", "Socket.IO CX"]
aliases: ["errors event ExpertFlow", "errors socket CX"]
last-updated: 2026-03-12
---

# errors

Event is triggered to notify the agent whenever any error occurs in the system or on any request.

| Property | Value |
|---|---|
| **Event Name** | `errors` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

This event carries a generic error object. No fixed payload structure is defined — the error content varies depending on the system or request that triggered the error.

## Related Articles

- [Socket Events Overview](./index.md)
- [connect_error](./connectError.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
