# CX Knowledgebase : WebRTC Deployment Guide-not to publish

# Prerequisites

Follow the guides [here ](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197885954/4.5+Setting+up+Expertflow+CX+Voice)to deploy the components for CX Voice.

Once CX Voice is deployed below are the following points to follow:

  * Cisco Jabber device (UCCX - SU3) is required to set-up WebRTC Secure link deployment.

  * A Cisco CUBE is needed for integration between Jabber extensions and EFSwitch.




# Secure Link Component Deployment 

## Step 1: Clone the repository
[code] 
    git clone -b main https://efcx:RecRpsuH34yqp56YRFUb@gitlab.expertflow.com/cti/securelinkgenreation_deployment.git
[/code]
[code] 
    cd securelinkgenreation_deployment
[/code]

## Step 2: Update configMap

FQDN and Widgetidentifier must be the same as the EFCX WebRTC widget.

  1. Open **** securelinkgenreation_deployment/ConfigMaps/ef-securelinkgeneration-configmap.yaml _****_ file and add the following parameters
[code] SPRING_DATASOURCE_URL : jdbc:postgresql://ef-postgresql.ef-external.svc.cluster.local:5432/securelinkgeneration_db
            SPRING_DATASOURCE_USERNAME : "sa"
            SPRING_DATASOURCE_PASSWORD : "Expertflow123"
            ENCRYPTION_KEY: "1234567890123456"
            webwidgetfqdn : https://cim.expertflow.com/customer-widget/#/widget
            source : "SLG"
            linktimeout : "30"
            widgetIdentifier : "webrtc-widget"
[/code]




##   


## Step 3: Update FQDN

Expertflow CX should be accessible by a fully qualified domain name. Assign the FQDN that resolves to the control plane node or KubeVIP.

