# CX Knowledgebase : Setup Alerts via Gmail

## Pre-requisites for setting up alerts via Gmail.  
  
The monitoring solution must be deployed before setting up the alerts. Follow [this](https://expertflow-docs.atlassian.net/wiki/x/nI8m) guide to deploy the monitoring solution.

Change the directory
[code] 
    cd cim-solution/kubernetes
[/code]

## Update the variables.

Update the variables in values-small.yaml
[code] 
    vi monitoring/kube-prometheus-stack/values-small.yaml
[/code]

Update these values
[code] 
    additionalScrapeConfigs:
        - job_name: 'blackbox'
          metrics_path: /probe
          params:
            module: [icmp]  # Use the icmp module defined in blackbox.yml
          static_configs:
            - targets:
              - <Target IP>  # Replace with the IP you want to ping
          relabel_configs:
            - source_labels: [__address__]
              target_label: __param_target
            - source_labels: [__param_target]
              target_label: instance
            - target_label: __address__
              replacement: prometheus-blackbox-exporter:9115  # Blackbox exporter address
    
[/code]
[code] 
    additionalPrometheusRulesMap:
      rule-name:
        groups:
        - name: my_group
          rules:
          # For Instance Down 
          - alert: InstanceDown
            expr: probe_success == 0
            for: 30s
            labels:
              severity: critical
            annotations:
              summary: "Instance {{ $labels.instance }} is down"
              description: "Instance {{ $labels.instance }} has been down for more than 30 seconds."
          #For CPU High Load on pod level
          - alert: CPULoadHigh
            expr: sum by(container, pod, namespace) (increase(container_cpu_cfs_throttled_periods_total{container!="metrics-server-nanny"}[5m])) / sum by(container, pod, namespace) (increase(container_cpu_cfs_periods_total[5m])) > (80 / 100)
            for: 1m
            labels:
              severity: critical
            annotations:
              summary: "Processes experience elevated CPU throttling."
              description: "{{ $value | humanizePercentage }} throttling of CPU in namespace {{ $labels.namespace }} for container {{ $labels.container }} in pod {{ $labels.pod }}."
          # For PodNotReady state 
          - alert: KubePodNotReady
            annotations:
              description: Pod {{ $labels.namespace }}/{{ $labels.pod }} has been in a non-ready state for longer than 5 minutes.
              runbook_url: https://runbooks.prometheus-operator.dev/runbooks/kubernetes/kubepodnotready
              summary: Pod has been in a non-ready state for more than 15 minutes.
            expr: |-
               sum by (namespace, pod, cluster) (max by(namespace, pod, cluster) (kube_pod_status_phase{job="kube-state-metrics", namespace=~"^.*$", phase=~"Pending|Unknown"}) * on(namespace, pod, cluster) group_left(owner_kind) topk by(namespace, pod, cluster) (1, max by(namespace, pod, owner_kind, cluster) (kube_pod_owner{owner_kind!="Job"}))) > 0
            for: 5m
            labels:
              severity: critical
          #For High Cpu Usage On Node
          - alert: HighCpuUsageOnNode
            #expr: (sum(rate(node_cpu_seconds_total{mode!="idle"}[5m])) by (instance)) / sum(machine_cpu_cores) by (instance) > 0.9
            expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80
            for: 5m
            labels:
              severity: critical
            annotations:
              summary: "High CPU usage on node {{ $labels.instance }}"
              description: "Node {{ $labels.instance }} has high CPU usage (greater than 90% for the last 5 minutes)."
          #For High Memory Usage On Node
          - alert: HighMemoryUsageOnNode
            # expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) > 0.9
            expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 80
            for: 5m
            labels:
              severity: critical
            annotations:
              summary: "High Memory usage on node {{ $labels.instance }}"
              description: "Node {{ $labels.instance }} has high memory usage (greater than 90% for the last 5 minutes)."
          #For Pod CreshLooping state 
          - alert: KubePodCrashLooping
            annotations:
              description: 'Pod {{ $labels.namespace }}/{{ $labels.pod }} ({{ $labels.container}}) is in waiting state (reason: "CrashLoopBackOff").'
              runbook_url: https://runbooks.prometheus-operator.dev/runbooks/kubernetes/kubepodcrashlooping
              summary: Pod is crash looping.
            expr: max_over_time(kube_pod_container_status_waiting_reason{reason="CrashLoopBackOff",job="kube-state-metrics", namespace=~"^.*$"}[5m]) >= 1
            for: 5m
            labels:
              severity: critical
[/code]
[code] 
    config:
        global:
          smtp_smarthost: 'smtp.gmail.com:<smtp port number>'
          smtp_require_tls: false  
          smtp_auth_username: '<email ID>'
          smtp_auth_password: '<auth token/password>'
          smtp_from: 'email ID'
          resolve_timeout: 5m
        inhibit_rules:
          - source_matchers:
              - 'severity = critical'
            target_matchers:
              - 'severity =~ warning|info'
            equal:
              - 'namespace'
              - 'alertname'
          - source_matchers:
              - 'severity = warning'
            target_matchers:
              - 'severity = info'
            equal:
              - 'namespace'
              - 'alertname'
          - source_matchers:
              - 'alertname = InfoInhibitor'
            target_matchers:
              - 'severity = info'
            equal:
              - 'namespace'
        route:
          group_by: ['namespace']
          group_wait: 30s
          group_interval: 5m
          repeat_interval: 15m
          receiver: 'email'
          routes:
          - receiver: 'email'
            matchers: 
              - severity=~"critical"   
          - receiver: 'null'
            matchers:
              - alertname =~ "InfoInhibitor|Watchdog"
        receivers:
        - name: 'null'
        - name: 'email'
          email_configs: 
            - to: '<receiver email ID>'
              from: '<email ID>'
              smarthost: 'smtp.gmail.com:<smtp port number>'
              require_tls: false
              auth_username: '<email ID>'
              auth_password: '<auth token/password>'  
        templates:
        - '/etc/alertmanager/config/*.tmpl'
    
[/code]
[code] 
    grafana:
      enabled: true
      namespaceOverride: ""
      #EXPERTFLOW
      grafana.ini:
        smtp:
          enabled: true
          host: smtp.gmail.com:<smtp port number>
          user: <email ID>
          password: <auth token/password>
          skip_verify: true
          from_address: <email ID>
          from_name: Grafana
        server:
          domain: <FQDN>
          #root_url: "%(protocol)s://%(domain)s/"
          root_url: https://<FQDN>/monitoring/
    
[/code]

enable kubeStateMetrics
[code] 
    ## Component scraping kube state metrics
    ##
    kubeStateMetrics:
      enabled: true
    
    ## Configuration for kube-state-metrics subchart
    ##
    kube-state-metrics:
      namespaceOverride: ""
      rbac:
        create: true
      releaseLabel: true
      prometheus:
        monitor:
          enabled: true
    
          ## Scrape interval. If not set, the Prometheus default scrape interval is used.
          ##
          interval: ""
    
          ## Scrape Timeout. If not set, the Prometheus default scrape timeout is used.
          ##
          scrapeTimeout: ""
    
          ## proxyUrl: URL of a proxy that should be used for scraping.
          ##
          proxyUrl: ""
    
          # Keep labels from scraped data, overriding server-side labels
          ##
          honorLabels: true
    
          ## MetricRelabelConfigs to apply to samples after scraping, but before ingestion.
          ## ref: https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md#relabelconfig
          ##
          metricRelabelings: []
          # - action: keep
          #   regex: 'kube_(daemonset|deployment|pod|namespace|node|statefulset).+'
          #   sourceLabels: [__name__]
    
          ## RelabelConfigs to apply to samples before scraping
          ## ref: https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md#relabelconfig
          ##
          relabelings: []
          # - sourceLabels: [__meta_kubernetes_pod_node_name]
          #   separator: ;
          #   regex: ^(.*)$
          #   targetLabel: nodename
          #   replacement: $1
          #   action: replace
    
      selfMonitor:
        enabled: true
[/code]

## Update monitoring solution.

Update monitoring solution using the following command
[code] 
    cd monitoring/
    helm upgrade --namespace monitoring --install=true kube-prometheus-stack --values=kube-prometheus-stack/values-small.yaml  kube-prometheus-stack
[/code]

## Pull blackbox helm chart.
[code] 
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm pull prometheus-community/prometheus-blackbox-exporter
[/code]

Open the values.yaml file
[code] 
    vi prometheus-blackbox-exporter/values.yaml
[/code]

Update the following values:-
[code] 
    config:
      modules:
        http_2xx:
          prober: http
          timeout: 5s
          http:
            valid_http_versions: [ "HTTP/1.1", "HTTP/2" ]
            valid_status_codes: []  # Defaults to 2xx
            follow_redirects: true
        icmp:
          prober: icmp
          timeout: 5s
[/code]

## Deploy the blackbox exporter:-

Deploy the blackbox exporter using the following command.
[code] 
    helm upgrade --namespace monitoring --install=true prometheus-blackbox-exporter --values=prometheus-blackbox-exporter/values.yaml  prometheus-blackbox-exporter
[/code]
