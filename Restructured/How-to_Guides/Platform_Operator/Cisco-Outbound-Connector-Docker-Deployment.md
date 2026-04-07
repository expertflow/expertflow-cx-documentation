---
title: "Cisco Outbound Connector — Docker Deployment"
summary: "How-to guide for deploying the Cisco Outbound Connector on Debian 12 using Docker Compose — covering prerequisites, Redis setup, port configuration, docker-compose.yml, and all environment variable definitions for CCX and CCE deployments."
audience: [hosting-partner]
product-area: [voice, channels]
doc-type: how-to
difficulty: intermediate
keywords: ["Cisco outbound connector Docker CX", "Cisco outbound Docker deployment CX", "UCCX connector Docker CX", "Cisco CCX CCE connector CX", "docker-compose Cisco connector CX"]
aliases: ["Cisco outbound Docker CX", "UCCX Docker connector CX", "Cisco connector deployment Docker CX"]
last-updated: 2026-03-10
---

# Cisco Outbound Connector — Docker Deployment

This guide deploys the ExpertFlow Cisco Outbound Connector on Debian 12 using Docker Compose. The connector bridges Cisco UCCX or UCCE outbound campaigns with ExpertFlow CX.

---

## Prerequisites

| Component | Requirement |
|---|---|
| Operating System | Debian 12 |
| Docker | v24 or higher |
| ExpertFlow CX | Latest version, deployed and accessible |
| Cisco UCCX or UCCE | Latest version, with campaigns configured |
| Redis | Latest version, installed on this server |

---

## Required Ports

| Port | Protocol | Purpose |
|---|---|---|
| 7115 | TCP | Cisco Connector access (mapped in docker-compose.yml) |
| 6379 | TCP | Redis |

Open the ports:

```bash
sudo iptables -A INPUT -p tcp -m tcp --dport 7115 -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 6379 -j ACCEPT
sudo iptables-save
```

---

## Redis Setup

After installing Redis, enable and start the service:

```bash
systemctl enable redis
systemctl start redis
systemctl enable redis-server
systemctl start redis-server
```

Configure Redis for external access and set a password (replace `PASSWORD` with your chosen password):

```bash
sed -i '/protected-mode/c\protected-mode no' /etc/redis/redis.conf
sed -i '/bind 127.0.0.1 -::1/c\# bind 127.0.0.1 -::1' /etc/redis/redis.conf
sed -i '/bind 127.0.0.1 ::1/c\# bind 127.0.0.1 ::1' /etc/redis/redis.conf
sed -i '/# requirepass/c\requirepass PASSWORD' /etc/redis/redis.conf
```

Restart Redis:

```bash
systemctl restart redis-server
systemctl restart redis
```

---

## Deploy the Connector

### Step 1: Create the project directory

```bash
mkdir cisco-outbound-connector
cd cisco-outbound-connector
```

### Step 2: Create `docker-compose.yml`

```bash
vi docker-compose.yml
```

Paste:

```yaml
version: "3"
services:
  cisco-outbound-connector:
    image: gitimages.expertflow.com/rtc/cisco-outbound-connector:1.1
    container_name: cisco-outbound-connector
    ports:
      - 7115:8080
    env_file:
      - docker-variables.env
    restart: always
```

### Step 3: Create `docker-variables.env`

```bash
vi docker-variables.env
```

Paste and update all values for your environment:

```env
CISCO_FQDN=https://uccx.test
CISCO_PASS=1234
CISCO_TYPE=CCX
CISCO_USERNAME=administrator
CX_FQDN=https://efcx.com
DB_IP=192.168.1.10
DB_NAME=dbname
DB_PASS=1234
DB_PORT=1504
DB_USERNAME=user
LOG_LEVEL=DEBUG
REDIS_DB=0
REDIS_HOST=localhost
REDIS_PASS=1234
REDIS_PORT=6379
REDIS_DELAY=10
SERVICE_ID=1234
```

### Environment Variable Reference

| Variable | Description |
|---|---|
| `CISCO_FQDN` | URL of the Cisco UCCX/UCCE deployment |
| `CISCO_USERNAME` | Admin username for Cisco |
| `CISCO_PASS` | Admin password for Cisco |
| `CISCO_TYPE` | `CCX` or `CCE` |
| `CX_FQDN` | ExpertFlow CX URL (`https://FQDN`) |
| `DB_IP` | IP address of the Cisco database server |
| `DB_NAME` | Cisco database name — CCX: `dialinglist` table; CCE: database containing `Dialer_Detail` |
| `DB_PASS` | Cisco database password |
| `DB_PORT` | Database port — CCX default: `1504`; CCE default: `1433` |
| `DB_USERNAME` | Cisco database username |
| `LOG_LEVEL` | Log verbosity: `INFO` (default) or `DEBUG` |
| `REDIS_DB` | Redis database index (0–16) for storing call IDs |
| `REDIS_HOST` | Redis server IP; use `localhost` if Redis is on the same server |
| `REDIS_PASS` | Redis password |
| `REDIS_PORT` | Redis port (default: `6379`) |
| `REDIS_DELAY` | Minutes between Redis call result checks |
| `SERVICE_ID` | Service Identifier from EF CX Unified Admin channel settings |

### Step 4: Start the container

```bash
docker compose up -d
```

Verify the container is running:

```bash
docker ps
```

Check logs:

```bash
docker logs -f cisco-outbound-connector
```

---

## Related Articles

- [Cisco Outbound Connector — Kubernetes Deployment](Cisco-Outbound-Connector-Kubernetes-Deployment.md)
- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
