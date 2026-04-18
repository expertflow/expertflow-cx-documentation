---
title: "URL Message"
summary: "CIM schema reference for the URL message type — used by agents and bots to send a URL link to the customer, such as for app installation or system updates."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["URL message CIM", "CIM URL schema", "send URL message CX", "link message CX", "CIM message type URL", "bot send link CX", "outbound URL message CX"]
aliases: ["url message CX", "link message CIM", "CIM URL type"]
last-updated: 2026-03-10
---

# URL Message

The URL message is an **outbound message** type used by agents and bots to send a URL to the customer — for example, a link to install an app, access a document, or initiate a system update.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"URL"` |
| `markdownText` | String | No | Optional plain text message to accompany the URL. Routed from CCM to the channel connector webhook. |
| `mediaURL` | String | Yes | The URL to be sent to the customer. |

## Example

```json
"body": {
  "type": "URL",
  "markdownText": "You can download our Android app from this link.",
  "mediaUrl": "https://play.google.com/store/apps/details?id=com.example.app"
}
```

## Notes

- The `mediaURL` field is the primary required content. The `markdownText` is optional context displayed alongside the link.
- Channel-side rendering of the URL (as a hyperlink, preview card, etc.) depends on the receiving channel's capabilities.

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Plain Text Message](Plain-Text-Message.md)
- [Button Message](Button-Message.md)
- [Message Body](Message-Body.md)
