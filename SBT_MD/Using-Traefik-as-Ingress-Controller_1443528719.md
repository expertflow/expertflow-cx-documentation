# CX Knowledgebase : Using Traefik as Ingress Controller

Expertflow CX Solution is delivered with ingress-nginx as the default ingress controller and all the helm based deployment of CX are customized to use the ingress-nginx as ingress controller. However, if this is not the case due to existing ingress controller being used is traefik, please use below given list of annotations and middle wares for Traefik to work properly.

### Create Traefik Middlewares

These middleware routine need to created only in `expertflow` namespace, all other namespaces will reference to them using kubernetes CRDs.

Create `traefik-middlewares.yaml` with below given contents
[code] 
    apiVersion: traefik.containo.us/v1alpha1
    kind: Middleware
    metadata:
      name: cim-stripprefix
      namespace: expertflow
    spec:
      stripPrefix:
        prefixes:
          - /agent-manager
          - /bot-framework
          - /business-calendar
          - /ccm
          - /cim-customer
          - /customer-widget
          - /file-engine
          - /license-manager
          - /routing-engine
          - /minio
          - /monitoring
          - /unified-admin
          - /unified-agent
          - /web-channel-manager
          - /360connector
          - /twilio-connector
          - /conversation-manager
          - /realtime-reports
          - /grafana
          - /facebook-connector
          - /cim
          - /telegram-connector
          - /scheduler
          - /assets
          - /instagram-connector
          - /team-announcement
          - /smppconnector
          - /viber-connector
          - /twitter-connector
          - /historical-reports
        forceSlash: false
    ---
    apiVersion: traefik.containo.us/v1alpha1
    kind: Middleware
    metadata:
      name: cim-cors
      namespace: expertflow
    spec:
      headers:
        accessControlAllowMethods:
          - "GET"
          - "OPTIONS"
          - "PUT"
          - "POST"
          - "DELETE"
          - "PATCH"
        accessControlMaxAge: 100
        accessControlAllowCredentials: true
        accessControlAllowHeaders:
          - "*"
        accessControlAllowOriginList:
          - http://devops211.ef.com
    ---
    apiVersion: traefik.containo.us/v1alpha1
    kind: Middleware
    metadata:
      name: cim-limit
      namespace: expertflow
    spec:
      buffering:
        maxRequestBodyBytes: 20000000
    
[/code]

### Update Ingress annotations for Traefik

Now add these annotations to all components

**component**| **annotations**  
---|---  
  
  * CX
    * web-channel-manager
    * team-announcement
    * routing-engine
    * license-manager
    * historical-reports
    * customer-widget
    * cim-customer
    * bot-framework
    * agent-manager
    * conversation-monitor
    * conversation-manager
    * ccm
  * Web Channels
    * viber-connector
    * twitter-connector
    * twilio-connector
    * telegram-connector
    * smpp-connector
    * facebook-connector
    * connect360
  * agent-desk
    * unified-agent
    * grafana
  * Surveys
    * scheduled-activities
  * keycloak

|  [kubernetes.io/ingress.class:](http://kubernetes.io/ingress.class:) traefik  
[traefik.ingress.kubernetes.io/router.middlewares:](http://traefik.ingress.kubernetes.io/router.middlewares:) expertflow-cim-stripprefix@kubernetescrd  
[traefik.ingress.kubernetes.io/router.entrypoints:](http://traefik.ingress.kubernetes.io/router.entrypoints:) websecure  
[traefik.ingress.kubernetes.io/router.tls:](http://traefik.ingress.kubernetes.io/router.tls:) 'true'  
  
  * agent-desk
    * unified-agent-assets

|  [kubernetes.io/ingress.class:](http://kubernetes.io/ingress.class:) traefik  
[traefik.ingress.kubernetes.io/router.entrypoints:](http://traefik.ingress.kubernetes.io/router.entrypoints:) websecure  
[traefik.ingress.kubernetes.io/router.tls:](http://traefik.ingress.kubernetes.io/router.tls:) 'true'  
  
  * CX
    * unified-admin
    * default
    * historical-reports
    * file-engine

|  [kubernetes.io/ingress.class:](http://kubernetes.io/ingress.class:) traefik  
[traefik.ingress.kubernetes.io/router.middlewares:](http://traefik.ingress.kubernetes.io/router.middlewares:) expertflow-cim-stripprefix@kubernetescrd, expertflow-cim-cors@kubernetescrd  
[traefik.ingress.kubernetes.io/router.entrypoints:](http://traefik.ingress.kubernetes.io/router.entrypoints:) websecure  
[traefik.ingress.kubernetes.io/router.tls:](http://traefik.ingress.kubernetes.io/router.tls:) 'true'  
  
### General Rules for other components

If there is `nginx.ingress.kubernetes.io/rewrite-target: /$2` existing for an ingress resources, its compatible alternate option is `traefik.ingress.kubernetes.io/router.middlewares: expertflow-cim-stripprefix@kubernetescrd` in Traefik, however other annotations will remain same.

For CORS sensitive components, you will have to add `expertflow-cim-cors@kubernetescrd` as CORS controllerr.
