# CX Knowledgebase : Consult, Transfer and Conference

Allows CX agents to consult, transfer an active conversation, or add agents to the conference, and send Whisper Message.

## Consult on a Conversation

Agents can consult another agent on an ongoing conversation to assist them in answering the customer's query in a better way. A consult can be initiated for a conversation in the following ways:

  * Queue Consult

  * Agent Consult 

  * Consult on External Numbers




### Queue Consult

Agents can initiate a consult request in an active conversation on any queue. The system looks for a suitable agent to join the conversation to assist the primary agent.

#### To Consult on the Queue

![](images/icons/grey_arrow_down.png)Follow these steps to consult

  1. Click ![](attachments/2528529/2568799.png?height=35)the button on the control toolbar. The agent will see a dropdown containing the list of all the queues linked to _CX Voice_ or _CHAT_ _MRD_ with the following information:

     1. Queue Name (department name or any queue name)

     2. Number of agents available (ready + active) in the queue. This helps the agent decide whether the consult request should be started on the selected queue or not (based on the available agents count). 

![queue consult-20250108-133001-20250124-072925.png](attachments/2528529/830734475.png?width=342)

  2. Choose a queue from the list and click the **Consult** option ![Capture2.PNG](attachments/2528529/438599774.png) .

  3. A queue consult request can be placed even if no active agent is available on the queue. 

     1. At this stage, the request is placed in the queue. If an agent becomes available, the request is routed to that available agent.

     2. If no agent becomes available, the request is removed from the queue after the TTL(time to live) timer expires, The primary agent gets a notification ‘ _**No Agent Available’**_ in the interaction history. 

     3. If the agent initiates another request and a request is already in process, the user will be notified with an error from the system.

![](attachments/2528529/438599742.png?width=371)
  4. Upon successful request, the **Queue Consult** dialog box appears (for Chat only). The agent can optionally type a message for the receiving/secondary agent who is going to join the conversation. Click the **Consult** **Request** button to initiate the request.

![image-20240731-071522.png](attachments/2528529/438599748.png?width=368)

  5. The agent will see a notification indicating that a "_Queue Consult Request_ has been _placed_ " in the interaction history.

  6. The request will be parked on priority. The system will look for an available agent from the queue to route the request to an agent.

  7. If the other agent does not accept the request, the system keeps on looking for another agent for some time.

  8. If no agent is found, 

     1. The request is timed out.

     2. The agent will see a notification, "_No Agent Available_ ".




Writing a note while initiating a consult request is an optional thing for agents to describe something about the conversation to the consulted agent.

In case, an agent receives a consult request from another agent, 

  1. A consult request notification will be received with the following information:

     1. Channel icon via which the request is placed (WhatsApp, Web, Facebook, etc.) 

     2. A button to **Accept** the request. 

     3. Name of the Agent in case of a _Chat_ session **OR** the agent extension in case of a _Voice_ session.

     4. The optional notes are entered by the agent while the consult request is ringing on the request agent (Only available for Chat).

![image-20240731-071942.png](attachments/2528529/438599754.png?width=395)

  2. Click the **Accept** button to accept the request.

  3. The primary agent will also be notified that another agent has joined the conversation as an _Assistant_.




![1-Qconsult.gif](attachments/2528529/826802278.gif?width=855)

### Agent Consult

Agents can consult directly with another agent via using contacts tab directly or go to queues tab locate specific queue and expand dropdown find specific agent.

![](images/icons/grey_arrow_down.png)Follow these steps to transfer via named agent

  1. Click the _Agent Assistance_ button ![](attachments/2528529/2568799.png?height=35) on the control toolbar. The agent will see a dropdown containing the list of all the queues linked to _CX Voice_ or _CHAT_ _MRD_ with the following information:

     1. Queue Name (department name or any queue name)

     2. Number of agents available (ready + active) in the queue. This helps the agent decide whether the consult request should be started on the selected queue or not (based on the available agents count). 

  2. Expand a queue to view the list of agents available on that particular queue.  


