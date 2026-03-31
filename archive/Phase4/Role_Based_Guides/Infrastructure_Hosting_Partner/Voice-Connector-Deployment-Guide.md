---
title: "Voice Connector Deployment Guide"
summary: "Step-by-step instructions for deploying the Unified Voice Connector using Docker Compose, including ESL connectivity and security settings."
audience: [partner]
product-area: [voice]
doc-type: how-to
difficulty: intermediate
aliases: []
last-updated: 2026-03-11
---

# Voice Connector Deployment Guide

The Unified Voice Connector acts as a bridge between the Media Server (FreeSWITCH) and the ExpertFlow CX Core. It translates telephony events into CX interaction events.

## 1. Prerequisites

### Software Requirements
| Item | Recommended |
| :--- | :--- |
| **Operating System** | Debian 12 |
| **Docker** | v24 or higher |
| **Media Server** | Latest EFSwitch version |
| **ExpertFlow CX** | Latest version deployed on Kubernetes |

### Network & Port Requirements
The following ports must be accessible from the Voice Connector container:

| Port | Description | Target Component |
| :--- | :--- | :--- |
| **8021** | ESL (Event Socket Layer) | Media Server |
| **7443** | Secure WebSocket | Media Server |
| **8115** | API Access (Incoming) | Voice Connector Port |
| **6666** | Dialer API | Outbound Dialer |

---

## 2. Container Deployment

### Create Deployment Directory
```bash
mkdir voice-connector && cd voice-connector
```

### Configure `docker-compose.yml`
Create a `docker-compose.yml` file:
```yaml
version: "3.8"
services:
  voice-connector:
    image: gitimages.expertflow.com/freeswitch/ecx_generic_connector:TAG
    container_name: unified-voice-connector
    ports:
      - 8115:8080
    env_file:
      - ./env.txt
    deploy:
      resources:
        limits:
          memory: 1024m
        reservations:
          memory: 256m
    restart: always
```
*Note: Replace `TAG` with the specific image version from the ExpertFlow release notes.*

### Configure Environment Variables
Create an `env.txt` file with the following parameters:

| Variable | Description | Example Value |
| :--- | :--- | :--- |
| `CX_FQDN` | The FQDN of your CX platform | `https://cim.expertflow.com` |
| `ESL_PORT` | FreeSWITCH ESL port | `8021` |
| `ESL_PASSWORD` | FreeSWITCH ESL password | `MyEslPass` |
| `DIALER_API` | Dialer API URL | `http://192.168.1.10:6666` |
| `AUTH_ENABLED` | Enable API authentication | `true` |
| `API_USERNAME` | Keycloak API Username | `admin` |
| `API_PASS` | Keycloak API Password | `password` |
| `ROOT_DOMAIN` | The root domain for multi-tenancy | `expertflow.com` |

---

## 3. Launch and Verification

1.  Login to the ExpertFlow registry:
    ```bash
    docker login gitimages.expertflow.com
    ```
2.  Start the service:
    ```bash
    docker compose up -d
    ```
3.  Check the logs to ensure successful ESL connection:
    ```bash
    docker logs -f unified-voice-connector
    ```
    Look for: `Successfully connected to FreeSWITCH ESL`.

---

## Related Guides
*   [CX Voice Deployment Overview](CX-Voice-Deployment.md)
*   [CX Dialer Deployment Guide](CX-Dialer-Deployment-Guide.md)
*   [Media Server Configuration Reference](../Solution_Admin/Media-Server-Configuration-CX-Voice.md)
