# CX Knowledgebase : Customizing CX Helm Chart Deployments

# Overview 

Traditionally, customisation of CX Helm charts required downloading and editing the full `values.yaml`:
[code] 
    helm show values expertflow/cx --version 4.10.0 > helm-values/ef-cx-custom-values.yaml
[/code]

However, this approach tightly couples your custom values to a specific version. Upgrading to a new chart version (e.g., from `4.10.0` to `4.10.1`) requires manually syncing or merging your custom file with the latest changes — a time-consuming and error-prone process.

This guide introduces a **modular approach** that allows you to:

  * Apply only the customisations you need.

  * Seamlessly upgrade to newer Helm chart versions.

  * Avoid maintaining full duplicate copies of chart values.




## New Customization Strategy Overview

Key Concept| Description  
---|---  
`global`| Set global parameters (e.g., ingress, registry, imagePullSecrets). Customizable per deployment.  
`efConnectionVars`| Central location to override common EF-related connections (Mongo, Redis, Vault, etc.).  
`efCommonVars`| Common environment variables across components  
`extraEnvVars`| Holds default environment variables shipped with the chart.  
`siteEnvVars`| Holds **your custom overrides**. These override matching keys in `extraEnvVars`.  
  
You can check the default values.yaml by using the `helm show values` command, to check core values,yaml
[code] 
    helm show values expertflow/<chart name> --version 4.10.0
    
    # i-e to list the default values.yaml for cx chart
    
    helm show values expertflow/cx --version 4.10.0
[/code]

### **Step-by-Step: Customise Chart with Minimal Overrides**

Create a custom-values.yaml file and add the customised values that you need.

You can now provide a **lightweight override YAML file** (e.g., `ef-cx-custom-values.yaml`) like this:
[code] 
    global:
      ingressRouter: "custom.domain.com"
      efCommonVars_IS_WRAP_UP_ENABLED: true
      efCommonVars_WRAPUP_TIME: "90"
    
    efConnectionVars:
      ACTIVEMQ_KEY_STORE_PASSWORD: "CustomSecureKey123"
      REDIS_PASSWORD: "CustomRedisPwd"
    
    agent-manager:
      siteEnvVars:
        - name: LOG_LEVEL
          value: "info"
        - name: ACCEPT_TIMEOUT
          value: "90000"
    
[/code]

Then install/upgrade with:
[code] 
    helm upgrade --install ef-cx expertflow/cx \
      --namespace expertflow \
      --version 4.10.1 \
      --values ef-cx-custom-values.yaml
    
[/code]

### Examples of Customisations by Section

### 1\. `global` and `efCommonVars`Section

Customise domain, registry, certs, timezones, logging, and feature toggles.
[code] 
    global:
      ingressRouter: "devops234.ef.com"
      ingressClassName: "nginx"
      imageRegistry: "gitimages.expertflow.com"
      imagePullSecrets:
        - ef-gitlab-secret
    
      efCommonVars_IS_WRAP_UP_ENABLED: true
      efCommonVars_WRAPUP_TIME: "90"
      efCommonVars_TZ: Asia/Karachi
    
[/code]

### 2\. `efConnectionVars`

Used for secure connections to MongoDB, Redis, Vault, Keycloak, etc.
[code] 
    efConnectionVars:
      MONGODB_HOST: "mongo-mongodb.custom.svc:27017"
      MONGODB_PASSWORD: "CustomMongoPwd123"
      REDIS_PASSWORD: "CustomRedisPwd"
[/code]

### 3\. `siteEnvVars` (Component-Level Overrides)

Overrides specific environment variables for a component without touching `extraEnvVars`.
[code] 
    agent-manager:
      siteEnvVars:
        - name: LOG_LEVEL
          value: "warn"
        - name: SOCKET_PING_TIMEOUT
          value: "30000"
[/code]

You can apply `siteEnvVars` to any component like `routing-engine`, `conversation-manager`, `cim-customer`, etc.

### **Upgrading to a New Version**

When upgrading:
[code] 
    helm upgrade --install ef-cx expertflow/cx \
      --namespace expertflow \
      --version 4.10.1 \
      --values ef-cx-custom-values.yaml
[/code]

**What happens:**

  * Default chart values from `4.10.1` are used.

  * Your file overrides only the values you specify.

  * Any new variables in `4.10.1` will use their default value unless explicitly overridden.



