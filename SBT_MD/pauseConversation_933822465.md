# CX Knowledgebase : pauseConversation

  


**Event Name**|  pauseConversation  
---|---  
**Event Description**|  Event is emitted when agent requests to agent manager to hold/pause the conversation  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
participantId| type: String ID of the supervisor for whom the event has been emitted|   
conversationId| type: String ID of the conversation for whom the event has been emitted| -  
roomInfo| type: Object| -  
duration| type: timestampFor how much time the conversation could be in on hold state|   
state| type: Stringdesc: "ON_HOLD"| 
[code] 
    {
      "participantId": "65a63fee6a264c3b8edece8a",
      "conversationId": "65b3acaec94e6061e70a0ef5",
      "roomInfo":  {
        "id": "65a625609487373651365bfb",
        "mode": "CONTACT_CENTER"
      },
      duration:"1740715196",
      state: "ON_HOLD"
    }
[/code]  
  
  

