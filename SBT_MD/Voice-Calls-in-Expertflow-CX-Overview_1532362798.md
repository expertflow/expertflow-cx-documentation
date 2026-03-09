# CX Knowledgebase : Voice Calls in Expertflow CX Overview

# Voice Calls

Handle inbound and outbound customer calls with skills-based routing, IVR self-service, and full agent call controls — all within Expertflow CX.

## Overview

Voice Calls in Expertflow CX lets your contact center handle customer phone calls over PSTN or SIP. Customers dial from landlines or mobile phones, and agents manage the interaction in Agent Desk. It covers the full call lifecycle—from IVR self-service and routing to live agent handling, transfers, conferencing, and wrap-up.

## What You Can Configure

### Inbound Calls

  * Route incoming calls based on skills, availability, and business rules

  * Configure IVR menus (traditional or conversational AI)

  * Manage queues with hold music, announcements, and callbacks

  * Enable transfers between agents, queues, or external numbers




### Outbound Calls

  * Enable manual outbound dialing from Agent Desk

  * Run campaigns with preview or progressive dialing

  * Configure IVR-based campaigns for announcements, surveys, or reminders

  * Track call outcomes and dispositions




For agent and supervisor capabilities, see the **Agent Guide** and **Supervisor Guide**.

## Before You Begin

  * Expertflow CX deployed

  * SIP trunk configured for PSTN access

  * Media Server deployed

  * Voice channel configured in Unified Admin

  * Agent extensions created




* * *

## How It Works

  1. Call arrives via SIP trunk to the **Media Server**

  2. Media Server answers and runs IVR flow

  3. If agent needed, system requests one from **CX Routing**

  4. CX Routing finds available agent with right skills

  5. Agent receives alert in **Agent Desk** and answers

  6. Media Server bridges customer and agent audio

  7. After call ends, agent completes wrap-up




All call activity, recordings, and metadata are stored in **CX Activities**.

* * *

## Where to Go Next

Topic| Description  
---|---  
Inbound Calls| Understand inbound routing, IVR, and queueing  
Outbound Calls| Configure outbound calling and campaigns  
Agent Guide| How agents handle calls in Agent Desk  
Supervisor Guide| Real-time monitoring and controls for supervisors  
Infrastructure| Learn about Media Server and SIP Proxy deployment  
  
* * *

## Current Limitations

For the full list and details, see **Limitations**.
