# CX Knowledgebase : CX-Voice Limitations

_**Disclaimer**_

  * The**** permissions for the microphone should be enabled for the Agent Desk in the browser _. For Details see_[ _CIM-26650_](https://expertflow-docs.atlassian.net/browse/CIM-26650)

  * Any **private browser window** is not supported, as the system is using the browser cache for state maintenance.

  * Failover cases are not supported for**Consult, Transfer,** and **Silent monitoring** features.




##   
Voice Limitations 

Following are the Voice Channel capabilities  
Expertflow CX offers the following voice and video interaction features. Using CX Voice, a business can:

**Description**| **Support**  
---|---  
Connect via WebRTC using a customer widget for audio and video calls.| ![\(error\)](images/icons/emoticons/error.png)  
  
The following are the limitations of the solution:

### Feature Related

| 

  * [Consult](Consult%2C-Transfer-and-Conference_2528529.html#Limitations)
  * [Consult Transfer](Consult%2C-Transfer-and-Conference_2528529.html#Limitations.1)
  * [Direct Agent Transfer](Consult%2C-Transfer-and-Conference_2528529.html#Direct-Agent-Transfer)
  * [Manual Outbound Call](Make-a-Manual-Outbound-Contact_2528797.html#Limitations)
  * [Silent Monitoring](Silent-Monitoring_2529320.html#Limitations)

  
---|---  
  
### **General Cases**

| 

  * The conversation gets stuck when Agent1 is on the call with a customer and another Agent joins with Agent1’s credentials while the call is active. For Details see [CCC-659](https://expertflow-docs.atlassian.net/browse/CCC-659)
  * Optional note in the notification & requesting agent info option is not available for CX-Voice as incoming request notification.
  * CX Rona is not yet integrated with the CX Voice (FreeSWITCH) solution. Leveraging the ringing timeout of the FreeSWITCH to provide the RONA feature for this channel. 
  * When a customer call is placed on hold and either the customer or agent ends the call during the hold time, an error message "incorrect object for call" is displayed on the Agent Desk and the agent's MRD status is set to "Not-Ready." For Details see [CIM-15531](https://expertflow-docs.atlassian.net/browse/CIM-15531)
  * When a customer disconnects the call immediately at certain second after the agent is reserved, the system throws an "`invalid action answerCall`" error, and the CX Voice MRD transitions to the "Not Ready" state. This issue disrupts the agent's availability for future calls. For Details see [CIM-15904](https://expertflow-docs.atlassian.net/browse/CIM-15904)
  * When a customer disconnects the voice call immediately after the agent accepts the conversation, the voice call ends, but the conversation remains open, causing the MRD to stay busy. This results in the agent having to manually close the conversation to free up the MRD as it remains in a busy state. For Details see [CIM-15881](https://expertflow-docs.atlassian.net/browse/CIM-15881)
  * Customers in Queue Not Routed to Available Agent Until CX-Voice MRD is Toggled On/Off if A1 ends call while it was ringing on Agent Desk. For Details see [CIM-25994](https://expertflow-docs.atlassian.net/browse/CIM-25994)
  * When an agent (A1) changes their MRD state to "Ready" while a customer ends the call or the agent refreshes their browser, an error message "Topic Closed Already" is displayed on the front end and in the console. This causes the agent's MRD to become stuck, preventing any further changes in the MRD state. As a result, the agent cannot receive additional calls, even though no active tasks or conversations are present in the system. The only way to resolve this issue is for the agent to log out and log back in, which allows the MRD state to be changed and calls to be received again. For Details see [CIM-26651](https://expertflow-docs.atlassian.net/browse/CIM-26651)
  * When an agent (A1) is on a call or initiating a call transfer or consult, if microphone permission is removed before the second agent (A2) answers, the Voice MRD state does not update as expected. Instead of transitioning to "PENDING_NOT_READY," which indicates the agent is temporarily unavailable the MRD state either remains "READY" or shifts to "NOT_READY" depending on the scenario, causing incorrect status representation. for more details see [CIM-26797](https://expertflow-docs.atlassian.net/browse/CIM-26797)

  
---|---  
  
### Multichannel Cases

| 

  * The MRD of the queue for a channel must match the MRD of the corresponding channel type. Failure to adhere to this requirement may lead to issues such as incorrect enqueuing of requests and failure to update MRD states during agent interactions.For Details see [CIM-13610](https://expertflow-docs.atlassian.net/browse/CIM-13610)
  * When a voice call request is enqueued and a customer simultaneously starts a web chat, if the customer leaves the voice call while the web chat is still active and upon pressing "_talk to agent_ " from the web chat interface after ending the voice call, the RASA response incorrectly states that an agent is requested but in reality, the chat is not routed to any agent. For Details see [CIM-13309](https://expertflow-docs.atlassian.net/browse/CIM-13309)
  * When a customer starts a web chat with an agent and subsequently initiates a voice call, if the initial agent (A1) does not answer the call and then becomes available again, the voice call is not routed back to A1 but remains in the queue. If another agent becomes available, the call is routed to other agents instead of A1. For Details see [CIM-14343](https://expertflow-docs.atlassian.net/browse/CIM-14343)

  
  
### Failover Scenarios

**Network Failure**| 

  * For Queue/Named Agent consult when the connection is re-establishing,and customer leaves during re-connection. The call will only end on the Agent Desk after the Agent presses the end call button for A1 and A2 call will be ended without any issue.
  * When the network is down and the Agent presses the _**Queue Transfer**_ button multiple times, no immediate error is shown. Once the network is restored, multiple Queue Error pop-ups are triggered and displayed to the user, corresponding to the number of times the _Queue Transfer_ button was clicked while the network was down.
  * If the SIP Media Server (Freeswitch) requires a VPN to be accessible, while the EFCX does not, then the following case may arise:
    * Agent disconnects from the VPN during a call.
    * Agent requests the call to be transferred to a named agent, or makes a request for a named-agent consult call.
    * A request is sent from the Agent Desk to Core, and a reserved agent is returned.
    * SIPjs throws an error as Media Server is inaccessible.
    * There is no further handling so the reserved agent stays stuck in a reserved state until the main call ends and conversation closes(closing associated tasks).

  
---|---  
**Refresh Cases**| 

  * If an agent refreshes during an active call, then the call ends for the customer, and a CALL LEG ENDED event is sent from the Agent Desk.
  * If an agent refreshes during/right before ringing, there are multiple cases that may occur that may arise depending on the net speed and how quickly refresh occurred:
    * Freeswitch catches the error as USER_NOT_REGISTERED i.e. C1 was attempted to be transferred to A1 but A1 extension was not registered(page had not loaded yet). The customer is played a message and their call ends. No issue on A1 side.
    * Freeswitch catches the error as NO_USER_RESPONSE i.e. A1 was refreshing in the middle of C1 transferring to A1. The customer is played a message and their call ends. No issue on A1 side.
    * Once the agent has refreshed their page, they will have their voice MRD stuck on READY. In the customer call, music stops, but after 30 seconds, the RONA case occurs. A new request is sent to core for an agent, however even a second agent will not receive this call. In core the task media has state RESERVED with task state ACTIVE. The conversation and task, both have A1 assigned to them. If C1 ends their call then conversation and task close and A1 is freed.
    * Additional cases if there are other calls in the queue as there may be an affect on the next call to be routed depending on total agents in the queue.
    * Even more additional cases possible in cases of manual outbound, consult, transfers (blind/consult), silent monitoring, barge.

  
**Routing Engine Pod Failure**| 

  * When a customer initiates a call and interacts with the IVR system, dialing a number before pressing `0`, and the RE (Routing Engine) pod is deleted during this process, the call gets stuck in the queue after pressing `0`. It does not route to an agent, and remains in the queue even though other agents are available. The call will only be cleared when the customer ends it. However, if the same customer calls again after ending the stuck call, the normal call flow proceeds as expected without any issue. For Details see [CIM-26658](https://expertflow-docs.atlassian.net/browse/CIM-26658)
  * Call Connects in Background Without Conversation View When RE Pod Is Restarted During Agent Reservation. For Details see [CIM-26659](https://expertflow-docs.atlassian.net/browse/CIM-26659)

  
**General Routing Issues**| 

  * Case: [CIM-25994](https://expertflow-docs.atlassian.net/browse/CIM-25994)[ CIM-12012](https://expertflow-docs.atlassian.net/browse/CIM-12012)
    * There is one agent Active for chat/voice in the system.
    * A chat/call is ringing on this agent, while there are others queued up.
    * If the customer ends their call/chat during ringing then the next call/chat is not routed to the agent.
  * Case: [CIM-15948](https://expertflow-docs.atlassian.net/browse/CIM-15948)
    * There is one agent in the system, and they are Active on a chat.
    * The agent makes a consult request on their own (empty) queue.
    * A customer chat enters the queue, and is placed behind the consult request.
    * The customer chat is not routed to the (only available) agent.
  * Case: [CIM-14343](https://expertflow-docs.atlassian.net/browse/CIM-14343)
    * A CX Voice call is ringing on an agent. The call times out, Voice MRD changes to NOT READY and RONA case occurs. There are two outcomes possible depending on the agent’s immediate action:
      * If the agent changes their Voice MRD to READY within 3 seconds, then the call is routed back to them.
      * If the agent waits for longer than 3 seconds to change their MRD to READY, then the call will be not be routed to them, even if there is no other agent in the system.
    * The RCA is provided in the linked task above.

  
  
  

