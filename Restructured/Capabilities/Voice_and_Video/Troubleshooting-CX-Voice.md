---
title: "Troubleshooting CX Voice"
summary: "How-to guide for diagnosing and resolving common CX Voice issues across inbound call routing, queue transfer, IVR-based outbound, progressive agent-based outbound, and Voice Connector/Dialer connectivity."

product-area: [voice]
doc-type: how-to
difficulty: advanced
keywords: ["CX Voice troubleshooting", "voice troubleshooting", "inbound call not routing", "IVR troubleshooting", "dialer troubleshooting", "ESL connection", "voice connector logs", "RONA troubleshooting"]
aliases: ["voice troubleshooting guide", "CX Voice debug", "inbound call diagnosis"]
last-updated: 2026-03-10
---

# Troubleshooting CX Voice

This guide covers common CX Voice issues across inbound routing, queue transfers, outbound IVR campaigns, and agent-based outbound campaigns. Work through each section methodically — most issues are resolved by cross-checking logs across the Voice Connector, Media Server, and Agent Desk.

## Inbound Call Scenarios

### Customer Selects Agent Option from IVR but Waits Indefinitely

**Check Agent Desk first:**
1. Confirm an agent is logged in and their **CX Voice MRD** is in **Ready** state.
2. Check the Agent Desk browser console (F12) for SIP-related errors.

**Check Voice Connector logs:**
1. Open Voice Connector logs.
2. Confirm `RECEIVED AGENT RESERVATION REQUEST` is logged with correct values:
   - `eslHost`, `callUid`, `queueType`, `callingNumber`, `priority`, `queue`, `callSipId`, `direction`, `serviceIdentifier`
3. In the `ASSIGN_RESOURCE_REQUESTED` payload, verify:
   - `ServiceIdentifier` matches the dialled number and the serviceIdentifier in Unified Admin CX Voice channel settings.
   - `customerChannelIdentifier` equals the calling number.
   - Queue info is correct (empty queue name means the default queue is used — verify the queue assigned to agents in Unified Admin and in the Media Server `cx_env` file).
   - `direction` is `INBOUND` or `DIRECT TRANSFER` as expected.
4. If `RECEIVED AGENT RESERVATION REQUEST` is **not** logged:
   - Verify that `VC IP/Port` in the Media Server `cx_env` file is correct.
   - Verify that the VC port is unblocked on the VC server.
