# CX Knowledgebase : Outbound Calls

Enable agents to make outbound calls and run automated campaigns to reach customers proactively.

## Overview

Outbound Calls in Expertflow CX lets your contact center make calls to customers rather than just receiving them. This includes manual outbound calls made by agents and automated campaigns that dial customers based on contact lists.

This page covers how outbound calling works and what you can configure.

## Types of Outbound Calls

### Manual Outbound

Agents dial customer numbers directly from Agent Desk. Use this for:

  * Follow-up calls after a support interaction

  * Returning missed calls

  * One-off calls to specific customers




No campaign setup required — agents just enter the number and dial.

### Campaign-Based Outbound

Automated dialing from a contact list. Use this for:

  * Sales outreach

  * Appointment reminders

  * Payment collection

  * Surveys and feedback

  * Announcements and notifications




Campaigns are managed through **Campaign Manager**.

## How Outbound Calling Works

### Manual Outbound Flow

  1. Agent clicks dial in **Agent Desk** and enters customer number

  2. **Media Server** places the call via SIP trunk

  3. Customer answers

  4. Agent and customer are bridged

  5. After the call, agent sets wrap-up code




### Campaign Outbound Flow

  1. Admin creates campaign in **Campaign Manager** with contact list

  2. Campaign starts at scheduled time

  3. **Dialer** picks contacts from the list and places calls via Media Server

  4. For agent-based campaigns: answered calls are routed to available agents

  5. For IVR campaigns: answered calls are connected to an IVR flow

  6. Call outcomes are logged for reporting




## What You Can Configure

### Manual Outbound

  * **Outbound caller ID** — Set the number displayed to customers

  * **Wrap-up codes** — Define call outcome categories




Configured in Unified Admin.

### Campaigns

  * **Contact lists** — Upload or integrate customer contact data

  * **Dialing mode** — Choose how calls are placed:

    * **Preview** — Agent sees contact info, then decides to dial

    * **Progressive** — System dials automatically when agent becomes available

  * **Campaign schedule** — Set start time, end time, and days of operation

  * **Retry rules** — Define how to handle unanswered calls or busy signals

  * **Call outcomes** — Track dispositions (answered, no answer, voicemail, etc.)




Configured in Campaign Manager.

### IVR Campaigns

  * **IVR flow** — Define the automated message or interaction

  * **Contact list** — Upload numbers to dial

  * **Schedule** — Set when the campaign runs




IVR flows are configured on Media Server. Campaign settings are in Campaign Manager.

## Configuration Checklist

Step| Where  
---|---  
Enable outbound dialing for agents| Unified Admin  
Set outbound caller ID| Unified Admin  
Define wrap-up codes| Unified Admin  
Create contact list| Campaign Manager  
Create campaign (preview/progressive)| Campaign Manager  
Build IVR flow (for IVR campaigns)| Media Server  
Schedule and launch campaign| Campaign Manager  
  
* * *

## Where to Go Next

Topic| Description  
---|---  
Campaign Manager Guide| Detailed guide to creating and managing campaigns  
Contact List Management| How to upload and manage contact lists  
Dialer Configuration| Configure dialing modes and retry rules  
Agent Guide| How agents handle outbound calls  
Inbound Calls| Configure inbound routing and IVR  
  
* * *

## Current Limitations

For the full list and details, see **Limitations**.
