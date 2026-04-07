---
title: "Configuring the Load Balancer in CX SIP Proxy"
summary: "How-to guide for configuring the OpenSIPS Load Balancer module in the ExpertFlow CX SIP Proxy — covering Group IDs for each voice component, channel resource limits, probe modes, and Dialplan attribute mapping."
audience: [platform-operator]
product-area: [voice, platform]
doc-type: how-to
difficulty: intermediate
keywords: ["OpenSIPS load balancer CX", "SIP proxy load balancer config CX", "CX SIP proxy Group ID", "load balancer module OpenSIPS CX", "SIP LB channel resources CX"]
aliases: ["LB CX SIP proxy", "OpenSIPS Group ID CX", "configure load balancer CX"]
last-updated: 2026-03-10
---

# Configuring the Load Balancer in CX SIP Proxy

The OpenSIPS **Load Balancer** module provides capacity-aware traffic distribution. Unlike the Dispatcher module, it tracks resource usage (e.g., active channels) and routes new calls only to destinations with available capacity. Destinations are grouped by **Group ID**.

---

## Group ID Reference

| Group ID | Voice Component |
|---|---|
| 1 | Cisco CVP |
| 2 | Cisco Cube |
| 3 | Cisco VVB |
| 4 | Cisco CUCM |
| 5 | Dialer |

---

## Step 1: Open the Load Balancer Configuration

1. Log in to the OpenSIPS Control Panel at `http://<server-ip>/`.
2. Navigate to **System → Load Balancer**.
3. Click **Add Destination** to add a new entry.

---

## Step 2: Configure a Destination

Fill in the following fields for each SIP destination:

| Field | Description | Example |
|---|---|---|
| **Group ID** | Load balancer group number (see reference above) | `1` |
| **SIP URI** | Address of the destination endpoint | `sip:192.168.1.10:5060` |
| **Resources** | Capacity definition for the destination | `channel=200` |
| **Probe mode** | Health check behavior | `On Disable` |
| **Socket** | OpenSIPS listening socket to send from | `udp:0.0.0.0:5060` |

### Resources Field

The `Resources` field defines the maximum capacity for each destination. Use `channel=<max>` to limit the number of simultaneous calls:

```
channel=200
```

This tells the load balancer that the destination can handle up to 200 concurrent channels.

### Probe Modes

| Mode | Behavior |
|---|---|
| **No Probing** | No health checks — destination is always assumed available |
| **On Disable** | Send SIP OPTIONS probes only when the destination is marked disabled |
| **Permanent** | Continuously probe with SIP OPTIONS; re-enable when the destination recovers |

---

## Step 3: Configure Dialplan Attributes

The Dialplan maps incoming SIP requests to the correct load balancer group. Attribute values use the `LB-x` key format:

```json
{
  "LB-1": "sip:192.168.1.10:5060",
  "LB-2": "sip:192.168.1.20:5060",
  "LB-3": "sip:192.168.1.30:5060",
  "LB-4": "sip:192.168.1.40:5060",
  "LB-5": "sip:192.168.1.50:5060"
}
```

| Attribute Key | Maps To |
|---|---|
| `LB-1` | Load Balancer Group 1 (CVP) |
| `LB-2` | Load Balancer Group 2 (Cube) |
| `LB-3` | Load Balancer Group 3 (VVB) |
| `LB-4` | Load Balancer Group 4 (CUCM) |
| `LB-5` | Load Balancer Group 5 (Dialer) |

---

## Step 4: Add a Dialplan Rule

1. Navigate to **System → Dialplan** in the control panel.
2. Click **Add Rule**.
3. Configure the rule:

| Field | Value |
|---|---|
| **DPID** | Dialplan group ID (e.g., `1`) |
| **Priority** | Rule priority (higher = evaluated first) |
| **Match operator** | `REGEX` or `EQUAL` |
| **Match expression** | Pattern matching the incoming Request-URI or called number |
| **Substitution expression** | Replacement expression (if transforming the URI) |
| **Attributes** | Select the `LB-x` attribute to route to the target group |

---

## Dispatcher vs. Load Balancer

| Feature | Dispatcher | Load Balancer |
|---|---|---|
| Routing basis | Stateless (round-robin, hash, etc.) | Capacity-aware (channel count) |
| Health probing | Optional | Optional (3 probe modes) |
| Resource tracking | No | Yes (`channel=N`) |
| Best for | Simple distribution | Environments with capacity limits |

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md)
- [Load Balancing via Dispatcher Module](Load-Balancing-Dispatcher-Module.md)
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)
