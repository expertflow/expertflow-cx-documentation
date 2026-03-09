# CX Knowledgebase : Notification Message

Notification message is used to notify various components within Expertflow CX when [CIM Events](Messages%2C-Events%2C-and-Activities_2528021.html) are emitted.  


Notification message is sent when the following events take place in the system:

Event| Description  
---|---  
SYSTEM_ERROR | System error notifications.  
CHANNEL_SESSION_STARTED | Notification when a new channel session is provisioned on the Channel Manager.  
CHANNEL_SESSION_EXPIRED| When a channel session is expired due to CUSTOMER_INACTIVITY_TIMEOUT on the Channel Manager.  
CHANNEL_SESSION_ENDED| When a channel session is deprovisioned on the Channel Manager.  
AGENT_SUBSCRIBED| When an agent joins a chat. See [Socket Events](Socket-Events_2530728.html) for pull or push notifications.  
AGENT_UNSUBSCRIBED| When an agent leaves a chat. See [Socket Events](Socket-Events_2530728.html) for pull or push notifications.  
CONSULT_TRANSFER|   
  
CONSULT_CONFERENCE| When an agent requests for another agent (from a certain queue) to join the active conversation. See [directConferenceRequest](directConferenceRequest_2531711.html) for details.  
DIRECT_TRANSFER| When an agent wants to leave the conversation and transfer it to another agent (from a certain queue) to takeover the active conversation. See [directTransferRequest](directTransferRequest_2531715.html) for details.  
NO_AGENT_AVAILABLE| When all agents are busy. See [Socket Events](Socket-Events_2530728.html) for pull or push notifications.  
TYPING_STARTED| Connector-Channel Manager two way event  
TYPING_STOPPED| Connector-Channel Manager two way event  
AGENT_RESERVED| When agent is reserved. See [Socket Events](Socket-Events_2530728.html) for pull or push notifications.  
  
**Property**| **Desc.**  
---|---  
type - String - Required| Value = "NOTIFICATION"  
markdownText - String - Optional| Contains custom plain text message.  
notificationType - Enum - Required| Possible values are:

  *     * SYSTEM_ERROR 
    * CHANNEL_SESSION_STARTED
    * CHANNEL_SESSION_EXPIRED
    * CHANNEL_SESSION_ENDED
    * AGENT_SUBSCRIBED
    * AGENT_UNSUBSCRIBED
    * CONSULT_TRANSFER
    * CONSULT_CONFERENCE
    * DIRECT_TRANSFER
    * NO_AGENT_AVAILABLE
    * TYPING_STARTED
    * TYPING_STOPPED
    * AGENT_RESERVED


[code] 
    "body":{
            "type": "NOTIFICATION",
            "markdownText": "Optional",
            "notificationType":"TYPING_STARTED"
        }
    }
[/code]  
  
  

