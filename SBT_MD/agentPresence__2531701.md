# CX Knowledgebase : agentPresence_

**Event Name**|  agentPresence  
---|---  
**Event Description**|  Event triggered to update agent state information.  
**Emitter**|  Agent Manager  
**Action**|  Possible values are:

  * AGENT_STATE_UNCHANGED - when the event is received without any change in state.
  * AGENT_STATE_CHANGED - when the event is received with change in state.

  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
agentPresence| type: ObjectThe [AgentPresence](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2531701/agentPresence_#AgentPresence) object|   
agent | type: ObjectDesc: Defines the properties of the CC agent| 

  1. participantType - String - describes the type of user - agent or user
  2. id - String - system generated id of user
  3. keycloakUser - Object - contains properties of the agent as authenticated by keyCloack
  4. associatedRoutingAttributes - Array - for routing conversation to the agent

  
state| type: ObjectDesc: State of the agent (READY, NOT_READY) and the reason| 

  1. name - String - name of the state
  2. reasonCode - String - reason for change in state

  
stateChangeTime| type: Date ObjectDesc: time since change of state| -  
agentMrdStates| type: ObjectDesc: retains properties of state changes of the agent| 

  1. MRD - Array - contains details of the change of state of the agent such as id, name, description, interruptible, maxRequests

  
action| type: ObjectDesc: describes if event is fired without state change or not| -  
agentLoginTime| type: timestamp|   
agentStateChanged| type: boolean

  * true - in case of agent state changed
  * false - in case of agent MRD state changed

|   
mrdStateChanges| type: arraydesc: id of the MRD which state is going to be changed|   
  
### **AgentPresence**
[code] 
    {
      "agent": {
        "participantType": "CCUser",
        "id": "1fd5b05a-7c12-4955-bd59-8567f3e74445",
        "keycloakUser": {
          "id": "1fd5b05a-7c12-4955-bd59-8567f3e74445",
          "firstName": "admin",
          "lastName": null,
          "roles": [
            "offline_access",
            "default-roles-university",
            "admin",
            "uma_authorization"
          ],
          "username": "admin",
          "permittedResources": {
            "Resources": [
              {
                "rsid": "972e9078-ebb8-4fe2-9fc4-942a6914abf7",
                "rsname": "routing-engine",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "38e46d28-31bb-4e5f-8f56-13f10f5879d8",
                "rsname": "business-calendar",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "1365a664-afd1-4c1d-a21c-e9a4ccf0e332",
                "rsname": "general-settings",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "24c037dc-4792-4cf4-8f71-66a0d0ddd618",
                "rsname": "pull-mode-list",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "8f226171-1a57-4f79-b553-82c7344e66da",
                "rsname": "forms",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "35fa435d-b456-4faa-aab4-99064ae57987",
                "rsname": "reason-code",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "fe0f4e8c-47bb-487b-b8b9-c2726926217d",
                "rsname": "bot-settings",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "0c0e9f33-cc46-4cde-b88c-68d93a643b20",
                "rsname": "web-widget",
                "scopes": [
                  "view",
                  "manage"
                ]
              },
              {
                "rsid": "a61043f6-9980-4e31-a57b-e2c866f101ee",
                "rsname": "channel-manager",
                "scopes": [
                  "view",
                  "manage"
                ]
              }
            ]
          },
          "realm": "university"
        },
        "associatedRoutingAttributes": []
      },
      "state": {
        "name": "NOT_READY",
        "reasonCode": null
      },
      "stateChangeTime": 1651434965139,
      "agentMrdStates": [
        {
          "mrd": {
            "id": "6232cc5d44a4093550fea233",
            "name": "VOICE",
            "description": null,
            "interruptible": true,
            "maxRequests": 5
          },
          "state": "NOT_READY",
          "stateChangeTime": 1651434965138,
          "lastReadyStateChangeTime": 639057660000
        },
        {
          "mrd": {
            "id": "62302def6b1fba2525db2713",
            "name": "whatsapp-chat",
            "description": "ThisMRDistobeusedfortwilio-connectortestingbyWAQAS\t",
            "interruptible": true,
            "maxRequests": 10
          },
          "state": "NOT_READY",
          "stateChangeTime": 1651434965138,
          "lastReadyStateChangeTime": 639057660000
        },
        {
          "mrd": {
            "id": "6223b491ef484b28639e9ca4",
            "name": "chat",
            "description": null,
            "interruptible": true,
            "maxRequests": 5
          },
          "state": "NOT_READY",
          "stateChangeTime": 1651434965138,
          "lastReadyStateChangeTime": 639057660000
        },
        {
          "mrd": {
            "id": "6233dde8c004592808ad3c0d",
            "name": "Ahmad'sMrd",
            "description": "ThisMRDistobeusedfordevtestingbyAhmad",
            "interruptible": true,
            "maxRequests": 5
          },
          "state": "NOT_READY",
          "stateChangeTime": 1651434965138,
          "lastReadyStateChangeTime": 639057660000
        }
      ]
    }
[/code]

**Event received from the agent manager**
[code] 
    {
        "action": "AGENT_STATE_CHANGED",
        "agentStateChanged": false,
        "mrdStateChanges": [
            "20316843be924c8ab4f57a7a"
        ],
        "agentPresence": {
            "agent": {
                "participantType": "CCUser",
                "id": "eed4c6de-27b0-4321-b057-2a618dcad6d1",
                "keycloakUser": {
                    "id": "eed4c6de-27b0-4321-b057-2a618dcad6d1",
                    "firstName": "",
                    "lastName": "",
                    "roles": [
                        "default-roles-expertflow",
                        "agent",
                        "offline_access",
                        "uma_authorization"
                    ],
                    "username": "sabahat",
                    "permittedResources": {
                        "Resources": [
                            {
                                "rsid": "0697f9c1-e15f-436b-9dd4-de11f80887d1",
                                "rsname": "customer-labels",
                                "scopes": [
                                    "assign_label"
                                ]
                            },
                            {
                                "rsid": "1f4de32d-7beb-4d4b-9b1d-a486e97d0a0f",
                                "rsname": "agent-dashboard",
                                "scopes": [
                                    "view"
                                ]
                            },
                            {
                                "rsid": "db95f093-7a90-43ab-a0d7-7afca15fbec6",
                                "rsname": "agent-conversation-control",
                                "scopes": [
                                    "view_history",
                                    "view_leave_chat",
                                    "view_history_active_customer ",
                                    "view_direct_transfer",
                                    "view_initiate_chat",
                                    "view_wrap_up",
                                    "view_conference",
                                    "view_consult"
                                ]
                            },
                            {
                                "rsid": "5d0a7462-6bc3-4f76-89a4-9259073fb9fd",
                                "rsname": "customer",
                                "scopes": [
                                    "masked_pii",
                                    "view",
                                    "view_in_conversation",
                                    "manage_in_conversation"
                                ]
                            },
                            {
                                "rsid": "2158c6d6-cfdc-4ecb-aab4-8c521ee0d193",
                                "rsname": "subscribed-list",
                                "scopes": [
                                    "view"
                                ]
                            },
                            {
                                "rsid": "81e4cf55-e5fe-4612-965a-14e6d5888ca2",
                                "rsname": "state-change",
                                "scopes": [
                                    "manage_state_change"
                                ]
                            },
                            {
                                "rsid": "28310ed8-282f-4bda-8254-36cb81382c72",
                                "rsname": "recording-link",
                                "scopes": [
                                    "view"
                                ]
                            }
                        ]
                    },
                    "realm": "expertflow",
                    "attributes": {},
                    "userTeam": {
                        "teamId": "0d8b2ab5-8eb9-4060-a366-c5d23b45020a",
                        "teamName": "sabahat"
                    },
                    "supervisedTeams": []
                },
                "associatedRoutingAttributes": [
                    {
                        "routingAttribute": {
                            "id": "67c04c22a1f239243fad84a1",
                            "name": "sabahat-chat",
                            "description": null,
                            "type": "BOOLEAN",
                            "defaultValue": 1
                        },
                        "value": 1
                    }
                ],
                "associatedMrds": [
                    {
                        "mrdId": "62f9e360ea5311eda05b0242",
                        "maxAgentTasks": 1
                    },
                    {
                        "mrdId": "6305de07166ba1099d11d8e6",
                        "maxAgentTasks": 5
                    },
                    {
                        "mrdId": "20316843be924c8ab4f57a7a",
                        "maxAgentTasks": 1
                    }
                ]
            },
            "state": {
                "name": "READY",
                "reasonCode": null
            },
            "stateChangeTime": 1740656226434,
            "agentMrdStates": [
                {
                    "mrd": {
                        "id": "62f9e360ea5311eda05b0242",
                        "type": "64f6ee2dd49f4e9d7eb5f591",
                        "name": "CX VOICE",
                        "description": "Standard voice MRD for CX Voice",
                        "maxRequests": 1,
                        "interruptible": false
                    },
                    "state": "NOT_READY",
                    "previousState": null,
                    "stateChangeTime": 1740656023739,
                    "lastReadyStateChangeTime": 639057660000,
                    "maxAgentTasks": 1
                },
                {
                    "mrd": {
                        "id": "6305de07166ba1099d11d8e6",
                        "type": "64f6edf8b89b71cc6cb60917",
                        "name": "CHAT",
                        "description": "Standard chat MRD",
                        "maxRequests": 5,
                        "interruptible": true
                    },
                    "state": "READY",
                    "previousState": "NOT_READY",
                    "stateChangeTime": 1740656231094,
                    "lastReadyStateChangeTime": 1740656231094,
                    "maxAgentTasks": 5
                },
                {
                    "mrd": {
                        "id": "20316843be924c8ab4f57a7a",
                        "type": "64f6ee374776bb029f1174e1",
                        "name": "CISCO CC",
                        "description": "Standard voice MRD for CISCO CC",
                        "maxRequests": 1,
                        "interruptible": false
                    },
                    "state": "READY",
                    "previousState": "NOT_READY",
                    "stateChangeTime": 1740656530586,
                    "lastReadyStateChangeTime": 1740656530586,
                    "maxAgentTasks": 1
                }
            ],
            "agentLoginTime": 1740656023704
        },
        "correlationId": "cc79cbe2-55b7-4b8f-be10-28e0f6a440fe"
    }
[/code]
