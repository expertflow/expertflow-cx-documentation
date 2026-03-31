---
title: "LinkedIn Connector Deployment — Helm"
summary: "How-to guide for deploying the LinkedIn channel connector using Helm on Kubernetes — covering database creation, values.yaml configuration, Helm upgrade command, access token generation, and Unified Admin setup."
audience: [solution-admin]
product-area: [channels, digital]
doc-type: how-to
difficulty: advanced
keywords: ["LinkedIn connector deployment", "LinkedIn Helm deployment", "LinkedIn connector Kubernetes", "LinkedIn values.yaml", "LinkedIn database setup", "LinkedIn Helm chart", "LinkedIn CX deployment"]
aliases: ["deploy LinkedIn connector", "LinkedIn Helm setup", "LinkedIn connector install"]
last-updated: 2026-03-10
---

# LinkedIn Connector Deployment — Helm

This guide covers deploying the LinkedIn channel connector on a Kubernetes cluster using Helm — including database provisioning, Helm chart configuration, access token generation, and Unified Admin setup.

## Prerequisites

- Kubernetes cluster with ExpertFlow CX deployed (CX 4.10.3+).
- PostgreSQL (`ef-postgresql`) running in the `ef-external` namespace.
- Helm chart at `helm/Channels/` with `helm-values/cx-channels-custom-values.yaml` available.
- A LinkedIn App with **Standard Tier** (Community Management API) access. See [LinkedIn Account Onboarding](LinkedIn-Account-Onboarding.md).
- The `kubectl` and `helm` CLI tools available in your environment.

---

## Step 1: Create Required Databases

The LinkedIn connector requires two dedicated PostgreSQL databases. Create them by executing the following commands:

```bash
kubectl exec -it ef-postgresql-0 -n ef-external -- \
  psql -U sa -d postgres -c "CREATE DATABASE linkedinmetadata;"

kubectl exec -it ef-postgresql-0 -n ef-external -- \
  psql -U sa -d postgres -c "CREATE DATABASE linkedincommentmetadata;"
```

> When prompted for the PostgreSQL `sa` password, the default is `Expertflow123`.

---

## Step 2: Configure values.yaml

Edit the Helm channels values file to enable and configure the LinkedIn connector:

```bash
vi helm/Channels/values.yaml
```

Add or update the `linkedin-connector` section with the following configuration:

```yaml
##############################linkedin-connector##############################
linkedin-connector:
   enabled: true
   replicaCount: 1
   image:
      repository: project_dev/linkedinconnector
      tag: "4.10.1"
   efConnectionVars: true
   efEnvironmentVars: false
   containerPorts:
      - name: "http-li-9001"
        containerPort: 9001
   extraEnvVars:
      - name: http.connect.timeout.sec
        value: "500000"
      - name: http.read.timeout.sec
        value: "1000000"
      - name: http.request.timeout.sec
        value: "10000000"
      - name: enable.ssl.env
        value: "false"
      - name: linkedin.scheduler.fixed-rate
        value: "150"
      - name: LINKEDIN_CIM_SERVICE_ID
        value: "2001"
      - name: AUTO_SCHEDULER_STARTUP
        value: "true"
      - name: TZ
        value: '{{ .Values.global.efCommonVars_TZ }}'
      - name: LOGGING_CONFIG
        value: '{{ .Values.global.efCommonVars_LOGGING_CONFIG }}'
      - name: LINKEDIN_CIM_SERVICE_URL
        value: "http://{{ .Values.global.efCxReleaseName }}-ccm-svc.{{ .Release.Namespace }}.svc:8081"
      - name: LINKEDIN_CIM_FILE_ENGINE_URL
        value: "http://{{ .Values.global.efCxReleaseName }}-file-engine-svc.{{ .Release.Namespace }}.svc:8080"
      - name: FILE_ENGINE_BASE_FQDN
        value: "http://{{ .Values.global.efCxReleaseName }}-file-engine-svc.{{ .Release.Namespace }}.svc:8080"
      - name: MASKING_LAYOUT_CLASS
        value: "com.linkedin.connector.logging.MaskingPatternLayout"
      - name: DATABASE_URL
        value: jdbc:postgresql://ef-postgresql.ef-external.svc:5432/linkedinmetadata?sslmode=verify-ca&sslrootcert=/postgresql/ca.crt
      - name: DATABASE_USERNAME
        value: "sa"
      - name: DATABASE_PASSWORD
        value: "Expertflow123"
   siteEnvVars: []
   configKeys: []
   service:
      enabled: true
      port: 9001
      portName: "http-li-9001"
      targetPort: "http-li-9001"
   ingress: {enabled: false}
   extraVolumes:
      - name: ef-logback
        configMap:
          name: ef-logback-cm
      - name: ef-postgresql-crt-vol
        secret:
          secretName: ef-postgresql-crt
   extraVolumeMounts:
      - name: ef-logback
        mountPath: /logback
      - name: ef-postgresql-crt-vol
        mountPath: /postgresql
```

**Key configuration values:**

| Variable | Description |
|---|---|
| `linkedin.scheduler.fixed-rate` | Polling interval in seconds (default: `150`) |
| `LINKEDIN_CIM_SERVICE_ID` | Fixed service ID for the LinkedIn connector (`2001`) |
| `AUTO_SCHEDULER_STARTUP` | Auto-starts the comment polling scheduler on startup |
| `DATABASE_URL` | PostgreSQL JDBC URL for the `linkedinmetadata` database |

