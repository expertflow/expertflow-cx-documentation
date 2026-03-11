---
title: "Environment Configurations for Cisco"
summary: "How-to guide for configuring the AgentDesk Helm chart values to enable Cisco UCCX/UCCE integration with ExpertFlow CX — covering all CTI configuration variables, SSO, HA, RONA, encrypted credentials, and the hostAliases fix for Finesse DNS resolution."
audience: [integrator, partner]
product-area: [voice, channels]
doc-type: how-to
difficulty: intermediate
keywords: ["Cisco UCCX UCCE Helm config CX", "Cisco Finesse values.yaml CX", "isCiscoEnabled CX", "Cisco CTI config CX", "Finesse HA config CX", "CISCO_SERVICE_IDENTIFIER CX"]
aliases: ["Cisco Helm config CX", "Finesse AgentDesk config CX", "Cisco environment variables CX"]
last-updated: 2026-03-10
---

# Environment Configurations for Cisco

This guide covers the `values.yaml` changes required in the **AgentDesk Helm chart** to enable Cisco UCCX or UCCE integration with ExpertFlow CX.

---

## Step 1: Update CTI Configuration Variables

Open your `helm-values/cx-agent-desk-custom-values.yaml` file and update the following variables under the unified-agent configurations section:

```yaml
# Enable Cisco contact center integration
isCiscoEnabled: "true"

# Primary Cisco Finesse domain name
domain: "<finesse domain>"

# Secondary Cisco Finesse domain name (leave blank if no secondary)
subDomain: "<secondary finesse domain>"

# Primary Cisco Finesse BOSH URL
boshUrl: "<finesse bosh api URL>"

# Secondary Cisco Finesse BOSH URL (leave blank if no secondary)
subBoshUrl: "<secondary finesse bosh api URL>"

# SSO backend URL (only if Finesse SSO is enabled)
ssoBackendUrl: "<SSO backend URL>"

# Cisco UCC flavor — UCCE for all UCCE/PCCE deployments; UCCX for all UCCX deployments
finesseFlavor: "[UCCE|UCCX]"

# RONA timeout reason as configured in Cisco Finesse
ronaStateOnCisco: "<call timeout reason configured on finesse>"

# Enable Finesse HA mode
IS_FINESSE_HA_ENABLED: true

# Primary Cisco Finesse FQDN or IP address
finesseURLForAgent: "https://[Cisco-Finesse-FQDN/IP]"

# Secondary Cisco Finesse FQDN or IP address (HA only)
SECONDARY_FINESSE_URL: "https://[Secondary-Finesse-FQDN/IP]"

# Static channel identifier for the CISCO_CC channel type in CX
CISCO_SERVICE_IDENTIFIER: "<static identifier to use as channel identifier>"
```

### Variable Reference

| Variable | Description |
|---|---|
| `isCiscoEnabled` | Set to `"true"` to enable Cisco integration |
| `domain` | Primary Cisco Finesse domain name |
| `subDomain` | Secondary Finesse domain (leave blank if not HA) |
| `boshUrl` | Primary Finesse BOSH API URL |
| `subBoshUrl` | Secondary Finesse BOSH URL (leave blank if not HA) |
| `ssoBackendUrl` | SSO backend URL (only if Finesse is SSO-enabled) |
| `finesseFlavor` | `UCCE` for UCCE/PCCE deployments; `UCCX` for UCCX |
| `ronaStateOnCisco` | RONA timeout reason code as configured on Finesse |
| `IS_FINESSE_HA_ENABLED` | `true` if Finesse is running in HA mode |
| `finesseURLForAgent` | Primary Finesse FQDN or IP |
| `SECONDARY_FINESSE_URL` | Secondary Finesse FQDN or IP (HA only) |
| `CISCO_SERVICE_IDENTIFIER` | Static identifier used as the channel identifier for `CISCO_CC` channel type |

---

## Step 2: Add Encrypted Credentials

The `cf-admin` credentials must be encrypted using the ExpertFlow encryption utility. Share the plain-text `cf-admin` credentials with the ExpertFlow support team. They will provide the encrypted values to add:

```yaml
ctiParam: "<Encrypted cf admin username>"
ctiParam2: "<Encrypted cf admin password>"
```

---

## Step 3: Deploy the AgentDesk Chart

```bash
helm upgrade --install --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" \
  cx-agent-desk --debug \
  --values helm-values/cx-agent-desk-custom-values.yaml \
  expertflow/agent-desk
```

---

## Troubleshooting: Finesse DNS Resolution

If `agent-manager` cannot connect to Finesse (DNS resolution failure), add a `hostAliases` entry to the **Core Helm chart** `values.yaml` under `agent-manager`:

```yaml
hostAliases:
  - ip: "192.168.1.33"
    hostnames:
      - "uccx12-5p.ucce.ipcc"
```

Replace the IP and hostname with your actual Finesse server values.

---

## Related Articles

- [Cisco Voice Channel Configuration](Cisco-Voice-Channel-Configuration.md)
- [Cisco Contact Center Integration Reference](Cisco-Contact-Center-Integration-Reference.md)
- [Synchronizing Cisco Users and Teams](Synchronizing-Cisco-Users-and-Teams.md)
- [Finesse Integration Prerequisites](Finesse-Integration-Prerequisites.md)
