# CX Knowledgebase : Interruptible and Non-Interruptible Medias

This configuration enables the system to mark media as either interruptible or non-interruptible.

An interruptible media can be interrupted if the agent receives a request on a non-interruptible media. In contrast, a non-interruptible media cannot be interrupted, regardless of any requests received on other media.

**Voice MRD**| **Chat MRD**| **Result**  
---|---|---  
Non-Interruptible| Non-Interruptible| 

  1. Voice call comes in first:
     1. On agent reserve state, don’t interrupt Chat MRD
     2. This means that if a new chat arrives, it will be routed to the agent and he will be handling both voice and chat
  2. Chat comes in first:
     1. On agent reserve state, don’t interrupt Voice MRD
     2. This means that if a new voice call arrives, it will be routed to the agent.

  
Non-Interruptible| Interruptible| 

  3. Voice call comes in first:
     1. On agent reserve state, interrupt Chat MRD.
     2. This means that the agent's chat state will be changed to “interrupted”, and he will not receive any chats.
  4. Chat comes in first:
     1. On agent reserve state, don’t interrupt Voice MRD
     2. This means that if a new voice call arrives, it will be routed to the agent.
        1. Now at this stage, as chat MRD is interruptible, the chat state will be changed to “interrupted”.
           1. Send a chat interrupted event to the controller to decide what to do with the existing chats e.g, re-route to queue, or hold the conversation, etc.  
(**by default, we will re-route all ongoing chats to their relevant queues - with a custom message to the customer**)

  
Interruptible| Non-Interruptible| 

  1. Voice call comes in first:
     1. On agent reserve state, don’t interrupt Chat MRD
     2. This means that if a new chat arrives, it will be routed to the agent and he will be handling both voice and chat.
        1. As chat is a non-interruptible MRD and voice is interruptible in this case, the voice state will be changed to “interrupted”.
           1. Send a voice interrupted event to the controller to decide what to do with the existing voice: EF to not do anything to the existing voice call.
  2. Chat comes in first:
     1. On agent reserve state, interrupt Voice MRD
     2. The voice state will be changed to “interrupted”. (In the case of Cisco, it can be Not_Ready with an “interrupted” reason code)

  
Interruptible| Interruptible| 

  3. Voice call comes in first:
     1. On agent reserve state, interrupt Chat MRD
     2. Chat state will be changed to “interrupted” and no chats can be assigned.
  4. Chat comes in first:
     1. On agent reserve state, interrupt Voice MRD
     2. Voice state will be changed to “interrupted” (In the case of Cisco, it can be Not_Ready with “interrupted” reason code)

  
  
For the Cisco CC channel, even if the channel is not integrated with the system, the associated MRD will be set to **INTERRUPTED**. This change has been introduced in the **CX 4.7.3** release.

The 'Put Conversation on Hold' action is available starting from release 4.10.6. Prior releases only have the default action 'Remove All Agents'."

## Actions on Interruptible Medias:

When an agent is serving an interruptible media and a request is received on a non-interruptible media, there are several actions we can configure to happen with the existing requests on the interruptible media. This configuration can be set by going to Conversation Studio and selecting the appropriate action for the "On MRD Interrupted" node of the "Agent MRD Interrupted" flow.

![image-20260213-051410.png](attachments/556597289/1730805854.png?width=772)

Following are the actions available in the system:

  1. **Remove All Agents**



  * When enabled, if an interruptible MRD is interrupted, all conversations will be removed from the agent who has accepted a request on a non-interruptible MRD.



  2. **Put Conversation on Hold**



  * When enabled, the interrupted conversation will be put on hold. The conversation will resume back to active state if:

    * The agent gets freed from the request on non-interruptible media.

    * The agent sends a message to the customer. 



