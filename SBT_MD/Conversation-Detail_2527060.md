# CX Knowledgebase : Conversation Detail

**Report Summary**|  Provides the details of a customer conversation including a conversation's direction, queue name, list name, start time, end time, duration, agent's name, customer's name, routing mode of the conversation, internal transferred count, external transfer, percentage of agent/bot participation, transcript, and disposition.  
---|---  
  
This detail is based on the number of activities exchanged in a conversation.

## Report Columns

**Fields**| **Description**  
---|---  
Conversation ID | The unique identifier of a customer conversation  
Calling Number| Customer Number when the direction is **INBOUND** , and using N/A when the direction is **OUTBOUND.**  
Called Number| Customer Number when the direction is **OUTBOUND** , and using **N/A** for **INBOUND** direction.  
Direction| This determines the direction of conversation **i.e.** INBOUND/OUTBOUND.There can be multiple channel sessions (INBOUND/OUTBOUND) in a conversation. We'll consider the conversation's direction based on the first channel session's direction in the conversation.   
Queue| This determines the queue(s) name on which the conversation was landed originally. This might change during the course of the conversation but this field will only show the name of the first queue on which the conversation landed.   
List Name| This determines the list(s) name on which the agent has joined the conversation in case of PULL-based conversation.  
Start Time| This determines the start time of the conversation. This is the actual time when the customer started the conversation.  
End Time| This determines the time when the conversation was actually closed   
Duration | The elapsed time between the start time and end time of the complete conversation  
Agent(s) Name| Names of agent(s) who participated in the conversation. It could be multiple agents joining the same conversation such as a pull-based request and conferenced conversation being joined by 2 or more agents or agent-initiated conversations where more than one agent can start a conversation with the same customer.   
Wrap up Reason(s)| This shows the wrap-ups (wrapup_category & wrapup_label) applied to a conversation by one or more agents who have joined the conversation.  
Notes| This shows the Notes entered during a conversation by the agent who has joined the conversation.  
Customer's Name| Name of the customer who initiated the conversation.  
Routing Mode| This shows the routing mode of the conversation if it is PULL Mode or PUSH Mode.  
Transferred Count| This is the number of times this conversation has been transferred internally.  
External Direct Transfer| This indicates that the count is one when the conversation is being externally transferred.  
External Consult Transfer| This indicates that the count is one when the conversation is being external consult transfers.  
% Bot participation| Calculated by the number of messages sent by the bot on the conversation  
% Agent participation| Calculated by the number of messages sent by the agent during the conversation  
Transcript| This field gives the option to View or Download the conversation transcript.  
Disposition| This determines the disposition of the conversation from the **disposition** column of the **conversation** table, which could be one of the following: 

  * **In case of inbound:**
    * **Agent Handled** \- If the latest agent task for this conversation has the state CLOSED, with reason code DONE, it is considered as Agent Handled. This is the case when the agent has successfully answered the queries of the customer and closes the conversation from the Agent Desk front-end.
    * **Bot Handled** \- It is when the conversation was actually closed by the bot. 
    * **Abandoned** : This normally happens when a customer leaves the conversation while waiting in the queue, or while ringing to an agent (i.e. an agent was reserved but the customer left). In this case, the agent task created for this conversation is closed with a disposition CANCELLED.
  * **In case of outbound:**
    * **Normal Clearing**  
A conversation that ended normally without any issues or interruptions.
    * **Customer**  
A conversation that was ended by the customer.
    * **Inactivity**  
A conversation that was automatically closed because the customer became inactive.
    * **Agent**  
A conversation that was ended by the agent.
    * **User Busy**  
A conversation where the customer did not answer or was busy.
    * **Forced Closed**  
A conversation closed when the agent exited the browser tab while the task was still active.
    * **Network**  
A conversation that ended due to a customer’s network issue.
    * **Decline**  
A conversation where the customer ended it before responding.
    * **Unknown**  
A conversation with an undetermined or unclassified disposition.

See [Reporting Database Schema -> conversation ](Reporting-Database-Schema_2526317.html)table for more details about the conversation dispositions. For each agent joining a conversation, a new agent task is created. Since multiple agents can join a conversation, there can be multiple agent tasks created in the conversation (i.e. whenever a new agent is added). All of these tasks are sorted and the disposition of the latest tasks' are considered for determining the disposition of the conversation.  
  
## Report Filters 

  * Date/Time - select the date you want to see the data for.

  * Agent Name - select a name from a dropdown list of agent names. These names appear based on the data available in reports.

  * Queue - select the name of the queue(s) you want to see the data for.

  * List - select the name of the list(s) you want to see the data for.




![msedge_vTrujwjJhx.gif](attachments/2527060/1027342357.gif?width=1511)
