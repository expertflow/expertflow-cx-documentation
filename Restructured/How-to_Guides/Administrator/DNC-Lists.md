---
title: "Do Not Contact (DNC) Lists"
summary: "Explanation of the Do Not Contact (DNC) list system in ExpertFlow CX — covering label-based DNC management, pre-dial scrubbing, granular campaign enforcement, dynamic opt-out mechanisms, external list integration, and regulatory compliance."
audience: [administrator]
product-area: [channels, digital]
doc-type: explanation
difficulty: intermediate
keywords: ["DNC list CX", "do not contact CX", "outbound DNC compliance", "pre-dial scrubbing CX", "opt-out CX", "TCPA compliance CX", "DNC label CX", "campaign suppression CX"]
aliases: ["DNC CX", "do not call list CX", "opt-out management CX"]
last-updated: 2026-03-10
---

# Do Not Contact (DNC) Lists

ExpertFlow CX manages Do Not Contact (DNC) compliance through a **label-based system** within CX Customers. Contacts flagged with DNC labels are automatically suppressed from outbound campaigns before any contact attempt is made.

## How DNC Works

### Label-Based DNC

Administrators define one or more DNC labels and assign them to customer profiles in CX Customers. Labels can represent different opt-out scopes.

**Example labels:**

| Label | Scope |
|---|---|
| `DNC_Global` | Suppressed from all outbound contact |
| `DNC_Sales` | Suppressed from sales campaigns only |
| `DNC_Surveys` | Suppressed from survey campaigns only |

### Pre-Dial Scrubbing

Before any outbound call attempt, the system automatically checks whether the contact has any DNC label associated with the campaign being executed. Contacts flagged with the relevant label are suppressed and never dialed.

### Granular Campaign Enforcement

Each outbound flow is configured to check for specific DNC labels. This allows a contact to opt out of one campaign type while remaining reachable for others.

**Example:** A contact with `DNC_Sales` is suppressed from promotional calls but remains eligible for service notification campaigns.

## Opt-Out Mechanisms

Contacts can be added to a DNC list dynamically:

| Channel | Method |
|---|---|
| **IVR / Bot** | Automated flow captures the request and applies the DNC label using the **Add Contact Label** node in Conversation Studio. |
| **Agent** | During a live conversation, the agent triggers a function on Agent Desk to apply the DNC label to the customer profile. |

The label is applied immediately — the contact is suppressed from future campaigns from that point forward.

## External DNC List Integration

In addition to the internal label system, CX can be configured to validate against **external public DNC lists** for broader regulatory compliance.

Supported regulatory frameworks include:

| Regulation | Region |
|---|---|
| **NDNC** | India |
| **TPS** (Telephone Preference Service) | United Kingdom |
| **TSR** (Telemarketing Sales Rule) | USA |
| **TCPA** (Telephone Consumer Protection Act) | USA |
| **ACMA** | Australia |

## Integration

DNC management integrates with external CRMs, compliance systems, and list management tools via APIs. DNC enforcement is **channel-agnostic** — suppression applies across Voice, SMS, WhatsApp, and all other configured channels.

## Related Articles

- [Managing Outbound Campaigns](Managing-Outbound-Campaigns.md)
- [Customer Interaction Profiles Overview](Customer-Interaction-Profiles-Overview.md)
- [Channel and Connector Setup](Channel-and-Connector-Setup.md)
