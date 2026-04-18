---
title: "Agent SLA Limitations"
summary: "Known limitations of the Agent SLA feature in ExpertFlow CX — covering wrap-up interaction with multi-agent SLA and the absence of default thresholds for color and popup actions."
audience: [supervisor-qa]
product-area: [channels, digital]
doc-type: reference
difficulty: intermediate
keywords: ["agent SLA limitations CX", "SLA wrap-up CX", "multi-agent SLA CX", "SLA timer CX limitations", "agent SLA color threshold CX", "SLA popup CX", "agent SLA known issues CX"]
aliases: ["agent SLA known issues CX", "SLA limitations CX", "agent SLA limitations"]
last-updated: 2026-03-10
---

# Agent SLA Limitations

The following known limitations apply to the Agent SLA feature in ExpertFlow CX.

## Known Limitations

### 1. Wrap-up Stops SLA in Multi-Agent Conversations

**Affects:** CX 4.5 and later

When an agent applies a **wrap-up** to a conversation, the system sends the wrap-up as an agent message. In multi-agent scenarios (e.g., consult or conference), this has the following side-effect:

- If one agent leaves the conversation and provides a wrap-up, the system treats it as an agent message.
- This **stops the Agent SLA timer** for all other agents still active in the conversation — even though those agents have not yet responded to the customer.

**Impact:** In consult or conference scenarios, the SLA may be marked as met prematurely when only one of the participating agents has wrapped up.

---

### 2. No Default Thresholds for Color Change and Popup Actions

By default, the system does **not** configure threshold values for the **Change Color** and **Show Popup** SLA actions.

These actions must be configured explicitly using the API. There is no UI-based default configuration for these thresholds in the current release.

---

## Related Articles

- [Customer Inactivity SLA](Customer-Inactivity-SLA.md)
- [SLA Calculations](SLA-Calculations.md)
- [Understanding Response SLA](../Agent/Understanding-Response-SLA.md)
