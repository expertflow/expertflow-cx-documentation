---
title: "taskRequest"
summary: "Emitted by Agent Manager to notify an agent of a new conversation request that has been routed to them."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["taskRequest socket event CX", "taskRequest Agent Manager CX", "Socket.IO CX"]
aliases: ["taskRequest event ExpertFlow", "taskRequest socket CX"]
last-updated: 2026-03-12
---

# taskRequest

Event is triggered on a new conversation request. The Agent Manager emits this event to notify the assigned agent of the incoming task.

| Property | Value |
|---|---|
| **Event Name** | `taskRequest` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `channelSession` | Object | Contains values of properties related to the session established through a particular channel (e.g., web). |
| `ccUser` | Object | Contains agent information (CCUser properties). |
| `taskId` | String | ID of the task (chat or call request). |
| `taskState` | Object | Current state of the task. Includes `name` (current state name). |
| `conversationId` | String | ID of the conversation. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (room mode). |
| `taskDirection` | String | Direction of the task: `INBOUND` or `OUTBOUND`. |
| `queue` | Object | Contains `id` (queue ID) and `name` (queue name). |
| `note` | String | Optional note associated with the task. |
| `requestedBy` | String | Identifier of who requested the task (if applicable). |

## Example Payload

```json
{
  "conversationId": "67c1cb75956d765cfc275754",
  "channelSession": {
    "participantType": "ChannelSession",
    "id": "67c1cb74d9244213fbf316d5",
    "channel": {
      "id": "673f128f7f433c0c29f3e997",
      "name": "chat-khurram",
      "serviceIdentifier": "0900",
      "defaultOutbound": false,
      "tenant": {
        "id": "6790b05cf718dd632e317c9e",
        "name": null
      },
      "channelConfig": {
        "id": "6790b05cf718dd632e317c9f",
        "channelMode": "HYBRID",
        "conversationBot": "",
        "responseSla": 0,
        "customerActivityTimeout": 600,
        "customerSla": {
          "totalDuration": null,
          "action": null,
          "startTime": null
        },
        "customerIdentificationCriteria": {
          "value": null
        },
        "routingPolicy": {
          "agentSelectionPolicy": "LONGEST_AVAILABLE",
          "routeToLastAgent": false,
          "routingMode": "PUSH",
          "routingObjectId": "673f125576e125429ea2f2b7",
          "agentRequestTtl": 800
        },
        "botId": "6712cf4bfb156449bb04ce99"
      },
      "channelConnector": {
        "id": "6712cb370b72db03b37236b9",
        "name": "web",
        "channelProviderInterface": {
          "id": "6712cb300b72db03b37236b7",
          "name": "web",
          "supportedChannelTypes": [
            {
              "id": "671270060b72db03b37236ad",
              "name": "WEB",
              "channelLogo": "_WEB.svg",
              "isInteractive": true,
              "mediaRoutingDomain": "6305de07166ba1099d11d8e6"
            }
          ],
          "providerWebhook": "http://ef-web-channel-manager-svc:7000",
          "channelProviderConfigSchema": []
        },
        "channelProviderConfigs": [],
        "tenant": {
          "id": "67aa110f0bda607923ca9bfa",
          "name": null
        }
      },
      "channelType": {
        "id": "671270060b72db03b37236ad",
        "name": "WEB",
        "channelLogo": "_WEB.svg",
        "isInteractive": true,
        "mediaRoutingDomain": "6305de07166ba1099d11d8e6"
      }
    },
    "customer": {
      "_id": "67c1cb75d66fbd82f98990ad",
      "firstName": "test",
      "phoneNumber": [],
      "isAnonymous": true,
      "__v": 0,
      "web": [
        "0991223"
      ]
    },
    "customerSuggestions": [],
    "channelData": {
      "channelCustomerIdentifier": "0991223",
      "serviceIdentifier": "0900",
      "requestPriority": 0,
      "customerFirstName": "test",
      "customerLastName": null,
      "additionalAttributes": [
        {
          "key": "WebChannelData",
          "type": "WebChannelData",
          "value": {
            "browserDeviceInfo": {
              "browserId": null,
              "browserIdExpiryTime": null,
              "browserName": null,
              "deviceType": null
            },
            "queue": "",
            "locale": {
              "timezone": null,
              "language": null,
              "country": null
            },
            "formData": {
              "id": 0.15920776548895632,
              "formId": "676abb5d245290002736779a",
              "filledBy": "web-widget",
              "attributes": [
                {
                  "value": "test",
                  "key": "first_name",
                  "type": "string"
                },
                {
                  "value": "0991223",
                  "key": "phone",
                  "type": "string"
                }
              ],
              "createdOn": "2025-02-28T14:43:00.364Z"
            }
          }
        }
      ]
    },
    "latestIntent": null,
    "customerPresence": {
      "value": null
    },
    "isActive": true,
    "conversationId": "67c1cb75956d765cfc275754",
    "roomInfo": {
      "id": "67c1cb75956d765cfc275753",
      "mode": "CONTACT_CENTER"
    },
    "state": {
      "name": "STARTED",
      "reasonCode": "CUSTOMER"
    },
    "channelSessionDirection": "INBOUND",
    "active": true
  },
  "roomInfo": {
    "id": "67c1cb75956d765cfc275753",
    "mode": "CONTACT_CENTER"
  },
  "taskId": "8d0e3f28-3094-4f08-8d53-f2758b8bd06d:0b5e04fa-8b51-4aaf-ae6c-aa0004aa38aa",
  "taskState": {
    "name": "RESERVED"
  },
  "taskDirection": "INBOUND",
  "queue": {
    "id": "673f125576e125429ea2f2b7",
    "name": "chat-khurram"
  },
  "note": null,
  "requestedBy": null,
  "correlationId": "44737847-ec2e-44b5-b460-3eedb89e8592"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [revokeTask](./revokeTask.md)
- [topicSubscription](./topicSubscription.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
