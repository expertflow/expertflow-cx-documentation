# CX Knowledgebase : JoinAsSilentMonitor

**Event Name**|  JoinAsSilentMonitor  
---|---  
**Event Description**|  Event is emitted when supervisor requests to agent manager to join an active conversation of a team member (agent) as a silent member.  
**Emitter**|  Agent Desk  
  
**Name**| **Description**| **Payload Properties**  
---|---|---  
topicParticipant| type: Objectagent details such as id, type, keycloack user authentication fields etc.|   
agentId | type: StringDesc: Id of the supervisor who want to join the chat as a silent monitor|   
channelSession| type: ObjectDesc: contains values of properties related to the session that has been established through a particular channel e.g. web.| 
