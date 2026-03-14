---
title: "Logging and Tracing Integration with OpenSearch"
summary: "Operations guide for integrating ExpertFlow CX audit logging with OpenSearch — covering OpenSearch cluster deployment, index and dashboard configuration, and Fluent Bit output plugin setup."
audience: [integrator, solution-admin]
product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["OpenSearch CX logging", "audit logging OpenSearch CX", "Fluent Bit OpenSearch CX", "CX log integration OpenSearch", "audit log index CX", "logging tracing CX", "OpenSearch dashboard CX", "Fluent Bit output CX"]
aliases: ["OpenSearch logging CX", "CX audit OpenSearch", "Fluent Bit CX logging"]
last-updated: 2026-03-10
---

# Logging and Tracing Integration with OpenSearch

This guide walks the operations team through integrating the ExpertFlow CX audit logging system with OpenSearch for centralized log storage, search, and visualization.

## Overview

The integration has three phases:

1. Deploy OpenSearch
2. Configure index, mappings, index patterns, and dashboards
3. Configure Fluent Bit to forward audit logs to OpenSearch

---

## Step 1: Deploy OpenSearch

Set up an OpenSearch cluster in your Kubernetes environment using the OpenSearch and OpenSearch Dashboards Deployment Guide.

**Key outputs after deployment:**

| Output | Value |
|---|---|
| OpenSearch cluster URL | `http://{{baseURL}}:9200` |
| OpenSearch Dashboards URL | `http://{{baseURL}}:5601` |
| Admin credentials | Configured during deployment |
| Cluster health | Must be GREEN before proceeding |

---

## Step 2: Configure Index, Mappings, and Dashboards

Follow the Index Configuration and OpenSearch Dashboard Setup Guide to create the audit logging index and visualizations.

**Key outputs after configuration:**

| Item | Value |
|---|---|
| Index name | `audit_log_index` |
| Index status | ACTIVE |
| Index pattern | `audit-logs-*` |
| Time field | `timestamp` |
| Visualization | Created |
| Search | Enabled, fields discoverable in Dashboards |

---

## Step 3: Configure Fluent Bit Output

Connect Fluent Bit to OpenSearch so audit logs are forwarded automatically.

Update the `OUTPUT` section in `helm-values/cx-fluent-bit-custom-values.yaml`:

```ini
[OUTPUT]
    Name            opensearch
    Match           audit.admin
    Host            [opensearch-host]
    Port            9200
    Index           audit_log_index
    HTTP_User       [opensearch-user]
    HTTP_Passwd     [opensearch-password]
    Logstash_Format Off
    Replace_Dots    On
    Suppress_Type_Name On
    Retry_Limit     5
    tls             [opensearch-tls-verification]
    tls.verify      Off
```

Replace `[opensearch-host]`, `[opensearch-user]`, and `[opensearch-password]` with your actual OpenSearch cluster values.

**Key outputs after Fluent Bit configuration:**

- Fluent Bit successfully connected to OpenSearch
- Audit logs arriving in the `audit_log_index`
- Index naming pattern functioning correctly
- No connection errors in Fluent Bit logs

---

## Related Articles

- [Audit Logging](../Functional_Areas/Security_Compliance/Audit-Logging.md)
- [Accessing Kubernetes Logs](../Solution_Admin/Accessing-Kubernetes-Logs.md)
- [RKE2 SSL Certificate Extension](../Solution_Admin/RKE2-SSL-Certificate-Extension.md)
