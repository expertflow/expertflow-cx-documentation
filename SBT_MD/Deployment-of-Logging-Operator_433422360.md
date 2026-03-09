# CX Knowledgebase : Deployment of Logging Operator

### Architecture 

logging-operator is a logging aggregator which collects and aggregates the logs from the EF-CX solution and routes the logs to a centralized console for evaluations using Elasticsearch/Kibana ( ELK Stack ). Logging operator is deployed per kubernetes cluster and routing of the logs is performed on per namespace basis.

This guide expects that you have already deployed the ELK stack using [ELK for Logs Analysis](Logging-Solution-Deployment-Guide_396362236.html). Use appropriate credentials.

### Add helm repository
[code] 
    helm repo add expertflow https://expertflow.github.io/charts/
[/code]

update helm repo
[code] 
    helm repo update expertflow
[/code]
[code] 
    helm upgrade --install --namespace=logging --create-namespace  logging-operator expertflow/logging-operator
[/code]

Verify that the pods are running:-
[code] 
    kubectl  -n logging get pods
[/code]

### Logging-operator configuration

create fluent-bit configuration 
[code] 
    kubectl apply -f - <<"EOF"
    apiVersion: logging.banzaicloud.io/v1beta1
    kind: FluentbitAgent
    metadata:
      name: expertflow-fluentbit-agent
      namespace: logging
    spec:
        filterKubernetes:
          Kube_URL: "https://kubernetes.default.svc:443"
        bufferStorage: 
          storage.path: /buffers
        bufferStorageVolume:
          hostPath:
            path: ""
        bufferVolumeImage: {}
        inputTail:
          storage.type: filesystem
        positiondb:
          hostPath:
            path: ""
        resources: {}
        updateStrategy: {}
    EOF
[/code]

Create Fluentd configuration
[code] 
    kubectl apply -f - <<"EOF"
    apiVersion: logging.banzaicloud.io/v1beta1
    kind: Logging
    metadata:
      name: expertflow-fluentd-logging
      namespace: logging
    spec:
      enableRecreateWorkloadOnImmutableFieldChange: true
      controlNamespace: logging
      fluentd:
        scaling:
          drain:
            enabled: true
          replicas: 1
        bufferStorageVolume:
          pvc:
            spec:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 40Gi
              volumeMode: Filesystem
    
    EOF
[/code]

Repeat below given steps for all the namespaces from which logs are to be collected and sent to ELK Stack.

### Update the Logging Output file

Execute the following command to apply secrets per namespace. Replace <ELASTICSEARCH_PASSWORD> with the password that was used to setup [ELK for Logs Analysis](Logging-Solution-Deployment-Guide_396362236.html)
[code] 
    kubectl -n <namespace> create  secret generic  elastic-password  --from-literal=password=<ELASTICSEARCH_PASSWORD>
[/code]

#### Create logging flow for logging-operator. 

Change below given placeholders with actual values before applying the manifest.

  * <NAMESPACE>

  * <CLUSTER_NAME>




