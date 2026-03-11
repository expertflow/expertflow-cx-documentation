---
title: "CX Dialer Deployment Guide"
summary: "Technical instructions for deploying the Outbound Dialer component using Docker Compose, including PostgreSQL database setup and network configuration."
audience: [partner]
product-area: [voice, outbound]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# CX Dialer Deployment Guide

The ExpertFlow CX Outbound Dialer is responsible for automated outbound calling. It integrates with the EFSwitch (FreeSWITCH) and the Voice Connector to orchestrate proactive customer engagement.

## 1. Prerequisites

### Software Requirements
| Item | Recommended |
| :--- | :--- |
| **Operating System** | Debian 12 |
| **Docker** | v24 or higher |
| **PostgreSQL** | v13 or higher |
| **Media Server** | Latest EFSwitch version |
| **Voice Connector** | v4.5 or higher |

### Network & Port Requirements
Ensure the following ports are open between the Dialer server and other components:

| Type | Application | Description | Port |
| :--- | :--- | :--- | :--- |
| **TCP** | Media Server | Event Socket Layer (ESL) | 8021 |
| **TCP** | Media Server | WebSocket Port | 7443 |
| **TCP** | Dialer | API/Access Port | 6666 |
| **TCP** | PostgreSQL | Database Access | 5432 |

---

## 2. PostgreSQL Database Setup

The Dialer requires a dedicated table in PostgreSQL to manage contact lists and call states.

### Configure PostgreSQL Access
1.  Edit `postgresql.conf` (usually in `/etc/postgresql/<version>/main/`):
    *   Set `listen_addresses = '*'` to allow remote connections.
2.  Edit `pg_hba.conf`:
    *   Add the following line to the bottom: `host all all 0.0.0.0/0 md5`.
3.  Restart the service:
    ```bash
    systemctl restart postgresql
    ```

### Create Database and User
1.  Access the PostgreSQL prompt:
    ```bash
    su - postgres
    psql
    ```
2.  Execute the following SQL commands:
    ```sql
    CREATE USER efswitch WITH PASSWORD 'your_secure_password';
    CREATE DATABASE efcx;
    ALTER DATABASE efcx OWNER TO efswitch;
    GRANT ALL PRIVILEGES ON DATABASE efcx TO efswitch;
    ```
3.  Initialize the schema:
    Connect to the `efcx` database as the `efswitch` user and run:
    ```sql
    CREATE TABLE contacts (
        id varchar(40) PRIMARY KEY NOT NULL,
        customer_number varchar(20) NOT NULL,
        campaign_type varchar(20) NOT NULL,
        ivr varchar(20),
        gateway_id varchar(40) NOT NULL,
        tenant_id varchar(40) NOT NULL,
        status varchar(20),
        call_result varchar(40),
        received_time timestamp with time zone,
        dial_time timestamp with time zone,
        campaign_id varchar(40) NOT NULL,
        campaign_contact_id varchar(40),
        start_time timestamp with time zone,
        end_time timestamp with time zone,
        priority integer,
        dialing_mode varchar(20),
        routing_mode varchar(20),
        resource_id varchar(40),
        queue_name varchar(20)
    );
    ```

---

## 3. Container Deployment

The Dialer is deployed as a Docker container.

### Create Deployment Directory
```bash
mkdir outbound-dialer && cd outbound-dialer
```

### Configure `docker-compose.yml`
Create a `docker-compose.yml` file with the following structure:
```yaml
version: "3"
services:
  outbound-dialer:
    image: gitimages.expertflow.com/rtc/outbound-dialer:TAG
    container_name: outbound-dialer
    ports:
      - 6666:8080
    env_file:
      - docker-variables.env
    restart: always
```
*Note: Replace `TAG` with the specific version from the release notes.*

### Configure Environment Variables
Create a `docker-variables.env` file. Key parameters include:

| Variable | Description | Default/Example |
| :--- | :--- | :--- |
| `DB_URL` | IP of the PostgreSQL server | `192.168.1.10` |
| `DB_USERNAME` | Dialer DB username | `efswitch` |
| `DB_PASS` | Dialer DB password | `your_secure_password` |
| `ESL_IP` | IP of the EFSwitch server | `192.168.1.10` |
| `ESL_PORT` | FreeSWITCH ESL port | `8021` |
| `ESL_PASSWORD` | FreeSWITCH ESL password | `ClueCon` |
| `VOICE_CONNECTOR` | URL of the Voice Connector | `http://192.168.1.10:8115` |
| `MAX_CONCURRENT_CALLS`| Limit for active calls | `10` |

---

## 4. Launch and Verification

1.  Login to the ExpertFlow registry:
    ```bash
    docker login gitimages.expertflow.com
    ```
2.  Start the container:
    ```bash
    docker compose up -d
    ```
3.  Verify the logs:
    ```bash
    docker logs -f outbound-dialer
    ```
    Ensure the logs show a successful connection to both the Database and the EFSwitch ESL.

---

## Related Guides
*   [Voice Connector Deployment](Voice-Connector-Deployment-Guide.md)
*   [Media Server Configuration](../Solution_Admin/Media-Server-Configuration-CX-Voice.md)
