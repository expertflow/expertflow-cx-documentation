---
title: "Setting Up CX Analyser Reports"
summary: "Clinical step-by-step guide for importing report definitions and configuring the reporting scheduler after core platform deployment."
audience: [platform-operator]
product-area: [reporting, analytics]
doc-type: how-to
difficulty: advanced
last-updated: 2026-03-11
---

# Setting Up CX Analyser Reports

This guide details the mandatory "Day 1" and "Day 2" steps required to enable historical reporting in ExpertFlow CX. 

> **Mandatory Prerequisite:** You must have already completed the [CX-Analyser Infrastructure Setup](CX-Analyser-Infrastructure-Setup.md) (TLS certificates and SQL database schemas) before proceeding with this guide.

---

## 1. Day 1: Enabling the Reporting Scheduler
The Reporting Scheduler is the "heart" of the analytics engine. It must be activated immediately after the core Helm chart deployment.

1.  **Configure Cron Jobs:** In your `values.yaml` for the Reporting Scheduler, ensure the intervals for ETL (Extract, Transform, Load) processes are defined (e.g., every 15 minutes).
2.  **Verify Pod Connectivity:** Check the logs of the `reporting-scheduler` pod to ensure it can successfully connect to the SQL database initialized in the infrastructure phase.
    ```bash
    kubectl logs -f <reporting-scheduler-pod> -n <tenant-ns>
    ```
3.  **Validate Data Sync:** Ensure that the first batch of interaction records has moved from MongoDB to the relational SQL tables.

---

## 2. Day 2: Importing Report Definitions
Once the data pipeline is operational, the Solution Admin (Olivia) or Integrator (Ian) must import the specific report templates into the visualization engine (Superset).

### Step-by-Step Import:
1.  **Download Templates:** Obtain the `.zip` or `.yaml` report definition files from the ExpertFlow release package.
2.  **Access Superset:** Log in to the Superset UI.
3.  **Import Dashboard:**
    *   Navigate to **Dashboards**.
    *   Click the **Import Dashboard** icon (up arrow).
    *   Upload the template file and select the target SQL database as the data source.
4.  **Assign Permissions:** Ensure the correct supervisor groups have access to view these dashboards.

---

## 3. Post-Setup Verification
A successful setup is confirmed when:
*   [ ] The SQL table `ConversationActivities` is populating with new interaction IDs.
*   [ ] The Superset dashboard displays "Live" interaction counts for the current day.
*   [ ] There are no `connection_refused` errors in the Reporting Connector logs.

---

## Related Guides
*   [CX-Analyser Infrastructure Setup](CX-Analyser-Infrastructure-Setup.md)
*   [Superset Reports Configuration](../Administrator/Superset-Reports-Configuration.md)
*   [Historical Reports Reference](../Supervisor_and_QA_Lead/Historical-Reports-Reference.md)
