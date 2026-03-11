---
title: "Cisco Integration Known Limitations"
summary: "Technical reference documenting tested versions, failover behaviors, and known constraints of the Cisco Voice integration."
audience: [integrator]
product-area: [voice, cisco-integration]
doc-type: reference
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Cisco Integration Known Limitations

This reference document outlines the tested configurations and known technical behaviors of the ExpertFlow Cisco Voice integration. Review these items during system design and troubleshooting.

## 1. Supported Versions & Hardware
- **Cisco UCCX:** 12.5, 12.5.1 SU3.
- **Cisco UCCE:** Supported (Multiple Versions).
- **IP Phones:** CIPC version 8.6.x, Jabber 14.x, hard phones (7965, 7942).
- **Authentication:** Tested with non-SSO; Cisco SSO is assumed to be compatible.

## 2. Platform Constraints
- **Independent Logout:** Logging out of Finesse does **not** log the agent out of ExpertFlow CX. Agents will still appear as active in CX dashboards unless manually signed out or timed out.
- **Reason Codes:** The system **requires** at least one custom "Not Ready" reason and one custom "Logout" reason to function correctly.

## 3. Failover Behaviors
In the event of a Cisco Finesse failover (HA switch), observe the following:
- **State Reset:** If Finesse is restored while a call is in progress, the agent's state will default to **Not Ready**.
- **Call Leg Duration:** If a call ends during the failover window, the Agent Desk may show a 0-second call leg duration as the CTI event data is lost.
- **Direct Transfer:** During a failover, the customer's phone number may appear as `null` in the call leg display once Finesse is restored.

## 4. Sync Service Constraints
- **Manual Deletion:** Deleting a team or user in Cisco will disable them in CX, but will **not** delete the group from Keycloak. The administrator must manually remove these groups from IAM.
- **Team Initialization:** Cisco teams are not synced to Keycloak until an agent from that team performs their first successful login to Finesse.

---

*To verify your network configuration against these limits, see [Finesse Integration Prerequisites](Finesse-Integration-Prerequisites.md).*
