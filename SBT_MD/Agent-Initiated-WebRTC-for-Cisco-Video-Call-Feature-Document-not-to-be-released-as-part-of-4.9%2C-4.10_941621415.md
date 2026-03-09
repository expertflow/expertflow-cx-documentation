# CX Knowledgebase : Agent Initiated WebRTC for Cisco Video Call Feature Document-not to be released as part of 4.9, 4.10

**Agent initiated WebRTC** allows agents to securely start WebRTC video and audio calls with customers during chats. It seamlessly integrates with Cisco Finesse, SIP, and CCM to ensure ongoing conversations. Encrypted, one-time links maintain security and prevent unauthorized access.  
  
## Business Value

  * **Seamless Transition** : Seamless Transition: Transition from chat to video/audio calls without disrupting workflows.

  * **Enhanced Security** : Time-bound, encrypted links ensure secure communication.

  * **Unified History** : Maintain a consolidated conversation history across chat and WebRTC channels.

  * **Improved Resolution** : Visual troubleshooting leads to faster issue resolution.




## Feature Details

### 1\. Secure Link Generation & Management

**System validates:**

  * No ongoing call or active WebRTC link exists.

  * Customer profile exists.




**Agent Experience**

  * During an active chat session, the agent clicks the "Video Link" option within the Message Composer.  



![glb.png](attachments/941621415/969506826.png?width=940)

  * A secure link preview appears in the message composer.  



![glbpre.png](attachments/941621415/969441360.png?width=910)

  * A secure, time-bound link is generated and sent to the customer.  



![glbsent.png](attachments/941621415/969441397.png?width=917)

**Customer Experience**

  * Receives the secure link via Web Chat  



![customer-view.png](attachments/941621415/969539601.png?width=361)

  * Receives the secure link via other chat channels (WhatsApp, Facebook , Instagram, etc)


![secure link whatsapp.jpg](attachments/941621415/969768961.jpg?width=591)

  
  


### 2\. Secure Link Component:

  * Generates time-bound encrypted URL (default 15min expiry)

  * Updates agent’s state to "**Not Ready - WebRTC Call** " via Finesse API  



![state-change-to-rtc.png](attachments/941621415/969408529.png?width=923)

  *  _Link Expiry Scenarios:_  





**Condition**| **Action**  
---|---  
  
  * Agent manually changes state

| 

  * Expire link, toaster notification displayed  
![manual-state-change.png](attachments/941621415/969408543.png?width=848)

  
  
  * Successful call establishment

| 

  * Auto-expire link, toaster notification displayed  
![expired-ongoing-call.png](attachments/941621415/969637933.png?width=848)  


  
  
  * Timeout (default:15min)

| 

  * Auto-expire link

  
  
  * New link generation attempt

| 

  * Block until current link expires, toaster notification displayed![already-gen7.png](attachments/941621415/969408550.png?width=848)

  
  
### 3\. WebRTC Session Establishment

 _**Customer Experience:**_

**Secure link received via web chat channel**  
---  
**Action**| **Customer** **Experience**  
  
  * Clicks the secure link in received in web chat

| ![Screenshot 2025-03-17 063318.png](attachments/941621415/969441463.png?width=351)  
  
  * Can switch to the web chat tab during an active WebRTC call.

| ![switch to chat.png](attachments/941621415/969605205.png?width=206)  
  
  * Can switch to the video call tab during an active WebRTC call.

| ![switch to video.png](attachments/941621415/969638026.png?width=208)  
  
**Secure link received via non web chat channels (WhatsApp, Facebook , Instagram, etc)**  
---  
**Action**| **Customer Experience**  
Clicks the link| ![initiate via third.png](attachments/941621415/969605212.png?width=229)  
  
  * Clicks the Join button  
Only video icon is visible since the customer joins the link via non web chat channel

| ![only video button.png](attachments/941621415/970031106.png?width=201)  
  
  * Ends the call  
As there is no active web channel, the following screen will appear to the customer

| ![call end when initiate whatsapp.png](attachments/941621415/970063878.png?width=195)  
  
  


**Agent Experience**

  * Receives an inbound call via Jabber/Agent Desk  



![ringing-call.png](attachments/941621415/969539592.png?width=784)

  * Accepts the call to establish the WebRTC session.  



![active call agent.png](attachments/941621415/969965589.png?width=953)

### 4\. Expired Link

  * If the customer clicks an expired link sent via web chat, they are notified that the link is no longer valid 


![Screenshot 2025-03-17 063558.png](attachments/941621415/969637926.png?width=335)

  * Similarly, if the customer clicks an expired Link sent via non web chat channels (WhatsApp, Facebook , Instagram, etc)  
The join button will be disabled  



![disable join button.png](attachments/941621415/969408717.png?width=186)

## Note:

### **Link Expiry and Call Duration Details**

  1. **Link Expiry** :

     * The expiry time applies exclusively to the secure link and is independent of the call duration or termination.

     * The expiry timer initiates immediately upon link generation, irrespective of whether the link has been shared with the customer.

     * If a link is re-generated for the same customer, the system will return the same link, provided the previous link has not yet expired.

     * If the chat session is closed and the link is not expired then agent has to manually change the cisco state to expire the link for the new customer

  2. **Customer SLA for WebRTC Channel** :

     * The customer's Service Level Agreement (SLA) for the WebRTC channel must exceed the maximum allowable call duration to ensure uninterrupted service.

  3. **Agent SLA and Voice Channel Considerations** :

     * If a voice channel is active within the conversation (as WebRTC is inherently a voice-based channel), the agent's SLA will be automatically disabled.

  4. **Maximum Call Duration Timer** :

     * The **Maximum Call Duration Timer** defines the maximum time (in minutes) a call can remain active before Cisco CallManager terminates it.

     * **Key Details** :

       * **Default Value** : 720 minutes

       * **Minimum Value** : 0 (disables the timer)

       * **Maximum Value** : 35,791 minutes

       * **Unit** : Minutes

     * **Note** : This is a mandatory configuration field.




