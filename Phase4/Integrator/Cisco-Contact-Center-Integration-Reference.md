---
title: "Cisco UCCE/X Integration Reference"
summary: "Technical reference for integrating ExpertFlow CX with Cisco Finesse and Contact Center environments."
audience: [integrator, partner]
product-area: [integrations, voice]
doc-type: reference
difficulty: advanced
aliases: []
last-updated: 2026-03-08
---

# Cisco UCCE/X Integration Reference

ExpertFlow CX integrates seamlessly with Cisco Contact Center Express (UCCX) and Enterprise (UCCE) environments. This integration allows agents to manage digital channels within the Cisco Finesse interface or handle Cisco voice calls within the ExpertFlow Agent Desk.

## 1. Deployment Models

ExpertFlow CX supports two primary integration patterns for Cisco environments:

| Model | Description | Primary Use Case |
|-------|-------------|------------------|
| **Embedded Gadget** | The ExpertFlow Agent Desk is loaded as a gadget within the Cisco Finesse toolbar. | Agents who primarily handle Cisco Voice but need digital channel access. |
| **Standalone Desk** | The Cisco Finesse CTI bar is integrated into the ExpertFlow Agent Desk. | Agents who primarily handle Digital Channels but need Cisco Voice controls. |

## 2. Capability Matrix

The following table defines which platform controls specific call actions during an integrated session.

| Capability | Cisco Finesse | ExpertFlow Agent Desk | Notes |
|------------|---------------|-----------------------|-------|
| **Agent Login** | Supported | Supported | SSO and Non-SSO supported. |
| **State Change** | Supported | Synchronized | State changes in Finesse update the CX MRD state. |
| **Answer/End Call**| Supported | Supported | Bi-directional CTI control. |
| **Hold/Resume** | Supported | View Only | Managed via Finesse CTI bar. |
| **Direct Transfer** | Supported | Initiated via Finesse| Supports Queue and Extension transfers. |
| **Consult Call** | Supported | Initiated via Finesse| Integrated with CX interaction history. |
| **Wrap-up** | Supported | Supported | Finesse wrap-up codes are pushed to CX. |

## 3. Interaction Data & History

For every active Cisco call, ExpertFlow CX provides:
- **Unified Interaction History:** View past chats, emails, and calls for the specific customer.
- **IVR Activity Tracking:** Real-time visibility into the customer's journey through the Cisco IVR before the call reached the agent.
- **Recording Integration:** Support for Eleveo and other 3rd-party recording links within the CX activity timeline.

## 4. Operational Requirements

### Browser Persistence
ExpertFlow uses browser cache for state synchronization between Finesse and the Agent Desk. **Incognito/Private mode** is not recommended as it may block required state maintenance.

### State Synchronization
Agent state changes (Ready/Not Ready) are bi-directionally synchronized. A "Not Ready" state applied in Finesse will automatically update the agent's status in ExpertFlow digital channels.

## 5. Known Integration Behaviors

- **Manual Outbound:** Outbound calls dialed via Finesse are recorded as 'Voice Activities' in ExpertFlow.
- **Consult Leg Tracking:** Consult call durations are included in the overall CX Call Duration metrics.
- **Transfer Correlation:** When calls are transferred between agents, ExpertFlow maintains a single conversation thread for end-to-end context.

---

*For detailed version compatibility and component-level configuration, see the [Cisco Voice Channel Configuration Guide](Cisco-Voice-Channel-Configuration.md).*
