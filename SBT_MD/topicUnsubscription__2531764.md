# CX Knowledgebase : topicUnsubscription_

**Event Name**|  topicUnsubscription  
---|---  
**Event Description**|  Agent requests to agent manager for the topic unsubscription by emitting this event.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
conversationId| type: StringID of the conversation for unsubscription|   
agentId| type: String ID of the agent for whom the event has been emitted| -  
roomInfo| type: Object| 
[code] 
    {
        "conversationId": "261c271a-58e6-4571-9d25-77ad26d745d6",
        "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
        "roomInfo":  {
          "id": "65a625609487373651365bfb",
          "mode": "CONTACT_CENTER"
        }
    }
[/code]