## Limitations

  1. **No Real-Time Notifications** :

     * Customers and agents are not notified in real-time if a link expires due to timeout.

     * Customers must click the link to check its validity.

  2. **Session Interruptions** :

     * Logging out during an active WebRTC session may cause unexpected behavior.

     * Refreshing the agent’s tab stops the video on the customer’s side.

     * Refreshing the customer’s tab drops the call.

  3. **UI Behavior** :

     * The "Generate Link" button disappears if the agent types a message in the composer.  


![type text.png](attachments/941621415/969506943.png?width=914)
     * Unexpected behaviors may occur during hold/resume, mute/unmute, or camera on/off actions.

  4. In certain cases, when a customer holds and quickly resumes a Secure Link call, audio issues may occur, such as the customer not hearing the agent while hold music continues on the agent's side.

  5. Rapid toggling of the camera (stop/start) may lead to UI and video playback state becoming out of sync, resulting in incorrect status indicators or a grey screen in the video display area.

  6. Performing rapid and repeated hold/resume actions may cause the call view to terminate unexpectedly on the customer side, leading to a UI hang when attempting to join a new Secure Link session.

  7. When an agent ends the conversation with Customer1 before they join a previously generated Secure Link, a new link cannot be generated for Customer2 until the original link expires or the agent manually resets the Cisco state

  8. After the agent resumes a Secure Link call from hold, the customer's video may be delayed or appear frozen on the agent's side for 7–10 seconds, resulting in inconsistent video rendering.

  9. When an agent handles both a Secure Link call and a direct extension call simultaneously, ending the Secure Link call may trigger duplicate confirmation dialogs and prevent manual conversation closure until the agent desk is refreshed.

  10. Audio and video controls remain active when a Secure Link call is placed on hold by the agent, allowing unintended interaction; these controls should be disabled during hold state.

  11. When an agent ends a conversation after sending a Secure Link, the link remains active, allowing the customer to join and initiate a call. However, the agent cannot send messages during this resumed call until or unless customer sends the message first (WhatsApp/Facebook).

  12. Under conditions of slow or unstable internet, minimizing the Secure Link call window and switching to the browser can cause UI disruption on the Jabber screen.

  13. When a WebRTC audio call ends, either by the agent or customer, the wrap-up window does not appear on the Agent Desk, preventing agents from completing the post-call wrap-up process and requiring manual state changes for CX-Voice.

  14. During an active Secure Link call, the agent’s video may freeze or get stuck on the customer widget, causing disrupted video display on the customer side.

  15. "When an agent closes the browser tab during an active Secure Link call and then logs back in, the Secure Link call remains active while simultaneously allowing a Cisco IP call to start, causing overlapping active calls and SLA conflicts.

  16. The agent’s state and Cisco MRD state may not update correctly during an active Secure Link call, leading to inconsistencies in call status tracking. The state remain the same but his dialog went into the TALKING

  17. "The agent and Cisco MRD states may not update correctly when accepting calls initiated from Cisco (IP), causing inaccurate status reporting.

  18. Even with certificates installed, the customer widget may close unexpectedly after joining a Secure Link call, requiring re-login (sometimes in incognito mode) to resolve

  19. "When the WebRTC customer inactivity timeout expires, the session-end message does not trigger call termination, causing the Secure Link call to remain active on both ends

  20. When an agent begins typing a message before generating a Secure Link, the options to generate the link and attach files become unavailable, restricting message composition flexibility

  21. WebRTC calls are browser-based calls, and once the page is refreshed or closed from the customer widget, the Active calls get dropped. There is no way to retrieve those calls; the only solution is to initiate a new call. for reference [CX-Voice Limitations](CX-Voice-Limitations_74448913.html)

  22. Refreshing the agent’s browser during an active Secure Link call may cause the agent’s video feed to stop on the customer side, disrupting the video communication.

  23. The system behaves inconsistently when an agent logs out during an active Secure Link call, leaving the call active on the customer side while the agent session resets, causing confusion and broken call state synchronization.

  24. In the case of **Voice session getting started for the same customer** who already has an ongoing **Chat session** , the default behavior is as follows:

     * The **Chat media** in the task is closed and the media is elevated to the **Voice MRD**.

     * As a result, the **Chat MRD** state is updated accordingly:

       * For example, if only a single chat was active, the MRD state would have been **Active** and will now change to **Ready**.

Regarding the **Voice MRD** :

     * If the voice task is a **queue-based task** , the **Voice MRD** will be set to **Busy**.

     * If it is an **agent-based task** (i.e., assigned directly to the agent without routing), the **Voice MRD state will not be updated**.




## Conclusion

This feature enhances customer support by enabling secure, seamless transitions from chat to video/audio calls. While it offers significant business value, users should be aware of its limitations to ensure optimal usage

  

