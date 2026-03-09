# CX Knowledgebase : Agent Desk Developer Guide

## Purpose  
  
The purpose of this document is to describe how to build custom Agent Desk using Agent Manager integration interfaces. Agent Manager is used to manage customer-support conversations with the customers. 

## Audience

The document is intended for developers with sound understanding of event-driven Javascript including SocketIO libraries.

## Technical Overview

The following diagram describes the technical communication infrastructure between the Agent Manager and custom Agent Desk. The customers can send messages to the customized Agent Desk from multiple mediums (web browser, mobile app, and desktop).

  * The custom Agent Desk will communicate with the Agent Manager using REST APIs. A 3rd-party notification service, Firebase Cloud Messaging platform (FCM) will push the messages from Agent Manager to the custom Agent Desk. The customized Agent Desk should implement the APIs for receiving the notifications sent by FCM.

  * To listen to the events from Agent Manager, customized Agent Desk must implement the listener events. The message format will be SocketIO. 




### Assumptions and Constraints

The integration of mediums (web browser, mobile app, and desktop) with the Agent interface is left at the developer's discretion and not included in this guide.

## Getting Started

\- Establish the connection between Agent-interface and Agent Manager for the exchange of messages:

  * Agent Manager server URL - This is the URL that is used to make REST API calls and set up a SocketIO connection. 

    * REST API URL - https://{`AGENT_MANANGER`}/

    * SockeIO URL - https://{`AGENT_MANANGER`}/




The details of the events are mentioned in [Socket Events](Socket-Events_2530728.html).

## Use cases

The use cases for custom Agent Desk are explained in detail below:

### 1\. Establish Connection with Agent Manager

#### To login to Agent Manager

