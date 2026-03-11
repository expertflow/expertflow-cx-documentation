---
title: "Voice Recording Components Deployment Guide"
summary: "Detailed instructions for deploying the Recording Link Uploader and Middleware components to enable call recording playback and management."
audience: [partner]
product-area: [voice, quality-management]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# Voice Recording Components Deployment Guide

The ExpertFlow CX Voice Recording solution consists of two primary microservices: the **Recording Link Uploader** (which pushes metadata to CX) and the **Recording Middleware** (which serves the audio files for playback).

## 1. Prerequisites

### Software Requirements
| Item | Recommended |
| :--- | :--- |
| **Operating System** | Debian 12 |
| **MongoDB** | Latest stable version |
| **ExpertFlow CX** | Latest version deployed on Kubernetes |
| **Media Server** | Latest EFSwitch (FreeSWITCH) version |
| **Secondary FQDN** | A separate FQDN (e.g., `middleware.expertflow.com`) routed to the Media Server |

### Network & Port Requirements
Ensure these ports are open on the Media Server:

| Port | Description |
| :--- | :--- |
| **27017** | MongoDB Access |
| **5432** | PostgreSQL Access (Media Server DB) |
| **6115** | Middleware API Access |

---

## 2. Database Preparation

### Configure PostgreSQL Access
The Recording Uploader needs to read call metadata from the Media Server's PostgreSQL database (`fusionpbx`).

1.  Enable remote listening in `postgresql.conf`: `listen_addresses = '*'`.
2.  Allow the Uploader IP in `pg_hba.conf`: `host all all 0.0.0.0/0 md5`.
3.  Restart PostgreSQL: `systemctl restart postgresql`.

### Create MongoDB Database
The Uploader uses MongoDB to track which recording links have already been processed.

1.  Access MongoDB: `mongosh --host <IP> --port 27017`.
2.  Create the database and user:
    ```javascript
    use recording-link-activities
    db.createUser({
      user: "efcx",
      pwd: "your_secure_password",
      roles: []
    })
    ```

---

## 3. Component Deployment (Docker)

### Recording Link Uploader
This component monitors the Media Server's file system and pushes links to the CX Conversation Manager.

1.  **Create directory:** `mkdir recording-link-uploader && cd recording-link-uploader`.
2.  **`docker-compose.yml`:**
    ```yaml
    version: "3.8"
    services:
      recording-link-uploader:
        image: gitimages.expertflow.com/voice-recording-solution/recording-link-activities:TAG
        container_name: recording-link-uploader
        env_file: ./env.txt
        volumes:
          - /var/lib/freeswitch/recordings/:/var/lib/freeswitch/recordings/
        restart: no
    ```
3.  **Configure `env.txt`:** Ensure `CX_FQDN`, `MONGODB_HOST`, and `DB_IP` are set correctly.

### Recording Middleware
This component handles requests from the Agent Desk to play or download recording files.

1.  **Create directory:** `mkdir recording-middleware && cd recording-middleware`.
2.  **`docker-compose.yml`:**
    ```yaml
    services:
      recording-middleware:
        image: gitimages.expertflow.com/voice-recording-solution/recording-middleware:TAG
        container_name: recording-middleware
        ports:
          - 6115:8080
        env_file: ./env.txt
        volumes:
          - /var/lib/freeswitch/recordings/:/var/lib/freeswitch/recordings/
        restart: always
    ```

---

## 4. Kubernetes Integration (Ingress Setup)

To allow the CX platform to access the middleware on the Media Server, you must create a Service and Ingress on your K8s cluster.

### `ef-recording-middleware.yaml`
```yaml
apiVersion: v1
kind: Service
metadata:
  name: efswitch-service
spec:
  ports:
  - name: https
    port: 6115
    targetPort: 6115
---
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: efswitch-service-1
  labels:
    kubernetes.io/service-name: efswitch-service
addressType: IPv4
endpoints:
  - addresses: ["<MEDIA-SERVER-IP>"]
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: efswitch-service
spec:
  rules:
  - host: <SECONDARY-FQDN>
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: efswitch-service
            port: { number: 6115 }
```
Apply the configuration: `kubectl apply -f ef-recording-middleware.yaml`.

---

## Related Guides
*   [CX Voice Deployment Overview](CX-Voice-Deployment.md)
*   [Managing the QA Workflow](../QM/Managing-the-Quality-Assurance-Workflow.md)
