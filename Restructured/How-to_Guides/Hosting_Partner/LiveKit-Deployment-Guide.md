---
title: "LiveKit Deployment Guide"
summary: "How-to guide for deploying the ExpertFlow LiveKit AI voice agent integration on Debian 12 using Docker Compose — covering infrastructure, dashboard, AI agent configuration, SIP trunk setup via lk CLI and dashboard, dispatch rules, and FusionPBX routing."
audience: [hosting-partner]
product-area: [voice, platform]
doc-type: how-to
difficulty: advanced
keywords: ["LiveKit deployment CX", "LiveKit AI agent CX", "LiveKit Docker CX", "LiveKit SIP trunk CX", "LiveKit FusionPBX CX", "OpenAI realtime API CX"]
aliases: ["LiveKit CX deployment", "AI voice agent LiveKit CX", "LiveKit SIP CX"]
last-updated: 2026-03-10
---

# LiveKit Deployment Guide

This guide deploys the ExpertFlow LiveKit integration — an AI-powered voice agent that handles inbound SIP calls, engages with customers using OpenAI's Realtime API, and transfers calls to human agents via ExpertFlow CX when needed.

---

## Prerequisites

### System Requirements

| Resource | Minimum | Recommended |
|---|---|---|
| OS | Debian 12 (Bookworm) | Debian 12 |
| CPU | 4 cores | 8 cores |
| RAM | 8 GB | 16 GB |
| Storage | 50 GB free | — |

### Required Software

- Docker 24.0+
- Docker Compose 2.20+
- Git

### External Dependencies

- FusionPBX server (can be on a separate VM)
- OpenAI API key with Realtime API access
- Deepgram API key
- ExpertFlow CX with a CCM endpoint (Unified Agent tenant)

### Required Ports

| Service | Port(s) | Protocol | Purpose |
|---|---|---|---|
| LiveKit Server | 7880, 7881 | TCP | WebSocket / HTTP API |
| LiveKit RTC | 50000–50200 | UDP | WebRTC media streams |
| SIP Service | 5060 | TCP/UDP | SIP signalling |
| RTP Media | 10000–10200 | UDP | Voice/media streams |
| Redis | 6379 | TCP | Internal state management |
| Dashboard | 8000 | TCP | Web interface |

---

## Step 1: Install Docker

Check if Docker is already installed:

```bash
docker --version
```

If not installed:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

---

## Step 2: Configure Firewall

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 7880 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 7881 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 50000:50200 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 5060 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 5060 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 10000:10200 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -i lo -j ACCEPT

sudo apt install -y iptables-persistent
sudo netfilter-persistent save
```

---

## Step 3: Clone the Repository

```bash
cd ~
sudo apt install -y git
git clone -b develop \
  https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/livekit.git livekit-project
cd livekit-project
```

Expected directory structure:

```
agent/
dashboard/
infrastructure/
dispatch-rule.json
README.md
```

---

## Step 4: Configure and Start Infrastructure

### 4.1 Set your VM IP

```bash
cd ~/livekit-project/infrastructure
nano docker-compose.yaml
```

Find and update:

```yaml
external_ip: "YOUR_VM_IP_ADDRESS"
```

> `livekit-config.yaml` does not require changes. The network is created automatically.

### 4.2 Start infrastructure containers

```bash
docker compose up -d --build
docker ps
```

---

## Step 5: Configure and Start the Dashboard

```bash
cd ~/livekit-project/dashboard
nano .env
```

Update credentials if desired:

```env
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your_secure_password_here
```

Start the dashboard:

```bash
docker compose up -d
docker ps | grep dashboard
docker logs livekit-dashboard --tail 50
```

---

## Step 6: Configure and Start the AI Agent

### 6.1 Set API keys

```bash
cd ~/livekit-project/agent/src
nano .env
```

Required:

```env
OPENAI_API_KEY=sk-proj-YOUR_OPENAI_API_KEY_HERE
DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY_HERE
```

Optional (ElevenLabs):

```env
ELEVEN_API_KEY=your_elevenlabs_key_here
ELEVENLABS_AGENT_ID=your_agent_id_here
```

### 6.2 Update agent configuration

```bash
nano complete_flow_agent.py
```

Find the configuration block (around line 360–390) and update:

```python
fusionpbx_ip = "192.168.1.17"       # Your FusionPBX server IP
agent_extension = "99900"            # Extension routing to human agents on FusionPBX
service_identifier = "1122"          # Must match your CX channel Service Identifier in Unified Admin

