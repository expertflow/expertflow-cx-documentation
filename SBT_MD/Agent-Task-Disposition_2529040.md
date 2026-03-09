# CX Knowledgebase : Agent Task Disposition

  


**Task Disposition**| **Description**  
---|---  
RONA| When the system reserves an agent for a conversation but he/she does not accept the request within the preconfigured RONA timeout , the task is closed with the disposition RONA (Ringing-On-No-Reply). The request goes back to the queue to be routed to another available agent.  
DONE| Whenever the agent leaves the conversation, the agent's task will be closed with the disposition 'DONE'. In case, if the customer is still there while the agent leaves, BOT will decide whether the request has to be enqueued again or closed.   
AGENT_LOGOUT| The task is closed with the disposition 'AGENT_LOGOUT' when the Agent logs out and there is an active task for that agent.In this case, the conversation will go back to the queue. Another task will be created for the conversation and enqueued to find an agent. The system will find an agent within the request TTL.   
  
CANCELLED| When an agent is reserved for a customer and the customer leaves before the agent joins the conversation, then the task is closed with the disposition 'CANCELLED'.  
TRANSFERRED| When the agent transfers the chat to another agent using the "Transfer" feature, the task of the requesting agent is closed with the disposition 'TRANSFERRED'.   
NO_AGENT_AVAILABLE| When a task is ENQUEUED but no agent is available (READY or ACTIVE), the task is closed with the disposition 'NO_AGENT_AVAILABLE'.  
FORCE_CLOSED| Making a call to the Queue Flush API flushes all tasks in the queue. In that case, the disposition of the closed tasks is set to 'FORCE_CLOSED'.  
  
  

