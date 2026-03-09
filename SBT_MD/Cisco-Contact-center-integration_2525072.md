# CX Knowledgebase : Cisco Contact center integration

Expertflow CX can be integrated with Cisco Contact Center Express and Enterprise. See this [Architecture Diagram](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/2529293/Platform+Architecture+Overview) for how CX solution components integrate with Cisco UCCE/X.   
  
The CX Agent Desk communicates with Cisco Finesse to login Cisco Contact Center agents on the Agent Desk and receive CTI events. 

## Supported Features

  * **Embed Agent Desk as a Finesse Gadget**

    * You can embed the CX Agent Desk in Cisco Finesse for agent and supervisor controls to handle digital and social media interactions in addition to Cisco contact center calls. 

  * **Finesse Agent Login in Standalone Agent Desk**

    * You can login the Cisco Finesse for agent and supervisor in standalone CX Agent Desk to handle digital and social media interactions in addition to Cisco contact center calls. 

    * Finesse Call Controls are used for call handling.




### Agent Login 

A finesse agent is logged in to CX Agent Desk automatically upon login to Cisco Finesse for both NON-SSO and SSO and for both UCCX and UCCE.

Upon the Agent Desk login, the system uses the browser cache for state maintenance. Therefore any private browser or incognito-mode blocking browser cache will not work.

### Agent State Change

As an agent, you can change your agent state from Cisco Finesse. The state change is synchronized with the CX-Agent state (Cisco CC MRD). 

### Wrap-up call

As an agent, you can wrap up the call from within the Agent Desk by using a Finesse Wrap-up timer and wrap-ups. 

When a call ends, the finesse wrap-up timer starts and you can add Finesse wrap-ups by using Finesse wrap-up codes. Wrap-up codes applied using the Finesse toolbar are part of the call leg and visible in the Agent Desk conversation view as past interactions. 

When the finesse wrap-up timer ends, the Agent Desk conversation view closes. You can even add wrap-up codes and notes from within the CX Agent Desk. Wrap-up codes applied from the Agent Desk are just visible in the conversation view but not pushed to Cisco Finesse.

Wrap-up time is also added in the CX Call Duration.

### Call Controls

