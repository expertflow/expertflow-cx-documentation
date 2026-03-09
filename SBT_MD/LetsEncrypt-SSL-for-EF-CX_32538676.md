# CX Knowledgebase : LetsEncrypt SSL for EF-CX

If the EFCX solution is deployed using an FQDN that is accessible from the internet, a LetsEncrypt based SSL is also another option to secure the traffic using HTTPS.

Follow these steps to enable LE based SSL certificate for the EFCX solution.

## Deploy Cert-Manager

if the cert-manager is not already deployed, you can run this command to deploy it.
[code] 
    helm repo add jetstack https://charts.jetstack.io --force-update
[/code]
[code] 
    helm upgrade --install cert-manager jetstack/cert-manager \
      --namespace cert-manager --create-namespace \
      --version v1.18.2 \
      --set installCRDs=true
    
[/code]

verify all the pods are in running state 
[code] 
    kubectl get pods -n cert-manager
[/code]

sample output 
[code] 
    # kubectl get pods -n cert-manager
    NAME                                      READY   STATUS    RESTARTS      AGE
    cert-manager-6fb4cc6c55-k7wnh             1/1     Running   4 (17h ago)   72d
    cert-manager-cainjector-86f7f4749-qpgvt   1/1     Running   4 (17h ago)   72d
    cert-manager-webhook-66c85f8577-vlljw     1/1     Running   4 (17h ago)   72d
[/code]

## Create ClusterIssuer Resource

once the deployment of cert-manager is ready, create the ClusterIssuer resource.

Create ClusterIssuer reource file `cert-manager-cluster-issuer.yaml`.
[code] 
    apiVersion: cert-manager.io/v1
    kind: ClusterIssuer
    metadata:
      name: ef-letsencrypt-prod
      namespace: cert-manager
    spec:
      acme:
        # The ACME server URL
        server: https://acme-v02.api.letsencrypt.org/directory
        # Email address used for ACME registration
        email: devops@expertflow.com
        # Name of a secret used to store the ACME account private key
        privateKeySecretRef:
          name: ef-letsencrypt-prod
        # Enable the HTTP-01 challenge provider
        solvers:
        - http01:
            ingress:
              class: nginx  #  Change the class: nginx to traefik when using traefik ingress controller ( default in k3s based deployments ) 
    
[/code]

apply the manifest
[code] 
    kubectl apply -f cert-manager-cluster-issuer.yaml
[/code]

get the status of the ClusterIssuer ( you might have to wait for sometime to get the ClusterIssuer ready ) 

a ready state ClusterIssuer is required before proceeding with next steps.

sample output
[code] 
    # kubectl get -f cert-manager-cluster-issuer.yaml
    NAME                  READY   AGE
    ef-letsencrypt-prod   True    55m
[/code]

once the ClusterIssuer is in the ready state, update the ingress manifests to use the newly created ClusterIssuer.

Next step is completely optional, unless you want to customize the certificate with custom details, which is normally not required for CX and its associated components. 

## Create Certificate ( Optional ) 

We are not creating any certificate as the ingresses created below when applied, will automatically call the respective ClusterIssuer to generate a certificate with default choices. However, if there is a requirement of creating a certificate with customizable options like key size ( default 2048), commonName, cipher algorithms, it becomes necessary to add them to the Certificate request before it is signed by the ClusterIssuer.

create a file `ef-certificate.yaml` with below given contents

below given is a template of a Certificate request which contains most of the possible options to be customized if required 
[code] 
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
      name: devops.expertflow.com
      namespace: expertflow  # repeat this for ef-external, ef-cti, ef-voice
    spec:
      # Secret names are always required.
      secretName: le-ef-ingress-tls-secret
    
      # secretTemplate is optional. If set, these annotations and labels will be
      # copied to the Secret named example-com-tls. These labels and annotations will
      # be re-reconciled if the Certificate's secretTemplate changes. secretTemplate
      # is also enforced, so relevant label and annotation changes on the Secret by a
      # third party will be overwriten by cert-manager to match the secretTemplate.
      secretTemplate:
        annotations:
          my-secret-annotation-1: "foo"
          my-secret-annotation-2: "bar"
        labels:
          my-secret-label: foo
    
      duration: 2160h # 90d
      renewBefore: 360h # 15d
      subject:
        organizations:
          - expertflow
      # The use of the common name field has been deprecated since 2000 and is
      # discouraged from being used.
      commonName: devops.expertflow.com
      isCA: false
      privateKey:
        algorithm: RSA
        encoding: PKCS1
        size: 2048
      usages:
        - server auth
        - client auth
      # At least one of a DNS Name, URI, or IP address is required.
      dnsNames:
        - devops.expertflow.com
        - www.devops.expertflow.com
      uris:
        - spiffe://cluster.local/ns/sandbox/sa/example
      ipAddresses:
        - 192.168.0.5
      # Issuer references are always required.
      issuerRef:
        name: ef-letsencrypt-prod
        # We can reference ClusterIssuers by changing the kind here.
        # The default value is Issuer (i.e. a locally namespaced Issuer)
        kind: Issuer
        # This is optional since cert-manager will default to this value however
        # if you are using an external issuer, change this to that issuer group.
        group: cert-manager.io
[/code]

apply the `ef-certificate.yaml`
[code] 
    kubectl apply -f ef-certificate.yaml
[/code]

for EFCX, this has to be applied for both `expertflow` and `ef-external` namespaces.

Skip rest of the steps mentioned below for helm based deployments and update the helm charts' values files accordingly.

## Update the ingress manifests ( for non-helm based releases only )

#### When using nginx ingress controller 

add the `cert-manager/cluster-issuer` annotation to ingress manifests.
[code] 
    sed -i  '/nginx$/a\    cert-manager.io/cluster-issuer: "ef-letsencrypt-prod"' cim/Ingresses/nginx/*.yaml
[/code]

change the name of the secret holding the SSL certificate generated by cert-manager.
[code] 
    sed -i -e 's/ef-ingress-tls-secret/le-ef-ingress-tls-secret/g' cim/Ingresses/nginx/*.yaml
[/code]

Apply the ingress manifests 
[code] 
    kubectl  apply -f cim/Ingresses/nginx/
[/code]

#### When using traefik as ingress controller

add the `cert-manager/cluster-issuer` annotation to ingress manifests.
[code] 
    sed -i  '/traefik$/a\    cert-manager.io/cluster-issuer: "ef-letsencrypt-prod"' cim/Ingresses/traefik/*.yaml
[/code]

change the name of the secret holding the SSL certificate generated by cert-manager.
[code] 
    sed -i -e 's/ef-ingress-tls-secret/le-ef-ingress-tls-secret/g' cim/Ingresses/traefik/*.yaml
[/code]

Apply the ingress manifests 
[code] 
    kubectl  apply -f cim/Ingresses/traefik/*.yaml
[/code]

##### Validation

after the ingresses are applied, all required namespaces are populated with the required Certificate as secret.
[code] 
    # k get certificate -A
    NAMESPACE     NAME                          READY   SECRET                        AGE
    ef-external   le-ef-ingress-tls-secret      True    le-ef-ingress-tls-secret      51m
    expertflow    le-ef-ingress-tls-secret      True    le-ef-ingress-tls-secret      51m
    expertflow    le-le-ef-ingress-tls-secret   True    le-le-ef-ingress-tls-secret   51m
    
[/code]
