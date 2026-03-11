---
title: "Adding Agent Extensions for CX Voice"
summary: "How-to guide for configuring the Media Server extension (agentExtension) for individual agents in Keycloak, required for CX Voice call routing to agent phones."
audience: [solution-admin]
product-area: [voice]
doc-type: how-to
difficulty: beginner
keywords: ["agent extension", "CX Voice extension", "Keycloak extension", "agentExtension", "voice extension setup", "media server extension"]
aliases: ["configure agent extension", "set agent extension", "voice extension Keycloak"]
last-updated: 2026-03-10
---

# Adding Agent Extensions for CX Voice

Each agent who receives CX Voice calls requires a **Media Server extension** configured in Keycloak. This extension is the SIP address or FreeSWITCH extension the platform dials when routing a call to the agent.

## Prerequisites

- Access to the Keycloak administration console for your CX deployment.
- The agent's Media Server extension number (assigned by your telephony administrator).

## Steps

1. Navigate to `https://<your-FQDN>/auth` in your browser.

2. Select the **Expertflow** realm from the realm dropdown.

3. Navigate to **Users** in the left navigation.

4. Search for and select the agent user you want to configure.

5. Click the **Attributes** tab on the user's profile page.

6. Add a new attribute:
   - **Key**: `agentExtension`
   - **Value**: The agent's extension number (e.g., `1001`)

7. Click **Save**.

8. Inform the agent that they must **log out and log back in** to the Agent Desk for the extension to take effect.

## Limitations

| Limitation | Detail |
|---|---|
| **Re-login required** | The extension is only reflected after the agent logs out and logs back in following the configuration. |
| **One extension per agent** | Only a single extension can be configured per user. Multiple extensions per user are not supported. |
| **No shared extensions** | The same extension must not be assigned to more than one user. Shared extensions will cause routing conflicts. |

## Related Articles

- [Inbound Calls](Inbound-Calls.md)
- [CTI Call Controls](CTI-Call-Controls.md)
- [IAM Keycloak Configuration](../../Solution_Admin/IAM-Keycloak-Configuration.md)
- [CX Voice Limitations](CX-Voice-Limitations.md)
