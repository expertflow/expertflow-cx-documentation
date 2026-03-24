---
title: "Deploying Finesse Gadget"
summary: "Step-by-step guide for deploying the ExpertFlow CX Agent Gadget on Cisco Finesse — covering file preparation, FTP upload to the Finesse server, desktop layout configuration, and CTI environment variable setup."
audience: [developer-integrator]
product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["Finesse gadget deployment CX", "deploy Finesse gadget", "Cisco Finesse CX integration", "agent gadget Finesse", "Finesse desktop layout CX", "CTI Finesse CX", "Finesse FTP deployment CX"]
aliases: ["Finesse gadget CX", "deploy agent gadget Finesse", "Cisco Finesse agent desk CX"]
last-updated: 2026-03-10
---

# Deploying Finesse Gadget

This guide covers the deployment of the ExpertFlow CX Agent Gadget onto Cisco Finesse, enabling agents to use Agent Desk within the Finesse interface.

## Prerequisites

- ExpertFlow CX deployed and accessible via FQDN
- Cisco Finesse server access with FTP credentials (provided by the System/IT admin)
- Access to the CX deployment machine

---

## Step 1: Locate the Gadget Files

On the CX deployment machine, navigate to the Finesse gadget directory:

```bash
cd kubernetes/post-deployment/3rdPartyResources/Finesse-gadget
```

---

## Step 2: Update the Gadget URL

Edit `AgentGadget.js` and replace the value of `agentGadgetURL` with your CX FQDN:

```javascript
var agentGadgetURL = "https://your-cx-fqdn.example.com";
```

Save the file.

---

## Step 3: Upload Files to Finesse via FTP

1. Open your FTP client and connect to the Finesse FTP server:
   - **Host**: Finesse server IP
   - **Username / Password**: Provided by the System/IT admin

2. After connecting, navigate to the `files` directory on the Finesse server.

3. Create a new folder named `AgentGadget` inside the `files` directory.

4. Transfer all files from:
   ```
   <cx-install-dir>/3rdPartyResources/Finesse-gadget/
   ```
   to:
   ```
   /3rdpartygadget/files/AgentGadget/
   ```
   on the Finesse server.

---

## Step 4: Add the Gadget to the Finesse Desktop Layout

1. Open Cisco Finesse administration (`cfadmin`).
2. Navigate to **Desktop Layout**.
3. Add the following gadget entry to the desktop layout XML:
   ```xml
   <gadget>/3rdpartygadget/files/AgentGadget/AgentGadget.xml</gadget>
   ```
4. Save the settings.

---

## Step 5: Configure CTI Environment Variables

Update the CTI config variables in the unified-agent/Agent Desk environment variables according to your Cisco environment. Refer to the **Environment Configurations for Cisco** guide for the full list of variables.

---

## Step 6: Verify

Log in to Finesse as an agent. The Agent Gadget panel should appear in the desktop layout and load the ExpertFlow CX Agent Desk interface.

---

## Related Articles

- [Finesse Integration Prerequisites](Finesse-Integration-Prerequisites.md)
- [Cisco Voice Channel Configuration](Cisco-Voice-Channel-Configuration.md)
- [Synchronizing Cisco Users and Teams](Synchronizing-Cisco-Users-and-Teams.md)
- [Cisco Integration Known Limitations](Cisco-Integration-Known-Limitations.md)
