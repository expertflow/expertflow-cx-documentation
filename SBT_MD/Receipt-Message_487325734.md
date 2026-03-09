# CX Knowledgebase : Receipt Message

**Description**|  This message is used to contain the message delivery receipt  
---|---  
  
The body should be in JSON format and include the following properties:

**Property**| **Type**| **Desc.**  
---|---|---  
type REQUIRED | String| Value = "RECEIPT"  
REQUIRED | Object| The object is described [here](carouselMessageType_487948327.html).  
REQUIRED | Map| Data of each action is given below in the table.
