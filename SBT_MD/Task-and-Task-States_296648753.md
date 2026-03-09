# CX Knowledgebase : Task and Task States

The Routing Engine creates a new task for a human agent for each new request routed to an agent. When the agent closes the request, the task state is also closed.

A Task can be in any one of the following states:

  * **Queued:** When the Task is enqueued in a precision queue

  * **Reserved:** When the task is offered to an agent and the agent is yet to accept it.

  * **Active:** When an agent has accepted and is active on the Task.

  * **Wrap-up:** When the agent is applying a wrap-up (yet to be implemented)

  * **Closed:** When the task is done and no further action is required.



