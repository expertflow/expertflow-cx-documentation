# CX Knowledgebase : Realtime Reports and Dashboards

The dashboards embedded in Agent Desk are the real-time dashboards for supervisors and agents to view the summary statistics of the contact center including queues, agent states, and the real-time conversations that are ongoing with agents and the bots.

Supervisors can monitor team-wise conversations. 

  * A supervisor must have at least one team, for instance, Team Alpha

  * A supervisor must have **at least one** agent within her team. For instance, Agent-1 is a member of Team Alpha, which is supervised by Supervisor John.

  * Next, access the unified admin platform and assign agent attributes to Agent-1. This will establish a connection between Agent-1 and any available queue.

  * Then, log in as Agent-1 in the Agent Desk **at least once**. This will ensure that all the changes made to Agent-1 take effect.

  * Now, the supervisor can log in as Supervisor John and observe that the Team Alpha & the queue(s) associated with Team Alpha are visible on the dashboard|. This allows the supervisor to view the corresponding data.

  * Adding or removing agents from a team in Keycloak will take effect upon the agent's next login, not in real-time on dashboards.

  * If a supervisor is also an agent, he’ll only be able to view and see the teams in the dashboard that he supervises and not the team in which he is added as an agent.




There are two types of dashboards currently available:

  * Summary Dashboards - built within Grafana to display summarized stats of queues, agents, active conversations and MRDs

  * Detail Dashboards - built within Agent Desk for details about active/queued conversations, agent activities




Let's walk through the following to know more details.

## Summary Dashboard

After logging in, the dashboard is the first screen a user will see. 

This dashboard shows the summary statistics of all conversations being queued, active with agents/bots and the overall agent states. 

If you are a supervisor, you will first select the team that you want to monitor, out of all the teams that are assigned to you as a supervisor. After selection of a team, the next step is to select a queue from the Queeus dropdown. This dropdown shows the list of all queues that are associated with a team. Once selected, the user can select multiple or single queue(s) to monitor the queue(s) statistics that are part of the selected team.

If you are an agent, you will only see the **Queues** dropdown and an available list of queues that you are a part of.

To see the conversations on the dashboard, use the following filters in the sequence:

  * _Bot Name_ \- Choose the name of the bot from the dropdown to see the conversations that are currently going on between the customer and the bot 

  * _Team Name_ \- Choose one team from the dropdown to see the associated queues. The selection here directly affects the queues list being populated in the **Queues** dropdown so that only the queues that are linked to a team are populated in the dropdown. 

  *  _Queue Name_ \- Based on the Team's selection, the Queues dropdown populates the queue(s) associated with the specified Team. Once the queue(s) is selected, the Conversational statistical data on the dashboard is filtered based on the selected queue(s). 

  *  _MRD Name_ \- Based on the Team's selection, choose one MRD to see the current MRD states of those agents that are part of a team. 




Each box on the Summary Dashboard is named as a _Panel_.

The dashboard contains three rows where related data is grouped under each row.

Those three rows are:

  * Queue Stats

  * Agent States

  * Bot Stats 




  * Any changes made to an agents attributes / to;Adding or removing agent attributes that affect queue associations will take effect upon the agent's next login, not in real-time on dashboards.




See the following sections to learn more about the panels grouped under each row. 

### Queue Stats 

On the Queues Stats panel, you can see the following information by selecting one or multiple queues from the Queues checkbox.

![supervisor_dashboard.png](attachments/2529305/1035731024.png?width=1794)

**Panel**| **Description**  
---|---  
**Service Level%**|  Shows the Service Level % of the queue(s) based on the Queues filter given on top of the dashboard. This data is retrieved from the historical database which is why, it gets updated after the historical reporting interval. The reporting interval is configurable. By default, it is set to 5 minutes. This is calculated based on the Service Level Type set in the queue definition by the administrator. See [Reporting Database Schema -> Key Reporting Concepts](Reporting-Database-Schema_2526317.html) to learn more about this parameter.  
  
