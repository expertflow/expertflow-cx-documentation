# CX Knowledgebase : publishCimEvent

**Event Name**|  publishCimEvent  
---|---  
**Event Description**|  Event is emitted when agent requests to agent manager for publishing in-conversation events such as the messages of multiple types such as plain, media, contact, location, URL and WrapUp.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
[ cimEvent](Messages%2C-Events%2C-and-Activities_2528021.html#CIMEvents)| type: Objectcontains parameter required for sending messages | 

  1. id - String - system generated
  2. name - String - value will always be "AGENT_MESSAGE" for message sent by agent
  3. type - String - value will always be "MESSAGE" in this case
  4. timestamp - epoch - system generated time
  5. data - CIMMessage Object - contains header and body of the message: 
     1. id - String - system generated identifier
     2. header - MessageHeader - header as defined in [Messages](CIM-Messages_2530195.html) section
     3. body - MessageBody - body as defined in [Messages](CIM-Messages_2530195.html) section

  
agentId| type: String ID of the agent from whom the event has been emitted| -  
conversationId| type: StringID of the conversation subscribed by the agent | -  
roomInfo| type: Object| 

  1. id - id of the room
  2. mode - mode of room 


[code] 
    {
      "cimEvent": {
        "id": "c65bb9da-f596-48a2-bef5-bd47f0732dbe",
        "name": "AGENT_MESSAGE",
        "type": "MESSAGE",
        "timestamp": 1653888665578,
        "data": {
          "id": "142ad3a6-6ab8-4cf7-9553-959e2c3605c2",
          "header": {
            "timestamp": 1653888665578,
            "sender": {
              "id": "688ef131-9cd6-4108-893e-033943eb2be0",
              "type": "AGENT",
              "participant": {
                "id": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
                "participantType": "CCUser",
                "keycloakUser": {
                  "id": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
                  "username": "faizan",
                  "permittedResources": {
                    "Resources": [
                      {
                        "scopes": [
                          "view",
                          "manage"
                        ],
                        "rsid": "44e205bc-86f0-4e6a-b03a-844c1317722d",
                        "rsname": "leave-chat"
                      },
                      {
                        "scopes": [
                          "dummy"
                        ],
                        "rsid": "6e8c5866-3f42-4131-b72a-f9da6ba1bfa5",
                        "rsname": "dummy"
                      },
                      {
                        "scopes": [
                          "view",
                          "manage"
                        ],
                        "rsid": "24978903-b9c3-4823-b3bb-e5731ee37a65",
                        "rsname": "state-change"
                      },
                      {
                        "scopes": [
                          "view",
                          "manage"
                        ],
                        "rsid": "dbcb5f8c-03d5-4171-989f-b4f3365882e9",
                        "rsname": "subscribed-list"
                      },
                      {
                        "scopes": [
                          "view",
                          "manage"
                        ],
                        "rsid": "e59b98ee-9fff-4583-9a09-8f85ed78459d",
                        "rsname": "customer-list"
                      },
                      {
                        "scopes": [
                          "view",
                          "manage"
                        ],
                        "rsid": "33020afa-6fee-4c3b-830d-96c241a997ca",
                        "rsname": "customer-conversation-view"
                      }
                    ]
                  },
                  "roles": [
                    "agent",
                    "offline_access",
                    "default-roles-university",
                    "uma_authorization"
                  ],
                  "realm": "university"
                },
                "associatedRoutingAttributes": []
              },
              "token": null,
              "topicId": "261c271a-58e6-4571-9d25-77ad26d745d6",
              "role": "PRIMARY",
              "userCredentials": null,
              "state": "SUBSCRIBED"
            },
            "channelSession": {
              "participantType": "ChannelSession",
              "id": "7f570b41-1d5d-4932-bffe-fcdabcec1f3d",
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
                    "providerWebhook": "https://bb5c-115-186-148-106.ngrok.io/message/receive",
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
                "_id": "6294565557bd6a3cc1280bb9",
                "firstName": "JaneDoe",
                "phoneNumber": [],
                "isAnonymous": true,
                "__v": 0,
                "web": [
                  "43466"
                ]
              },
              "customerSuggestions": [],
              "channelData": {
                "channelCustomerIdentifier": "43466",
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
                        "id": 0.9542203461353682,
                        "formId": 0.5467590643299935,
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
                            "value": "43466",
                            "key": "channelIdentifier1",
                            "type": "string"
                          }
                        ],
                        "createdOn": "2022-05-30T05:30:29.323Z"
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
              "topicId": "261c271a-58e6-4571-9d25-77ad26d745d6",
              "state": "STARTED",
              "active": true
            },
            "channelData": {
              "channelCustomerIdentifier": "43466",
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
                      "id": 0.9542203461353682,
                      "formId": 0.5467590643299935,
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
                          "value": "43466",
                          "key": "channelIdentifier1",
                          "type": "string"
                        }
                      ],
                      "createdOn": "2022-05-30T05:30:29.323Z"
                    }
                  }
                }
              ]
            }
          },
          "body": {
            "markdownText": "fsadf",
            "type": "PLAIN"
          }
        }
      },
      "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "conversationId": "261c271a-58e6-4571-9d25-77ad26d745d6",
      "roomInfo": {
        "id": "65a625609487373651365bfb",
        "mode": "CONTACT_CENTER"
      }
    }
[/code]
