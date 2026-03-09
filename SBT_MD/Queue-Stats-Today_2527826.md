# CX Knowledgebase : Queue Stats Today

**Report Summary**|  Provides statistics of a queue for the current day since midnight  
---|---  
  
Includes tasks offered, handled, transferred, and SLA % on a given queue for today. 

The queue-based reports are developed based on Agent Tasks that are created each time a conversation is queued to a queue (and is not based upon conversations).

See [Reporting Database Schema -> agent_task](Reporting-Database-Schema_2526317.html) to see details of agent tasks.

## Report Columns

Following are the report columns:

**Fields**| **Description**  
---|---  
Queue name| The name of the queue  
Date| Shows the date  
Total Offered| Total offered tasks to the queue since midnight   
Done| The count of tasks that have the disposition DONE  
Cancelled| The count of tasks that have the disposition CANCELLED (where the customer left in queue or while ringing the chat on agent)  
Transferred Out| Shows the count of tasks transferred out from this particular queue  
External Direct Transfer| Shows the count of tasks externally transferred from this particular queue  
External Consult Transfer| Shows the count of tasks external consult transfer from this particular queue  
RONA| Shows the count of tasks that are close due to  RONA disposition  
No Agent Available| Shows the count of tasks that are closed due to No Agent Available disposition  
Agent Logout| Shows the count of tasks that are closed due to 'Agent Logged Out' disposition  
Force Closed| Shows the count of tasks that are closed due to  FORCE_CLOSED disposition  
Reroute| Shows the count of tasks that are closed due to "REROUTE" disposition  
Response Timeout| Shows the count of tasks that are closed due to  "RESPONSE_TIMEOUT" disposition  
Minimum Queue Duration| The minimum time a task waited in the queue since midnight. This is calculated as:(task_reserved_time - task_queue_time)**Format** hours:minutes:seconds (00:00:00)  
Maximum Queue Duration| The maximum time a task waited in the queue since midnight. This is calculated as:(task_reserved_time - task_queue_time)**Format** hours:minutes:seconds (00:00:00)   
Average Queue Duration | The average time a task remains in this queue while waiting to be routed to an agent  
This is calculated as:`Total Queue Duration/Total Offered` **Format** hours:minutes:seconds (00:00:00)   
Total Queue Duration| Total time tasks waited in the queue since midnight. This is calculated as:(task_reserved_time - task_queue_time)**Format** hours:minutes:seconds (00:00:00)   
Minimum Handled Duration| The minimum time duration that it took to handle a task on this queue. This is the shortest of all tasks handling time. For a single task, it is calculated as:min ( task_end_time - task_answered_time)Task Answered Time: when the agent answered itTask End Time: when the task is closed**Format** hours:minutes:seconds (00:00:00)  
Maximum Handled Duration | The maximum time duration that it took to handle a task on this queue. This is the longest of all tasks handling time. For a single task, it is calculated as:Max ( task_end_time - task_answered_time)  
  
Task Answered Time: when the agent answered itTask End Time: when the task is closed**Format** hours:minutes:seconds (00:00:00)  
Average Handled Duration | The average time an agent takes to handle a task of this queue.Handled duration is equal to:`(task_end_time - task_answered_time)` in [**Reporting Database Schema - >** **agent_task**](Reporting-Database-Schema_2526317.html) table**Format** hours:minutes:seconds (00:00:00) In case if a conversation was joined and handled by multiple agents, the conversation's total handled duration is a sum of the handle durations of all agent tasks (created for each agent who joined the conversation).The average handled duration is calculated as:`Total Handled Duration/ Total Handled` This handle time might not be equal to the total conversation duration (since a conversation may remain active with the bot even after the agent left the conversation).  
Total Handled Duration| Total time duration that it took to handle all tasks on this queue. This is the total handling time for all tasks. It is calculated as:sum ( task_end_time - task_answered_time)Task Answered Time: when the agent answered itTask End Time: when the task is closed**Format** hours:minutes:seconds (00:00:00)  
Answered Within SL| A count of all tasks that were answered within the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Answered After SL| A count of all tasks that were answered after the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Abandoned Within SL| A count of all tasks that were abandoned within the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Abandoned After SL| A count of all tasks that were abandoned after the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Service Level%| Service Level % of the queue.This is calculated as per the Service Level Type value set in the queue definition on the Unified Admin application. See the [Administrator Guide](Unified-Admin-Guide_2524407.html) to learn more about Service Level configuration.Based on one of the following values specified in the Service Level Type field, the Service Level is calculated as the following:

  * **1** \- **Ignore Abandoned Chats** \- If Service Level Type = 1 THEN `(AnsweredWithinSL/(TotalOffered - AbandonedWithin SL)) * 100`
  * **2** \- **Abandoned Chats have Negative Impact** \- If Service Level Type = 2 THEN 

`(Answered Within SL/TotalOffered) * 100`

  * **3** -__**Abandoned Chats have Positive Impact** \- If Service Level Type = 3 THEN `((AnsweredWithinSL + AbandWithinSL)/TotalOffered) * 100`

For more details on SLA calculations, see [Key Reporting Concepts](Key-Reporting-Metrics_2526622.html) and [SLA Calculations](SLA-Calculations_2525629.html)  
%Answered within Service Level | A percentage of all tasks that were answered within the Service Level threshold, as defined in the queue definition in [Unified Admin](Unified-Admin-Guide_2524407.html).This is calculated as:`AnsweredWithinSL/Total Answered`  
%Abandoned within Service Level| A percentage of all tasks that were abandoned within the [Service Level threshold](Key-Reporting-Metrics_2526622.html)`AbandonedWithinSL/Total Abandoned`  
%Answered after Service Level| A percentage of all tasks that were answered after the [Service Level threshold](Key-Reporting-Metrics_2526622.html) `AnsweredAfterSL/Total Answered`  
%Abandoned after Service Level | A percentage of all tasks that were abandoned after the [Service Level threshold](Key-Reporting-Metrics_2526622.html)`AbandonedAfterSL/Total Abandoned`  
Minimum Abandoned Duration| The minimum time a task remains in this queue before abandoned.**Format** hours:minutes:seconds (00:00:00)  
Maximum Abandoned Duration| The maximum time a task remains in this queue before abandoned.**Format** hours:minutes:seconds (00:00:00)  
Average Abandoned Duration| The average time a task remains in this queue before abandoned.This is calculated as:`Total abandoned Duration/Total abandoned`**Format** hours:minutes:seconds (00:00:00)  
Total Abandoned Duration| Total time tasks remain in this queue before abandoned.**Format** hours:minutes:seconds (00:00:00)  
  
## Report Filters

  * Queue - Select the queue(s) for which you want to see the stats for Today 




![msedge_YzUTGC3XQQ.gif](attachments/2527826/1027833880.gif?width=1511)

 _Queue Stats Today_
