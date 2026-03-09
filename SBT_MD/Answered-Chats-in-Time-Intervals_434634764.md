# CX Knowledgebase : Answered Chats in Time Intervals

**Report Summary**|  Show all conversation tasks handled/answered by the agent on queue in different time intervals segregated by 15 minutes interval.  
---|---  
  
## Report Columns

Following are the report columns

**Fields**| **Description**  
---|---  
Queue| Shows the name of the queue.  
DateTime| Shows the date and time of interval (30 minutes).  
Average Speed of Answer| Shows the average time it takes to answer chats/calls after being reserved within the 30 minutes time interval.   
This is the average speed of answer (the time it takes the agent to accept the task since it began ringing on the Agent Desk. This will be calculated asSUM (task_alert_duration)/COUNT (agent_task_id)  
**Format** hours:minutes:seconds (00:00:00)  
Average Abandoned Time| The average time a task remains in this queue before abandoned within the 30 minutes time interval..This is calculated as:`Total abandoned Duration/Total abandoned`**Format** hours:minutes:seconds (00:00:00)  
Interval (60 SEC)| Shows the 60-second interval time in minutes like **01:00** (Always Static).   
Answered 60 SEC| Count of total number of chats/calls answered by agents within a 60-second queue time.  
Abandoned 60 SEC| Count of total number of chats/calls abandoned in the queue within a 60-second queue time.  
Interval (120 SEC)| Shows the 120-second interval time in minutes like **02:00** (Always Static).  
Answered 120 SEC| Count of total number of chats/calls answered by agents within a 120-second queue time.  
Abandoned 120 SEC| Count of total number of chats/calls abandoned in the queue within a 120-second queue time.  
Interval (180 SEC)| Shows the 180-second interval time in minutes like **03:00** (Always Static).  
Answered 180 SEC| Count of total number of chats/calls answered by agents within a 180-second queue time.  
Abandoned 180 SEC| Count of total number of chats/calls abandoned in the queue within a 180-second queue time.  
Interval (240 SEC)| Shows the 240-second interval time in minutes like: **04:00** (Always Static).  
Answered 240 SEC| Count of total number of chats/calls answered by agents within a 240-second queue time.  
Abandoned 240 SEC| Count of total number of chats/calls abandoned in the queue within a 240-second queue time.  
Interval (OVER 240 SEC)| Shows the over 240-second interval time in minutes like: **> 04:00** (Always Static).  
Answered OVER 240 SEC| Count of total number of chats/calls answered by agents over a 240-second queue time.  
Abandoned OVER 240 SEC| Count of total number of chats/calls abandoned in the queue over a 240-second queue time.  
Total Answered| Count of total number of answered chats/calls in queue within the 30 minutes time interval.  
Total Abandoned| Count of total number of abandoned chats/calls in queue within the 30 minutes time interval.  
MAX Queued| Count of total chats/calls landed in queue within the 30 minutes time interval.  
Longest Queued| The maximum time a chats/calls spend in the queue within the 30 minutes time interval.This will be calculated asmax(task_queue_time)**Format** hours:minutes:seconds (00:00:00)  
  
![Answered Chats in Time Intervals.gif](attachments/434634764/434274447.gif?width=1154)

## Report Filters

The following report filters are available

  * Date/Time - Choose the date to filter out the data. You may also select the date ranges to see the data falling under the said period

  * Queues - Select the name/names of the queues you want to see the data for.



