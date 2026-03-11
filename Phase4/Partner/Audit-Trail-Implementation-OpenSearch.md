---
title: "Audit Trail Implementation (OpenSearch Pattern)"
summary: "Tutorial for implementing a centralized audit trail using the OpenSearch pattern. Note: OpenSearch is an optional pattern; partners may use any equivalent SIEM or logging solution."
audience: [partner, integrator]
product-area: [platform, security]
doc-type: tutorial
difficulty: advanced
last-updated: 2026-03-11
---

# Audit Trail Implementation (OpenSearch Pattern)

This tutorial demonstrates how to implement a centralized audit trail for ExpertFlow CX using the **OpenSarch Pattern**. 

> **Important Architecture Note:** The OpenSearch stack is provided as an optional reference pattern for SIEM (Security Information and Event Management) and Audit Trail compliance. Partners and customers are free to use any equivalent logging solution (e.g., Splunk, ELK, Azure Monitor) by configuring the platform's Fluent Bit outputs accordingly.

## 1. The Audit Trail Architecture
The ExpertFlow platform generates audit events for all administrative actions. These events are captured by **Fluent Bit** and can be forwarded to your preferred security repository. In this pattern, we use OpenSearch as the repository.

### **Workflow Overview:**
1.  **Event Generation:** CX Core components emit JSON audit logs.
2.  **Collection:** Fluent Bit (running as a DaemonSet) picks up these logs.
3.  **Forwarding:** Fluent Bit pushes logs to the OpenSearch API.
4.  **Visualization:** OpenSearch Dashboards provide the UI for security audits.

---

## 2. Step-by-Step Implementation

### Step 1: Deploy the OpenSearch Stack
Follow the standard Helm-based deployment for OpenSearch in your preferred namespace (e.g., `logging`). Ensure the cluster status is **Green** before proceeding.

### Step 2: Configure the Audit Index
In OpenSearch Dashboards, create an index pattern named `audit-logs-*`. This will allow you to query data across daily or monthly indices.

### Step 3: Configure the Fluent Bit Output
Update your ExpertFlow Fluent Bit configuration to point to your OpenSearch endpoint. 

**Example `OUTPUT` configuration:**
```ini
[OUTPUT]
    Name            opensearch
    Match           audit.*
    Host            opensearch-cluster-master.logging.svc.cluster.local
    Port            9200
    Index           audit_log_index
    HTTP_User       admin
    HTTP_Passwd     your_secure_password
    tls             On
    tls.verify      Off
```

---

## 3. Verification & Compliance
Once configured, navigate to the **Discover** tab in OpenSearch Dashboards. You should see incoming events with the following critical metadata:
*   `timestamp`: When the action occurred.
*   `actor`: Which user performed the change.
*   `action`: What change was made (e.g., "Updated Queue Routing").
*   `result`: Success or Failure.

---

## Related Guides
*   [Logging and Tracing Integration Reference](../Integrator/Logging-and-Tracing-OpenSearch.md)
*   [Managing Audit Logs](../Functional_Areas/Security_Compliances/Audit-Logging.md)
*   [Platform Security Overview](../Decision_Maker/Security-and-Compliance-Whitepaper.md)
