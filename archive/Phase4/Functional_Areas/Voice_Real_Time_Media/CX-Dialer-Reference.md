---
title: "CX Dialer Reference"
summary: "Technical reference for the CX Dialer component — covering dialing flow, database schema, contact lifecycle states, campaign controls, and configuration parameters."
audience: [solution-admin, developer]
product-area: [voice, dialer]
doc-type: reference
difficulty: advanced
keywords: ["CX Dialer", "dialer configuration", "outbound dialer", "dialer database", "contact schema", "dialing flow", "IVR campaign", "agent campaign", "CALLS_PER_SECOND", "MAX_CONCURRENT_CALLS"]
aliases: ["dialer reference", "outbound dialer documentation", "CX Dialer config"]
last-updated: 2026-03-10
---

# CX Dialer Reference

The **CX Dialer** is the CX Voice component responsible for outbound dialing. It receives dialing requests via the CX Dialer APIs, enqueues them in its database, dials out following its internal dialing flow, and returns call results to the CX VoiceConnector. For agent-based campaigns, it also initiates agent reservation requests through the VoiceConnector to CX Routing.

## Dialing Flow

### Contact Selection

The Dialer periodically queries its database and selects contacts for dialing based on available Call Slots:

**If free Call Slots > number of active campaigns:**
- At least one contact is picked from each campaign.
- Preference is given to the campaign with the fewest contacts.
- Within a campaign, contacts are selected in FIFO order.
- Overall dialing order: smallest campaign first.

**If free Call Slots ≤ number of active campaigns:**
1. Within each campaign, contacts are ordered by `received_time` ascending.
2. The oldest contact per campaign is added to a candidate list.
3. The candidate list is sorted by `received_time` ascending.
4. The first X contacts from the list are selected, where X = free Call Slots.

### IVR Campaigns

1. The IVR number is taken from the contact entry if set; otherwise the default IVR from dialer configuration is used.
2. The dialer checks via EFSwitch ESL that the configured gateway is valid.
   - **Gateway valid**: EFSwitch originates the call to the customer number and plays the IVR.
   - **Gateway invalid**: Contact status is set to `failed`. No retry.
   - **Gateway down**: Contact status is reset to `pending` for retry on the next polling cycle.
3. Call Slots are decremented by 1.
4. When the call ends, the dialer receives a call-ended event from EFSwitch ESL and:
   - Stores the call result in the database (`status = ended`).
   - Sends the call result to the VoiceConnector for CCM delivery notification.
   - Increments Call Slots by 1.

### Agent Campaigns

1. Contact `status` is set to `agent_pending` and call information is posted to the VoiceConnector API.
2. Call Slots are decremented by 1.
3. The VoiceConnector returns an agent reservation result:
   - **No agent available**: Contact `status` is reset to `pending` for the next polling cycle.
   - **Agent reserved**: Dialer validates the gateway, then sends the originate command to EFSwitch to dial the customer and bridge the answered call to the reserved agent.
4. If the customer drops the call before the agent bridge completes, the dialer detects this via call variables in the call-ended event and sends an `END_CHAT` payload to the CCM to close the conversation and free the agent.
5. On call end: call result is stored, result is sent to VoiceConnector, and Call Slots are incremented.

## Contact Lifecycle States

| Status | Description |
|---|---|
| `pending` | Awaiting processing by the Dialer |
| `agent_pending` | Awaiting agent reservation from VoiceConnector |
| `dialed` | Sent to EFSwitch for dialing; waiting for result |
| `ended` | Call result received from EFSwitch |
| `stopped` | Stopped via the Campaign Stop API |
| `failed` | An error occurred (e.g., invalid gateway, EFSwitch connection failure) |

## Database Schema (`contacts` table)

| Field | Type | Description | Set By |
|---|---|---|---|
| `id` | VARCHAR(40) NOT NULL | Unique UUID for this contact/call | Campaign Manager |
| `customer_number` | VARCHAR(20) NOT NULL | Phone number to dial | Campaign Manager |
| `campaign_type` | VARCHAR(20) NOT NULL | `IVR` or `AGENT` | Campaign Manager |
| `gateway_id` | VARCHAR(40) NOT NULL | UUID of the EFSwitch gateway | Campaign Manager |
| `campaign_id` | VARCHAR(40) NOT NULL | Campaign identifier | Campaign Manager |
| `status` | VARCHAR(20) | Contact state (see lifecycle table above) | Dialer |
| `call_result` | VARCHAR(40) | EFSwitch call result (e.g., `NORMAL_CLEARING`, `USER_BUSY`) | Dialer |
| `received_time` | DateTime | When the contact was received by the Dialer | Dialer |
| `dial_time` | DateTime | When the contact was sent to EFSwitch or agent was requested | Dialer |
| `ivr` | VARCHAR(20) | Extension for the IVR to play on answer (IVR campaigns only) | Campaign Manager |
| `dialing_mode` | VARCHAR(20) | `PREDICTIVE`, `PREVIEW`, or `PROGRESSIVE`. Currently only `PROGRESSIVE` is supported. Required for AGENT campaigns. | Campaign Manager |
| `routing_mode` | VARCHAR(20) | `AGENT` or `QUEUE`. Currently only `QUEUE` is supported. Required for AGENT campaigns. | Campaign Manager |
| `queue_name` | VARCHAR(20) | Queue from which to pick an agent. Uses default queue if empty. | Campaign Manager |
| `resource_id` | VARCHAR(40) | Agent ID (if `routing_mode=AGENT`) or Queue ID (if `routing_mode=QUEUE`) | Campaign Manager |
| `priority` | Integer | Contact priority 1–10. Currently not in use. | Campaign Manager |

