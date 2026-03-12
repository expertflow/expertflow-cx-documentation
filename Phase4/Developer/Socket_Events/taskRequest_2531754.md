# CX Knowledgebase : taskRequest

**Event Name**|  taskRequest  
---|---  
**Event Description**|  Event is triggered on a new conversation request.  
**Emitter**|  Agent Manager  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
channelSession| type: Objectdesc: contains values of properties related to the session that has been established through a particular channel e.g. web.|   
ccUser| type: Objectdesc: This object contains agent information| Properties are described [here](https://docs.expertflow.com/display/CIMp/CC+User).  
taskId| type: Stringdesc: ID of the task i.e. chat/call request| -  
taskState| type: Object| 

  * name - current state of the task

  
conversationId| type: Stringdesc: ID of the conversation| -  
roomInfo| type: Object|   
taskDirection| type: stringDirection of the task either INBOUND or OUTBOUND|   
queue| type: Object| 

  * id - ID of the queue
  * name - name of the queue

  
note| type: string|   
requestedBy| type: string| 
[code] 
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
          ],
          "urlTest2": "https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2528142/Agent+Desk+Permissions+-+Resource+Scope+Groups+Mapping"
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
[/code]
