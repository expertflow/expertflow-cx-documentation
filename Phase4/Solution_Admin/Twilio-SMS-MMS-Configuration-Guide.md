---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Twilio SMS / MMS Connector Configuration

Expertflow CX utilizes Twilio Messaging-X to support SMS and MMS interactions alongside WhatsApp within a single connector.

## 1. Twilio Account Setup
1. Create a project at [Twilio Console](https://console.twilio.com).
2. **Phone Number**: Purchase an active number. Ensure it has the **SMS and MMS icons** next to it. (US/Canada numbers are recommended for global reach).
3. **Webhook Binding**:
   - In your active number settings, under **Messaging**, select "Webhook".
   - **URL**: `{FQDN}/twilio-connector/twilio-msg/receive`.
   - **Method**: POST.

## 2. Unified Admin Configuration

### Channel Provider
- **Provider Webhook**: `http://ef-twilio-connector-svc:8080` (K3s).
- **Custom Attributes**:
  - `TWILIO_ACCOUNT_SID`: Found in your Twilio Console.
  - `TWILIO_AUTH_TOKEN`: Found in your Twilio Console.

### Channel Connector
- Use the SID and Token from the specific account or sub-account tied to your phone number.

### Channel (SMS)
- **Service Identifier**: The active phone number (e.g., `+1234567890`).
- **Channel Type**: Select `SMS`.

## 3. Testing
- **Twilio Dev-Phone**: Use this for basic SMS testing if you don't have a physical device in the target region.
- **MMS Testing**: Use the Twilio API Explorer to send media URLs and verify they appear in the Agent Desk.

## 4. WhatsApp Sandbox (Optional)
To test WhatsApp for free:
1. Use the "Try it out" section in Twilio Messaging.
2. Set the sandbox webhook to `{FQDN}/twilio-connector/twilio-msg/receive`.
3. Use the `whatsapp:+1234567890` format for the Service Identifier in the WhatsApp channel config.

*Note: In production, switch to a Paid WhatsApp Sender via the Twilio Messaging menu.*

---

## Related Articles
- [Routing Strategy: Pull Mode](./Routing-Strategy-Pull-Mode.md)
- [WhatsApp Channel Overview](../Functional_Areas/Digital_Channel_Management/WhatsApp-Channel-Overview.md)
- [Channel and Connector Setup](Channel-and-Connector-Setup.md)
*
