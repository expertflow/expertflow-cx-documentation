# CX Knowledgebase : Change Default ActiveMQ Passwords Using ConfigMap

This guide explains the process of updating ActiveMQ Passwords.

This process requires the system to be in an idle state before starting it.

## Step 1: Change the Directory
[code] 
    cd cim-solution/Kubernetes
[/code]

## Step 2: Create a New Directory

create a new directory inside `pre-deployment` directory to store ConfigMap:-
[code] 
    mkdir pre-deployment/activemq/
[/code]

## Step 3: Create a ConfigMap

Create/open the ConfigMap file to update the passwords using the following command
[code] 
    vi pre-deployment/activemq/activemq-jetty-cm.yaml
[/code]

once the file is opened, paste the following content and update `<admin-password>` and `<user-password>` to set the passwords for each user.
[code] 
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: activemq-jetty-conf
      namespace: ef-external
    data:
      activemq-jetty-conf: |
        admin: <admin password>, admin
        user: <user password>, user
[/code]

## Step 4: Apply the ConfigMap

use the following commands to delete and re-apply the ConfigMap created earlier.
[code] 
    kubectl apply -f pre-deployment/activemq/activemq-jetty-cm.yaml
[/code]

## Step 5: Update the ActiveMQ Deployment File

Run the following command to open the ActiveMQ deployment file.
[code] 
    vi cim/StatefulSet/ef-amq-statefulset.yaml
[/code]

Head over to `volumes` section and add the following volume:-
[code] 
          - name: activemq-jetty-conf
            configMap:
              name: activemq-jetty-conf
[/code]

Now move to the `volumeMounts` section and add the following volume mount:-
[code] 
              - name: activemq-jetty-conf
                mountPath: "/opt/apache-activemq-5.17.1/conf/jetty-realm.properties"
                subPath: activemq-jetty-conf
[/code]

ActiveMQ container requires root privileges to change the passwords. So we need to remove the following lines to remove container security:-
[code] 
          securityContext:
            runAsUser: 100
            fsGroup: 101
            runAsNonRoot: true
[/code]

Once pod security has been updated, we must update the service to NodePort so that users can access the ActiveMQ dashboard via the browser. Update the service with the following configurations:- 
[code] 
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        ef.service: ef-amq-svc
        ef: expertflow
      name: ef-amq-svc
      namespace: ef-external
    spec:
      type: NodePort
      ports:
          - name: "ef-amq-svc-8161"
          port: 8161
          targetPort: 8161
          nodePort: 30001
        - name: "ef-amq-svc-8162"
          port: 8162
          targetPort: 8162
          nodePort: 30002
        - name: "ef-amq-svc-61613"
          port: 61613
          targetPort: 61613
          nodePort: 30003
        - name: "ef-amq-svc-61614"
          port: 61614
          targetPort: 61614
          nodePort: 30004
        - name: "ef-amq-svc-61615"
          port: 61615
          targetPort: 61615
          nodePort: 30005
        - name: "ef-amq-svc-61616"
          port: 61616
          targetPort: 61616
          nodePort: 30006
        - name: "ef-amq-svc-61617"
          port: 61617
          targetPort: 61617
          nodePort: 30007 
      selector:
        app: ef-amq
[/code]

## Step 6: Redeploy the ActiveMQ

Run the following commands to redeploy the ActiveMQ with updated passwords:-
[code] 
    kubectl delete -f cim/StatefulSet/ef-amq-statefulset.yaml
    kubectl apply -f cim/StatefulSet/ef-amq-statefulset.yaml
[/code]

## Step 7: Access the Admin Panel

ActiveMQ dashboard can be accessed by using the following URL with the updated credentials:
[code] 
    <Host IP>:30001
[/code]
