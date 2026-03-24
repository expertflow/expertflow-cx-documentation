---
title: "Monitoring the Platform"
summary: "How-to guide for platform operators — covers the key health checks, log locations, alerting setup, and dashboards for keeping an ExpertFlow CX deployment healthy."
audience: [administrator, hosting-partner, platform-operator]
doc-type: how-to
difficulty: intermediate
keywords: [monitoring, health checks, platform operations]
aliases: []
last-updated: 2026-03-24
status: placeholder
---

# Monitoring the Platform

> **Placeholder** — This document needs to be written. See the outline below for intended content.

This guide covers day-to-day monitoring responsibilities for platform operators — administrators and hosting partners responsible for keeping an ExpertFlow CX deployment healthy.

## Prerequisites

- kubectl access to the RKE2 cluster
- Access to the observability stack (OpenSearch / Grafana / Superset — whichever is deployed)

## Key Components to Monitor

| Component | What to watch | Normal range |
| --- | --- | --- |
| CX Router | Queue depth, conversation latency | TBD |
| Media Server | Active calls, SIP registration | TBD |
| MongoDB | Replication lag, slow queries | TBD |
| Redis | Memory usage, eviction rate | TBD |
| Kubernetes nodes | CPU, memory, disk | TBD |

## Checking Cluster Health

```bash
# Node status
kubectl get nodes

# Pod status (all namespaces)
kubectl get pods -A | grep -v Running
```

## Reading Application Logs

- How to access logs via OpenSearch / Kibana
- Most important log streams and what errors to watch for
- Cross-reference: [Logging and Tracing with OpenSearch](../Developer_Integrator/Logging-and-Tracing-OpenSearch.md)

## Alerting Setup

- Recommended alert thresholds
- How to configure Superset alerts
- Cross-reference: [Superset Alerts and Reports Enablement](../Administrator/Superset-Alerts-Reports-Enablement.md)

## Routine Health Check Checklist

- [ ] All pods in Running state
- [ ] MongoDB replication healthy
- [ ] Redis memory within limits
- [ ] No recurring ERROR patterns in application logs
- [ ] SIP registrations stable (if voice is enabled)
- [ ] Disk usage below 75% on all nodes
