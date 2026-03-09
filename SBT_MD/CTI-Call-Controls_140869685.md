# CX Knowledgebase : CTI Call Controls

Agents avail with call control functions via Agent Desk (Agent SDK) CTI toolbar. To improve usability, and enhance agents' overall call-handling experience, agents have the option to fix the CTI toolbar in the conversation view.

When agents answer a call, they have a clear indicator showing the active call status, in a fixed location and the conversation view is open for agents to perform any activity.

![image-20241018-103200.png](attachments/140869685/601980968.png?width=1080)

### Call Controls

  * Agents have the following call control functions via the Agent Desk CTI toolbar.




**Capability**| **Description**  
---|---  
Answer call| View and respond to an incoming call alert  
End call| End the current call  
Hold call| Hold the call - with hold timer started  
Resume call| Resume the call - with hold timer closed  
Consult/Conference| Consult, consult-transfer, conference with other agents  
Consult Transfer| Transfer the call to the consulted agent.  
Popout toolbar| The icon on the extreme left on the toolbar allows to popout the toolbar in a floating view where it can easily be dragged and dropped to reposition. Agents may also choose to fix it in one location.  
  
CX-Voice is under active development. See [CX Voice Limitations](CX-Voice-Limitations_74448913.html) for some open agent controls/capabilities issues. 

### Answer Call

  * On accepting an incoming customer call, the CTI toolbar appears with the following controls:




**CTI Call Controls**|   
---|---  
  
  1. Maximize/Minimize
  2. Mute/Unmute
  3. Hold/Resume
  4. End Call
  5. Dialpad for DTMF

| ![image-20241018-103317.png](attachments/140869685/602374159.png?width=364)  
  
### Minimize

  * This Minimize button provided on the toolbar facilitates the agent to clear his conversation view. As the agent accepts the call, this toolbar pops up anywhere on the screen. On clicking this Minimize button, this toolbar moves automatically on the right-hand expandable side of the conversation view as can be seen in the screenshot below.


[2024-10-18_15-47-03.mp4](attachments/140869685/602112042.mp4?width=1080)

### Mute/Unmute

This ![image-20241018-103409.png](attachments/140869685/602243091.png) button on the toolbar enables an agent to mute or unmute the call if and when required.

### Call Hold/Resume

  * The agent can put an active call on hold using the **Hold** button. once hold button clicked hold timer started.

  * In the same way, one can resume the held call using the **Resume** button as they become available again & hold timer stopped once resume button is clicked.




For now, one button is being used for hold/resume.

![holdTimer-20241112-134131.png](attachments/140869685/671089041.png?width=720)

### End Call 

  * The agent can end a call using the **End** Call button. This will end the call leg between the agent and the customer.


![image-20241018-104222.png](attachments/140869685/602177577.png?width=720)

## Dialpad Integration for DTMF

  * Agents can send Dual-Tone Multi-Frequency (DTMF) signals using the dialpad on the Agent Desk interface.




### DTMF during Active calls

  * During active calls, agents can send Dual-Tone Multi-Frequency (DTMF) signals through the available dialplan to interact with systems or press the key for specific information.


![dtmf-min-20241028-122304.png](attachments/140869685/626524182.png?width=800)

![dtmf-max-20241028-085831.png](attachments/140869685/625475654.png?width=800)