For the agent to login to the Agent Manager, it is required to:

  1. Initiate a post request to the agent manager as given in the [User Login API](https://api.expertflow.com/#25dd7bff-9418-4d7d-a4f5-fa58865741a7) in Postman. A successful response will provide the agent with the keyCloack user details.

  2. Make the [socket.io](http://socket.io) handshaking with the agent manager as given bellow in the code block. The FQDN contains the agent-manager address _._

     1. on successful creation of the connection, the socket library will receive a _‘connect’_ event

     2. on failure, the _‘connect_error’_ event is received with the error details

**Note** : The version of [socket.io](http://socket.io)-client should be 4.4.0.




##### **Agent Login**
[code] 
    import { io } from "socket.io-client";     
    let uri = {{FQDN}};     
    let origin = new URL(uri).origin;    
    let path = new URL(uri).pathname;     
    let socket = io(origin, { path: path == "/" ? "" : path + "/socket.io", auth: {agent: {{keycloak_User}}, fcm: ""}});
[/code]

After login with the agent manager, the agent will receive an event called [_‘agentPresence’_](agentPresence__2531701.html). 

### 2\. Change Agent States

#### a. To change parent state of agent

For changing the agent’s parent state, custom Agent Desk should emit the event called [_‘changeAgentState’_](changeAgentState_2531704.html)`:`

  * The `‘action’ `parameter should be named _‘_`agentState` _’_ and the ‘`state.name`’ parameter can have the possible values ‘`READY`’, ‘`NOT_READY`’, or ‘`LOGOUT`’

  * With the state `‘READY’` the reasonCode must be set to `'null'` but for the state` ‘LOGOUT’ `and `‘NOT_READY’` the reasonCode can be set with some additional details as mentioned in the object but can be set to '`null`' too.




#### b. To change MRD state of agent

For changing the agent’s mrd state, custom Agent Desk should emit the event called, [_‘changeAgentState’_](changeAgentState_2531704.html):

  * The `‘action’` __ parameter should be named `‘agentMRDState’` _._




### 3\. Agent Presence Event

On every request of changing the state, the Agent Manager will emit an event called, [_’agentPresence’_](agentPresence__2531701.html)`:`

The _‘action’_ parameter in this object has two possible values 

  1. AGENT_STATE_CHANGED ⇒ When the state is successfully changed

  2. AGENT_STATE_UNCHANGED => When the state can’t be changed at that time




**NOTE** : In order to set the MRD state ‘`READY`’, the Agent’s parent state should be ‘`READY`’ first and when the Agent’s parent state is set to `‘NOT_READY`’ then all the MRD states would automatically be set to ‘`NOT_READY`’.

### 4\. Push Mode Tasks

#### a. Request received by custom Agent Desk

Whenever there is a task request initiated from the routing engine, the custom Agent desk will receive an event called, [_’_](changeAgentState_2531704.html)[ _taskRequest_](taskRequest_2531754.html)[ _’_](changeAgentState_2531704.html):

  * This task state is set to _‘_`RESERVED` _’_ at that time for the agent and a RONA timer is initiated for that request. 

  * If the task is accepted within the RONA time the task state is set to '`ACTIVE'`__ else the task state is set to '`CLOSED` _'_ with reason RONA and the agent manager will emit the event [_‘revokeTask_](revokeTask_2531748.html)[ _’_](changeAgentState_2531704.html).




#### b. To accept a task

In order to accept the task, the custom Agent desk should emit an event called, [_’_](changeAgentState_2531704.html)[ _topicSubscription_](topicSubscription_2531760.html)[ _’_](changeAgentState_2531704.html):

  * On accepting the request, the agent manager will emit an event called, [_’_](changeAgentState_2531704.html)[ _onTopicData_](onTopicData_2531736.html)[ _’_](changeAgentState_2531704.html) which contains all the possible information related to this conversation.




### 5\. Emit [Socket.io](http://Socket.io) Events (Custom Agent Desk - Agent Manager)

Several types of events are emitted from Custom Agent Desk to Agent Manager and vice versa. The page [Socket Events](Socket-Events_2530728.html) enlist all possible event types and their descriptions.

### 6\. Emit CIM Events 

There are two types of CIM Events that the Agent Desk must handle - Messages and System Events. 

#### Exchange Messages in a Conversation

Whenever a message is sent by the agent or system activity is generated, the custom Agent desk should emit an event called, ['_publishCimEvent_ ’](publishCimEvent_2531739.html):

  * On accepting the request, the agent manager will emit an event called, [_‘onCimEvent’_](onCimEvent_2531728.html) _._

  * Multiple types of messages should be supported by Agent Desk. The types of messages are described here in [CIM Messages](CIM-Messages_2530195.html).




#### Reply to a Specific Message

In case of reply to any message in the conversation, the object "data" contains the ID of a previous message you are replying to. In case of a new message, a unique ID is generated. 

For example:

##### **publishCimEvent**
[code] 
    "data": {            
      "id": "142ad3a6-6ab8-4cf7-9553-959e2c3605c2" //reply to an existing message 
      "header": { ......... } 
      "body": { .............. } 
    }
[/code]

#### Edit a Specific Message

In case of edit any message in the conversation, the object "header" in data contains the `intent` UPDATE, and ID of a original message you are editing. Only text messages that are part of ongoing conversation are supported to edit.

For example:

##### **publishCimEvent**
[code] 
    "data": {            
      "id": "142ad3a6-6ab8-4cf7-9553-959e2c3605c2"
      "header": {
        ...
        "intent": "UPDATE",
        "originalMessageId": "reference id of original message"
      },
      "body": { .............. } 
    }
[/code]

#### Handle System Events

Whenever a system activity takes place, the custom Agent desk should emit an event called, ['_publishCimEvent_ ’](publishCimEvent_2531739.html):

  * On accepting the request, the agent manager will emit an event called, [_‘onCimEvent’_](onCimEvent_2531728.html) _._

  * There are several types of system activities to be handled. These activities are described here in [CIM Activities](https://expertflow-docs.atlassian.net/wiki/spaces/EF/pages/1284998/CIM+Activities).




### **7\. Reroute Chat Requests to Queues or a specific agent**

An agent can request to reroute the chats in two cases:

a. Conference Request - whenever an agent wants to add another agent to the conference.

b. Transfer Request - whenever an agent wants to transfer the conversation to another agent.

c. Consult Request - whenever an agent wants to add another agent in the conversation for consultation without notifying the customer.

#### Conference Request

Whenever an agent wants to request another agent to the ongoing/active conversation and selects a specific queue or an agent to make a conference request, the custom Agent Desk should emit an event called, '[directConferenceRequest](directConferenceRequest_2531711.html)':

  * the Routing Engine will choose an available agent (if any) in case of queue request and offer this request to that agent. Once the other agent accepts that request, that agent will become a participant in the conversation.

  * In case the other agent does not accept the request and RONA occurs, the Routing Engine will continue to find another available agent until TTL time expires.




#### Transfer Request

Whenever an agent wants to completely transfer the ongoing/active conversation to another agent and selects a specific queue or agent to make the transfer request, the custom Agent Desk should emit an event called, '[directTransferRequest](directTransferRequest_2531715.html)':

  * after making the transfer request that agent will no longer be the part of that conversation. The Routing engine will choose an available agent (if any) and offer this request to that agent. If the other agent will accepts that request, that agent will also be the part of that conversation.

  * If the agent will not accept that request and RONA occurs Routing engine will continue to find another available agent until TTL time expires.




#### Consult Request

Whenever an agent wants consultation from another agent without notifying the customer, he can select a specific queue or a specific agent and place a request, the custom agent desk should emit an event [consultRequest](https://expertflow-docs.atlassian.net/wiki/x/GgCmNw)

  * If the agent will not accept that request and RONA occurs Routing engine will continue to find another available agent until TTL time expires.

  * If the agent joins the conversation, now both the agents will communicate in whisper mode, the [Whisper Message](Whisper-Message_2529350.html) will not be sent to the customers.

  * The agent can conference or transfer the conversation to the consulted agent with the **offerToAgent**`: false` flag in the socket event.




### 8\. Silent Monitoring

Silent monitoring and bargin features are for supervisors. The pre-requisites are:

  * supervisors should have one or more assigned teams.

  * this feature is for push-mode and active chats only.

  * supervisor can only send [Whisper Message](Whisper-Message_2529350.html) as long as he is in silent monitoring role.




Whenever supervisors want to monitor any active conversation of any agent in their own teams, the custom agent desk should emit an event, ‘[JoinAsSilentMonitor](JoinAsSilentMonitor_2528276.html)'. On accepting the request, the agent manager will subscribe the supervisor to the conversation with the event called, ‘[ _onTopicData_](onTopicData_2531736.html) _’_.

#### Barge In Feature

Whenever a supervisor wants to intervene in the on-going conversation instead of being a silent observer, the custom Agent Desk should emit an event, ‘[JoinAsBargin](JoinAsBargin_2523671.html)’

The Agent Manager will emit an event, [_‘onCimEvent’_](onCimEvent_2531728.html) _,_ updating the role of the supervisor as BargIn. Now the supervisor can send all types of [CIM Messages](CIM-Messages_2530195.html) along with whisper message.

### 9\. Hand Raise 

Whenever an agent need any assistance during ongoing conversation, he can click the "Hand Raise" icon to signal the supervisor. Agent desk will emit a `publishCimEvent` with the bellow payload, hand raise will appear in the ongoing conversation dashboard. Supervisor can join the conversation as a whisper by clicking on the handraise icon, the agent manager will subscribe the supervisor to the conversation with the event called, ‘[ _onTopicData_](onTopicData_2531736.html) _’_.
[code] 
    {
      "id": "",
      "name": "HAND_RAISED",
      "type": "NOTIFICATION",
      "timestamp": 1709709884545,
      "conversationId": "",
      "eventEmitter": {},
      "channelSession": {}, // Channel Session Object,
      "data": {
        "agentId": "142ad3a6-6ab8-4cf7-9553-959e2c3605c2",
        "userName": "testuser"
      },
      "roomInfo": {}
    }
[/code]

### 10\. Leave Conversation

In order to leave any joined conversation, the custom Agent desk should emit an event called, '[topicUnsubscription_](topicUnsubscription__2531764.html)' please ignore the underscore in the event name.

  * In response to this event, the agent manager will close the agent’s task associated with this conversation and emits an event _‘_[ _topicUnsubscription_](topicUnsubscription_2531762.html) _’_ back to agent desk.