> **Note:** `campaign_contact_id`, `start_time`, `end_time`, `scheduling_metadata`, `tenant_metadata`, and `tenant_id` fields are present in the schema but are reserved for future versions.

## Data Lifetime and Stuck Contacts

There is no automatic expiry for contact records. A scheduled task runs every 10 minutes to resolve stuck contacts:

- If a contact's `status` is `dialed` or `agent_pending` and the time elapsed since `dial_time` exceeds `MAX_CALL_TIME`, the contact is reset to `pending` for re-processing.
- This handles cases where a database connection loss prevented the Dialer from receiving the EFSwitch call result.

## Campaign Control APIs

| Action | Description |
|---|---|
| **Start** | Sets all `stopped` contacts in a campaign back to `pending` |
| **Stop** | Sets all `pending` contacts in a campaign to `stopped` |
| **Purge** | Removes all `pending` contacts for a given campaign ID |

## Configuration Parameters

| Parameter | Type / Example | Description |
|---|---|---|
| `DB_URL` | IP address | URL of the Dialer database server |
| `DB_USERNAME` | Text | Database username |
| `DB_PASS` | Text | Database password |
| `DB_PORT` | Number (default: 5432) | Database port |
| `DB_NAME` | Text (e.g., `dialer`) | Database name |
| `DB_CONN_TIMEOUT` | Number in ms (default: 3000) | Max time for database connection |
| `ESL_IP` | IP address | IP of the EFSwitch ESL server |
| `ESL_PORT` | Number (default: 8021) | EFSwitch ESL port |
| `ESL_PASSWORD` | Text (default: `ClueCon`) | EFSwitch ESL password |
| `DEFAULT_IVR` | IVR number (e.g., `*9664`) | Default IVR extension for IVR campaigns without a specific IVR set |
| `SERVICE_IDENTIFIER` | Number (e.g., `1218`) | Service identifier for the VoiceConnector |
| `VOICE_CONNECTOR` | URL | VoiceConnector webhook (e.g., `http://192.168.1.2:4321`) |
| `ESL_CONNECT_DELAY` | Seconds (e.g., `60`) | Interval between EFSwitch ESL connection status checks |
| `CONTACT_RETRIEVAL_DELAY` | Seconds (e.g., `20`) | Interval between database polls for pending contacts |
| `CALLS_PER_SECOND` | Number | **Critical**: Maximum calls to generate per second. Must always be less than EFSwitch `sessions-per-second`. Exceeding this leaves contacts stuck in `dialed` state. |
| `MAX_CONCURRENT_CALLS` | Number | **Critical**: Maximum active calls at any time. Must always be less than the SIP trunk's maximum concurrent call limit. |
| `MAX_CALL_TIME` | Minutes | Max time a contact can remain in `dialed` or `agent_pending` before being reset to `pending`. Must be greater than Agent TTL in CX Channel Settings. |
| `LOG_LEVEL` | `INFO` or `DEBUG` | Log verbosity. Use `DEBUG` for troubleshooting. |

> **Important:** Setting `MAX_CONCURRENT_CALLS` or `CALLS_PER_SECOND` higher than your SIP trunk or EFSwitch limits will cause contacts to get stuck in `dialed` state. Stuck contacts can only be resolved by direct database intervention.

## Terminology

| Term | Definition |
|---|---|
| **Call Slots** | The number of contacts available for simultaneous dialing. Calculated as: `MAX_CONCURRENT_CALLS − (count of dialed + agent_pending contacts)` |
| **ESL** | EFSwitch Event Socket Layer — the interface the Dialer uses to send dial commands and receive call events from EFSwitch |
| **VoiceConnector** | The middleware component that bridges CX Core routing with CX Voice/Dialer |

## Known Limitations

- No way to switch between LIFO/FIFO/priority within a campaign.
- No priority differentiation when allocating call slots across campaigns.
- Cannot add more than 1 contact at a time to the database via API.
- If EFSwitch connection is lost, the call counter resets to zero as a precaution; total active calls may temporarily exceed `MAX_CONCURRENT_CALLS`.
- No expiry time for individual contacts.
- No detection of invalid IVR numbers — calls to invalid IVR destinations return `NORMAL_CLEARING` as the result.
- Multiple campaigns cannot share the same customer contact number.
- There is no limit on gateway-down retries for a given contact.

## Related Articles

- [Outbound Calls](Outbound-Calls.md)
- [CX Dialer Benchmarks](CX-Dialer-Benchmarks.md)
- [Miscellaneous Dialer Call Results](Miscellaneous-Dialer-Call-Results.md)
- [Managing Outbound Campaigns](../../Solution_Admin/Managing-Outbound-Campaigns.md)
- [Connected Calls Detail Report](Connected-Calls-Detail-Report.md)
