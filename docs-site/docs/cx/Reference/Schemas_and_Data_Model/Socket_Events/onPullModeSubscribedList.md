---
title: "onPullModeSubscribedList"
summary: "Emitted by Agent Manager when an agent subscribes or unsubscribes from a pull-mode list, delivering the updated list details."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["onPullModeSubscribedList socket event CX", "onPullModeSubscribedList Agent Manager CX", "Socket.IO CX"]
aliases: ["onPullModeSubscribedList event ExpertFlow", "onPullModeSubscribedList socket CX"]
last-updated: 2026-03-12
---

# onPullModeSubscribedList

Triggered when the agent subscribes or unsubscribes from a list where certain customer-agent conversations are maintained.

| Property | Value |
|---|---|
| **Event Name** | `onPullModeSubscribedList` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `name` | String | Name of the list the agent has subscribed to. |
| `description` | String | Description of the list. |
| `id` | String | System-generated ID of the list. |

## Example Payload

```json
{
    "name": "L1",
    "description": null,
    "id": "6224aa24378c960030df479f"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [subscribePullModeList](./subscribePullModeList.md)
- [pullModeSubscribedListRequests](./pullModeSubscribedListRequests.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
