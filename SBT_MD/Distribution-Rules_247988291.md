# CX Knowledgebase : Distribution Rules

Addresses with distribution rules of routing such as queues to agent mapping, multi-steps per queue, agent reservation, priority routing, queue priority (In progress)

  * Queues To Agent Mapping
  * Multi Steps per Queue
  * Agent Reservation
  * Priority Routing
  * Multi-Queue Priority



## Queues To Agent Mapping

Queues to Agents are mapped based on the attributes assigned to the agents. Within each queue, we can create multiple steps. Each step has an associated criteria and a timeout period, which is used to find agents that meet the criteria.

All agents that fulfill the criteria specified by all the steps fall within that queue, or in other words, are mapped to that queue.

![image-20240729-120228.png](attachments/247988291/412483635.png?width=1202)

## Multi Steps per Queue

As discussed above, we can have multiple steps associated with each queue. The purpose of having multiple steps within a queue is to ensure that the chat is assigned to an agent as soon as possible. To understand this more clearly, we need to first understand how the process of finding an agent works by following steps mentioned below:

### Step Timer Initialization

Once the chat is enqueued, a step timer is started based on the timeout value associated with the first step.

### Agent Search in First Step: 

The Routing Engine (RE) will try to find an agent that fulfills the criteria mentioned in the first step.

### Move to the Next Step 

The RE will move to the next step if the step timer expires and no suitable agent is found. The timer for the second step will be started, and the system will now iterate from the first step to the second step, trying to reserve an agent available for any of these steps.

### Increment to Subsequent Steps

If the timer for the second step expires, the RE will move to the third step. It will first look for agents associated with the first step, then the second step, and finally the third step.

### Continual Process

This process continues, with the system iterating through all the steps in sequence. The goal is to find the best available agent who meets the criteria for the highest priority step. If no such agent is available, the system will attempt to find an agent to fulfill the criteria for the subsequent steps.

The whole purpose is to try and find the best available agent that fulfills the topmost step criteria. If that's not possible, the system will at least find an agent that fulfills the lower-step criteria.

## Agent Reservation

The agent reservation within a single step follows this process:

  1. **Sorting Agents** : All agents are sorted based on the longest availability.

  2. **Validation** : Agents are filtered to ensure they are available on the MRD and are not already active in the conversation for which this task is created.

  3. **Agent Selection** : From the sorted and validated agents, the one with the least active tasks will be reserved for this new task.




By following the above reservation process, it is ensured that the agents are assigned chats evenly within a single step.

## Priority Routing

Priority routing is a feature of the system that allows us to route a chat with higher priority compared to normal priority. This is achieved by assigning a specific label to a customer. Each label has a priority value associated with it, which is configured in the controller. For more details, please refer to this [document](https://expertflow-docs.atlassian.net/l/cp/gPTP0Npz).

## Multi-Queue Priority 

This implementation allows the system to define priority for each queue (1-10 with 1 being the lowest, and 10 being the highest). The system routes high-priority tasks to the agents first before routing them to other queues. 

Chats are distributed to agents in the following order:

  * **Step 1:** The system considers the **Queue-Priority** first. Tasks within high-priority queues are routed first. (Within a single queue, task priority will be considered before FIFO).

  * **Step 2:** If multiple or all queues have the same priority, The system considers the **Task Priority** within all queues. Task with the highest priority (regardless of the queue) will be routed first, then the second highest priority task will be routed and so on.

  * **Third Step:** If both queue and task priority are the same, RE considers the **longest waiting task** to be routed in that order. 




**Limitation:**

When an agent is in the**RESERVED** state (due to a chat request), he will not receive requests from other queues during that time. Upon accepting the chat, the agent continues to miss requests from any other queue because only the queue associated with the accepted chat request is invoked. Since other requests are on different queues, those queues are not triggered.  
This behavior will only occur if there is a single agent available and that agent is in the **RESERVED** state. If a request comes in while the agent is reserved, that request will not be routed to that agent on accepting the reserved chat. The request will only be routed if the agent manually changes the MRD associated with that queue or if another agent becomes available.

  

