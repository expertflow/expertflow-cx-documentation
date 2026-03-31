---
title: "Configuring the Dispatcher in CX SIP Proxy"
summary: "How-to guide for configuring the OpenSIPS Dispatcher module in the ExpertFlow CX SIP Proxy — covering Set IDs for each voice component (CVP, Cube, VVB, CUCM, Dialer), control panel configuration steps, and Dialplan attribute mapping."
audience: [partner]
product-area: [voice, platform]
doc-type: how-to
difficulty: intermediate
keywords: ["OpenSIPS dispatcher CX", "SIP proxy dispatcher config CX", "CX SIP proxy Set ID", "dispatcher module OpenSIPS CX", "SIP dispatcher CVP CX"]
aliases: ["dispatcher CX SIP proxy", "OpenSIPS Set ID CX", "configure dispatcher CX"]
last-updated: 2026-03-10
---

# Configuring the Dispatcher in CX SIP Proxy

The OpenSIPS **Dispatcher** module provides stateless load distribution across SIP destinations. Destinations are grouped into **Sets** identified by a Set ID. The ExpertFlow CX SIP Proxy uses a dedicated Set ID for each voice component type.

---

## Set ID Reference

| Set ID | Voice Component |
|---|---|
| 1 | Cisco CVP |
| 2 | Cisco Cube |
| 3 | Cisco VVB |
| 4 | Cisco CUCM |
| 5 | Dialer |

---

## Step 1: Open the Dispatcher Configuration

1. Log in to the OpenSIPS Control Panel at `http://<server-ip>/`.
2. Navigate to **System → Dispatcher**.
3. Click **Add Destination** to add a new entry.

---

## Step 2: Configure a Destination

Fill in the following fields for each SIP destination:

| Field | Description | Example |
|---|---|---|
| **Set ID** | Dispatcher set number (see reference above) | `1` |
| **SIP URI** | Address of the destination endpoint | `sip:192.168.1.10:5060` |
| **Socket** | OpenSIPS listening socket to send from | `udp:0.0.0.0:5060` |
| **State** | Initial destination state | `Active` |
| **Probing** | Enable SIP OPTIONS-based health probing | `Enabled` |
| **Weight** | Relative traffic weight for this destination | `1` |

Repeat for each upstream destination, using the correct Set ID for the component type.

---

## Step 3: Configure Dialplan Attributes

The Dialplan maps incoming SIP requests to the correct dispatcher set. Each dialplan rule uses a **Dialplan Attribute** value to select the target Set ID.

Attribute values follow this format:

```json
{
  "DS-1": "sip:192.168.1.10:5060",
  "DS-2": "sip:192.168.1.20:5060",
  "DS-3": "sip:192.168.1.30:5060",
  "DS-4": "sip:192.168.1.40:5060",
  "DS-5": "sip:192.168.1.50:5060"
}
```

| Attribute Key | Maps To |
|---|---|
| `DS-1` | Dispatcher Set 1 (CVP) |
| `DS-2` | Dispatcher Set 2 (Cube) |
| `DS-3` | Dispatcher Set 3 (VVB) |
| `DS-4` | Dispatcher Set 4 (CUCM) |
| `DS-5` | Dispatcher Set 5 (Dialer) |

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
| **Attributes** | Select the `DS-x` attribute to route to the target set |

Use **REGEX** matching for prefix-based routing (e.g., all calls starting with `+1`). Use **EQUAL** for exact matches.

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [Configuring the Load Balancer in CX SIP Proxy](Configuring-Load-Balancer-in-CX-SIP-Proxy.md)
- [Load Balancing via Dispatcher Module](Load-Balancing-Dispatcher-Module.md)
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)
