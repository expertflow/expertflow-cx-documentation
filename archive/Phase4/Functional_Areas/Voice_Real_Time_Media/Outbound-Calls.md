---
title: "Outbound Calls"
summary: "How-to guide for placing manual outbound calls and running campaign-based outbound dialing in ExpertFlow CX, including flow steps, dialer modes, and agent actions."
audience: [agent, supervisor, solution-admin]
product-area: [voice, dialer]
doc-type: how-to
difficulty: intermediate
keywords: ["outbound calls", "outbound dialing", "manual outbound", "campaign dialing", "CX Dialer", "outbound campaign", "preview dialing", "progressive dialing"]
aliases: ["outbound call guide", "outbound voice", "campaign calls"]
last-updated: 2026-03-10
---

# Outbound Calls

ExpertFlow CX supports two types of outbound calling: **manual outbound calls** (agent-initiated, one-off calls to a customer number) and **campaign-based outbound** (automated dialing from a contact list managed by the CX Dialer). This guide covers both flows.

## Prerequisites

- CX Voice channel is configured with an outbound SIP trunk or CUCM route.
- For campaign-based outbound: a campaign is created and assigned to a queue.
- Agent is in a Ready state with a registered extension.

## Manual Outbound Calls

Manual outbound calls are placed by agents directly from the Agent Desk without a campaign.

### Steps

1. In the Agent Desk, open the **Dial** panel or the outbound call control.
2. Enter the customer's phone number in E.164 format (e.g., `+14155552671`).
3. Select the outbound route or trunk if multiple routes are configured.
4. Click **Call** (or press Enter).
5. The platform originates the call via SIP to the customer's number.
6. When the customer answers, the call connects to the agent's registered extension.
7. Handle the call using standard CTI controls (Hold, Transfer, DTMF).
8. When done, click **End Call** and complete wrap-up.

Manual outbound calls are logged in the Outbound Summary Report under the agent's name with a disposition of the session outcome.

## Campaign-Based Outbound (CX Dialer)

Campaign-based outbound uses the CX Dialer to automatically dial contacts from a list and connect answered calls to available agents.

### Dialing Modes

| Mode | Description | Best Use Case |
|---|---|---|
| **Preview** | Agent sees contact details before the call is placed and clicks to dial. | High-value outbound where agents need preparation time (e.g., collections, sales) |
| **Progressive** | Platform dials automatically when an agent becomes available; one call per agent at a time. | Moderate-volume outbound with consistent contact lists |
| **Predictive** | Platform dials multiple numbers simultaneously per available agent, factoring in answer rates and handle times. | High-volume outbound where maximising connect time is the priority |

### Campaign Outbound Flow

1. **Contact list is uploaded** to the campaign in the Outbound Campaign management interface.
2. **Dialer selects the next contact** from the list based on priority, retry rules, and dial schedule.
3. **Platform originates the call** to the contact's number via SIP.
4. The **IVR or answering machine detection (AMD)** layer runs:
   - If a human answers: call is connected to a ready agent.
   - If an answering machine is detected: the call is either abandoned or left with a pre-recorded message, depending on campaign configuration.
   - If no answer: the contact is flagged for retry according to the retry schedule.
5. **Agent receives the connected call** automatically (no manual dial required).
6. Agent handles the call, then wraps up with a wrap-up reason.
7. **Call result is recorded**: the Dialer logs the outcome (Connected, Not Answered, User Busy, etc.) against the contact record.

### Retry Rules

Contacts that do not connect are retried according to the campaign's retry configuration:
- Maximum number of retry attempts
- Minimum time between retries (e.g., retry after 1 hour)
- Time-of-day restrictions (e.g., no calls before 9am or after 8pm)
- Do Not Call (DNC) list enforcement

## Call Dispositions

After each outbound session, the result is recorded as one of the following dispositions:

| Disposition | Meaning |
|---|---|
| **Normal Clearing** | Clean disconnection at end of call |
| **Customer** | Session ended by the customer |
| **Agent** | Session ended by the agent |
| **User Busy** | Customer line was busy or not answered |
| **Network** | Customer-side network failure |
| **Decline** | Customer ended before responding |
| **Forced Closed** | Agent closed browser while task was active |
| **Unknown** | Unclassified session outcome |

## Reporting

- **[Connected Calls Detail Report](Connected-Calls-Detail-Report.md)**: Row-level record of each connected outbound call.
- **[Outbound Summary Report](../Performance_Insights_Data/Outbound-Summary-Report.md)**: Agent-level summary of outbound outcomes by date and channel.
- **[Campaign Performance Reports](../../Supervisor/Campaign-Performance-Reports.md)**: Campaign-level connect rates, attempts, and contact list progress.

## Related Articles

- [Inbound Calls](Inbound-Calls.md)
- [CX Dialer Reference](CX-Dialer-Reference.md)
- [CX Dialer Benchmarks](CX-Dialer-Benchmarks.md)
- [Managing Outbound Campaigns](../../Solution_Admin/Managing-Outbound-Campaigns.md)
- [Miscellaneous Dialer Call Results](Miscellaneous-Dialer-Call-Results.md)
- [CX Voice Limitations](CX-Voice-Limitations.md)
