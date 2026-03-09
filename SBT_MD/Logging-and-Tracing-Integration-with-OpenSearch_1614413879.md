# CX Knowledgebase : Logging and Tracing Integration with OpenSearch

This guide, intended for the operations team, walks you through integrating your audit logging system with OpenSearch. It is divided into clear steps:

  1. Deploy OpenSearch

  2. Configure index, mappings, index patterns, and dashboards

  3. Configure Fluent Bit Output




## Deploy OpenSearch

Set up OpenSearch cluster in your Kubernetes environment using the following guide.

[_Opensearch and Opensearch Dashboard Deployment Guide_](Deployment-of-Opensearch-and-Opensearch-Dashboards_1277919276.html)

**Key Outputs**

  * OpenSearch cluster URL: http://{{baseURL}}:9200

  * OpenSearch Dashboards URL: http://{{baseURL}}:5601

  * Admin credentials configured

  * Cluster health: GREEN




## Configure Index, Mappings, index patterns and dashboards

Follow this guide to create the audit logging index and dashboards in OpenSearch Dashboard

[ _Index Configuration, Opensearch and Opensearch Dashboard Setup Guide_](Opensearch-Setup-for-Logging-and-Tracing_1612415217.html)

**Key Outputs** :

  * Index created: `audit_log_index`

  * Mappings configured

  * Index status: ACTIVE

  * Index pattern created: audit-logs-*

  * Time field configured: timestamp

  * Visualization created

  * Fields discoverable in Dashboards

  * Search functionality enabled




## Configure Fluent Bit Output

Connect Fluent Bit to send audit logs to OpenSearch.

  * Configure Fluent Bit output plugin

  * Set OpenSearch endpoint URL

  * Configure authentication (if needed)

  * Enable retry and buffering policies




update the OUTPUT section in `helm-values/cx-fluent-bit-custom-values.yaml`
[code] 
    [OUTPUT]
          Name  opensearch
          Match audit.admin
          Host  [opensearch host]
          Port  9200
          Index audit_log_index
          HTTP_User [opensearch user]
          HTTP_Passwd [opensearch password]
          Logstash_Format Off
          Replace_Dots On
          Suppress_Type_Name On
          Retry_Limit 5
          tls [opensearch tls verification]
          tls.verify Off
[/code]

**Key Outputs** :

  * Fluent Bit connected to OpenSearch

  * Logs being received successfully

  * Index naming pattern working

  * No connection errors in Fluent Bit logs



