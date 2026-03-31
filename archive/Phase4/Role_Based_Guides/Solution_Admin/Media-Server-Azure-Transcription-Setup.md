---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Media Server: Azure Transcription Setup

This guide details the prerequisites and steps to enable real-time speech-to-text using Microsoft Azure within the Expertflow Media Server.

## 1. Prerequisites
- **OS**: Debian 12
- **Hardware**: 8 Cores, 16GB RAM, 150GB Disk
- **Firewall**: Ports 5060-5091 (SIP), 8021 (ESL), 16384-32768 (RTP), 7443 (WebRTC) must be open.

## 2. Setup Azure Speech Service
1. Create an **Azure Speech Resource** in your Azure Portal.
2. Note your **Subscription Key**, **Region**, and **Endpoint**.
3. Create a speech endpoint via the Azure API using a supported model (e.g., `en-US`).
4. Capture the `webSocketConversation` URL (starting with `wss://`).

## 3. Installation
SSH into your server and run:
```bash
git clone -b azure_transcribe https://gitlab.expertflow.com/rtc/media-server-setup.git
cd media-server-setup/debian && ./install.sh
```

## 4. Global Configuration
1. Log in to the Media Server web interface.
2. Go to **Advanced > Variables**.
3. Add a variable: `Category: Defaults`, `Name: transcription-vendor`, `Value: azure`.
4. Reload XML in **Status > SIP Status**.

## 5. Dialplan Configuration
Create a new Dialplan named `azure_transcription`:
- **Condition**: `${transcription-vendor}` matches `^azure$`
- **Actions**:
  - `export: AZURE_SUBSCRIPTION_KEY=<your-key>`
  - `export: AZURE_SERVICE_ENDPOINT=<your-wss-endpoint>`
  - `export: AZURE_REGION=<your-region>`
  - `export: nolocal:execute_on_answer=lua start_transcribe.lua azure en-US ${uuid}`

Save and test with a live call to verify the transcription stream in the Agent Desk.
