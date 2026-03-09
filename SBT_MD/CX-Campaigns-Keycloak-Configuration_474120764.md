# CX Knowledgebase : CX Campaigns Keycloak Configuration

# Overview

This document illustrates the steps for Keycloak configuration required for CX Campaigns

## Keycloak Configuration

Before using the CX Campaigns' management menu in Unified Admin, you must configure Keycloak since CX Campaigns is an optional feature of ExpertFlow CX. Here are the configuration steps:

#### Step 1: Login to Keycloak

Access the Keycloak Administration console by opening this URL in your browser: [https://<FQDN>/auth](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/511639665/CX+Surveys+Deployment+Guide)

Default username and password is “admin” and “admin” respectively.

![](attachments/474120764/598966365?width=1800)

#### Step 2: Open the cim client

In the **ExpertFlow realm** , select **Clients** from the left navigation bar, then click on the **cim** client.

If the ExpertFlow realm is not present. Refer to this [documentation](/wiki/pages/createpage.action?spaceKey=SBT&title=IAM%20user%20Creation%20guide&linkCreation=true&fromPageId=474120764) to import the ExpertFlow realm and additional configuration

![](attachments/474120764/598966447?width=1800)

#### Step 3: Navigate to the Import pop-up

In the **cim** client, select the **Authorization** tab, then click **Import**.

![](attachments/474120764/599556172?width=1800)

#### Step 4: Navigate to the Import pop-up

After clicking **Import** , a popup window will appear. Upload this file [![](attachments/thumbnails/474120764/1203273840)](attachments/474120764/1203273840.json) which contains all the CX Campaigns related authorization configuration and click **Confirm**.  
For MTT campaigns upload this file [![](attachments/thumbnails/474120764/1310556197)](attachments/474120764/1310556197.json)

![](attachments/474120764/599425127?width=1800)

Campaigns tab should now be visible in the **Unified Admin**.

![campaigns-enabled-in-unified-admin.png](attachments/474120764/598966453.png?width=1131)
