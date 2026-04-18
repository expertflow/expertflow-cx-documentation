---
title: "onChannelTypes"
summary: "Emitted by Agent Manager once a socket connection is established, delivering the list of available channel types to the Agent Desk."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["onChannelTypes socket event CX", "onChannelTypes Agent Manager CX", "Socket.IO CX"]
aliases: ["onChannelTypes event ExpertFlow", "onChannelTypes socket CX"]
last-updated: 2026-03-12
---

# onChannelTypes

Event is triggered once a connection is established through a channel, delivering the list of configured channel types to the Agent Desk.

| Property | Value |
|---|---|
| **Event Name** | `onChannelTypes` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `id` | String | System-generated channel ID. |
| `name` | String | Name of the channel type (e.g., `FACEBOOK`, `WEB`, `WHATSAPP`). |
| `channelLogo` | Image Object | Logo associated with the channel type. |
| `isInteractive` | Boolean | `true` for chat-based interactive channels. |
| `mediaRoutingDomain` | MRD Object | The Media Routing Domain associated with this channel type. |

## Example Payload

```json
[
  {
    "id": "622222cb5bd05f57c1c1841d",
    "name": "FACEBOOK",
    "channelLogo": "_FACEBOOK.svg",
    "isInteractive": false,
    "mediaRoutingDomain": null
  },
  {
    "id": "622222cc5bd05f57c1c1841e",
    "name": "VIBER",
    "channelLogo": "_VIBER.svg",
    "isInteractive": false,
    "mediaRoutingDomain": null
  },
  {
    "id": "622222cc5bd05f57c1c1841f",
    "name": "WHATSAPP",
    "channelLogo": "_WHATSAPP.svg",
    "isInteractive": true,
    "mediaRoutingDomain": "62302def6b1fba2525db2713"
  },
  {
    "id": "622222cc5bd05f57c1c18420",
    "name": "SMS",
    "channelLogo": "_SMS.svg",
    "isInteractive": false,
    "mediaRoutingDomain": null
  },
  {
    "id": "622222cc5bd05f57c1c18421",
    "name": "WEB",
    "channelLogo": "_WEB.svg",
    "isInteractive": true,
    "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
  },
  {
    "id": "622222cc5bd05f57c1c18422",
    "name": "GENERIC",
    "channelLogo": "_GENERIC.svg",
    "isInteractive": false,
    "mediaRoutingDomain": null
  },
  {
    "id": "6233de0e3ef6175890847d4c",
    "name": "web",
    "channelLogo": "32917_web-1873373_1280.png",
    "isInteractive": true,
    "mediaRoutingDomain": "6233dde8c004592808ad3c0d"
  }
]
```

## Related Articles

- [Socket Events Overview](./index.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
