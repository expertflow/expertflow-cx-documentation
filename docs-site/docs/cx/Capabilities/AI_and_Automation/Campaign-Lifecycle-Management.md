---
title: Campaign Lifecycle Management
summary: >
  How ExpertFlow CX automatically starts and stops outbound campaigns based on
  a configured date and time window, removing the need for manual supervisor
  intervention at launch or shutdown.
doc-type: explanation
audience:
  - conversation-designer
  - administrator
product-area:
  - outbound
  - campaign-management
keywords:
  - campaign scheduling
  - start date
  - end date
  - dateTimeBounds
  - campaign lifecycle
  - auto-start
  - auto-stop
last-updated: 2026-06-04
---

# Campaign Lifecycle Management

ExpertFlow CX lets you define a **Start Date/Time** and **End Date/Time** for
any outbound campaign. Once set, the platform automatically begins dialing at
the configured start and ceases all new contact initiation at the configured
end — without a supervisor having to manually publish or stop the campaign at
the exact moment.

---

## How It Works

Campaign lifecycle bounds are enforced by the **START Node** in
Conversation Studio. The START Node acts as the gatekeeper for every pulse
that drives the campaign flow.

### The Pulse Gating Mechanism

The START Node is configured with a `triggerInterval` (how often it fires, in
seconds) and a `dateTimeBounds` object containing `startTime` and `endTime`
values.

On every trigger interval, the START Node evaluates two conditions before
allowing a pulse to propagate downstream:

| Condition | Check |
|---|---|
| **Time window** | Is the current system time ≥ `startTime` **and** ≤ `endTime`? |
| **Campaign status** | Is the campaign status `PUBLISHED`? (verified via `GET /campaigns/campaignfromflowid/{flowId}`) |

If either condition is false, the pulse is suppressed and nothing flows to the
SEIZE or INIT nodes. Agents are not seized, no contacts are loaded, and no
dials are placed.

### What Happens at Start Time

Before the `startTime`, the START Node suppresses every pulse. At the first
trigger interval that falls on or after `startTime`, the pulse is released and
the campaign begins operating normally — agents are seized, contacts are loaded
via the INIT node, and dials are placed.

### What Happens at End Time

When the current system time passes the configured `endTime`, the START Node
permanently stops emitting pulses for that campaign flow — even if the campaign
status is still `PUBLISHED`. No new contacts are passed to the INIT node and
no new agent seize requests are made.

### Graceful Termination

The end-time cutoff applies to **new batches only**. Contacts that are already
in the pipeline — seized, being dialed, or in an active conversation — are
allowed to complete their current step. The platform does not forcefully drop
in-progress interactions when the end time is reached.

---

