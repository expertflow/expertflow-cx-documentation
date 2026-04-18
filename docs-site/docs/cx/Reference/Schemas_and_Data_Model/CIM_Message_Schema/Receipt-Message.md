---
title: "Receipt Message"
summary: "CIM schema reference for the Receipt message type — used to contain message delivery receipt information within the ExpertFlow CX messaging framework."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["receipt message CIM", "CIM receipt schema", "delivery receipt CX", "RECEIPT type CIM", "message receipt CX"]
aliases: ["receipt message CIM", "CIM RECEIPT type"]
last-updated: 2026-03-10
---

# Receipt Message

The Receipt message is used to contain message delivery receipt information within the ExpertFlow CX CIM framework.

## Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be `"RECEIPT"` |

> For delivery status details (DELIVERED, READ, FAILED, etc.), see [Delivery Notification Message](Delivery-Notification-Message.md) which provides the full status and reason code schema.

## Related Articles

- [CIM Messages](CIM-Messages.md)
- [Delivery Notification Message](Delivery-Notification-Message.md)
- [Message Body](Message-Body.md)
