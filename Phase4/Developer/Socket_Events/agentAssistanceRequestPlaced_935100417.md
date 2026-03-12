# CX Knowledgebase : agentAssistanceRequestPlaced

**Event Name**|  agentAssistanceRequestPlaced  
---|---  
**Event Description**|  Event is triggered in response of direct conference and direct transfer request  
**Emitter**|  Agent Manager  
  
**Name**| **Description**  
---|---  
requestAction| type: StringValue could be `transfer` or `conference`  
mode| type: StringValue is `queue`
[code] 
    {
        "requestAction": "transfer",
        "mode": "queue"
    }
[/code]
