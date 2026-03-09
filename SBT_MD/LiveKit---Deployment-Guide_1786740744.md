# CX Knowledgebase : LiveKit - Deployment Guide

## 1\. Prerequisites

### 1.1 System Requirements

**Requirement**| **Specification**  
---|---  
**Operating System**|  Debian 12 (Bookworm)  
**CPU**|  Minimum 4 cores (8 cores recommended)  
**RAM**|  Minimum 8GB (16GB recommended)  
**Storage**|  Minimum 50GB free space  
  
### 1.2 Required Software

  * Docker (Version 24.0+)

  * Docker Compose (Version 2.20+)

  * Git (For Cloning Repo)




### 1.3 External Dependencies

  * FusionPBX Server (can be on separate VM)

  * OpenAI API Key with Realtime API access

  * CCM Endpoint (Expertflow Unified Agent tenant)




### 1.4 Required Ports

**Services**| **Ports**| **Protocol**| **Description**  
---|---|---|---  
LiveKit Server| 7880, 7881| TCP| WebSocket/HTTP API  
LiveKit RTC| 50000-50200| UDP| WebRTC media streams  
SIP Service| 5060| TCP/UDP| SIP signalling  
RTP Media| 10000-10200| UDP| Voice/media streams  
Redis| 6379| TCP| State management (internal)  
Dashboard| 8000| TCP| Web interface  
SSH| 22| TCP| Remote access (If needed)  
  
* * *

## 2\. Installation Steps

### Step 1: Install Docker

**Check if Docker is already installed:**
[code] 
    docker --version
[/code]

If Docker is installed, you'll see version information. **Skip to Step 2.**

If not installed, run the following:
[code] 
    # Update system packages
    sudo apt update && sudo apt upgrade -y
    
    # Install required packages
    sudo apt install -y ca-certificates curl
    
    # Add Docker's official GPG key
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    
    # Add Docker repository
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    # Update package index
    sudo apt update
    
    # Install Docker
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    
    # Add current user to docker group
    sudo usermod -aG docker $USER
    
    # Apply group changes
    newgrp docker
    
    # Verify installation
    docker --version
    docker compose version
    ```
    
    **Expected output:**
    ```
    Docker version 24.x.x
    Docker Compose version 2.x.x
[/code]

### Step 2: Configure Firewall (Iptables)
[code] 
    # Allow SSH (IMPORTANT: Don't lock yourself out!)
    sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
    
    # Allow LiveKit Server (WebSocket/HTTP)
    sudo iptables -A INPUT -p tcp --dport 7880 -j ACCEPT
    sudo iptables -A INPUT -p tcp --dport 7881 -j ACCEPT
    
    # Allow LiveKit RTC (WebRTC media)
    sudo iptables -A INPUT -p udp --dport 50000:50200 -j ACCEPT
    
    # Allow SIP Service
    sudo iptables -A INPUT -p tcp --dport 5060 -j ACCEPT
    sudo iptables -A INPUT -p udp --dport 5060 -j ACCEPT
    
    # Allow RTP Media
    sudo iptables -A INPUT -p udp --dport 10000:10200 -j ACCEPT
    
    # Allow Dashboard
    sudo iptables -A INPUT -p tcp --dport 8000 -j ACCEPT
    
    # Allow established connections
    sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    
    # Allow loopback
    sudo iptables -A INPUT -i lo -j ACCEPT
    
    # Save iptables rules
    sudo apt install -y iptables-persistent
    sudo netfilter-persistent save
    
    # Verify rules
    sudo iptables -L -n -v
[/code]

### Step 3: Clone Repository
[code] 
    # Navigate to home directory
    cd ~
    
    # Install git if not already installed
    sudo apt update
    sudo apt install -y git
    
    # Clone repository
    git clone -b develop https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/rtc/livekit.git livekit-project
    
    # Navigate to project
    cd livekit-project
    
    # Verify directory structure
    ls -la
    ```
    
    **Expected output:**
    ```
    agent/
    dashboard/
    infrastructure/
    dispatch-rule.json
    README.md
    requirements-linux.txt
    requirements-window.txt
[/code]

### Step 4: Configure Infrastructure

#### 4.1 Update SIP Service External IP
[code] 
    cd ~/livekit-project/infrastructure
    nano docker-compose.yaml
[/code]

Find this line:
[code] 
    external_ip: "192.168.1.161"
[/code]

Change to your VM actual IP address:
[code] 
    external_ip: "YOUR_VM_IP_ADDRESS"
[/code]

Save and exit (Ctrl+X, Y, Enter)

The `livekit-config.yaml` file does **NOT** require any changes. The infrastructure `docker-compose.yaml` creates the network automatically, so no manual network creation is needed.

#### 4.2 Start Infrastructure Containers
[code] 
    cd ~/livekit-project/infrastructure
    
    # Start all infrastructure services
    docker compose up -d --build
    
    # Verify containers are running
    docker ps
