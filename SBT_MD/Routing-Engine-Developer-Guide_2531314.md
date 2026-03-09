# CX Knowledgebase : Routing Engine Developer Guide

## Introduction  
  
The core functionality of the [Routing engine](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/2525975) i.e. to find an agent to converse with the customer when needed. The routing-engine micro service however handles a lot more than this. This doc presents a detailed overview of the concepts and functionalities of the Routing-Engine component in the CIM application.

Routing Engine contains the following sub-components

  * Push-mode automatic routing.

  * Agent and Agent-MRD state manager

  * Task state manager for both PUSH and PULL mode routing.

  * Agents' Routing Attributes, Media Routing Domains and Routing Queues configurations backend.




## Terms and Concepts

### Routing Attributes

A Routing Attribute serves as a Skill assigned to an Agent or a Supervisor. An agent can be assigned unlimited number of unique Routing-attributes

Routing Attributes are of the following two types: 

  * **Proficiency** : A value on a scale of 1 to 10. This implies how much proficient an Agent is on a particular skill. For instance, if an Agent is assigned an attribute, named, `English`, with a value of 8, this means that the agent is proficient enough in the English language to assist English-speaking customers. 

  * **Boolean:** True or False. This assumes that if an agent has a skill or does not have a skill. 




Routing Attributes are configured (Create, Retrieve, Update, Delete) in the Unified-admin dashboard. While creating an Attribute, the admin can specify a default value. This default value is automatically assigned to the agent at the time of attribute assignment. The admin may change the value for each attribute assigned to an agent at the time of the Attribute-assignment. 

A Routing Attribute entity contains the following fields:

**Field**| **Description**  
---|---  
**Id**|  A unique identifier (assigned automatically by the Routing Engine configurations backend)  
**Name**|  Name of the routing attribute  
**Description**|  Short description of the routing attribute   
**Type**|  Boolean or Proficiency-level  
**Default-value**|  An integer value. 0 or 1 for boolean type and 1 - 10 for proficiency-level type. When assigning a routing attribute to an agent, if a value is not provided then this default value is used.  
  
### Media Routing Domains 

A Media Routing Domain (MRD) is a collection of precision queues associated with a common media class. It is used to organise how requests for each communication medium, such as voice and chat, are routed to agents. An MRD is associated with a precision queue and a particular **Channel Type**. The relationship of these 2 associations is 1 to many. A precision queue can only have one MRD whereas one MRD can be associated to multiple precision queues. Similarly a channel-type can have only one MRD where as one MRD can be associated to multiple channel types.

A real life example of this is: suppose we have a Chat MRD to handle all chat type media like whatsapp, facebook messages e.t.c. and suppose we have two channel-types WHATSAPP and FACEBOOK configured in the system. Both of these channel-types will have the Chat MRD associated to them hence grouping these channel types under a single media domain. Further more suppose we have two routing queues, one handles the chat requests and the other handles the voice requests. The queue handling the chat requests will have the Chat MRD associated to it and requests coming from both whatsapp and facebook channels will be routed to this queue. This is just one example of how we can use the MRDs to group media types at channel level and queue level. This configuration is flexible and up-to to the user to decide.

Another role of the MRDs is at the Agents' state level. Agents have independent states for each MRD they are associated with. For instance, let's say we have an agent who is associated to two MRDs - chat and voice. The agent will receive the requests from only these two media domains. A request of let's say Email MRD will never be routed to this agent. The agent can choose to be available on each MRD independently. For instance, making itself READY for the Chat MRD and NOT_READY for voice MRD. Agent states in each MRD are independent of the other MRDs.

**Note:** As per the current implementation all agents are associated to all MRDs configured in the Unified-admin. In the future a configuration will be added in the unified-admin allowing the user to associate MRDs with each Agent in the system.

