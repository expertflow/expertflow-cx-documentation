# CX Knowledgebase : Tainting a Control Plane Node

By default, a control plane node can manage application workloads as well. This is okay for a lighter workload (~50 concurrent conversations) and [CX Single Node Deployment](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/64487674/RKE2+Single+Node+Deployment). But, for a higher workload or a multi-cluster setup, all control plane nodes should be tainted to schedule control-plane pods only. 

First get the nodes to identify which are control plane / master nodes.
[code] 
    kubectl get nodes
[/code]

Then to taint the master nodes, use the following command for each of the master node.
[code] 
    kubectl taint nodes (nodename) node-role.kubernetes.io/master:NoSchedule
[/code]

Once done allow the RKE Ingress to spin up on control plane as well.
[code] 
    kubectl patch deploy nginx-ingress-nginx-ingress-controller -n ingress-nginx --type json -p='[{"op": "add", "path": "/spec/template/spec/tolerations", "value": [{"key": "node-role.kubernetes.io/master", "operator": "Exists", "effect": "NoSchedule"}]}]'
    kubectl patch deploy nginx-ingress-nginx-ingress-controller-default-backend -n ingress-nginx --type json -p='[{"op": "add", "path": "/spec/template/spec/tolerations", "value": [{"key": "node-role.kubernetes.io/master", "operator": "Exists", "effect": "NoSchedule"}]}]'
[/code]
