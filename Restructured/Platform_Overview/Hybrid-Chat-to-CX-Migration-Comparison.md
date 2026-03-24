---
audience: [platform-overview]
doc-type: explanation
difficulty: beginner
aliases: []
---

# Comparing Hybrid Chat 3.x and Expertflow CX

This document highlights the architectural and functional differences between the legacy Hybrid Chat 3.x and the modern Expertflow CX platform.

## Summary at a Glance

| Feature | Hybrid Chat 3.x | Expertflow CX |
| :--- | :--- | :--- |
| **Scope** | Digital add-on for Cisco | Full Contact Center Platform |
| **Voice** | Relies on Cisco UCCE/X | Native Voice (SIP/WebRTC) |
| **Architecture** | Docker-based (Single) | Microservices (Kubernetes) |
| **Tenancy** | Single-tenant | Multi-tenant |
| **Capabilities** | Chat, WhatsApp, Social | Voice, Digital, AI, QM, WFM, Surveys |

## Key Platform Shifts

### From Add-on to primary Platform
Hybrid Chat 3.x was a digital engagement layer extending Cisco. Expertflow CX is a complete CX suite that can run **standalone** or as an overlay to Cisco, adding AI and analytics.

### Integrated Voice & Recording
Unlike 3.x, Expertflow CX includes a native voice stack with integrated recording, which enables automated Quality Management (QM) across 100% of interactions.

### AI Orchestration
CX introduces **Conversation Studio** (low-code flow design) and **Agent Assist** (real-time transcription/translation), moving beyond the basic chatbot integration of 3.x.

## Migration Note
Moving from 3.x to CX is a **platform upgrade**, not a simple version update. While all digital channels from 3.x are preserved, CX introduces entirely new layers for Voice, QM, WFM, and Omnichannel Surveys.