![agent Consult-20250108-134019-20250124-073029.png](attachments/2528529/830701693.png?width=342)

  3. Choose an agent from the list and click the **Consult** button ![Capture2.PNG](attachments/2528529/438599774.png), available upon hovering on the agent.

  4. The agent will see a notification indicating that "_Agent Consult Request_ has been _placed_ " in the interaction history.

  5. The consult request will be routed to the selected agent based on their availability.

  6. On a successful request, the requested agent will see an incoming request notification with the following information:

     1. Channel icon via which the request is placed (CX Voice).

     2. A button to **Accept** the request.

     3. Name of the customer, the name of the agent in case of a _Chat_ session **OR** the agent extension in case of a _Voice_ session.

     4. The optional notes are entered by the agent while the consult request is ringing on the requested agent (Only available for Chat).

  7. Click the **Accept** button to accept the consult request.




### Consult on an External Number

  * Agents can consult in an active conversation on any external number if they think that the third party can assist them in answering the customer's query. A consult can be initiated as follows:




![](images/icons/grey_arrow_down.png)Follow these steps to consult

  1. Click the agent assistance button ![image-20250221-103050.png](attachments/2528529/914325699.png) on the control toolbar. The agent will see a dropdown, where they can navigate to the dialpad.

![image-20250221-103210.png](attachments/2528529/914325706.png?width=332)

  2. Users can enter any number(between 2 to 18 digits) to enable the actions.

  3. Once the number has been entered, the user can click the consult button to place the request. 

![image-20250221-103517.png](attachments/2528529/914325712.png?width=326)
  4. Upon clicking the button, the request is forwarded to the dialed number, and a notification with the message "_Consult request placed successfully_ " is shown to the user.

![image-20250221-103843.png](attachments/2528529/914325718.png?width=334)



