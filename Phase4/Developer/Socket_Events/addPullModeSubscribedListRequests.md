---
title: "addPullModeSubscribedListRequests"
summary: "Emitted by Agent Manager when an agent subscribes to a list, delivering the list of existing conversations in that list."
audience: [developer]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["addPullModeSubscribedListRequests socket event CX", "addPullModeSubscribedListRequests Agent Manager CX", "Socket.IO CX"]
aliases: ["addPullModeSubscribedListRequests event ExpertFlow", "addPullModeSubscribedListRequests socket CX"]
last-updated: 2026-03-12
---

# addPullModeSubscribedListRequests

Event is triggered when an agent subscribes to a list. If the list contains chats, a list of conversations is returned; otherwise an empty array is returned.

| Property | Value |
|---|---|
| **Event Name** | `addPullModeSubscribedListRequests` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

Each item in the returned array contains:

| Property | Type | Description |
|---|---|---|
| `id` | String | System-generated ID of the conversation (chat request). |
| `channelSession` | Object | Contains values of properties related to the session established through a particular channel (e.g., web). |
| `status` | String | Status of the conversation in the list (e.g., `CREATED`). |
| `listId` | String | ID of the list containing the chat request. |
| `time` | Date | Time when the request was sent. |

## Example Payload

```json
[
  {
    "id": "8dda94ac-370b-4f8d-a0d5-b5527e3a8365",
    "channelSession": {
      "participantType": "ChannelSession",
      "id": "2047cb9b-6733-4864-ad76-84476666350c",
      "channel": {
        "id": "6227699608df8d31bb15d2e5",
        "name": "faizan-web",
        "serviceIdentifier": "1212",
        "tenant": {
          "id": "cd234bf9-0f38-42c1-8d31-b6ee21ad320f",
          "name": null
        },
        "channelConfig": {
          "id": "dab265fc-8302-4486-8363-83e7058330ca",
          "channelMode": "HYBRID",
          "conversationBot": "",
          "responseSla": 300,
          "customerActivityTimeout": 60,
          "customerIdentificationCriteria": {
            "value": null
          },
          "routingPolicy": {
            "agentSelectionPolicy": "LONGEST_AVAILABLE",
            "routeToLastAgent": true,
            "routingMode": "PULL",
            "routingObjectId": "622769a8ca110c0030fe0f31",
            "agentRequestTtl": 300
          },
          "botId": "8bce469d-91d9-43a1-bf14-1f0832396588"
        },
        "channelConnector": {
          "id": "6227693508df8d31bb15d2ca",
          "name": "faizan-web",
          "channelProviderInterface": {
            "id": "62276c5808df8d31bb15d38b",
            "name": "faizan-web",
            "supportedChannelTypes": [
              {
                "id": "622222cc5bd05f57c1c18421",
                "name": "WEB",
                "channelLogo": "_WEB.svg",
                "isInteractive": true,
                "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
              }
            ],
            "providerWebhook": "https://cim.expertflow.com/web-channel-manager/message/receive",
            "channelProviderConfigSchema": []
          },
          "channelProviderConfigs": [],
          "tenant": {
            "id": "b846ccdb-39f4-4577-9469-c6fb17694c3a",
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
        "_id": "6274cec4b5ccce4ac3e1f452",
        "firstName": "Jane Doe",
        "phoneNumber": [],
        "isAnonymous": true,
        "__v": 0,
        "web": [
          "2342334"
        ]
      },
      "customerSuggestions": [],
      "channelData": {
        "channelCustomerIdentifier": "2342334",
        "serviceIdentifier": "1212",
        "requestPriority": 0,
        "channelTypeCode": "webChannel",
        "additionalAttributes": [
          {
            "key": "WebChannelData",
            "type": "WebChannelData",
            "value": {
              "browserDeviceInfo": {
                "browserId": "123456",
                "browserIdExpiryTime": "9999",
                "browserName": "chrome",
                "deviceType": "desktop"
              },
              "queue": "",
              "locale": {
                "timezone": "asia/karachi",
                "language": "english",
                "country": "pakistan"
              },
              "formData": {
                "id": 0.8710788430006686,
                "formId": 0.6175360465901849,
                "filledBy": "web-init",
                "attributes": [
                  {
                    "value": "",
                    "key": "firstName",
                    "type": "string"
                  },
                  {
                    "value": "",
                    "key": "lastName",
                    "type": "string"
                  },
                  {
                    "value": "",
                    "key": "email",
                    "type": "string"
                  },
                  {
                    "value": "2342334",
                    "key": "channelIdentifier1",
                    "type": "string"
                  }
                ],
                "createdOn": "2022-05-06T07:32:03.764Z"
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
      "topicId": "8dda94ac-370b-4f8d-a0d5-b5527e3a8365",
      "state": "STARTED",
      "active": true
    },
    "status": "CREATED",
    "listId": "622769a8ca110c0030fe0f31",
    "time": "2022-05-06T07:31:16.708+00:00"
  }
]
```

## Related Articles

- [Socket Events Overview](./index.md)
- [subscribePullModeList](./subscribePullModeList_2531752.md)
- [pullModeSubscribedListRequests](./pullModeSubscribedListRequests_2531743.md)
- [AgentManager SDK Integration Guide](../AgentManager-SDK-Integration-Guide.md)
