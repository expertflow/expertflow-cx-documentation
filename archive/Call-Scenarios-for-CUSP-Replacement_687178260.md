# CX Knowledgebase : Call Scenarios for CUSP Replacement

The following scenarios shows the replacement of CUSP by CX SIP Proxy for inbound and outbound calls:

## Inbound Call

For inbound calls, the EF SIP Proxy, positioned after the Cisco Cube, directs SIP traffic to various destinations like CVPs, VBB, and CUCMs. It evaluates the status and load of each destination, ensuring calls are efficiently routed to the least loaded and operational component.

## Outbound Call

In outbound situations, the EF SIP Proxy is crucial in three scenarios: manual outbound, agent-based campaigns, and IVR-based campaigns. It effectively manages load balancing for Cisco Cube in these outbound processes.

### Manual Outbound

In manual outbound, the agent inititates the call using CUCM which messages SIP Proxy. The SIP Proxy server routes the call to CISCO CUBE to connect with the customer.

### Agent-based and IVR-based Campaigns

For Agent-based or IVR-based Campaigns, the Cisco dailer initiates a call at a scheduled time. The call lands on SIP Proxy server and is routed to CUBE for routing to either the:

  * CUCM(s) for the agent

  * VVP(s) where the IVR prompts are played for the customer



