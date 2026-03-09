# CX Knowledgebase : Messages, Events, and Activities

## Room 

A Room is the container of all CIMEvents and CIMActivities for tracking a Customer Journey throughout the Customer lifetime. 

## Actor

An Actor is a Customer, a Human Agent, an AI Agent, a Supervisor, or an Application performing CIMEvents. 

## CIMMessage

CX-Core platform communicates with its clients as CIMMessage. A CIMMessage carries CIMEvent. 

## CIMEvents

CIMEvent is the smallest amount of considerable change in the source application from the perspective of an Interaction. CIMEvents are always stateless. CX-Core Client is an application that uses CX-Core for storing and publishing events to other applications of interest. Any type and number of applications may register with CX-Core for publishing, subscribing, and reporting of CIMEvents. 

A CIMEvent Subscriber may use CIMEvents for: 

  * Audit trail

  * Agent performance and customer journey tracking analytics

  * Service levels, customer channels and Bot Performance Monitoring 

  * For customer interaction such as consolidate interesting events into Activities for agent serving customers

  * For agent productivity such as capturing agent actions for optimizing workforce

  * For Bot retraining i.e. use CX data to retrain bot via supervised/semi-supervised learning




## CIMActivity

A CIMActivity is an aggregation of one or more CIMEvents. 

ChannelSessions are always stateful. They may or may not be interactive. For example, a call is an interactive session and the chat is a non-interactive session. 

A call leg is an activity and the call is a session. 

Stateful| When it's important to monitor and keep track of the state of a session  
---|---  
Interactive| When a session cannot last if any of the participants leave the session.   
  
The following table provides a list of few possible scenarios that can be classified as activities:

**Activity**| **Description**| **Actor**  
---|---|---  
CIM Messages| CIM Messages are of many types such as plain, video etc. Messages are described in detail [here](CIM-Messages_2530195.html).| Customer, CC User, botParticipant, App  
Agent call| Call leg of a voice call handled by an agent| Agent  
IVR activity| IVR system initiates IVR in an on-going conversation.| App  
Call recording link| A call recording app sends a call recording link for a recently completed call.| App  
WrapUp Message| Wrap-up activity is performed on an active conversation. It is a type of structured message and described [here](WrapUp-Message_2532492.html).| Agent  
Survey question| Survey sent in a conversation by campaign manager/3rd-party app.| App  
Customer-conversation Ilink| Link customer to a conversation| Agent, App  
Whisper Message| send whisper message| Agent, App  
Bot suggestion| Bot sends a suggestion in a conversation| Bot  
Recording/Transcript Link| Generate recording link or transcript URL| App (Recording Solution, CCM)  
Push Schedule activity| Push schedule activity to CX| App  
Push survey application| A survey application pushes customer satisfaction survey score to the conversation| App  
Push Customer’s traversal tree information| A self-service system such as IVR pushes customer's traversal tree information to the conversation (the different menu options that the customer selected on the IVR)| App  
  
#### 3rd party voice call scenario

