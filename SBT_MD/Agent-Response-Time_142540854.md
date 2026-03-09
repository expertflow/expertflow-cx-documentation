# CX Knowledgebase : Agent Response Time

Indicates the time limit in seconds that the agent must respond to a customer’s message received in a certain Queue or List.

As a new customer message is received on the conversation, the agent response time timer starts. Agents will see a countdown timer on top of the Message Composer, with changing colors, based on the time left to respond to the message. Agents can see the timer running on top of the Message Composer as shown in the screenshot below.

![Screenshot 2024-03-07 134652.png](attachments/142540854/151355739.png?width=878)

The timer stops as soon as a reply from the agent is sent to the customer.

When a conversation is on hold, the timer is stopped and reset when the conversation is resumed. 

For push-based conversations, this timer is set on a per-queue basis in the Unified Admin. For the pull-based conversations, this setting is defined on the List level.

The Agent Response Time runs on the conversation level, instead of the agent level, i.e., one time per conversation rather than a time per agent. This means that if a conversation carries several agents and if any one of the primary agents respond to the customer within time, this timer will be reset. On the other hand, if the timer expires for a conversation having multiple agents, all agents in the conversation will be removed and the conversation will be rerouted to the other available agents.

agent response time is disabled for voice channels.

The timer only starts when there is no active voice channel session of the customer in the conversation. 

## How to Setup Agent Response Time

  1. On the List or Queue configuration, specify Agent Response Time****

     1. A new field (Agent Response Time) has been added for queue and list configurations.

     2. To use agent response time, this field must have a non-null value for the duration.


![](attachments/142540854/151781592.png?width=878)

  2. **Thresholds:**




There can also be multiple threshold levels for that time, and for each threshold, the system will emit an action.

Threshold levels (can be defined on Controller) - a maximum of three levels from 0 - 100%. For example, 

  * Level 1: 0%

  * Level 2: 50%

  * Level 2: 75%

  * Level 3: 100%




The 1st and last levels are already configured by default. 1st level has an action START_TIMER that will initially start the timer, and the last level has the action, REMOVE_ALL_AGENTS that will remove all the agents within the conversation.

Other than 1st level, all the levels are customized and can be configured. 

**Configure** **Thresholds:**

  1. The last level REMOVE_ALL_AGENTS is configured on the controller bot, which is invoked when the timer reaches 100%. This action can be configured in the bot training.

  2. To configure threshold values, below POST API on Conversation-Monitor is exposed.



[code] 
     POST    {root-url}/conversation-monitor/agent-sla-thresholds
[/code]

  * This takes a list of agent response time Thresholds.




![image-20250529-112830.png](attachments/142540854/1112867142.png?width=878)

  3. To use the API, you can refer to [this](https://api.expertflow.com/#a846bc2f-6bf1-41d6-85e4-0fe27389c20b) documented endpoint.

  4. Please **NOTE** that at the moment the system is configured for the following actions:

     1. **CHANGE_COLOR** : This changes the color of the timer clock being displayed on the agent UI to Yellow (#ffaa00).


![Screenshot from 2025-05-29 16-13-31.png](attachments/142540854/1113030723.png?width=878)

b**.CHANGE_COLOR_TO_RED** : This changes the color of the timer clock being displayed on the agent UI to Red (#be0000).

![Screenshot from 2025-05-29 16-17-12.png](attachments/142540854/1112965195.png?width=878)

c. **SHOW_POPUP** : This shows a pop-up to the agent whether he/she wants to remain in the conversation. If agent selects to remain in the conversation, then the timer value will get reset. Otherwise, the agent will be unsubscribed from the conversation.

![Screenshot from 2025-05-29 16-17-20.png](attachments/142540854/1112736043.png?width=878)

**View Thresholds:**

You can also view the configured agent response time thresholds, for this another [API](https://api.expertflow.com/#06289064-bcf8-4ad6-8fb5-bfa54ab73f3d) is exposed on Conversation-Monitor

  1. 
[code]GET    {root-url}/conversation-monitor/agent-sla-thresholds
[/code]


![Get-Sla-Thresholds.png](attachments/142540854/725549138.png?width=878)

  
**Delete Thresholds:**

To delete existing thresholds in the system, call the same create thresholds API with an empty list object as the body just like below:
[code] 
    Endpoint: POST {root-url}/conversation-monitor/agent-sla-thresholds
    
    Body:
    [
    ]
[/code]

In case no thresholds are defined in the system, the agent response time will run for the complete duration specified on the queue/list without any intermediate action
