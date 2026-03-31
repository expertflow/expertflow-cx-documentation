---
title: "Button Message"
summary: "CIM schema reference for the Button message type — used by agents and bots to present customers with pre-defined options as single buttons or a list of buttons."
audience: [developer]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["button message CIM", "CIM button schema", "quick reply CX", "button message bot CX", "outbound button message CX", "CIM message type button", "bot button options CX"]
aliases: ["button message schema CX", "quick reply message CX", "CIM BUTTON type"]
last-updated: 2026-03-10
---

# Button Message

The Button message is an **outbound message** type used by agents and conversational bots to present pre-defined options to customers. It supports single buttons and lists of buttons (quick replies).

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"BUTTON"` |
| `markdownText` | String | No | Custom plain text sent alongside the buttons. |
| `buttonMessageType` | String | Yes | `"Quick_Replies"` or `"Button"` |
| `buttons` | List | Yes | One or more button objects (see below). |
| `additionalDetails` | Object | No | Additional rendering data — header, body, footer, etc. Includes `defaultIntent` from RASA for out-of-range selections. |

### Button Object Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `title` | String | Yes | Label displayed on the button. |
| `type` | String | Yes | Type of the button (user-defined). |
| `payload` | String | Yes | Value passed when the customer clicks the button. |
| `additionalButtonDetails` | Object | No | Section grouping details (`sectionNo`, `sectionTitle`, `description`). |

### Text Alignment

Set `"textAlignment"` to `"left"`, `"center"`, or `"right"` in `additionalDetails` to control button label alignment.

## Example

```json
"body": {
  "type": "BUTTON",
  "markdownText": "Hi",
  "buttonMessageType": "BUTTON",
  "additionalDetails": {
    "interactive": {
      "type": "list",
      "button": "Main Menu",
      "header": {
        "type": "text",
        "text": "Select an option"
      },
      "body": {
        "text": "How can we help you?"
      },
      "footer": {
        "text": "Reply with a number"
      }
    }
  },
  "buttons": [
    {
      "type": "String",
      "title": "Technical Support",
      "payload": "tech-support-guid",
      "additionalButtonDetails": {
        "sectionNo": 1,
        "sectionTitle": "Support",
        "description": "For device and connectivity issues"
      }
    },
    {
      "type": "String",
      "title": "Billing Inquiry",
      "payload": "billing-guid",
      "additionalButtonDetails": {
        "sectionNo": 2,
        "sectionTitle": "Billing",
        "description": "For invoice and payment questions"
      }
    }
  ]
}
```

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Plain Text Message](Plain-Text-Message.md)
- [Carousel Message](Carousel-Message.md)
- [Message Body](Message-Body.md)