`Replace <FQDN> with your FQDN for Expertflow CX and run this command.`
[code] 
    sed -i 's/devops[0-9]*.ef.com/<FQDN>/g' ConfigMaps/* Ingresses/nginx/* Ingresses/traefik/*
[/code]

## Step 4: Pull Image Mannualy
[code] 
    CONTAINERD_ADDRESS=/run/k3s/containerd/containerd.sock /var/lib/rancher/rke2/bin/ctr  -n k8s.io i pull -u saifullah:saifullah96 gitimages.expertflow.com/cti/securelinkgeneration:1.6
[/code]

##   
Step 5: Update Deployment   

[code] 
    kubectl apply -f ConfigMaps/ef-securelinkgeneration-configmap.yaml
    kubectl apply -f Services/ef-securelinkgeneration-service.yaml
    kubectl apply -f Deployments/ef-securelinkgeneration-deployment.yaml
    
    #Apply Ingresses 
    #for RKE
    kubectl apply -f Ingresses/nginx/ef-securelinkgeneration-ingress.yaml
    
    #or 
    #for Traefik
    kubectl apply -f Ingresses/traefik/ef-securelinkgeneration-ingress.yaml
[/code]

# Customer Widget Configuration

  1. Open **cim-solution/kubernetes/cim/ConfigMaps/**_**ef-customer-widget-configmap.yaml**_ file and add the following parameter
[code] AUTHENTICATOR_URL : https://<FQDN>/secure-link
[/code]


![image-20240222-075343.png](attachments/349634566/349634606.png?width=250)

  2. Run the following commands to update the configMaps of the customer widget



[code] 
    kubectl delete -f ef-customer-widget-configmaps.yaml -n expertflow
    kubectl apply -f ef-customer-widget-configmaps.yaml -n expertflow
[/code]

  3. Open **cim-solution/kubernetes/cim/Deployments/**_**ef-customer-widget-deployment.yaml**_ file and add the following parameter
[code] - name: AUTHENTICATOR_URL
             valueFrom:
               configMapKeyRef:
                 key: AUTHENTICATOR_URL
                 name: ef-customer-widget-cm
[/code]


![image-20240222-075741.png](attachments/349634566/349634603.png?width=250)

  3. Run the following commands to update the Deployments of the customer widget
[code] kubectl delete -f ef-customer-widget-deployments.yaml -n expertflow
         kubectl apply -f ef-customer-widget-deployments.yaml -n expertflow
[/code]




# Unified Agent Configuration

  1. Open **cim-solution/kubernetes/cim/ConfigMaps/ef-unified-agent-configmap.yaml** _****_ file and add the following parameter
[code] SECURE_LINK_URL : https://<FQDN>/secure-link
         ENABLE_SECURE_LINK : "true"
[/code]

  2. Run the following commands to update the configMaps of the customer widget



[code] 
    kubectl delete -f ef-unified-agent-configmaps.yaml -n expertflow
    kubectl apply -f ef-unified-agent-configmaps.yaml -n expertflow
[/code]

  2. Open **cim-solution/kubernetes/cim/Deployments/ef-unified-agent-deployment.yaml** _****_ file and add the following parameter
[code] - name: SECURE_LINK_URL
             valueFrom:
               configMapKeyRef:
                 key: SECURE_LINK_URL
                 name: ef-unified-agent-cm
         - name: ENABLE_SECURE_LINK
             valueFrom:
               configMapKeyRef:
                 key: ENABLE_SECURE_LINK
                 name: ef-unified-agent-cm
[/code]


![image-20240222-084451.png](attachments/349634566/349634597.png?width=250)

# EFSwitch Configurations

### Configure SIP Trunk for outbound calls

  * Note: The SIP trunk in this case will be the Cisco CUBE gateway.

  * Open in browser: **https://IP-addr** , where**IP-addr** is the IP address of the server that EFSwitch is deployed on. 


![](attachments/349634566/349634618?width=500)

  * Add the **username** and **password** that was shown upon [installation of EFSwitch](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197886727/4.5+EFSwitch+Installation+Guide) and press **LOGIN**.

  * Press the **IP address** in the top right and select the **Domain** created in the **Domain creation section** of the [EFSwitch configuration document](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197886088/4.5+EFSwitch+Configurations+for+CX+Voice).

  * ![](attachments/349634566/349634615?width=500)
  * Open the **Gateways** section under the **Accounts** tab.

![image-20240222-095737.png](attachments/349634566/349634657.png?width=500)
  * Press the **ADD** button in the top right.

![image-20240222-095900.png](attachments/349634566/349634654.png?width=500)
  * Set the following fields:

    1. **Gateway** : A name of your choice e.g. MySipTrunk

    2. **Username** : The username of the SIP Trunk. Not needed for **IP-based** SIP trunks.

    3. **Password** : The password of the SIP Trunk. Not needed for**IP-based** SIP trunks.

    4. **Proxy** : The IP address and port of the SIP trunk e.g. 192.168.25.35:5060.

    5. **Register** : Set to **True**. Set to **False** for **IP-based** SIP trunks.

  * ![image-20240222-100014.png](attachments/349634566/349634651.png?width=500)
  * Press the **SAVE** button on the top right.

  * Open this newly created gateway and note the **URL** opened in the browser.

![image-20240222-110233.png](attachments/349634566/349634648.png?width=500)
  * From this URL note the **gateway ID** , i.e. :

    * For the URL https://192.168.1.201/app/gateways/gateway_edit.php?id=becc1f43-68b9-459a-908d-bbac57d042d5

    * The gateway ID is becc1f43-68b9-459a-908d-bbac57d042d5 (everything after **?id=**)

  * Add the IP address of the **SIP trunk** to the **EFSwitch ACL** :

    * Open **SIP Profiles** under the **Advanced** tab.

![image-20240222-100519.png](attachments/349634566/349634633.png?width=500)
  * Open the **external** profile and note the value of the **apply-register-acl** field.

![image-20240222-100419.png](attachments/349634566/349634645.png?width=500)
  * Open **Access controls** under the **Advanced** tab.

![image-20240222-100249.png](attachments/349634566/349634642.png?width=500)
  * Open the entry that matches the aforementioned **apply-register-acl** field.

![image-20240222-100648.png](attachments/349634566/349634639.png?width=500)
  *   * At the bottom add an entry where the the **Type** is set to ‘**allow** ’ and the **CIDR** field contains the **address** of the SIP Trunk.

  * Press the **SAVE** button on the top right.

  * Open **SIP Status** under the **Status** tab.

![image-20240222-100938.png](attachments/349634566/349634636.png?width=500)
  *     * Press the **Reload ACL** button at the top right.

  * Open **SIP Profiles** under the **Advanced** tab.

![image-20240222-100519.png](attachments/349634566/349634633.png?width=500)
  * Open the **external** profile and note the value of the **sip-port** field.

![](attachments/349634566/349634630?width=500)
  * Back out via the **BACK** button on the top right.

  * Open the **internal** profile and note the value of the **sip-port** field.

![](attachments/349634566/349634627?width=500)
  * Open a terminal and SSH into the EFSwitch machine via the command

  * 
[code]ssh EFSwitch-Server-Username@EFSwitch-Server-IP-Address
[/code]

  * Enter the EFSwitch server **SSH password** when prompted.

  * Enter and run the command

  * 
[code]su
[/code]

  * And enter the EFSwitch server **root password**.

  * Run the command

  * 
[code]sudo iptables -A INPUT -p tcp -m tcp --dport PORT -j ACCEPT
[/code]

    * Where **PORT** is the port noted down in the previous steps. Run the command once for each port.

  * Run the command

  * 
[code]sudo iptables-save
[/code]

  * Contact the SIP Trunk provider and have all traffic from the **EFSwitch** machine **public** IP address allowed.




### Configuring Call Dialplan

  * Open **Unified Admin** via the link **https://CX-FQDN/unified-admin**

    * Where **CX-FQDN** is the fully qualified domain name of the EF CX.

  * Open the **Web Widget** section.

![image-20240222-102658.png](attachments/349634566/349634624.png?width=500)
  *   * Open the **Widget** created for video calling, via the **Edit** option.

![image-20240222-105659.png](attachments/349634566/349634621.png?width=500)
  * Scroll down and note the value of the **Dialing URI** field.

  * Open in browser: **https://IP-addr** , where**IP-addr** is the IP address of the server that EFSwitch is deployed on. 


![](attachments/349634566/349634618?width=500)

  * Add the **username** and **password** that was shown upon [installation of EFSwitch](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197886727/4.5+EFSwitch+Installation+Guide) and press **LOGIN**.

  * Press the **IP address** in the top right and select the **Domain** created in the **Domain creation section** of the [EFSwitch configuration document](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197886088/4.5+EFSwitch+Configurations+for+CX+Voice).

![](attachments/349634566/349634615?width=500)
  * Open the **Dialplan Manager** section under the **Dialplans** tab.

![image-20240222-102113.png](attachments/349634566/349634612.png?width=500)
  * Press the **ADD** button in the top right.

![image-20240222-102222.png](attachments/349634566/349634609.png?width=500)
  * Fill the form with following details :

    * Name = WebRTC Video Call

    * Condition 1 = Select **destination_number** from list and set the value to the value of the**Dialing URI** noted in the previous steps.

    * Action 1 = Select first item from the list 

  * Press the **SAVE** button on top right Corner.

  * Re-open the **WebRTC Video Call** dialplan.

  * Set the **Context** field to the value of the **Domain** set in the **Domain creation section** of the [EFSwitch configuration document](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197886088/4.5+EFSwitch+Configurations+for+CX+Voice).

  * Set the **Domain** field to the value of the **Domain** set in the **Domain creation section** of the [EFSwitch configuration document](https://expertflow-docs.atlassian.net/wiki/spaces/CX/pages/197886088/4.5+EFSwitch+Configurations+for+CX+Voice).

  * Change the value of the **Type** column in the **Action** row to **bridge** and the **Data** field to **sofia/gateway/GATEWAY-ID/55${sip_h_X-Agent-Extension}@DOMAIN**

    * Where **GATEWAY-ID** is the **SIP Trunk gateway ID** noted in the previous section.

    * And **DOMAIN** is the value of the **Proxy** set in the **Gateway creation** section.

  * Press the **SAVE** button on top right Corner.



