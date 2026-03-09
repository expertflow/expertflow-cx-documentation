# CX Knowledgebase : Reporting Database Schema

This document covers the SQL-based reporting database schema.  
  
The naming convention for table names and field names is an all-small snake case. Example: _multiple_word_variable._

  * Records are updated in the following tables in the reporting database, as per the scheduled interval of all ETL jobs.

  * If any changes are done to the configurations, the previous report records are not updated and the new changes are applied to the new reporting data only.

  * This schema guide provides details about the reporting database tables which are used only for historical reporting. For real-time dashboards, the data is extracted through real-time [REST APIs](https://www.postman.com/expertflow/workspace/expertflow-s-public-workspace/folder/4288348-dde2c14e-9822-4f44-aa50-4bd0a7fd784f?ctx=documentation) and available on [real-time dashboards for supervisors](Realtime-Reports-and-Dashboards_2529305.html).




## Channels and Channel Sessions

### channel_type

A channel type describes the type/class of the channels, for example, WHATSAPP, SMS, WEB. Multiple channels of a channel type can be created. 

See more on [Channel related terms](Channel-Related-Objects_276594689.html)

See [Administrator Guide -> Add Channel Type](Unified-Admin-Guide_2524407.html) for more details on Channel types.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
channel_type_id| PK, NOT NULL| [nvarchar](50) | [varchar](50) | Unique id to identify this channel type  
channel_type_name| NOT NULL| [nvarchar](50)| [varchar](50) | Records the name for this channel type, any alphanumeric value  
  
### channel

A channel instance is created when a new communication channel is registered by the admin. It includes all the configuration details of a channel, for example, the channel name, service identifier, channel mode, etc. A channel is of a particular channel type. For instance, we can create two channels WhatsApp-external and WhatsApp-internal, both of a channel type WHATSAPP. 

See more on [Channel related terms](Channel-Related-Objects_276594689.html)

See [Administrator Guide -> Step 11: Set up a new Channel](Unified-Admin-Guide_2524407.html) for more details on Channel types.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
channel_id| PK, NOT NULL| [nvarchar](50)| [varchar](50) | Unique id to identify this channel  
channel_name| NOT NULL| [nvarchar](50)| [varchar](50) | Records the name for this channel  
channel_type_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the channel type for this channel  
channel_mode | NOT NULL| [nvarchar](20)| [varchar](20) | Indicates the channel mode for this channel

  * **HYBRID** \- Both the bot and the human agents are engaged on communication with the customer. 
  * **BOT** \- Only bot is engaged in communication with the customer. 
  * **AGENT** \- Only human agents are engaged in communication with the customer. 

  
service_identifier| NOT NULL| [nvarchar](MAX)| [varchar](250) | Unique identifier like a phone number or URL associated to this channel. **Example** : For a WhatsApp channel, the business WhatsApp account's phone number which is registered for receiving customer's messages will come here.  
created_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is created.  
updated_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is updated.  
is_deleted| NOT NULL| [bit]| [TINYINT](1)| Indicates that this channel has been deleted from the system. (Used for soft deletion)  
  
### channel_session

A customer can converse on multiple channels at a time in one conversation. A new channel session is created every time a customer initiates a session on a channel. For instance, a customer first opens up a chat from Webchat and later on, sends a message from its WhatsApp.

See more on [Channel related terms](Channel-Related-Objects_276594689.html)  


**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
session_id| PK, NOT NULL| [nvarchar](50) | [varchar](50) | Unique id to identify this channel session.  
**conversation_id**| **FK, NOT NULL**| **[nvarchar](50)**| **[varchar](50)**| **Identifies the conversation, this channel session is associated to**  
channel_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the channel, this channel session is associated to  
start_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the channel session is started.  
end_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the channel session is ended.  
total_session_duration| NOT NULL| [int]| [INT]| Records the value of total duration of this channel session **i.e.** end_time minus start_time  
disposition| NOT NULL| [nvarchar](20)| [varchar](20) | Indicates the reason why the channel session was ended.**AGENT** \- the human agent ended the channel session. This is valid in case of Pull-based chats from the list by clicking the "Close" button.  
**CUSTOMER** \- the customer ended the session. This happens in case when the web chat widget is closed by the customer. Only true for web chat channels.  
**INACTIVITY** \- the customer was inactive for a configured timeout (timeout is managed by the Bot).  
**NETWORK** \- the conversation ended due to some network error usually in case when the network is disconnected. **FORCE_CLOSED** \- the system (ExpertFlow CX) ends the channel session.  
bot_activity_count| NOT NULL| [int]| [INT]| Records the number of messages sent by the bot on this channel session  
agent_activity_count| NOT NULL| [int]| [INT]| Records the number of messages sent by the agent(s) on this channel session  
customer_activity_count| NOT NULL| [int]| [INT]| Records the number of messages sent by the customer on this channel session  
~~avg_bot_confidence_level~~| ~~NOT NULL~~| [decimal]| [DECIMAL(5,5)]| Reserved for future.For each bot response, there is a percentage value that tells how confidently the bot was able to answer a query. This field gives us the average value for all bot-confidence values.  
record_creation_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the record is created in source DB**i.e.** MongoDB  
device| NULL| [nvarchar](40)| [varchar](40)|   
  
browser_type| NULL| [nvarchar](40)| [varchar](40)|   
  
country| NULL| [nvarchar](40)| [varchar](40)|   
  
language| NULL| [nvarchar](40)| [varchar](40)|   
  
channel_customer_identifier| NULL| [nvarchar](255)| [varchar](255)| Channel customer identifier extracted from `CHANNEL_SESSION_STARTED` & `CHANNEL_SESSION_ENDED` CIM events  
  
## Conversations

### conversation

A conversation entity records the customer's conversation details. A conversation consists of all channel sessions where a customer is conversing, the conversation participants (bots, agents, customers) and optionally also some conversation data.

See more about Conversations on [Conversation Objects](Conversation-Objects_2528831.html) Unique id to identify this conversation

This table only records the essential conversation fields. There are separate tables for conversation data and conversation participants.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
conversation_id| PK, NOT NULL| [nvarchar](50) | [varchar](50) |   
  
room_id (reserved for future)| FK, NULL| [nvarchar](50)| [varchar](50) | Identifies the room this conversation is a part of. Currently, null since a conversation is not a part of any room.  
customer_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the customer with whom this conversation is associated.  
customer_name| NOT NULL| [nvarchar](50)| [varchar](50) | Records the customer name with whom this conversation is associated.  
start_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this conversation was started.  
end_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this conversation was ended.  
conversation_duration| NOT NULL| [int]| [INT]| Records the value of total duration of this conversation **i.e.** end_time minus start_time  
bot_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifier of the bot who was a participant of this conversation.  
task_state| NULL|   
| [varchar](50)| Records the state of conversation **i.e. ACTIVE, CLOSED**  
reason_code| NULL|   
| [varchar](50)| Records the reason code of conversation **i.e. DONE, AGENT_LOGOUT, CANCELED, NO_AGENT_AVAILABLE, RONA, NULL**  
disposition| NOT NULL| [nvarchar](20)| [varchar](20) | This is the reason why the conversation was closed. The details can be referenced from the document [Task Reason Codes](Task-Reason-Codes_144212603.html) There can be multiple tasks created for a conversation. We will sort these tasks w.r.t the date and time and see the latest ones. The disposition will be considered on last task.  
direction| NOT NULL| [nvarchar](20)| [varchar](20) | Records the direction of conversation **i.e.** INBOUND/OUTBOUND.There can be multiple channel sessions (INBOUND/OUTBOUND) in a conversation. We'll consider the conversation's direction based on the first channel session's direction in a conversation.   
  
### conversation_data

A conversation can have key-value pairs to record any arbitrary additional data required. This is known as the conversation data. A single key-value pair for a conversation is inserted as one record in this table.

See [Conversation Data](ConversationData_2526208.html) for more details.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
conversation_id| FK, NOT NULL| [nvarchar](50) | [varchar](50) | Identifies the conversation for which this conversation data record is inserted  
key| NOT NULL| [nvarchar](50)| [varchar](50) | Any alphanumeric value  
value| NOT NULL| [nvarchar](100)| [varchar](100) | Any alphanumeric value  
  
### conversation_participant

Conversation participants are the participants that take part in a conversation. For example , customers, bots and agents. Each record in the table represents a Conversation Participant.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
id| PK, NOT NULL | [nvarchar](50) | [varchar](50) | A unique identification of a participation by agent/customer/bot etc.  
participant_id| NOT NULL| [nvarchar](50)| [varchar](50) | Unique id (Customer ID/ Bot ID / Agent ID) to identify a participant.  
conversation_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the conversation this participant is part of.  
participant_role (AGENT | CUSTOMER | EXTERNAL)| NOT NULL| [nvarchar](30)| [varchar](30) | Indicates the role of a participant in the conversation

  * **AGENT** \- If the participant is an agent
  * **CUSTOMER** \- If the participant is one of the channel_sessions that a customer is conversing on.
  * **EXTERNAL** \- Other participants like a bot etc.

  
record_creation_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the record is created in source DB**i.e.** MongoDB  
  
### wrapup_detail

A conversation's wrap-up details are recorded in this table.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
wrapup_time| NOT NULL| [DateTime]| [DateTime](3)| Records the time when the wrap-up was applied.  
conversation_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the conversation to which the wrap-up was applied   
wrapup_label| NULL| [nvarchar](50)| [varchar](50) | The wrap-up label for the applied wrap-up   
category_name| NULL| [nvarchar](50)| [varchar](50) | Records the wrap-up category  
agent_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the agent who did the wrap up on the associated conversation  
notes| NULL| [nvarchar](350)| [varchar](350) | Optional notes entered by agents while applying wrap up to a conversation  
record_creation_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the record is created in source DB**i.e.** MongoDB  
  
## Room (reserved for future)

### room

A room is a group of customers conversing among each other and with the system entities like a bot or human agents. One customer participating in a room is inserted as one record in this table

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
room_id| PK, NOT NULL| [nvarchar](50)| [varchar](50) | Unique id to identify the room  
customer_id| FK, NOT NULL| [nvarchar](50) | [varchar](50) | Identifies a customer participating in this room  
creation_time| NOT NULL| [DateTime] | [DateTime](3)| Records the date and time when this record is created in this table.  
  
## Bots

### bot

This table records the details of a bot configured in the system by the admin. One bot's details are added as a single record in this table

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
bot_id| PK, NOT NULL| [nvarchar](50)| [varchar](50) | Unique id of identifying the bot  
bot_name| NOT NULL| [nvarchar](50)| [varchar](50) | Records the name of the bot.  
created_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is created.  
updated_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is updated.  
is_deleted| NOT NULL| [bit]| [TINYINT](1)| Indicates the bot has been deleted from the system.(Used for soft deletion)  
  
## Agents and States

### agent

This table records the details of an agent. One agent's details are inserted as a single record in the table.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
agent_id| PK, NOT NULL| [nvarchar](50)| [varchar](50) | Unique id to identify this agent  
agent_name| NOT NULL| [nvarchar](100)| [varchar](100) | Records the agent name   
username| NOT NULL| [nvarchar](100)| [varchar](100) | The agent's unique username is logged.  
agent_extension| NULL| [nvarchar](10)| [varchar](10) | Records the agent's extension  
team_id (reserved for future)| FK, NULL| [nvarchar](50)| [varchar](50) | Identifies the team this agent is part of. This field is currently null since teams are not yet set up  
created_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is created.  
updated_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is updated.  
is_deleted| NOT NULL| [bit]| [TINYINT](1)| Indicates the agent has been deleted from the system. (Used for soft deletion)  
  
### agent_mrd_state

This table records the details of an agent's MRD state at a particular instance. Each time an agent changes its state on the MRD, a new record is inserted into this table.

Learn more about [Agent MRD state transitions](Change-Agent-State_2524603.html)

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
login_date_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when MRD state changed to login.  
agent_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the Agent whose Agent MRD state is recorded here  
mrd_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the MRD this MRD state is associated to  
agent_mrd_state| NOT NULL| [nvarchar](20)| [varchar](20) | Records the MRD state. For example 'READY', 'ACTIVE' etc.  
duration| NOT NULL| [int]| [INT]| The length of time MRD spent in the specified state as recorded in the "agent_mrd_state" column.  
  
This duration is recorded in seconds.   
**Note:** When the duration value is **"-1** " , it indicates that the MRD is presently in its current state and has not transitioned to the succeeding state yet.  
state_change_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the MRD state was changed  
  
agent_state

This table records the details of an agent's state at a particular instance. For example, if this agent's state is 'READY' then 'NOT_READY' and then 'READY' again, three records will be inserted into the table.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
login_date_time | NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when MRD state changed to login.  
agent_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the agent whose Agent state is recorded here.  
agent_state| NOT NULL| [nvarchar](20)| [varchar](20) | Records the Agent state value. For example, 'READY', 'NOT_READY', 'LOGOUT' etc.  
reason_code| NULL| [nvarchar](100)| [varchar](100) | Records the reason why agent switched to NOT_READY or LOGOUT state.**For example ,** SHORT_BREAK , TIME_OFF etc  
duration| NOT NULL| [int]| [INT]| The length of time agent spent in the specified state as recorded in the "agent_state" column.  
  
This duration is recorded in seconds.**Note:** When the duration value is **"-1** ", it indicates that the Agent is presently in its current state and has not transitioned to the succeeding state yet.   
  
state_change_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the Agent state was changed.  
  
agent_team (reserved for future)

A team is a list of agents that are grouped together to be managed by a contact center supervisor. 

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
team_id| PK, NOT NULL| [nvarchar](50)| [varchar](50) | Unique id to identify this team. ETL job will put dummy values.  
team_name| NOT NULL| [nvarchar](50)| [varchar](50) | Records the team name, any alphanumeric value  
description| NULL| [nvarchar](100)| [varchar](100) | Records a short description of this team's value proposition  
created_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is created.  
updated_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is updated.  
is_deleted| NOT NULL| [bit]| [TINYINT](1)| Indicates the team has been deleted from the system. (Used for soft deletion)  
  
## Routing

### queue

This table records the properties of a routing queue. Whenever a human agent is required for a conversation, a request to assign an agent is created by the system and offered to a precision queue.

To learn more about queues, see [precision routing](Precision-Routing_2525641.html)

Also, see [Unified Admin Guide](Unified-Admin-Guide_2524407.html) to learn more about each queue properties listed below

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
queue_id| PK, NOT NULL| [nvarchar](50) | [varchar](50) | Unique Id to identify this queue  
queue_name| NOT NULL| [nvarchar](50) | [varchar](50) | Records the queue name, any alphanumeric string  
sl_type| NOT NULL| [int]| [INT]| Service level type can have the following values1 = Ignore Abandoned Chats2 = Abandoned Chats have a Negative Impact3 = Abandoned Chats have a Positive Impact  
sl_threshold| NOT NULL| [int]| [INT]| Indicates the number of seconds in which a request must be routed to an agent  
created_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is created.  
updated_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is updated.  
is_deleted| NOT NULL| [bit]| [TINYINT](1)| Indicates that the queue has been deleted from the system.(Used for soft deletion)   
  
### agent_task

Whenever a conversation needs a human agent, Expertflow CX creates an agent task to be routed to an agent.

This is also true when a conversation is re-queued to the queue for whatever reasons, say, RONA occurred, no agents were available or agent got logged out. 

This means that a conversation can have multiple agent tasks created for each agent joining the conversation.

This table keeps the details of an agent task whenever a new task is created for a conversation. 

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
agent_task_id| PK, NOT NULL| [nvarchar](50)| [varchar](50) | Unique id to identify this task  
conversation_id| FK, NOT NULL| [nvarchar](50)| [varchar](50) | Identifies the conversation this task is created for  
agent_id| FK, NULL| [nvarchar](50)| [varchar](50) | Identifies the agent which was assigned to this task. If the task was ended while in the queued state then this field is null  
task_queue_time| NULL| [DateTime]| [DateTime](3)| Records the date and time when the task is offered to a routing queue like in case of PUSH mode routing.This field is NULL in following cases :

  * If the task routing is skipped and the task is directly assigned to the agent, like in the case of pull mode routing.
  * If agent has initiated the chat i.e. OUTBOUND chat.

  
task_reserved_time| NULL| [DateTime]| [DateTime](3)| Records the date and time when an agent is reserved for this task.This field is NULL in following cases :

  * If the task is directly assigned to the agent, like in the case of pull mode routing.
  * If agent has initiated the chat i.e. OUTBOUND chat.
  * If the task was ended while in the queued state i.e. for PUSH mode routing.

  
task_answered_time| NULL| [DateTime]| [DateTime](3)| Records the date and time when the reserved agent accepts the task. This field is null if the agent never answered the task.For example in following cases : 

  * if the task was closed while in the queued state.
  * If the task was presented to the agent but the agent did not accept it.

  
queue_id| FK, NULL| [nvarchar](50)| [varchar](50) | Identifies the queue in which this task is enqueued for routing.This field is NULL in following cases :

  * In case where queue routing is skipped and the task is directly assigned to an agent like in the case of pull mode routing.
  * If agent has initiated the chat i.e. OUTBOUND chat.

  
task_queue_duration| NOT NULL| [int]| [INT]| For PUSH mode routing , it will record the task_reserved_time minus task_queue_time value.It will be 0 in following cases :

  * For PULL mode routing.
  * If agent has initiated the chat i.e. OUTBOUND chat.
  * If the task was ended while in the queued state i.e. for PUSH mode routing.

  
task_alert_duration| NOT NULL| [int]| [INT]| For PUSH mode routing , it will record the task_answered_time minus task_reserved_time value.It will be 0 in following cases :

  * For PULL mode routing.
  * If agent has initiated the chat i.e. OUTBOUND chat.
  * If the task was ended while in the queued state i.e. for PUSH mode routing.

  
task_end_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the task was ended/closed.  
task_disposition| NOT NULL| [nvarchar](30)| [varchar](30) | This is basically the reason why the task was ended.  
The reason could be one of the following.

  * DONE
  * RONA
  * RESPONSE_TIMEOUT
  * NO_AGENT_AVAILABLE
  * REROUTE
  * CANCELLED
  * AGENT_LOGOUT
  * TRANSFERRED 
  * FORCE_CLOSED.

  
record_creation_time| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when the record is created in source DB**i.e.** MongoDB  
wrapup_duration (future use)| NOT NULL| [int]| [INT]|   
  
mrd_id| FK, NULL| [nvarchar](50) | [varchar](50) | Unique Id to identify the MRD through which this task is created.  
task_direction| NOT NULL| [nvarchar](50) | [varchar](50) | This records the direction how the task was created. The directions can be one of the following.

  * INBOUND
  * OUTBOUND
  * CONSULT
  * **CONSULT_TRANSFER:** A task direction changed from Consult to transfer, when the call is transferred to a consulted agent
  * **CONSULT_CONFERENCE:** A task direction changed from Consult to conference, when the call is conferenced to a consulted agent
  * **DIRECT_TRANSFER:** Directly transferred to an agent (the agent is not consulted first in this case)
  * **DIRECT_CONFERENCE:** Directly transferred to an agent (the agent is not consulted first in this case)

  
task_mode| NOT NULL| [nvarchar](50) | [varchar](50) | This records the mode how the task was created. The mode can be one of the following.

  * **AGENT** : Directly assigned to an agent.
  * **QUEUE:** Task pushed to queue to route to any agent.

  
routing_mode| NOT NULL| [nvarchar](50) | [varchar](50) | This records one of the following outing modes.

  * **PUSH** : The incoming request was pushed to a queue to be routed to agents.
  * **PULL** : Broadcasted to a Pull-based List to be taken up by any agents subscribed to the List. ****

  
channel_session_id| NOT NULL| [nvarchar](50) | [varchar](50) | A unique identifier for this channel session is associated with this task.  
list_id| NULL| [nvarchar](50) | [varchar](50) |   
  
  
### media_routing_domain

This table records the properties of a media routing domain (MRD.) .

To learn more about queues, see [Channel Categories (Media Routing Domains)](2532738.html)

Also, see the [Unified Admin Guide](Unified-Admin-Guide_2524407.html) to learn more about each MRD properties listed below

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
mrd_id| PK, NOT NULL| [nvarchar](50) | [varchar](50) | Unique Id to identify this MRD.  
mrd_name| NOT NULL| [nvarchar](50) | [varchar](50) | Records the MRD name, any alphanumeric string  
description| NULL| [nvarchar](250) | [varchar](250) | Short description of the media routing domain  
max_task_request| NOT NULL| [int]| [INT]| This is the max tasks that the MRD can receive.  
is_interruptible| NOT NULL| [bit]| [TINYINT](1)| Tells whether a conversion of a specific media domain can be interrupted at the agent's end by a higher priority conversation. For instance, a chat conversation on WhatsApp can be interrupted by a voice call. On the contrary an ongoing voice call cannot be interrupted by a chat request.  
is_managed_by_re| NOT NULL| [bit]| [TINYINT](1)| When the value is true, it indicates that the Routing Engine is responsible for managing this MRD. Conversely, if the value is false, it means that other sources, such as Cisco, are in charge of managing this specific MRD.  
created_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is created.  
updated_at| NOT NULL| [DateTime]| [DateTime](3)| Records the date and time when this record is updated.  
is_deleted| NOT NULL| [bit]| [TINYINT](1)| Indicates that the queue has been deleted from the system.(Used for soft deletion)   
  
## IVR

### ivr

This table records the properties of an IVR.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
conversation_id| FK, NOT NULL| [nvarchar](50) | [varchar](50)|   
  
help_line| NULL| [nvarchar](50) | [varchar](50)|   
  
start_date_time| NULL| DATETIME| DATETIME|   
  
caller_number| NULL| [nvarchar](20)| [varchar](20)|   
  
main_menu_selection| NULL| [nvarchar](20)| [varchar](20)|   
  
sub_menu_option_selected| NULL| [nvarchar](20)| [varchar](20)|   
  
journey| NULL| [nvarchar](250)| [varchar](250)|   
  
selection| NULL| [nvarchar](250)| [varchar](250)|   
  
duration| NOT NULL| INT| INT|   
  
language| NULL| [nvarchar](20)| [varchar](20)|   
  
call_id| NOT NULL| [nvarchar](50)| [varchar](50)|   
  
end_date_time| NULL| DATETIME| DATETIME|   
  
start_direction| NULL| [nvarchar](50)| [varchar](50)|   
  
call_disposition| NULL| [nvarchar](50)| [varchar](50)|   
  
record_creation_time| NOT NULL| DATETIME| DATETIME|   
  
  
## LIST

### list

This table records the properties of a routing queue. Whenever a human agent is required for a conversation, a request to assign an agent is created by the system and offered to a precision queue.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
list_id| PK, NOT NULL| [nvarchar](50) | [varchar](50) |   
  
list_name| NOT NULL| [nvarchar](50) | [varchar](50) |   
  
created_at| NOT NULL| DATETIME(3)| DATETIME(3)|   
  
updated_at| NOT NULL| DATETIME(3)| DATETIME(3)|   
  
is_deleted| NOT NULL| BOOLEAN| BOOLEAN|   
  
  
## conversation_hold_resume

This table records the properties of conversations that were held and later resumed, capturing key details such as the time of hold and resume events, and the agent or channel session interaction involved.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
conversation_id| FK, NOT NULL| [nvarchar](50) | [varchar](50) | Unique identifier for the conversation, linking it to the main conversation table.  
conversation_state| NOT NULL| [nvarchar](50) | [varchar](50) | Indicates the current state of the conversation (e.g., HOLD, RESUMED).  
agent_id| NULL| [nvarchar](50) | [varchar](50) | Identifier for the agent involved in the conversation, if applicable.  
event_timestamp| NOT NULL| DATETIME(3)| DATETIME(3)| Timestamp of the hold or resume event in the conversation.  
channel_session_id| NOT NULL| [nvarchar](50) | [varchar](50) | Unique identifier for the communication session related to the conversation.  
record_creation_time| NOT NULL| DATETIME(3)| DATETIME(3)| Timestamp indicating when the record was created in the source i.e mongoDB  
  
## Forms and Survey

### Forms

This table records the submitted forms data coming from the _conversation_manager_db_ of mongodb within the _CustomerTopicEvents_ collection`. The objects are filtered based on their _cimEvent_ , which corresponds to “**FORMS_DATA** ,” which is further transformed and loaded into a table whose schema details are as follows. Learn more about forms <https://expertflow-docs.atlassian.net/wiki/x/dKAm>

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
row_id| PK, NOT NULL, AUTO-INCREMENT| STRING(255)| STRING(255)| Unique identifier for the table  
conversation_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the conversation, linking it to the main conversation table.  
channel_session_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the communication session related to the conversation.  
channel_customer_identifier| NULL| STRING(255) | STRING(255)| Used to identify channel from where customer is coming  
service_indentifier| NULL| STRING(255)| STRING(255)| Service being used by the customer  
customer_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the customer  
customer_is_anonymous| NULL| STRING(255)| STRING(255)| Checking if the form submitted by customer is anonymous or not  
customer_first_name| NULL| STRING(255)| STRING(255)| Customers first name  
room_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the conversation, linking it to the room table  
activity_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier to show the various activities performed by customers  
form_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the submitted forms  
form_title| NULL| TEXT| TEXT| Title of the submitted form  
form_weightage| NULL| STRING(255)| STRING(255)| Represents the overall weightage assigned to a form in a survey or assessment.  
form_score| NULL| INTEGER| INTEGER| Represents the overall score rating of the form answers.  
enable_weightage| NULL| STRING(255)| STRING(255)| Indicates whether the weightage feature is enabled for the form or survey.  
intent| NULL| STRING(255)| STRING(255)| Scope of the submitted form activity  
sentiment_result| NULL| STRING(255)| STRING(255)| Stores the sentiment analysis result, typically reflecting the emotional tone of the response.  
sender_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the agent that sent the form  
sender_type| NULL| STRING(255)| STRING(255)| The channel from where the form is sent  
sender_name| NULL| STRING(255)| STRING(255)| Name of the sender  
section_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the various sections of form  
section_name| NULL| TEXT| TEXT| Name of the section  
section_weightage| NULL| STRING(255)| STRING(255)| Weightage assigned to a specific section within a form or survey.  
section_score| NULL| INTEGER| INTEGER| Represents the overall score rating of a form’s section.  
attribute_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the attributes  
attribute_type| NULL| TEXT| TEXT| Type of atribute allocated to the section of form  
e.g. **INPUT** = descriptive section of form (_shortAnswer_)  
**OPTION** = MCQs section of form  
attribute_label| NULL| TEXT| TEXT| Label of the section on the form  
attribute_weightage| NULL| STRING(255)| STRING(255)| Weightage assigned to individual attributes within a form or survey section.  
attribute_score| NULL| INTEGER| INTEGER| Represents the overall score rating of the attributes of a form.  
value_type| NULL| TEXT| TEXT| Type of output associated with the section  
e.g. **shortAnswer** , **mcq** , **5-star-rating**  
skip_type| NULL| STRING(255)| STRING(255)| Specifies the condition or rule under which a question or section can be skipped in a form or survey.  
answer_label| NULL| TEXT| TEXT| Output labels associated with each section  
answer_value| NULL| TEXT| TEXT| Answer submitted for each section  
is_selected| NULL| BOOL| BOOL| Options selected in each section   
option_weightage| NULL| STRING(255)| STRING(255)| Percentage that each option carries with them  
additional_details| NOT NULL| JSON| JSON| Raw data containing any additional details of the respective form data.  
timestamp| NOT NULL| DATETIME| DATETIME| Time when the record is created  
recordCreationTime| NOT NULL| DATETIME| DATETIME| Time when the record is created  
_etl_inserted_at| NOT NULL| DATETIME| DATETIME| Date and Time when data was loaded in the table.  
  
### Forms_gold

This table stores the aggregated/pre-calculated data after the gold queries have been applied to the original forms data from the forms table.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
id| PK, NOT NULL, AUTO-INCREMENT| INT| INT| Unique identifier for the table  
inter| NULL| DATETIME| DATETIME| Time interval  
agent_id| NULL| STRING(255)| STRING(255)| Unique identifier for agent, linking it to agent table  
agent_name| NULL| STRING(255)| STRING(255)| Name of the agent  
conversation_id| FK, NULL| STRING(255)| STRING(255)| Unique identifier for the conversation, linking it to the main conversation table.  
channel_session_id| NULL| STRING(255)| STRING(255)| Unique identifier for the communication session related to the conversation.  
customer_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the customer.  
attribute_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the attributes  
attribute_label| NULL| TEXT| TEXT| Label of the section on the form  
form_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the submitted forms  
section_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the various sections of form  
value_type| NULL| TEXT| TEXT| Type of output associated with the section  
e.g. **shortAnswer** , **mcq** , **5-star-rating**  
answer_label| NULL| TEXT| TEXT| Output labels associated with each section  
TotalAnswers| NULL| STRING(255)| STRING(255)| Total answers available with each section  
  
### forms_schema

The table records all of the schema for the form data (that is required for QM data as well) coming from the _adminPanel_ db of mongodb within the _forms_ folder, which is further transformed and loaded into a table whose schema details are as follows.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
row_id| PK, NOT NULL, AUTO-INCREMENT| STRING(255)| STRING(255)| Unique identifier for the table  
form_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the submitted forms  
form_title| NULL| TEXT| TEXT| Title of the submitted form  
form_weightage| NULL| STRING(255) | STRING(255)| Represents the overall weightage assigned to a form in a survey or assessment.  
form_description| NULL| TEXT| TEXT| Description of the submitted form  
form_score| NULL| INTEGER| INTEGER| Represents the overall score rating of the form answers.  
section_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the various sections of form  
section_name| NULL| TEXT| TEXT| Name of the section  
section_weightage| NULL| STRING(255)| STRING(255)| Weightage assigned to a specific section within a form or survey.  
attribute_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the attributes  
attribute_type| NULL| TEXT| TEXT| Type of atribute allocated to the section of form  
e.g. **INPUT** = descriptive section of form (_shortAnswer_)  
**OPTION** = MCQs section of form  
attribute_label| NULL| TEXT| TEXT| Label of the attribute on the form  
attribute_key| NULL| STRING(255)| STRING(255)| Key of the attribute on the form  
attribute_weightage| NULL| STRING(255)| STRING(255)| Weightage assigned to individual attributes within a form or survey section.  
value_type| NULL| TEXT| TEXT| Type of output associated with the section  
e.g. **shortAnswer** , **mcq** , **5-star-rating**  
attribute_data_label| NULL| STRING(255)| STRING(255)| Data label of the attribute on the form  
option_label| NULL| TEXT| TEXT| Output labels associated with each option  
option_value| NULL| TEXT| TEXT| Answer submitted for each option  
is_deleted| NULL| Boolean| Boolean| flag for soft deletion  
created_id| NOT NULL| DATETIME| DATETIME| Record creation time  
updated_at| NOT NULL| DATETIME| DATETIME| Record update time  
  
### Survey_distribution

This table records the survey distribution data coming from the _surveydb_ of mongodb within the _surveydistributions_ folder, which is further transformed and loaded into a table whose schema details are as follows.

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
id| PK, NOT NULL,| STRING(255)| STRING(255)| MongoDB Object id  
survey_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for survey  
form_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the submitted forms  
customer_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for the customers  
activity_message| NULL| TEXT| TEXT| Form message that is sent when the chat has ended  
deleted| NULL| Boolean| Boolean| flag for soft deletion  
created_id| NOT NULL| DATETIME| DATETIME| Record creation time  
updated_at| NOT NULL| DATETIME| DATETIME| Record update time  
_etl_inserted_at| NOT NULL| DATETIME| DATETIME| Date and Time when data was loaded in the table.  
  
## Teams

### Team

This table records the details of the teams data

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
team_id| PK, NOT NULL,| STRING(255)| STRING(255)| Unique indentifier for teams  
team_name| NULL| STRING(255)| STRING(255)| Name of the team  
supervisor_id| NULL| STRING(255)| STRING(255)| Unique identifier for supervisors  
source| NULL| TEXT| TEXT| Unique identifier for the customers  
created_by| NULL| STRING(255)| STRING(255)| Record created by  
created_at| NOT NULL| DATETIME| DATETIME| Record creation time  
updated_at| NOT NULL| DATETIME| DATETIME| Records update time  
  
### Team_members

This table records the details of the team members data

**Field**| **Constraints**| **Data type (MsSQL)**| **Data type (MySQL)**| **Description**  
---|---|---|---|---  
id| PK, NOT NULL| STRING(255)| STRING(255)| Unique identifier for the table  
team_id| NOT NULL,| STRING(255)| STRING(255)| Unique identifier for teams  
type| NOT NULL| STRING(255)| STRING(255)| Type of person e.g. agent, secondary-supervisor  
username| NOT NULL| STRING(255)| STRING(255)| Username of person  
user_id| NOT NULL| STRING(255)| STRING(255)| Unique identifier for person  
created_at| NOT NULL| DATETIME| DATETIME| Record creation time  
updated_at| NOT NULL| DATETIME| DATETIME| Records update time  
  
## Activities

### Voice_activities

This table records the details of the voice activities data

**Field**| **Constraint**| **Source Field ( MongoDB)**| **Source Data Type ( MongoDB)**| **MySQL Data Type**| **MSSQL Data Type**| **Description**  
---|---|---|---|---|---|---  
row_id| PK, NOT NULL| | | varchar(255)| varchar(255)| Primary-Key: Hashing Field to implement upserting  
id| NOT NULL| _id| Object ID| varchar(255)| varchar(255)| Unique field for mongo document  
customer_id| NOT NULL| customerId| String| varchar(255)| varchar(255)| Unique field for customer_id  
conversation_id| NOT NULL| conversationId| String| varchar(255)| varchar(255)| Unique field for conversation_id  
channel_session_id| NOT NULL| channelSessionId| String| varchar(255)| varchar(255)| Unique field for channel session id  
channel_session_direction| NOT NULL| activity.channelSession.channelSessionDirection| String| varchar(255)| varchar(255)| Field showing channel session direction (Inbound/Outbound)  
channel_id| NOT NULL| acitivity.channelSession.channel._id| Object ID| varchar(255)| varchar(255)| Unique field for channel id  
channel_name| NOT NULL| acitivity.channelSession.channel.name| String| varchar(255)| varchar(255)| Channel Name (e.g. CX voice etc)  
channel_customer_identifier| NOT NULL| acitivity.channelSession.channelData.channelCustomerIdentifier| String| varchar(255)| varchar(255)| Unique customer identifier  
service_identifier| NOT NULL| acitivity.channelSession.channel.serviceIdentifier| String| varchar(255)| varchar(255)| Service identifier for CX  
tenant_id| NOT NULL| acitivity.channelSession.channel.tenant._id| Object ID| varchar(255)| varchar(255)| Unique field for tenant id  
customer| NOT NULL| acitivity.channelSession.customer| Object| JSON| nvarchar(max)| Array containing customer information  
room_id| NOT NULL| roomId| String| varchar(255)| varchar(255)| Unique field for room id  
activity_id| NOT NULL| activity._id| Object ID| varchar(255)| varchar(255)| Unique field for activity id  
activity_name| NOT NULL| activity.name| String| varchar(255)| varchar(255)| Activity name (e.g. voice-activity)  
activity_timestamp| NOT NULL| activity.timestamp| Date| DATETIME(3)| DATETIME(3)| Timestamp for activity  
event_emitter_id| NOT NULL| activity.eventEmitter.id| String| varchar(255)| varchar(255)| Unique field for event emitter id  
event_emitter_type| NOT NULL| activity.eventEmitter.type| String| varchar(255)| varchar(255)| Type of event emitter (e.g. Bot)  
state_name| NOT NULL| activity.channelSession.state.name| String| varchar(255)| varchar(255)| State of the conversation (e.g. Started  
state_reason_code| NOT NULL| activity.channelSession.state.reasonCode| String| varchar(255)| varchar(255)| Reason code for state (e.g. Customer)  
start_time| NOT NULL| activity.data.startTime| Date| DATETIME(3)| DATETIME(3)| Start time of the conversation  
end_time| NOT NULL| activity.data.endTime| Date| DATETIME(3)| DATETIME(3)| End time of the conversation  
total_duration| NOT NULL| activity.date.duration| Int64| Int| Int| Total duration of the conversation  
conversation_hold_time| NOT NULL| activity.data.holdTime| Double| Int| Int| Total hold time of the conversation  
sender_id| NOT NULL| activity.data.callLegs.sender.id| String| varchar(255)| varchar(255)| Unique field for sender id/Agent id  
sender_type| NOT NULL| activity.data.callLegs.sender.type| String| varchar(255)| varchar(255)| Type of sender (e.g. agent, bot)  
sender_name| NOT NULL| activity.data.callLegs.sender.name| String| varchar(255)| varchar(255)| Name of the sender/agent  
call_leg_start_direction| NOT NULL| activity.data.callLegs.startDirection| String| varchar(255)| varchar(255)| Start direction for call leg (e.g. Inbound/Outbound)  
call_leg_end_direction| NOT NULL| activity.data.callLegs.endDirection| String| varchar(255)| varchar(255)| End direction for call leg (e.g. Transfer/Direct Transfer/ Dialog Ended)  
call_leg_start_time| NOT NULL| activity.data.callLegs.startTime| Date| DATETIME(3)| DATETIME(3)| Start time for the call leg  
call_leg_end_time| NOT NULL| activity.data.callLegs.endTime| Date| DATETIME(3)| DATETIME(3)| End time for the call leg  
call_leg_duration| NOT NULL| activity.data.callLegs.duration| Int64| Int| Int| Duration of the call leg  
recordCreationTime| NOT NULL| recordCreationTime| Date| DATETIME(3)| DATETIME(3)| Time when record was created  
timestamp| NOT NULL| timestamp| Date| DATETIME(3)| DATETIME(3)| Time stamp of the activity  
_etl_inserted_at| NOT NULL| | | DATETIME(3)| DATETIME(3)| Date and time when the ETL was run and data was inserted in table  
  
### Voice_connector_activities

This table records the details of the voice connector activities data

**Field**| **Constraint**| **Source Field ( MongoDB)**| **Source Data Type ( MongoDB)**| **MySQL Data Type**| **MSSQL Data Type**| **Description**  
---|---|---|---|---|---|---  
activity_id| PK, NOT NULL| activity._id| Object ID| varchar(255)| varchar(255)| Primary-Key: Unique field for activity id  
activity_name| NOT NULL| activity.name| String| varchar(255)| varchar(255)| Name of activity (e.g. Third_party_activity)  
activity_type| NOT NULL| activity.type| String| varchar(255)| varchar(255)| Type of activity  
activity_timestamp| NOT NULL| activity.timestamp| String| DATETIME(3)| DATETIME(3)| Timestamp of activity  
event_emitter_id| NOT NULL| activity.eventEmitter.id| String| varchar(255)| varchar(255)| Unique field for event emitter id  
event_emitter_type| NOT NULL| activity.eventEmitter.type| String| varchar(255)| varchar(255)| Type of event emitter (e.g. Connector)  
sender_name| NOT NULL| activity.eventEmitter.senderName| String| varchar(255)| varchar(255)| Name of the sender (e.g CX-Voice-Connector)  
customer_id| NOT NULL| docuemnt.customerId| String| varchar(255)| varchar(255)| Unique field for customer id  
customer| NOT NULL| activity.data.header.customer| Object| JSON| nvarchar(max)| Array containing customer information  
channel_session_id| NOT NULL| activity.channelSession._id| Object ID| varchar(255)| varchar(255)| Unique field for channel session id  
participant_type| NOT NULL| activity.channelSession.participantType| String| varchar(255)| varchar(255)| Type of participant (e.g. Channel Session)  
channel_id| NOT NULL| activity.channelSession.channel._id| Object ID| varchar(255)| varchar(255)| Unique field for channel id  
tenant_id| NOT NULL| activity.channelSession.channel.tenant._id| Object ID| varchar(255)| varchar(255)| Unique field for tenant id  
channel_config_id| NOT NULL| activity.channelSession.channel.channelConfig._id| Object ID| varchar(255)| varchar(255)| Unique field for channel config id  
channel_connector_id| NOT NULL| activity.channelSession.channel.channelConnector._id| Object ID| varchar(255)| varchar(255)| Unique field for channel connector id  
channel_type_id| NOT NULL| activity.channelSession.channel.channelType._id| Object ID| varchar(255)| varchar(255)| Unique field for channel type id  
scheduling_meta_data| NOT NULL| activity.data.header.schedulingMetaData| Object| JSON| nvarchar(max)| Array containing scheduling meta data  
activity_data_id| NOT NULL| activity.data.id| String| varchar(255)| varchar(255)| Unique field for activity data id  
sender_id| NOT NULL| activity.data.header.sender.id| String| varchar(255)| varchar(255)| Unique filed for sender id  
sender_type| NOT NULL| activity.data.header.sender.type| String| varchar(255)| varchar(255)| Type of sender (e.g. Connector)  
channel_customer_identifier| NOT NULL| activity.data.header.channelData.channelCustomerIdentifier| String| varchar(255)| varchar(255)| Unique customer identifier  
service_identifier| NOT NULL| activity.data.header.channelData.serviceIdentifier| String| varchar(255)| varchar(255)| Service identifier for CX  
message_type| NOT NULL| activity.data.body.type| String| varchar(255)| varchar(255)| Type of message (e.g. Delivery Notification)  
message_id| NOT NULL| activity.data.body.id| String| varchar(255)| varchar(255)| Unique field for message id  
message_text| NULL| activity.data.body.messageText| NULL| TEXT| TEXT| Message Text  
status| NOT NULL| activity.data.body.status| String| varchar(255)| varchar(255)| Status (e.g. Connected)  
reason_code| NOT NULL| activity.data.body.reasonCode| String| varchar(255)| varchar(255)| Reason Code (e.g. Normal clearing)  
room_id| NOT NULL| activity.roomInfo._id| Object ID| varchar(255)| varchar(255)| Unique field for room id  
room_mode| NOT NULL| activity.roomInfo.mode| String| varchar(255)| varchar(255)| Room mode (e.g. Contact center)  
timestamp| NOT NULL| timestamp| Date| DATETIME(3)| DATETIME(3)| Timestamp of the activity  
recordCreationTime| NOT NULL| recordCreationTime| Date| DATETIME(3)| DATETIME(3)| Date Time when record was created  
_etl_inserted_at| NOT NULL| | | DATETIME(3)| DATETIME(3)| Date and time when the ETL was run and data was inserted in table  
  
## Campaigns

### campaigns

This table records the details of campaigns data

**Field**| **Constraint**| **Source Field ( MongoDB)**| **Source Data Type ( MongoDB)**| **MySQL Data Type**| **MSSQL Data Type**| **Description**  
---|---|---|---|---|---|---  
id| PK, NOT NULL| _id| Object ID| varchar(24)| varchar(24)| Unique field for source document  
flow_id| NOT NULL| flowId| String| varchar(255)| varchar(255)| Unique field for flow id  
title| NOT NULL| title| String| varchar(255)| varchar(255)| Title of the campaign  
number_of_contacts| NOT NULL| numberOfContacts| Int(32)| Int| Int| Number of contacts in the campaigns  
sources| NOT NULL| sources| Array| JSON| nvarchar(max)| Sources array of the campaigns  
status| NOT NULL| status| String| varchar(100)| varchar(100)| Status of the campaign  
created_at| NOT NULL| createdAt| Date| DATETIME(3)| DATETIME(3)| Date and time when the campaign was created  
updated_at| NOT NULL| updatedAt| Date| DATETIME(3)| DATETIME(3)| Date and time when the campaign was updated  
version| NOT NULL| __v| Int(32)| Int| Int| Version  
_etl_inserted_at| NOT NULL| | | DATETIME(3)| DATETIME(3)| Date and time when the ETL was run and data was inserted in table  
  
### campaign_scheduler

This table records the details of the campaign scheduler data.

**Field**| **Constraint**| **Source Field ( MongoDB)**| **Source Data Type ( MongoDB)**| **MySQL Data Type**| **MSSQL Data Type**| **Description**  
---|---|---|---|---|---|---  
activity_id| PK, NOT NULL| activity._id| Object ID| varchar(255)| varchar(255)| Unique field for activity id  
name| NOT NULL| activity.name| String| varchar(255)| varchar(255)| Name of the activity  
type| NOT NULL| activity.type| String| varchar(255)| varchar(255)| Type of the activity  
activity_timestamp| NOT NULL| activity.timestamp| Date| DATETIME(3)| DATETIME(3)| Date and time of the activity  
event_emitter_id| NOT NULL| activity.eventEmitter.id| String| varchar(255)| varchar(255)| Unique field for event emitter id  
event_emitter_type| NOT NULL| activity.eventEmitter.type| String| varchar(255)| varchar(255)| Type of event emitter  
sender_name| NOT NULL| activity.eventEmitter.senderName| String| varchar(255)| varchar(255)| Name of the sender  
customer_id| NOT NULL| document.customerId| String| varchar(255)| varchar(255)| Unique field for customer id  
customer| NOT NULL| activity.channelSession.customer| Object| JSON| nvarchar(max)| Object containing all the information of the customer  
channel_session_id| NOT NULL| activity.channelSession._id| Object ID| varchar(255)| varchar(255)| Unique field for channel session id  
participant_type| NOT NULL| activity.channelSession.type| String| varchar(255)| varchar(255)| Type of the participant  
channel_id| NOT NULL| activitiy.channelSession.channel._id| Object ID| varchar(255)| varchar(255)| Unique field for channel id  
default_outbound| NOT NULL| activity.channelSession.channel.defaultOutbound| Boolean| tinyint(1)| bit| Default Outbound (True/False)  
tenant_id| NOT NULL| activity.channelSession.channel.tenant._id| Object ID| varchar(255)| varchar(255)| Unique field for tenant id  
channel_config_id| NOT NULL| activity.channelSession.channel.channelConfig._id| Object ID| varchar(255)| varchar(255)| Unique field for channel config id  
channel_connector_id| NOT NULL| activity.channelSession.channel.channelConnector._id| Object ID| varchar(255)| varchar(255)| Unique field for channel connector id  
channel_type_id| NOT NULL| activity.channelSession.channel.channelType._id| Object ID| varchar(255)| varchar(255)| Unique field for channel type id  
is_interactive| NULL| activity.channelSession.channel.channelType.isInteractive| Boolean| tinyint(1)| bit| Is interactive (True/False)  
is_active| NOT NULL| activity.channelSession.isActive| Boolean| tinyint(1)| bit| Is active (True/False)  
scheduling_meta_data| NOT NULL| activity.data.header.schedulingMetadat| Object| JSON| nvarchar(max)| Object containing scheduling meta data  
activity_data_id| NOT NULL| activity.data.id| String| varchar(255)| varchar(255)| Unique field for activity id  
sender_id| NOT NULL| activity.data.header.sender.id| String| varchar(255)| varchar(255)| Unique field for sender id  
sender_type| NOT NULL| activity.data.header.sender.type| String| varchar(255)| varchar(255)| Type of sender  
channel_customer_identifier| NOT NULL| activity.data.header.channelData.channelCustomerIdentifier| String| varchar(255)| varchar(255)| Channel customer identifier  
service_identifier| NOT NULL| activity.data.header.channelData.serviceIdentifier| String| varchar(255)| varchar(255)| Service identifier for CX  
message_type| NOT NULL| activity.data.body.type| String| varchar(255)| varchar(255)| Type of message  
messageId| NULL| | | varchar(255)| varchar(255)| Unique field for message id  
message_text| NULL| activity.data.body.messageText| String| Text| Text| Text of the message  
status| NULL| | | varchar(255)| varchar(255)| Status  
reason_code| NULL| activity.data.body.reasonCode| Null| varchar(255)| varchar(255)| Reason code  
call_id| NULL| activity.data.body.callId| Null| varchar(255)| varchar(255)| Unique field for call id  
room_id| NOT NULL| activity.roomInfo._id| Object ID| varchar(255)| varchar(255)| Unique field for room id  
room_mode| NOT NULL| activity.roomInfo.mode| String| varchar(255)| varchar(255)| Room mode  
timestamp| NOT NULL| timestamp| Date| DATETIME(3)| DATETIME(3)| Time stamp  
recordCreationTime| NOT NULL| recordCreationTime| Date| DATETIME(3)| DATETIME(3)| Date Time when record was created  
_etl_inserted_at| NOT NULL| | | DATETIME(3)| DATETIME(3)| Date and time when the ETL was run and data was inserted in table.  
  
## Messages

### messages_bronze

This table records the complete raw details of the message level data.

**Field**| **Constraint**| **Source Field ( MongoDB)**| **Source Data Type ( MongoDB)**| **MySQL Data Type**| **MSSQL Data Type**| **Description**  
---|---|---|---|---|---|---  
id| PK, NOT NULL| _id| ObjectId| varchar(255)| varchar(255)| Identifier for MongoDB document.  
customer_id| NOT NULL| customerId| String| varchar(255)| varchar(255)| Unique identifier for customer  
conversation_id| NOT NULL| conversationId| String| varchar(255)| varchar(255)| Unique identifier for conversation  
channel_session_id| NOT NULL| channelSessionId| String| varchar(255)| varchar(255)| Unique identifier for channel session  
channel_session_direction| NOT NULL| channelSession.channelSessionDirection| String| varchar(255)| varchar(255)| Shows the channel session direction (Inbound/Outbound)  
activity_id| NOT NULL| activity._id| ObjectId| varchar(255)| varchar(255)| Unique identifier for activity  
activity_name| NOT NULL| activity.name| String| varchar(255)| varchar(255)| Activity name showing the type of message (e.g. customer_message, agent_message, bot_message)  
activity_type| NOT NULL| activity.type| String| varchar(255)| varchar(255)| Shows the type of activity. (in this case this is ‘Message’)  
activity_timestamp| NOT NULL| activity.timestamp| Date| DATETIME(3)| DATETIME(3)| Timestamp for activity  
event_emitter_type| NOT NULL| eventEmitter.type| String| varchar(255)| varchar(255)| Type of event emitter (e.g. Bot, Customer, Agent)  
channel_name| NOT NULL| channelSession.channel.name| String| varchar(255)| varchar(255)| Channel Name (e.g. CX voice, web, Facebook etc)  
channel_customer_identifier| NOT NULL| data.header.channelData.channelCustomerIdentifier| String| varchar(255)| varchar(255)| Unique customer identifier  
service_identifier| NOT NULL| data.header.channelData.serviceIdentifier| | varchar(255)| varchar(255)| Service identifier for CX  
channel_mode | NOT NULL| channelSession.channel.channelConfig.channelMode| String| varchar(255)| varchar(255)| Indicates the channel mode for this channel

  * **HYBRID** \- Both the bot and the human agents are engaged on communication with the customer. 
  * **BOT** \- Only bot is engaged in communication with the customer. 
  * **AGENT** \- Only human agents are engaged in communication with the customer. 

  
routing_mode| NOT NULL| channelSession.channel.channelConfig.routingPolicy.routingMode| String| varchar(255)| varchar(255)| This records one of the following outing modes.

  * **PUSH** : The incoming request was pushed to a queue to be routed to agents.
  * **PULL** : Broadcasted to a Pull-based List to be taken up by any agents subscribed to the List.

  
agent_selection_policy| NOT NULL| channelSession.channel.channelConfig.routingPolicy.agentSelectionPolicy| String| varchar(255)| varchar(255)| Shows the agent selection policy for agent engagement in the conversation (e.g. LONGEST_AVAILABLE)   
state_name| NOT NULL| channelSession.state| String| varchar(255)| varchar(255)| State of the conversation (e.g. Started)  
state_reason_code| NOT NULL| channelSession.reasonCode| String| varchar(255)| varchar(255)| Reason code for state change (e.g. Customer)  
customer_name| NOT NULL| channelSession.customer.firstName| String| varchar(500)| varchar(500)| Records the customer name with whom this conversation is associated.  
sender_id| NOT NULL| data.header.sender.id| String| varchar(255)| varchar(255)| Unique field for sender id/Agent id  
sender_type| NOT NULL| data.header.sender.type| String| varchar(255)| varchar(255)| Type of sender (e.g. agent, bot)  
sender_name| NOT NULL| data.header.sender.name| String| varchar(255)| varchar(255)| Name of the sender/agent  
action_message| NULL| activity.data.name| String| varchar(255)| varchar(255)| Shows the action message sent in the system (if available)  
action_message_data| NULL| activity.data.data| String| JSON| JSON| JSON Array containing raw data regarding the associated action message  
body| NOT NULL| activity.data.body| String| JSON| JSON| JSON Array containing all the raw data for the associated message. (Message text, Message type etc)  
room_id| NOT NULL| activity.roomInfo._id| ObjectId| varchar(255)| varchar(255)| Unique identifier for room  
room_mode| NOT NULL| activity.roomInfo.mode| String| varchar(255)| varchar(255)| Room mode (e.g. Contact center)  
channel_tenant_id| NOT NULL| channelSession.channel.tenant._id| ObjectId| varchar(255)| varchar(255)| Unique identifier for the channel tenant  
tenant_id| NOT NULL| | | varchar(255)| varchar(255)| Unique identifier for tenant. (Hard-coded to ‘expertflow’)  
recordCreationTime| NOT NULL| recordCreationTime| Date| DATETIME(3)| DATETIME(3)| Time when record was created in MongoDB  
timestamp| NOT NULL| timestamp| Date| DATETIME(3)| DATETIME(3)| Timestamp of the activity  
_etl_inserted_at| NOT NULL|  |  | DATETIME(3)| DATETIME(3)| Date and time when the ETL was run and data was inserted in table.  
  
For further schema of Messages data please check the following docs:

  * Silver Layer Tables (<https://expertflow-docs.atlassian.net/wiki/x/CAAKSw> )