### Limitations

  * The optional note is only available for chat.

  * If a consult is already in progress on chat for a conversation, and the Voice session gets active afterward, the consult will only be limited to chat.

  * If any changes are done with permissions on Keycloak, the agent or anyone else in that role needs to re-login for the changes to be reflected.

  * When Agent A1 initiates a consult call on a queue, the full DN with ID is displayed. For Details see [CIM-15520](https://expertflow-docs.atlassian.net/browse/CIM-15520)

  * In a consulted conversation, consulted Agent is able to send message to customer when A1 is applying wrap up. For Details see [CIM-15671](https://expertflow-docs.atlassian.net/browse/CIM-15671)

  * Repeated consult requests at the same time are not supported by the system and the system displays a generic error message if the above scenario arises in case of chat. For Details see [CIM-15537](https://expertflow-docs.atlassian.net/browse/CIM-15537)

  * Error Message and Task Stuck When Voice Queue Consult Request Fails on Agent A2. For Details see [CIM-15228](https://expertflow-docs.atlassian.net/browse/CIM-15228)

  * When a consult call is initiated and an agent is reserved, if the customer leaves immediately after the request is placed, agents receive error messages on their interface, and their MRDs are set to "Not Ready". For Details see [CIM-15949](https://expertflow-docs.atlassian.net/browse/CIM-15949)

  * No external leg data is stored in CX.

  * A2 is unable to close the conversation view when A1 dials A2's extension in the **External Number Dial-pad** and initiates a consult. For Details see [CCC-1634](https://expertflow-docs.atlassian.net/browse/CCC-1634)

  * A2 is unable to close the conversation view when A1 dials the **Queue DN** in the **External Number Dial-pad** and initiates a consult. For Details see [CCC-1633](https://expertflow-docs.atlassian.net/browse/CCC-1633)




## To Consult Transfer a Conversation

Agents can transfer an ongoing conversation to the consulted agent to help them assist the customer's query. 

Agents can initiate a consult transfer request in the following ways based on the active channels.

#### Consult Transfer For Chat

![](images/icons/grey_arrow_down.png)Follow these steps to consult transfer

  1. Click the participants list button ![image-20240731-080347.png](attachments/2528529/439189526.png), on the toolbar in the active conversation view.

  2. The agent will see a dropdown containing the participant's list in the ongoing conversation.

![image-20240731-080540.png](attachments/2528529/439189533.png?width=168)
  3. Check for the participant with the _ASSISTANT_ role, and click the _**Transfer**_ button to initiate the transfer request to the consulted agent. 

![image-20240731-080705.png](attachments/2528529/439189539.png?width=246)

  4. A notification message with the text "_Consult transfer request_ has been _placed_ " is added in the interaction history.

  5. On a successful transfer,

     1. The Primary agent is unsubscribed from the conversation and a notification of the _‘agent left’_ appears in the interaction history.

     2. The _ASSISTANT_ agent now becomes the _PRIMARY_ agent,__ and can directly interact with the customer.

     3. The customer also sees the notification that the other agent has joined (in case of _Web_).




#### Consult Transfer For CX Voice

![](images/icons/grey_arrow_down.png)Follow these steps to consult transfer

In case of an active consult call, the _PRIMARY_ agent can view the consult transfer option on the CTI toolbar  


![2024-11-19_18-48-53-20241119-135042.png](attachments/2528529/692551681.png?width=555)

  1. Click the consult transfer button ![image-20240731-083404.png](attachments/2528529/439189557.png) , to initiate a transfer request.

  2. Upon a successful request, 

     1. A notification message "_Consult transfer request_ has been _placed_ " appears in the interaction history.

     2. The Primary agent is now unsubscribed from the conversation and the ‘agent left’ notification appears in the interaction history.

     3. The _ASSISTANT_ agent has now become the _PRIMARY_ agent,__ and can directly interact with the customer.




#### Consult Transfer on an External Number 

  * Agents can initiate the consult transfer request to the consulted external number as follows:




![](images/icons/grey_arrow_down.png)Follow these steps to consult transfer

  1. Once the consult call is active, the users can click the consult transfer button ![image-20250221-104832.png](attachments/2528529/914325724.png) on the Call Control bar to transfer the call to the consulted external numbers.

![2024-11-19_18-48-53-20241119-135042.png](attachments/2528529/692551681.png?width=555)
  2. Once the button is clicked, the transfer request will be forwarded to the consulted external number. 

     1. Once the request is placed, a notification with the message "_Transfer request placed successfully_ " will be shown to the user.

![image-20250221-105536.png](attachments/2528529/914325744.png?width=414)
     2. The agent will unsubscribe from the conversation in CX.




### Disclaimer

  * Consult Transfer for a voice session should only be done if the consulted agent is also part of the voice call/session.

  * The primary agent can only initiate the transfer request.

  * Internal numbers/DNs are not supported and are not recommended to be dialed.




### Limitations

  * No external leg data is stored in CX.

  * After Agent1 transfers a call to Agent2 following a supervisor barge-in, the call control interface is removed, but the conversation view remains open. The call continues in the background, and the conversation view does not close automatically when the customer ends the call. Manual intervention, such as a refresh by the supervisor or customer, is required to end the call session. For details see [CCC-1724](https://expertflow-docs.atlassian.net/browse/CCC-1724)




## To Consult Conference a Conversation

This allows agents to add the consulted agent to a conference with the customer in an ongoing conversation to collaborate and assist the customer together. When another agent is added to the conversation, it becomes a conferenced conversation. The newly added agent in the conference has the same level of rights and permissions as the first primary agent in the conversation. This also implies that if the first agent leaves the conversation, the conference will continue with the agents in the conversation.

Agents can initiate a consult conference request in the following ways based on the active channels.

#### Consult Conference For Chat

![](images/icons/grey_arrow_down.png)Follow these steps to consult conference

  1. Click the participants list button ![image-20240731-080347.png](attachments/2528529/439189526.png), to view the participant's list in the ongoing conversation.

  2. Check for the participant with the _ASSISTANT_ role, and click the _**Conference**_ button to initiate the conference request to the consulted agent. 

![image-20241119-134414.png](attachments/2528529/692027393.png?width=275)

  3. A notification message with the text "_Consult Conference request_ has been _placed_ " is added in the interaction history.

  4. On a successful request,

     1. The _ASSISTANT_ agent becomes the _PRIMARY_ agent,__ who can directly interact with the customer.

     2. The customer also sees the notification that the other agent has joined (in the case of _Web_).




#### Consult Conference For CX Voice

![](images/icons/grey_arrow_down.png)Follow these steps to consult conference

In case of an active consult call, the _PRIMARY_ agent can view the consult transfer option on the CTI toolbar  


![2024-11-19_18-48-53-20241119-134943.png](attachments/2528529/692322306.png?width=555)

  1. Click the consult conference button ![image-20241119-135153.png](attachments/2528529/692387842.png) , to initiate a conference request.

  2. Upon a successful request, 

     1. A notification message "_Consult Conference request_ has been _placed_ " appears in the interaction history.

     2. The _ASSISTANT_ agent is now unsubscribed from the conversation and the ‘agent left’ notification appears in the interaction history for the _PRIMARY_ agent.

     3. The _ASSISTANT_ agent now rejoins the conversation as the _PRIMARY_ agent,__ and can directly interact with the customer now.




#### Limitations

  * A maximum of only 4 participants can be part of a conference call simultaneously.




#### Consult Conference on External Numbers

Enables agents to initiate a consult conference call with external numbers during an ongoing CX Voice session. This allows agents to bring in external parties (such as mobile or PSTN contacts) into a live conference call with a customer.

![](images/icons/grey_arrow_down.png)Follow these steps to consult conference

  1. When the consult call is active, the users can click the consult conference button ![image-20250421-074627.png](attachments/2528529/1052311553.png) on the Call Control bar to add the consulted external number to the customer call.

![2024-11-19_18-48-53-20241119-134943.png](attachments/2528529/692322306.png?width=555)
  2. The system processes the conference request and incorporates the consulted external number into the ongoing call. 

  3. Once the request is successful, the consult leg will be dropped, and the external numbers will be added to the customer call. Now, the call will be converted to a conference call, enabling direct communication with the customer.

![image-20250421-074518.png](attachments/2528529/1051951194.png?width=1137)



### Disclaimer

  * There should be a CX Voice session active in the conversation.

  * Internal numbers/DNs are not supported and are not recommended to be dialed.




### Limitations

  * No external leg data is stored in CX.




## Transfer a Conversation

Agents can transfer an ongoing conversation to another agent if they think that the other agent will better answer the customer's query. A conversation can be transferred in the following ways:

  * Direct Queue Transfer

  * Direct Agent Transfer

  * Direct Transfer on External Numbers




### Direct Queue Transfer

Agents can transfer a conversation to a queue. The system looks for a suitable agent to join the conversation. 

#### To Transfer to the queue  


![](images/icons/grey_arrow_down.png)Follow these steps to transfer

  1. Click ![](attachments/2528529/2568799.png?height=35)the button on the control toolbar. The agent will see a dropdown containing the list of all queues with the following information:

     1. Queue Name (department name or any queue name)

     2. Number of agents available (ready + active) in the queue. This helps the agent to decide whether this conversation should be transferred to the selected queue or not (based on the available agents count).

  2. Choose a queue from the list and select the **Transfer** option.

  3. A queue transfer request can be placed even if no active agent is available on the queue. 

     1. Upon request, the request is placed in the queue. If an agent becomes available, the request is routed to that agent.

     2. If no agent becomes available, the request is removed from the queue after the TTL timer expires, _**No Agent Available**_ is published and a notification is shown in the interaction history. 

     3. If a user initiates another request and a request is already in process, the user will be notified with an error from the system.

  4. In the Message box in the **Transfer to Queue** dialog box, the agent can optionally type a message for the receiving agent. This message is then received by the other agent who is going to join the conversation. Click the **Transfer** button to transfer the conversation.

  5. The agent will see two notifications. One is a notification that "_Conversation is closed due to CHAT TRANSFERRED_ " and another toaster notification "_Transfer request placed successfully_ "

  6. The chat will be parked in the transferred queue on priority. The system will look for an available agent from the queue to route the conversation to an agent.

  7. The customer sees a notification, "_Your request is being transferred to <queue-name>, please wait!_", followed by another notification that, "_Agent1 has left_ ".

  8. If the other agent does not accept the request, the system keeps on looking for another agent for some time.

  9. If no agent is found, 

     1. The request is timed out.

     2. The customer will see a notification, "_No agents were available_ ".




Writing a note while transferring a request is an option thing for agents to describe something about the conversation to the transferee. 

In case, an agent receives a transferred request from another agent, 

  1. A transfer request notification will be received with the following information:

     1. Channel icon via which the request is placed (WhatsApp, Web, Facebook, etc.) 

     2. A button to **Accept** the request 

     3. Name of the customer if identified

     4. The optional notes are entered by the agent while transferring the conversation. (See point #3 above.)

  2. Click the **Accept** button to accept the conversation

  3. The customer will also be notified that 'You have joined the conversation'.




![queue transfer \(1\).gif](attachments/2528529/827588614.gif?width=855)

### Direct Agent Transfer

Agents can transfer directly with another agent via using contacts tab directly or go to queues tab locate specific queue and expand dropdown find specific agent

The conversation will be closed after the configured customer activity timer expires and the requested agent will remain reserved in case the transfer request fails on FS.

![](images/icons/grey_arrow_down.png)Follow these steps to transfer a conversation to an agent

  1. Click the _Agent Assistance_ button ![](attachments/2528529/2568799.png?height=35) on the control toolbar. The agent will see a dropdown containing the list of all the queues linked to CX Voice _MRD_ with the following information:

     1. Queue Name (department name or any queue name)

     2. Number of agents available (ready + active) in the queue. This helps the agent decide whether this conversation should be transferred to the selected queue or not (based on the available agents count).

  2. Expand a queue to view the list of agents available on that particular queue.  


![Screenshot \(75\)-20250108-170149-20250124-073306.png](attachments/2528529/830701699.png?width=341)

  3. Choose an agent from the list and select the **Transfer** button ![image-20240305-074151.png](attachments/2528529/147161135.png) , available upon hovering on the agent.

  4. The agent will see two notifications. One is a notification that _"Agent transfer request has been placed"_ and another toaster notification "_Transfer request placed successfully_ ".

  5. The conversation will be transferred to the selected agent based on his availability.

  6. On a successful transfer, the requested agent will see an incoming request notification with the following information:

     1. Channel icon via which the request is placed (CX Voice).

     2. A button to **Accept** the request.

     3. Name of the customer.

     4. Number of the customer.

  7. Click the **Accept** button to accept the conversation




### To Direct Transfer to an External Number

Users can directly transfer the call to external numbers

![](images/icons/grey_arrow_down.png)Follow these steps to transfer

  1. Click the agent assistance button ![image-20250221-103050.png](attachments/2528529/914325699.png) on the control toolbar. The agent will see a dropdown, where they can navigate to the dialpad.

![image-20250221-103210.png](attachments/2528529/914325706.png?width=332)

  2. Users can enter any number(between 2 to 18 digits) to enable the actions.

  3. Once the number has been entered, the user can click the transfer button to place the request. 

![image-20250221-103517.png](attachments/2528529/914325712.png?width=326)
  4. Once the button is clicked, the transfer request will be forwarded to the external number. 

     1. Once the request is placed, a notification with the message "_Transfer request placed successfully_ " will be shown to the user.

![image-20250221-105536.png](attachments/2528529/914325744.png?width=414)
     2. The agent will unsubscribe from the conversation in CX.




### Disclaimer

  * There should be a CX Voice session active in the conversation.

  * Internal numbers/DNs are not supported and are not recommended to be dialed.




### Limitations

  * No external leg data is stored in CX.

  * No error message is displayed when an agent clicks the **Transfer** button from the **External Number Dial-pad** while the gateway is down. For Details, see [CCC-1625](https://expertflow-docs.atlassian.net/browse/CCC-1625)

  * No error is displayed, and the customer drops when the agent dials an invalid external number and attempts to transfer the call. For Details see [CCC-1622](https://expertflow-docs.atlassian.net/browse/CCC-1622)




##   
Add Agents to Conference

This allows agents to add one or more agents to the conference with the customer. The recent implementation allows the customer to place a request on the queue even if there is no agent available on the queue.

When an agent is added to the conference, the conversation becomes a conferenced conversation. All newly added agents in the conference have the same level of rights and permissions as the first primary agent in the conversation. This also implies that if the first agent leaves the conversation, the conference will continue with the agents in the conversation. 

![](images/icons/grey_arrow_down.png)Follow the steps mention below

  1. Click ![](attachments/2528529/2568799.png?height=35)button on the control toolbar. A dropdown will appear with a list of all available queues with:

     1. Queue Name 

     2. Number of agents available (ready + active) in the queue

  2. Choose a queue name from the list and hit the **Queue Conference** button.

  3. A queue conference request can be placed even if no active agent is available on the queue. 

     1. Upon request, the request is placed in the queue. If an agent becomes available, the request is routed to that agent.

     2. If no agent becomes available, the request is removed from the queue after the TTL timer expires, _**No Agent Available**_ is published and a notification is shown in the interaction history. 

     3. If a user initiates another request and a request is already in process, the user will be notified with an error from the system

  4. A Message box will appear in the **Conference** dialog box.

  5. Type a message for the receiving agent. This is an optional message. This message is then received by the other agent who is going to join the conversation.

  6. Then, click the **Add to Conference** button to make it a Conference Conversation

  7. The system looks for an available agent to be added as a  _Primary Participant_ to the conversation The system will route the conversation to Agent2 

  8. The first agent can see a toaster notification that "_a conference request has been placed successfully."_

  9. You will see a notification in the Activity Timeline that the "Conference request has been successfully placed" and on the other hand

  10. An incoming conference request notification will be received to Agent2 (receiving agent) with the following information:

     1. **A special indication that this is a Conference Chat reques** t from Agent1

     2. **Name of the identified/linked customer** (if done by Agent)

     3. **Note entered by Agent1** (if available) before placing the Conference request 

     4. A button to **Accept** the request

  11. By clicking the Accept button, Agent2 joins the conversation as the  _Primary Participant_.

     1. Agent1 sees the notification that A2 has joined 

     2. The Customer sees the same notifications in the Conversation history on the Customer side

     3. Agent2 can send/receive **Whisper** messages with Agent1.

     4. Agent2 can also see all the message exchanges in the current conversation. 

     5. Agent2 will see the Customer Profile and all the Media Channels, Active Sessions of the customer (based on the permissions) along with the Conversation Data and the past conversation history 

     6. Agent2 can perform other operations based on the  _Primary Participant_ permissions.

  12. Agent 2 can leave the chat

  13.      1.         1. All other conversation participants will see a notification, "<agent-names> left the conversation"

  14. In case, Agent2 does not accept the request. 

     1.         1. The system keeps on looking for another available agent from the selected queue until it finds one

  15. No agents available

     1. The request will be canceled.

     2. Agent1 sees a notification in the Activity Timeline such as, "No agents were available to join the conference conversation"




![](attachments/2528529/2568879.gif?width=647)

  

