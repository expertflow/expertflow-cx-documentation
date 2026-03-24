---
title: "Outbound Flows Limitations"
summary: "Reference list of known limitations in ExpertFlow CX outbound campaign flows — covering contact uploads, campaign duplication, decision node behavior, reporting gaps, UCCE wrap-up restrictions, and Cisco multi-tenant limitations."
audience: [conversation-designer]
product-area: [channels, voice]
doc-type: reference
difficulty: beginner
keywords: ["outbound flow limitations CX", "campaign limitations CX", "outbound dialing limitations CX", "CX campaigns known issues", "outbound flows CX restrictions"]
aliases: ["outbound limitations CX", "campaign known issues CX", "outbound flows known issues CX"]
last-updated: 2026-03-10
---

# Outbound Flows Limitations

The following are known limitations in ExpertFlow CX outbound campaign flows.

---

1. **Campaign duplication is disabled.** The duplicate campaign feature is not available in the current release and will be added in a future version.

2. **CSV contact uploads are not immediate.** When you upload a CSV file, contacts are stored in chunks rather than all at once. A manual refresh is required to see the updated contact count in the UI.

3. **Maximum 50,000 contacts per CSV upload.** Files containing more than 50,000 contacts are not supported.

4. **RESTful API via Contact Source is disabled in the UI.** The underlying API is available, but the Contact Source section in Unified Admin does not expose it.

5. **Decision node does not handle all call results from EF CC (FreeSWITCH).** Unified call result codes are documented in the Outbound Result Notifications reference.

6. **Modifying a running campaign's flow only affects unexecuted contacts.** Changes apply to contacts not yet dialed and any newly uploaded contacts. Contacts already in progress are not affected.

7. **Campaign reports do not show multiple agents for transferred or consulted calls.** If a call involves a transfer or consult, only one agent record appears in the campaign report.

8. **Call duration in campaign reports includes ringing time.** The reported duration is from dial initiation to hang-up, not from the moment the customer answers.

9. **Multiple wrap-ups for a single call are not allowed in UCCE.**

10. **Team changes affect historical campaign report data.** If an agent's team is changed and the pipeline is re-run, the updated team name is displayed in campaign reports even for historical records.

11. **Dial Rate and Success Rate can exceed 100%.** This can occur if a dialer node is deleted and re-configured within a published campaign that has already run.

12. **Personal callback data is not shown separately in campaign reports.** Callbacks are included in the aggregate data but are not broken out as a distinct record type.

13. **Cisco Dialer integration is not available in the CX Multi-Tenant solution.**

14. **UCCX 12.0 HA node switch during active call causes missing conversation records.** If a node switch occurs in a UCCX 12.0 HA setup during an active call, conversation data is not generated on the Cisco side and the record will be missing in Unified Admin.

---

## Related Articles

- [Conversation Flow for Outbound Dialing Modes](Conversation-Flow-for-Outbound-Dialing-Modes.md)
- [Managing Outbound Campaigns](../Administrator/Managing-Outbound-Campaigns.md)
- [Campaign Performance Reports](../Supervisor_and_QA_Lead/Campaign-Performance-Reports.md)
