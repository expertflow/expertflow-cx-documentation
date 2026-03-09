# CX Knowledgebase : JoinAsBargin

  


**Event Name**|  JoinAsBargin  
---|---  
**Event Description**|  Event is emitted when supervisor requests to agent manager to barge-in an active conversation instead of being a silent member.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
participantId| type: String ID of the supervisor for whom the event has been emitted|   
conversationId| type: String ID of the conversation for whom the event has been emitted| -  
roomInfo| type: Object| -
[code] 
    {
      "participantId": "65a63fee6a264c3b8edece8a",
      "conversationId": "65b3acaec94e6061e70a0ef5",
      "roomInfo":  {
        "id": "65a625609487373651365bfb",
        "mode": "CONTACT_CENTER"
      }
    }
[/code]  
  
  

