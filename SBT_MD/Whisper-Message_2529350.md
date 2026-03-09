# CX Knowledgebase : Whisper Message

Agents can exchange messages amongst each other in an active conversation. The customer will not be able to see whisper messages. Any type of message can be sent here e.g. Plain, Video, Image etc.

  
the ['_publishCimEvent_ ’](publishCimEvent_2531739.html) will contain WHISPER_MESSAGE event in the cimEvent

  


**WHISPER_MESSAGE** event
[code] 
    {
        "id": "d86ba3a8-57fb-4512-871d-0c7ed0172f13",
        "name": "WHISPER_MESSAGE",
        "type": "MESSAGE",
        "conversationId": "694135361fde7e4212be1824",
        "roomInfo": {
            "id": "694135361fde7e4212be1823",
            "mode": "CONTACT_CENTER"
        },
        "timestamp": 1765881831351,
        "data": {
            "id": "33873c88-9a2e-4017-a92c-9b2f08ead2b0",
            "header": {
                "timestamp": 1765881831350,
                "sender": {
                    "id": "3c24d80a-4571-4df1-acdf-2be68a32ed85",
                    "senderName": "raza",
                    "type": "AGENT",
                    "additionalDetail": {
                        "firstName": "raza",
                        "lastName": ""
                    }
                },
                "channelData": {
                    "channelCustomerIdentifier": "1212",
                    "serviceIdentifier": "9956",
                    "requestPriority": 0,
                    "customerFirstName": null,
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
                                    "id": 0.983499490272885,
                                    "formId": "6932b1c1345852183beec3a5",
                                    "filledBy": "web-widget",
                                    "attributes": [
                                        {
                                            "value": "transfer",
                                            "key": "name",
                                            "type": "string"
                                        },
                                        {
                                            "value": "1212",
                                            "key": "phone",
                                            "type": "string"
                                        }
                                    ],
                                    "createdOn": "2025-12-16T10:32:22.052Z"
                                }
                            }
                        }
                    ]
                },
                "intent": null,
                "additionalData": {
                    "isEncoded": true
                },
                "conversationId": "694135361fde7e4212be1824",
                "roomId": "694135361fde7e4212be1823",
                "channelSessionId": "69413536c18fae43a7913dba",
                "customer": {
                    "_id": "694130729b2330ed2d0a3ea0",
                    "firstName": "1212",
                    "phoneNumber": [],
                    "isAnonymous": true,
                    "__v": 0,
                    "web": [
                        "1212"
                    ]
                },
                "channelSession": {
                    "participantType": "ChannelSession",
                    "id": "69413536c18fae43a7913dba",
                    "channel": {
                        "id": "6932b17e3f19753775b74490",
                        "calendarId": "",
                        "name": "Amna-Web",
                        "serviceIdentifier": "9956",
                        "defaultOutbound": false,
                        "tenant": {
                            "id": "69413477c18fae43a7913daf",
                            "name": null
                        },
                        "channelConfig": {
                            "id": "69413477c18fae43a7913db0",
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
                                "routeToLastAgent": true,
                                "routingMode": "PUSH",
                                "routingObjectId": "6932ae541fb1996dc2e79529",
                                "agentRequestTtl": 120
                            },
                            "botId": "6932aed1098c173271a2025b"
                        },
                        "channelConnector": {
                            "id": "6932ae953f19753775b7448a",
                            "name": "Web",
                            "channelProviderInterface": {
                                "id": "6932ae2b3f19753775b74488",
                                "name": "Web",
                                "supportedChannelTypes": [
                                    {
                                        "id": "693203343f19753775b74473",
                                        "name": "WEB",
                                        "channelLogo": "_WEB.svg",
                                        "isInteractive": false,
                                        "mediaRoutingDomain": "6305de07166ba1099d11d8e6",
                                        "deleted": false
                                    }
                                ],
                                "providerWebhook": "http://ef-cx-web-channel-manager-svc:7000",
                                "channelProviderConfigSchema": []
                            },
                            "channelProviderConfigs": [],
                            "tenant": {
                                "id": "6932ae953f19753775b7448c",
                                "name": null
                            }
                        },
                        "channelType": {
                            "id": "693203343f19753775b74473",
                            "name": "WEB",
                            "channelLogo": "_WEB.svg",
                            "isInteractive": false,
                            "mediaRoutingDomain": "6305de07166ba1099d11d8e6",
                            "deleted": false
                        }
                    },
                    "customer": {
                        "_id": "694130729b2330ed2d0a3ea0",
                        "firstName": "1212",
                        "phoneNumber": [],
                        "isAnonymous": true,
                        "__v": 0,
                        "web": [
                            "1212"
                        ]
                    },
                    "customerSuggestions": [],
                    "channelData": {
                        "channelCustomerIdentifier": "1212",
                        "serviceIdentifier": "9956",
                        "requestPriority": 0,
                        "customerFirstName": null,
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
                                        "id": 0.983499490272885,
                                        "formId": "6932b1c1345852183beec3a5",
                                        "filledBy": "web-widget",
                                        "attributes": [
                                            {
                                                "value": "transfer",
                                                "key": "name",
                                                "type": "string"
                                            },
                                            {
                                                "value": "1212",
                                                "key": "phone",
                                                "type": "string"
                                            }
                                        ],
                                        "createdOn": "2025-12-16T10:32:22.052Z"
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
                    "conversationId": "694135361fde7e4212be1824",
                    "roomInfo": {
                        "id": "694135361fde7e4212be1823",
                        "mode": "CONTACT_CENTER"
                    },
                    "state": {
                        "name": "STARTED",
                        "reasonCode": "CUSTOMER"
                    },
                    "channelSessionDirection": "INBOUND",
                    "active": true
                }
            },
            "body": {
                "markdownText": "aGVsbG8=",
                "type": "PLAIN"
            }
        },
        "channelSession": {
            "participantType": "ChannelSession",
            "id": "69413536c18fae43a7913dba",
            "channel": {
                "id": "6932b17e3f19753775b74490",
                "calendarId": "",
                "name": "Amna-Web",
                "serviceIdentifier": "9956",
                "defaultOutbound": false,
                "tenant": {
                    "id": "69413477c18fae43a7913daf",
                    "name": null
                },
                "channelConfig": {
                    "id": "69413477c18fae43a7913db0",
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
                        "routeToLastAgent": true,
                        "routingMode": "PUSH",
                        "routingObjectId": "6932ae541fb1996dc2e79529",
                        "agentRequestTtl": 120
                    },
                    "botId": "6932aed1098c173271a2025b"
                },
                "channelConnector": {
                    "id": "6932ae953f19753775b7448a",
                    "name": "Web",
                    "channelProviderInterface": {
                        "id": "6932ae2b3f19753775b74488",
                        "name": "Web",
                        "supportedChannelTypes": [
                            {
                                "id": "693203343f19753775b74473",
                                "name": "WEB",
                                "channelLogo": "_WEB.svg",
                                "isInteractive": false,
                                "mediaRoutingDomain": "6305de07166ba1099d11d8e6",
                                "deleted": false
                            }
                        ],
                        "providerWebhook": "http://ef-cx-web-channel-manager-svc:7000",
                        "channelProviderConfigSchema": []
                    },
                    "channelProviderConfigs": [],
                    "tenant": {
                        "id": "6932ae953f19753775b7448c",
                        "name": null
                    }
                },
                "channelType": {
                    "id": "693203343f19753775b74473",
                    "name": "WEB",
                    "channelLogo": "_WEB.svg",
                    "isInteractive": false,
                    "mediaRoutingDomain": "6305de07166ba1099d11d8e6",
                    "deleted": false
                }
            },
            "customer": {
                "_id": "694130729b2330ed2d0a3ea0",
                "firstName": "1212",
                "phoneNumber": [],
                "isAnonymous": true,
                "__v": 0,
                "web": [
                    "1212"
                ]
            },
            "customerSuggestions": [],
            "channelData": {
                "channelCustomerIdentifier": "1212",
                "serviceIdentifier": "9956",
                "requestPriority": 0,
                "customerFirstName": null,
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
                                "id": 0.983499490272885,
                                "formId": "6932b1c1345852183beec3a5",
                                "filledBy": "web-widget",
                                "attributes": [
                                    {
                                        "value": "transfer",
                                        "key": "name",
                                        "type": "string"
                                    },
                                    {
                                        "value": "1212",
                                        "key": "phone",
                                        "type": "string"
                                    }
                                ],
                                "createdOn": "2025-12-16T10:32:22.052Z"
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
            "conversationId": "694135361fde7e4212be1824",
            "roomInfo": {
                "id": "694135361fde7e4212be1823",
                "mode": "CONTACT_CENTER"
            },
            "state": {
                "name": "STARTED",
                "reasonCode": "CUSTOMER"
            },
            "channelSessionDirection": "INBOUND",
            "active": true
        },
        "eventEmitter": {
            "id": "3c24d80a-4571-4df1-acdf-2be68a32ed85",
            "senderName": "raza",
            "type": "AGENT",
            "additionalDetail": {
                "firstName": "raza",
                "lastName": ""
            }
        }
    }
[/code]

  


  


  


  

