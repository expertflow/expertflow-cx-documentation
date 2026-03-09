# CX Knowledgebase : WebRTC for CX

Introduces WebRTC functionality to the Expertflow CX platform, enabling customers to initiate direct voice and video communication with agents using standard web browsers. 

## WebRTC Capabilities

  * Audio Calls

  * Video Calls  





WebRTC call is always a **multichannel** call because the web session is always initiated first. After initiating the web session one can start audio or video calls.

### Audio Calls 

Allows customers to initiate an audio call to the business and engage with a self-service experience through either traditional or conversational IVR. Based on the nature of their inquiry, customers can be routed to the appropriate agent to ensure the resolution.

#### Steps to Initiate an Audio Call 

  * Allows the customer to initiate an audio call from the customer widget after filling the pre-conversation form.

![W1.png](attachments/687211264/1017479338.png?width=332)

  * Click the start chat button ![startchat.png](attachments/687211264/1118109744.png). The customer will see a bot welcome message and two icons ![Audiocontrols.png](attachments/687211264/1118044266.png) , one for chat and the other for call, on top of the customer widget. 

  * The customer has to enable the browser microphone permissions before initiating the call.

  * After clicking the call button, the customer can initiate an Audio call. 

![W4.png](attachments/687211264/1017217218.png?width=323)



###   
Video Calls

Enables customers to initiate a video call to the business and have access to a self-service experience through either traditional or conversational IVR. I expect to be routed and connected to the appropriate agent based on my needs.

Enables customers to initiate video calls directly with the business and engage with a self-service journey via traditional or conversational IVR. Based on the inquiry, the system routes them to the most appropriate agent to ensure faster resolution.

#### Steps to Initiate a Video Call 

  * The customer initiates a video call using the customer widget after filling out the pre-conversation form.

![W1.png](attachments/687211264/1017479338.png?width=332)



  * Click the start chat button ![startchat.png](attachments/687211264/1118109744.png). The customer sees a bot welcome message & two icons, ![cahtToolbar.png](attachments/687211264/1116768015.png) for Video & Chat, on top of the customer widget. 

  * The customer has to enable the browser microphone & camera permissions before initiating the call.

  * After clicking the video button, the customer can initiate a video call.

![Customer use1-20250725-080505.png](attachments/687211264/1211039922.png?width=366)



  * During an active video call, if the agent puts the call on hold and the customer stops and restarts their video, the customer will see a black screen instead of the remote video. ([CCC-1806](https://expertflow-docs.atlassian.net/browse/CCC-1806))

  * Camera Permissions

    * If removed **during an active call** , both agent and customer videos stop, voice continues, and a console error is logged without UI feedback.

    * Granting camera permission does not auto-enable video; the user must press the camera icon twice to resume video.

    * Removing camera permission and toggling the camera shows no UI error but logs a console error, disables local video on the customer widget, and breaks functionality.




## Related Articles

  * To see WebRTC configurations, check this [guide](WebRTC-Configuration-Guide_687309794.html).

  * To see the customer widget media permission details, check this [guide](Managing-Microphone-and-Camera-Permissions-in-the-Customer-Widget_1733230599.html).

  * To see the agent’s experience of handling WebRTC calls, check this [article](Handle-WebRTC-Calls_1208254675.html).



