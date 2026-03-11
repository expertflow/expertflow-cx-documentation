---
title: "Finesse Integration Prerequisites"
summary: "Technical reference for Integration Specialists detailing the ports, protocols, and credentials required for Cisco Finesse integration."
audience: [integrator]
product-area: [voice, cisco-integration]
doc-type: reference
difficulty: intermediate
aliases: []
last-updated: 2026-03-08
---

# Finesse Integration Prerequisites

To successfully integrate the ExpertFlow Agent Desk with Cisco Finesse, you must ensure that all network paths and credentials are provisioned according to the specifications below.

## 1. Access Credentials
| Component | Credential Required | Purpose |
| :--- | :--- | :--- |
| **Cisco Finesse** | Admin Credentials | For initial configuration and gadget management. |
| **Agent Desk** | Cisco Finesse Agent Credentials | To monitor CTI events and perform state changes. |

## 2. Port and Protocol Matrix
The following ports must be open between the Agent Desk (Client Browser) and the Cisco Finesse servers.

| Source | Destination | Protocol | Port | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Agent Desk** | Cisco Finesse | HTTPS (REST) | 8445 | State change requests and Media Blending commands. |
| **Keycloak** | Cisco Finesse | HTTPS (REST) | 8445 | Agent identity synchronization. |
| **Finesse XMPP** | Agent Desk | XMPP | 5222 | Real-time CTI and Agent State change events. |

## 3. Connectivity Notes
- **XMPP Security:** Communication over port 5222 is un-secure. The Agent Desk uses the specific agent's Finesse credentials to subscribe to these events.
- **SSL Bypass:** The Agent Desk is configured to bypass SSL certificate verification for REST API requests to Finesse (Port 8445) to ensure high-availability routing even with self-signed certificates.

---

*For common issues and edge cases, see [Cisco Integration Known Limitations](Cisco-Integration-Known-Limitations.md).*
