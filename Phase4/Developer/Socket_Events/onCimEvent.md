---
title: "onCimEvent"
summary: "Emitted by Agent Manager to send real-time CIM Events to the agent during an active conversation."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["onCimEvent socket event CX", "onCimEvent Agent Manager CX", "Socket.IO CX"]
aliases: ["onCimEvent event ExpertFlow", "onCimEvent socket CX"]
last-updated: 2026-03-12
---

# onCimEvent

The Agent Manager sends real-time CIM Events to the agent through this event.

| Property | Value |
|---|---|
| **Event Name** | `onCimEvent` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `cimEvent` | Object | The CIM Event object containing all event details. Includes `id` (String, system generated ID), `name` (event name), `type` (event type), `timestamp` (epoch), and `data` (event payload with header, suggestions, requestedMessage). |
| `conversationId` | String | ID of the conversation associated with the CIM event. |

## Example Payload

```json
{
  "cimEvent": {
    "id": "e8ced09f-50b9-4721-bcfd-80ca07994cfd",
    "name": "BOT_SUGGESTION",
    "type": "SUGGESTION",
    "timestamp": 1651938185572,
    "data": {
      "id": "bcc62bd4-e021-4ca0-b285-a5b200192f81",
      "header": {
        "sender": {
          "type": "BOT",
          "role": "ASSISTANT",
          "participant": {
            "participantType": "TopicMonitor",
            "id": "fcfe0af2-87a3-4cdf-b6f3-a3286e621ea7",
            "displayName": "Topic Monitor: fcfe0af2-87a3-4cdf-b6f3-a3286e621ea7"
          },
          "id": "0af29801-14f9-4e36-b4d3-f36ca14310de",
          "joiningTime": 1651937794361,
          "token": null,
          "topicId": "9a8d8480-3df6-494b-90cc-b324fe5c5224",
          "isActive": true,
          "userCredentials": {},
          "state": "SUBSCRIBED",
          "stateChangedOn": 1651937794361
        },
        "channelData": {
          "channelCustomerIdentifier": "113377701",
          "serviceIdentifier": "1111",
          "requestPriority": 0,
          "channelTypeCode": "webChannel",
          "additionalAttributes": []
        },
        "language": {},
        "timestamp": 1651938185571,
        "securityInfo": {},
        "stamps": [],
        "intent": null,
        "entities": {},
        "channelSession": {
          "participantType": "ChannelSession",
          "id": "a5c80b3f-ea41-4caf-979d-641a1c32f9bd",
          "channel": {
            "id": "6224aa535bd05f57c1c18517",
            "name": "web",
            "serviceIdentifier": "1111",
            "tenant": {
              "id": "42c622fe-4458-46f2-a30e-f74daaf9182b",
              "name": null
            },
            "channelConfig": {
              "id": "ea26b041-df49-465b-9ac0-eee14702aa13",
              "channelMode": "HYBRID",
              "conversationBot": "",
              "responseSla": 60000,
              "customerActivityTimeout": 30000,
              "customerIdentificationCriteria": {
                "value": null
              },
              "routingPolicy": {
                "agentSelectionPolicy": "LONGEST_AVAILABLE",
                "routeToLastAgent": true,
                "routingMode": "PULL",
                "routingObjectId": "6224aa24378c960030df479f",
                "agentRequestTtl": 60000
              },
              "botId": "8bce469d-91d9-43a1-bf14-1f0832396588"
            },
            "channelConnector": {
              "id": "6224a9d25bd05f57c1c18506",
              "name": "web",
              "channelProviderInterface": {
                "id": "6224a9c75bd05f57c1c18500",
                "name": "web",
                "supportedChannelTypes": [
                  {
                    "id": "622222cc5bd05f57c1c18421",
                    "name": "WEB",
                    "channelLogo": "_WEB.svg",
                    "isInteractive": true,
                    "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                  },
                  {
                    "id": "6233de0e3ef6175890847d4c",
                    "name": "web",
                    "channelLogo": "32917_web-1873373_1280.png",
                    "isInteractive": true,
                    "mediaRoutingDomain": "6233dde8c004592808ad3c0d"
                  }
                ],
                "providerWebhook": "https://cim.expertflow.com/web-channel-manager/message/receive",
                "channelProviderConfigSchema": []
              },
              "channelProviderConfigs": [],
              "tenant": {
                "id": "123308f8-e662-418b-abc1-1b2f8873cb26",
                "name": null
              }
            },
            "channelType": {
              "id": "622222cc5bd05f57c1c18421",
              "name": "WEB",
              "channelLogo": "_WEB.svg",
              "isInteractive": true,
              "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
            }
          },
          "customer": {
            "_id": "62768c7eb5ccce3b85e1f47c",
            "firstName": "Jane Doe",
            "phoneNumber": [],
            "isAnonymous": true,
            "__v": 0,
            "web": [
              "113377701"
            ]
          },
          "customerSuggestions": [],
          "channelData": {
            "channelCustomerIdentifier": "113377701",
            "serviceIdentifier": "1111",
            "requestPriority": 0,
            "channelTypeCode": "webChannel",
            "additionalAttributes": []
          },
          "latestIntent": null,
          "customerPresence": {
            "value": null
          },
          "isActive": true,
          "topicId": "9a8d8480-3df6-494b-90cc-b324fe5c5224",
          "state": "STARTED",
          "active": true
        },
        "replyToMessageId": null,
        "providerMessageId": null
      },
      "suggestions": [
        {
          "messageBody": {
            "type": "PLAIN",
            "markdownText": "Bot could not understand your message, all relevant agents have been notified, agent(s) will join you shortly. Please wait!"
          },
          "confidenceLevel": 0
        }
      ],
      "requestedMessage": {
        "id": "622a53b0-ce1c-11ec-be50-d52d6fe9d1bf",
        "header": {
          "sender": {
            "type": "BOT",
            "role": "ASSISTANT",
            "participant": {
              "participantType": "TopicMonitor",
              "id": "fcfe0af2-87a3-4cdf-b6f3-a3286e621ea7",
              "displayName": "Topic Monitor: fcfe0af2-87a3-4cdf-b6f3-a3286e621ea7"
            },
            "id": "0af29801-14f9-4e36-b4d3-f36ca14310de",
            "joiningTime": 1651937794361,
            "token": null,
            "topicId": "9a8d8480-3df6-494b-90cc-b324fe5c5224",
            "isActive": true,
            "userCredentials": {},
            "state": "SUBSCRIBED",
            "stateChangedOn": 1651937794361
          },
          "channelData": {
            "channelCustomerIdentifier": "113377701",
            "serviceIdentifier": "1111",
            "requestPriority": 0,
            "channelTypeCode": "webChannel",
            "additionalAttributes": []
          },
          "language": {},
          "timestamp": 1651938185571,
          "securityInfo": {},
          "stamps": [],
          "intent": null,
          "entities": {},
          "replyToMessageId": null,
          "providerMessageId": null
        },
        "body": {
          "type": "PLAIN",
          "markdownText": "ok"
        }
      }
    }
  },
  "conversationId": "<<UUID>>"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [publishCimEvent](./publishCimEvent.md)
- [CIM Messages](../CIM-Message-Schema/CIM-Messages.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
