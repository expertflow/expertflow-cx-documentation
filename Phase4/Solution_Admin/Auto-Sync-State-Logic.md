---
title: "Auto-Sync State Logic"
summary: "Explanation of the auto-synchronization feature between the agent's parent state and individual channel (MRD) states."
audience: [admin]
product-area: [agent-desk, routing]
doc-type: explanation
difficulty: beginner
aliases: []
last-updated: 2026-03-08
---

# Auto-Sync State Logic

The **Auto-Sync MRD State** feature simplifies the agent experience by automatically synchronizing an agent's global "Parent State" with their individual "Media Routing Domain" (MRD) states.

## 1. How Auto-Sync Works
In a standard configuration, an agent would need to manually set themselves to **Ready** for each channel (Voice, WhatsApp, Chat) one-by-one.
- **Enabled Logic:** When Auto-Sync is enabled, setting the **Parent State** to **Ready** will automatically set all compatible MRDs to **Ready.**
- **Reverse Sync:** If an agent manually sets their **last active MRD** to **Not Ready,** the system will automatically transition their **Parent State** to **Not Ready.**

## 2. Admin Configurations
As a Solution Admin (Olivia), you can enable or disable this feature for each specific MRD.
- **The Requirement:** When creating a new MRD, the **"Autosync state with the parent state"** toggle must be enabled for the initial creation. 
- **The Flexibility:** Once the MRD is created, you can disable the auto-sync option if you want agents to have manual control over that specific channel.

## 3. Important Exceptions
- **Voice Channels:** If auto-sync is enabled for the **CX-Voice** MRD for a non-voice agent (or if the FreeSwitch connection fails), the agent will be unable to manually change their state to "Not Ready."
- **Feature Flag:** This functionality is controlled by a system-wide flag in the **Routing Engine.** To disable the feature completely, set `IS_MRD_AUTO_SYNC_ENABLED=false` in the deployment environment variables.

### Why use Auto-Sync?
1. **Efficiency:** It reduces the number of clicks an agent needs to perform to start their shift. 
2. **Adherence:** It ensures that when an agent is ready for work, they are immediately available on all their assigned channels.

---

*For technical details on these states, see the [Presence and State Technical Reference](../Agent/Presence-and-State-Technical-Reference.md).*