---

## Step 3: Deploy the Helm Chart

Run the Helm upgrade command to deploy or update the LinkedIn connector:

```bash
helm upgrade --install \
  --namespace expertflow \
  --set global.efCxReleaseName="ef-cx" \
  --debug \
  cx-channels \
  --values helm-values/cx-channels-custom-values.yaml \
  helm/Channels
```

Verify the connector pod is running:

```bash
kubectl get pods -n expertflow | grep linkedin
```

---

## Step 4: Generate a LinkedIn Access Token

1. Go to the [LinkedIn OAuth Token Generator](https://www.linkedin.com/developers/tools/oauth/token-generator).
2. Sign in with your LinkedIn account (the one associated with your LinkedIn App).
3. If you have multiple apps, select the correct one from the dropdown.
4. Under **Select OAuth 2.0 Scopes**, select all permissions required for your app.
5. Check **"I understand this tool will update my app's redirect URL settings."**
6. Click **Request access token**.
7. Authorise the app when prompted by LinkedIn.
8. **Copy the generated Access Token** — this is your `Refresh-Token` value for Unified Admin.

---

## Step 5: Unified Admin Configuration

### Channel Type

1. Navigate to **Channel Manager → Channel Type**.
2. Create a new Channel Type if it does not already exist.
3. Select **CHAT** as the MRD type.

### Channel Provider

1. Navigate to **Channel Manager → Channel Provider**.
2. Create a new Channel Provider named **LinkedIn Provider**.
3. In the **Provider Webhook** field, enter:
   `http://<linkedin-connector-svc-name>:9001/comments`
   _(Use `kubectl get svc -n expertflow` to confirm the service name.)_
4. Add the following **11 custom attributes**:

| Attribute Name | Type |
|---|---|
| `Organizational-ID` | PositiveNumber |
| `Refresh-Token` | String2000 |
| `Comments-Batch-Size` | PositiveNumber |
| `API-Version` | PositiveNumber |
| `Host-Url` | String100 |
| `Client-ID` | String100 |
| `Client-Secret` | String100 |
| `Start-Time` | AlphanumSpecial200 |
| `EDIT_MESSAGE_SUPPORT_DM` | Boolean |
| `EDIT_MESSAGE_SUPPORT_SM` | Boolean |
| `Nested-Comments-Batch-Size` | PositiveNumber |

5. Click **Save**.

### Channel Connector

1. Navigate to **Channel Manager → Channel Connector**.
2. Create a new Channel Connector named **LinkedIn Connector**.
3. Select the **LinkedIn Provider** as the Channel Provider Interface.
4. Fill in the attribute values:

| Attribute | Description |
|---|---|
| `Organizational-ID` | Numeric organisation ID from the LinkedIn company page URL: `linkedin.com/company/<ID>/admin/dashboard/` |
| `Refresh-Token` | Access token generated in Step 4 |
| `Comments-Batch-Size` | Number of comments per poll batch (default: `20`) |
| `API-Version` | LinkedIn API version number |
| `Host-Url` | LinkedIn API base URL |
| `Client-ID` | Found in the **Auth** tab of your LinkedIn Developer Portal app |
| `Client-Secret` | Found in the **Auth** tab of your LinkedIn Developer Portal app |
| `Start-Time` | ISO 8601 timestamp — only comments from this time onwards will be routed to agents |
| `EDIT_MESSAGE_SUPPORT_DM` | Direct message editing support (`false` — currently unavailable) |
| `EDIT_MESSAGE_SUPPORT_SM` | Social media comment editing support on Agent Desk (`true` to enable) |
| `Nested-Comments-Batch-Size` | Number of nested comments per poll batch (default: `20`) |

5. Click **Save**.

### Channel

1. Navigate to **Channel Manager → Channel**.
2. Click **Add new channel** under the LinkedIn channel type.
3. Fill in the channel details:
   - **Name**: e.g., `LinkedIn`
   - **Service Identifier**: `2001`
   - **Bot**: Select the Bot ID from the dropdown
   - **Channel Connector**: Select **LinkedIn Connector**
   - **Customer Activity Timeout**: 300 seconds
   - **Channel Mode**: HYBRID
   - **Routing Mode**: PUSH or PULL
   - **Queue**: Select the queue for LinkedIn interactions
   - **Agent Selection Policy**: LONGEST AVAILABLE
   - **Agent Response Time**: 300 seconds
4. Click **Save**.

---

## Developer Tier API Rate Limit Note

In **Developer Tier**, the LinkedIn API has strict rate limits. To conserve API calls:

- Only enable the comment polling scheduler when actively recording demo videos or testing.
- Disable the scheduler when not in active use.

The scheduler can be toggled via the LinkedIn connector's scheduler control APIs.

---

## Related Articles

- [LinkedIn Account Onboarding](LinkedIn-Account-Onboarding.md)
- [LinkedIn Channel Overview](LinkedIn-Channel-Overview.md)
- [LinkedIn Configuration Guide](LinkedIn-Configuration-Guide.md)
- [Channel and Connector Setup](../../Solution_Admin/Channel-and-Connector-Setup.md)
