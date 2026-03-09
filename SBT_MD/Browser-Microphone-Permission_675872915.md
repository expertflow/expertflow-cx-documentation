# CX Knowledgebase : Browser Microphone Permission

Enables agents to have a smooth call experience by managing microphone access and preventing unclear call drops by clearly indicating the need for mic permission.

#### To enable

The agent must grant microphone access in the browser settings. There are no other specific prerequisites.

#### How it works

The following outlines the flow of how it works:

  1. **Agent Login and State Change**   
After the agent logs into the Agent Desk, attempts to set their _Voice MRD_ to a "Ready" state.

     * At this point, the browser prompts the agent to grant microphone access.

     * If the agent grants permission, the _Voice MRD_ is set to "Ready."

     * If the agent denies permission, the _Voice MRD_ is set to "Not Ready."

  2. **Post-Permission impact on Voice MRD**:

     * If the agent initially grants permission but removes it later, the _Voice MRD_ is automatically set to "Not_Ready."

     * If the agent changes the permission during an active call, the _Voice MRD_ is set to "Pending_Not_Ready."

  3. **Outbound Calls** :

     * Microphone permission is required to initiate outbound (OB) calls. If permission is not granted, the agent will be unable to start OB calls.




####  Impact on the Current System

**Before**| **Now**  
---|---  
  
  * If microphone permission is not granted before initiating or accepting a call, the call will drop without providing a clear reason, leading to confusion for the agent.
  * If an agent attempts to initiate a consult or outbound call without microphone permission, the call will then drop without indicating the cause.
  * If permission is removed during a call, the call will go silent, and even if permission is later re-granted, the voice functionality will not be restored.

| 

  * If microphone permission is not granted, the _Voice MRD_ is set to "Not_Ready," meaning the agent will be unable to receive any calls.
  * If a call reaches an agent after the mic permission is denied, the call will not drop. Instead, it will connect without audio. However, if the agent grants microphone permission during the call, audio will be re-established.
  * If microphone permission is removed mid-call, the _Voice MRD_ is set to "Pending_Not_Ready." If the agent re-grants permission, they will need to manually enable the _Voice MRD_ to resume handling calls.

  
  
#### Limitations

When an agent (A1) is on a call or trying to transfer or consult with another agent (A2), and microphone permission is removed before A2 answers, the Voice MRD status doesn’t update correctly. Instead of changing to "PENDING_NOT_READY" (which shows the agent is temporarily unavailable), the status either stays "READY" or switches to "NOT_READY," depending on the situation, which leads to an inaccurate status display. For more details see [CIM-26797](https://expertflow-docs.atlassian.net/browse/CIM-26797)
