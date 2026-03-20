---
title: "Handling Your First Call"
summary: "Step-by-step tutorial for agents handling their first inbound voice call in ExpertFlow CX — from logging in and setting state through call controls, transfer, and wrap-up."
audience: [agent]
product-area: [voice, agent-desk]
doc-type: tutorial
difficulty: beginner
keywords: ["first call", "inbound call tutorial", "agent voice call", "CTI controls", "answer call", "wrap-up voice", "agent onboarding"]
aliases: ["agent first call", "handle a voice call", "inbound call agent guide"]
last-updated: 2026-03-21
---

# Handling Your First Call

This tutorial walks you through a complete inbound voice call from start to finish — logging in, making yourself available, answering the call, using the controls mid-call, and completing wrap-up. By the end you will have handled a full call cycle in ExpertFlow CX.

---

## Before You Start

Confirm the following with your administrator before your first shift:

- Your user account is active in Unified Admin and your agent extension is registered.
- You know your login URL and credentials.
- Your headset or soft phone is connected and tested.
- You are assigned to at least one voice queue.

---

## Step 1 — Log In to Agent Desk

1. Open the Agent Desk URL provided by your administrator in a supported browser (Chrome recommended).
2. Enter your credentials and complete MFA if prompted.
3. The Agent Desk loads with your status set to **Not Ready** by default — you will not receive calls yet.

---

## Step 2 — Set Your State to Ready

You must be in a **Ready** state to receive inbound calls.

1. Locate the **Presence / State** control in the top bar or sidebar.
2. Click it and select **Ready** (or the equivalent label your team uses).
3. Your status indicator turns green. You are now in the routing pool and eligible to receive calls.

> If you need a moment before taking calls — for example, to review notes — use a **Not Ready** reason code rather than staying logged out. This is tracked differently in reporting.

---

## Step 3 — Receive an Inbound Call

When a customer call is routed to you, an incoming call notification appears in the Agent Desk showing:

- **Queue name** the call came from
- **Customer phone number** (ANI) and name if the customer profile is recognised
- **Wait time** — how long the customer has been in queue

Click **Accept** (or answer your physical/soft phone extension) to connect.

The **CTI toolbar** appears automatically once the call is live. You can drag it to any position on screen or pin it to the side panel.

---

## Step 4 — Handle the Call

During the call you have the following controls available in the CTI toolbar:

| Control | When to use |
| --- | --- |
| **Mute / Unmute** | Toggle your microphone — use when consulting notes or a colleague without the customer hearing |
| **Hold / Resume** | Place the customer on hold while you look something up; hold music plays on their end |
| **DTMF Dialpad** | Send tones if you need to navigate an external IVR or conference bridge |
| **Consult** | Start a private call to another agent without the customer hearing |
| **Conference** | Add your consulted colleague into the call as a three-way conversation |
| **Transfer** | Hand the customer to another agent or queue |
| **End Call** | Disconnect after the customer issue is resolved |

### Putting a Call on Hold

1. Click **Hold** — a hold timer starts and the customer hears hold music.
2. Look up the information you need.
3. Click **Resume** — the timer stops and you are reconnected with the customer.

### Transferring a Call

If you need to pass the customer to a colleague or a different team:

1. Click **Consult** and dial the destination agent or queue.
2. Brief the destination agent while the customer is on hold.
3. Click **Consult Transfer** to complete the handoff and disconnect yourself.

> For an immediate handoff without briefing the destination, use **Blind Transfer** instead. The customer is transferred instantly.

---

## Step 5 — End the Call

Once the issue is resolved:

1. Say goodbye and click **End Call**.
2. Your state changes automatically to **Wrap-up** — no new calls arrive during this time.

---

## Step 6 — Complete Wrap-up

Wrap-up is where you record the outcome of the call for reporting and future agent reference.

1. Click the **Notes** icon in the toolbar to open the wrap-up panel.
2. Select a **Category** (e.g., Billing, Technical Support).
3. Select a **Reason** (e.g., Issue Resolved, Escalated, Follow-up Required). You can apply up to five codes.
4. Type a brief note in the **Notes** field summarising what was discussed and resolved. Notes are internal — the customer never sees them.
5. Click **Submit** (or the equivalent button in your configuration).

Your state returns to **Ready** automatically and you are eligible for the next call.

> If your queue has a **Wrap-up Timer**, you will see a countdown. Complete your codes and notes before it expires — an expired timer closes the interaction without a wrap-up code recorded.

---

## What to Do If Something Goes Wrong

| Symptom | Likely cause | Action |
| --- | --- | --- |
| Call notification appears but no audio | Headset not connected or wrong audio device selected | Check your browser audio settings and headset connection |
| Call rings but drops before you answer | Extension registration issue | Contact your administrator to verify your extension in Keycloak |
| Customer cannot hear you | Microphone muted or browser microphone permission denied | Check the Mute button; check browser permissions |
| Wrap-up panel does not appear | Queue may not require wrap-up | Check with your supervisor — some queues skip wrap-up |

---

## Related Articles

- [CTI Call Controls](../../Functional_Areas/Voice_Real_Time_Media/CTI-Call-Controls.md)
- [Inbound Calls](../../Functional_Areas/Voice_Real_Time_Media/Inbound-Calls.md)
- [Managing Your Presence and States](Managing-Your-Presence-and-States.md)
- [Wrap-up and Follow-up Work](Wrap-up-and-Follow-up-Work.md)
- [Handling Customer Interactions](Handling-Customer-Interactions.md)