See [Media Channels](https://docs.expertflow.com/display/CIMp/Media+Channels) to learn more about **Channels, Channel Types, Channel Connectors,** and **Channel Sessions**.

Media Routing Domains are configured (Create, Retrieve, Update, Delete) in the Unified-admin dashboard. Their association with the channel type and routing queue is also configured in the unified admin. A media routing domain entity consist of the following fields:

**Field**| **Description**  
---|---  
**Id**|  A unique identifier (assigned automatically by the Routing Engine configurations backend)  
**Name**|  Name of the media routing domain  
**Description**|  Short description of the media routing domain  
**Interruptible**|  Boolean field. Tells whether a conversion of a specific media domain can be interrupted at the agent's end by a higher priority conversation. For instance, a chat conversation on whatsapp can be interrupted by a voice call. On the contrary an ongoing voice call cannot be interrupted by a chat request. This feature is **not** implemented yet in the routing engine and hence this field is not being used yet.  
  
### Routing Queues

A routing queue or precision queue is responsible for hosting new requests (tasks) generated by a customer. In each precision queue, there are some agents to answer customer requests being queued in the precision queue. Agents become members of precision queues automatically based on their Routing Attributes which are compared to one or more Criteria known as **Steps**.

For instance, if a precision queue requires an agent who lives in Boston, who speaks fluent Spanish, and who is proficient in troubleshooting a specific piece of equipment, an agent with the attributes, `Boston = True, Spanish = True, and Repair = 10` automatically becomes a part of the precision queue. Therefore, a Spanish caller in Boston who needs help with the equipment is routed to that agent.

A precision queue consists of **Steps** which are basically criteria to associate agents to the queue. A queue can have **at most** 10 of these steps. Each step has a bucket or list of agents associated to it which are used to route customer requests in the queue. At implementation level it is the Step in the queue that has agents associated to it, so for example:

Lets say we have a Queue _Q1_ with 2 Steps _S1_ and _S2_ which are configured as follows

S1 has associated agents → [A1, A2, A3]

S2 has associated agents → [A4, A5]

The overall queue Q1 has agents A1 to A5 available to it to route requests. When a request comes, the routing engine first tries to assign it to the agents associated to the first step; if no agent is available in the first step, it tries to assign it to the agents associated to the second step and so on. This process is described in detail in the "Steps" section below.

Furthermore a precision queue is a multi level queue

#### Term

A term compares an attribute against a value. For example, you can create the following term: Spanish == 10. Each precision queue can have multiple attributes, and these attributes can be used in multiple terms. For example, to select an agent with an English proficiency value between 5 and 10, the admin may create one term for English > 5 and another for English<10.

#### Expression

An expression is a combination of one or more terms. For instance, an expression `(Boston == true) AND (Spanish == true) AND (Repair == 10)` implies that agents living in BOSTON, fluent in Spanish and excellent in repairing skills are the best candidates for routing customer requests in this queue. 

The expressions are by default evaluated from left to right. For instance, the following expression is evaluated as the following: 

  


`(Boston == true) AND (Spanish == true) AND (Repair == 10)`  
  
`→ true` `AND true` `AND false`  
  
`→ true` `AND false`  
  
`→ false`  
---  
  
  


#### Step

A step consists of a combination of one or multiple expressions. When a request is landed in a queue, the steps are executed to evaluate the routing logic and pick the right agent. You can add one or more steps for one queue. Each step has a step timeout in seconds which determines the time that the system waits before jumping on to the next step in the queue. 

After the evaluation of the first step, if the system finds no agent matching the routing logic defined in the step, it jumps to evaluate the next step and keeps doing so until it finds an available agent. Steps are executed in the order they are created. 

### List

Most small-scale businesses or certain channel types with asynchronous activities require customer requests to be broadcasted to a **List** that an agent may subscribe to. Lists allow the system to park requests of certain channels in a list instead of queueing them. Agents subscribed to the List get real-time notifications of new chats being landed on the List. Agents may subscribe to one or multiple Lists. This type of request routing is called **Pull-based Routing.** See the following sections to learn more about Pull Routing.

To learn how to create new lists and assign them to certain channels, see [Admin Features](https://docs.expertflow.com/display/CIMp/Admin+Features).

  


A **Request** (a List entry or a new chat in the list) may be in any one of the following states:

  * UNREAD - until no agent has joined it

  * ACTIVE - when at least one agent is working on it

  * INACTIVE - when there's no agent working on this request. But, at least one agent joined this request earlier and left without closing it.

  * CLOSED - upon closure of the request when the request was removed




### Agents

Agents are supposed to be the contact center users who are eligible to answer customer requests.

Agents can be synchronized with the client's Active Directory and/or can be created and managed within Keycloak manually. Business admins can view all users having a certain Keycloak role or a set of roles in a **User list** within the Unified Admin App. They can then assign these users some Routing Attributes for the system to route customer requests to them.

#### Agent States

An Agent can be in any one of the following global states irrespective of the MRD which the agent is a part of:

**From**| **To**| **Description**  
---|---|---  
  
|  UNKNOWN| If the agent state is unknown, the state is UNKNOWN. This scenario is unlikely.  
LOGOUT| LOGIN | LOGIN is a transient state and transitions to NOT_READY.  
LOGIN| NOT_READY| When an agent is NOT_READY MRE doesn’t route any new request to this agent. After login, the agent is transitioned to NOT_READY.  
NOT_READY| READY| Once an agent is ready, new requests of an MRD may be routed to the agent depending upon the [A](https://docs.google.com/document/d/1M7d2RgtoyaVwPHu8QnVauWARUI2mfqV2xR65GZYlGqI/edit#heading=h.11somzhrkrhh)gent MRD State.  
READY| NOT_READY| Once an agent switches the state to `NOT_READY `state`,` all MRD switches will be turned off. The top agent-state dropdown turns grey and displays the Not Ready reason of the agent.   
NOT_READY| LOGOUT| Switch-off all MRDs, re-route all tasks, and Logout this agent  
any logged-in state| LOGOUT| If the agent has any active tasks on any MRD it'll be re-routed.   
  
#### Agent MRD States

Additionally, the agent can be in a different MRD state based on the number of tasks he/she's handling on that MRD.

**From**| **To**| **Description**| **Routable**  
---|---|---|---  
\- | LOGIN| The agent's state immediately after signing in. No tasks are assigned to an agent while in this state. The LOGIN state is a transitive state; LOGIN triggers a change that results in a new state (NOT_READY).| None; the user transitions to NOT_READY automatically  
LOGIN| NOT_READY| The agent won't be assigned tasks. The agent enters the NOT_READY state automatically after signing in.The toggle switch of the MRD state turns grey and remains `OFF`.| ![\(error\)](images/icons/emoticons/error.png)  
NOT_READY| READY| The agent is available to take new requests on this MRD. The toggle switch of the MRD state goes green and turns `ON`.| ![\(tick\)](images/icons/emoticons/check.png)  
  
| INTERRUPTED| When the routing engine has interrupted the agent on this MRD because of some other high-priority MRD task. Note: The agent cannot switch himself to this state. | ![\(error\)](images/icons/emoticons/error.png)  
READY| NOT_READY|   
|   
  
READY| ACTIVE| When the agent is working on at least one task in this MRD. The toggle switch of the MRD state goes orange and remains `ON`.| ![\(tick\)](images/icons/emoticons/check.png)  
ACTIVE| BUSY| When the agent has already been offered the maximum number of tasks in this MRD. The agent can therefore not receive new tasks in this MRD. [no-of-tasks = max_tasks]Note: The agent cannot switch himself to this state. The toggle switch of the MRD state goes red and remains `ON`.| ![\(error\)](images/icons/emoticons/error.png)  
  
| UNKNOWN| In a failover scenario, an agent state may be set to UNKNOWN. The agent can switch to READY or NOT_READY from an UNKNOWN state.| ![\(error\)](images/icons/emoticons/error.png)  
ACTIVE| PENDING_NOT_READY| If and when the agent switches off this MRD while the agent is `ACTIVE` . The toggle switch of the MRD state goes purple and turns `OFF`.| ![\(error\)](images/icons/emoticons/error.png)  
ACTIVE| READY| If the last task for an Agent MRD is closed, change state to READY| ![\(tick\)](images/icons/emoticons/check.png)  
BUSY| PENDING_NOT_READY| If and when the agent switches off this MRD while the agent is `BUSY` . The toggle switch of the MRD state goes purple and turns `OFF`.| ![\(error\)](images/icons/emoticons/error.png)  
PENDING_NOT_READY| NOT_READY| The agent state will be transited to NOT_READY automatically after all the active tasks are ended when the agent is in the PENDING_NOT_READY state.The toggle switch of the MRD state goes grey and remains `OFF`.| ![\(error\)](images/icons/emoticons/error.png)  
  
### Task

The Routing Engine creates a new task for a human agent for each new request that is routed to the agent. When the agent closes the request, the task status is also closed.

A Task can be in any one of the following states:

  * Created: When the Task is created

  * Active: When an agent is active on the Task.

  * Wrap-up: When the agent is applying a wrap-up 

  * Closed: When all channel sessions are closed and the agent leaves the chat 




### Routing Policy

Routing policy determines if a request should be pushed to an agent or should be broadcasted to a List.

Two types of routing policies are there:

  * Push Routing

  * Pull Routing




#### Push Routing

In this type of routing policy, the business decides to route and assign requests to the best suitable agent based on the agent selection criteria defined under the queue configurations. Whenever a new request is received from a channel, it is parked in a queue associated with the channel. To learn how to add new channels and associate queues to channels, see [Admin Features](https://docs.expertflow.com/display/CIMp/Admin+Features).

Based on the routing logic embedded in the Queue **Steps** (mentioned above), the Routing Engine picks an available agent who best matches the criteria and assigns the request. In short, this type of policy lets the system  _push_ a customer request to an agent. The agent has no option other than to Accept such a request. 

#### Sample Use case with Push Routing

  


##### Admin Configurations

A business administrator creates a new Media Routing Domain (MRD), `xyz` for entertaining any chat channel requests. 

The administrator also adds a new channel type `WhatsApp` to handle WhatsApp chats and links this channel type to the MRD, `xyz` . Then, it creates a new channel, `C1` of the channel type, `WhatsApp` . Assume that this channel is supposed to take customer chat requests from WhatsApp. 

The admin now needs to create a precision queue `Q1` to enqueue any sales inquiries coming from the channel `C1`. While creating the queue, the admin links the MRD `xyz` to the queue `Q1` and also adds `Q1,` as the default queue of the channel, `C1,` with the **Routing Policy** selected as **Push,** under the channel configurations. This implies that all requests coming on the channel `C1` will always be enqueued to the queue `Q1`.

The admin creates the following Routing Attributes to handle English-speaking customers coming from Los Angeles.

  * English (Boolean)

  * Los Angeles (Boolean) 




Suppose the routing logic of the queue says that if an agent is `English` speaking and belongs to `Los Angeles`, it should be able to take new chat requests coming from `Los Angeles `on the channel `C1. `

Step1: (English==true) AND (Los Angeles==true)

##### Chat Flow

Let's see what happens when a new request on `C1` comes in:

  1. Customer John Williams sends a WhatsApp message from Los Angeles, to subscribe to a new service launched recently in his area. 

  2. The chat request is routed to the queue `Q1 `which is the default queue for channel `C1.`

  3. Bot Framework checks if a Conversation from John Williams already exists. If not, it creates a new Conversation for the customer.

  4. A new channel session for the customer John is created in the system for this channel request.

  5. The Routing Engine looks for an available agent in the queue based on the routing logic defined by the queue steps.

  6. The Routing Engine finds an agent, Sussane Ready to take requests on the MRD `xyz.`

  7. The Routing Engine assigns the chat request to Sussane.

  8. The Routing Engine creates a Task for Sussane to work on this chat request. 

  9. Sussane accepts the request and starts a conversation with John.

  10. Sussane's state turns from `Ready` to `Active `on the MRD `xyz.`

  11. John gets the answer to his query.

  12. Sussane greets John and leaves the chat.

  13. Sussane's MRD state turns from `Active `to `Ready `on the MRD `xyz.`

  14. The system clears the Topic from Sussane's interface and closes the Task.

  15. Bot framework decides whether or not to close the Topic based on the Bot training data. The Topic can be closed automatically if certain intents such as (Thank you, Good Bye) are detected. The Channel Session would also automatically close after a certain timeout if not closed immediately.




  


#### Pull Routing

In this policy, a customer request received from a certain channel is supposed to land on a **List** (described above) instead of a Queue. To learn how to add new channels and associate Lists to channels, see [Admin Features](https://docs.expertflow.com/display/CIMp/Admin+Features).

An agent who's subscribed to the List notifications would be able to see that a new request is received on the List. He may then choose to JOIN the request or Dismiss the notification and may later join if needed. One or more agents may JOIN a request simultaneously and may choose to Leave the request at any time. 

A request listed on a List may be closed by an authorized agent at any time. A request can be closed if it is:

  * **Active** with an Agent

  * In **Inactive** state

  * In **Unread** state




#### Sample Use case with Pull Routing

  


##### Admin Configurations

Assume that the same system configurations are done in Unified Admin, for this scenario as done for [Push-based Routing](https://docs.expertflow.com/display/CIMp/Use+case+with+Push-based+Routing), except for the following differences:

The admin creates a new List, `L1` to take chat requests of channel `C1`.

In the channel configurations of `C1`, the admin chooses the **Routing Mode** as **Pull** (instead of Push) and links the list, `L1` with this channel.

##### Chat Flow

  * An admin creates an MRD to capture Facebook Page comments.

  * The admin also creates a Channel, adds a new List, and maps the Channel to the List. This channel is supposed to receive all customer comments posted on the Facebook page and drop them on the List.

  * A new comment is posted on the Facebook Page. 

  * The Channel manager publishes the request to the associated List. 

  * All agents subscribed to the List get the new incoming request notification. 

  * One or more agents attempt to join the Conversation. 

  * The agent(s) are subscribed to the Conversation.