CCM_URL = "https://YOUR-TENANT.expertflow.com/ccm/message/receive"
```

Leave `outbound_trunk_id` — update it in Step 7.4 after creating the outbound trunk.

### 6.3 Build and start the agent

```bash
cd ~/livekit-project/agent
docker compose build
docker compose up -d --build
docker ps | grep agent
```

---

## Step 7: Configure SIP Trunks and Dispatch Rules

### 7.1 Install and configure the LiveKit CLI

```bash
cd /tmp
wget https://github.com/livekit/livekit-cli/releases/download/v2.2.0/livekit-cli_2.2.0_linux_amd64.tar.gz
tar -xzf livekit-cli_2.2.0_linux_amd64.tar.gz
sudo mv lk /usr/local/bin/
sudo chmod +x /usr/local/bin/lk

export LIVEKIT_URL=http://localhost:7880
export LIVEKIT_API_KEY=devkey
export LIVEKIT_API_SECRET=h1J2kL3mN4pQ5rS6tU7vW8xY9zA0bC1d
```

### 7.2 Create the inbound trunk (FusionPBX → LiveKit)

The dashboard does not support custom header mapping required for passing caller information. Use the CLI:

```bash
cd ~/livekit-project
nano inbound-trunk.json
```

Paste:

```json
{
  "trunk": {
    "name": "Testing Trunk",
    "numbers": ["10005"],
    "headers_to_attributes": {
      "P-Asserted-Identity": "caller_id",
      "From": "from_header",
      "X-Caller-Extension": "caller_extension"
    },
    "include_headers": 1
  }
}
```

Update `numbers` to the extension customers dial to reach the AI.

Create the trunk:

```bash
lk sip inbound create inbound-trunk.json
```

**Save the trunk ID** (format: `ST_abc123xyz456`) — you need it for the dispatch rule in Step 7.5.

### 7.3 Access the Dashboard

Open `http://YOUR_VM_IP:8000` and log in with the credentials from Step 5.

### 7.4 Create the outbound trunk (LiveKit → FusionPBX)

In the dashboard, navigate to **Outbound Calls** in the left sidebar and click **Create New Trunk**. Switch to JSON mode and paste (update the address and numbers):

```json
{
  "name": "Agent Transfer Trunk",
  "address": "192.168.1.17",
  "transport": "tcp",
  "numbers": ["99900"]
}
```

**Copy the trunk ID** (format: `ST_...`).

Update the agent code with this trunk ID:

```bash
cd ~/livekit-project/agent/src
nano complete_flow_agent.py
```

Find and replace:

```python
outbound_trunk_id = "ST_YOUR_NEW_TRUNK_ID"
```

Restart the agent:

```bash
cd ~/livekit-project/agent
docker compose restart
```

### 7.5 Create a Dispatch Rule

In the dashboard, navigate to **Inbound Rules → Dispatch Rules** and click **Create Rule**:

| Field | Value |
|---|---|
| Name | `Main Dispatch Rule` |
| Trunk | Select your inbound trunk |
| Room Prefix | `_FreeSWITCH_` |
| Agent Name | Leave blank (automatic dispatch) |

---

## FusionPBX Setup

### Create an extension

In FusionPBX, hover over **Accounts → Extensions** and click **Add**.

### Outbound Route (FusionPBX → LiveKit)

1. Go to **Dialplan → Outbound Routes → Add**.
2. Create a gateway pointing to `YOUR_LIVEKIT_VM_IP:5060`.
3. Set the destination number to `99900`.
4. Select the LiveKit gateway in the outbound route.

### Inbound Route (LiveKit → FusionPBX)

1. Go to **Dialplan → Public → Add**.
2. Configure an inbound route for calls coming from LiveKit.
3. Add a dialplan connecting to the CX Voice Connector.
4. After changes, reload: go to FusionPBX **Status → XML Caching** and reload, or run `reloadxml` in the FreeSWITCH CLI.

---

## Verify All Containers

```bash
docker ps
```

Expected running containers:

| Container | Image |
|---|---|
| `livekit-agent` | `agent-livekit-agent` |
| `livekit-dashboard` | `dashboard-dashboard` |
| `infrastructure-sip-1` | `livekit/sip:latest` |
| `infrastructure-livekit-1` | `livekit/livekit-server:latest` |
| `infrastructure-redis-1` | `redis:7-alpine` |

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [EasySIPp Deployment Guide](EasySIPp-Deployment-Guide.md)