> **Ready to configure it?** See [Managing Outbound Campaigns](../../How-to_Guides/Administrator/Managing-Outbound-Campaigns.md#set-a-campaign-lifecycle-window) for step-by-step instructions on setting Start and End Date/Time in the Campaign Manager UI.

---

## Business Use Cases

| Scenario | How lifecycle bounds help |
|---|---|
| **Business-hours compliance** | Set end time to 17:00 daily so agents never accidentally dial customers after close of business. |
| **Time-boxed promotion** | A 3-day sale campaign starts and ends automatically without supervisor action. |
| **Overnight digital campaigns** | An SMS blast runs from 08:00 to 20:00 each day while voice campaigns idle — no manual scheduling needed. |
| **Regulatory compliance** | Enforce TCPA or Ofcom "permitted hours" constraints at the flow level, not just through agent discipline. |

---

## Relationship to Time & Day Windows

The START Node supports two complementary scheduling mechanisms:

| Setting | Scope | Purpose |
|---|---|---|
| **Campaign Lifecycle Bounds** (`dateTimeBounds`) | The entire campaign lifespan | Defines the outer date-range envelope — when the campaign is eligible to run at all |
| **Time & Day Windows** | Repeating intraday/weekly schedule | Restricts pulses to specific times of day or days of the week within the lifecycle envelope |

Use both together for full control: lifecycle bounds to define the campaign
window (e.g., June 12–15), and time/day windows to restrict dialing to
business hours within that window (e.g., 09:00–17:00 weekdays only).

---

## Limitations

- **Pulse-interval resolution.** The end time is enforced at the next trigger
  interval evaluation, not at the exact millisecond. A campaign with a
  10-second trigger interval may run up to 10 seconds past the configured end
  time before the pulse is suppressed.

- **In-flight contacts are not interrupted.** Graceful termination means
  contacts already seized or being dialed when end time is reached will
  complete their current step. If your campaign has a long INIT batch or long
  call durations, activity may continue briefly beyond end time.

- **Published status alone is not sufficient past end time.** After the end
  time passes, a `PUBLISHED` campaign will not emit pulses. To restart a
  campaign whose end time has elapsed, update the `endTime` to a future value
  before republishing.

- **No auto-republish.** The system does not automatically re-publish a
  campaign when the start time arrives. The campaign must already be in
  `PUBLISHED` status before `startTime` for lifecycle gating to take effect.
  Publishing at or after the start time is valid — pulses begin on the next
  trigger interval after publication.

- **System clock dependency.** Lifecycle bounds rely on the server-side system
  clock. Clock drift between nodes is not compensated for. For campaigns where
  the cutoff window must be precise to the second, verify NTP synchronisation
  across your cluster.

- **One-time range only.** Each campaign can hold one `dateTimeBounds` range.
  If you need a campaign to run during multiple disjoint windows (e.g.,
  weekdays only across several weeks), use the Time & Day Windows setting in
  combination with a broad lifecycle range, or create separate campaign
  instances per window.

---

## Frequently Asked Questions

**Does setting an end time pause or stop the campaign permanently?**

It suppresses new pulses — the campaign remains in `PUBLISHED` status but
no new contacts are initiated. The campaign is not moved to a `Stopped` state
automatically. You can update the end time and the campaign will resume on the
next valid pulse interval.

**What happens if I publish a campaign after its end time has already passed?**

The START Node will evaluate `dateTimeBounds` on the first pulse and find the
current time is past `endTime`. The pulse will be suppressed and the campaign
will produce no dials. Update the end time to a future value before publishing.

**Can I set a start time without an end time, or vice versa?**

Yes. If only a start time is set, the campaign begins automatically at that
time and runs indefinitely (until manually stopped or ended). If only an end
time is set, the campaign starts as soon as it is published and stops
automatically at the configured end time.

**What happens to agents who have seized contacts when the end time is reached?**

Seized agents will complete their current in-progress interaction. The platform
does not interrupt active conversations. However, no new seize requests are
made after the end time, so agents will not receive new contacts for this
campaign.

**Does the end time apply to retry logic in the flow?**

Yes. Retry paths in your flow (e.g., looping a contact back to the Dial node
after a busy signal) depend on the START Node emitting the next pulse. Once
end time is reached, no new pulses are emitted, so no new retry batches are
initiated.

**Can I change the start or end time while the campaign is already running?**

Yes. You can edit the campaign and update the `dateTimeBounds` while it is
published. The START Node picks up the new values on the next trigger interval
evaluation.

**How does this interact with the "Stopped" campaign status?**

`Stopped` is a permanent terminal state — a stopped campaign cannot be
republished regardless of lifecycle bounds. Lifecycle bounds only gate pulses
on `PUBLISHED` campaigns. If you want to re-run a campaign, create a new one.

---

## Related Pages

- [Campaign Manager Solution](../../Solutions/Campaign_Manager/index.md) —
  complete outbound solution overview
- [Managing Outbound Campaigns](../../How-to_Guides/Administrator/Managing-Outbound-Campaigns.md) —
  step-by-step configuration guide
