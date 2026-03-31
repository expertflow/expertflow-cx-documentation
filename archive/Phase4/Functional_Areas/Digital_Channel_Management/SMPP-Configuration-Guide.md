---
title: "SMPP Configuration Guide"
summary: "Reference for configuring the SMPP SMS connector in ExpertFlow CX — covering Unified Admin Channel Provider, Channel Connector, Channel setup, and all SMPP configuration variables."
audience: [solution-admin]
product-area: [channels, digital]
doc-type: reference
difficulty: advanced
keywords: ["SMPP configuration", "SMPP connector setup", "SMPP Unified Admin", "SMPP variables", "SMS configuration", "SMPP-REMOTE-IP-ADDRESS", "SMPP-SYSTEM-ID"]
aliases: ["SMPP connector configuration", "configure SMPP", "SMPP SMS setup"]
last-updated: 2026-03-10
---

# SMPP Configuration Guide

This reference covers the Unified Admin and configuration variable setup for the CX SMPP connector. Obtain connection details (IP, port, system ID, password, bind type) from your SMPP gateway or mobile carrier provider before proceeding.

## Unified Admin Configuration

### Channel Type

The SMPP channel type is automatically bootstrapped by the system as part of the channels connector deployment. No manual creation is required.

### Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Create a new Channel Provider with any name (e.g., **SMPP Provider**).
3. Select **SMS** as the Supported Channel Type. _(Select the applicable channel type — SMS or both if configured.)_
4. In the **Provider Webhook** field, enter the SMPP connector service URL:
   - K3s: `http://ef-smpp-connector-svc:8115`
   - Helm: `http://cx-channels-smpp-connector-svc:8115`
5. Click **Save**.

### Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Create a new Channel Connector (e.g., **SMPP Connector**).
3. Select the Channel Provider Interface created above (e.g., SMPP Provider).
4. Fill in the SMPP configuration attributes (see [Configuration Variables](#configuration-variables) below).
5. Click **Save**.

### Channel

1. Navigate to **Channel Manager → Channel**.
2. Click **Add new channel** under the **SMS** channel type.
3. Fill in the channel details:
   - **Name**: e.g., `SMPP SMS Channel`
   - **Service Identifier**: The active phone number bound to this SMPP channel.
   - Fill in the remaining routing and queue fields as required.
4. Click **Save**.

> **Note**: The Service Identifier must also be added as a service identifier in the component's ConfigMap, as it is required during the initial API call to fetch Unified Admin configurations.

## Configuration Variables

These variables are set in the Channel Connector configuration or the component's environment/ConfigMap:

| Variable | Description | Example Value | Type |
|---|---|---|---|
| `CCM-API` | FQDN of the Customer Channel Manager deployment | `https://cimdemo.expertflow.com` | String100 |
| `SMPP-SECURE` | Whether SMPP connection is secured (TLS) | `false` | Boolean |
| `SMPP-REMOTE-IP-ADDRESS` | IP address of the SMPP gateway | `127.0.0.1` | String100 |
| `SMPP-REMOTE-PORT` | Port of the SMPP gateway | `2775` | PositiveNumber |
| `SMPP-FROM-NUMBER` | Source address for outbound SMS. Customer replies are also received on this number. | `1218` or carrier-assigned number | String100 |
| `SMPP-SYSTEM-ID` | System ID for SMPP authentication | `smppclient1` | String100 |
| `SMPP-PASSWORD` | Password for SMPP authentication | `password` | String100 |
| `SMPP-SYSTEM-TYPE` | System type value (provided by SMPP administrator; usually a short string) | `SMS` | String100 |
| `SMPP-BIND-TYPE` | Bind type: `0` = TX (Transmitter), `1` = RX (Receiver), `2` = TRX (Transceiver) | `2` | String100 |
| `SMPP-NUMBER-TYPE` | Number format: `0` = numeric, `1` = alphanumeric | `0` | String100 |
| `PUBLISHER-ENABLE` | Whether to publish delivery receipts for outbound SMS | `true` or `false` | Boolean |

## Bind Type Reference

| Value | Name | Description |
|---|---|---|
| `0` | TX (Transmitter) | Can only send SMS; cannot receive |
| `1` | RX (Receiver) | Can only receive SMS; cannot send |
| `2` | TRX (Transceiver) | Can both send and receive SMS |

> For two-way agent-customer SMS conversations, use TRX (`2`).

## Related Articles

- [SMPP Channel Overview](SMPP-Channel-Overview.md)
- [Channel and Connector Setup](../../Solution_Admin/Channel-and-Connector-Setup.md)
- [Twilio SMS/MMS Configuration Guide](../../Solution_Admin/Twilio-SMS-MMS-Configuration-Guide.md)
