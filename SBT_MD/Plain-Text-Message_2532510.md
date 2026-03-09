# CX Knowledgebase : Plain Text Message

**Description**|  Plain messages are simplest of the message types and are supported by all channels.   
---|---  
  
The body should be in JSON format and include the following properties:

**Property**| **Type**| **Desc.**  
---|---|---  
type REQUIRED | String| Value = "PLAIN"  
markdownText OPTIONAL | String| Contains custom plain text message sent by end user.
[code] 
    "body": {
            "type": "PLAIN",
            "markdownText": "Hi"
        }
[/code]
