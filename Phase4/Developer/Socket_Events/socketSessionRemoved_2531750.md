# CX Knowledgebase : socketSessionRemoved

**Event Name**|  socketSessionRemoved  
---|---  
**Event Description**|  Event is triggered when agent switches to another tab. The Agent desk listens to the event and removes the agent from the previous session. Automatically logs the agent out from the previous session.  
**Emitter**|  Agent Manager  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
agentId| type: String| -
[code] 
    {
        "agentId": "cc76c196-912d-4a47-a9dd-8a2357f54399"
    }
[/code]
