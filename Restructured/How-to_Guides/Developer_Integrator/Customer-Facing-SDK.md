---
title: "Customer-Facing SDK for Omnichannel Communication"
summary: "Overview of the ExpertFlow CX Customer-Facing SDK — enabling developers to embed web chat, audio calls, video calls, and screen sharing into mobile and web applications using a custom UI backed by the SDK."
audience: [developer-integrator]
product-area: [sdk, channels]
doc-type: explanation
difficulty: intermediate
keywords: ["customer facing SDK CX", "omnichannel SDK CX", "web chat SDK CX", "video call SDK CX", "mobile SDK CX", "customer widget SDK CX", "ExpertFlow SDK"]
aliases: ["CX customer SDK", "omnichannel communication SDK CX", "chat SDK CX"]
last-updated: 2026-03-10
---

# Customer-Facing SDK for Omnichannel Communication

The ExpertFlow CX Customer-Facing SDK enables developers to embed real-time communication features — web chat, audio calls, video calls, and screen sharing — into mobile (native or hybrid) and web applications.

The SDK handles the backend communication with ExpertFlow CX while allowing developers to build and use a **fully custom user interface**.

---

## Supported Capabilities

| Capability | Status |
|---|---|
| Web Chat | Available |
| Audio Calls (WebRTC) | Available |
| Video Calls (WebRTC) | Available |
| Screen-sharing Calls | Available |
| Contact Center Stats (queue depths, wait times) | Roadmap |
| Contact Center Availability Timings | Roadmap |
| Agent Availability Check | Roadmap |
| Expected Waiting Time | Roadmap |

---

## Integration Options

### Web Application — CDN

Add the SDK directly to your web app via a CDN script tag:

```html
<!-- Standard -->
<script src="https://cdn.jsdelivr.net/gh/expertflow/sdk-for-customer-facing-channels@latest/sdk.js"></script>

<!-- Minified -->
<script src="https://cdn.jsdelivr.net/gh/expertflow/sdk-for-customer-facing-channels@latest/sdk.min.js"></script>
```

### Mobile / Web Application — NPM

Install via NPM for native or hybrid mobile apps:

```bash
npm i @expertflow/sdk-for-customer-facing-channels
```

Full NPM package reference: `https://www.npmjs.com/package/@expertflow/sdk-for-customer-facing-channels`

---

## Use Cases

- **Custom chat widget**: Embed a branded chat experience in your website or mobile app without using the standard ExpertFlow widget.
- **In-app calling**: Add WebRTC audio/video call capability to a mobile app using the SDK's call controls.
- **Omnichannel customer experience**: Enable customers to switch between chat and voice within a single app session.

---

## Developer Guide

For the full developer guide, SDK function reference, configuration parameters, WebRTC setup, and event listeners, see the [JavaScript SDK for Customer-Facing Channels](JavaScript-SDK.md).

---

## Related Articles

- [JavaScript SDK for Customer-Facing Channels](JavaScript-SDK.md)
- [Customer Widget Features and Capabilities](../Administrator/Customer-Widget-Features-Capabilities.md)
- [WebRTC Configuration Guide](../Administrator/WebRTC-Configuration-Guide.md)
- [CIM Messages](../../Reference/Schemas_and_Data_Model/CIM_Message_Schema/CIM-Messages.md)