**Capability**| **Description**  
---|---  
Answer call| In addition to Cisco Finesse, agents can see and respond to an incoming call alert from within the Agent Desk.   
End call| In addition to Cisco Finesse, agents can end the call from within the Agent Desk.   
Inbound Call| Agents can handle inbound calls using Cisco Finesse or the Agent Desk.  
Hold/Resume| Available via Cisco Finesse call controls. Not available from within the Agent Desk  
Direct Transfer| Enables agents to transfer the ongoing call using the finesse toolbar along with the active conversation. This feature is available for both queue and extension.

  * When call is transferred on Jabber Agent Extension, unstable behavior is observed, for details see [CIM-12336](http://project.expertflow.com:8080/browse/CIM-12336)
  * In CCX, on a manual OB call, when ending a call transferred from A1 to DN, the dialogState event incorrectly shows CallEnded as 1 while the call is still ACTIVE. This causes erroneous data transmission to the CX core, creating two separate activities on direct transfer. For details see [CIM-10890](http://project.expertflow.com:8080/browse/CIM-10890)
  * In CCE, When a direct transfer is made to an extension, an incorrect "Consult Call" is received on the Agent Desk instead of the expected alert event. This prevents the alerting notification from appearing on the Agent Desk. For details see [CIM-13867](https://expertflow-docs.atlassian.net/browse/CIM-13867)
  * In CCE, When Agent A transfers a call to Agent B on extension, and Agent B transfers it back to Agent A, the call duration for the third leg is not displayed, and the total duration is calculated based only on the first two legs. In addition to this, the third leg incorrectly shows a queue name, and the tooltip on the phone icon displays "Direct Transfer" instead of "Call End." For Details see [CIM-26267](https://expertflow-docs.atlassian.net/browse/CIM-26267)
  * In CCE, When Agent A directly transfers a customer's call to a queue, and Agent B accepts the call, two separate call legs are created in the conversation view instead of being correlated. For Details see [CIM-26287](https://expertflow-docs.atlassian.net/browse/CIM-26287)

  
Consult Call| Allows agents to initiate a consult call using the finesse toolbar. This feature is available for both queue and extension.

  * The agent can do a consult call using Cisco Finesse controls for initiating a consult call. However, the Consult call activity is not stored as a CX-Activity as part of the interaction history.
  * In CCE, When Agent A initiates a consult call to Agent B via DN/Queue, receive incorrect events when we make a consult call to A2 and instead of the assistant role A2 becomes the primary participant which makes the call ‘Conference’ instead of consult. If either Agent ends the call, the CTI signals DIALOG_ENDED, closing the session only for that agent, while the other agent's conversation view remains open and needs to be manually closed. No tracking occurs for the consult call as no event is passed to the core. Additionally, if the customer or Agent A leaves, the consult call persists, and Agent B's conversation view remains open until manually closed. For details see [CIM-13869 ](https://expertflow-docs.atlassian.net/browse/CIM-13869)
  * In CCE, When a consult call is initiated to a queue, both Agent A1 (consulting agent) and Agent A2 (consulted agent) are incorrectly marked as primary agents. This allows A2 to send messages to the customer in the web chat, even though A1 should remain the primary agent for both the call and chat. The participant list should reflect A1 as the primary agent, with A2 as a secondary participant, preventing A2 from sending messages to the customer. For details see [CIM-26311](https://expertflow-docs.atlassian.net/browse/CIM-26311)
  * Consult leg time is also added in the CX Call Duration.

  
Consult Transfer| Enables agents to transfer an ongoing customer call to the consulted agent using the Finesse toolbar.

  * In CCX, when A1 tries to transfer a customer call after establishing a consult call with A2, a duplicate ending event occurs. A1 receives an error message indicating a session issue, while A2 receives a misleading error message but retains the conversation view. For Details see [CIM-14253](http://project.expertflow.com:8080/browse/CIM-14253)
  * In CCE, When Agent A initiates a consult call to Agent B via DN/Queue, the lack of a distinct indicator for the consult call causes Agent B to be treated as a primary participant, creating a conference scenario. Upon transfer, CTI events on Agent A indicate the call as ended instead of transferred, closing the session for Agent A. However, no end event is received for Agent B, leaving the conversation open, and needs to be closed manually. As a result, the CX activity remains inconsistent. For details see [CIM-13870](https://expertflow-docs.atlassian.net/browse/CIM-13870)
  * In CCE, When a consult call is made to Agent A2 on their extension, the tooltip that appears when hovering over the call leg incorrectly displays "Direct Transfer" instead of "Consult Transfer."For Details see [CIM-26312 ](https://expertflow-docs.atlassian.net/browse/CIM-26312)

  
Consult Conference| Enables agents to add a consulted agent to an ongoing customer call resulting in a conference call using the finesse toolbar.

  * In CCX, for A2, the Conversation View disappears intermittently. No event is recorded in Conversation View as conversation history. For details see [CIM-12218](http://project.expertflow.com:8080/browse/CIM-12218)
  * When a customer disconnects a conference call involving A1 and A2, agents must manually close their conversation view after the other agent ends the call. Specifically, if A1 disconnects after the customer, A2's conversation view needs to be manually closed, and if A2 disconnects after the customer, A1's conversation view needs to be manually closed. For Details see [CIM-14282](http://project.expertflow.com:8080/browse/CIM-14282)****
  * In CCE, When Agent A initiates a conference consult call with Agent B and the customer, Agent B is added as a primary participant without proper indication of the call type. If any agent leaves the call, a DIALOG_ENDED reason is received, closing the session only for that agent. The other agent’s conversation view remains open and needs to be manually closed. Additionally, CX activity inaccurately shows only one call leg for the consult conference. For details see [CIM-13871](https://expertflow-docs.atlassian.net/browse/CIM-13871)

  
Consult/Conference/Transfer| Available via Cisco Finesse call controls. Not available from within the Agent Desk  
Manual Outbound Call| Agents can manually dial outbound calls directly from Cisco Finesse.In an Outbound Call, the ringing time is also added in CX Call Duration.  
  
### Customer Interactions

For an active call, the agent can see the interaction history with the calling customer. For the active call, the agent can also see IVR activities. The interaction history shows past activities with the customer including but not limited to chat, calls, and scheduled activities. See [CX Activities](Messages%2C-Events%2C-and-Activities_2528021.html) for more information.

## Compatibility with Cisco Contact Center releases

The solution works with Cisco UCCX and UCCE. Contact center integration limitations are covered in [Cisco Voice Channel Limitations](Cisco-Voice-Channel-Limitations_74514469.html). 

### Eleveo Recordings to CX (Integrated with Cisco)

We support middleware to push the recording links from Eleveo with the CX call activity. Following are the **limitations** of this feature:

**Limitation**| **Description**  
---|---  
Direct Transfer| 

  * If a call is direct transfer to the same agent which receive customer's call then recording gets merged.
  * The recording of A1C1 initially and at the end when A1 receives the C1 call, both recordings get merged and repeated in first and third leg. For Details see [CCC-1734](https://expertflow-docs.atlassian.net/browse/CCC-1734)

  
Outbound via campaign| 

  * Call which made via Outbound campaign, its activity is not created in the system and so recording will not be pushed. See [CCC-1736](https://expertflow-docs.atlassian.net/browse/CCC-1736)

  
A2 left conference| 

  * Middleware not retrieve A1C1 audio when A2 left the conference. For details see [CCC-1738](https://expertflow-docs.atlassian.net/browse/CCC-1738)

  
A2 hold during conference| 

  * When A2 hold during a conference, then A1C1 audio not recorded. For details see [CCC-1742](https://expertflow-docs.atlassian.net/browse/CCC-1742)

  
A1 resume during conference| 

  * During conference when A1 hold and then A2 hold.
  * When A1 resume, A1C1 segment will not be recorded. For details see [CCC-1742](https://expertflow-docs.atlassian.net/browse/CCC-1742)

  
When customer left conference| 

  * When customer left the conference call, then the conference leg is not being created in the system. For details see [CCC-1739](https://expertflow-docs.atlassian.net/browse/CCC-1739)

  
Conference case| Conference leg audio repeats twice when a user playback the recording. This only occurs in old recording method. For details see [CCC-1762](https://expertflow-docs.atlassian.net/browse/CCC-1762)  
Hold Time| Hold Time is also calculated in CX Call Duration.  
  
### Recording Permissions on the Agent Desk

**Limitation**| **Description**  
---|---  
Permission for Conference Recording| Currently, A1 can’t access the conference leg recording. It can only be accessible by A2. For details see [CCC-1753](https://expertflow-docs.atlassian.net/browse/CCC-1753)
