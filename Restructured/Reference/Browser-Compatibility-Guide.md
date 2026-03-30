---
title: "Browser Compatibility Guide"
summary: "Reference guide for supported browsers and known limitations when running ExpertFlow CX Agent Desk, including notification, audio, and WebRTC support per browser."

product-area: [platform]
doc-type: reference
difficulty: beginner
keywords: ["browser compatibility", "supported browsers", "agent desk browser", "WebRTC browser support", "browser notifications CX", "Chrome Firefox Safari Edge agent desk"]
aliases: ["supported browsers", "browser requirements", "agent desk browser support"]
last-updated: 2025-07-14
---

# Browser Compatibility Guide

This guide lists the browsers supported for running ExpertFlow CX Agent Desk and documents known per-browser limitations for notifications, audio, and WebRTC calling.

## Supported Browsers

| Browser | Minimum Version | Agent Desk UI | Browser Notifications | Sound Alerts | WebRTC Calling |
|---|---|---|---|---|---|
| Google Chrome | 90+ | ✅ Full support | ✅ | ✅ | ✅ |
| Microsoft Edge | 90+ | ✅ Full support | ✅ | ✅ | ✅ |
| Mozilla Firefox | 88+ | ✅ Full support | ✅ | ✅ | ✅ |
| Apple Safari | 15+ | ⚠️ Partial — see notes | ⚠️ Partial — see notes | ✅ | ✅ |
| Opera | 76+ | ✅ Full support | ✅ | ✅ | ✅ |

> **Recommended browser**: Google Chrome or Microsoft Edge for the most consistent experience across all Agent Desk features.

## Per-Browser Notes

### Safari
- Browser notifications require macOS 13 (Ventura) or later and Safari 16+. On earlier versions, the Notifications permission prompt does not appear and notifications are silently blocked.
- Safari requires a user gesture (e.g. a click) before it will play audio. If an agent opens Agent Desk without interacting with the page first, the first sound alert may be suppressed.
- On iOS and iPadOS, browser notifications from web apps are only supported on iOS 16.4+ when the site is added to the Home Screen as a Progressive Web App (PWA). Standard browser tabs do not receive notifications on iOS.

### Firefox
- Firefox may show a notification permission prompt differently from Chrome/Edge — it appears as a small icon in the address bar rather than a modal dialog. Agents may miss it if not looking for it.

### Chrome and Edge
- Both browsers may reset site-level notification permissions after a major browser update. If agents report notifications suddenly stopping, re-granting permission via the lock icon in the address bar resolves this.
- Chrome on Android supports browser notifications from Agent Desk when the tab is open in the foreground. Background notification delivery on mobile depends on Android version and battery optimisation settings.

## Unsupported Environments

The following environments are **not supported** for Agent Desk:

- Internet Explorer (any version)
- Browsers in private/incognito mode — notification permissions cannot be persisted and will reset on every session
- Embedded browser views (e.g. inside Electron apps, CRM iframes) — WebRTC and notification APIs may be restricted by the host application

## Related Articles

- [Browser and Sound Notifications](../Capabilities/Digital_Channels/Browser-and-Sound-Notifications.md)
- [Browser-Based Calling](../Capabilities/Voice_and_Video/Browser-Based-Calling.md)
- [WebRTC for CX](../Capabilities/Voice_and_Video/WebRTC-for-CX.md)