5. Check that the CCM API IP/Port or FQDN is correct.
6. Confirm CCM returns `200 OK` and `CHANNEL_SESSION_STARTED` after the reservation request.
7. If no agent is reserved even though the CCM responds: toggle the agent's CX Voice MRD off and back on.
8. If you cannot toggle: hang up the call, ask Support to clear the conversation via the Conversation Manager API, then retry.
9. Verify the agent assigned to the call has the same queue assigned as expected in Unified Admin.
10. If `AGENT_RESERVED` payload returns `[agentExtension] not found`: assign a Media Server extension to that agent in Keycloak and have them log back in. See [Adding Agent Extensions for CX Voice](Adding-Agent-Extensions-CX-Voice.md).
11. If `AGENT_RESERVED` returns `[uuid] not found`: this indicates a version mismatch between EF CX and the Voice Connector. Contact Support.
12. After `AGENT_RESERVED`, confirm `CALL TRANSFERRED` is logged with no errors from the Media Server.
13. If you see `rude rejection` with `Received message: [EslMessage]`: add the VC server IP and VC Docker container IP to the Media Server ACL.
14. If an error appears after `Opening ESL Connection`: verify Media Server is running and that port `8021` is open on the Media Server. See [ESL Connection issues](#esl-connection-issues) below.
15. Verify the `agentExtension` after `AGENT RESERVED` matches the agent's extension on the Agent Desk.

---

### IVR Menu Does Not Play When Call Starts

1. Dial `*9664` and verify audio is heard.
   - If not: check VPN connection (if remote), reconnect or change the agent extension.
   - If still not heard: contact Support.
2. Check the Media Server dialplan to verify the `cxIvr.lua` script is set.
3. If neither fix works: contact Support.

---

### Call Drops After Selecting the Agent Option

1. Check the Media Server dialplan for the `cxIvr.lua` script.
2. Check Media Server logs for errors logged at call start.
3. Contact Support to verify the IVR script is not failing on the agent option selection.

---

### Error Message Plays: "We Have Encountered an Error. Please Try Again Later"

**Check Agent Desk:**
1. Verify at least one agent is logged in.
2. Confirm all logged-in agents have their browser tab open (not closed during ringing).
3. Ensure agents are using the proper log-out function, not closing the tab.
4. Verify microphone permission is granted in the browser before the call arrives.

**Check Media Server:**
1. Note the agent's voice extension from the Agent Desk.
2. Open the Registrations section in the Media Server browser interface.
3. Verify the agent's extension is listed in the **User** column.
   - Listed twice: another agent is using the same extension (shared extensions are not supported).
   - Not listed: reload the agent's tab and confirm "CX Voice Connected" appears at the top of the page.

---

### RONA — Call Not Routed to Any Agent and Call Ends Abruptly

1. Check the Media Server RONA dialplan.
2. If the `rona` action is missing from the `local_extension` dialplan, add the following line at the end:

```
action | lua | vcApi.lua 'rona' | 1 | 76 | true
```

---

### RONA — Queue Music Plays But No New Agent Is Assigned

1. Verify an agent is logged in with CX Voice MRD in Ready state.
2. Confirm no SIP errors in the Agent Desk browser console.
3. Check Unified Admin to confirm the agent has the correct queue assigned.
4. Check Voice Connector logs for errors.

---

## Queue Transfer Scenarios

### Call Connected to First Agent But Does Not Transfer to Second Agent

1. Verify the second agent was logged in at the time of transfer.
2. Check Voice Connector logs for errors.
3. Open the Agent Desk config map and note the value of `STATIC_QUEUE_TRANSFER_DN`.
4. Verify that value matches the Queue Transfer dialplan in the Media Server and the `vcApi.lua` Media Server script.

---

## IVR-Based Outbound

### Error Returned When Contact is Added via API

| Error Code | Meaning | Resolution |
|---|---|---|
| `406` | Ongoing call with the same contact number already exists | Disconnect the previous call. If error persists after disconnection, contact Support. |
| `400` | Incorrect or missing field in the contact payload | Check the VC logs for the missing field; correct the payload. |
| `500` | Unexpected error while dialling | Check VC logs for error description; contact Support if not self-explanatory. |
| `503` | Dialer database issue | Follow the database connection troubleshooting steps. |

---

### Contact Added But Customer Receives No Call

**Check Dialer logs:**

| Dialer Log Pattern | Action |
|---|---|
| Database error logged | Follow database connection troubleshooting steps |
| No log with "CAMPAIGN TYPE:" | Verify correct database details in Dialer environment variables; confirm `MAX_CONCURRENT_CALLS` ≥ 1 and `CALLS_PER_SECOND` ≥ 1 |
| `NO EFSWITCH CONNECTION` | Verify correct Media Server details in Dialer env; confirm Media Server is running; add Dialer IP to Media Server ACL |
| `INVALID GATEWAY` | Verify the gateway ID in the contact payload is correct |
| `GATEWAY DOWN` | Restart the gateway in the Media Server browser interface |
| `CALLED THE CUSTOMER` shown but no call received | Verify the IVR number in the contact payload matches the IVR menu on the Media Server |

---

## Progressive Agent-Based Outbound

### Contact Added But Customer Receives No Call

**Check Dialer logs:**
1. If database error: follow database connection troubleshooting.
2. If no "CAMPAIGN TYPE:" log: verify database details, `MAX_CONCURRENT_CALLS` ≥ 1, `CALLS_PER_SECOND` ≥ 1.
3. If `UNABLE TO REQUEST AGENT FROM VOICE CONNECTOR FOR CALL ID`:
   - `400`: incorrect/missing contact payload fields.
   - `503`: CX may be down; check CCM port.
   - `500`: check VC logs; contact Support if unclear.
4. If error after `AGENT REQUESTED FOR CALL ID`: follow database troubleshooting.
5. If `RECEIVED RESERVED AGENT INFO FOR CALL ID` is not shown within 1 minute of `AGENT REQUESTED`: check Voice Connector logs.
6. If `INVALID GATEWAY`: verify gateway ID. If `GATEWAY DOWN`: restart the gateway.
7. If `UNEXPECTED ERROR` after `DIALING AGENT-BASED CONTACT WITH ID`: verify Media Server is up; check Media Server ACL.
8. If `AGENT-BASED CONTACT WITH ID SENT TO EFSWITCH` is shown but no call received:
   - `CALL_REJECTED` / `NO_ANSWER`: PSTN issue; retry the call.
   - `UNALLOCATED_NUMBER`: the contact number does not exist.

**If no Dialer log output:**
Check Voice Connector logs. If `DIALER INTERNAL SERVER ERROR. CODE 500`:
1. Verify correct Media Server details in Dialer env.
2. Confirm Media Server is running.
3. Add Dialer IP to Media Server ACL.
4. Confirm the Dialer container is running.
5. Verify VC env has correct Dialer IP and port; confirm Dialer port is open.

If `DIALER SERVICE ERROR. CODE 503`: follow database connection troubleshooting.

---

### Customer Received Call But Call Was Not Bridged to Agent

1. Note the agent's extension in the Agent Desk.
2. Open Dialer logs and note the `agentExtension` value after `RECEIVED RESERVED AGENT INFO FOR CALL ID`.
3. If the two extensions do not match: another agent with the same queue may have logged in and been reserved instead. Check Unified Admin for duplicate queue assignments.

---

## ESL Connection Issues

If an error appears immediately after `Opening ESL Connection` in the Voice Connector or Dialer logs:

**1. Verify ESL port 8021 is open:**
```bash
sudo netstat -tulnp | grep 8021
```
If not open: ensure FreeSWITCH is running and the ESL module is loaded.

**2. Add Docker IPs to FreeSWITCH ACL:**
```bash
docker inspect <container_name> | grep -E "IPAddress|Gateway"
```
Add both the container's IPv4 address and its gateway IP to the ESL ACL in FusionPBX. Then restart FreeSWITCH:
```bash
sudo systemctl restart freeswitch
```

**3. Verify ESL password:**
```bash
sudo nano /etc/freeswitch/autoload_configs/event_socket.conf.xml
```
Ensure the password in this file matches your application environment variable (`ESL_PASSWORD`).

**4. Restart Docker containers:**
```bash
docker compose down
docker compose up -d
```

**5. Recheck logs:**
```bash
docker logs <container_name> -f
```

---

## Related Articles

- [CX Voice Limitations](CX-Voice-Limitations.md)
- [Adding Agent Extensions for CX Voice](Adding-Agent-Extensions-CX-Voice.md)
- [CX Dialer Reference](CX-Dialer-Reference.md)
- [Accessing CX Voice Components](../../How-to_Guides/Administrator/Accessing-CX-Voice-Components.md)
- [Accessing Kubernetes Logs](../../How-to_Guides/Administrator/Accessing-Kubernetes-Logs.md)
- [Inbound Calls](Inbound-Calls.md)
- [Outbound Calls](Outbound-Calls.md)
