---
title: "pullModeSubscribedListRequests"
summary: "Emitted by Agent Manager when there are existing chat requests present in a list subscribed by the agent."
audience: [developer-integrator]
product-area: [sdk, platform]
doc-type: reference
difficulty: advanced
keywords: ["pullModeSubscribedListRequests socket event CX", "pullModeSubscribedListRequests Agent Manager CX", "Socket.IO CX"]
aliases: ["pullModeSubscribedListRequests event ExpertFlow", "pullModeSubscribedListRequests socket CX"]
last-updated: 2026-03-12
---

# pullModeSubscribedListRequests

Event is triggered if there are chat requests present in a list subscribed by the agent. Returns an array of pending conversation requests in the list.

| Property | Value |
|---|---|
| **Event Name** | `pullModeSubscribedListRequests` |
| **Emitter** | Agent Manager |
| **Direction** | Agent Manager → Agent Desk |

## Payload Properties

Each item in the returned array contains:

| Property | Type | Description |
|---|---|---|
| `id` | String | System-generated ID of the chat request (conversation ID). |
| `channelSession` | Object | Contains values of properties related to the session established through a particular channel (e.g., web). |
| `status` | String | Status of the conversation in the list (e.g., `CREATED`). |
| `listId` | String | ID of the list containing the chat request. |
| `time` | Date | Time when the request was sent. |

## Example Payload

```json
[
    {
        "id": "be945b2b-4c64-423b-aa72-9dde5b128da4",
        "channelSession": {
            "participantType": "ChannelSession",
            "id": "af254fa9-6833-4f57-8de9-13741840b9ea",
            "channel": {
                "id": "6224aa535bd05f57c1c18517",
                "name": "web",
                "serviceIdentifier": "1111",
                "tenant": {
                    "id": "f7c4da93-680d-4f73-8465-3dbc22689243",
                    "name": null
                },
                "channelConfig": {
                    "id": "176db0b0-ac05-4a3f-ae0e-562a5e230a20",
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
                "_id": "626ef6b8b5ccce3610e1f41f",
                "firstName": "Jane Doe",
                "phoneNumber": [],
                "isAnonymous": true,
                "__v": 0,
                "web": [
                    "1133777"
                ]
            },
            "customerSuggestions": [],
            "channelData": {
                "channelCustomerIdentifier": "1133777",
                "serviceIdentifier": "1111",
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
                                "id": 0.2894963641253081,
                                "formId": 0.5638593069997029,
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
                                        "value": "1133777",
                                        "key": "channelIdentifier1",
                                        "type": "string"
                                    }
                                ],
                                "createdOn": "2022-05-07T15:00:00.406Z"
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
            "topicId": "be945b2b-4c64-423b-aa72-9dde5b128da4",
            "state": "STARTED",
            "active": true
        },
        "status": "CREATED",
        "listId": "6224aa24378c960030df479f",
        "time": "2022-05-07T14:59:08.252+00:00"
    }
]
```

## Related Articles

- [Socket Events Overview](./index.md)
- [onPullModeSubscribedListRequest](./onPullModeSubscribedListRequest.md)
- [subscribePullModeList](./subscribePullModeList.md)
- [AgentManager SDK Integration Guide](../../../How-to_Guides/Developer_Integrator/AgentManager-SDK-Integration-Guide.md)
