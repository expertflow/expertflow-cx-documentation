---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Superset Alerts & Reports Feature Enablement

This guide details the steps to enable the Alerts and Reports feature in Apache Superset within a Kubernetes environment.

## Prerequisites
- Access to the customer’s Kubernetes cluster.
- Helm access to the existing Superset release.
- Account credentials for SMTP setup (provided by the customer).

## Feature Enablement Steps

### 1. Update Custom Values
Edit your `superset-custom-values.yaml` file to include the following configurations:

#### Ingress Configuration
Ensure the ingress is configured with the correct host and SSL settings.
```yaml
ingress:
  enabled: true
  hosts:
    - your-superset-domain.com
  tls:
    - secretName: ef-ingress-tls-secret
      hosts:
        - your-superset-domain.com
```

#### SMTP Environment Variables
Add your SMTP credentials to the `extraEnv` section:
```yaml
extraEnv:
  ENABLE_TEMPLATE_PROCESSING: "True"
  ENABLE_ALERTS_REPORTS: "True"
  SMTP_HOST: "smtp.example.com"
  SMTP_USER: "user@example.com"
  SMTP_PASSWORD: "secure-password"
  SMTP_MAIL_FROM: "superset@example.com"
```

#### Celery and Feature Flags
Update the `configOverrides` to enable the alert scheduler:
```python
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
}
class CeleryConfig:
    broker_url = "redis://superset-redis-master:6379/0"
    result_backend = "redis://superset-redis-master:6379/0"
    beat_schedule = {
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
    }
```

### 2. Upgrade Superset via Helm
Run the following command to apply the changes:
`helm upgrade --install --namespace ef-bi --values=helm-values/superset-custom-values.yaml superset expertflow/superset`

### 3. Verify Enablement
Once the upgrade is complete, log in to Superset and verify that the "Alerts & Reports" option appears in the settings menu.
