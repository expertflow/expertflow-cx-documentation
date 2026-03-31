---
title: "WebRTC Channel Configuration Guide"
summary: "Step-by-step guide for configuring the WebRTC voice channel in ExpertFlow CX — covering prerequisites, Unified Admin queue and channel manager setup, pre-chat form schema, and customer web widget configuration."
audience: [solution-admin]
product-area: [voice]
doc-type: how-to
difficulty: advanced
keywords: ["webrtc configuration CX", "webrtc voice channel setup", "webrtc unified admin", "freeswitch webrtc CX", "webrtc queue setup", "webrtc channel type", "web widget webrtc", "sip extension webrtc CX"]
aliases: ["configure webrtc CX", "webrtc setup CX", "webrtc channel CX"]
last-updated: 2026-03-10
---

# WebRTC Channel Configuration Guide

This guide explains how to configure the **WebRTC** voice channel in ExpertFlow CX, enabling browser-based audio/video calls through the customer web widget.

## Prerequisites

- Voice Connector deployed and configured
- EF Switch deployed
- Microphone and camera permissions enabled on both agent and customer sides
- EF Media Server and ExpertFlow CX Server times synchronized

## Important Notes

- WebRTC is always a **multichannel call** — the web session must be established first, then audio/video. The Web channel must be configured before the WebRTC channel.
- Do **not** enable WebRTC and Cisco Voice Channel simultaneously. Only one voice channel should be active at a time.
- Set **Customer Inactivity Timeout** and **Agent Request TTL** to at least **3600 seconds** (1 hour), or greater than your contact center's maximum configured call duration.
- Private browser windows are not supported.

---

## Step 1: Unified Admin — Routing Engine

### Create a Routing Attribute

1. Navigate to **Routing Engine → Routing Attributes**.
2. Create a new attribute (e.g., `WebRTC Voice`) with type **Boolean**.
3. Save.

### Create a Queue

1. Navigate to **Routing Engine → Queues**.
2. Create a new queue (e.g., `WebRTC Queue`).
3. Set the **MRD type** to `CX Voice`.
4. After saving, open the queue and click **Add Step**.
5. Link the queue step to the `WebRTC Voice` routing attribute.

### Assign Routing Attribute to Agents

1. Open the **Agent Attributes** section.
2. Assign the `WebRTC Voice` attribute to agents who should receive WebRTC voice calls.

---

## Step 2: Unified Admin — Channel Manager

### Create a Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Select the `WEB_RTC` channel type.
3. In the **Provider Webhook** field, enter the Voice Connector callback URL:
   ```
   http://{VC-IP}:{VC-PORT}/ccm-msg/receive
   ```
4. Save.

### Create a Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Associate the connector with the WEB_RTC channel provider configured above.
3. Save.

### Create a Channel

1. Navigate to **Channel Manager → Channel** and add a new channel for the `WEB_RTC` channel type.
2. Fill in the channel settings:

   | Field | Value |
   |---|---|
   | **Channel Name** | e.g., `WebRTC Voice Channel` |
   | **Service Identifier** | The DN (Dial Number) configured as the Dialing URI in the customer widget |
   | **Bot** | Select the configured bot |
   | **Channel Connector** | Select the WEB_RTC connector |
   | **Channel Mode** | `HYBRID` |
   | **Agent Selection Policy** | `LONGEST AVAILABLE` |
   | **Routing Mode** | `PUSH` |
   | **Queue** | Select the `WebRTC Queue` (CX Voice MRD) |
   | **Customer Inactivity Timeout** | Minimum 3600 seconds |
   | **Agent Request TTL** | Minimum 3600 seconds |

3. Save.

---

## Step 3: Create a Pre-Chat Form

A pre-chat form must be created to collect customer name and phone number before the call. This data is sent to FreeSWITCH, which forwards it to CCM for customer identification on the agent desk.

1. Navigate to **Unified Admin → Forms**.
2. Create a new form with type **Pre-conversation**.
3. Add a **Name** field following the required naming convention.
4. Add a **Phone** field following the required naming convention.
5. Save.

> Ensure the naming conventions for the Name and Phone fields follow the expected format — the data is passed directly to FreeSWITCH for call identification.

---

## Step 4: Configure the Customer Web Widget

1. Navigate to **Channel Manager → Web Widget** and create or edit a web widget.
2. Fill in the widget details (identifier, title, form info, language, etc.).
3. Enable the **Enable WebRTC** toggle. Additional fields will appear.
4. Fill in the WebRTC-specific settings:

   | Field | Description |
   |---|---|
   | **FreeSwitch Server URL & Port** | URL and port of the FreeSWITCH server connected to your instance. |
   | **Dialing URI** | Must match the DN configured in your WebRTC dial plan and as the channel's Service Identifier. |
   | **SIP Extension** | A SIP extension created on the FreeSWITCH server. For multi-tenant (MTT), use the domain name instead. |
   | **SIP Extension Password** | Password for the SIP extension. |
   | **Channel Name** | Name of the WebRTC channel created in Step 2. |
   | **WebSocket Server (WSS) URL** | WSS server URL — mandatory for WebRTC to function. |

5. Save.

---

## CTI Environment Variables

To update CTI config variables in the unified-agent config map, refer to the Updating Environment Variables for WebRTC guide. For user extension configuration, refer to the extension configuration guide.

---

## Related Articles

- [Web App Calls Overview](../Functional_Areas/Voice_Real_Time_Media/Web-App-Calls-Overview.md)
- [Accessing CX Voice Components](Accessing-CX-Voice-Components.md)
- [Media Server Configuration CX Voice](Media-Server-Configuration-CX-Voice.md)
- [Voice Channel Configuration Limitations](Voice-Channel-Configuration-Limitations.md)
- [Configuring the Customer Widget](Configuring-the-Customer-Widget.md)
