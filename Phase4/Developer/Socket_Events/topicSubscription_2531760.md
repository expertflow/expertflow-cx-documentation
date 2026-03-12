# CX Knowledgebase : topicSubscription

**Event Name**|  topicSubscription  
---|---  
**Event Description**|  Agent requests to agent manager for the topic subscription by emitting this event.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
topicParticipant| type: Objectdesc:| id  
conversationId| type: Stringdesc: ID of the conversation for subscription|   
agentId| type: String desc: ID of the agent for whom the event has been emitted| -  
taskId| type: Stringdesc: ID of the task subscribed by the agent | -  
roomInfo| type: Object| 
[code] 
    {
      "topicParticipant": {
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
      "conversationId": "261c271a-58e6-4571-9d25-77ad26d745d6",
      "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "taskId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "roomInfo":  {
        "id": "65a625609487373651365bfb",
        "mode": "CONTACT_CENTER"
      }
    }
[/code]
