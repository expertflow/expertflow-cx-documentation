# CX Knowledgebase : Controller Bot Training

## **Context**  
  
In this document we will explain the overall controller training and also explain how we add new training for controller.

## **Controller****Training**

In controller there are different training for controller which already configure in it and we also add new training file.First we discuss the the already configure training's and after that we see that how we add new training to the controller. Before explaining the list of training event / action we explain the common things which is use in all the training.

All the training file is basically is a python file and all are containing a method called **run** which accept some parameter which are listed below.

Parameter| Description  
---|---  
self|  the self variable is a commonly used convention for referring to the instance of a class within its own methods  
conversation| conversation parameter contain an object of conversation which contain all info about conversation  
slots| slots parameter contain attribute in key value pair for a conversation / event .we also add slots in a conversation.  
dispatcher| dispatcher is basically a respond back action from a controller  
metadata| metadata contain metadata of a conversation its not be used in training  
  
Here is the list of all the configure training events:

Event| Description  
---|---  
**CONVERSATION_STARTED**|  In this training action we first get the channel session from slot and than we get bot id from that channel session and set the role is **PRIMARY**. After that we respond back an action with the help of dispatcher name **ASSIGN_BOT** with bot id and role.  
**AGENT_SUBSCRIBE**|  In this training action we get conversation id from conversation and agent id from slot **agentParticipant- >participant→id. **If there is no channel session than we respond back an action with the help of dispatcher name **REVOKE_REQUEST** with reasonCode **CANCELLED** and agent_id. After that we return by set the slot of **agent_state** to **not_requested.** If there is a channel session than we get bot participant from conversation and if there is bot participant and its role is **PRIMARY** than we get bot id and respond bank an action by dispatcher name **CHANGE_PARTICIPANT_ROLE** with role is **ASSISTANT** and bot id latter we set the slot **agent_state** to **subscribed.**  
**AGENT_UNSUBSCRIBE**|  In this training action we first get conversation id from conversation after that we get cc_user list and channel session list from conversation. If there is no cc_user mean there is no agent all the agent are left the conversation we get the agent_state from slot and direction from agent_state if the agent_state is "**requested** " and direction is "**DIRECT_CONFERENCE** " than we respond back an action by dispatcher name **CANCEL_RESOURCE** with reasonCode **CANCELLED**. After that we check that if there is no channel session main all the customer are left that we respond back an action by dispatcher name **END_CONVERSATION** and return with type reset. Otherwise if customer is still present than we check if there is a bot participant than change his role **PRIMARY** with the help of dispatcher action name **CHANGE_PARTICIPANT_ROLE** with role. After that we get schedule timer as events from slot and conversation . If agent_state is requested and direction is **DIRECT_TRANSFER** than return that events. After that we get routing mode from conversation channel session and reason code from slot **agentSubUnSubReason**. If routing_mode is **PUSH** and reason code is **FORCE_LOGOUT** than dispatcher an action name **FIND_AGENT** and append event with set slot agent_state to request and return that events .Otherwise append event with set slot agent_state to not_requested and return that events.   
CHANNEL_SESSION_STARTED| In this training we first get conversation id from conversation after that we get channel session from slot and channel sessions list from conversation. After that we get **channel_session_sla_map** from slot key and set channel session['id'] in channel_session_sla_map to **False.** After that we schedule timer for all sessions as a event .After that we get latestIntent from channel session if there is no channel session than dispatcher a text "Hey! this is sparrow from Expert Flow. How may i help you today?" and return all events  
CHANNEL_SESSION_EXPIRED| In this training we first get conversation id from conversation ,channel session from slot ,channel session list from conversation and also get cc_user list from conversation. If there is no channel session list mean customer is left than we get agent state from slot and if agent state is requested that we respond back with a dispatcher action name **CANCEL_RESOURCE** with reasonCode **CANCELLED** and append events array with slot agent_state. After that if there is no cc_user mean all agent are left that we call a dispatcher action name **END_CONVERSATION** and return with type reset. ......................................  
**TASK_STATE_CHANGED**|  In this training we first check is there is a conversation or not if there is no conversation than do nothing else if there is a conversation then get taskDto from slots and get task_state from taskDto if task_state name is **CLOSED** and reasonCode is **FORCE_CLOSED** then get task_type from taskDto if task type direction is **DIRECT_CONFERENCE** and mode **QUEUE** then dispatcher a text "'Your chat has ended due to technical issues'.'Please come back later at a convenient time'" and set slot agent_state and return.  
**end_chat**|  In this training we first get conversation id and channel session from conversation if there is no channel session then just console info log that there is no channel session unable to post channel session expired. Otherwise dispatcher an action with name **CHANNEL_SESSION_EXPIRED** with channel session.  
`default`| In default training we just log info that default action called.  
  
## **How to add new training:**

  1. Add training event into the action_mapper.py class with his mapper class.
  2. Create training event class which run method with a parameter as we mentioned above.
  3. Write the functionality into that run method.
  4. Save the training file and it ready to use.


