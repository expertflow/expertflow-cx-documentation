---
audience: [administrator]
doc-type: reference
difficulty: beginner
aliases: []
---

# Infrastructure Sizing Guidelines

This guide provides estimated capacity planning for Expertflow CX deployments based on communication volume, agent concurrency, and channel types.

## Voice Channel Sizing
For accurate sizing of voice traffic (inbound and outbound), consider the following parameters:

| Parameter | Description |
| :--- | :--- |
| **Call Arrival Rate** | Expected calls arriving per hour. |
| **Peak Call Volume** | Highest expected volume during peak periods. |
| **Average Handle Time (AHT)** | Average duration of a call including wrap-up. |
| **Service Level Targets** | Target answer rates (e.g., 80% in 20 seconds). |
| **Agent Capacity** | Total available agents and their skill levels. |
| **Call Concurrency** | Number of simultaneous live voice calls. |
| **Trunk/Port Requirements** | Telephony channels needed to avoid blocking. |

## Digital Channel Sizing (Chat, SMS, WhatsApp)
Key parameters for identifying prerequisites for digital channels:

| Parameter | Description |
| :--- | :--- |
| **Agent Concurrency** | Number of simultaneous chat sessions an agent can handle (typically 1-5). |
| **Daily Message Volume** | Expected total messages per day. |
| **Peak Traffic** | Maximum concurrent chats during peak hours. |
| **Message Frequency** | Average number of messages per session (impacts bandwidth). |
| **Integration Overhead** | Load from Bot or CRM backend lookups. |

*Note: These guidelines are for internal capacity planning and should be reviewed by technical leads for production deployments.*
