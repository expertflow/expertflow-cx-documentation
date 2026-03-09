# CX Knowledgebase : Kubernetes Distributions

Expertflow CX requires a Kubernetes distribution for most of its core solution components. You may use any of the [CNCF certified Kubernetes distributions](https://landscape.cncf.io). Expertflow team uses and recommends [RKE2](https://docs.rke2.io/). To setup RKE for CX, see[RKE2 Control plane Deployment](RKE2-Control-plane-Deployment_2528874.html)

Expertflow CX product releases are tested on RKE2 unless mentioned otherwise in a release documentation. To learn more about Kubernetes, read [this article from Google](https://kubernetes.io/docs/concepts/overview/). 

The Expertflow team has tested the solution with following additional distributions are also supported. 

**RKE2** RECOMMENDED | [RKE2](https://docs.rke2.io/), also known as RKE for Government, is a Rancher's next-generation CNCF certified Kubernetes distribution. Expertflow recommends using RKE2 for an on-premise production deployment. Expertflow CX product releases are tested on RKE2 unless mentioned otherwise in a release documentation.   
---|---  
**K8s (Kube-adm)**| [Kubernetes (k8s)](https://kubernetes.io/) is the distribution used and maintained by Google for on-prem, cloud, and hybrid deployments. Use this distribution for a high available Kubernetes cluster deployment.  
**Tanzu Kubernetes Grid**|  Provided by VMWare with commercial support , consider using [Tanzu Kubernetes Grid](https://tanzu.vmware.com/kubernetes-grid) with VSphere and [vSAN, the VMware cloud-native storage](https://www.vmware.com/products/cloud-native-storage.html). This distribution is recommended for customer who want a enterprise class production kubernetes deployments.  
**K3s** | [K3s](https://k3s.io/) is lightweight and edge kubernetes distribution from Rancher. K3s is packaged as a single <70MB binary that reduces the dependencies and steps needed to install. You may use this distribution for a non-redundant simplex deployment or for testing of the solution within a single node. To proceed with using K3s for CX installation, follow [this installation guide](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2525046/K3s+Pre-Deployment+Installation+Guide).  
**MicroK8s**| [MicroK8s](https://microk8s.io/) is lightweight Kubernetes distribution from Canonical described as a **low-ops, minimal production** Kubernetes distribution.