[/code]

### Step 5: Configure Dashboard

#### 5.1 Update Dashboard Environment
[code] 
    cd ~/livekit-project/dashboard
    nano .env
[/code]

You can change the admin username and password in this file:
[code] 
    ADMIN_USERNAME=admin
    ADMIN_PASSWORD=your_secure_password_here
[/code]

All other settings are pre-configured and do not need changes.

**Save and exit** if you made changes (Ctrl+X, Y, Enter)

#### 5.2 Start Dashboard Container
[code] 
    cd ~/livekit-project/dashboard
    
    # Start dashboard
    docker compose up -d
    
    # Verify container is running
    docker ps | grep dashboard
    
    # Check logs
    docker logs livekit-dashboard --tail 50
[/code]

### Step 6: Configure AI Agent

#### 6.1 Update Agent Environment Variables
[code] 
    cd ~/livekit-project/agent/src
    nano .env
[/code]

Update the following required fields:

We are using OpenAI Realtime API so we don’t need any other vendor to use.
[code] 
    # ⚠️ REQUIRED: Add your OpenAI API key
    OPENAI_API_KEY=sk-proj-YOUR_OPENAI_API_KEY_HERE
    
    # ⚠️ REQUIRED: Add your Deepgram API key
    DEEPGRAM_API_KEY=YOUR_DEEPGRAM_API_KEY_HERE 
[/code]

**Optional:** If using ElevenLabs, update:
[code] 
    ELEVEN_API_KEY=your_elevenlabs_key_here
    ELEVENLABS_AGENT_ID=your_agent_id_here
[/code]

Without valid API keys, the agent will fail silently. Ensure you have valid keys before proceeding.

Save and exit.

#### **6.2 Update Agent Configuration**
[code] 
    cd ~/livekit-project/agent/src
    nano complete_flow_agent.py
[/code]

Find these lines (around line 360-390) and update:
[code] 
    # ⚠️ UPDATE THESE VALUES:
    fusionpbx_ip = "192.168.1.17"          # Your FusionPBX Server IP
    agent_extension = "99900"              # Extension that routes to human agent Inbound route on FusionPBX.
    service_identifier = "1122"            # Your service identifier should be same as you channel in Unified Admin
    
    # ⚠️ UPDATE CCM ENDPOINT:
    CCM_URL = "https://YOUR-TENANT.expertflow.com/ccm/message/receive"
    # Example: "https://efcx-dev2.expertflow.com/ccm/message/receive"
[/code]

Update:

  * `fusionpbx_ip`: Your FusionPBX server IP address

  * `CCM_URL`: Your CCM tenant URL




We'll update the `outbound_trunk_id` after creating the trunk in Step 7.

Save and exit.

#### 6.3 Build and Start Agent Container

Be patience it will take time to build.
[code] 
    cd ~/livekit-project/agent
    
    # Build the agent Docker image
    docker compose build
    
    # Start the agent
    docker compose up -d --build
    
    # Verify agent is running
    docker ps | grep agent
[/code]

## Configuration

### Step 7: Configure SIP Trunks and Dispatch Rules

#### 7.1 Install LiveKit CLI
[code] 
    cd /tmp
    wget https://github.com/livekit/livekit-cli/releases/download/v2.2.0/livekit-cli_2.2.0_linux_amd64.tar.gz
    tar -xzf livekit-cli_2.2.0_linux_amd64.tar.gz
    sudo mv lk /usr/local/bin/
    sudo chmod +x /usr/local/bin/lk
    
    # Verify installation
    lk --version
[/code]

Connect LiveKit CLI to server so we can manage trunks,dispatch rules etc form lk cli as well.
[code] 
    # Configure CLI environment
    export LIVEKIT_URL=http://localhost:7880
    export LIVEKIT_API_KEY=devkey
    export LIVEKIT_API_SECRET=h1J2kL3mN4pQ5rS6tU7vW8xY9zA0bC1d
[/code]

These `LIVEKIT_API_KEY` and `LIVEKIT_API_SECRET` are set in `docker-compose.yml`. When you run these `export` commands, you're setting **environment variables** in your current terminal session. These tell the LiveKit CLI (`lk` command) **where to connect** and **how to authenticate**.

#### 7.2 Create Inbound Trunk (FusionPBX → LiveKit)

Now we need to create inbound,outbound trunks and dispatch rules for our LiveKit agent. We will create inbound trunk using `lk cli` but for dispatch rules and outbound trunks we will use dashboard for ease.

**Why lk cli for inbound trunk?** The dashboard doesn't support custom header mapping, which is required for passing caller information to the agent.

Create trunk configuration file:
[code] 
    cd ~/livekit-project
    nano inbound-trunk.json
[/code]

Add this content:
[code] 
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
[/code]

