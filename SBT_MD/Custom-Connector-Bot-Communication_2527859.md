# CX Knowledgebase : Custom Connector-Bot Communication

The custom Bot Connector sends information to the bot about a particular conversation by transmitting messages and intents. The bot responds by sending a message or bot suggestion or request for action.

Messages are customer generated events in a conversation. Intents are system events intended to convey a specific system activity e.g. CHANNEL_SESSION_STARTED. An intent also directs the bot on how to respond to the sender. Messages, Bot Suggestion and Actions are types of bot responses as a result of the intent. 

**Quick Links**




The request-response structure from the custom bot connector-bot is given below:

## CIM Request

There are two types of request that the custom Bot connector must handle:

  1. **** Message: customer message to be sent to the bot for response/action.
  2. **** Intent:**** intent needs to be sent to the bot for response/action.



### Send a Message to the Bot

Whenever a message request is received by the Bot Framework as CIM event CUSTOMER_MESSAGE, the connector must compose a request body with `type = "message"` indicating user message and not the intent of the message. The code example is given on the right hand side.

  * the request body also contains entities and metadata
    * entities are `NULL` for messages
    * metadata contains CIM Message object. The CIM Message Object can contain any type of message and the format is described [here](CIM-Messages_2530195.html) in detail.



### Send an Intent to the Bot

There are multiple types of intents that needs to be sent to the bot for action. Whenever an intent is sent to the bot by the custom Bot Connector, the request body contains:

  * `type = "intent"` indicating that this contains the intent of the message
  * the request body also contains entities and metadata
    * entities contain the data of the intent e.g. channel session object etc. 
    * metadata for an intent is `NULL`



The following table gives the list of intents. 

Intent name| Intent Data| Fired When  
---|---|---  
CHANNEL_SESSION_STARTED| A channelSession object| A customer starts a conversation on a channel.  
CHANNEL_SESSION_ENDED| A channelSession object| A chat ended on a channel  
END_CONVERSATION| A channelSession object|   
  
AGENT_RESERVED|   
| An agent is reserved and will be added to the conversation  
AGENT_SUBSCRIBED| A CcUser Object| An agent joins a conversation  
AGENT_UNSUBSCRIBED| A CcUser Object| An agent leaves a conversation  
  
**Message Request**
[code] 
    {
        "conversation": "1234",
        "type": "message",
        "message": "Hello how are you",
        "entities": null,
        "metadata": {<CimMessage>}
    }
[/code]

  


  


**Intent Request**
[code] 
    {
      "conversation": "1234",
      "type": "intent",
      "message": "CHANNEL_STARTED_STARTED",
      "entities": {
        "channelSession": {}
       },
      "metadata": null
    }
[/code]

## Bot Response 

The custom Bot Connector should expect three types of responses from the bot at most:

  1. messages - Message types are described [here](CIM-Messages_2530195.html) in detail
  2. bot suggestion - is also a type of message
  3. action - these are described in the table Bot Actions



In all of the three cases, following is the response structure. Examples are shown in the code block on the right:

Payload Property| Type| Description  
---|---|---  
intent OPTIONAL| object| It contains the following information:

  1. name - String - name of the event/intent.
  2. confidence - Numeric - specifies confidence level i.e.how confident the bot is about its understanding of message. For system events the confidence will be 1.0.

  
mode OPTIONAL| String| The mode specifies whether the bot is primary or secondary (message vs. suggestion)   
body REQUIRED| Object| It contains the following information:

  1. type - String - specifies type of message e.g. Plain, Video or Action etc. The [message types](CIM-Messages_2530195.html) are described in detail.
  2. markdownText - String - Any text from the agent/customer
  3. name - String - Name of event e.g. FIND_AGENT, END_CONVERSATION. The actions are listed below in the table.

  
  
## Bot Actions

Following are the actions sent by the bot to the custom connector:

Action name| Action Data  
---|---  
END_CONVERSATION|   
  
FIND_AGENT|   
  
ASSIGN_AGENT|   
  
~~CUSTOMER_RESPONSE_TIMEOUT~~|   
  
~~AGENT_RESPONSE_TIMEOUT~~|   
  
~~END_CHANNEL_SESSION~~|   
  
~~CHANNEL_SESSION_EXPIRED~~|   
  
~~ACCEPT_TIMEOUT~~|   
  
CANCEL_RESOURCE| 

  * reasonCode - CANCELLED

  
REVOKE_REQUEST| 

  * reasonCode - CANCELLED

  
  
**Response: Message\Suggestion**
[code] 
    {
     "intent": {
        "name": "Greet",
        "confidence": 0.92
      },
      "mode": "message | suggestion",
       "body": {
         "type": "PLAIN",
         "markdownText": "Welcome"
        }
    }
[/code]

**Response: Action**
[code] 
    {
      "intent": {
        "name": "TALK_TO_AGENT",
        "confidence": 0.92
      },
      "mode": null,
      "body": {
        "type": "ACTION",
        "markdownText": "",
        "name": "FIND_AGENT",
        "data": {}
      }
    }
[/code]
