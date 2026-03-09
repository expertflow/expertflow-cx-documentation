# CX Knowledgebase : channelSession

Object Name| channelSession  
---|---  
Description| This object contains properties related to the session that has been established through a particular channel e.g. web, voice etc. Each customer conversing with an agent/bot will have their own channel session.  
  
  


Parameter| Type| Description  
---|---|---  
`Id REQUIRED`| String| Unique Id of the ChannelSession  
`participantType REQUIRED`| String| Type of participant in the channel session. See [ParticipantType](ParticipantType_2525473.html) for details.  
`channel REQUIRED`| Channel| Specifies the channel for the particular session. See [Channel](Channel_2525261.html) for details.  
`customer OPTIONAL`| Customer| See [customer object](customer-object_2526154.html) for details.  
`customerSuggestions OPTIONAL`| List| Provides list of customer suggestions  
`channelData REQUIRED`| ChannelData| Specifies the data for the channel. This data is unique to each channel. See [channelData](channelData_2528008.html) for details.  
`latestIntent OPTIONAL`| String| Intents are system events to inform the conversational bot to take action on the intent. The channelSession object will contain the latest intent for the session e.g. CHANNEL_SESSION_STARTED.  
`customerPresence UNDEFINED`| Object|   
  
`isActive OPTIONAL`| Bool| If the channelSession is still active,` isActive` will be `TRUE` else `FALSE`.  
`conversationId OPTIONAL`| UUID| This is the ID of the conversation to which this channel session belongs.   
`state REQUIRED`| ChannelSessionState| See [channelSessionState](channelSessionState_2527123.html) for details.
