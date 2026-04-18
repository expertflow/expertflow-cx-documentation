---
title: "Miscellaneous Dialer Call Results"
summary: "Reference tables for outbound call result codes across CCX, CCE, and EFSwitch (FreeSWITCH), used for interpreting CX Dialer campaign outcomes."

product-area: [voice, dialer]
doc-type: reference
difficulty: advanced
keywords: ["dialer call results", "call result codes", "CCX call codes", "CCE call codes", "FreeSWITCH hangup codes", "EFSwitch call results", "outbound codes", "NORMAL_CLEARING", "USER_BUSY"]
aliases: ["call result codes", "dialer disposition codes", "FreeSWITCH hangup causes"]
last-updated: 2026-03-10
---

# Miscellaneous Dialer Call Results

This reference lists the call result codes used across the three telephony systems that CX Dialer integrates with: **Cisco CCX**, **Cisco CCE**, and **EFSwitch (FreeSWITCH)**. Use this reference when interpreting raw call results stored in the Dialer database's `call_result` field or when diagnosing unexpected campaign outcomes.

## Cisco CCX Call Result Codes

These codes are used when CX Dialer integrates with Cisco Unified Contact Center Express (UCCX).

| Code | Numeric Value | Description |
|---|---|---|
| `DIAL_TIMEOUT` | 0 | Call attempt timed out before connecting |
| `INVALID_NUMBER` | 4 | The dialled number is invalid |
| `CALL_REJECTED` | 5 | Call was rejected by the remote party |
| `WRONG_NUMBER` | 6 | Connected to a different number than intended |
| `WRONG_PERSON` | 7 | Connected to a person other than the intended contact |
| `CALLBACK_REQUESTED` | 8 | Customer requested a callback |
| `AGENT_REJECTED` | 9 | Agent rejected the call |
| `AGENT_CLOSED` | 10 | Agent closed the call |
| `RING_NO_ANSWER` | 12 | Number rang but was not answered |
| `CALLBACK_FAILED` | 13 | Callback attempt failed |
| `CALLBACK_MISSED` | 14 | Callback was missed |
| `CALL_ABANDONED` | 16 | Call was abandoned |
| `GATEWAY_ERROR` | 17 | Error occurred at the gateway |
| `CUSTOMER_ABANDONED` | 18 | Customer abandoned before connecting to an agent |

**Reference**: [Cisco UCCX Database Schema Guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_11_6/reference/guide/UCCX_BK_CF9FAD2A_00_cisco-unified-ccx-database-schema/UCCX_BK_CF9FAD2A_00_cisco-unified-ccx-database-schema_chapter_00.md)

## Cisco CCE Call Result Codes

These codes are used when CX Dialer integrates with Cisco Unified Contact Center Enterprise (UCCE).

| Code | Numeric Value | Description |
|---|---|---|
| `DIAL_TIMEOUT` | 0 | Call attempt timed out |
| `DIALING_ERROR` | 2 | Error during dialing |
| `UNALLOCATED_NUMBER` | 3 | Number is unallocated |
| `NO_NETWORK_RESPONSE` | 4 | No response from the network |
| `OPERATOR_INTERCEPT` | 5 | Call intercepted by an operator |
| `NO_TONE` | 6 | No dial tone detected |
| `INVALID_NUMBER` | 7 | The dialled number is invalid |
| `DIALING_STOPPED` | 13 | Dialing was stopped |
| `CALLBACK_REQUESTED` | 14 | Customer requested a callback |
| `ANSWERING_MACHINE_CALLBACK` | 15 | Answering machine detected; callback scheduled |
| `NO_AGENT_AVAILABLE` | 16 | No agent was available to take the call |
| `CALLBACK_RESERVE_FAIL` | 17 | Agent reservation for callback failed |
| `AGENT_REJECTED` | 18 | Agent rejected the call |
| `AGENT_REJECTED_CLOSE` | 19 | Agent rejected and closed the call |
| `IVR_ABANDON` | 20 | Customer abandoned during IVR |
| `CALL_DROPPED` | 21 | Call was dropped |
| `TDM_SWITCH` | 22 | TDM switch event |
| `WRONG_NUMBER` | 23 | Wrong number reached |
| `WRONG_PERSON` | 24 | Wrong person answered |
| `NOT_ATTEMPTED` | 25 | Contact was not attempted |
| `DO_NOT_CALL` | 26 | Contact is on the Do Not Call list |
| `RING_DISCONNECT` | 27 | Call disconnected during ringing |
| `DEAD_AIR` | 28 | Dead air detected |
| `NOT_SUPPORTED` | 29 | Operation not supported |
| `NOT_AUTHORIZED` | 30 | Not authorised |
| `INVALID_SIP_MESSAGE` | 31 | Invalid SIP message received |
| `CM_CONNECTION_LOST` | 32 | Connection to Call Manager was lost |
| `AGENT_TIMEOUT` | 33 | Agent failed to respond within the timeout |

**Reference**: [Cisco UCCE Outbound Option Guide](https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_11_6_1/User/Guide/b_ucce_outbound_option_Release_11_6_1/b_ucce_outbound_option_Release_11_6_1_appendix_01001.pdf)

## EFSwitch (FreeSWITCH) Hangup Cause Codes

When CX Dialer uses EFSwitch (the FreeSWITCH-based media server), the `call_result` field in the Dialer database contains EFSwitch hangup cause codes rather than the CCX/CCE numeric codes above.

Common EFSwitch hangup causes relevant to outbound dialing include:

| Cause Code | Meaning |
|---|---|
| `NORMAL_CLEARING` | Call completed successfully and ended cleanly |
| `USER_BUSY` | Customer's line was busy |
| `NO_USER_RESPONSE` | Customer did not answer |
| `NO_ANSWER` | Call rang with no answer |
| `CALL_REJECTED` | Remote party rejected the call |
| `UNALLOCATED_NUMBER` | Number is not in service |
| `SUBSCRIBER_ABSENT` | Customer is not reachable |

**Reference**: [FreeSWITCH Hangup Cause Code Table](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Troubleshooting-Debugging/Hangup-Cause-Code-Table_3964945/) (SignalWire developer documentation)

## Usage Notes

- In standard CX Dialer deployments with EFSwitch, the `call_result` field in the `contacts` table will contain EFSwitch hangup cause strings (e.g., `NORMAL_CLEARING`, `USER_BUSY`).
- CCX and CCE codes apply only in hybrid deployments where CX Dialer feeds call results back to a Cisco contact center system.
- `NORMAL_CLEARING` in EFSwitch does not necessarily mean the customer answered — it means the call leg ended cleanly. For IVR campaigns, a call to an invalid IVR number will also return `NORMAL_CLEARING`. See [CX Dialer Reference](CX-Dialer-Reference.md#known-limitations).

## Related Articles

- [CX Dialer Reference](CX-Dialer-Reference.md)
- [Outbound Calls](Outbound-Calls.md)
- [Connected Calls Detail Report](Connected-Calls-Detail-Report.md)
- [Outbound Summary Report](../Reporting_and_Analytics/Outbound-Summary-Report.md)
