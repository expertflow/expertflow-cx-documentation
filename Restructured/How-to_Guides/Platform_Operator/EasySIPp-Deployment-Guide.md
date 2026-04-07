---
title: "EasySIPp Deployment Guide"
summary: "How-to guide for deploying EasySIPp — a web-based SIPp frontend for SIP load testing — using Docker Compose on Linux, including the custom UAC scenario for unique caller IDs and FusionPBX trust configuration."
audience: [platform-operator]
product-area: [voice, platform]
doc-type: how-to
difficulty: intermediate
keywords: ["EasySIPp deployment CX", "SIPp load testing CX", "SIP load test Docker CX", "EasySIPp Docker CX", "SIP performance test CX"]
aliases: ["EasySIPp CX", "SIPp web GUI CX", "SIP load testing tool CX"]
last-updated: 2026-03-10
---

# EasySIPp Deployment Guide

EasySIPp is a web-based frontend for [SIPp](https://github.com/SIPp/sipp), making SIP call load testing accessible via a browser interface.

> **Critical requirement**: EasySIPp **must** be installed on a **different server** than your FreeSWITCH/FusionPBX. Do not run load tests from the same machine as the switch.

---

## Prerequisites

- Docker and Docker Compose installed on a Linux server.

Verify:

```bash
docker --version
docker-compose --version
```

---

## Step 1: Create the Project Directory

```bash
mkdir -p /opt/easysipp
mkdir -p /opt/easysipp/xml
cd /opt/easysipp
```

---

## Step 2: Create the Custom SIP Scenario

This scenario assigns a **unique caller ID** to every call, which is required for accurate load testing.

```bash
nano xml/uac_custom.xml
```

Paste the following content exactly:

```xml
<?xml version="1.0" encoding="ISO-8859-1" ?>
<!DOCTYPE scenario SYSTEM "sipp.dtd">
<scenario name="Unique Caller ID UAC">
  <!-- Small delay before INVITE to stagger start -->
  <pause milliseconds="2000"/>
  <send retrans="500">
    <![CDATA[
      INVITE sip:[service]@[remote_ip]:[remote_port] SIP/2.0
      Via: SIP/2.0/[transport] [local_ip]:[local_port];branch=[branch]
      From: sipp-[call_number] <sip:sipp-[call_number]@[local_ip]:[local_port]>;tag=[pid]SIPpTag00[call_number]
      To: [service] <sip:[service]@[remote_ip]:[remote_port]>
      Call-ID: [call_id]
      CSeq: 1 INVITE
      Contact: sip:sipp@[local_ip]:[local_port]
      Max-Forwards: 70
      Subject: Performance Test
      Content-Type: application/sdp
      Content-Length: [len]
      v=0
      o=user1 53655765 2353687637 IN IP[local_ip_type] [local_ip]
      s=-
      c=IN IP[media_ip_type] [media_ip]
      t=0 0
      m=audio [media_port] RTP/AVP 0
      a=rtpmap:0 PCMU/8000
    ]]>
  </send>
  <recv response="100" optional="true"></recv>
  <recv response="180" optional="true"></recv>
  <recv response="183" optional="true"></recv>
  <recv response="200" rtd="true"></recv>
  <send>
    <![CDATA[
      ACK sip:[service]@[remote_ip]:[remote_port] SIP/2.0
      Via: SIP/2.0/[transport] [local_ip]:[local_port];branch=[branch]
      From: sipp-[call_number] <sip:sipp-[call_number]@[local_ip]:[local_port]>;tag=[pid]SIPpTag00[call_number]
      To: [service] <sip:[service]@[remote_ip]>[peer_tag_param]
      Call-ID: [call_id]
      CSeq: 1 ACK
      Contact: sip:sipp@[local_ip]:[local_port]
      Max-Forwards: 70
      Subject: Performance Test
      Content-Length: 0
    ]]>
  </send>
  <!-- Call duration: 1 hour (3600000 ms) -->
  <pause milliseconds="3600000"/>
  <send retrans="500">
    <![CDATA[
      BYE sip:[service]@[remote_ip]:[remote_port] SIP/2.0
      Via: SIP/2.0/[transport] [local_ip]:[local_port];branch=[branch]
      From: sipp-[call_number] <sip:sipp-[call_number]@[local_ip]:[local_port]>;tag=[pid]SIPpTag00[call_number]
      To: [service] <sip:[service]@[remote_ip]>[peer_tag_param]
      Call-ID: [call_id]
      CSeq: 2 BYE
      Contact: sip:sipp@[local_ip]:[local_port]
      Max-Forwards: 70
      Subject: Performance Test
      Content-Length: 0
    ]]>
  </send>
  <recv response="200" crlf="true"></recv>

  <ResponseTimeRepartition value="10, 20, 30, 40, 50, 100, 150, 200"/>
  <CallLengthRepartition value="10, 50, 100, 500, 1000, 5000, 10000"/>
</scenario>
```

---

## Step 3: Create `docker-compose.yml`

```bash
nano docker-compose.yml
```

Paste:

```yaml
version: '3.8'
services:
  easysipp:
    container_name: easysipp
    image: krndwr/easysipp
    network_mode: host
    user: root
    volumes:
      - ./xml/uac_custom.xml:/app/easySIPp/xml/uac_custom.xml
    entrypoint: >
      /bin/sh -c "
      sed -i 's/8080/8089/g' /etc/nginx/sites-available/easysipp-nginx.conf &&
      sed -i 's/8000/8001/g' /entrypoint.sh &&
      sed -i 's/8000/8001/g' /etc/nginx/sites-available/easysipp-nginx.conf &&
      /entrypoint.sh"
    cap_add:
      - NET_RAW
      - NET_ADMIN
    restart: unless-stopped
```

> The entrypoint remaps the GUI to port **8089** and the app to port **8001** to avoid conflicts with other services on the host.

---

## Step 4: Start the Container

```bash
docker-compose up -d --build
```

Access the web UI at:

```
http://<YOUR_SERVER_IP>:8089
```

---

## Configuration

### Verify Connectivity

Confirm the EasySIPp server can reach the target FreeSWITCH server:

```bash
ping <FREESWITCH_IP>
```

### Trust Setup (Required)

FreeSWITCH/FusionPBX will reject unauthenticated calls with `407 Proxy Authentication Required` unless the EasySIPp server IP is trusted.

**FusionPBX — Add trusted IP:**

1. Log in to FusionPBX.
2. Go to **Advanced → Access Control**.
3. Select the `providers` list (or create a new one with default `deny`).
4. Add your EasySIPp server IP (e.g., `192.168.2.24/32`) with Type `allow`.
5. Go to **Status → SIP Status**.
6. Click **ReloadACL**.

---

## Running a Test

In the EasySIPp GUI, select the **UAC** tab and fill in:

| Field | Value |
|---|---|
| **Select UAC XML** | `uac_custom.xml` |
| **Remote Address** | FreeSWITCH/FusionPBX IP |
| **Remote Port** | `5060` |
| **Local Address** | `0.0.0.0` |
| **Local Port** | `5062` |
| **Dialed Number** | Target extension or inbound route (prefix `11` for internal DNs — e.g., internal DN `1225` becomes `111225`) |
| **Protocol** | `UDP` |

---

## Remote Server Configuration

On the FusionPBX/FreeSWITCH server:

1. Create an inbound route for the dialed number.
2. Create a dialplan routing the number to the test IVR.
3. Place the `cxIvr<DN>.lua` script in `/usr/share/freeswitch/scripts/`.

The script filename format is: `cxIvr<DN>.lua` — for example, `cxIvr1225.lua`.

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)
