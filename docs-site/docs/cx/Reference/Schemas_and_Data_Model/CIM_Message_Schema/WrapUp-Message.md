---
title: "WrapUp Message"
summary: "CIM schema reference for the WrapUp message type — used by agents to attach admin-defined wrap-up categories and notes to conversations at the end of interactions."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["wrapup message CIM", "CIM wrapup schema", "wrap-up message CX", "CIM message WRAPUP", "wrap up category CIM", "conversation tagging CX", "agent wrapup API CX"]
aliases: ["wrapup message CIM", "CIM WRAPUP type", "conversation wrap-up schema CX"]
last-updated: 2026-03-10
---

# WrapUp Message

The WrapUp message is used when an agent wants to tag all or part of a conversation by attaching admin-defined categories to it, optionally with a free-text note.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"WRAPUP"` |
| `wrapups` | Array | Yes | One or more wrap-up category entries (see below). |
| `markdownText` | String | No | Optional plain text sent by the agent. |
| `note` | String | No | Additional free-text details added by the agent. |

### Wrapup Object

| Property | Type | Required | Description |
|---|---|---|---|
| `categoryName` | String | Yes | The wrap-up category name as selected by the agent (must match an admin-defined category). |
| `value` | String | Yes | The value entered by the agent for this category. |

## Example

```json
{
  "markdownText": " ",
  "type": "WRAPUP",
  "wrapups": [
    {
      "categoryName": "Issue Type",
      "value": "internet disconnectivity"
    },
    {
      "categoryName": "Resolution",
      "value": "plan upgradation"
    }
  ],
  "note": "Customer requested follow-up call in 2 days."
}
```

## Notes

- Multiple `wrapups` entries can be included to apply several categories simultaneously.
- `categoryName` values must match categories configured by the administrator in the Wrap-up Forms settings.

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Configuring Wrap-up Forms](../../../How-to_Guides/Administrator/Configuring-Wrap-up-Forms.md)
- [Message Body](Message-Body.md)
