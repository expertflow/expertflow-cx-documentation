---
title: "CX SIP Proxy Deployment Guide"
summary: "Overview and deployment index for the ExpertFlow CX SIP Proxy — covering single-node and HA deployment modes, hardware prerequisites, required ports, and links to installation and configuration guides."
audience: [hosting-partner]
product-area: [voice, platform]
doc-type: explanation
difficulty: intermediate
keywords: ["CX SIP proxy deployment", "OpenSIPS CX", "SIP proxy ExpertFlow", "CX SIP proxy HA", "SIP proxy prerequisites CX"]
aliases: ["EF SIP proxy overview", "CX SIP proxy guide", "OpenSIPS ExpertFlow deployment"]
last-updated: 2026-03-10
---

# CX SIP Proxy Deployment Guide

The ExpertFlow CX SIP Proxy is built on **OpenSIPS 3.4** and acts as the SIP signaling layer between ExpertFlow CX and upstream voice infrastructure (Cisco CVP, Cube, VVB, CUCM, and the Dialer). It supports two deployment modes: **single node** and **high availability (HA)**.

---

## Deployment Modes

| Mode | Description | When to Use |
|---|---|---|
| **Single Node** | One OpenSIPS server handles all SIP traffic | Development, testing, or low-volume production |
| **HA (High Availability)** | Two or more OpenSIPS servers with a shared virtual IP managed by Keepalived/VRRP | Production deployments requiring failover |

In HA mode, a **virtual IP address** floats between the primary and backup nodes. Keepalived monitors node health and promotes the backup if the primary fails.

---

## Prerequisites

### Hardware (per node)

| Resource | Minimum |
|---|---|
| CPU | 4 cores |
| RAM | 8 GB |
| Disk | 500 GB |

### Software

- **OS**: Debian 12 (Bookworm)
- **PHP**: 7.4 (required for the OpenSIPS Control Panel)
- **Database**: MariaDB (for OpenSIPS dialplan and dispatcher/LB data)

---

## Required Ports

| Port | Protocol | Purpose |
|---|---|---|
| 5060 | TCP | SIP signaling |
| 5060 | UDP | SIP signaling |
| 5555 | BIN (binary) | OpenSIPS inter-node clustering (HA only) |

Ensure these ports are open between OpenSIPS nodes and between OpenSIPS and all upstream voice components.

---

## Deployment Steps

Follow these guides in order:

1. **[CX SIP Proxy Installation Guide](CX-SIP-Proxy-Installation-Guide.md)** — Install OpenSIPS 3.4, MariaDB, and the OpenSIPS Control Panel on each node.

2. **Configure traffic routing** — choose one method:
   - **[Configuring the Dispatcher Module](Configuring-Dispatcher-in-CX-SIP-Proxy.md)** — Stateless load distribution; configured via opensips.cfg and the control panel.
   - **[Configuring the Load Balancer Module](Configuring-Load-Balancer-in-CX-SIP-Proxy.md)** — Capacity-aware load balancing using channel resources; configured via opensips.cfg and the control panel.

3. **[Load Balancing via the Dispatcher Module](Load-Balancing-Dispatcher-Module.md)** — Apply dispatcher-based load balancing rules in opensips.cfg with failure route handling.

4. *(HA only)* **[HA Setup for the EF SIP Proxy](HA-in-EF-SIP-Proxy.md)** — Configure OpenSIPS clustering, Keepalived/VRRP virtual IP, and the PHP authentication fix.

---

## Related Articles

- [CX SIP Proxy Installation Guide](CX-SIP-Proxy-Installation-Guide.md)
- [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md)
- [Configuring the Load Balancer in CX SIP Proxy](Configuring-Load-Balancer-in-CX-SIP-Proxy.md)
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)
- [Load Balancing via Dispatcher Module](Load-Balancing-Dispatcher-Module.md)
