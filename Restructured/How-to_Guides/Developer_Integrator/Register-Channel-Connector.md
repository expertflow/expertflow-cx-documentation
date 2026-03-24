---
title: "Register Channel Connector"
summary: "Step-by-step guide for registering a custom channel connector in ExpertFlow CX Unified Admin — covering Channel Type creation, Channel Provider setup, Channel Connector creation, Channel configuration, and Customer Schema attribute definition."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["register channel connector CX", "channel type unified admin CX", "channel provider CX", "custom channel CX", "new channel type CX", "channel connector registration CX", "customer schema channel CX"]
aliases: ["add channel connector CX", "channel connector setup CX", "register connector CX"]
last-updated: 2026-03-10
---

# Register Channel Connector

Registering a channel connector in Unified Admin defines how ExpertFlow CX communicates with an external media channel. This 5-step process must be completed before the connector can send and receive messages.

---

## Step 1: Add Channel Type

ExpertFlow CX ships with built-in channel types. If your connector targets a new channel not already in the system, create a custom Channel Type.

1. Navigate to **Unified Admin → Channel Manager → Channel Type**.
2. Click **New Channel Type**.
3. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | Name of the channel (e.g., `Custom SMS`) |
   | **Media Routing Domain** | Select the MRD for this channel (e.g., Chat, Voice) |
   | **Channel Type Logo** | Upload a logo icon for the channel |

4. Save.

---

## Step 2: Add Channel Provider

The Channel Provider defines the webhook where CCM sends outbound messages to your connector.

1. Navigate to **Channel Manager → Channel Provider** and click **New Channel Provider**.
2. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | Name of the provider (e.g., `Custom SMS Provider`) |
   | **Supported Channel Types** | Select one or more channel types. Custom types created in Step 1 will appear here. |
   | **Provider Webhook** | The webhook URL of your connector service (e.g., `http://my-connector-svc:7000`). For in-cluster services, use the Kubernetes service name. |
   | **Add Custom Attributes** | Add any channel-specific fields (e.g., API keys, tokens). Values are set in Step 3. |

3. Save.

---

## Step 3: Create Channel Connector

The Channel Connector binds a provider to its runtime credential values.

1. Navigate to **Channel Manager → Channel Connector** and click **Create Connector**.
2. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | Name for this connector instance |
   | **Channel Provider Interface** | Select the Channel Provider created in Step 2 |

3. The custom attribute fields defined in Step 2 will appear — fill in their values (e.g., API key, token).
4. Save.

---

## Step 4: Create New Channel

The Channel connects the connector to a routing queue and defines operational behavior.

1. Navigate to **Channel Manager → Channel** and click **New Channel**.
2. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Name** | Channel name |
   | **Service Identifier** | Unique identifier for this channel (e.g., phone number, page ID, username) |
   | **Bot ID** | Bot associated with this channel for self-service routing |
   | **Response SLA** | Seconds before an unanswered request is re-routed |
   | **Channel Connector** | Select the connector created in Step 3 |
   | **Customer Activity Timeout** | Seconds of inactivity before the session expires |
   | **Channel Mode** | `HYBRID` (recommended) |
   | **Agent Selection Policy** | `LONGEST AVAILABLE` |
   | **Agent Request TTL (sec)** | Time before an unaccepted agent request expires |
   | **Routing Mode** | `PUSH` or `PULL` |
   | **Default Queue / List** | Queue (Push mode) or List (Pull mode) |
   | **Route To Last Agent** | Toggle to route returning customers to their previous agent |
   | **Default Outbound Channel** | Toggle to make this the default channel for outbound messages |

3. Save.

---

## Step 5: Create Customer Schema Attribute for Channel Identification

Associate customers with this channel so CX can identify them when they reconnect.

1. Navigate to **Unified Admin → Customer Schema**.
2. Click **Create New Attribute**.
3. Fill in the fields:

   | Field | Value |
   |---|---|
   | **Label** | Attribute name (e.g., `custom-sms-id`) |
   | **Description** | Brief description of this attribute |
   | **Field Type** | `String` |
   | **Number of Characters** | Maximum value length |
   | **Mandatory Attribute** | Check if this field must always have a value |
   | **PII** | Check if this is personally identifiable information (will be encrypted) |
   | **Channel Identifier** | Check this and select the channel created in Step 4 |

4. Save.

---

## Next Steps

With the connector registered, implement the message exchange between your connector and CCM following the [Channel Connector Developer Guide](Channel-Connector-Developer-Guide.md) and the [CIM Messages](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md) schema reference.

## Related Articles

- [Channel Connector Developer Guide](Channel-Connector-Developer-Guide.md)
- [Channel and Connector Setup](../Administrator/Channel-and-Connector-Setup.md)
- [CIM Messages](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md)
