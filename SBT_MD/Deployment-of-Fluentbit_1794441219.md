# CX Knowledgebase : Deployment of Fluentbit

Fluent Bit is an open-source and lightweight log processor and forwarder designed for cloud-native environments. It is part of the Fluent ecosystem and is specifically optimized for performance and memory usage. Fluent Bit enables you to collect, process, and ship logs from various sources to multiple destinations, including log storage and analysis systems such as OpenSearch, Elasticsearch, and various cloud services.

## Deployment Steps

To deploy Fluent Bit using Helm, you first need to add the ExpertFlow Helm repository.
[code] 
    helm repo add expertflow https://expertflow.github.io/charts/
[/code]

Ensure you have the latest charts from the ExpertFlow repository.
[code] 
    helm repo update expertflow
[/code]

You can deploy Fluent Bit by using a custom values file for configuration. First, create the custom values file based on the default configuration provided by the chart.
[code] 
    helm show values expertflow/fluent-bit > helm-values/cx-fluent-bit-custom-values.yaml 
[/code]

Now, use the following command to deploy Fluent Bit with the custom values.
[code] 
    helm upgrade --install --namespace ef-external --set global.efCxReleaseName="ef-cx"  cx-fluent-bit --debug --values helm-values/cx-fluent-bit-custom-values.yaml expertflow/fluent-bit
[/code]

After deploying Fluent Bit, it is essential to verify that it is running correctly and processing logs as expected. 

  * Ensure that the Fluent Bit pod is running without errors.



[code] 
    kubectl get pods -n ef-external
[/code]

  * To view the logs of the Fluent Bit pod, use the following command:



[code] 
    kubectl logs -f <fluent-bit-pod-name> -n ef-external
[/code]

## Uninstall Fluentbit

If you need to disable or remove the Fluent Bit deployment, use the following command:
[code] 
    helm uninstall -n ef-external cx-fluent-bit
[/code]
