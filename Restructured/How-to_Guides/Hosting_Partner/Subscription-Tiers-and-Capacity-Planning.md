---
title: "Subscription Tiers & Capacity Planning"
summary: "Reference guide to ExpertFlow CX subscription tiers, included products, concurrent agent limits, and guidance for helping customers choose the right plan."
audience: [hosting-partner]
product-area: [licensing, platform]
doc-type: reference
difficulty: beginner
last-updated: 2026-03-14
---

# Subscription Tiers & Capacity Planning

ExpertFlow CX is sold as a subscription service. As a Reseller, you are responsible for matching customers to the right tier and planning for capacity growth over time.

---

## Subscription Tiers

| Tier | Typical Customer | Concurrent Agents | Core Products Included |
|------|-----------------|-------------------|------------------------|
| **Starter** | Small contact centers, pilots | Up to 25 | Unified Admin, Web Widget, Basic Voice, Chat |
| **Professional** | Mid-size operations | Up to 100 | Starter + WhatsApp, Outbound Dialer, Conversation Studio, Reporting |
| **Enterprise** | Large or complex environments | 100+ (custom) | Professional + WFM, AI Co-Pilot, Conversation Search, Multi-language NLU |

> Exact tier limits and included products are defined in your Reseller Partner Agreement. Contact your ExpertFlow account manager for the current commercial schedule.

---

## Concurrent Agent Licensing Explained

ExpertFlow CX licenses by **concurrent agents** — the number of agents actively logged into the system at the same time, not the total number of agent accounts created.

**Example:** A customer with 200 total agents but a peak of 80 agents logged in simultaneously needs a **Professional** tier with an 80-seat concurrent license.

### Planning for Peak Capacity

When scoping a customer's license:

1. **Identify peak hours** — When does the customer have the most agents logged in simultaneously?
2. **Add a buffer** — Plan for 110–120% of current peak to accommodate growth.
3. **Account for supervisors** — Supervisors logged into the Unified Admin also consume a concurrent seat if they are handling interactions.
4. **Per-product consumption** — Each product (Voice, Outbound, WFM) consumes licenses independently. An agent active on both Voice and Chat counts as one concurrent agent overall, but both MRDs must have capacity.

---

## Add-On Products

The following products can be added to any tier:

| Product | Description | Typical Buyer Signal |
|---------|-------------|----------------------|
| **Outbound Dialer** | Preview, Progressive, and Predictive dialing | Customer runs outbound campaigns |
| **Workforce Management (WFM)** | Scheduling, adherence, and forecasting | 50+ agents, HR-driven scheduling |
| **Conversation Search** | Full-text search across interaction transcripts | Quality or compliance teams |
| **AI Co-Pilot** | Real-time agent assistance and suggested responses | High-volume, script-heavy environments |
| **Voice Recording** | Call recording with replay and archival | Regulatory compliance requirements |
| **Multi-language NLU** | Arabic, Urdu, and regional language intent detection | MENA-region deployments |

---

## Upgrading a Subscription

Upgrades take effect immediately once the new license key is uploaded:

1. Agree the new tier or add-on with the customer.
2. Raise an upgrade request via the EF Partner Portal.
3. ExpertFlow issues a new **Master License Key**.
4. Upload the key in **Unified Admin > General Settings > License Info**.

> There is no downtime during an upgrade. The new capacity is available as soon as the key is applied.

---

## Downgrading a Subscription

Downgrades take effect at the next renewal date. ExpertFlow does not issue partial refunds for mid-term downgrades.

If a customer downgrades to a tier with fewer concurrent seats than their current consumption, agents beyond the new limit will be unable to log in after the downgrade takes effect. Plan and communicate this to the customer in advance.

---

## Capacity Planning Checklist

Use this checklist when scoping a new customer:

- [ ] Peak concurrent agents (current)
- [ ] Forecast growth over 12 months
- [ ] Channels required (Voice, Chat, WhatsApp, Email, Social)
- [ ] Outbound dialing required?
- [ ] Compliance/recording requirements?
- [ ] Language and localization needs?
- [ ] Integration with existing CRM or ticketing system?
- [ ] Supervisor headcount (impacts concurrent seat count)

---

## Related Guides

- [Managing Licenses Across Tenants](Managing-Licenses-Across-Tenants.md)
- [License Renewal & Reactivation](License-Renewal-and-Reactivation.md)
- [Reseller Quickstart](Reseller-Quickstart.md)