For ELK Stack, use the following configurations:-
[code] 
    kubectl apply -f - <<"EOF"
    apiVersion: logging.banzaicloud.io/v1beta1
    kind: Flow
    metadata:
      name: <NAMESPACE>-flow-es
      namespace:  <NAMESPACE>
      labels:
         ef: expertflow
    spec:
          filters:
            - record_modifier: # if you e.g. have multiple clusters
                records:
                  - cluster: "<CLUSTER_NAME>"
            - record_transformer:
                enable_ruby: true
                records:
                  - message: ${record["message"].gsub(/\e\[([;\d]+)?m/, '')}
            # replaces dots in labels and annotations with dashes to avoid mapping issues (app=foo (text) vs. app.kubernetes.io/name=foo (object))
            # fixes error: existing mapping for [kubernetes.labels.app] must be of type object but found [text]
            - dedot:
                de_dot_separator: "-"
                de_dot_nested: true
          localOutputRefs:
            - <NAMESPACE>-output-es
    
    EOF
[/code]

For OpenSearch Deployment, use the following configurations for Flow:-
[code] 
    apiVersion: logging.banzaicloud.io/v1beta1
    kind: Flow
    metadata:
      labels:
        ef: expertflow
      name: <NAMESPACE>-flow-es
      namespace: <NAMESPACE>
      resourceVersion: "58721691"
      uid: 091c87e3-5a1a-4012-b13c-775d088eed76
    spec:
      filters:
      - record_modifier:
          records:
          - cluster: ef-cx
      - record_transformer:
          enable_ruby: true
          records:
          - message: ${record["message"].gsub(/\e\[([;\d]+)?m/, '')}
      - dedot:
          de_dot_nested: true
          de_dot_separator: '-'
      localOutputRefs:
      - ef-external-output-es
    status:
      active: true
[/code]

#### Create Output for logging-operator 

For ELK Stack, use the following configurations:-

Change these parameters before applying the manifest.

  * <NAMESPACE>

  * <INDEX_NAME>

  * <ELASTICSEARCH_HOST_IP>

  * <PORT>



[code] 
    kubectl apply -f - <<"EOF"
    apiVersion: logging.banzaicloud.io/v1beta1
    kind: Output
    metadata:
      name: <NAMESPACE>-output-es
      namespace:  <NAMEPSACE>
      labels:
              ef: ef-external
    spec:
          elasticsearch:
            host: <ELASTICSEARCH_HOST_IP>
            port: 30920
            user: elastic
            index_name: <INDEX_NAME>
            password:
              valueFrom:
                secretKeyRef:
                  name: elastic-password   #kubectl -n logging create  secret generic  elastic-password  --from-literal=password=admin123
                  key: password
            scheme: https
            ssl_verify: false
            #logstash_format: true # this creates its own index, so dont enable it
            include_timestamp: true
            reconnect_on_error: true
            reload_on_failure: true
            buffer:
              flush_at_shutdown: true
              type: file
              chunk_limit_size: 4M # Determines HTTP payload size
              total_limit_size: 1024MB # Max total buffer size
              flush_mode: interval
              flush_interval: 10s
              flush_thread_count: 2 # Parallel send of logs
              overflow_action: block
              retry_forever: true # Never discard buffer chunks
              retry_type: exponential_backoff
              retry_max_interval: 60s
            # enables logging of bad request reasons within the fluentd log file (in the pod /fluentd/log/out)
            log_es_400_reason: true
    EOF
[/code]

For Opensearch, use the following configurations:-

Change these parameters before applying the manifest.

  * <NAMESPACE>

  * <INDEX_NAME>

  * <OPENSEARCH_HOST_IP>

  * <PORT>



[code] 
    apiVersion: v1
    items:
    - apiVersion: logging.banzaicloud.io/v1beta1
      kind: Output
      metadata:
        labels:
          ef: <NAMESPACE>
        name: <NAMESPACE>-output-es
        namespace: <NAMESPACE>
      spec:
        opensearch:
          buffer:
            chunk_limit_size: 4M
            flush_at_shutdown: true
            flush_interval: 10s
            flush_mode: interval
            flush_thread_count: 2
            overflow_action: block
            retry_forever: true
            retry_max_interval: 60s
            retry_type: exponential_backoff
            total_limit_size: 1024MB
            type: file
          host: <OPENSEARCH HOST>
          include_timestamp: true
          index_name: <INDEX_NAME>
          password:
            valueFrom:
              secretKeyRef:
                key: password
                name: elastic-password
          port: <PORT>
          reconnect_on_error: true
          reload_on_failure: true
          scheme: https
          ssl_verify: false
          user: admin
      status:
        active: true
    kind: List
    metadata:
      resourceVersion: ""
[/code]

Verify status of all logging resources created 
[code] 
    kubectl get logging-all -A
[/code]
