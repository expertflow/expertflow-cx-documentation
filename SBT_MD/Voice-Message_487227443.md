# CX Knowledgebase : Voice Message

**Description**|  The user can send audio messages. through this message type  
---|---  
  
The body should be in JSON format and include the following properties:

**Property**| **Type**| **Desc.**  
---|---|---  
type REQUIRED | String| Value = "VOICE"  
callId REQUIRED | String|   
leg REQUIRED | String|   
reasonCode| String|   
additionalDetail| object{String}| 
