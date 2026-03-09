# CX Knowledgebase : Delivery Notification Message

Delivery Notification is used to indicate that the message has been processed by the system. It has the following states:  
  
  * DELIVERED - has been delivered to the recipient (agent or customer).

  * CONNECTED - mainly used for voice cases when a call is connected to a recipient

  * READ - has been read by the recipient (agent or customer).

  * FAILED - delivery has failed. There are reason codes associated with each failure.


The body should be in JSON format and include the following properties:

**Property**| **Desc.**  
---|---  
type - String - Required| Value = "DELIVERYNOTIFICATION"  
messageId - String - Required| ID of the message for which delivery notification is being sent.  
markdownText - String - Optional| Contains custom plain text message.  
status - Enum - Required| Possible Values:

  * Delivered
  * Connected
  * Read
  * Failed

  
reasonCode - String - Required| 

  * Delivered - 200
  * Read - 200
  * Failed:
    * 400 - bad request 
    * 404 - this channel is undefined and unregistered on Unified Admin
    * 500 - internal system error

  
  
  

[code] 
    "body": {
            "type": "DELIVERYNOTIFICATION",
            "markdownText": "Optional",
            "messageId": "abc12345",
            "status":"READ",
            "reasonCode":200
        }
[/code]

  


  


  

