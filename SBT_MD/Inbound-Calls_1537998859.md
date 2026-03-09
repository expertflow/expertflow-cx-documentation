# CX Knowledgebase : Inbound Calls

Route incoming customer calls to the right agents using skills-based routing, IVR self-service, and queue management.  
  
## Overview

Inbound Calls in Expertflow CX handles calls from customers who dial your contact center number. Calls arrive via SIP trunk, pass through an IVR for self-service or information gathering, and then route to an available agent based on skills and business rules.

This page covers how inbound routing works and what you can configure.

## How Inbound Routing Works

  1. Customer dials your contact center number

  2. Call arrives via SIP trunk to the **Media Server**

  3. Media Server runs the **IVR flow** (greetings, menus, data collection)

  4. IVR determines the routing destination (queue, skill, or specific agent)

  5. **CX Routing** finds an available agent matching the required skills

  6. Agent receives the call alert in **Agent Desk**

  7. Agent answers and is bridged with the customer

  8. After the call, agent sets wrap-up code and becomes available




## What You Can Configure

### IVR

The Interactive Voice Response system greets callers and guides them before reaching an agent.

  * **Welcome prompts** — Greet callers with custom messages

  * **Menu options** — Let callers select options via keypress (DTMF)

  * **Conversational IVR** — Use AI-powered speech recognition for natural language input

  * **Data collection** — Gather customer information (account number, reason for call)

  * **Self-service** — Resolve simple queries without agent involvement




IVR flows are configured on the Media Server.

### Queues

Queues hold calls until an agent becomes available.

  * **Queue assignment** — Assign calls to queues based on IVR selection or routing rules

  * **Hold treatment** — Configure hold music and periodic announcements

  * **Queue priority** — Prioritize certain calls (e.g., VIP customers)

  * **Service levels** — Define target answer times for reporting




Queues are configured in Unified Admin.

### Skills-Based Routing

Route calls to agents based on their skills and proficiency.

  * **Skill definition** — Define skills (e.g., language, product expertise, support tier)

  * **Agent skill assignment** — Assign skills and proficiency levels to agents

  * **Routing rules** — Match call requirements to agent skills

  * **Fallback routing** — Define overflow behavior if no skilled agent is available




Skills and routing are configured in Unified Admin under CX Routing.

### Transfers

Agents can transfer calls during or after connecting with the customer.

  * **Direct transfer** — Transfer directly to another agent or queue

  * **Consult transfer** — Speak with the target agent before transferring

  * **Queue transfer** — Transfer to a different queue

  * **External transfer** — Transfer to an external phone number




Transfer options are available in Agent Desk. Configuration for external transfers is in Unified Admin.

* * *

## Configuration Checklist

Step| Where  
---|---  
Create IVR flow with prompts and menus| Media Server  
Define queues and hold treatment| Unified Admin  
Define skills| Unified Admin → CX Routing  
Assign skills to agents| Unified Admin → CX Routing  
Configure routing rules| Unified Admin → CX Routing  
Set up voice channel with inbound number| Unified Admin  
  
* * *

## Where to Go Next

Topic| Description  
---|---  
IVR Configuration| Step-by-step guide to building IVR flows  
Queue Configuration| How to set up queues in Unified Admin  
Skills-Based Routing| Detailed guide to configuring skills and routing rules  
Agent Guide| How agents handle inbound calls  
Outbound Calls| Configure outbound calling and campaigns  
  
* * *

## Current Limitations

For the full list and details, see **Limitations**.
