# CX Knowledgebase : Handle WebRTC Calls

Allows agents to manage customer-initiated WebRTC interactions initiated directly through standard web browsers, ensuring smooth, real-time communication.

  * The WebRTC call is always a **multi-channel** call because the web session is always initiated first, and one can initiate audio or video calls.

  * The browser microphone and camera permissions should be enabled on the agent’s browser before responding to the calls.




## Audio Calls

An agent can only respond to the customer request when one’s status is available with a global state _Ready,_ and the MRD state for _CX Voice_ is also _Ready._

Upon receiving a new WebRTC audio call, the agent will see an incoming call notification with a button to **Accept** the request. The notification contains appropriate details of the customer, with a channel type icon to determine the channel through which the request was received (such as Web)

![image-20250724-100108.png](attachments/1208254675/1208778916.png?width=1141)

  * As the agent accepts the call, the call controls such as (answer, hold, resume, end) appear to handle the call.

  * The conversation view opens with _WebRTC_. The _WEB_ session starts and is active in the conversation view. The Channel Session data for the active channel is also available under the **Active Channels** dropdown in the conversation view.   


![W6.png](attachments/1208254675/1208778831.png?width=1072)



##   
  
Video Calls

Upon initiating a WebRTC video session, the agent responds to the request as follows:

  * The agent sees an incoming call notification with a button to **Accept** the request. The notification contains appropriate details of the customer, with a channel type icon to determine the channel through which the request was received.  


![image-20250724-093817.png](attachments/1208254675/1208877078.png?width=1125)



  * As the agent accepts the video call, the call controls and the customer video stream appear as the main view, along with a small view to represent the agent’s local video stream.

  * The conversation view opens with the _WebRTC_ and _WEB_ session active.


![AgentSide Use-20250725-095136.png](attachments/1208254675/1211236484.png?width=915)

  * The wrap-up window does not appear when a WebRTC audio call is ended. Agents are unable to submit wrap-up codes or notes post-call for WebRTC audio interactions.

  * Silent Monitoring & barge-in during ongoing conversations are not allowed.

  * Assistance Controls, such as Agent consult/conference/transfer, are not supported as of now.

  * Call Timer Freezes on Maximized View when Navigating Away During WebRTC Video Call in Minimized Mode




## Related Articles

  * To see WebRTC configurations, please check this [guide](WebRTC-Configuration-Guide_687309794.html). 



