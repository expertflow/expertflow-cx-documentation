# CX Knowledgebase : conversationParticipant

Object Name| conversationParticipant  
---|---  
Description| This object contains properties of the conversation participant.   
  
  


Parameter| Type| Description  
---|---|---  
`Id REQUIRED`| String| Unique Id of the ChannelSession  
`ParticipantType`| ParticipantType|   
  
`role OPTIONAL`| ParticipantRole|   
  
`participant OPTIONAL`| Participant|   
`joiningTime OPTIONAL`| Timestamp| time when the participant joined the conversation.  
`token REQUIRED`| String|   
  
`conversationId REQUIRED`| String| This is the UUID of the active conversation. Sample:   
`isActive REQUIRED`| Bool| If the channelSession is still active, `isActive` will be `TRUE` else `FALSE`.  
`state REQUIRED`| ConversationParticipantState|   
  
stateChangedOn| Timestamp| Time when the state of the conversation was changed.
