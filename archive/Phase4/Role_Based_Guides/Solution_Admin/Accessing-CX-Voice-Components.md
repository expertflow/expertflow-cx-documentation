---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Accessing CX Voice Components

This guide provides technical instructions for system administrators to access and monitor backend voice components (Media Server, Dialer, Voice Connector).

## SSH Access
Connect to your component servers using standard SSH:
```bash
ssh username@IP-addr
# Use 'su' if root access is required
```

## Firewall and Ports
- **Verify Status**: Use `sudo iptables -S` to see currently open ports.
- **Open a Port**: `sudo iptables -A INPUT -p tcp -m tcp --dport PORT -j ACCEPT`.
- **Save Changes**: `sudo iptables-save`.
- **Key Ports**: 8021 (ESL), 5432 (Postgres), and component-specific ports (e.g., 3001 for Voice Connector).

## Accessing Logs

### Media Server (Freeswitch)
Use the Freeswitch CLI to see live call signaling:
```bash
fs_cli -p YOUR_PASSWORD
# If connection fails, restart: systemctl restart freeswitch
```

### Dialer and Voice Connector
These components run in Docker. Find the container ID and follow the logs:
```bash
docker ps
docker logs -f [CONTAINER_ID]
```

### Core Components (K8s)
For CCM and other core services:
```bash
kubectl get pods -n expertflow
kubectl logs -f [POD_NAME] -n expertflow
```

## Troubleshooting Databases
Access the contacts database to verify dialer records:
```bash
psql -h 127.0.0.1 -p 5432 -U [USERNAME] -d [DB_NAME]
# Query example: SELECT * FROM contacts;
```
Ensure port 5432 is accessible from the Dialer/Voice Connector servers.
