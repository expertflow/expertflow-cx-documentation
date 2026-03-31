---
title: "SMPP Configuration Guide"
summary: "How-to guide for configuring an SMPP SMS channel in ExpertFlow CX Unified Admin — covering Channel Type, Channel Provider, Channel Connector, and Channel setup with all 11 SMPP environment variables."
audience: [solution-admin]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["SMPP configuration CX", "SMS SMPP CX", "SMPP connector CX", "SMPP channel unified admin CX", "SMS channel CX", "SMPP bind type CX", "configure SMPP CX"]
aliases: ["SMPP SMS setup CX", "SMPP channel configuration CX"]
last-updated: 2026-03-10
---

# SMPP Configuration Guide

This guide explains how to configure an SMPP-based SMS channel in ExpertFlow CX Unified Admin. SMPP (Short Message Peer-to-Peer) allows CX to send and receive SMS messages through a carrier or aggregator's SMSC.

> The SMPP Channel Type is pre-installed (bootstrapped) in ExpertFlow CX. You do not need to create it manually.

---

## Prerequisites

- SMPP connector service deployed and accessible within the cluster at `ef-smpp-connector-svc:8115`.
- SMPP credentials from your SMS provider (host, port, system ID, password).
- Access to Unified Admin.

---

## Step 1: Verify the Channel Type

The **SMPP** Channel Type is bootstrapped with ExpertFlow CX. To confirm it exists:

1. Navigate to **Unified Admin → Channel Manager → Channel Type**.
2. Verify that an entry named **SMPP** (or similar) is present.

No action is required unless the entry is missing — in that case, create a new Channel Type and select the appropriate Media Routing Domain (e.g., Chat).

---

## Step 2: Add Channel Provider

The Channel Provider defines the webhook where CCM delivers outbound messages to your SMPP connector service.

1. Navigate to **Channel Manager → Channel Provider** and click **New Channel Provider**.
2. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | `SMPP Provider` (or any descriptive name) |
   | **Supported Channel Types** | Select **SMPP** |
   | **Provider Webhook** | `http://ef-smpp-connector-svc:8115` |

3. Add the following **Custom Attributes** (these will be filled in Step 3):

   | Attribute Key | Description |
   |---|---|
   | `SMPP-HOST` | SMSC server hostname or IP |
   | `SMPP-PORT` | SMSC server port |
   | `SMPP-SYSTEM-ID` | SMPP system ID (username) |
   | `SMPP-PASSWORD` | SMPP password |
   | `SMPP-BIND-TYPE` | Bind mode: `0` = TX (transmit), `1` = RX (receive), `2` = TRX (transceive) |
   | `SMPP-NUMBER-TYPE` | Number type for source/destination addresses |
   | `SMPP-SECURE` | `true` to use TLS/SSL; `false` for plain TCP |
   | `SMPP-SYSTEM-TYPE` | System type string (provider-specific; often left blank) |
   | `SMPP-SOURCE-ADDR` | Source address (sender ID or short code) |
   | `SMPP-ENCODING` | Message encoding (e.g., `GSM7`, `UCS2`) |
   | `SMPP-ENQUIRE-LINK-TIMER` | Interval (ms) for keep-alive enquire_link PDUs |

4. Save.

---

## Step 3: Create Channel Connector

The Channel Connector binds the provider to its runtime credential values.

1. Navigate to **Channel Manager → Channel Connector** and click **Create Connector**.
2. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | `SMPP Connector` |
   | **Channel Provider Interface** | Select the provider created in Step 2 |

3. Fill in the custom attribute values:

   | Variable | Description | Example |
   |---|---|---|
   | `SMPP-HOST` | Hostname or IP of the SMSC | `smsc.provider.com` |
   | `SMPP-PORT` | SMSC port | `2775` |
   | `SMPP-SYSTEM-ID` | Your SMPP system ID | `mySystemId` |
   | `SMPP-PASSWORD` | Your SMPP password | `••••••••` |
   | `SMPP-BIND-TYPE` | `0` = TX only, `1` = RX only, `2` = TRX (recommended) | `2` |
   | `SMPP-NUMBER-TYPE` | Address type for phone numbers | `1` |
   | `SMPP-SECURE` | Enable TLS | `false` |
   | `SMPP-SYSTEM-TYPE` | Provider system type (if required) | `""` |
   | `SMPP-SOURCE-ADDR` | Sender ID displayed to customers | `+1234567890` |
   | `SMPP-ENCODING` | Character encoding for messages | `GSM7` |
   | `SMPP-ENQUIRE-LINK-TIMER` | Keep-alive interval in milliseconds | `30000` |

4. Save.

---

## Step 4: Create Channel

The Channel links the connector to a routing queue and defines behavior for incoming SMS interactions.

1. Navigate to **Channel Manager → Channel** and click **New Channel**.
2. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | `SMS Channel` |
   | **Service Identifier** | The inbound phone number or short code (e.g., `+15551234567`) |
   | **Channel Connector** | Select the connector created in Step 3 |
   | **Channel Mode** | `HYBRID` (recommended) |
   | **Routing Mode** | `PUSH` or `PULL` |
   | **Default Queue / List** | Assign the appropriate queue (Push) or list (Pull) |
   | **Response SLA** | Time (seconds) before an unanswered request is re-routed |
   | **Customer Activity Timeout** | Seconds of inactivity before the session expires |
   | **Agent Selection Policy** | `LONGEST AVAILABLE` |
   | **Agent Request TTL (sec)** | Time before an unaccepted agent request expires |

3. Save.

---

## SMPP Bind Types

| Value | Mode | Description |
|---|---|---|
| `0` | TX (Transmitter) | Connector can only send messages |
| `1` | RX (Receiver) | Connector can only receive messages |
| `2` | TRX (Transceiver) | Connector can send and receive — use for full duplex SMS |

For most deployments, use `2` (TRX).

---

## Related Articles

- [Channel and Connector Setup](Channel-and-Connector-Setup.md)
- [Register Channel Connector](../Integrator/Register-Channel-Connector.md)
- [Media Routing Domains (MRD) Overview](Media-Routing-Domains-MRD-Overview.md)
- [Channel Connector Developer Guide](../Integrator/Channel-Connector-Developer-Guide.md)
