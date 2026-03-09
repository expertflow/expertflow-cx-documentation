# CX Knowledgebase : addPullModeSubscribedListRequests

**Event Name**|  addPullModeSubscribedListRequests  
---|---  
**Event Description**|  Event is triggered when an agent subscribes to a list. If it contains chats, then a list of conversations is returned else the array is returned empty.  
**Emitter**|  Agent Manager  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
id| type: Stringsystem generated ID of the event| -  
channelSession| type: Objectcontains values of properties related to the session that has been established through a particular channel e.g. web.| Properties of channelSession can be accessed here.  
status| type: Stringstatus of the conversation in the list| -  
listId| type: StringID of the list containing the chat request| -  
time| type: Datetime when the request was sent| -
[code] 
    {
            "id": "8dda94ac-370b-4f8d-a0d5-b5527e3a8365",
            "channelSession": {
                "participantType": "ChannelSession",
                "id": "2047cb9b-6733-4864-ad76-84476666350c",
                "channel": {
                    "id": "6227699608df8d31bb15d2e5",
                    "name": "faizan-web",
                    "serviceIdentifier": "1212",
                    "tenant": {
                        "id": "cd234bf9-0f38-42c1-8d31-b6ee21ad320f",
                        "name": null
                    },
                    "channelConfig": {
                        "id": "dab265fc-8302-4486-8363-83e7058330ca",
                        "channelMode": "HYBRID",
                        "conversationBot": "",
                        "responseSla": 300,
                        "customerActivityTimeout": 60,
                        "customerIdentificationCriteria": {
                            "value": null
                        },
                        "routingPolicy": {
                            "agentSelectionPolicy": "LONGEST_AVAILABLE",
                            "routeToLastAgent": true,
                            "routingMode": "PULL",
                            "routingObjectId": "622769a8ca110c0030fe0f31",
                            "agentRequestTtl": 300
                        },
                        "botId": "8bce469d-91d9-43a1-bf14-1f0832396588"
                    },
                    "channelConnector": {
                        "id": "6227693508df8d31bb15d2ca",
                        "name": "faizan-web",
                        "channelProviderInterface": {
                            "id": "62276c5808df8d31bb15d38b",
                            "name": "faizan-web",
                            "supportedChannelTypes": [
                                {
                                    "id": "622222cc5bd05f57c1c18421",
                                    "name": "WEB",
                                    "channelLogo": "_WEB.svg",
                                    "isInteractive": true,
                                    "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                                }
                            ],
                            "providerWebhook": "https://cim.expertflow.com/web-channel-manager/message/receive",
                            "channelProviderConfigSchema": []
                        },
                        "channelProviderConfigs": [],
                        "tenant": {
                            "id": "b846ccdb-39f4-4577-9469-c6fb17694c3a",
                            "name": null
                        }
                    },
                    "channelType": {
                        "id": "622222cc5bd05f57c1c18421",
                        "name": "WEB",
                        "channelLogo": "_WEB.svg",
                        "isInteractive": true,
                        "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                    }
                },
                "customer": {
                    "_id": "6274cec4b5ccce4ac3e1f452",
                    "firstName": "Jane Doe",
                    "phoneNumber": [],
                    "isAnonymous": true,
                    "__v": 0,
                    "web": [
                        "2342334"
                    ]
                },
                "customerSuggestions": [],
                "channelData": {
                    "channelCustomerIdentifier": "2342334",
                    "serviceIdentifier": "1212",
                    "requestPriority": 0,
                    "channelTypeCode": "webChannel",
                    "additionalAttributes": [
                        {
                            "key": "WebChannelData",
                            "type": "WebChannelData",
                            "value": {
                                "browserDeviceInfo": {
                                    "browserId": "123456",
                                    "browserIdExpiryTime": "9999",
                                    "browserName": "chrome",
                                    "deviceType": "desktop"
                                },
                                "queue": "",
                                "locale": {
                                    "timezone": "asia/karachi",
                                    "language": "english",
                                    "country": "pakistan"
                                },
                                "formData": {
                                    "id": 0.8710788430006686,
                                    "formId": 0.6175360465901849,
                                    "filledBy": "web-init",
                                    "attributes": [
                                        {
                                            "value": "",
                                            "key": "firstName",
                                            "type": "string"
                                        },
                                        {
                                            "value": "",
                                            "key": "lastName",
                                            "type": "string"
                                        },
                                        {
                                            "value": "",
                                            "key": "email",
                                            "type": "string"
                                        },
                                        {
                                            "value": "2342334",
                                            "key": "channelIdentifier1",
                                            "type": "string"
                                        }
                                    ],
                                    "createdOn": "2022-05-06T07:32:03.764Z"
                                }
                            }
                        }
                    ]
                },
                "latestIntent": null,
                "customerPresence": {
                    "value": null
                },
                "isActive": true,
                "topicId": "8dda94ac-370b-4f8d-a0d5-b5527e3a8365",
                "state": "STARTED",
                "active": true
            },
            "status": "CREATED",
            "listId": "622769a8ca110c0030fe0f31",
            "time": "2022-05-06T07:31:16.708+00:00"
        },
        {
            "id": "1ef75821-84cf-4643-95c2-31ee7171a188",
            "channelSession": {
                "participantType": "ChannelSession",
                "id": "46c7da52-2d8d-4c2d-95eb-e2591f40cb67",
                "channel": {
                    "id": "6227699608df8d31bb15d2e5",
                    "name": "faizan-web",
                    "serviceIdentifier": "1212",
                    "tenant": {
                        "id": "cd234bf9-0f38-42c1-8d31-b6ee21ad320f",
                        "name": null
                    },
                    "channelConfig": {
                        "id": "dab265fc-8302-4486-8363-83e7058330ca",
                        "channelMode": "HYBRID",
                        "conversationBot": "",
                        "responseSla": 300,
                        "customerActivityTimeout": 60,
                        "customerIdentificationCriteria": {
                            "value": null
                        },
                        "routingPolicy": {
                            "agentSelectionPolicy": "LONGEST_AVAILABLE",
                            "routeToLastAgent": true,
                            "routingMode": "PULL",
                            "routingObjectId": "622769a8ca110c0030fe0f31",
                            "agentRequestTtl": 300
                        },
                        "botId": "8bce469d-91d9-43a1-bf14-1f0832396588"
                    },
                    "channelConnector": {
                        "id": "6227693508df8d31bb15d2ca",
                        "name": "faizan-web",
                        "channelProviderInterface": {
                            "id": "62276c5808df8d31bb15d38b",
                            "name": "faizan-web",
                            "supportedChannelTypes": [
                                {
                                    "id": "622222cc5bd05f57c1c18421",
                                    "name": "WEB",
                                    "channelLogo": "_WEB.svg",
                                    "isInteractive": true,
                                    "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                                }
                            ],
                            "providerWebhook": "https://cim.expertflow.com/web-channel-manager/message/receive",
                            "channelProviderConfigSchema": []
                        },
                        "channelProviderConfigs": [],
                        "tenant": {
                            "id": "b846ccdb-39f4-4577-9469-c6fb17694c3a",
                            "name": null
                        }
                    },
                    "channelType": {
                        "id": "622222cc5bd05f57c1c18421",
                        "name": "WEB",
                        "channelLogo": "_WEB.svg",
                        "isInteractive": true,
                        "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                    }
                },
                "customer": {
                    "_id": "6225a4f12716254f42f134e0",
                    "firstName": "Jane Doe",
                    "phoneNumber": [],
                    "isAnonymous": true,
                    "__v": 0,
                    "web": [
                        "543234"
                    ]
                },
                "customerSuggestions": [],
                "channelData": {
                    "channelCustomerIdentifier": "543234",
                    "serviceIdentifier": "1212",
                    "requestPriority": 0,
                    "channelTypeCode": "webChannel",
                    "additionalAttributes": [
                        {
                            "key": "WebChannelData",
                            "type": "WebChannelData",
                            "value": {
                                "browserDeviceInfo": {
                                    "browserId": "123456",
                                    "browserIdExpiryTime": "9999",
                                    "browserName": "chrome",
                                    "deviceType": "desktop"
                                },
                                "queue": "",
                                "locale": {
                                    "timezone": "asia/karachi",
                                    "language": "english",
                                    "country": "pakistan"
                                },
                                "formData": {
                                    "id": 0.8610970879908775,
                                    "formId": 0.12538274867641674,
                                    "filledBy": "web-init",
                                    "attributes": [
                                        {
                                            "value": "",
                                            "key": "firstName",
                                            "type": "string"
                                        },
                                        {
                                            "value": "",
                                            "key": "lastName",
                                            "type": "string"
                                        },
                                        {
                                            "value": "",
                                            "key": "email",
                                            "type": "string"
                                        },
                                        {
                                            "value": "543234",
                                            "key": "channelIdentifier1",
                                            "type": "string"
                                        }
                                    ],
                                    "createdOn": "2022-04-29T09:43:36.050Z"
                                }
                            }
                        }
                    ]
                },
                "latestIntent": null,
                "customerPresence": {
                    "value": null
                },
                "isActive": true,
                "topicId": "1ef75821-84cf-4643-95c2-31ee7171a188",
                "state": "STARTED",
                "active": true
            },
            "status": "CREATED",
            "listId": "622769a8ca110c0030fe0f31",
            "time": "2022-04-29T09:46:11.469+00:00"
        },
        {
            "id": "c4d93b35-5488-4bf3-8b48-31b4c10dacde",
            "channelSession": {
                "participantType": "ChannelSession",
                "id": "612b7e92-f94c-433c-a590-cac6f54d78bc",
                "channel": {
                    "id": "6227699608df8d31bb15d2e5",
                    "name": "faizan-web",
                    "serviceIdentifier": "1212",
                    "tenant": {
                        "id": "cd234bf9-0f38-42c1-8d31-b6ee21ad320f",
                        "name": null
                    },
                    "channelConfig": {
                        "id": "dab265fc-8302-4486-8363-83e7058330ca",
                        "channelMode": "HYBRID",
                        "conversationBot": "",
                        "responseSla": 300,
                        "customerActivityTimeout": 60,
                        "customerIdentificationCriteria": {
                            "value": null
                        },
                        "routingPolicy": {
                            "agentSelectionPolicy": "LONGEST_AVAILABLE",
                            "routeToLastAgent": true,
                            "routingMode": "PULL",
                            "routingObjectId": "622769a8ca110c0030fe0f31",
                            "agentRequestTtl": 300
                        },
                        "botId": "8bce469d-91d9-43a1-bf14-1f0832396588"
                    },
                    "channelConnector": {
                        "id": "6227693508df8d31bb15d2ca",
                        "name": "faizan-web",
                        "channelProviderInterface": {
                            "id": "62276c5808df8d31bb15d38b",
                            "name": "faizan-web",
                            "supportedChannelTypes": [
                                {
                                    "id": "622222cc5bd05f57c1c18421",
                                    "name": "WEB",
                                    "channelLogo": "_WEB.svg",
                                    "isInteractive": true,
                                    "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                                }
                            ],
                            "providerWebhook": "https://cim.expertflow.com/web-channel-manager/message/receive",
                            "channelProviderConfigSchema": []
                        },
                        "channelProviderConfigs": [],
                        "tenant": {
                            "id": "b846ccdb-39f4-4577-9469-c6fb17694c3a",
                            "name": null
                        }
                    },
                    "channelType": {
                        "id": "622222cc5bd05f57c1c18421",
                        "name": "WEB",
                        "channelLogo": "_WEB.svg",
                        "isInteractive": true,
                        "mediaRoutingDomain": "6223b491ef484b28639e9ca4"
                    }
                },
                "customer": {
                    "_id": "6274b410b5ccce92a9e1f43e",
                    "firstName": "Jane Doe",
                    "phoneNumber": [],
                    "isAnonymous": true,
                    "__v": 0,
                    "web": [
                        "5314"
                    ]
                },
                "customerSuggestions": [],
                "channelData": {
                    "channelCustomerIdentifier": "5314",
                    "serviceIdentifier": "1212",
                    "requestPriority": 0,
                    "channelTypeCode": "webChannel",
                    "additionalAttributes": [
                        {
                            "key": "WebChannelData",
                            "type": "WebChannelData",
                            "value": {
                                "browserDeviceInfo": {
                                    "browserId": "123456",
                                    "browserIdExpiryTime": "9999",
                                    "browserName": "chrome",
                                    "deviceType": "desktop"
                                },
                                "queue": "",
                                "locale": {
                                    "timezone": "asia/karachi",
                                    "language": "english",
                                    "country": "pakistan"
                                },
                                "formData": {
                                    "id": 0.11335307144711093,
                                    "formId": 0.09193565941545856,
                                    "filledBy": "web-init",
                                    "attributes": [
                                        {
                                            "value": "",
                                            "key": "firstName",
                                            "type": "string"
                                        },
                                        {
                                            "value": "",
                                            "key": "lastName",
                                            "type": "string"
                                        },
                                        {
                                            "value": "",
                                            "key": "email",
                                            "type": "string"
                                        },
                                        {
                                            "value": "5314",
                                            "key": "channelIdentifier1",
                                            "type": "string"
                                        }
                                    ],
                                    "createdOn": "2022-05-06T05:38:06.706Z"
                                }
                            }
                        }
                    ]
                },
                "latestIntent": null,
                "customerPresence": {
                    "value": null
                },
                "isActive": true,
                "topicId": "c4d93b35-5488-4bf3-8b48-31b4c10dacde",
                "state": "STARTED",
                "active": true
            },
            "status": "CREATED",
            "listId": "622769a8ca110c0030fe0f31",
            "time": "2022-05-06T05:37:20.580+00:00"
        }
[/code]
