# CX Knowledgebase : Message Header

The parameters present in Message Header are given as follows:

**Parameter**| **Description**| **Type**  
---|---|---  
**sender** REQUIRED**** for inbound and outbound messages| It contains sender information. Helps to identify sender type and role e.g. Agent or Customer. Properties are given as follow:

  * id - String - unique identifier of the sender - Required
  * type - Enum - sender type with options: agent/bot/connector/app/system - Required
  * senderName - String - Required
  * additionalDetail - Map (String, Object) - Optional

| Sender object.  
[**channelData**](channelData_2528008.html) REQUIRED**** for outbound messages| The details of the object are given [here](channelData_2528008.html).| ChannelData class object  
**language** FOR FUTURE USE| This field is not in use as yet but can be used in future. | LanguageCode class object  
**timestamp** OPTIONAL| The timestamp at which the message was sent by client.| Timestamp  
**securityInfo** FOR FUTURE USE | -| MessageSecurity class object  
**stamps** FOR FUTURE USE | -| List (String)  
**Intent** OPTIONAL for conversation bot and bot connector only.| Intents specify the purpose of the message. It defines what client wants to achieve from message. In case of the normal messages, intent is NULL. E.g. plain, text, structured messages etc. The types of intents are given [here](Intent_478347287.html).| Enum  
**Entities** OPTIONAL****|  Entities are the data of intent. e.g. channel session object etc. | Map (string or object)  
**channelsessionId** OPTIONAL**** FOR INTERNAL USE ONLY | System generated ID set by CX to manage and track the session internally.| UUID  
**conversationId** REQUIRED**** FOR INTERNAL USE ONLY | System generated ID set by CX to manage the conversation. This | String  
**schedulingMetaData** OPTIONAL | Applicable for campaigns messages as it contains metadata for scheduled campaigns.| Map (string or object)  
**customer** REQUIRED**** for outbound messagesOPTIONAL for inbound messages| Details of this object are given [here](customer-object_2526154.html).| Customer class object  
**room Id**|  It is optional for contact center rooms. Required for private rooms. Client specifies room IDs for private rooms.| String  
**providerMessageId** OPTIONAL| See [Intent page ](Intent_478347287.html)for REPLY_TO intent.| String  
**originalMessageId** OPTIONAL| ID of a message within a conversation. See [Intent page ](Intent_478347287.html)for REPLY_TO intent.| String
