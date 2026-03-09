# CX Knowledgebase : Email Message

**Description**|  This message is used to send an email.  
---|---  
  
The body should be in JSON format and include the following properties:

**Property**| **Type**| **Desc.**  
---|---|---  
type REQUIRED | String| Value = "EMAIL"  
subject OPTIONAL | String|   
from REQUIRED | String|   
replyTo REQUIRED | List{String}|   
receivingDate REQUIRED | Long|   
htmlBody| String|   
recipientsTo| List{String}|   
recipientsCc| List{String}|   
recipientsBcc| List{String}|   
emailThreads| List{String}|   
attachments| List{Attachment}|   
additionalDetails| JsonNode| 
