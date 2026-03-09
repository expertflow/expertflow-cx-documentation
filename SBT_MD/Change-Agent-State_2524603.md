# CX Knowledgebase : Change Agent State

Enables agents to change their states globally and MRD-wise.After getting logged in, agents are in a **Not-Ready** state by default. They need to change their state to **Ready** to receive requests from the assigned MRDs. There are two levels of state changes in the AgentDesk.  
  
**Global state change** \- Global states are the high-level states that serve as the basis for setting MRD states. The state change on this level affects state changes on all assigned MRDs.

In this section, we will explore the various global state changes that the agent can be in at any time.

After logging in, an agent can go through the following state transitions:

**From**| **To**| **Description**  
---|---|---  
LOGOUT| LOGIN | `LOGIN `is a transient state and transitions to` NOT_READY` automatically after the agent logs in. A transient state is a state in which agents stay shortly (typically for a few seconds/mins) and transition to a more permanent state.  
LOGIN| NOT_READY| Once an agent switches its state to `NOT_READY, `the switches of all MRDs is turned off.  When an agent is in` a NOT_READY` state, the Routing Engine doesn’t route any new requests to this agent.The top agent-state dropdown turns grey and displays the Not Ready reason of the agent.No reason code is assigned when the agent transitions to the Not Ready state immediately after the LOGIN state.  
NOT_READY| READY| Once an agent is ready, new requests for an MRD may be routed to the agent depending on the Agent's MRD State. See ** _MRD State Transitions_** in the table below.  
READY| NOT_READY| The Agent can specify one of the not-ready reason codes, upon changing their state to NOT_READY. All Not-ready reasons are currently defined by the system administrator in Unified Admin.   
NOT_READY| LOGOUT| On logging out, the system waits for the Agent_Disconnect timer timeout to expire. Upon expiry, all the current tasks of the agent are re-routed to another available agent, and the agent is logged out. Agents can also log out while in the Ready state as well as when in the Not Ready state.   
  
| unknown| If the agent state is `unknown`, then it means that the state is not determined(unknown). This scenario is unlikely to happen.  
  
Agents can also see the real-time timer going on to count how much time the agent remains in a state (Ready, Not Ready). This state timer is reset every time the global state is changed.

![global state change-1.png](attachments/2524603/129892489.png?width=800)

### Change MRD State

MRD states are specifically for a particular MRD. Once agents set themselves as Ready, or Not Ready on a specified MRD, they make themselves available or not available to take requests from that particular MRD.

In addition to the state changes as discussed above, agents can also manage their state in individual MRDs such as going Ready for a Chat MRD and Not Ready for the Voice call MRD.

An agent can go through the following MRD state transitions:

### Note

The state timer does not apply to the MRD state change. It is only applicable to global state changes.

![mrd-state-change-blur.png](attachments/2524603/129695957.png?width=800)

For voice, agents can change the present state (Voice MRD) as available (Ready), not-available ( Not Ready) to receive inbound and campaign outbound calls.

  


  

