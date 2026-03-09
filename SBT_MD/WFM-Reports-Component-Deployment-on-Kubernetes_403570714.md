# CX Knowledgebase : WFM-Reports Component Deployment on Kubernetes

This document illustrates the procedure and steps to deploy WFM-Reports Components on Kubernetes.

# Before you begin, verify

  * Installed Kubernetes. If not, see [Deployment Planning](/wiki/pages/createpage.action?spaceKey=SBT&title=Deployment%20Planning&linkCreation=true&fromPageId=403570714)
  * Have already setup storage. If not yet, see [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started)



# Prepare for WFM-Reports Deployments

## Step 1: Clone the WFM-Reports repository
[code] 
    git clone -b <branch Name> https://gitlab.expertflow.com/wfm/wfm-reports.git
[/code]
[code] 
    cd wfm-reports/
[/code]

## Step 2: Create Namespaces

  1. Create a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) `wfm` for all WFM components.



[code] 
    kubectl create namespace wfm
[/code]

## Step 3: Apply Image Pull secret

  1. Run the following commands for applying ImagePullSecrets of WFM images.



[code] 
    kubectl apply -f WFM-Reports/ef-imagePullSecret-wfm.yaml
[/code]

## Step 4: Update FQDN

Wfm-Reports Component should be accessible by a fully qualified domain name. Assign the FQDN.

`Replace <FQDN> with your FQDN for wfm-reports and run this command.`
[code] 
    sed -i 's/devops[0-9]*.ef.com/<FQDN>/g' WFM-Reports/ConfigMaps/*  WFM-Reports/Ingresses/nginx/* WFM-Reports/Ingresses/traefik/*
[/code]

## Step 5: Deploy WFM-Report Component

  1. Change the directory
[code] cd WFM-Reports/
[/code]

  2. Apply ConfigMaps 
[code] kubectl apply -f ConfigMaps/ef-wfm-reports-configmap.yaml
[/code]

  3. Create services for wfm-report 
[code] kubectl apply -f Services/ef-wfm-reports-service.yaml
[/code]

  4. Apply the Deployment manifest 
[code] kubectl apply -f Deployments/ef-wfm-reports-deployment.yaml
[/code]

  5. Before proceeding to the the next steps, wait for all the solution components to be up and ready.
[code] kubectl get pods -n wfm 
[/code]




## Step 6 :Setup Ingress Routes

For RKE2-based Ingresses using Ingress-Nginx Controller
[code] 
    kubectl apply -f Ingresses/nginx/ef-wfm-reports-Ingress.yaml
[/code]
