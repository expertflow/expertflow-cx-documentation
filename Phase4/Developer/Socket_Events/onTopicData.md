---
title: "onTopicData"
summary: "Emitted by Agent Manager when an agent subscribes to a topic, delivering full conversation topic data including participants, channel session, and event history."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["onTopicData socket event CX", "onTopicData Agent Manager CX", "Socket.IO CX"]
aliases: ["onTopicData event ExpertFlow", "onTopicData socket CX"]
last-updated: 2026-03-12
---

# onTopicData

Event is triggered when an agent subscribes to a topic. Delivers comprehensive conversation topic data to the agent.

| Property | Value |
|---|---|
| **Event Name** | `onTopicData` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

| Property | Type | Description |
|---|---|---|
| `conversationId` | String | System-generated ID for the conversation. |
| `correlationId` | Object | Correlation ID for tracing. |
| `roomInfo` | Object | Contains `id` (room ID) and `mode` (`PRIVATE` or `CONTACT_CENTER`). |
| `taskId` | String | ID of the task associated with this topic subscription. |
| `topicData` | Object | Full topic data including: `id`, `topicParticipant`, `customer`, `conversationData`, `state`, `participants`, `durationInSeconds`, `customerSuggestions`, `topicEvents`, `holdTimerDetails`, `externalGadgets`, `wrapUps`, `agentHandRaise`, `agentParticipants`, `agentSla`, `channelSession`. |

## Example Payload

```json
{
  "topicData": {
    "id": "67c1cb75956d765cfc275754",
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
    "conversationData": {
      "first_name": "test",
      "phone": "0991223"
    },
    "state": "CREATED",
    "participants": [
      {
        "type": "BOT",
        "role": "PRIMARY",
        "participant": {
          "participantType": "Bot",
          "id": "6712cf4bfb156449bb04ce99",
          "type": "RASA",
          "name": "Rasa",
          "uri": "http://192.168.1.184:30800"
        },
        "id": "67c1cb75956d765cfc27576a",
        "joiningTime": "2025-02-28T14:43:01.614+00:00",
        "token": null,
        "conversationId": null,
        "isActive": true,
        "userCredentials": {},
        "state": null,
        "stateChangedOn": null
      }
    ],
    "agentParticipants": [],
    "agentSla": {
      "totalDuration": null,
      "action": null,
      "startTime": null
    },
    "durationInSeconds": null,
    "customerSuggestions": [],
    "topicEvents": [
      {
        "id": "67c1cb75956d765cfc27576b",
        "name": "BOT_SUBSCRIBED",
        "type": "NOTIFICATION",
        "timestamp": "2025-02-28T14:43:01.619+00:00",
        "conversationId": "67c1cb75956d765cfc275754",
        "eventEmitter": {
          "id": "38327e73-4a21-4ad4-a958-a6385c8636aa",
          "type": "BOT",
          "senderName": "CONVERSATION_MONITOR",
          "additionalDetail": null
        },
        "roomInfo": {
          "id": "67c1cb75956d765cfc275753",
          "mode": "CONTACT_CENTER"
        }
      }
    ],
    "holdTimerDetails": {
      "totalDuration": null,
      "startTime": null
    },
    "agentHandRaise": {
      "handRaised": false,
      "agentNames": []
    },
    "externalGadgets": [],
    "wrapUps": [],
    "topicParticipant": {
      "id": "02366928-e194-4801-b5e8-432a4a087ebd",
      "type": "AGENT",
      "participant": {
        "id": "7dcdf513-da75-4667-968b-94b8098bc689",
        "participantType": "CCUser",
        "keycloakUser": {
          "id": "7dcdf513-da75-4667-968b-94b8098bc689",
          "firstName": "",
          "lastName": "",
          "username": "sabahat-agent1",
          "roles": [
            "default-roles-expertflow",
            "agent",
            "offline_access",
            "uma_authorization"
          ],
          "realm": "expertflow"
        },
        "associatedRoutingAttributes": []
      },
      "token": null,
      "conversationId": "67c1cb75956d765cfc275754",
      "role": "PRIMARY",
      "userCredentials": null,
      "state": "SUBSCRIBED"
    }
  },
  "correlationId": "c47c90e8-efbe-493b-90bf-7c1448217834",
  "conversationId": "67c1cb75956d765cfc275754",
  "roomInfo": {
    "id": "67c1cb75956d765cfc275753",
    "mode": "CONTACT_CENTER"
  },
  "taskId": "8d0e3f28-3094-4f08-8d53-f2758b8bd06d:0b5e04fa-8b51-4aaf-ae6c-aa0004aa38aa"
}
```

## Related Articles

- [Socket Events Overview](./index.md)
- [topicSubscription](./topicSubscription.md)
- [taskRequest](./taskRequest.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
