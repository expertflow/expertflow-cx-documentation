# CX Knowledgebase : Agent States

### Change Agent State  
  
After getting logged in, agents are set to the **Not Ready** state by default. Upon changing their state to **Ready,** they can receive requests from the assigned Channel Categories (Channel Categories). 

There are two levels of state changes in the Agent Desk:

  * Global state change - global states are the high-level states that serve as the basis for setting channel category (Channel Category) states. The state change on this level affects state changes on all assigned channel categories (Channel Categories).

  * Channel Category (Channel Category) state change - Channel Category (Channel Category) states are specifically for a particular Channel Category (Channel Category). Once agents set themselves as Ready, or Not Ready on a specified channel category (Channel Category), they make themselves available or not available to take requests from that particular channel category (Channel Category).




The agent state only matters for PUSH Mode Routing. An agent can cater to PULL Mode requests in any state if he/she is logged in and has subscribed to the correct List

In this section, we will explore the various global state changes that the agent can be in at any time.

After logging in, an agent can go through the following state transitions:

**From**| **To**| **Description**  
---|---|---  
LOGOUT| LOGIN | `LOGIN `is a transient state and transitions to` NOT_READY` automatically after the agent logs in. A transient state is a state in which agents stay shortly (typically for a few secs/mins) and transition to a more permanent state.  
LOGIN| NOT_READY| Once an agent switches its state to `NOT_READY, `the switches of all Channel Categories are turned off.  When an agent is in` a NOT_READY` state, the Routing Engine doesn’t route any new requests to this agent.The top agent-state dropdown turns grey and displays the Not Ready reason of the agent.No reason code is assigned when the agent transitions to the Not Ready state immediately after the LOGIN state.  
NOT_READY| READY| Once an agent is ready, new requests for a Channel Category may be routed to the agent depending upon the Agent's Channel Category State. See [ _Channel Category State Transitions_](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/2531294/Agent+States#Change-MRD-State) in the table below.  
READY| NOT_READY| The Agent can specify one of the not-ready reason codes, upon changing their state to NOT_READY. All Not-ready reasons are currently defined by the system administrator in Unified Admin.   
NOT_READY/READY| LOGOUT| When logs out, the system waits for the Agent_Disconnect timer timeout to expire. Upon expiry, all the current tasks of the agent are re-routed to another available agent and the agent is logged out. Agents can also log out while in the Ready state as well as when in the Not Ready state.   
  
| unknown| If the agent state is `unknown`, then it means that the state is not determined(unknown). This scenario is unlikely to happen.  
  
Agents can also see the real-time timer going on to count how much time the agent remains in a state (Ready, Not Ready). This state timer is reset every time the global state is changed.

![](attachments/2531294/2550070.png?width=400)

### Change Channel Category State

In addition to the state changes as discussed above, agents can also manage their state in individual Channel Categories, such as going **Ready** for a Chat Channel Category and Not Ready for the Voice call Channel Category.

An agent can go through the following Channel Category state transitions:

**From**| **To**| **Description**| **Routable (if a task of this Channel Category can be routed in this state)**  
---|---|---|---  
\- | LOGIN| Login is the agent's state immediately after signing in. No tasks are assigned to the agent while in this state. The LOGIN state is a transitive state; LOGIN triggers a change that results in a new state, i.e. NOT_READY.| None  
LOGIN| NOT_READY| By default, agents are set to NOT_READY after logging in. Agents won't be assigned any new tasks in this state. In this state, the toggle button of the Channel Category state turns **grey** and remains `OFF`. | ![\(error\)](images/icons/emoticons/error.png)  
NOT_READY| READY| In this state, agents are available to take new requests for a particular Channel Category. The toggle switch of the Channel Category state goes **green** and turns `ON`. | ![\(tick\)](images/icons/emoticons/check.png)  
READY| ACTIVE| When the agent is working on at least one task in this Channel Category. This is a system-defined state. Agents automatically transition to this state as soon as they accept a task on the specified Channel Category.The toggle switch of the Channel Category state goes **orange** and remains `ON`.| ![\(tick\)](images/icons/emoticons/check.png)  
ACTIVE| BUSY| When an agent has already been offered the maximum number of tasks in this Channel Category as per the specified "Max Tasks" limit defined by the administrator. Agents automatically transition to this state as soon as their limit is reached for the specified Channel Category. When set to BUSY, agents will receive no new tasks from the particular Channel Category. However, this setting is available from the Channel Category settings in Unified Admin. Your system administrator defines the max task limit.The toggle switch of the Channel Category state goes **red** and remains `ON`. | ![\(error\)](images/icons/emoticons/error.png)  
ACTIVE| PENDING_NOT_READY| If and when the agent switches off an Channel Category while being `ACTIVE` on at least one task in this Channel Category, it automatically transitions to this state.This is a transient state while the active tasks of the agent are cleared from the Agent's interface. Once cleared, the agent's Channel Category has switched off automatically.The toggle switch of the Channel Category state goes **purple** and turns `OFF`.| ![\(error\)](images/icons/emoticons/error.png)  
BUSY| PENDING_NOT_READY| If and when the agent switches off this Channel Category while being `BUSY` handling tasks on this Channel Category, it automatically transitions to this state. | ![\(error\)](images/icons/emoticons/error.png)  
PENDING_NOT_READY| NOT_READY| The agent state will be transited to NOT_READY automatically after all the active tasks are cleared from the agent when the agent is in the PENDING_NOT_READY state.| ![\(error\)](images/icons/emoticons/error.png)  
ACTIVE| READY| If the last task for an Agent Channel Category is closed, the agent automatically transitions to `READY.`| ![\(tick\)](images/icons/emoticons/check.png)  
READY| NOT_READY| Agents make themselves `NOT_READY` for a reason (optionally selected) if they don't want to receive any new tasks. | ![\(error\)](images/icons/emoticons/error.png)  
  
| unknown| In a failover scenario, an agent state may be set to UNKNOWN. The agent can switch to READY or NOT_READY from an UNKNOWN state.| ![\(error\)](images/icons/emoticons/error.png)  
  
The state timer does not apply to the Channel Category state change. It is only applicable to global state changes.

![MRD state change.png](attachments/2531294/66650136.png?width=633)
