# CX Knowledgebase : Historical Reports

This section describes that all listed reports are historical and only update after a conversation or channel session is closed and processed, typically every five minutes. Reports do not reflect ongoing conversations; data appears only once sessions are finalized. 

### Important

  * All reports listed in the document are historical reports. Data in the reports are only updated once a conversation or channel session becomes a part of the history. Usually, this is updated as per the ETL intervals defined during deployment. By default, this is set to 5-minute intervals.

  * A conversation that is routed to an agent won't be reflected in the historical reports below until closed by the agent from Agent Desk (in case of an external agent application, this happens when the Unsubscribed event is fired to Agent Manager to remove an agent from the conversation)

  * For all dropdown filters, note that the data is only filtered using one value and not with multiple values. So if more than one value is specified in the filters, the report records having either one of the said values will appear, but will exclude the records where both of the specified filter values exist. For instance, if an agent joined several conversations while some of them were also joined by some other agents, the results will display only the records where this agent was the only agent, while skipping those where this agent was present along with some other agents.




Below is a list of our standard reports. To get deeper insights, see the [**Reporting Database Schema**](Reporting-Database-Schema_2526317.html) to build your own custom reports.

For a better understanding of real-time data and ongoing activity, refer to the [Realtime Dashboards](Realtime-Reports-and-Dashboards_2529305.html) to provide supervisors and agents with live statistics on queues, agent states, and active conversations.