See the finalized flow of Voice call events and related use cases in [Mapping CTI events on CIM](http://expertflow-docs.atlassian.net/wiki/spaces/CIMT/pages/1311589/Mapping+CTI+events+on+CIM).

## Examples of Activities

An activity may be updated based on reactions, modify-activity events, and delivery notifications. Examples: 

  * a customer message

    * REACTION bot-suggestion is a reaction to the customer message

    * MODIFY-ACTIVITY edit/delete-message-event - the customer chose to change or delete the message 

    * DELIVERY-NOTIFICATION when the agent has read the message. The agent-manager will send this delivery-notification.

  * an agent message

    * DELIVERY-NOTIFICATION received message delivery notifications

    * REACTION customer's reactions to the message in the form of an emoji

    * REACTION supervisor's reaction to flag the response as rude, inappropriate, misleading, excellent - based on defined custom flags

  * a bot message

    * DELIVERY-NOTIFICATION received message delivery notifications

    * REACTION customer's reactions to the message in the form of an emoji

    * REACTION Bot trainer's reaction to flag a response as inappropriate - based on defined custom flags

  * a structured message sent by the bot or the agent - selected from bug suggestions

    * REACTION one ore more customer responses to the structured message 

  * a campaign message - the campaign manager sent an outbound campaign message 

    * DELIVERY-NOTIFICATION received message delivery notifications

    * REACTION customer's reactions to the message in the form of flags - acknowledged / inappropriate / annoying

  * an IVR activity - the IVR application sent an activity for an ongoing call.

  * an agent call leg - a call leg of a voice call handled by an agent

  * a call recording link received - the call recording application sent a call recording link for a recently completed call. The event must have a call id.

  * a note - A note sent by an actor - this may or may not have a reference to a channelSession or a conversation ID. 

  * wrap-up - a wrap-up activity performed by the agent on a conversation / session. The event must have the session or a conversation identifier.

  * a survey question - the campaign manager sent a survey question as a **structured message**

    * REACTION customer's response to the survey question




### Types of CIMEvents

The types of CIMEvents are as follows:

**Type**| **Description**  
---|---  
ACTIVITY | An event is considered of type activity if it carries primary action performed by the actors such as customer, agent, bot or a third-party app. For example, all customer, agent and bot messages are encapsulated in events of type ACTIVITY.  
SUGGESTION| This type carries all events of type bot suggestions.  
Message| This event type carries internal communication . All internal and whisper communication among agents and bots.  
Notification| This event type carries all system notifications including REACTIONS or MODIFY EVENT or DELIVERY NOTIFICATION  
  
### Conversation Events

The list of all CIMEvents and their payloads are given as follows:

**Event name**| **Type**| **Description**| **Channel-Manager**| **Bot-Framework**| **Agent-Manager**| **Conversation Manager**| **Event Payload**  
---|---|---|---|---|---|---|---  
CUSTOMER_MESSAGE| ACTIVITYCONVERSATION_EVENT| When the system receives a message from a customer, this event is fired.| Publisher| Consumer.Cache this event in Redis.| ConsumerSend this event to the unified agent over the socket.| |   
AGENT_MESSAGE | ACTIVITY| When the system receives a message from an agent, this event is fired| Consumer| Consumer| Publisher| | [CIMMessage](CIM-Messages_2530195.html)  
BOT_MESSAGE| ACTIVITY| When the BotFramework receives a message from a bot, this event is fired| Consumer| Publisher| Consumer| | [CIMMessage](CIM-Messages_2530195.html)  
BOT_SUGGESTION | SUGGESTION| When the BotFramework receives a message from a bot, this event is fired| NA| Publisher| Consumer| | SuggestionMessage  
WHISPER_MESSAGE | MESSAGE| When the AgentManager receives a message from an agent, this event is fired| NA| NA| Publisher| | [Whisper Message](Whisper-Message_2529350.html)  
CHANNEL_SESSION_STARTED | NOTIFICATION| When a customer presence is detected on a channel, Channel Manager fires this event.| Publisher| Consumer| NA| | [ChannelSession Object](channelSession_2527365.html)  
CHANNEL_SESSION_ENDED | NOTIFICATION| When:

  * Customer closes/ends conversation
  * Customer Inactivity timer expires and the Controller instructs to end the channel session by sending REMOVE_CHANNEL_SESSION event

this event is published to indicate that customer session has ended| | Consumer| | | [ChannelSession Object](channelSession_2527365.html)  
CHANNEL_SESSION_EXPIRED| NOTIFICATION| When:

  * Customer Inactivity timer expires and the Controller instructs to end the channel session by sending REMOVE_CHANNEL_SESSION event

this event is published to indicate that customer session has ended| | Publisher| | | ChannelSession  
AGENT_RESERVED | NOTIFICATION| | NA| Consumer| NA| | 
[code] 
    {
    	"topicId": "<String>",
    	"ccUser": "<CcUser>"
    }
[/code]

  
  
EWT_MESSAGE FUTURE | ACTIVITY|   
| | | | |   
  
AGENT_SUBSCRIBED| NOTIFICATION|   
| | Consumer| Publisher| | 
[code] 
    {
    	"agentParticipant": {},
    	"reason": ""
    }
[/code]

  
  
AGENT_UNSUBSCRIBED | NOTIFICATION|   
| | Consumer| Publisher| | 
[code] 
    {
    	"agentParticipant": {},
    	"reason": ""
    }
[/code]

  
  
AGENT_RESPONSE_TIMEOUT | NOTIFICATION| When the agent response SLA is expired| | | | |   
  
BOT_TIMEOUT | NOTIFICATION| **BotFramework** fires this if and when the bot doesn't respond timely in response to a customer message.| | Publisher| | | String  
BOT_NOT_AVAILABLE | NOTIFICATION| not implemented yet| | | | |   
  
CUSTOMER_RESPONSE_TIMEOUT | NOTIFICATION|   
| | | | |   
  
TOPIC_STATE_CHANGED| NOTIFICATION|   
| | Publisher| | | CustomerTopic  
ASSOCIATED_CUSTOMER_CHANGED| NOTIFICATION|   
| | | | |   
  
MESSAGE_DELIVERY_NOTIFICATION| NOTIFICATION|   
| | | | |   
  
WRAPUP_APPLIED ?| ACTIVITY|   
| | | | |   
  
ACCEPT_TIMEOUT| NOTIFICATION|   
| | | | |   
  
TASK_STATE_CHANGED| NOTIFICATION|   
| | | | | TaskDto  
REVOKE_RESOURCE | NOTIFICATION|   
| NA| Publisher| Consumer| | 
[code] 
    {
    	"reasonCode": "<String>" 
    }
[/code]

  
  
CONVERSATION_DATA_CHANGED| NOTIFICATION|   
| | Publisher| | | Map<String, String> ... (any Key-value pairs)  
PARTICIPANT_ROLE_CHANGED| NOTIFICATION|   
| Consumer| | Consumer| | 
[code] 
    {
        "conversationParticipant {},
        "metadata": {} // (any)
    }
[/code]

  
  
NO_AGENT_AVAILABLE| NOTIFICATION| | NA| Consumer| NA| |   
  
ACTION_MESSAGE | MESSAGE|   
| NA| Publisher| NA| | CimMessage Object  
CALL_LEG_ENDED| ACTIVITY|   
| NA| Consumer| NA| | [CIMMessage](CIM-Messages_2530195.html)  
AGENT_OUTBOUND| ACTIVITY|   
| | | | |   
  
TASK_ENQUEUED| ACTIVITY|   
| | | | |   
  
MESSAGE_DELIVERY_NOTIFICATION| NOTIFICATION| Agent_manager fires it when the agent has read the customer message| Consumer| | Publisher| | [CIMMessage](CIM-Messages_2530195.html)  
THIRD_PARTY_ACTIVITY| NOTIFICATION|   
| Consumer| | Consumer| | [CIMMessage](CIM-Messages_2530195.html)  
CHANNEL_SESSION_DATA_UPDATED | NOTIFICATION| CCM fire it when the channelSession data is update| Publisher| | | | ChannelSession Object  
CALL_HOLD| NOTIFICATION| CCM fires it when it receives this from Agent Desk on hold of a voice call| Publisher| | | | 
[code] 
    {
        ...
        "name": "CALL_HOLD",
        "type": "NOTIFICATION",
        "eventEmitter": {
          "type": "AGENT",
          ...
        },
        "data": {
          ... // CimMessage of VOICE type having dialog and call details
        }
        ...
    }
[/code]  
  
CALL_RESUME| NOTIFICATION| CCM fires it when it receives this from Agent Desk on resume of a voice call| Publisher| | | | 
[code] 
    {
        ...
        "name": "CALL_RESUME",
        "type": "NOTIFICATION",
        "eventEmitter": {
          "type": "AGENT",
          ...
        },
        "data": {
          ... // CimMessage of VOICE type having dialog and call details
        }
        ...
    }
[/code]  
  
MRD_INTERRUPTED| NOTIFICATION| Routing Engine fires it when an MRD is interrupted. Conversation Manager consumes this event| N/A| N/A| N/A| | 
[code] 
    {
        ...
        "name": "MRD_INTERRUPTED",
        "type": "NOTIFICATION",
        "eventEmitter": {
          "type": "SYSTEM",
          ...
        },
        "data": {
          "mrdId": "123",
          "agentId": "123",
          "conversations": []  // list of convrsation IDs
        }
        ...
    }
[/code]  
  
AGENT_SLA_STARTED| NOTIFICATION| Conversation Monitor publishes this event when it starts the Agent Response Timer. It is published in following cases:

  * When it starts the agent sla timer on each threshold (threshold can be one or more than one)
  * When the agent subscribes the conversation.
  * When customer sends a message
  * When conversation resumes.

| | | | |   
AGENT_SLA_STOPPED| NOTIFICATION| Conversation Monitor publishes this event when it stops the Agent Response Timer. It is published in following cases:

  * When agent sends a message
  * When the agent unsubscribes the conversation and no more agent exists.
  * When channel session gets ended and no more agent exist in conversation.
  * When voice channel starts for the same customer on top of a non voice channel.
  * When all agents are in WRAP_UP role.
  * When conversation is put on hold.

| | | | |   
FIND_AGENT| NOTIFICATION| Whenever any component wants to find an agent for a conversation, the `FIND_AGENT` event is published in the following scenarios:

  1. **From CCM** :  
Upon receiving the `ASSIGN_RESOURCE_REQUESTED` intent, the CCM component performs validation on the received payload. After validation, it constructs the `FindAgent` DTO and publishes the `FIND_AGENT` event.
  2. **From Bot Framework** :  
When a bot is engaged with the customer and the customer requests to speak with an agent, the Rasa bot dispatches a `FIND_AGENT` action. This action contains empty data by default but may contain some data as per the defined payload of `FIND_AGENT` event. Upon receiving this action, the Bot Framework populates the `FIND_AGENT` DTO and publishes the `FIND_AGENT` event accordingly.

| Publisher| Publisher| N/A| Consumer

  * The **Conversation Manager** consumes the `FIND_AGENT` event and forwards it to the **Controller Training** module. The controller then performs the necessary processing as defined in this [document](https://expertflow-docs.atlassian.net/wiki/x/RYwm) and sends the response back to the Conversation Manager in the form of a `FIND_AGENT` action containing the required data.

| 
[code] 
    {
        "name": "FIND_AGENT",
        "type": "NOTIFICATION",
        "eventEmitter": {},
        "data": {
            "queue": {
                "type": "ID",
                "value": "123456789"
            },
            "requestType": {
                "direction": "INBOUND",  // Can be INBOUND or OUTBOUND etc
                "mode": "AGENT",         // Can be AGENT or QUEUE
                "metadata": {}           // Additional metadata related to the request
            },
            "additionalDetails": {
                "priority": 1,           // Example: priority of the request
            }
        }
    }
[/code]

The `additionalDetails` field can hold flexible information that doesn’t belong to the `queue` or `requestType` fields. Everything other than `queue` or `requestType` fields will be part of this.
