# CX Knowledgebase : unsubscribePullModeList

**Event Name**|  unsubscribePullModeList  
---|---  
**Event Description**|  When an agent unsubscribes to a list the agent desk emits an event of unsubscribePullModeList to the agent manager, agent manager listens to the event and successfully unsubscribes from the list for that agent.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
topicParticipant| type: Objectagent details such as id, type, keycloack user authentication fields etc.|   
agentId| type: String ID of the agent for whom the event has been emitted| -  
listId| type: StringID of the list unsubscribed by the agent | -  
list| type: Objectproperties of the unsubscribed list| 

  1. name - String - name of the list
  2. description - String - description of the list
  3. id - String - ID of the list


[code] 
    {
      "topicParticipant": {
        "id": "e7331318-cf3a-44dc-8467-d8a8d430ea8e",
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
        "topicId": "6224aa24378c960030df479f",
        "role": "PRIMARY",
        "userCredentials": null,
        "state": "SUBSCRIBED"
      },
      "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "listId": "6224aa24378c960030df479f",
      "list": {
        "name": "L1",
        "description": null,
        "id": "6224aa24378c960030df479f"
      }
    }
[/code]
