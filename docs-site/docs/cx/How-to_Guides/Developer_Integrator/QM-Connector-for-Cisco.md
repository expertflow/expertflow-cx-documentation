---
title: "QM Connector for Cisco"
summary: "How-to guide for deploying the ExpertFlow CX QM Connector for Cisco Contact Center — covering prerequisites, Unified Admin channel configuration, Helm deployment, and environment variable reference."
audience: [developer-integrator]
product-area: [voice]
doc-type: how-to
difficulty: advanced
keywords: ["QM connector Cisco CX", "quality management Cisco CX", "Cisco call recording QM", "VRS QM connector deployment", "qm-connector Helm CX", "Cisco UCCE QM CX", "QM connector environment variables"]
aliases: ["QM connector Cisco", "Cisco QM integration CX", "deploy QM connector CX"]
last-updated: 2026-03-10
---

# QM Connector for Cisco

The QM Connector is an **optional** component that enables Quality Management on conversations handled through Cisco Contact Center. It pulls call recordings from the Voice Recording Solution (VRS) and pushes them as conversations into ExpertFlow CX.

> Deploy this connector only if you intend to perform QM on Cisco Contact Center interactions.

## Prerequisites

- VRS for Cisco installed and operational (see the VRS for Cisco Installation Guide)
- ExpertFlow CX deployed with QM module enabled
- Access to the UCCE `awdb` database
- Helm and kubectl access to the ExpertFlow namespace

---

## Step 1: Configure Channels in Unified Admin

Create two channels of type `CISCO_CC` — one for inbound and one for outbound.

**Inbound channel:**
- Set **Service Identifier** to match the DN used for dialing.

**Outbound channel:**
1. Select a 4–5 digit number as the Service Identifier.
2. Set this value as `UCCE_OB_SERVICE_IDENTIFIER` in `helm-values/cx-qm-custom-values.yaml`.
3. Set **Routing Mode** to `External`.
4. Set **Channel Mode** to `HYBRID`.

**Create the VRS Keycloak user:**
1. In Keycloak, create a new user with **username** and **password** set to `vrs`.
2. Assign all **21 realm-management roles** to this user.
3. Set `KEYCLOAK_USERNAME` and `KEYCLOAK_PASSWORD` in `values.yaml` accordingly.

---

## Step 2: Deploy the QM Connector

### Enable the QM Connector

In `helm-values/cx-qm-custom-values.yaml`, set the `enabled` flag to `true` for the `qm-connector` component.

### Configure Environment Variables

Update the following environment variables in `helm-values/cx-qm-custom-values.yaml`:

| Variable | Description | Example |
|---|---|---|
| `RECORDING_SERVER_FQDN` | IP address of the VRS recording server | — |
| `EFCX_FQDN` | Fully qualified domain name of ExpertFlow CX | `https://efcx-qm.expertflow.com/` |
| `CALL_BACK_URL` | Webhook URL for conversation creation | — |
| `UCCE_ENGINE` | UCCE database engine | `sqlserver` |
| `UCCE_IP` | UCCE server IP | — |
| `UCCE_PORT` | UCCE database port | — |
| `UCCE_DATABASE` | UCCE `awdb` database name | — |
| `UCCE_USERNAME` | UCCE `awdb` database username | — |
| `UCCE_PASSWORD` | UCCE `awdb` database password | — |
| `UCCE_OB_SERVICE_IDENTIFIER` | Service Identifier for outbound calls | `8899` |
| `KEYCLOAK_REALM_NAME` | Keycloak realm name | `expertflow` |
| `KEYCLOAK_CLIENT_ID` | Keycloak client ID | `cim` |
| `KEYCLOAK_CLIENT_SECRET` | Keycloak client secret | — |
| `KEYCLOAK_USERNAME` | Keycloak user with all realm-management roles | `vrs` |
| `KEYCLOAK_PASSWORD` | Password for the Keycloak VRS user | `vrs` |
| `KEYCLOAK_AGENT_ROLE_NAME` | Role assigned to new agents created by QM Connector | `agent` |
| `KEYCLOAK_AGENT_ROLE_ID` | Role ID for the agent role | — |
| `DB_NAME` | VRS database name | — |
| `DB_USER` | VRS database username | — |
| `DB_PASSWORD` | VRS database password | — |
| `DB_ENGINE` | VRS database engine | `sqlserver` |
| `DB_HOST` | VRS database hostname or IP | — |
| `DB_PORT` | VRS database port | — |
| `DB_DRIVER` | JDBC driver for VRS database | `com.microsoft.sqlserver.jdbc.SQLServerDriver` |
| `CALL_START_DATE` | Cutoff date — only TCD records after this date are fetched | `2025-01-01` |
| `MAX_BATCH_SIZE` | Max users to fetch from Keycloak per batch | `30000` |

### Run the Helm Deploy Command

```bash
helm upgrade --install \
  --namespace=expertflow \
  --set global.efCxReleaseName="ef-cx" \
  --version 4.10.0 \
  qm \
  --debug \
  --values=helm-values/cx-qm-custom-values.yaml \
  expertflow/qm
```

---

## Related Articles

- [Cisco Voice Channel Configuration](Cisco-Voice-Channel-Configuration.md)
- [Cisco Integration Known Limitations](Cisco-Integration-Known-Limitations.md)
- [Playing Screen Recordings in Quality Management](../Supervisor_and_QA_Lead/Playing-Screen-Recordings.md)
- [Finesse Integration Prerequisites](Finesse-Integration-Prerequisites.md)
