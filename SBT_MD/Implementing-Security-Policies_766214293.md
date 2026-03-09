# CX Knowledgebase : Implementing Security Policies

This document illustrates the implementation of the following security policies in EF-CX Ingresses.  
  
  * x-content-type-options

  * x-frame-options

  * x-xss-protection




## Step 1: Change the Directory

change the directory to `cim-solution/kubernetes/cim/Ingresses/nginx/`
[code] 
    cd cim-solution/kubernetes/cim/Ingresses/nginx/
[/code]

## Step 2: Updating the Annotation:-

Open the Ingress deployment manifests one by one and update the `nginx.ingress.kubernetes.io/configuration-snippet` annotations for each Ingress as described below.

Following ingresses should be updated:-

  * customer-widget-assets

  * unified-agent-assets

  * unified-admin

  * unified-agent

  * keycloak




Open the Ingress file using the following command:-
[code] 
    vi <Ingress deployment manifest>.yaml
[/code]

for example:-
[code] 
    vi ef-unified-agent-Ingress.yaml
[/code]

`nginx.ingress.kubernetes.io/configuration-snippet`annotation should look like this:-
[code] 
        nginx.ingress.kubernetes.io/configuration-snippet: |
          more_set_headers "Access-Control-Allow-Origin:$http_origin";
          more_set_headers "X-Content-Type-Options: nosniff";
          more_set_headers "X-Frame-Options: SAMEORIGIN";
          more_set_headers "X-XSS-Protection: 1; mode=block";
[/code]

for `keycloak` Ingress, `nginx.ingress.kubernetes.io/configuration-snippet`annotation should look like this:-
[code] 
        nginx.org/server-snippets: |
          location / {
            proxy_set_header X-Forwarded-For $host;
            proxy_set_header X-Forwarded-Proto $scheme;
          }
          more_set_headers "Access-Control-Allow-Origin:$http_origin";
          more_set_headers "X-Content-Type-Options: nosniff";
          more_set_headers "X-Frame-Options: SAMEORIGIN";
          more_set_headers "X-XSS-Protection: 1; mode=block";
[/code]

## Step 3: Apply changes:-

Once all the changes are done, run the following commands to redeploy the ingresses with updated annotations:-
[code] 
    kubectl delete -f ef-customer-widget-assets-Ingress.yaml
    kubectl delete -f ef-unified-agent-assets-Ingress.yaml
    kubectl delete -f ef-unified-admin-Ingress.yaml
    kubectl delete -f ef-unified-agent-Ingress.yaml
    kubectl delete -f ef-keycloak-Ingress.yaml
    kubectl apply -f ef-customer-widget-assets-Ingress.yaml
    kubectl apply -f ef-unified-agent-assets-Ingress.yaml
    kubectl apply -f ef-unified-admin-Ingress.yaml
    kubectl apply -f ef-unified-agent-Ingress.yaml
    kubectl apply -f ef-keycloak-Ingress.yaml
[/code]
