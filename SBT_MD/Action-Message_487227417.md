# CX Knowledgebase : Action Message

**Description**|  Bot can send Action message to instruct the system to perform a specific action e.g. FIND_AGENT, ASSIGN_AGENT etc. See [this page](Custom-Connector-Bot-Communication_2527859.html) for details.  
---|---  
  
The body should be in JSON format and include the following properties:

**Property**| **Desc.**  
---|---  
type| Value = "ACTION"  
name - String - Required| name of the action  
data - Map - Required| Data of each action is given below in the table.  
  
**Action Name**| **Data**  
---|---  
ASSIGN_AGENT|   
ASSIGN_BOT|   
CHANGE_PARTICIPANT_ROLE|   
END_CONVERSATION|   
FIND_AGENT|   
REMOVE_ALL_AGENTS|   
REMOVE_CHANNEL_SESSION|   
REVOKE_BOT|   
REVOKE_RESOURCE|   
UPDATE_CONVERSATION_DATA| 
