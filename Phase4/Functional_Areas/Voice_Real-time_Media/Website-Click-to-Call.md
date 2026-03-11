---
title: "Website Click-to-Call"
summary: "Explanation of website click-to-call using WebRTC in ExpertFlow CX — covering the customer journey improvement, strategic page placement, cost benefits, mobile support, and key metrics."
audience: [decision-maker, solution-admin]
product-area: [voice]
doc-type: explanation
difficulty: beginner
keywords: ["click to call", "website calling", "WebRTC click to call", "browser calling", "customer journey", "conversion", "cart abandonment", "toll-free alternative"]
aliases: ["click-to-call", "web click to call", "website voice button"]
last-updated: 2026-03-10
---

# Website Click-to-Call

Click-to-call lets customers connect to your contact centre directly from your website without dialling a phone number — one click, microphone permission, and they are talking to an agent. The agent sees which page the customer was on, giving them context before the conversation starts.

## The Problem with Traditional Phone Contact

When customers have a question during a purchase or while using a product, the traditional path is:
1. Search the website for a phone number (not always easy to find)
2. Pick up a separate device and dial
3. Navigate IVR menus
4. Wait on hold
5. Explain to the agent what they were doing — from scratch, because all website context is lost

Each step adds friction. Many customers abandon rather than complete this process, especially during purchases.

## How Click-to-Call Solves This

A click-to-call button placed directly on high-intent pages removes the friction:
- The customer clicks the button without leaving the page.
- The browser requests microphone permission once.
- The customer is connected to the right agent within seconds.
- The agent sees which page the customer was viewing and what they were trying to do.
- The conversation starts with context, not from zero.

## Where to Place Click-to-Call

Strategic placement is more important than broad placement. High-value locations include:

| Page Type | Why It Works |
|---|---|
| **Pricing pages** | Customers comparing options often need a conversation to convert |
| **Checkout and cart** | Preventing abandonment at the moment of purchase decision |
| **Product configuration pages** | Complexity drives questions — make it easy to ask |
| **Support documentation** | Provide a path to human help when self-service reaches its limit |
| **Enterprise/solution pages** | B2B buyers want to talk before committing |
| **Exit-intent triggers** | Last-chance offer before the customer leaves the site |

Different buttons on different pages can route to different teams — a button on a product page goes to sales, a button on a support article goes to technical support.

## Cost Benefits

Traditional inbound calls have associated costs:
- Toll-free number charges, particularly for international callers (which can exceed $1/minute)
- IVR infrastructure costs

WebRTC click-to-call uses the customer's internet connection. There are no per-call telephony charges. For organisations with international customer bases, this alone can justify the WebRTC implementation.

## Mobile Support

Click-to-call works on mobile browsers. Customers on a mobile website tap the call button, grant microphone permission, and connect — without leaving the mobile browser to open a phone dialler.

This is particularly effective for location-based services, where a customer finds a business on their mobile browser and wants to call immediately.

## Customer Permission and Privacy

The first click-to-call triggers a browser microphone permission prompt — a browser security requirement that cannot be bypassed. Most customers who actively click the call button grant permission. Typical denial rates are 10–15%.

Always provide a visible fallback (display your phone number) for customers who decline microphone permission.

Customers control their audio at all times. They can mute or end the call from their browser without any override from the agent side.

## Measuring Impact

| Metric | What It Tells You |
|---|---|
| **Page conversion rate** | Compare pages with and without click-to-call — look for measurable lift on key conversion events |
| **Time to connection** | How long from button click to agent answer — should be faster than traditional call routing |
| **Context utilisation** | Do agents reference the page context? Is it useful? |
| **Cost per interaction** | Web-originated calls vs. toll-free charges — compare fully-loaded cost |
| **Customer satisfaction (CSAT)** | Click-to-call customers typically score higher than traditional callers due to reduced friction |

## Technical Implementation Notes

- Your website must have HTTPS enabled — WebRTC requires a secure context and will not work over HTTP.
- Implementation requires adding a JavaScript snippet to relevant pages (similar to analytics tags) and placing the call button HTML elements.
- ExpertFlow handles routing the WebRTC call into your contact centre infrastructure once the browser establishes the connection.
- Geofencing by IP is available if you need to restrict click-to-call to specific regions or countries.
- Abuse prevention options include email verification before calling, CAPTCHA on the call button, or usage monitoring.

## Queue Behaviour

If all agents are busy when a customer clicks to call, the customer enters a queue — the same behaviour as any inbound call. You can configure:
- Estimated wait time announcements
- Callback options (customer leaves number; platform calls them back when an agent is free)
- Alternative self-service paths

## Related Articles

- [Browser-Based Calling](Browser-Based-Calling.md)
- [WebRTC for CX](WebRTC-for-CX.md)
- [Video Customer Support](Video-Customer-Support.md)
- [Inbound Calls](Inbound-Calls.md)
- [Customer Widget Features and Capabilities](../../Solution_Admin/Customer-Widget-Features-Capabilities.md)
- [Web App Calls Overview](../../Solution_Admin/Web-App-Calls-Overview.md)
