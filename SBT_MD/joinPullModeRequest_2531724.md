# CX Knowledgebase : joinPullModeRequest

**Event Name**|  joinPullModeRequest  
---|---  
**Event Description**|  Event is emitted when an agent joins a chat, the agent desk emits an event of joinPullModeRequest to the agent manager, agent manager listens to the event and successfully joins the chat for the agent.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
topicParticipant| type: Object|   
agentId| type: String ID of the agent for whom the event has been emitted| -  
channelSession| type: Object contains values of properties related to the session that has been established through a particular channel e.g. web.|   
requestId| type: StringID of the task subscribed by the agent | -
[code] 
    {
      "topicParticipant": {},
      "agentId": "a13a49f4-7ec6-436b-91b0-0fd1be205799",
      "channelSession": {},
      "requestId": "a13a49f4-7ec6-436b-91b0-0fd1be205799"
    }
[/code]