#### **Active with Agents**

  
|  Shows a number of active conversations that are currently active with agents. This data is currently filtered based on the queue(s) that is selected from the queue filter on top of the dashboard, showing the conversations of the queue(s) that are currently active with agents.  
**Average Wait Time**|  This is the average time duration until the request remains in the queue. An average waiting time is calculated by summing all the waiting times and dividing them by the total number of all chats. If for the case when multiple queues are selected, the average wait time will be averaged based on the number of selected queues. This is shown in HH:MM: SS format.  
**Average Handle Time**|  This determines the average handle time of all closed tasks, regardless of any disposition. This duration is calculated as: task_end_time - task_answered_timeIn case a conversation is joined and handled by multiple agents, the conversation's total handled duration is the sum of the handled durations of all agent tasks (created for each agent who joined the conversation).The **average handled duration** is calculated as:`Total Handled Duration/ `Total Handled TasksIf for the case multiple queues are selected, the AHT will be calculated based on the average of the number of the selected queues.Format: hours minutes seconds (00:00:00)   
  
### Queue Summary Statistics

This panel lists all queues in a tabular representation with summary statistics of each queue including the total queues, and the oldest in the queue. With a queue filter dropdown, select a queue name from the list to filter out the data. You can select one or multiple desired queues to be shown under this panel.

![Queue Summary Stats.png](attachments/2529305/218333190.png?width=1800)

You can also apply sorting on the queue name to render the queue list in alphabetical order. 

**Queue Name**|  This shows the name of the queue. Lists down all precision queues created in the system whether or not it has some conversations in the queue.  
---|---  
**MRD Name**|  The name of the MRD that is associated with each queue by the administrator.  
**Total Queued**|  This is the total number of conversations that are currently queued to this queue  
**Oldest in Queue**|  This is the time duration of about how long a conversation stayed in a queue. This time is shown in 00:00:00 format. This is calculated out of all conversations that are currently in the queue, which is the longest waiting conversation. It stays in 00:00:00 if there's no conversation currently in the queue.   
**Not Ready**|  This is the count of agents who are currently in the **Not Ready** state on this queue. This is determined by the number of agents who are currently **Not Ready** on the MRD associated with this queue.  
**Ready**|  This is the count of agents who are currently in the **Ready** state on this queue. This is determined by the number of agents who are currently **Ready** on the MRD associated with this queue.  
**Active**|  This is the count of agents who are currently in **Active** state on this queue. This is determined by the number of agents who are currently **Active** on the MRD associated with this queue.  
**Pending Not Ready**|  This is the count of agents who are currently in the **Pending Not Ready** state on this queue. This is determined by the number of agents who are currently **Pending Not Ready** on the MRD associated with this queue.  
**Busy**|  This is the count of agents who are currently in a **Busy** state on this queue. This is determined by the number of agents who are currently **Busy** on the MRD associated with this queue.  
  
Service level, Average Wait Time, and Average Handle Time data are based on historical data and therefore, are updated only in the historical reporting interval (aka ETL job interval). The default interval is set to 5 minutes, however, this setting is configurable and can be changed as required by the business.

### Agent States

This panel shows a pie chart where each slice of the pie shows the count of agents in each MRD state. This data is filtered using the MRDs filter dropdown on top of the dashboard.

![agent stats.png](attachments/2529305/217546863.png?width=611)

### Bot Stats

This panel shows a number of active conversations that are currently active with the bot. This data is filtered using the Bots filter dropdown on top of the dashboard. 

![active with bots.png](attachments/2529305/217677938.png?width=640)

  * Currently, the software only supports having one bot. When multiple bots support will be added in the future, this filter can be used to filter conversations active with a specified bot.

  * A conversation is considered to be active with the bot unless some agent joins it.




#### Agent Desk Theme Synchronization with Summary Dashboard

  * When a user modifies the theme within any screen of the Agent Desk, the Summary Dashboard will automatically reflect the same theme upon being opened.

  * If a user modifies the Agent Desk theme while on the Summary Dashboard screen, the dashboard will automatically reload to display the updated theme.

  * If a user logs out of the Agent Desk while using the dark theme setting, the dark theme will be applied to both the Summary Dashboard and the Agent Desk upon subsequent logins.




## Detailed Dashboards

The following are the dashboards where conversation details are listed. Each dashboard is refreshed in 10 seconds. The application offers the following three types of detailed views:

### Queued Conversations Detail

This dashboard lists all conversations that are currently enqueued to a queue. 

To see the desired conversation on this dashboard, use the following filters in the given sequence:

  * **Team** \- Choose one team from the dropdown to see the relevant queues in the Queues dropdown. In case if you are an agent , you will only be able to see the name of the team that you are a part of.

  * **Queue**(s) - Based on the Team's selection, the Queues dropdown populates the queue(s) that are associated with the specified Team. Once the queue is selected, the data on the dashboard is filtered based on the selected queue. The dashboard will display data from all queues by default when a supervisor selects any team from the teams dropdown.




