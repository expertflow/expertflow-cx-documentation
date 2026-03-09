# CX Knowledgebase : Task Priority

Priority is an attribute assigned to any task to route that task to an agent in an expedited manner. By default, all tasks in the system have a priority of 1 and are served on a FIFO (First In, First Out) basis.

## Priority Range

The priority range in the system is from 1 to 11. Priority 11 is reserved exclusively for RONA cases. For all other tasks, the priority can be set from 1 to 10.

## How to set a Task Priority

  1. **From Controller**




We can set the task priority when calling the RE API to find an agent. Additionally, we can set the priority by assigning labels to customers.
[code] 
    {
        "queue": "62dff614d1f0c94191c244d2",
        "requestSession": null,
        "channelSessions": [],
        "type": null,
        "priority": 1
    }
[/code]

This is the payload required by the assign-resource API of RE. The Conversation Manager calls this API to assign an agent to a customer based on the action event FIND_AGENT. When the controller passes this FIND_AGENT event to the Conversation Manager, we can also pass the desired priority.

  2. **By assigning a label to customer**




We can also set the priority of a chat by assigning a label to the customer. For more details, please refer to this [document](https://expertflow-docs.atlassian.net/l/cp/gPTP0Npz).
