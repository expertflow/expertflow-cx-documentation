---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Media Server Configuration for CX Voice

This document details the software requirements and configuration steps for the Expertflow Media Server (Freeswitch-based) to support CX Voice features.

## 1. Lua Library Installation
SSH into the Media Server and install the required libraries for script execution:
```bash
apt install lua-socket lua-sec lua-json lua-dkjson
```

## 2. IVR Scripts and Recordings
1. **Clone Repository**: Clone the latest `freeswitch-scripts` from GitLab.
2. **Environment Setup**: Rename `cx_env.lua` to `cx_env{DN}.lua` where `{DN}` is your IVR's dialing number.
3. **Configuration**: Edit the `.lua` file to set your `cxFqdn`, `voiceConnectorApi`, and target `queue`.
4. **Deployment**: Move scripts to `/usr/share/freeswitch/scripts` and prompts to `/usr/share/freeswitch/sounds/ivr_prompts/`.

## 3. Dialplan Configuration
Configure the following dialplans via the FusionPBX web interface:
- **Inbound IVR**: Matches the destination number and triggers `lua cxIvr.lua`.
- **Outbound IVR**: Used for Dialer campaigns (optional).
- **Direct-Transfer**: Handles transfers to queues using `vcApi.lua 'directTransfer'`.
- **WebRTC**: Enables web-based calling via `vcApi.lua 'webrtc'`.
- **Manual Outbound**: Handles agent-initiated calls.

## 4. SIP Profile and ACL
- **ACL**: Add the IP addresses of the Voice Connector, Dialer, and Media Server itself to the `esl` access control list.
- **SIP Profile**: Enable `ws-binding` and `wss-binding` in the internal SIP profile to support WebRTC.

## 5. Event Socket Library (ESL)
Ensure the Event Socket is listening on `0.0.0.0:8021` with the correct password (default: `ClueCon`) to allow external components to control calls.
