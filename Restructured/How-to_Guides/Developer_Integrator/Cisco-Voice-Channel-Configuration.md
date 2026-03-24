---
title: "Cisco Voice Channel Configuration"
summary: "Technical guide for Integration Specialists to configure the Cisco CC channel type within the Unified Admin."
audience: [developer-integrator]
product-area: [voice, cisco-integration]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Cisco Voice Channel Configuration

As an Integration Specialist (Ian), you must ensure that the ExpertFlow CX platform is correctly linked to the Cisco Finesse and Unified Communications environment.

## 1. Prerequisites
- **Time Sync:** Finesse and CX Server clocks must be synchronized via NTP.
- **Timeout Alignment:** The **Customer Activity Timeout** in CX must always be greater than the configured call timeout in Cisco Finesse.

## 2. Unified Admin Setup
Follow these steps to enable the Cisco Voice channel.

### Step 1: Channel Provider
1. Go to **Channel Manager > Channel Providers**.
2. Add a provider for the **CISCO_CC** channel type. 
3. **Note:** Unlike digital channels, a Provider Webhook is not required for Cisco Voice.

### Step 2: Channel Connector
1. Create a new connector linked to the Cisco provider.
2. Enter the Finesse API credentials and server FQDNs.

### Step 3: Channel Registration
1. Go to the **Channel** section and add a new channel of type **CISCO_CC**.
2. **Service Identifier:** Enter a unique numeric ID. This same ID must be mapped to the `CISCO_SERVICE_IDENTIFIER` attribute in the Agent Desk configuration.
3. **Routing Mode:** Must be set to **EXTERNAL** (since Cisco handles the voice routing).
4. **Outbound:** Enable the "Default Outbound Channel" flag if this channel will be used for outbound campaigns.

## 3. Media Blending & MRDs
To ensure correct agent state management:
- **MaxTaskRequest:** Set to `1` for the CISCO CC MRD.
- **Autosync:** Set `Autosync state with parent state` to **False**. This prevents CX from overriding the Cisco voice state unexpectedly.

---

*For gadget deployment, see the [Deploying Finesse Gadgets](Deploying-Finesse-Gadget.md) guide.*
