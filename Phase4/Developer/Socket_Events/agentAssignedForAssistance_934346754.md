# CX Knowledgebase : agentAssignedForAssistance

**Event Name**|  agentAssignedForAssistance  
---|---  
**Event Description**|  Event is triggered when an agent assigned to the conversation in response of consult transfer or direct transfer  
**Emitter**|  Agent Manager  
  
**Name**| **Description**  
---|---  
conversationId| type: StringId of the conversation  
task| type: String  
type| type: String  
Value could be `consult`, `direct-transfer`
[code] 
    {
        "conversationId": "67c1cb75956d765cfc275754",
        "task": {},
        "type": "consult"
    }
[/code]