**Update:**

  * `allowed_addresses`: Your FusionPBX server IP (e.g., `"192.168.1.17/32"`). So for we are not using this by allowing any server ip to dial and call 10005.

  * `numbers`: Extension that customers dial to reach the AI (e.g., `["10005"]`)




Save and exit.

**Create the trunk:**
[code] 
    lk sip inbound create inbound-trunk.json
    
    **Expected output:**
    Created trunk: ST_abc123xyz456
    
    **SAVE THIS TRUNK ID** - you'll need it for the dispatch rule.
    
    #### 7.3 Access Dashboard and Create Outbound Trunk
    
    **Open your browser and navigate to:**
    ```
    http://YOUR_VM_IP:8000
[/code]

Example: `http://192.168.1.161:8000`

**Login credentials:**

  * Username: `admin` (or what you set in `.env`of dashboard)

  * Password: (what you set in dashboard `.env`)




#### **7.3 Create Outbound Trunk**

Now we create outbound trunk easily from dashboard, go to Outbound calls form left side bar and then click create new trunk you can add details manually or just switch json from popup and paste this 
[code] 
    {
      "sip_trunk_id": "ST_W7jqvDFA2VgG",
      "name": "Agent Transfer Trunk",
      "address": "192.168.1.17",
      "transport": "tcp",
      "numbers": [
        "99900"
      ]
    }
[/code]

![image-20260305-074747.png](attachments/1786740744/1791590413.png?width=1377)

Copy the Trunk ID (starts with `ST_...`)

SAVE THIS OUTBOUND TRUNK ID - you need to update the agent code with it.

#### **7.4 Update Agent with Outbound Trunk ID**
[code] 
    cd ~/livekit-project/agent/src
    nano complete_flow_agent.py
[/code]

Find this line (around line 380-385):
[code] 
    outbound_trunk_id = "ST_W7jqvDFA2VgG"
[/code]

Replace with your new outbound trunk ID:
[code] 
    outbound_trunk_id = "ST_YOUR_NEW_TRUNK_ID"
[/code]

Save and exit.

Restart the agent:
[code] 
    cd ~/livekit-project/agent
    docker compose restart
[/code]

#### **7.5 Create Dispatch Rule (via Dashboard)**

**In the Dashboard:**

![image-20260305-075449.png](attachments/1786740744/1792409601.png?width=1377)

  1. Navigate to left sidebar **Inbound Rules → Dispatch Rules**

  2. Click **"Create Rule"**

  3. Fill in the form **or** you can switch to json and write json as well.

     * **Name:** `Main Dispatch Rule`

     * **Trunk:** Select your **inbound trunk** (FusionPBX Inbound Trunk)

     * **Room Prefix:** `_FreeSWITCH_`

     * **Agent Name:** Leave blank (for automatic dispatch)

  4. Click **"Create"**




* * *

## FusionPBX Setup

### 1\. Create extension in FusionPBX

Hove on accounts and then go to extensions click Add.

### 2\. Outbound Route (FusionPBX → LiveKit)

**Configuration:**

  1. **Go to:** Dialplan → Outbound Routes → Add

  2. **Gateway Setup:**

![image-20260305-080057.png](attachments/1786740744/1792475138.png?width=1353)
     * Create a new gateway pointing to: `YOUR_LIVEKIT_VM_IP:5060`

     * Example: `192.168.1.161:5060`

  3. **Route Configuration:**

     * **Create a Destination Number:** `99900`

![image-20260305-080440.png](attachments/1786740744/1792507906.png?width=1329)
     * **Outbound Route:** Select the LiveKit gateway created above and create outbound route 

![image-20260305-080658.png](attachments/1786740744/1790771233.png?width=1329)



All headers Variables in Outbound route should be same as it is just change your gateway in last line.

### Inbound Route (LiveKit → FusionPBX)

**Purpose:** When LiveKit transfers a call to extension `99900`, route it to a human agent.

**Configuration:**

  1. **Go to:** Dialplan → Public → Add 

![image-20260305-081343.png](attachments/1786740744/1791524877.png?width=1353)



1122 is internal DN there which is our channel id in Unified Admin.

  2. **Go to Dialplan:**




Add a dialplan for connecting to Voice Connector. 

![image-20260305-081907.png](attachments/1786740744/1792147459.png?width=1377)

After making changes, reload the dialplan from FusionPBX interface or run `reloadxml` in FreeSwitch CLI.

* * *

## Testing

### Verify All Containers
[code] 
    docker ps
[/code]

**Expected output - 5 running containers:**

Container Name| Image| Status  
---|---|---  
livekit-agent| agent-livekit-agent| Up  
livekit-dashboard| dashboard-dashboard| Up  
infrastructure-sip-1| livekit/sip:latest| Up  
infrastructure-livekit-1| livekit/livekit-server:latest| Up  
infrastructure-redis-1| redis:7-alpine| Up
