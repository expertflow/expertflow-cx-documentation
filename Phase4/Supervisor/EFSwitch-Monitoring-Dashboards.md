---
title: "EFSwitch Monitoring Dashboards"
summary: "How-to guide for deploying EFSwitch Grafana monitoring dashboards in ExpertFlow CX — covering repository cloning, namespace creation, Prometheus scrape config with EFSwitch IP, Helm upgrade, and dashboard verification."
audience: [supervisor, solution-admin]
product-area: [voice]
doc-type: how-to
difficulty: advanced
keywords: ["EFSwitch monitoring CX", "EFSwitch Grafana dashboard", "Prometheus EFSwitch CX", "monitoring dashboard CX voice", "FreeSWITCH monitoring", "EFSwitch node exporter", "Helm monitoring CX", "CX monitoring solution"]
aliases: ["EFSwitch dashboards CX", "monitoring EFSwitch CX", "CX voice monitoring dashboards"]
last-updated: 2026-03-10
---

# EFSwitch Monitoring Dashboards

This guide explains how to deploy EFSwitch monitoring dashboards in the ExpertFlow CX monitoring solution. Dashboards are served via Grafana and pull metrics from Prometheus exporters running on the EFSwitch node.

## Prerequisites

- Monitoring solution already deployed. If not, complete the Monitoring Solution Deployment guide first.
- Helm installed and configured for your Kubernetes cluster.
- EFSwitch IP address available.

---

## Step 1: Clone the ExpertFlow CX Repository

```bash
git clone -b CX-4.9_f-CCC-1678 \
  https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git \
  CX-4.9_f-CCC-1678
```

---

## Step 2: Create the Monitoring Namespace

```bash
kubectl create ns monitoring
cd cim-solution/kubernetes/monitoring
```

---

## Step 3: Configure EFSwitch IP in values.yaml

Update the `additionalScrapeConfigs` section in `values.yaml` with your EFSwitch node IP address so Prometheus can collect metrics from the exporters:

```yaml
additionalScrapeConfigs:
  - job_name: "node"
    static_configs:
      - targets: ["<EFSwitch-IP>:9100"]
  - job_name: 'freeswitch'
    static_configs:
      - targets: ["<EFSwitch-IP>:9282"]
  - job_name: 'fusionpbx'
    scrape_interval: 60s
    static_configs:
      - targets: ['<EFSwitch-IP>:8080']
```

Replace `<EFSwitch-IP>` with your actual EFSwitch server IP address.

---

## Step 4: Replace Domain in values.yaml

Replace all occurrences of the default domain (`devops.ef.com`) with your actual FQDN:

```bash
sed -i -e 's/devops.ef.com/<YOUR-FQDN>/g' values.yaml
```

---

## Step 5: Deploy / Upgrade the Monitoring Solution

Run the following Helm command to install or upgrade the monitoring solution with the updated configuration:

```bash
helm upgrade --namespace monitoring --install=true \
  kube-stack-prometheus --values=values.yaml .
```

---

## Step 6: Verify the Dashboards

Open Grafana in your browser:

```
https://<FQDN>/monitoring
```

Search for dashboards with names containing **"EFSwitch"** to confirm each dashboard is displaying data correctly.

---

## Related Articles

- [Accessing CX Voice Components](../Solution_Admin/Accessing-CX-Voice-Components.md)
- [Media Server Configuration CX Voice](../Solution_Admin/Media-Server-Configuration-CX-Voice.md)
- [Monitoring Your Team in Real Time](Monitoring-Your-Team-in-Real-Time.md)
