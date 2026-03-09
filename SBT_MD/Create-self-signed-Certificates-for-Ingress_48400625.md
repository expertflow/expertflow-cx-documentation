# CX Knowledgebase : Create self-signed Certificates for Ingress

### Create self-signed SSL/TLS Ingress Certificates 

Need to modify the **< FQDN>** with your current FQDN before applying the following command.

  1. Create the ingress Certs directory,

  2. 
[code]mkdir ingress-certs
         cd ingress-certs
[/code]

  3. set the Variable name to your FQDN

  4. 
[code]export FQDN=<enter FQDN here>
[/code]

  5. Now generate a secret with the following commands.
[code] openssl req -x509 \
         -newkey rsa:4096 \
         -sha256 \
         -days 3650 \
         -nodes \
         -keyout ${FQDN}.key \
         -out ${FQDN}.crt \
         -subj "/CN=${FQDN}" \
         -addext "subjectAltName=DNS:www.${FQDN},DNS:${FQDN}"
[/code]

  6. Create kubernetes secret in your required namespace 
[code] kubectl -n <NAMESPACE> create secret tls ef-ingress-tls-secret --key  ${FQDN}.key --cert ${FQDN}.crt
[/code]

  7. Switch to the previous directory
[code] cd ../
[/code]



