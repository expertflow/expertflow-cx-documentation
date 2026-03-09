# CX Knowledgebase : Agent Hand Raise

This feature enhances agent-supervisor collaboration by allowing agents to request assistance during customer interactions discreetly. Supervisors can promptly identify and respond to these requests without disrupting the conversation flow.

### Initiating a Hand Raise Request

During a customer conversation, the agent can click the **Hand Raise** icon to signal a

supervisor for help. 

![image-20251125-072341.png](attachments/519569565/1484652584.png?width=399)

This icon can be toggled to withdraw the request if assistance is no longer needed.

### Supervisor Response to Hand Raise Request

When an agent raises their hand, supervisors receive a push notification with the following options:

![image-20251124-140329.png](attachments/519569565/1481212119.png?width=368)

**Action**| **Description**  
---|---  
Join| Enter the conversation in Whisper mode to assist the agent.  
Dismiss| Remove the notification from the screen.  
  
### Key Points:

  * Notifications are sent to both primary and secondary supervisors of the agent’s team.

  * Notifications automatically disappear after 30 seconds if no action is taken.

  * The notification is cleared for a supervisor once they join the conversation.

  * A sound alert is played once for multiple simultaneous requests and stops when all notifications are cleared or dismissed.




## Joining HandRaise Requests from Dashboard

In the **Ongoing Conversations Detail Dashboard** , an alert icon appears next to any conversation where an agent has raised their hand. Supervisors can join the conversation directly in Whisper mode by clicking this icon. 

![image-20251118-125834.png](attachments/519569565/1461026900.png?width=1418)

Alternatively, they may enter in Silent Monitoring mode and switch to Whisper mode as needed, which will automatically lower the hand raise request.

## Hand Lowering Upon Assistance

Once a supervisor joins the conversation in Whisper mode, the hand raise icon is removed from the dashboard and conversation view, indicating the request has been addressed.

**Limitations**

  * If a supervisor joins the conversation, the notification will not be dismissed for other supervisors. This means that more than one supervisor can join the conversation. However, the handraise icon on the dashboard no longer appears for a conversation where a supervisor has already joined.

  * The feature is available only for digital chat channels. HandRaise is not supported over CX Voice because Whisper over the Voice is not yet supported. 

  * In case if a voice session (CX_VOICE or CISCO_CC) is active, the hand raise icon will not be displayed.

  * If a voice session starts after a hand raise request, the supervisor will still see the request, but the icon will be disabled for the agent.

  * Agents can submit multiple hand raise requests per conversation. However, if a supervisor is already present, new requests will not be visible to that supervisor until they leave the conversation.



