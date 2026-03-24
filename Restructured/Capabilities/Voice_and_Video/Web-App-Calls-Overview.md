---
doc-type: explanation
difficulty: beginner
aliases: []
---

# Web and App Calls Overview

Expertflow CX allows customers to initiate voice and video calls directly from your website or mobile app without using a traditional phone line.

## Overview
Using WebRTC, customers can reach your contact center through a widget embedded in your digital platforms. These calls are routed to agents in Agent Desk just like standard PSTN calls.

## Comparison: Voice vs. Web & App Calls

| Feature | Voice Calls (PSTN) | Web & App Calls |
| :--- | :--- | :--- |
| **Origin** | Landline or Mobile Phone | Website or Mobile App |
| **Connection** | SIP Trunk / PSTN | WebRTC (Internet) |
| **Video/Screen Share** | No | Yes |
| **Agent Interface** | Agent Desk | Agent Desk |

## Key Capabilities

### Customer Experience
- **Widget Customization**: Change colors, branding, and placement.
- **Multimedia**: Choose between voice-only, video, or screen sharing.
- **Contextual Data**: Pass customer data from the web session directly to the agent.

### Agent Experience
- **Full Call Control**: Answer, hold, mute, and transfer.
- **Video Interaction**: Toggle video on/off as needed.
- **Screen View**: View the customer's shared screen for technical support.

## Configuration Steps
1. **Media Server**: Deploy and configure for WebRTC/ICE support.
2. **Unified Admin**: Configure the "Web & App Calls" channel and assign it to a queue.
3. **Widget Deployment**: Embed the Expertflow widget on your site or in your app.
4. **Skills**: Assign agents to the specific queues created for these digital calls.