The following details of a conversation are available on the dashboard:

**Field**| **Description**  
---|---  
**Customer**|  Name (if identified), along with the customer channel identifier and a channel type icon to identify from which channel the customer initiated the conversation.  
**Waiting Since**|  This is the time since this conversation is enqueued. This time is shown in terms of minutes, such as <x> minutes ago.  
**Queue Name**|  The name of the queue where the conversation is enqueued  
  
You can change the queue from the Queues filter drop-down to see enqueued conversations on the specified queue.

![](attachments/2529305/2570697.png?width=1241)

  * The filter of all queues shows **all queues** that are part of the specified team. 

  * Agents do not have access to this dashboard.

  * Adding or removing agent attributes that affect queue associations will take effect upon the agent's next login, and not in real-time on dashboards.




### Ongoing Conversations Detail

This dashboard lists all conversations that are currently active with agents, supervisors, or bots, with the details such as on which queue they were landed, name and channel identifier of the customer, and the time since they are active.

To see the desired conversations on this dashboard, use the following filters in the given sequence:

  * **Answered by Agents or Bots** \- To see active conversations with bots, switch the value in the first tab of the top row, and set the filter to **Answered by Bots.** By default, it is set to **Answered by Agents** which shows the active conversations that are currently active with agents/supervisors. 

  * **Team** \- Choose one team from the drop down to see the relevant queues in the Queues drop down. This allows a user to view active conversations in a queue.

  * **Queue(s)** \- Based on the Team's selection, the Queues drop down populates the queue(s) that are associated with the specified Team. Once the queue is selected, the data on the dashboard is filtered based on the selected queue. Select one or multiple queues to see the results.




The following details of a conversation are available on this dashboard:

**Field**| **Description**  
---|---  
**Direction**|  This shows the direction of the conversation, i.e. if it is Inbound or Outbound.  
**Channel**|  This is the channel through which the customer has initiated the conversation. For instance, WhatsApp, Facebook, Webchat.  
**Customer**|  Name (if identified) along with the channel identity (for instance, WhatsApp number, Facebook name, Email)  
**Active Since**|  This is the time since this conversation became active. This time is shown in terms of minutes, such as <x> minutes ago.  
**Agent**|  This shows the Agent's name along with the user name who handled the conversation.  
**Queue Name**|  The name of the queue on which the conversation is enqueued  
  
![ongoing-onhold status-1.png](attachments/2529305/469958661.png?width=1800)

As a primary supervisor, their default view include all agents within their team. 

As a secondary supervisor, their default view will include only the agents assigned to them within the team. Additionally, both (primary and secondary supervisor) have access to a filter enabling them to view agents managed by other secondary supervisors. This filter will dynamically load agents based on the selected secondary supervisor. Additionally, there will be an option labeled "All agents," enabling them to view details of all agents within the team.

  * When a team and a specific supervisor are selected, only chats that are active with agents assigned to that supervisor will be displayed.

  * When a team and the "all supervisors" option are selected, all chats that are active with agents and supervisors for that team will be shown.

  * If the supervisor selects **all supervisors** from the filter, conversations related to "agents + secondary supervisor + primary supervisor" will be listed on the dashboard. A supervisor can now also see their own ongoing conversations in the dashboard. 




For conversations that are put on hold, a user can also see them with an _on-hold_ status on the **Ongoing Conversations Detail** dashboard.

  * A conversation might appear on **Ongoing Conversations Detail → Answered by Bots** and **Queued Conversations Detail** at the same time. This is when it is still with the bot and not yet routed to an available agent from the queue. However, as soon as it is routed to an agent, it disappears from the Queued Conversations Detail dashboard.

  * In case of an active conversation with any agent of the queue who is not part of the supervisor's team, the conversation will not be visible to the supervisor on the dashboard. It will only be seen by the person who is the supervisor of that agent.

  * A conversation with multiple agents from different queues will be shown as two rows on the **Ongoing Conversations Detail → Answered by Agents** dashboard. However, in case of an active conversation with multiple agents from the same queue, this is shown as one conversation on the dashboard.

  * If a conversation is blindly transferred to an agent (or directly transferred to a named agent), it will disappear from the **Ongoing Conversations Detail** dashboard.

  * When Agent1 places a consult request and Agent2 accepts, the "**Ongoing Conversations Detail** " dashboard does not display A2's name for the supervisor. It appears as though only one agent is in the conversation.

  * After a consult transfer is completed and Agent2 accepts the call.The conversation between A2 and the customer does not appear on the "**Ongoing Conversations Detail** " dashboard.

  * The Outbound conversation does not appear in the “**Ongoing Conversation Detail** ”.

  * Agents cannot access this dashboard.