Title| Report Summary  
---|---  
[Agent & Team Leaderboard](/wiki/spaces/SBT/pages/1016234151/Agent+Team+Leaderboard)| The **Agent & Team Leaderboard** displays ranked performance data based on evaluation results. It aggregates scores across teams and agents, allowing users to compare quality performance against defined benchmarks. The report includes metrics such as the number of reviews, average scores, and score variance (standard deviation), enabling identification of top and low performers.  
[Agent Availability Report](/wiki/spaces/SBT/pages/2527630/Agent+Availability+Report)| Provides MRD-wise agent's availability statistics for each agent of the team to take necessary measures to improve the contact center performance.   
[Agent Not Ready Detail](/wiki/spaces/SBT/pages/436273153/Agent+Not+Ready+Detail)| Displays the details of all the not ready reasons of the agents.  
[Agent Not-Ready Summary](/wiki/spaces/SBT/pages/436830209/Agent+Not-Ready+Summary)| Displays the summary of all the not ready reasons of the agents.  
[Agent Performance Report](/wiki/spaces/SBT/pages/456130564/Agent+Performance+Report)| Shows the agent's key performance indicators to intervals (15 minutes).  
[Agent Productivity By Queue](/wiki/spaces/SBT/pages/2527642/Agent+Productivity+By+Queue)| Provides the concise summary of an agent's productivity by a queue, and also highlights the total number of tasks assigned to the agent per queue.  
[Agent State Analysis Report](/wiki/spaces/SBT/pages/2523192/Agent+State+Analysis+Report)| Provides a summary of the time duration of agents' state in ready or not-ready and the reason for being in a not-ready state. This helps the business to monitor the duration of the agent in each particular state for better visualization.  
[Agent Task Detail](/wiki/spaces/SBT/pages/2533148/Agent+Task+Detail)| Shows a detail of all conversation tasks handled/answered by the agent on queue including RONA.  
[Answered Chats in Time Intervals](/wiki/spaces/SBT/pages/434634764/Answered+Chats+in+Time+Intervals)| Show all conversation tasks handled/answered by the agent on queue in different time intervals segregated by 15 minutes interval.  
[Campaign Calls Detail Report](/wiki/spaces/SBT/pages/1016234087/Campaign+Calls+Detail+Report)| Shows the calls attempted by the dialer and not connected with the end user for any reason. The report includes agent-based and IVR-based campaign calls.  
[Campaign Summary](/wiki/spaces/SBT/pages/1016234024/Campaign+Summary)| Shows the summary of campaign contact status grouped by call result.  
[Channel Session Detail](/wiki/spaces/SBT/pages/2527421/Channel+Session+Detail)|  Provides the details of each individual channel session in a conversation  
[Channel Stats Graph](/wiki/spaces/SBT/pages/2532028/Channel+Stats+Graph)| Shows the percentage of channel sessions closed due to a particular disposition.  
[Channel Stats Summary](/wiki/spaces/SBT/pages/2528488/Channel+Stats+Summary)| Summarises all conversations opened for a particular channel during a particular period of time.  
[Connected Calls Detail](/wiki/spaces/SBT/pages/1016234045/Connected+Calls+Detail)| Shows the details of calls connected. It does not include any sort of abandoned calls.  
[Conversation Detail](/wiki/spaces/SBT/pages/2527060/Conversation+Detail)|  Provides the details of a customer conversation including a conversation's direction, queue name, list name, start time, end time, duration, agent's name, customer's name, routing mode of the conversation, internal transferred count, external transfer, percentage of agent/bot participation, transcript, and disposition.  
[Conversation Volume by Disposition](/wiki/spaces/SBT/pages/2532031/Conversation+Volume+by+Disposition)| Shows a bar chart display of the total number of conversations handled by Agent, Bot and Network  
[Evaluation Volume](/wiki/spaces/SBT/pages/1014530193/Evaluation+Volume)| Evaluation Volume report shows evaluation counts by status (planned, in progress, completed) for selected time periods (day, week, month, year). Data appears in both tabular and graphical view to track progress and trends.  
[Evaluator Comparison](/wiki/spaces/SBT/pages/1015546105/Evaluator+Comparison)| The **Evaluator Comparison Report** provides a visual and tabular comparison of how multiple evaluators have scored a single agent using the same evaluation form (questionnaire). It helps identify scoring variations and alignment across evaluators, supporting calibration and consistency in quality assessments. The report supports filtering by date, team, agent, and questionnaire.  
[Historical Conversation Summary](/wiki/spaces/SBT/pages/2530933/Historical+Conversation+Summary)| Summarises all conversations over a period of time regardless of the channel type and the queue  
[IVR Detail Report](/wiki/spaces/SBT/pages/80150550/IVR+Detail+Report)| Detail IVR journey of the customer for each call  
[IVR Summary Report](/wiki/spaces/SBT/pages/80183299/IVR+Summary+Report)| Summarizes the journey of IVR activities per day   
[Multichannel Session Detail](/wiki/spaces/SBT/pages/436994049/Multichannel+Session+Detail)| Provides the details of the Multiple channel sessions in a conversation.  
[Outbound Summary Report](/wiki/spaces/SBT/pages/1281261572/Outbound+Summary+Report)| Provides a summary of outbound conversations.  
[Queue Flushed Conversation Count](/wiki/spaces/SBT/pages/2532043/Queue+Flushed+Conversation+Count)| Displays the count of conversations closed forcefully in each queue by the administrator or supervisor  
[Queue Stats Today](/wiki/spaces/SBT/pages/2527826/Queue+Stats+Today)| Provides statistics of a queue for the current day since midnight  
[Queue-wise Stats Summary](/wiki/spaces/SBT/pages/2527840/Queue-wise+Stats+Summary)| Provides the count of requests received per queue, such as the number of chats or calls in case of voice offered, DONE, cancelled, transferred, etc., to view and analyze the performance of queues.   
[Repeated Caller Report](/wiki/spaces/SBT/pages/755761153/Repeated+Caller+Report)| This report shows customers who have made multiple calls/chats within a specified timeframe.  
[Skills Assessment](/wiki/spaces/SBT/pages/1015971843/Skills+Assessment)| Skills Assessment report displays agent or team performance based on evaluation form scores. Supports graphical and tabular views, with filters for date, teams, agents, and questionnaires (Evaluation Form). When multiple agents are selected, the report shows average scores per form.   
[Team Comparison](/wiki/spaces/SBT/pages/1015546076/Team+Comparison)| The Team Comparison Report provides a visual and tabular comparison of team-level evaluation scores over a selected time range. It supports filters by team, evaluation form (questionnaire), section (question group), and individual questions, allowing managers to analyze performance trends across multiple teams. The report displays data across different time scales (daily, weekly, monthly, yearly).  
[Transferred Tasks per Queue](/wiki/spaces/SBT/pages/2532035/Transferred+Tasks+per+Queue)| Shows the count of all tasks transferred out from a specific queue in the form of bar chart.  
[WebRTC Detail Report](/wiki/spaces/SBT/pages/1064763393/WebRTC+Detail+Report)| Shows the details of webrtc link.  
[WebRTC Summary Report](/wiki/spaces/SBT/pages/1064763418/WebRTC+Summary+Report)| Shows the summary of the webrtc generated links.  
[Wrap-up Summary](/wiki/spaces/SBT/pages/2532039/Wrap-up+Summary)| Provides the count of conversations along with associated wrap-up category and reason
