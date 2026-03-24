---
title: "CX Voice Deployment Overview"
summary: "High-level architectural overview and deployment sequence for the Voice components of ExpertFlow CX."
audience: [hosting-partner]
product-area: [voice]
doc-type: explanation
difficulty: intermediate
aliases: []
last-updated: 2026-03-11
---

# CX Voice Deployment Overview

ExpertFlow CX Voice is a multi-component subsystem that enables IVR, Inbound, and Outbound calling. This guide provides the recommended deployment sequence and links to the specific component setup guides.

## 1. Component Architecture

The Voice subsystem consists of four primary layers:

| Component | Responsibility | Deployment Type |
| :--- | :--- | :--- |
| **Media Server (EFSwitch)** | Call handling, RTP processing, and IVR execution. | Linux VM / Bare Metal |
| **Voice Connector** | Bridge between Media Server and the CX Core. | Docker Container |
| **Outbound Dialer** | Campaign management and proactive dialing logic. | Docker Container |
| **Recording Services** | SIPREC-based call recording and storage. | Docker/Kubernetes |

---

## 2. Recommended Deployment Sequence

To ensure proper service discovery and connectivity, components should be deployed in the following order:

1.  **Media Server (EFSwitch):** Install the core telephony engine first.
    *   [Installation Guide](CX-SIP-Proxy-Installation-Guide.md)
2.  **ExpertFlow CX Core:** Ensure the main platform is operational on Kubernetes.
    *   [Helm-Based Deployment](Helm-Based-Application-Deployment.md)
3.  **Voice Connector:** Deploy the bridge to connect the Media Server to the CX Core.
    *   [Voice Connector Deployment Guide](Voice-Connector-Deployment-Guide.md)
4.  **Outbound Dialer (Optional):** Deploy if proactive campaign features are required.
    *   [CX Dialer Deployment Guide](CX-Dialer-Deployment-Guide.md)
5.  **Recording Components (Optional):** Deploy if quality management/auditing is required.
    *   [Voice Recording Components Deployment](Voice-Recording-Components-Deployment.md)

---

## 3. Post-Deployment Configuration

Once the infrastructure is deployed, the **Solution Admin (Olivia)** must configure the business logic in the Unified Admin:

*   **Voice Channel Setup:** Map the Media Server to a specific CX channel.
    *   [CX Voice Channel Configuration Guide](../Administrator/Voice-Channel-Configuration-Limitations.md)
*   **Extension Mapping:** Assign Agent extensions to the Media Server.
    *   [Media Server Configuration Reference](../Administrator/Media-Server-Configuration-CX-Voice.md)
