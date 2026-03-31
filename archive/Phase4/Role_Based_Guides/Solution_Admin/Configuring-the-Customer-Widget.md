---
title: "Configuring the Customer Widget"
summary: "Guide for Solution Admins to customize the appearance, branding, and behavior of the web-based customer chat interface."
audience: [admin]
product-area: [widget, channels]
doc-type: how-to
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Configuring the Customer Widget

As a Solution Admin (Olivia), you can create multiple visual themes and behavioral configurations for your web-based chat interface. This allows you to provide different experiences for your public website vs. your private partner portal.

## 1. Creating a Widget Instance
1.  Open **Unified Admin** and go to **Channel Manager > Create Web Widget**.
2.  **Widget Identifier:** Enter a unique code (e.g., `support-portal`). This code is used by developers to embed the correct widget on your site.

## 2. Visual Customization
- **Widget Title & Subtitle:** Set the main headings (e.g., "Chat with Support").
- **Color Palette:** Choose your brand's accent colors.
- **Language:** Select the default language from your platform's locale settings.
- **Font Size:** Enable or disable the user's ability to adjust text size.

## 3. Behavioral Features
You can enable advanced interaction options for the customer:
- **File Transfer:** Allow customers to upload screenshots or documents.
- **Emoji Support:** Enable expressive chat interactions.
- **Download Transcript:** Allow customers to save their conversation history once finished.
- **WebRTC:** Enable the "Call" button to allow customers to initiate audio/video calls directly from the browser.

## 4. Automation & Notifications
- **Pre-Chat Form:** Select a form (built in Form Builder) to collect customer data before the chat is routed to an agent.
- **Webhook Notifications:** Configure alerts to be sent to your team's Google Workspace or Slack spaces when a new session starts.

---

*For technical embedding instructions, share the [JavaScript SDK for Customer-Facing Channels](../Developer/JavaScript-SDK.md) with your developer.*
