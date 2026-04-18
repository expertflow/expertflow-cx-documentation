---
title: "Delivery Notification Message"
summary: "CIM schema reference for the Delivery Notification message type — used to indicate the delivery, read, connection, or failure status of a message sent within ExpertFlow CX."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["delivery notification CIM", "CIM delivery schema", "message delivery status CX", "DELIVERYNOTIFICATION type CIM", "message read receipt CIM", "message failed status CX", "delivery status CIM"]
aliases: ["delivery notification message CIM", "CIM DELIVERYNOTIFICATION type", "message status CX"]
last-updated: 2026-03-10
---

# Delivery Notification Message

The Delivery Notification message indicates the delivery or read status of a message that was previously sent in a conversation. It is used to confirm that a message reached the recipient, was read, or failed to deliver.

## Delivery States

| State | Description |
|---|---|
| `DELIVERED` | Message was delivered to the recipient (agent or customer). |
| `CONNECTED` | Used for voice calls — the call has been connected to a recipient. |
| `READ` | Message was read by the recipient. |
| `FAILED` | Message delivery failed. See reason codes below. |

## Reason Codes

| Code | State | Description |
|---|---|---|
| `200` | DELIVERED or READ | Successful delivery or read confirmation. |
| `400` | FAILED | Bad request — malformed message payload. |
| `404` | FAILED | Channel is undefined or unregistered in Unified Admin. |
| `500` | FAILED | Internal system error. |

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"DELIVERYNOTIFICATION"` |
| `messageId` | String | Yes | ID of the original message being acknowledged. |
| `markdownText` | String | No | Optional plain text. |
| `status` | Enum | Yes | One of: `Delivered`, `Connected`, `Read`, `Failed` |
| `reasonCode` | String | Yes | Numeric reason code indicating the outcome. |

## Example

```json
"body": {
  "type": "DELIVERYNOTIFICATION",
  "markdownText": "Optional",
  "messageId": "abc12345",
  "status": "READ",
  "reasonCode": 200
}
```

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Notification Message](Notification-Message.md)
- [Message Body](Message-Body.md)
