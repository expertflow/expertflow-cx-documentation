# CX Knowledgebase : Eleveo Middleware Deployment Guide

Eleveo Middleware only supports Single Tenant in CX-5.0   
  
## Step 1: Install EF CX

Follow the guide for install EFCX through [Helm](Helm-based-Deployment-for-Expertflow-CX_2528431.html).

## Step 2: Create custom values.yaml

#### Create and Customise `cx-middleware-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-middleware-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-middleware-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-middleware-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/eleveo-middleware --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

#### Create and Customise `cx-middleware-cronjob-custom-values.yaml`

![](images/icons/grey_arrow_down.png)Customise cx-middleware-cronjob-custom-values.yaml

You must first create custom `values.yaml` file to define your minimum required configurations.

#### Step 1: Create the Values File

Run the following command to create a new file:
[code] 
    vi helm-values/cx-middleware-cronjob-custom-values.yaml
[/code]

#### Step 2: Add Required Minimum Configuration

In the opened file, add the following section to define the FQDN (Fully Qualified Domain Name) for ingress routing:
[code] 
    global:   
      ingressRouter: <CUSTOM-FQDN> 
[/code]

> 🔁 Replace `<CUSTOM-FQDN>` with your actual domain, e.g., `devops.example.com`.

This is the **minimum required customisation** for the CX Helm chart to work.

#### Optional: Add Further Customisations

You can extend the same `cx-middleware-cronjob-custom-values.yaml` file with additional configurations as needed, including environment variables, replica counts, etc.

To view all available default configurations and decide what you want to override:
[code] 
    helm show values expertflow/middleware-cronjob --version 4.10.0 
[/code]

This command prints the full default `values.yaml` file used by the CX chart, which serves as a reference for all configurable parameters.

> We recommend only overriding the values you need in your custom file to keep the configuration lean and maintainable.

## Step 3: Update the Configurations

Navigate to the Helm deployment folder of EFCX.
[code] 
    cd <CX-Folder>/kubernetes/
[/code]

Open the `helm-values/cx-middleware-custom-values.yaml` file and update the variables: 

Under `global` set the following value:

  1. ingressRouter: The FQDN of the host VM.




Under `siteEnvVars` set the values as follows:

  1. RECORDING_BACKEND: The mechanism for recording files. Leave at default **ELEVEO**.

  2. LOG_LEVEL: The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

  3. ELEVEO_ADMIN: The administrator username for Eleveo.

  4. ELEVEO_PASSWORD: The administrator password for Eleveo.

  5. ELEVEO_URL: The IP address of the Eleveo deployment in format **http://IP-address**.

  6. ELEVEO_ADMIN_PASSWORD: Password of Eleveo administrator.

  7. ELEVEO_USERNAME: Eleveo user

  8. CX_FQDN: The address of EF CX. [https://EFCX-FQDN](https://FQDN). This is set automatically via https://{{ .Values.global.ingressRouter }}




Open the `helm-values/cx-middleware-cronjob-custom-values.yaml` file and update the variables:

Under `global` set the following value:

  1. ingressRouter: The FQDN of the host VM.




Under `siteEnvVars` set the values as follows:

  1. RECORDING_BACKEND: The mechanism for recording files. Leave at default ELEVEO.

  2. LOG_LEVEL: The amount of detail in the logs. Default is **INFO** , and for more detailed logs the value should be **DEBUG**.

  3. CX_FQDN: The address of EF CX. [https://EFCX-FQDN](https://FQDN). This is set automatically via https://{{ .Values.global.ingressRouter }}

  4. CX_CONVERSATION_MANAGER: https://EFCX-FQDN/conversation-manager

  5. MIDDLEWARE_API: The API link of the recording middle-ware that will provide recording files. Format: [http://EFCX-FQDN/recording-middleware](http://IPPORT). This is set automatically.

  6. RETRIEVAL_INTERVAL: The number of past days to push recording links for on startup.

  7. ELEVEO_MAX_CALL_TIME: The maximum possible time in minutes a call is assumed to last.

  8. ELEVEO_PASSWORD: The administrator password for Eleveo.

  9. ELEVEO_PROCESSING_TIME: The time in minutes it takes for a call to appear in Eleveo after ending.

  10. ELEVEO_TIMEZONE: The timezone of the Eleveo deployment e.g. Asia/Karachi

  11. ELEVEO_URL: The IP address of the Eleveo deployment in format [**http://IP-address**](http://IP-address).

  12. ELEVEO_USERNAME: The username of the Eleveo deployment.

  13. TRUST_STORE_PASSWORD: Taken from the file `CX-<cx-version-tag>/cim-solution/kubernetes/helm/Core/values.yml`under the **efConnectionVars** section.

  14. KEY_STORE_PASSWORD: Taken from the file `CX-<cx-version-tag>/cim-solution/kubernetes/helm/Core/values.yml`under the **efConnectionVars** section.

  15. Authentication is not MTT Supported, do not add these variables if EFCX is multitenant. AUTH_ENABLED: **true** or **false** depending on whether APISIX authentication is enabled in EFCX. The four settings below are set if this value is **true**.

  16. API_USERNAME: The username created in Keycloak for API authentication.

     * On Keycloak create a user in the Expertflow realm.

     * Assign the **admin** and **default** roles, and have **Email-Verified** option enabled.

     * Assign a non-temporary password to this user as well.

  17. API_PASS: The password for the above user created in Keycloak for API authentication

  18. CLIENT_ID: Should always be **cim**.

  19. CLIENT_SECRET: Found on Keycloak in the **cim** client.




## Step 3: Deploy the Eleveo Middleware Helm Chart

Deploy the helm chart using the following command
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"  eleveo-middleware  --values helm-values/cx-middleware-custom-values.yaml expertflow/eleveo-middleware --version <cx-version>
[/code]

Check the pods by running the following command
[code] 
    kubectl get pods -n expertflow | grep eleveo-middleware
[/code]

## Step 4: Deploy the Eleveo Middleware Cronjob Helm Chart

Deploy the Eleveo Middleware Cronjob helm chart using the following command
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"  middleware-cronjob --debug --values helm-values/cx-middleware-cronjob-custom-values.yaml   expertflow/middleware-cronjob  --version <cx-version>
[/code]
