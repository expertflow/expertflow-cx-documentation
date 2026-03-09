# CX Knowledgebase : Voice Recording Components deployment on Kubernetes

This document illustrates the procedure and steps to deploy CX Voice Recording components on Kubernetes. 

# Before you begin, verify

  * Installed Kubernetes. If not, see [Deployment Planning](/wiki/pages/createpage.action?spaceKey=SBT&title=Deployment%20Planning&linkCreation=true&fromPageId=348880955)
  * Have already setup storage. If not yet, see [Storage Solution - Getting Started](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/2526989/Storage+Solution+-+Getting+Started)



# Prepare for CX Voice Recording Components Deployments

## Step 1: Clone the Expertflow CX repository
[code] 
    git clone -b <branch Name> https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cim/cim-solution.git
[/code]
[code] 
    cd cim-solution/kubernetes/
[/code]

## Step 2: Create Namespaces

  1. Create a [namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) `cx-voice-recording` for all Voice Recording components.



[code] 
    kubectl create namespace cx-voice-recording
[/code]

## Step 3: Apply Image Pull secret

  1. Run the following commands for applying ImagePullSecrets of Expertflow CX images.



[code] 
    kubectl apply -f cx-voice-recording/ef-imagePullSecret-cx-voice-recording.yaml
[/code]

## Step 4: Update FQDN

Voice Recording Componentes should be accessible by a fully qualified domain name. Assign the FQDN that resolves to the control plane node or KubeVIP.

`Replace <FQDN> with your FQDN for CX Voice Recording and run this command.`
[code] 
    sed -i 's/devops[0-9]*.ef.com/<FQDN>/g' cx-voice-recording/ConfigMaps/*  cx-voice-recording/Ingresses/nginx/* cx-voice-recording/Ingresses/traefik/*
[/code]

## Step 5: Deploy CX Voice Recording Components

  1. Change the directory 
[code] cd cx-voice-recording/
[/code]

  2. Apply all configurations in the ConfigMaps folder using: 
[code] kubectl apply -f ConfigMaps/
[/code]

  3. Create services for all deployment voice recording components
[code] kubectl apply -f Services/
[/code]

  4. Apply all the Deployment manifests 
[code] kubectl apply -f Deployments/
[/code]

  5. Before proceeding to the the next steps, wait for all the solution components to be up and ready.
[code] kubectl get pods -n cx-voice-recording 
[/code]




## Step 6 :Setup Ingress Routes

For RKE2-based Ingresses using Ingress-Nginx Controller
[code] 
    kubectl apply -f Ingresses/nginx/
[/code]
