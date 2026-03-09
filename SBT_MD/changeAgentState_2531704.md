# CX Knowledgebase : changeAgentState

**Event Name**|  changeAgentState  
---|---  
**Event Description**|  When an agent changes its MRD state, state, or logs out from the agent desk, the agent desk requests to agent manager to change its MRD states:

  * ready/not-ready
  * ready/not-ready with or without selecting reason of not ready)
  * log out (with or without selecting reason of logout).

  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
agentId| type: UUID/StringDesc: The ID of the agent for whom state needs to be changed| -  
action| type: StringDesc: describe action to be performed. There are two possible values:

  1. "agentState" 
  2. "agentMRDState"

| -  
state| type: Object, when the action is 'agentState'.type: String, when the action is 'agentMRDState'.Desc: State of the agent and the reason for the state| 

  * When the action is 'agentState'.


  1. name - String - name of the state. Possible values
     1. READY
     2. NOT_READY
     3. LOGOUT
  2. reasonCode - String - reason for change in state
     1. id - String - system generated
     2. name - String - Possible values are: Lunch Break, Out of Office, End of Shift
     3. type - String - Possible values: READY, NOT_READY, LOGOUT


  * When the action is 'agentMRDState' possible values that can be set by the agent are:


  1. READY
  2. NOT_READY

  
mrdId| This field is required when the "action" is "agentMRDState",In the `‘`[ _agentPresence’_](AgentPresence_2530472.html) event there will be a list of all available configured MRDs 'agentMrdStates' with their ids and additional info related to those MRDsMention the id of this particular MRD which needs to update| -  
  
##### **Reason codes:**

The reason codes for NOT_READY and LOGOUT can be defined on unified-admin.  
The reason codes can be obtained from the API,   
GET {{FQDN}}unified-admin/reasons

##### **reasonCode payload**
[code] 
    [
        {
            "name": "Out Of Office",
            "description": "A default log out reason code",
            "type": "LOGOUT",
            "isDeleted": false,
            "createdAt": "2025-10-09T05:25:49.866Z",
            "updatedAt": "2025-10-09T05:25:49.866Z",
            "code": 1,
            "id": "62ffc95cf12b6ccf1594d781"
        },
        {
            "name": "Short Break",
            "description": "A default not ready reason code",
            "type": "NOT_READY",
            "isDeleted": false,
            "createdAt": "2025-10-09T05:25:49.964Z",
            "updatedAt": "2025-10-09T05:25:49.964Z",
            "code": 2,
            "id": "62ffc9e9f12b6ccf1594d88b"
        }
    ]
[/code]

##### **agentState**
[code] 
    {
      "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "action": "agentState",
      "state": {
        "name": "NOT_READY || READY || LOGOUT",
        "reasonCode": {"id":"ef172d24-7b35-4c6d-ada5-41827034d308","name":"Lunch Break || Out of Office || End of Shift","type":"NOT_READY"} 
      } 
    }
[/code]

##### **agentMRDState**
[code] 
    {
    
      "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "action": "agentMRDState",
      "state": "READY || NOT_READY",
      "mrdId": "6233dde8c004592808ad3c0d"
    }
[/code]

**Other Logout Scenarios:**

Users may also be logged out in the following situations:

1)A supervisor logs out agents from the [_Available Agents Detail_](Realtime-Reports-and-Dashboards_2529305.html#Available-Agents-Detail) dashboard.

2)Log out due to [_disconnectivity_](https://expertflow-docs.atlassian.net/wiki/spaces/CIMT/pages/1480949854/Disconnectivity+Logout).

3) Log out due to [_inactivity_](User-Inactivity-Logout_1481802143.html).  
  
For the 1st scnerio, the logout reason payload should be  
`{ name: "FORCED_LOGOUT_BY_SUPERVISOR", description: "Logout by supervisor", type: "LOGOUT", code: 9, id: "62ffc95cf12b6ccf1594d934" }`  
  
for third scnerio the reason code payload should be  
`{ name: "SESSION_TIMEOUT_INACTIVITY", description: "Logout due to no activity on interface", type: "LOGOUT", code: 9, id: "12ffc95cf12b6ccf1594d948" }`
