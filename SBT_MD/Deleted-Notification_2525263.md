# CX Knowledgebase : Deleted Notification

Deleted Notification message is used to indicate that the message has been deleted by the system.

**Property**| **Desc.**  
---|---  
type - String - Required| Value = "DELETEDNOTIFICATION"  
messageId - String - Required| ID of the message for which deleted notification is being sent.  
timestamp - String - Optional| Contains the timestamp at which the message was deleted.
[code] 
    "body": {
            "type": "DELETEDNOTIFICATION",
            "messageId": "abc12345",
            "timestamp":"123456"
        }
[/code]
