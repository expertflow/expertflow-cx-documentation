# CX Knowledgebase : Deploy Fluentbit for Opensearch

This guide demonstrates the process for forwarding kube-logs to OpenSearch using FluentBit.

## Deploy Fluentbit using Helm Chart

Change the directory:-
[code] 
    cd CX-5.0/kubernetes/
[/code]

Open `values.yaml` file for fluentbit helm chart.
[code] 
    vi helm-values/fluentbit-values.yaml
[/code]

Paste the following the content in this file:-
[code] 
    config:
      service: |
        [SERVICE]
          Flush         5
          Daemon        Off
          Log_Level     info
          HTTP_Server   On
          HTTP_Listen   0.0.0.0
          HTTP_Port     2020
    
      inputs: |
        [INPUT]
          Name              tail
          Path              /var/log/containers/*.log
          Tag               kube.*
          Parser            docker
          Mem_Buf_Limit     100MB
          Skip_Long_Lines   On
    
      parsers: |
        [PARSER]
          Name         json_audit
          Format       json
          Time_Key     timestamp
          Time_Format  %Y-%m-%dT%H:%M:%S.%LZ
    
      filters: |
        # First: Parse Docker + Kubernetes metadata
        [FILTER]
          Name                kubernetes
          Match               kube.*
          Merge_Log           On
          Merge_Log_Key       log_processed
          K8S-Logging.Parser  On
          K8S-Logging.Exclude On
    
        # Second: Reparse the merged log as JSON to extract 'type' field
        [FILTER]
          Name                parser
          Match               kube.*
          Key_Name            log_processed
          Parser              json_audit
          Reserve_Data        On
          Preserve_Key        On
    
        # Third: Modify record to add tag or route based on 'type'
        [FILTER]
          Name                modify
          Match               kube.*
          Condition           Key_Value_Pairs_Contains type audit_logging
          Add                 log_type audit
    
      outputs: |
        # Audit logs only → separate index
        [OUTPUT]
          Name                opensearch
          Match               kube.*.audit
          Host                <Opensearch host IP>
          Port                <Port number>
          Index               audit_log_index
          Type                _doc
          TLS                 On
          Logstash_Format     On
          Retry_Limit         False
          HTTP_User           <Opensearch user>
          HTTP_Passwd         <Opensearch password>
    
        # Optional: Add a rewrite_tag filter to route audit logs
        [FILTER]
          Name                rewrite_tag
          Match               kube.*
          Rule                $type ^audit_logging$ kube.audit.audit true
[/code]

Update the <Opensearch host IP>, <Port number>, <Opensearch user> and <Opensearch password>

Save the content of the file and exit.  


Deploy the fluentbit helm chart using the following command:-
[code] 
    helm upgrade --install fluent-bit fluent/fluent-bit --namespace logging --create-namespace -f helm-values/fluentbit-values.yaml
[/code]

## Configuring Fluent Bit Output for Your SIEM Solution

Fluent Bit supports multiple output plugins and can forward logs to different SIEM and observability platforms.  
The **output section** of the Fluent Bit configuration is **SIEM-agnostic** and can be customized based on your logging backend.

To integrate Fluent Bit with your SIEM solution, update the `outputs` section in the Helm values file:
[code] 
    vi helm-values/fluentbit-values.yaml
[/code]

Replace the OpenSearch output with the appropriate output plugin for your SIEM.

### Example: Elasticsearch Output Configuration

If your solution is **Elasticsearch** , update the output section as shown below:

For audit logs routed separately:
[code] 
    [OUTPUT]
      Name                es
      Match               kube.*.audit
      Host                <Elasticsearch host>
      Port                <Elasticsearch port>
      Index               audit_log_index
      Type                _doc
      Logstash_Format     On
      Retry_Limit         False
      HTTP_User           <Elasticsearch user>
      HTTP_Passwd         <Elasticsearch password>
      TLS                 On
[/code]

### Important Notes

  * Only the **output section** needs to be modified when switching SIEM solutions.

  * Input, parser, and filter configurations remain unchanged.

  * Ensure network connectivity, TLS settings, and credentials are configured according to your SIEM security policies.



