# CX Knowledgebase : Cisco Connector

The Cisco Connector enables smooth integration between Cisco Contact Center and the EF CX Platform by capturing Cisco call events in real time, correlating them with call records from the Cisco CC database, and forwarding conversation activity into CX. This allows CX components to use the conversation based on the call data from Cisco.

* * *

## Purpose and Functionality

  * Listens to Cisco JTAPI events and captures every call leg in real time as it happens on the Cisco Contact Center.

  * Correlates captured call legs against Cisco CC database records (TCD rows) to enrich them with agent details, wrap-up codes, and call outcome information.

  * Forwards enriched conversation events (call started, call ended, wrap-up) to the EF CX Platform for downstream processing.

  * Normalizes customer phone numbers from local format to international format so they can be correctly delivered to WhatsApp or SMPP connectors for post-call surveys.




* * *

## Operational Flow

  * As calls are handled by Cisco agents, the connector captures each call leg via JTAPI and stores it locally.

  * A background job runs at a configurable interval, fetching unprocessed call legs in batches and matching them against Cisco CC database records to validate and enrich the data.

  * Once a call is fully correlated and validated, the connector builds CIM-compatible conversation events and sends them to the EF CX Platform's Conversation Manager.

  * The customer's phone number is normalized to international format (e.g., `03001234567` → `923001234567`) using configurable country code and local prefix settings, ensuring compatibility with WhatsApp and SMPP gateways.

  * Agent identity is resolved against Keycloak to associate the correct agent profile with each conversation event.




* * *

## Use Case Example

A Cisco agent completes a call with a customer. The Cisco Connector captures the call, correlates it with the Cisco CC database record to get the agent name, wrap-up code, and call outcome, then forwards the conversation events to CX (keycloak for agent creation and then Conversation Manager for conversation creation).

* * *

## Expected Behavior

  * Supports **inbound and outbound** call flows.

  * Each call may consist of **multiple legs** (e.g., consult, transfer, conference). The connector correlates and processes all legs together as a single conversation.

  * If a call leg cannot be matched to a Cisco CC record yet (e.g., the record is not yet written to the database), it is skipped and retried in the next batch interval.

  * **Wrap-up codes** captured by the agent on Cisco are included in the conversation events sent to CX.

  * If `CUSTOMER_COUNTRY_CODE` is not configured, phone number normalization is disabled and numbers are forwarded as-is.

  * Numbers already in international format (e.g., `923001234567` or `+923001234567`) are detected automatically and passed through unchanged to prevent double-prefixing.




* * *

## Deployment

To deploy the Cisco Connector in the CX Solution, follow the steps in the [Deployment Guide - Cisco Connector](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/1777008642/Deployment+Guide+-+Cisco+Connector).
