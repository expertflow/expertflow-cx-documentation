---
title: "Voice Message Schema"
summary: "Reference for the CIM Voice message type schema, defining the JSON body properties required to send voice/audio messages through the Customer Interaction Management (CIM) platform."

product-area: [voice]
doc-type: reference
difficulty: intermediate
keywords: ["voice message schema", "CIM message schema", "voice CIM", "audio message", "callId", "leg", "message type", "CIM JSON"]
aliases: ["voice CIM message", "audio message schema", "CIM voice body"]
last-updated: 2026-03-10
---

# Voice Message Schema

The **Voice** message type in the CIM (Customer Interaction Management) platform enables sending audio messages between participants in a conversation. The message body must be formatted as JSON and include the properties defined below.

## Message Properties

| Property | Type | Required | Description |
|---|---|---|---|
| `type` | String | Yes | Must be set to `"VOICE"` |
| `callId` | String | Yes | Unique identifier of the call associated with this message |
| `leg` | String | Yes | Identifies which leg of the call this message belongs to (e.g., agent leg, customer leg) |
| `reasonCode` | String | No | Optional code indicating the reason for this voice message event |
| `additionalDetail` | Object `{String}` | No | Optional key-value pairs providing supplementary detail about the voice message |

## Example Request Body

```json
{
  "type": "VOICE",
  "callId": "550e8400-e29b-41d4-a716-446655440000",
  "leg": "agent",
  "reasonCode": "NORMAL_CLEARING",
  "additionalDetail": {
    "duration": "120",
    "direction": "INBOUND"
  }
}
```

## Usage Notes

- `type` must be the literal string `"VOICE"` (uppercase). Any other value will be rejected.
- `callId` must match the UUID of an existing active or recently completed call in the platform.
- `leg` identifies the originator of the message — typically `"agent"` or `"customer"`. The exact permitted values depend on your platform configuration.
- `reasonCode` is used to pass call-end reason information (e.g., `NORMAL_CLEARING`, `USER_BUSY`) that aligns with the EFSwitch hangup cause codes. See [Miscellaneous Dialer Call Results](Miscellaneous-Dialer-Call-Results.md) for a complete list of EFSwitch hangup cause codes.

## Related Articles

- [Miscellaneous Dialer Call Results](Miscellaneous-Dialer-Call-Results.md)
- [CX Dialer Reference](CX-Dialer-Reference.md)
- [Action Message Bot Communication](../../How-to_Guides/Developer_Integrator/Action-Message-Bot-Communication.md)
- [Conversation Life Cycle Objects](../../How-to_Guides/Developer_Integrator/Conversation-Life-Cycle-Objects.md)
- [CIM Message Schema](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/)
