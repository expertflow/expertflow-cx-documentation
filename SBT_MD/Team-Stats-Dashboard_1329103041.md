# CX Knowledgebase : Team Stats Dashboard

Provides real-time insights into queue statistics, agent states, bot activity, channel distribution, and call trends.  
  
This updated  Summary Dashboard helps supervisors and managers track service levels, workload distribution, and agent/bot performance across multiple channels.

## **_Dashboard Structure_**

The dashboard consists of three main sections:

  1. **Queue Stats**

  2. **Agent & Channel States**

  3. **Bot Activity & Call Trends**




## **1\. Queue Stats**

This section displays performance metrics for queues and customer interactions.

### **_Panels_**

  * **Service Level %:** Shows the service level percentage of selected queues. Calculated from the number of answered interactions within the defined threshold versus total offered.

  * **Active with Agents:** Displays the number of conversations currently being handled by agents.

  * **Active with Bots:** Shows the number of conversations currently being handled by bots.

  * **Abandon Rate:** Percentage of customers who left the queue before being answered.




-**Answer Wait Time:** Average time customers waited before being answered. Format: HH:MM:SS.

  * **Average Handle Time (AHT):** Average duration agents spend handling tasks.




  
Formula: Total Handled Duration ÷ Total Handled Tasks

  * **Queue Performance Table:** Provides detailed statistics per queue for the associate **team** :

  * Queue Name

  * Channel

  * Total Queued

  * Answered

  * Abandoned

  * Service Level % (SL %)

  * Avg Wait

  * Max Wait




## **2\. Agent & Channel States**

This section shows real-time distribution of agent states and channel usage.

  * **Agent States (Pie Chart):** Displays the count of agents in different MRD states:

  * Not Ready

  * Ready

  * Active

  * Busy

  * Pending Not Ready

  * **Channel Category Distribution (Pie Chart):** Shows interactions by channel type:

  * Chat

  * LinkedIn

  * Voice




## **3\. Bot Activity & Call Trends**

This section monitors bot workloads and customer call flow.

  * Bot Activity Table: For each bot, the following metrics are displayed:

  * Bot Name

  * Channel

  * Assigned (conversations given to bot)

  * Completed (successfully handled by bot)

  * Escalated to Agent (handed off to a human agent)

  * Avg Response Time

  * **Calls Trends (Bar Graph):** Displays call routed to the queue over time, helping identify performance for customer interactions.




### **Filters**

  * **Team Name –** Select the team to monitor queues and activities.

  * **Queue Name –** Select one or multiple queues to view queue statistics.

  * **MRD Name –** Filter agent states by Media Routing Domain (MRD).

  * **Bot Name –** View conversations assigned to a specific bot.




**Agent active, bot active, and Agent States** panels show real-time values, and other panels **like Service Level, Answer Wait Time, and AHT etc** are calculated from historical reporting data and may update with a delay based on ETL interval (default: 5 minutes).

  

