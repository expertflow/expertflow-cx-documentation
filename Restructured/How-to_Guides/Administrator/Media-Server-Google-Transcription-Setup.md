---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Media Server: Google Transcription Setup

This guide details the steps to enable real-time speech-to-text using Google Cloud Speech-to-Text within the Expertflow Media Server.

## 1. Prerequisites
- **OS**: Debian 12
- **Hardware**: 8 Cores, 16GB RAM, 150GB Disk
- **Firewall**: Standard SIP and WebRTC ports must be open.

## 2. Setup Google Cloud Speech
1. Create a project in the **Google Cloud Console**.
2. Enable the **Cloud Speech-to-Text API**.
3. Create a **Service Account** and generate a **JSON Key**.
4. Rename the key to `google-creds.json` and upload it to the `/home` directory on your Media Server.

## 3. Installation
SSH into your server and run:
```bash
git clone -b google_transcribe https://gitlab.expertflow.com/rtc/media-server-setup.git
cd media-server-setup/debian && ./install.sh
```

## 4. Configuration
1. Log in to the Media Server web interface.
2. Go to **Advanced > Variables**.
3. Set `transcription-vendor` to `google`.
4. Create a Dialplan named `google_transcription`:
   - **Condition**: `${transcription-vendor}` matches `^google$`
   - **Actions**:
     - `action: set START_RECOGNIZING_ON_VAD=true`
     - `action: export nolocal:execute_on_answer=lua start_transcribe.lua google en-US ${uuid}`

Save and reload the XML status to activate.
