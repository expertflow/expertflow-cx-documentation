# CX Knowledgebase : Force Logout Agent

Enables a contact center supervisor to forcibly logout any agent, regardless of the agent’s current state, be it ** Ready**, **Not Ready** , **in a conversation** , **Consult** , **Conference** , or **Handling Multiple Conversations**.  
This is available for supervisors on the [**Available** **Agents Detail Dashboard**](Realtime-Reports-and-Dashboards_2529305.html#Active-Agents-Detail)**.**

Here are the details of the impact on agents and ongoing conversations in each state.

**Agent MRD States**| **Conversation states**| **Result**  
---|---|---  
Ready| -| 

  * The agent will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.

  
Not_Ready| -| 

  * The agent will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.

  
Active/Busy/Pending_Not_Ready| **Normal Chat**   
_Participants_ :

  1. Customer
  2. Agent-A

| 

  * All of his chats will be re-routed to the same queue with the Highest Priority (11). 
  * Agent-A will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.

  
Active/Busy/Pending_Not_Ready/Reserved| **Consult** _Participants_ :

  1. Customer
  2. Agent-A (Primary),
  3. Agent-B (Secondary)

| **Logout Request for Agent-A:**

  * **Agent-A** will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.
  * The system will automatically remove **Agent-B** from the conversation and reroute it to the same queue with the Highest Priority (11). 

**Logout Request for Agent-B:**

  * **Agent-B** will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.
  * **Agent-A** will get a notification that “Agent-B left the conversation”. NO IMPACT ON THE CURRENT CONVERSATION

  
Active/Busy/Pending_Not_Ready/Reserved| **Conference** _Participants_ :

  1. Customer
  2. Agent-A (Primary)
  3. Agent-B (Primary)

| 

  * Any of the agents whom the supervisor has sent the logout request will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR”.
  * The other agent will get a notification that the respective agent has left the conversation. NO IMPACT ON THE CURRENT CONVERSATION 

  
Active/Busy/Pending_Not_Ready/Reserved | **Conference** _Participants_ :

  1. Customer
  2. Agent-A
  3. Supervisor-X

| Logout request for Agent-A has been received and:  
**Supervisor X is in Silent-Monitoring Mode:**

  * Agent-A will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.
  * Supervisor X will be removed from the conversation.
  * The conversation will be re-routed to the same queue with the Highest Priority (11). 

**Supervisor X is in Whisper Mode:**

  * Agent-A will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.
  * Supervisor X will be removed from the conversation.
  * The conversation will be re-routed to the same queue with the Highest Priority (11). 

**Supervisor X is in Barge-in Mode:**

  * Agent-A will be logged out of the CX with reason code “FORCED_LOGOUT_BY_SUPERVISOR“.
  * The conversation will now be handled by Supervisor-X.


