# CX Knowledgebase : wrapupTimerStarted

**Event Name**|  wrapupTimerStarted  
---|---  
**Event Description**|  Event is triggered to start the wrapup timer  
**Emitter**|  Agent Manager  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
task| type: StringwrapupTimerStarted| -  
duration| type: timestamptime in milisecond|   
roomInfo| type: Object|   
conversationId| type: StringId of the conversation|   
statusCode| code: 200| 
[code] 
    {
      "task": "wrapupTimerStarted",
      "duration": "600000",
      "conversationId": "cc76c196-912d-4a47-a9dd-8a2357f54399",
      "roomInfo":  {
        "id": "65a625609487373651365bfb",
        "mode": "CONTACT_CENTER"
      },
      "statusCode": 200  
    }
[/code]
