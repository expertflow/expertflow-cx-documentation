---
title: "Location Message"
summary: "CIM schema reference for the Location message type — used to send GPS coordinates and optional address details to a conversation participant."
audience: [developer]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["location message CIM", "CIM location schema", "GPS message CX", "send location CX", "CIM message type location", "latitude longitude message CX"]
aliases: ["location message CX", "CIM LOCATION type", "GPS CIM message"]
last-updated: 2026-03-10
---

# Location Message

The Location message is used to send GPS coordinates (latitude/longitude) to a conversation participant. It supports optional address metadata such as place name, street address, and a URL.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"LOCATION"` |
| `location` | Object | Yes | Latitude and longitude coordinates (see below). |
| `markdownText` | String | No | Optional plain text to accompany the location. |
| `additionalDetails` | Object | No | Additional place details — name, address, URL. |

### Location Object

| Property | Type | Required | Description |
|---|---|---|---|
| `latitude` | Number | Yes | GPS latitude (e.g., `31.51335334777832`). |
| `longitude` | Number | Yes | GPS longitude (e.g., `74.3333969116211`). |

### Additional Details

| Property | Type | Description |
|---|---|---|
| `name` | String | Place name (e.g., `"Gaddafi Stadium"`). |
| `address` | String | Street address (e.g., `"Hafeez Kardar Road"`). |
| `url` | String | URL associated with the location (optional). |

## Example

```json
"body": {
  "type": "LOCATION",
  "location": {
    "latitude": 31.51335334777832,
    "longitude": 74.3333969116211
  },
  "markdownText": null,
  "additionalDetails": {
    "name": "Gaddafi Stadium",
    "address": "Hafeez Kardar Road",
    "url": null
  }
}
```

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Plain Text Message](Plain-Text-Message.md)
- [Message Body](Message-Body.md)