Only inbound conversations are shown in the **Ongoing Conversations Detail** dashboard**.**

### Available Agents Detail

This dashboard displays a list of all team agents, including the number of active conversations with each agent and the current state of each agent in each MRD. While viewing the list of active agents with a count of active conversations, a supervisor can also change an agent's state based on the agent's current state. This allows supervisors to manage long-idle agents and maintains workflow efficiency.

The supervisor can only change the global state of the agent and not its MRD state.

To do so, supervisors click on the "Change State" dropdown against the desired agent whose state needs to be changed. 

The available changes for the agent's global states are:

  * From **Not Ready** to **Ready**

  * From any other state to **Log Out:** To see how to forcefully log out an agent, see [Force Logout Agent](Force-Logout-Agent_1181941884.html)


![not ready-active agents detail.png](attachments/2529305/273154080.png?width=846)

To see the desired conversations on this dashboard, use the following filters:

  * Search Agent - This filter allows the supervisor to search for a specific agent of her team.

  * Team - Choose one team from the drop-down to see the active agent's details and the current state of agents in each MRD.




The following details are available on the dashboard. 

**Field**| **Description**  
---|---  
**Agent (s)**|  shows the name of an agent along with the current state Ready, Not Ready   
**Active Conversation**|  shows the number of active conversations going on with the agent for the selected queue.  
**MRD State**|  displays the current state of the agent in a particular MRDColored circles on the upper right corner of the dashboard represent the MRD state.For more details of MRD State Transitions, see [**< Agent State -> Change MRD States**](Agent-States_2531294.html)  
  
Agents can also access this dashboard. When logged in as an agent, they can view their team’s states only.

As a primary supervisor, their default view includes all agents within their team. 

As a secondary supervisor, their default view will include only the agents assigned to them within the team. Additionally, both (primary and secondary supervisor) have access to a filter enabling them to view agents managed by other secondary supervisors. This filter will dynamically load agents based on the selected secondary supervisor. Additionally, there will be an option labeled "All agents," enabling them to view details of all agents within the team.

  * When a team and a specific supervisor are selected, only agents assigned to that supervisor will be displayed.

  * When a team and the "all supervisors" option are selected, all agents and supervisors for that team will be shown.




### Limitations

  * Adding or removing agents from a team in Keycloak will take effect upon the agent's next login, not in real-time on dashboards. 

  * Currently, there is no visibility of the agent’s MRD state when it is in the _Reserved_ state. As a result, the **Logout** option will still appear even when an agent is _Reserved_ for a task. This limitation will be resolved once the _Reserved_ state for MRD is introduced in the system.




### Saving Dashboard Filters

Change the filter in any of the dashboards in Agent Desk applies to all dashboards.

While viewing the dashboards, the filters saved on one dashboard are automatically saved and remain valid for the other detailed dashboards as well.   
For instance, if you select Team A, and Queue B on the “Queued Conversations” dashboard to view the queued conversations in Queue B, the filter will be saved and applied on the other dashboards as well. If you then navigate to the “Ongoing Conversations” dashboard, or “Active Agents Detail” dashboard, the data in the dashboards are filtered based on the filter saved on the “Queued Conversations” dashboard.

Moreover, if a filter is changed on any dashboard, the changes will be saved and applied to all the dashboards.

For Summary Dashboards, the filters saved on one Agent Desk dashboard are also applicable on the Summary Dashboard as well.

  * The saved filters (Teams, Queues) will be stored under the browser cache.

  * If "All Teams" is selected in the "Active Agents Detail" dashboard, this filter won't be saved and won’t be applied to the rest of the dashboards.

  * However, if the Teams filter is changed later in another dashboard, the same filter will also apply to the "Active Agents Detail" dashboard. From the saved filters, only the filter that applies to a dashboard is applied to the dashboard.

  * If dashboards or saved filters get stuck after repeated refreshes, waiting for a few seconds and then refreshing again will resolve the issue.



