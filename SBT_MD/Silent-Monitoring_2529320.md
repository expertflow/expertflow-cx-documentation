# CX Knowledgebase : Silent Monitoring

Enables a supervisor to monitor an ongoing conversation silently between the agent and the customer.

To enable Silent Monitoring, 

  * Supervisor has to ensure to be assigned to a team within the Keycloak, with the supervisor’s name included in group attributes.




From the Ongoing Conversation Detail Dashboard, the supervisor can silently monitor a conversation but can not intervene in the conversation by sending a direct message or call to the customer.

## To Silently Monitor

Navigate to the _Ongoing Conversations Detail_ dashboard.

![navigate to ongoing dashboard.png](attachments/2529320/457932820.png?width=401)

The supervisors can see the active session for each conversation.

![active conversations-1.png](attachments/2529320/457736253.png?width=1095)

To silently monitor, click the ![image-20240819-080040.png](attachments/2529320/458162198.png) button

  * The supervisor can now join the conversation as a Silent Monitor.

  * And can monitor agent interactions during the conversation.


![bargein.png](attachments/2529320/1335033960.png?width=896)

  
In the case of chat, active conversations are listed on the left-hand side of the _Conversation View_. 

Supervisors can also see the monitored conversations with an eye icon![](attachments/2529320/2570726.png?width=30) to differentiate it from normal conversations.

In the _Ongoing Conversations Detail_ dashboards, the status of monitored conversations is shown on the left side of that particular conversation 

![ongoing conv ddb-1.png](attachments/2529320/458326050.png?width=1095)

While monitoring the conversation, supervisors can:

  * Exchange the whisper message with the agent using the Whisper**** tab to assist him without letting the customer know about it. To learn more, see [Send a Whisper Message](Send-a-Whisper-Message_143458310.html)

  * In case of chat, jump into conversations if required by clicking on the Barge-in button at any time. 

  * Leave the chat.




While silently monitoring the conversation, supervisors can not:

  * Directly send a message to the customer.

  * Transfer the conversation.

  * Have a conferenced conversation.




### Note:

  * When _Primary_ _Agent_ leaves the conversation, silent monitor participant automatically leaves the conversation.




### Limitations

  * There can be only one _Silent Monitor_ Supervisor at any given time.

  * If a _Silent Monitor_ is already in progress on chat for a conversation, and the CX Voice session gets active afterward, the _Silent Monitoring_ will only be limited to chat.

  * If any changes are done with roles on KeyCloak, the Supervisor/Agent needs to re-login for the changes to be reflected.

  * The **Whisper** option is only available for chat.

  * Silent Monitoring does not work for features **Outbound** ,**Direct Named Agent Transfer** ,**Consult Transfer** due to limitations, preventing further monitoring of the interaction.

  * If Agent1 places a Named Agent Consult request and Agent2 accepts, the "**Ongoing Conversations Detail** " dashboard does not display A2's name for the supervisor.

  * When a customer or agent ends a call while a supervisor is initiating silent monitoring, the call remains visible on the CTI toolbar even though it has ended. When the supervisor presses the "End" button on the CTI toolbar to clear the call, an error message "_invalid action releaseCall_ " is displayed, preventing the call from being properly removed from the interface.



