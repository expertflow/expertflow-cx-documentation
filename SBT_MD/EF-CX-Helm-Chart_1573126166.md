# CX Knowledgebase : EF CX Helm Chart

### Global Chart Details

In addition to sub-chart details, below given are the details for this meta chart. Any key: value pair present in this file supersedes the values file in sub-chart's values file.

**Section**| **Item**| **Details**| **default**  
---|---|---|---  
global| ingressRouter| FQDN used for the EF-CX Solution| “[devops.ef.com](http://devops.ef.com)”  
imageRegistry| default container registry to pull images from| "[gitimages.expertflow.com](http://gitimages.expertflow.com)"  
ingressCertName| default ingress certificate secret name. must be created before install| "ef-ingress-tls-secret"  
ingressClassName| ingress class name| “nginx”  
commonIngressAnnotations| common annotations for all ingress resources| ““  
efCommonVars_IS_WRAP_UP_ENABLED| Common Environment Variable| true  
efCommonVars_WRAPUP_TIME| Common Environment Variable| "60"  
efCommonVars_DEFAULT_ROOM_NAME| Common Environment Variable| CC  
efCommonVars_DEFAULT_ROOM_LABEL| Common Environment Variable| CC  
efCommonVars_DEFAULT_ROOM_DESCRIPTION| Common Environment Variable| Contact Center Room  
efCommonVars_CONVERSATION_SEARCH_WINDOW_HRS| Common Environment Variable| "24"  
efCommonVars_TZ| Common Environment Variable| UTC  
efCommonVars_MASK_ATTRIBUTES_PATH| Common Environment Variable| /sensitive.js  
efCommonVars_LOGGING_CONFIG| Common Environment Variable| /logback/logback-spring.xml  
efCommonVars_ROOM_IS_USER_ID| Common Environment Variable| false  
clusterDomain|  | root domain for the cluster DNS| “cluster.local”  
imageCredentials| registry| container image registry, must be same as global.imageRegistry| [gitimages.expertflow.com](http://gitimages.expertflow.com/)  
username| username for the registry| efcx  
password| password for the user of the registry| RecRpsuH34yqp56YRFUb  
email| email address for the registry config| [devops@expertflow.com](mailto:devops@expertflow.com)  
efConnectionVars|  | Contains list of all the sub-charts related connection parameters| list of parameters.  
sub-chart|  |  |   
enabled| enable of disable a sub-chart deployment. true | false| true  
  
`Image Pull Secret is created at runtime based on these variables, a valid dockerconfig in JSON format is created at runtime and added to the kubernetes engine as secret with the name of ef-gitlab-secret`

All sub-charts are named after the component name for which it is developed and its values are evaluated from meta chart’s values.yaml file 

### Sub-Chart Details

All sub-charts have below given details available. Click Expander to view.

![](images/icons/grey_arrow_down.png)Click here to expand...

## Parameters

### Global parameters

Name| Description| Value  
---|---|---  
`global.ingressRouter`| Global FQDN mapping| `""`  
`global.ingressCertName`| Ingress TLS Certificate secret must be created before deployment| `""`  
`global.ingressClassName`| ingress class name for all the ingress resources deployed using this helm chart| `""`  
`global.commonIngressAnnotations`| Common Annotations for all the ingress resources, add/update for individual resources if not common| `{}`  
`global.imageRegistry`| default image registry to images from| `""`  
`global.imagePullSecrets`| Global Docker registry secret names as an array| `[]`  
`global.compatibility.openshift.adaptSecurityContext`| Adapt the securityContext sections of the deployment to make them compatible with Openshift restricted-v2 SCC: remove runAsUser, runAsGroup and fsGroup and let the platform use their allowed default IDs. Possible values: auto (apply if the detected running cluster is Openshift), force (perform the adaptation always), disabled (do not perform adaptation)| `auto`  
  
### Common parameters

Name| Description| Value  
---|---|---  
`nameOverride`| String to partially override _**COMPONENT___NAME**_.fullname template (will maintain the release name)| `""`  
`fullnameOverride`| String to fully override _**COMPONENT___NAME**_.fullname template| `""`  
`namespaceOverride`| String to fully override common.names.namespace| `""`  
`kubeVersion`| Force target Kubernetes version (using Helm capabilities if not set)| `""`  
`clusterDomain`| Kubernetes Cluster Domain| `cluster.local`  
`extraDeploy`| Extra objects to deploy (value evaluated as a template)| `[]`  
`commonLabels`| Add labels to all the deployed resources| `{}`  
`commonAnnotations`| Add annotations to all the deployed resources| `{}`  
`diagnosticMode.enabled`| Enable diagnostic mode (all probes will be disabled and the command will be overridden)| `false`  
`diagnosticMode.command`| Command to override all containers in the the deployment(s)/statefulset(s)| `["sleep"]`  
`diagnosticMode.args`| Args to override all containers in the the deployment(s)/statefulset(s)| `["infinity"]`  
  
### _**COMPONENT___NAME**_ parameters

Name| Description| Value  
---|---|---  
`image.registry`|  _**COMPONENT___NAME**_ image registry| `REGISTRY_NAME`  
`image.repository`|  _**COMPONENT___NAME**_ image repository| `REPOSITORY_NAME/___COMPONENT___NAME___`  
`image.digest`|  _**COMPONENT___NAME**_ image digest in the way sha256:aa.... Please note this parameter, if set, will override the tag| `""`  
`image.pullPolicy`|  _**COMPONENT___NAME**_ image pull policy| `IfNotPresent`  
`image.pullSecrets`| Specify docker-registry secret names as an array| `[]`  
`automountServiceAccountToken`| Mount Service Account token in pod| `false`  
`hostAliases`| Deployment pod host aliases| `[]`  
`command`| Override default container command (useful when using custom images)| `[]`  
`args`| Override default container args (useful when using custom images)| `[]`  
`extraEnvVars`| Extra environment variables to be set on _**COMPONENT___NAME**_ containers| `[]`  
`extraEnvVarsCM`| ConfigMap with extra environment variables| `""`  
`extraEnvVarsSecret`| Secret with extra environment variables| `""`  
`efConnectionVars`| Configmap true false| `false`  
`efEnvironmentVars`| ConfigMap true false| `false`  
  
###  _**COMPONENT___NAME**_ deployment parameters

Name| Description| Value  
---|---|---  
`replicaCount`| Number of _**COMPONENT___NAME**_ replicas to deploy| `1`  
`revisionHistoryLimit`| The number of old history to retain to allow rollback| `10`  
`updateStrategy.type`|  _**COMPONENT___NAME**_ deployment strategy type| `RollingUpdate`  
`updateStrategy.rollingUpdate`|  _**COMPONENT___NAME**_ deployment rolling update configuration parameters| `{}`  
`podLabels`| Additional labels for _**COMPONENT___NAME**_ pods| `{}`  
`podAnnotations`| Annotations for _**COMPONENT___NAME**_ pods| `{}`  
`podAffinityPreset`| Pod affinity preset. Ignored if `affinity` is set. Allowed values: `soft` or `hard`| `""`  
`podAntiAffinityPreset`| Pod anti-affinity preset. Ignored if `affinity` is set. Allowed values: `soft` or `hard`| `""`  
`nodeAffinityPreset.type`| Node affinity preset type. Ignored if `affinity` is set. Allowed values: `soft` or `hard`| `""`  
`nodeAffinityPreset.key`| Node label key to match Ignored if `affinity` is set.| `""`  
`nodeAffinityPreset.values`| Node label values to match. Ignored if `affinity` is set.| `[]`  
`affinity`| Affinity for pod assignment| `{}`  
`hostNetwork`| Specify if host network should be enabled for _**COMPONENT___NAME**_ pod| `false`  
`hostIPC`| Specify if host IPC should be enabled for _**COMPONENT___NAME**_ pod| `false`  
`dnsPolicy`| Specifies the DNS policy for the _**COMPONENT___NAME**_ pod| `""`  
`dnsConfig`| Allows users more control on the DNS settings for a Pod. Required if `dnsPolicy` is set to `None`| `{}`  
`nodeSelector`| Node labels for pod assignment. Evaluated as a template.| `{}`  
`tolerations`| Tolerations for pod assignment. Evaluated as a template.| `[]`  
`priorityClassName`|  _**COMPONENT___NAME**_ pods' priorityClassName| `""`  
`schedulerName`| Name of the k8s scheduler (other than default)| `""`  
`terminationGracePeriodSeconds`| In seconds, time the given to the _**COMPONENT___NAME**_ pod needs to terminate gracefully| `""`  
`topologySpreadConstraints`| Topology Spread Constraints for pod assignment| `[]`  
`podSecurityContext.enabled`| Enabled _**COMPONENT___NAME**_ pods' Security Context| `false`  
`podSecurityContext.fsGroupChangePolicy`| Set filesystem group change policy| `Always`  
`podSecurityContext.supplementalGroups`| Set filesystem extra groups| `[]`  
`podSecurityContext.fsGroup`| Set _**COMPONENT___NAME**_ pod's Security Context fsGroup| `1001`  
`podSecurityContext.sysctls`| sysctl settings of the _**COMPONENT___NAME**_ pods| `[]`  
`containerSecurityContext.enabled`| Enabled containers' Security Context| `false`  
`containerSecurityContext.seLinuxOptions`| Set SELinux options in container| `nil`  
`containerSecurityContext.runAsUser`| Set containers' Security Context runAsUser| `1001`  
`containerSecurityContext.runAsGroup`| Set containers' Security Context runAsGroup| `1001`  
`containerSecurityContext.runAsNonRoot`| Set container's Security Context runAsNonRoot| `true`  
`containerSecurityContext.privileged`| Set container's Security Context privileged| `false`  
`containerSecurityContext.readOnlyRootFilesystem`| Set container's Security Context readOnlyRootFilesystem| `true`  
`containerSecurityContext.allowPrivilegeEscalation`| Set container's Security Context allowPrivilegeEscalation| `false`  
`containerSecurityContext.capabilities.drop`| List of capabilities to be dropped| `["ALL"]`  
`containerSecurityContext.seccompProfile.type`| Set container's Security Context seccomp profile| `RuntimeDefault`  
`containerPorts`| Array of additional container ports for the Nginx container| `[]`  
`resourcesPreset`| Set container resources according to one common preset (allowed values: none, nano, micro, small, medium, large, xlarge, 2xlarge). This is ignored if resources is set (resources is recommended for production).| `none`  
`resources`| Set container requests and limits for different resources like CPU or memory (essential for production workloads)| `{}`  
`lifecycleHooks`| Optional lifecycleHooks for the _**COMPONENT___NAME**_ container| `{}`  
`startupProbe.enabled`| Enable startupProbe| `false`  
`startupProbe.initialDelaySeconds`| Initial delay seconds for startupProbe| `30`  
`startupProbe.periodSeconds`| Period seconds for startupProbe| `10`  
`startupProbe.timeoutSeconds`| Timeout seconds for startupProbe| `5`  
`startupProbe.failureThreshold`| Failure threshold for startupProbe| `6`  
`startupProbe.successThreshold`| Success threshold for startupProbe| `1`  
`livenessProbe.enabled`| Enable livenessProbe| `true`  
`livenessProbe.initialDelaySeconds`| Initial delay seconds for livenessProbe| `30`  
`livenessProbe.periodSeconds`| Period seconds for livenessProbe| `10`  
`livenessProbe.timeoutSeconds`| Timeout seconds for livenessProbe| `5`  
`livenessProbe.failureThreshold`| Failure threshold for livenessProbe| `6`  
`livenessProbe.successThreshold`| Success threshold for livenessProbe| `1`  
`readinessProbe.enabled`| Enable readinessProbe| `true`  
`readinessProbe.initialDelaySeconds`| Initial delay seconds for readinessProbe| `5`  
`readinessProbe.periodSeconds`| Period seconds for readinessProbe| `5`  
`readinessProbe.timeoutSeconds`| Timeout seconds for readinessProbe| `3`  
`readinessProbe.failureThreshold`| Failure threshold for readinessProbe| `3`  
`readinessProbe.successThreshold`| Success threshold for readinessProbe| `1`  
`autoscaling.enabled`| Enable autoscaling for _**COMPONENT___NAME**_ deployment| `false`  
`autoscaling.minReplicas`| Minimum number of replicas to scale back| `""`  
`autoscaling.maxReplicas`| Maximum number of replicas to scale out| `""`  
`autoscaling.targetCPU`| Target CPU utilization percentage| `""`  
`autoscaling.targetMemory`| Target Memory utilization percentage| `""`  
`extraVolumes`| Array to add extra volumes| `[]`  
`extraVolumeMounts`| Array to add extra mount| `[]`  
`serviceAccount.create`| Enable creation of ServiceAccount for _**COMPONENT___NAME**_ pod| `false`  
`serviceAccount.name`| The name of the ServiceAccount to use.| `""`  
`serviceAccount.annotations`| Annotations for service account. Evaluated as a template.| `{}`  
`serviceAccount.automountServiceAccountToken`| Auto-mount the service account token in the pod| `false`  
`sidecars`| Sidecar parameters| `[]`  
`sidecarSingleProcessNamespace`| Enable sharing the process namespace with sidecars| `false`  
`initContainers`| Extra init containers| `[]`  
`pdb.create`| Created a PodDisruptionBudget| `false`  
`pdb.minAvailable`| Min number of pods that must still be available after the eviction.| `""`  
`pdb.maxUnavailable`| Max number of pods that can be unavailable after the eviction.| `""`  
  
### Traffic Exposure parameters

Name| Description| Value  
---|---|---  
`service.type`| Service type| `ClusterIP`  
`service.enabled`| whether the service object should be created for this component| `true`  
`service.type`| Type of the Service port exposed| `ClusterIP`  
`service.port`| Port Number of the service| `""`  
`service.targetPort`| targetPort for the container where this service will route the traffic to| `""`  
`service.portName`| Name of the Service's port -- should be same as targetPort| `""`  
`service.protocol`| Type of the protocol for this service TCP or UDP| `TCP`  
`service.nodePort`| Valid if the type is set to NodePort -- range 30000 to 32676| `""`  
`service.clusterIP`|  _**COMPONENT___NAME**_ service Cluster IP| `""`  
`service.extraPorts`| Extra ports to expose (normally used with the `sidecar` value)| `[]`  
`service.sessionAffinity`| Session Affinity for Kubernetes service, can be "None" or "ClientIP"| `None`  
`service.sessionAffinityConfig`| Additional settings for the sessionAffinity| `{}`  
`service.annotations`| Service annotations| `{}`  
`service.externalTrafficPolicy`| Enable client source IP preservation| `Cluster`  
`networkPolicy.enabled`| Specifies whether a NetworkPolicy should be created| `false`  
`networkPolicy.allowExternal`| Don't require server label for connections| `true`  
`networkPolicy.allowExternalEgress`| Allow the pod to access any range of port and all destinations.| `true`  
`networkPolicy.extraIngress`| Add extra ingress rules to the NetworkPolicy| `[]`  
`networkPolicy.extraEgress`| Add extra ingress rules to the NetworkPolicy (ignored if allowExternalEgress=true)| `[]`  
`networkPolicy.ingressNSMatchLabels`| Labels to match to allow traffic from other namespaces| `{}`  
`networkPolicy.ingressNSPodMatchLabels`| Pod labels to match to allow traffic from other namespaces| `{}`  
`ingress.enabled`| Set to true to enable ingress record generation| `true`  
`ingress.pathType`| Ingress path type| `ImplementationSpecific`  
`ingress.apiVersion`| Force Ingress API version (automatically detected if not set)| `""`  
`ingress.hostname`| Default host for the ingress resource| `fqdn.com`  
`ingress.path`| The Path to Nginx. You may need to set this to '/*' in order to use this with ALB ingress controllers.| `""`  
`ingress.annotations`| Additional annotations for the Ingress resource. To enable certificate autogeneration, place here your cert-manager annotations.| `{}`  
`ingress.ingressClassName`| Set the ingerssClassName on the ingress record for k8s 1.18+| `nginx`  
`ingress.extraHosts`| The list of additional hostnames to be covered with this ingress record.| `[]`  
`ingress.extraPaths`| Any additional arbitrary paths that may need to be added to the ingress under the main host.| `nil`  
`ingress.tlsSecretName`| If you're providing your own certificates, please use this to add the certificates as secrets| `{{ .Values.global.ingressCertName }}`  
`ingress.extraRules`| The list of additional rules to be added to this ingress record. Evaluated as a template| 
