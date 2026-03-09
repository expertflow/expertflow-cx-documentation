# CX Knowledgebase : LinkedIn Dev Connector Deployment using Helm

This document is for the support team to deploy the connector, add customer configurations, record the video, and request the standard tier.

### Requirements

  * Kubernetes. [Deployment Planning](/wiki/pages/createpage.action?spaceKey=SBT&title=Deployment%20Planning&linkCreation=true&fromPageId=1653800961)
  * Storage Solution [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started)
  * CX Deployment <https://expertflow-docs.atlassian.net/wiki/x/r5Qm> [Tag: 4.10.3](https://gitlab.expertflow.com/cim/cim-solution/-/blob/CX-4.10.3)  




### Deployment

Create a `linkedinmetadata` Database in Postgres
[code] 
    kubectl exec -it ef-postgresql-0 -n ef-external -- psql -U sa -d postgres -c "CREATE DATABASE linkedinmetadata;"
    kubectl exec -it ef-postgresql-0 -n ef-external -- psql -U sa -d postgres -c "CREATE DATABASE linkedincommentmetadata;"
    // Enter postgres sa password by default it is Expertflow123
[/code]

### CX Channels

Customise the deployment by fetching the values.yaml file and edit it as per the requirements.
[code] 
    vi helm/Channels/values.yaml
[/code]

Edit/update the values file `with`
[code] 
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
            value: '{{ .Values.global.efCommonVars_LOGGING_CONFIG  }}'
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
       ingress: {enabled: false} # <-- Explicitly disable standard Ingress
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
[/code]

Deploy the Channels helm chart by
[code] 
    helm upgrade --install --namespace expertflow  --set global.efCxReleaseName="ef-cx"   --debug   cx-channels --values  helm-values/cx-channels-custom-values.yaml  helm/Channels
[/code]

### **Generating an Access Token for LinkedIn's API**

Assuming you already have a verified app on the [_LinkedIn Developer Portal_](https://www.linkedin.com/developers/), you have also requested the standard upgrade.

  1. Go to the [_LinkedIn OAuth Token Generator_](https://www.linkedin.com/developers/tools/oauth/token-generator).

  2. Sign in with your LinkedIn account if you aren’t already logged in.

  3. If you have multiple apps in your LinkedIn Developer account, select the app you want to generate a token for from the dropdown menu.

  4. Under "Select OAuth 2.0 Scopes", choose all the permissions for your app.

  5. Check the button _'I understand this tool will update my app’s redirect URL settings.'_

  6. Click the "Request access token" button.  


![image-20250224-123157.png](attachments/1653800961/1653932060.png?width=1105)
  7. If you are not already logged in on LinkedIn, then it will ask you to login,

  8. LinkedIn will prompt you to authorise the app. Review the permissions and click "Allow".  


![image-20250224-123407.png](attachments/1653800961/1653932067.png?width=1008)
  9. Copy the generated Access Token from the tool.




## Unified Admin Configuration

To set up the LinkedIn Channel, the LinkedIn connector needs to be configured in the [ _Unified Admin_](https://expertflow-docs.atlassian.net/wiki/external/Yzc2NzU3MDdhMmY2NDQ5YjkzYmMxYjNlOTExZDNkMGU) of the Expertflow CX's application.

### Channel Type

  1. Create a new Channel Type (if it doesn't exist).

  2. Select a Chat in the MRD.


![image-20250224-125533.png](attachments/1653800961/1653932073.png?width=760)

### Channel Provider

It's recommended that the component’s service name be used in the **"Channel Provider - > Provider's Webhook"** field. However, FQDN can also be used with some additional custom configurations.

  1. Create a Channel Provider and give it the name "LinkedIn Provider"

  2. Provide the service name of LinkedIn Connector in the **Provider Webhook** field as http://{SERVICE-NAME}:{SERVICE-PORT}/comments. Replace the {**SERVICE-NAME} and**{**SERVICE-PORT}** in the URL with the component's k3s-based service name and port _(It can be fetched using k get svc -n expertflow)_

  3. Create the following additional attributes   





**Name**| **Type**  
---|---  
Organizational-ID| PositiveNumber  
Refresh-Token| String2000  
Comments-Batch-Size| PositiveNumber  
API-Version| PositiveNumber  
Host-Url| String100  
Client-ID| String100  
Client-Secret| String100  
Start-Time| AlphanumSpecial200  
EDIT_MESSAGE_SUPPORT_DM| Boolean  
EDIT_MESSAGE_SUPPORT_SM| Boolean  
Nested-Comments-Batch-Size| PositiveNumber  
  
  4. Click **Save**


![image-20251218-092850.png](attachments/1653800961/1653932079.png?width=1199)

### Channel Connector

  1. Create a Channel Connector and give it the name "LinkedIn Connector"

  2. Select LinkedIn in the Channel Provider Interface.

  3. add the details.




**Properties**| **Description**  
---|---  
`<ORGANIZATION-ID>`| You can get this from the organisation’s LinkedIn page dashboard URL  
[ _https://www.linkedin.com/company/_](https://www.linkedin.com/company/)<`<ORGANIZATION-ID>`>/admin/dashboard/  
`<Refresh-TOKEN>`| Generate using the [_OAuth token generator tool_](https://expertflow-docs.atlassian.net/wiki/spaces/SBT/pages/edit-v2/910492591#Generating-an-Access-Token-for-LinkedIn's-API)  
`Comments-Batch-Size`| Batch size for comments (default 20)  
`API-Version`| LinkedIn API version  
`Host-Url`| LinkedIn API url  
`Client-ID`| Available in the developer portal’s auth tab  
`Client-Secret`| Available in the developer portal’s auth tab  
`Start-Time`| All the comments from this time onwards will be routed to the agent  
`EDIT_MESSAGE_SUPPORT_DM`| Enable Direct Message support on the agent desk (currently not available)  
`EDIT_MESSAGE_SUPPORT_SM`| Enable Social Media comments support on the agent desk  
`Nested-Comments-Batch-Size`| Batch size for nested comments (default 20)  
  
  4. Click **Save**


![image-20251218-092806.png](attachments/1653800961/1653932085.png?width=800)

###   
Channel

  1. Add a Channel and give it a name like “LinkedIn”.

  2. Add Service Identifier as 2001.

  3. Select the Bot ID.

  4. Select the recently created “LinkedIn Connector” in Channel Connector.

  5. Set 300 sec as Customer Activity Timeout(sec).

  6. Set Channel Mode as HYBRID.

  7. Set the Routing Mode as per your need. PUSH or PULL.

  8. Set the required Queue where you want to route the LinkedIn Chats.

  9. Select LONGEST AVAILABLE as Agent Selection Policy.

  10. Set 300 sec as Agent Response Time(sec).

  11. Save.


![image-20250224-131514.png](attachments/1653800961/1653932091.png?width=741)

This will start pooling the comments. After every 150 sec, you can enable and disable schedular using the APIs. [![](attachments/thumbnails/1653800961/1652817934)](attachments/1653800961/1652817934.json)

Only enable when you have to recode the video, and after that, disable that, because in the developer tier, you only have limited api calls.
