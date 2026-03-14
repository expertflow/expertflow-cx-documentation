---
title: "SIP Proxy Architecture"
summary: "High-level architectural overview of the ExpertFlow CX SIP Proxy, explaining its role in signal flow, load balancing, and high availability for voice interactions."
audience: [partner]
product-area: [voice, platform]
doc-type: explanation
difficulty: intermediate
last-updated: 2026-03-11
---

# SIP Proxy Architecture

The ExpertFlow CX SIP Proxy is a high-performance signaling engine based on **OpenSIPS**. It serves as the central traffic controller for all SIP-based voice interactions, providing a scalable and resilient bridge between external telephony elements (Cisco, SIP Trunks) and the ExpertFlow media stack.

## 1. Role in the Voice Ecosystem
In a standard ExpertFlow CX deployment, the SIP Proxy does not process audio (RTP). Instead, it manages the **SIP signaling (INVITE, BYE, CANCEL)** to ensure that calls are routed to the most available and appropriate media resource.

### **Key Functions:**
*   **Signal Normalization:** Translates SIP headers between disparate systems (e.g., matching Cisco CVP labels to internal CX Dial Numbers).
*   **Security (Access Control):** Acts as a SIP firewall by maintaining a "Trusted List" of IP addresses for CUBEs, CUCMs, and CVPs.
*   **NAT Traversal:** Handles complex network topologies where media servers are behind private firewalls.

---

## 2. Load Balancing and High Availability
The SIP Proxy is the primary mechanism for achieving **High Availability (HA)** in the voice layer.

### **The Dispatcher Module**
The Proxy uses the OpenSIPS `dispatcher` module to monitor the health of downstream Media Servers (EFSwitch). 
- **Heartbeat Monitoring:** The Proxy sends periodic `OPTIONS` pings to each Media Server.
- **Failover Logic:** If a Media Server fails to respond, the Proxy automatically removes it from the routing pool and redirects new calls to healthy nodes.
- **Load Distribution:** It distributes calls across multiple Media Servers based on predefined algorithms (e.g., Round Robin or Weight-based).

---

## 3. Cisco Integration Architecture
When integrated with a Cisco Contact Center (UCCE/PCCE), the SIP Proxy maps the Cisco environment to the ExpertFlow platform using the following logic:

| Cisco Element | Mapping Logic | SIP Proxy Action |
| :--- | :--- | :--- |
| **CUBE** | Inbound Gateway | Routes incoming `INVITEs` to the internal CX Dialing Plan. |
| **CVP/VVB** | Media Resources | Maps labels (e.g., 9191, 9292) to specific internal VRU groups. |
| **CUCM** | Agent Endpoints | Handles transfers and conferences by bridging the SIP Trunk to agent extensions. |

---

## 4. Signal Flow Overview
1.  **Ingress:** A call arrives at the **CUBE** and is forwarded to the **SIP Proxy**.
2.  **Logic:** The Proxy identifies the tenant and destination based on the Request URI.
3.  **Dispatch:** The Proxy selects a healthy **Media Server (EFSwitch)** and forwards the signal.
4.  **Handover:** The Media Server takes over the RTP (audio) and communicates with the **Voice Connector** to notify the Agent Desk.

---

## Related Guides
*   [CX SIP Proxy Installation Guide](CX-SIP-Proxy-Installation-Guide.md)
*   [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md)
*   [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)
*   [Cisco Contact Center Integration Reference](../Getting_Started/Cisco-Contact-Center-Integration-Reference.md)
