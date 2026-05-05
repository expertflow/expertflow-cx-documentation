---
title: "Making an Outbound Contact"
summary: "How to initiate outbound voice calls, WhatsApp messages, and SMS from the Agent Desk."
audience: [agent]
product-area: [platform]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-05-04
---

# Making an Outbound Contact

Agents can initiate contact with a customer even when no conversation is currently active. The `+` icon at the top of the Agent Desk opens the outbound panel, which lets you dial a number or pick a customer from the Customer List.

Outbound is currently supported on three channels: **Voice**, **WhatsApp**, and **SMS**.

---

## Make an Outbound Call (Voice)

**Before you start:** Ensure you are connected to EFSWITCH. Outbound calls cannot be placed without this connection.

1. Click the **`+`** icon at the top of the Agent Desk.
2. Choose **Dial a Number** or select an existing customer from the Customer List.
3. Enter the customer's phone number, or click the **Voice** button against a customer record.
4. Click **Dial** to initiate the call.
5. Wait for the customer to answer.

Once connected, the Conversation View opens and the CTI toolbar appears with three call controls: **Mute/Unmute**, **Hold/Resume**, and **End**.

On initiating the call, your Voice MRD state automatically switches to **Not Ready** so no inbound call conflicts with your outbound session.

**Calling during an active chat:** You can also place a voice call while already in a chat conversation (WhatsApp, web, or any other channel). Follow the same steps above. Once connected, the voice session appears in the **Active Channels Pane** on the right-hand panel.

### Limitations
- Special characters are not supported when dialling numbers, except `*`, `#`, and `+`.
- Agent-to-agent manual outbound calls are not supported.
- Direct extension-to-extension calls are not supported.
- If the customer declines the call, a notification is received from Sip.js and your Agent State is set to **Not Ready**.
- Ringing and voicemail tones depend on the network provider. If the provider does not offer these tones, the system cannot generate them independently.

---

## Make an Outbound WhatsApp Message

### When there is no active conversation

1. Click the **`+`** icon at the top of the Agent Desk.
2. Search for the customer in the Customer List that opens.
3. Click the contact icon against the customer record.
4. In the Conversation View, expand the right panel and click the **WhatsApp** channel icon.
5. Send your message to initiate the conversation.

If you enter an invalid number, only the option to create a new customer record will appear.

### When there is an active conversation

1. Expand the right-side panel and open the **Media Channels** pane.
2. Select the channel identity (phone number) for the WhatsApp channel.
3. Click the dropdown and select the **chat icon** against **WhatsApp**.

This starts a new WhatsApp session alongside the existing conversation.

### Limitations
- A customer session with the business must have occurred within the last **24 hours** to initiate a new WhatsApp conversation.
- After the 24-hour window, template messages (purchased from WhatsApp) are required to reach the customer.
- If the customer does not reply within the channel timeout configured by your administrator, the conversation closes automatically.

---

## Send an Outbound SMS

**Prerequisite:** The SMS channel must be configured via Twilio and enabled in **Unified Admin → Agent Desk Settings**.

1. Click the **SMS icon** at the top of the Agent Desk (beside the `+` button).
2. Enter the customer's phone number, including the country prefix (default prefix is `+1`).
3. Type your message and send.

Your administrator can configure the default prefix and choose whether the SMS dialog closes automatically after sending.

### Limitation
- This feature works only when the SMS channel is configured via Twilio.
