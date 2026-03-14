---
title: "WFM Component Deployment Guide"
summary: "Procedures for deploying the Workforce Management (WFM) microservices — including Auth, Core, and Reports — on a Kubernetes cluster."
audience: [partner]
product-area: [workforce-management]
doc-type: how-to
difficulty: advanced
aliases: []
last-updated: 2026-03-11
---

# WFM Component Deployment Guide

ExpertFlow WFM is a suite of microservices that handle scheduling, forecasting, and real-time adherence. These components are deployed on Kubernetes using Helm or standard YAML manifests.

## 1. Prerequisites

Ensure the following dependencies are available in your cluster:
- **Keycloak:** For authentication and identity management.
- **PostgreSQL:** To store WFM core data and configurations.
- **ExpertFlow CX Core:** WFM must be able to communicate with the `conversation-manager`.
- **Redis:** Used for caching and real-time state management.

---

## 2. Component 1: WFM-Auth (Security Layer)

The WFM-Auth component manages the secure token exchange between WFM and the platform's Keycloak instance.

### Deployment Steps
1.  **Configure environment variables:**
    *   `KC_URL`: The FQDN of your Keycloak server.
    *   `KC_REALM`: The ExpertFlow realm name.
    *   `KC_CLIENT_ID`: The WFM client ID registered in Keycloak.
2.  **Execute Deployment:**
    ```bash
    kubectl apply -f wfm-auth-deployment.yaml
    ```
3.  **Verify:** Check that the service is reachable on port `8080`.

---

## 3. Component 2: WFM-Core (Business Logic)

This is the central microservice for WFM operations.

### Deployment Steps
1.  **Configure DB Connection:** Ensure the `DB_URL` points to your WFM database in PostgreSQL.
2.  **Helm Install:**
    ```bash
    helm upgrade --install wfm-core expertflow/wfm-core \
      --namespace expertflow \
      --set database.password=your_password
    ```
3.  **Validation:** Verify that the `wfm-core` pod status is `Running`.

---

## 4. Component 3: WFM-Reports (Analytics)

This component aggregates data from WFM-Core for reporting and forecasting.

### Deployment Steps
1.  **Database Sync:** WFM-Reports requires read access to the `wfm-core` database and write access to its own `wfm-reports` schema.
2.  **Apply Manifests:**
    ```bash
    kubectl apply -f wfm-reports-deployment.yaml
    ```
3.  **Verification:** Access the logs to ensure the reporting scheduler is initialized.

---

## 5. Post-Deployment Troubleshooting

*   **Connectivity Issues:** If WFM-Core cannot connect to PostgreSQL, verify that the `pg_hba.conf` on the DB server allows the Kubernetes node IPs.
*   **Auth Failures:** Ensure the `KC_CLIENT_SECRET` matches exactly what is configured in Keycloak for the WFM client.

---

## Related Guides
*   [WFM Overview](../Functional_Areas/Workforce_Schedule_Management/Workforce-Management-Overview.md)
*   [WFM Prerequisites](../Functional_Areas/Workforce_Schedule_Management/WFM-Prerequisites.md)
*   [WFM User Guide for Supervisors](../Supervisor/WFM-Admin-Supervisor-Guide.md)
