---
title: "Contact Message"
summary: "CIM schema reference for the Contact message type — used to send contact card details including name, phone, email, address, organization, and other personal information."
audience: [developer]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["contact message CIM", "CIM contact schema", "contact card message CX", "CONTACT type CIM", "send contact details CX", "vCard CIM message", "contact sharing CX"]
aliases: ["contact message CIM", "CIM CONTACT type", "contact card CX"]
last-updated: 2026-03-10
---

# Contact Message

The Contact message is used to send contact card details to the recipient — including name, phone, email, address, and organizational information.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"CONTACT"` |
| `markdownText` | String | No | Optional plain text to accompany the contact card. |
| `additionalDetails` | Object | No | Additional metadata for the message. |
| `contacts` | Array | Yes | One or more contact objects (see below). |

### Contact Object

#### Name

| Property | Type | Required | Description |
|---|---|---|---|
| `formattedName` | String | Yes | Full display name. |
| `additionalNameDetails` | Object | No | `first_name`, `last_name`, `middle_name`, `name_suffix`, `name_prefix` |

#### Phone

| Property | Type | Required | Description |
|---|---|---|---|
| `phone` | String | Yes | Phone number (e.g., `"+923001234567"`). |
| `additionalPhoneDetails` | Object | No | `type` (e.g., `"CELL"`) and `wa_id` (WhatsApp ID). |

#### Additional Contact Details (Optional)

| Field | Description |
|---|---|
| `addresses` | `street`, `city`, `state`, `zip`, `country`, `country_code`, `type` |
| `emails` | `email`, `type` |
| `org` | `company`, `department`, `title` |
| `urls` | `url`, `type` |
| `ims` | `service`, `userId` |
| `birthday` | Format: `"YYYY-MM-DD"` |

## Example

```json
"body": {
  "type": "CONTACT",
  "markdownText": null,
  "additionalDetails": null,
  "contacts": [
    {
      "name": {
        "formattedName": "Jane Smith",
        "additionalNameDetails": {
          "first_name": "Jane",
          "last_name": "Smith"
        }
      },
      "phones": [
        {
          "phone": "+923001234567",
          "additionalPhoneDetails": {
            "type": "CELL",
            "wa_id": null
          }
        }
      ],
      "additionalContactDetails": {
        "emails": [
          {
            "email": "jane@example.com",
            "type": "INTERNET"
          }
        ],
        "org": {
          "company": "Acme Corp",
          "department": "Engineering",
          "title": "Senior Developer"
        }
      }
    }
  ]
}
```

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Plain Text Message](Plain-Text-Message.md)
- [Message Body](Message-Body.md)
