---
title: "Configuring User Inactivity Logout"
summary: "How-to guide for Solution Admins to configure automated agent logout based on inactivity periods, including warning triggers and rerouting behavior."
audience: [administrator]
product-area: [platform, security, agent-desk]
doc-type: how-to
difficulty: beginner
last-updated: 2026-03-11
---

# Configuring User Inactivity Logout

The User Inactivity Logout feature enhances platform security by automatically logging out users from the Agent Desk after a defined period of idle time. This ensures that unattended sessions are terminated, preventing unauthorized access.

## 1. Admin Configuration
Only a Solution Admin (Olivia) can enable or adjust the inactivity parameters.

1.  Log in to the **Unified Admin**.
2.  Navigate to **Agent Desk Settings > Global Security**.
3.  **Inactivity Timeout:** Toggle this feature to **ON**.
4.  **Duration:** Set the idle time limit in seconds.
    *   **Allowed Range:** 30 seconds to 3600 seconds (1 hour).
5.  Click **Save**.

---

## 2. Agent Experience & Warning Trigger
To prevent accidental logouts during active work, the system utilizes a proactive warning mechanism.

*   **Detection:** Inactivity is defined as zero keyboard, mouse, or microphone input within the Agent Desk browser tab.
*   **The 80% Warning:** Once an agent has been idle for **80% of the configured duration**, a countdown prompt appears on their screen.
    *   *Example:* If the timeout is set to 10 minutes (600s), the warning appears at the 8-minute mark.
*   **Dismissal:** Moving the mouse or typing any key immediately dismisses the warning and resets the inactivity timer.

---

## 3. Conversation Rerouting Logic
If an agent is logged out due to inactivity while handling active interactions:
1.  The agent's state is set to `LOGOUT`.
2.  Any currently accepted interactions (Chat or Email) are immediately **rerouted** to the next available agent based on the queue's routing logic.
3.  The customer is notified that they are being transferred to a new representative.

---

## 4. Inactivity Exceptions
The inactivity timer **stops counting** (the agent remains "Active") in the following scenarios:
*   **Active Voice/Video Call:** Inactivity is never tracked while a SIP or WebRTC call is in progress.
*   **Tab Backgrounding:** If the Agent Desk tab is minimized or hidden, some browsers may pause the timer. ExpertFlow recommends keeping the tab in focus for accurate timeout behavior.

---

## Related Guides
*   [Agent States and Reason Codes](../Agent/Agent-States.md)
*   [Unified Admin Core Configuration](../../Getting_Started/For_Administrators/)
*   [Security and Compliance Whitepaper](../../Platform_Overview/Security-and-Compliance-Whitepaper.md)
