---
title: "removePullModeSubscribedListRequests"
summary: "Emitted by Agent Manager when an agent unsubscribes from a pull-mode list, providing the ID of the removed list."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["removePullModeSubscribedListRequests socket event CX", "removePullModeSubscribedListRequests Agent Manager CX", "Socket.IO CX"]
aliases: ["removePullModeSubscribedListRequests event ExpertFlow", "removePullModeSubscribedListRequests socket CX"]
last-updated: 2026-03-12
---

# removePullModeSubscribedListRequests

Event is triggered when an agent unsubscribes from a list. Returns the ID of the unsubscribed pull-mode list.

| Property | Value |
|---|---|
| **Event Name** | `removePullModeSubscribedListRequests` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `id` | String | ID of the unsubscribed pull-mode list. Example: `"622769a8ca110c0030fe0f31"`. |

## Example Payload

```json
"622769a8ca110c0030fe0f31"
```

## Related Articles

- [Socket Events Overview](./index.md)
- [addPullModeSubscribedListRequests](./addPullModeSubscribedListRequests.md)
- [unsubscribePullModeList](./unsubscribePullModeList.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
