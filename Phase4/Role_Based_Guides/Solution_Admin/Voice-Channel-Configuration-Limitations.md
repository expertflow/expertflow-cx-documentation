---
audience: [solution-admin]
doc-type: reference
difficulty: beginner
aliases: []
---

# Voice Channel Configuration: Limitations & Proposed Solutions

This document outlines current technical constraints when configuring voice channels for Cisco and EF-Switch (Freeswitch) environments.

## Current Limitations
- **Parameter Conflict**: The `ProviderWebhook` parameter is hidden for Cisco but required for EF-Switch.
- **MRD Sharing**: The `VOICE` Media Routing Domain (MRD) is bootstrapped for Cisco by default. To use it for EF-Switch, the `ManagedByRe` flag must be manually enabled.
- **Simultaneous Use**: The system currently cannot support both Cisco (external routing) and EF-Switch (internal routing) simultaneously using the same channel types.

## Proposed Strategy
1. **Separation**: Split voice into two distinct channel types: `Cisco-CC` and `CX-Voice`.
2. **Dedicated MRDs**: Bootstrap separate MRDs for each (e.g., `Cisco Voice` and `CX Voice`).
3. **Optional Webhooks**: Make the `ProviderWebhook` field optional rather than hidden.
4. **ANI Identification**: Shift customer identification from dialog IDs to ANI (caller number) to simplify cross-channel session lookups in Redis.

## Roadmap Tasks
- [ ] Remove hard-coded Voice MRD references from the Agent Desk UI.
- [ ] Bootstrap separate FreeSwitch and Cisco MRDs in the Routing Engine.
- [ ] Enable customer identification via ANI for all voice channels.
