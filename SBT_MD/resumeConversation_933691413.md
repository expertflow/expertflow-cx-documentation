# CX Knowledgebase : resumeConversation

  
  
  
**Event Name**|  resumeConversation  
---|---  
**Event Description**|  Event is emitted when agent requests to agent manager to resume the conversation  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
participantId| type: String ID of the supervisor for whom the event has been emitted|   
conversationId| type: String ID of the conversation for whom the event has been emitted| -  
roomInfo| type: Object| -  
state| type: Stringdesc: "ACTIVE"| 
[code] 
    {
      "participantId": "65a63fee6a264c3b8edece8a",
      "conversationId": "65b3acaec94e6061e70a0ef5",
      "roomInfo":  {
        "id": "65a625609487373651365bfb",
        "mode": "CONTACT_CENTER"
      },
      state: "ACTIVE"
    }
[/code]  
  
  

