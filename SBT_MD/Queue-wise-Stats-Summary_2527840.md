# CX Knowledgebase : Queue-wise Stats Summary

**Report Summary**|  Provides the count of requests received per queue, such as the number of chats or calls in case of voice offered, DONE, cancelled, transferred, etc., to view and analyze the performance of queues.   
---|---  
  
This count of requests may be different from the count of conversations.

The queue-based reports are developed based on agent tasks that are created each time a conversation is queued to a queue (and are not based on conversations). This means multiple agent tasks can be created for a single conversation in case the conversation is routed and rerouted to agents, one after the other.

See [Reporting Database Schema - Agent task](Reporting-Database-Schema_2526317.html#agent_task) to see details of agent tasks.

## Report Columns

Following are the report columns: 

**Fields**| **Description**  
---|---  
Queue name| The name of the queue  
Date| Shows week number and date in the following way as per the View of the report. | **Fields**| **Description**  
---|---  
Week Number| Shows week number in case of Weekly View  
Date| Shows date in case of Date-wise View and Interval View  
  
Weekly View| Shows the date of Week Start and the date of Week End in their respective columns  
Interval View| Shows the time of Interval Start and the time of Interval End in their respective columns  
Total Offered| The total number of offered tasks per queue.  
Done| The count of tasks that have the disposition DONE  
Cancelled| Shows the count of tasks that have the disposition CANCELLED (where the customer left in the queue or while ringing the chat/call on the agent)  
Transferred out| Shows the count of tasks transferred out from this particular queue  
External Direct Transfer| Shows the count of tasks external transfer from this particular queue  
External Consult Transfer| Shows the count of tasks external consult transfer from this particular queue  
RONA| Shows the count of tasks that are closed due to RONA disposition  
No Agent Available| Shows the count of tasks that are closed due to No Agent Available disposition  
Agent Logout| Shows the count of tasks that are closed due to 'Agent Logged Out' disposition  
Force Closed| Shows the count of tasks that are closed due to FORCE_CLOSED disposition  
Reroute| Shows the count of tasks that are closed due to "REROUTE" disposition  
Response Timeout| Shows the count of tasks that are closed due to "RESPONSE_TIMEOUT" disposition  
Unkown| Shows the count of tasks disposition that are unknown.  
Minimum Queue Duration| The minimum time a task remains in the queue. This is calculated as:(task_reserved_time - task_queue_time)**Format** hours:minutes:seconds (00:00:00)  
Maximum Queue Duration| The maximum time a task remains in the queue. This is calculated as:(task_reserved_time - task_queue_time)  
  
**Format** hours:minutes:seconds (00:00:00)  
Average Queue Duration | The average time a task remains in this queue while waiting to be routed to an agentThis is calculated as:`Total Queue Duration/Total Offered` **Format** hours:minutes:seconds (00:00:00)  
Total Queue Duration| Total time tasks remains in this queue while waiting to be routed to an agent.(task_reserved_time - task_queue_time)**Format** hours:minutes:seconds (00:00:00)  
Minimum Handled Duration| The minimum time it took to handle a task on this queue. This is the shortest of all task handling times. For a single task, it is calculated as:`min ( task_end_time - task_answered_time)`Task answer time is when the agent answered it.  
Task end time is when the task is closed.**Format** hours:minutes:seconds (00:00:00)  
Maximum Handled Duration| The maximum time it took to handle a task on this queue. This is the longest of all task handling times. For a single task, it is calculated as:`Max ( task_end_time - task_answered_time)`Task answer time is when the agent answered it.  
Task end time is when the task is closed.**Format** hours:minutes:seconds (00:00:00)  
Average Handled Duration | The average time any agent takes to handle a task in this queue.Handled duration is equal to:`(task_end_time - task_answered_time)` in  [**Reporting Database Schema - >** **agent_task**](Reporting-Database-Schema_2526317.html) table**Format** hours minutes seconds (00 00 00)The average handled duration is calculated as:`Total Handled Duration / Total Handled Task`  
Total Handled Duration| Total time to handle all tasks in this queue.`sum ( task_end_time - task_answered_time)`Task answer time is when the agent answered it.  
Task end time is when the task is closed.**Format** hours:minutes:seconds (00:00:00)  
Answered Within SL| A count of all tasks that were answered within the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Answered After SL| A count of all tasks that were answered after the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Abandoned Within SL| A count of all tasks that were abandoned in the queue within the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Abandoned After SL| A count of all tasks that were abandoned after the [Service Level threshold](Key-Reporting-Metrics_2526622.html)  
Service Level%| Service Level % of the queue.This is calculated as per the Service Level Type value set in the queue definition on the Unified Admin application. See the [Administrator Guide](Unified-Admin-Guide_2524407.html) to learn more about Service Level configuration.Based on one of the following values specified in the Service Level Type field, the Service Level is calculated as follows:

  * **1** \- **Ignore Abandoned Chats** \- If Service Level Type = 1 THEN `(AnsweredWithinSL/(TotalOffered - AbandonedWithin SL)) * 100`
  * **2** \- **Abandoned Chats have Negative Impact** \- If Service Level Type = 2 THEN 

`(AnsweredWithin SL/TotalOffered) * 100`

  * **3** -__**Abandoned Chats have Positive Impact** \- If Service Level Type = 3 THEN `((AnsweredWithinSL + AbandWithinSL)/TotalOffered) * 100`

For more details on SLA calculations, see [Key Reporting Metrics](Key-Reporting-Metrics_2526622.html) and [SLA Calculations](SLA-Calculations_2525629.html)  
%Answered within Service Level | A percentage of all tasks that were answered within the  [Service Level threshold](Key-Reporting-Metrics_2526622.html) This is calculated as:`AnsweredWithinSL/Total Answered`  
%Abandoned within Service Level| A percentage of all tasks that were abandoned within the  [Service Level threshold](Key-Reporting-Metrics_2526622.html) `AbandonedWithinSL/Total Abandoned`  
%Answered after Service Level| A percentage of all tasks that were answered after the  [Service Level threshold](Key-Reporting-Metrics_2526622.html) `AnsweredAfterSL/Total Answered`  
%Abandoned after Service Level | A percentage of all tasks that were abandoned after the  [Service Level threshold](Key-Reporting-Metrics_2526622.html) `AbandonedAfterSL/Total Abandoned`  
Minimum Abandoned Duration| The minimum time a task remains in this queue before being abandoned.**Format** hours:minutes:seconds (00:00:00)  
Maximum Abandoned Duration| The maximum time a task remains in this queue before being abandoned.**Format** hours:minutes:seconds (00:00:00)  
Average Abandoned Duration| The average time a task remains in this queue before being abandoned.This is calculated as:`Total abandoned Duration/Total abandoned`**Format** hours:minutes:seconds (00:00:00)  
Total Abandoned Duration| Total time tasks remain in this queue before abandoned.**Format** hours:minutes:seconds (00:00:00)  
  
![](attachments/2527840/1027506183.gif?width=813)

## Report Views

  * Weekly view - shows week-wise data in this view. You can select the week number from the filters to select the weeks that are required to be viewed in the reports 

  * Date-wise view - date-wise data. You can also select date ranges in the filter to show the data for the selected range

  * Interval view - Data of a 15-minute interval. This interval is currently hardcoded in the report backend.




## Report Filters

The following report filters are available for filtering the reporting data:

  * Queue - select the name of the queue(s) you want to see the data for. This filter is applicable to view all three tabs of the report; i.e., Weekly View, Day-wise View, and Interval View. 

  * Select Date - choose the date for which you want to filter out the data. You may also select date ranges to see the data falling under the said period. This filter is only applicable to the tabs, **Date-wise view,** and **Interval view**. In the case of an Interval, it filters out the interval-based data of only the specified date or date range. 

  * Week number - this filter allows you to filter out the data for particular weeks of the current year. It is only applicable to the **Weekly View** tab of the report. When specified, the report populates the data of only the specified week numbers in the Weekly view. 



