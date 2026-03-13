---
audience: [solution-admin]
doc-type: reference
difficulty: beginner
aliases: []
---

# Customer Widget: Features and Capabilities

The Expertflow Customer Widget provides a responsive, customizable interface for customers to engage with the contact center via web chat and voice/video escalation.

## Key Capabilities

### 1. Dynamic Pre-Chat Forms
Collect customer data before the session starts. Identification is driven by the `CHANNEL_IDENTIFIER` (email or phone). This data is automatically mapped to the CX Customer Profile.

### 2. Rich Messaging
- **Plain Text**: Up to 4096 characters.
- **Interactive Buttons**: Guidance from bots for quick actions.
- **Carousel Messages**: JSON-structured horizontal scrolling options.
- **File Sharing**: Support for images (png, jpg), documents (pdf, docx), audio (mp3), and video (mp4) with clickable previews.

### 3. Engagement Features
- **Business Hours**: Displays opening/closing status on the entry screen.
- **Notifications**: Browser and sound alerts for new messages, even when the tab is inactive.
- **Typing Indicators**: Visual feedback when an agent is responding.
- **Delivery Status**: Single/Double tick indicators for "sent," "delivered," and "read."

### 4. Accessibility and RTL Support
- **Font Resizing**: Options for small, medium, and large (12px, 14px, 16px).
- **RTL Support**: Native rendering for Arabic, Urdu, and other right-to-left languages based on browser settings.

### 5. Call Escalation (WebRTC)
Customers can escalate a chat to an **Audio or Video Call** directly within the widget. Agents can also push a secure video link to the customer during a session.

### 6. Transcripts
Upon session completion, customers can download a full chat transcript including multimedia and notification history.
