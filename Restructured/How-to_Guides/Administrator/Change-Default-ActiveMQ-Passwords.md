---
title: "Change Default ActiveMQ Passwords Using ConfigMap"
summary: "How-to guide for updating ActiveMQ admin and user passwords in an ExpertFlow CX Kubernetes deployment — using a ConfigMap mounted into the ActiveMQ StatefulSet, with service NodePort exposure and pod redeployment."
audience: [administrator]
product-area: [platform]
doc-type: how-to
difficulty: intermediate
keywords: ["ActiveMQ password change CX", "ActiveMQ ConfigMap CX", "ActiveMQ jetty-realm CX", "change ActiveMQ credentials CX", "ActiveMQ admin password Kubernetes CX"]
aliases: ["ActiveMQ password update CX", "ActiveMQ credentials CX", "jetty-realm.properties CX"]
last-updated: 2026-03-10
---

# Change Default ActiveMQ Passwords Using ConfigMap

This guide updates the ActiveMQ admin and user passwords in an ExpertFlow CX Kubernetes deployment. Passwords are injected via a ConfigMap mounted into the ActiveMQ StatefulSet as `jetty-realm.properties`.

> **Requirements**: The system must be in an **idle state** (no active conversations) before starting. This procedure requires redeploying the ActiveMQ pod.

---

## Step 1: Navigate to the CX Kubernetes Directory

```bash
cd cim-solution/Kubernetes
```

---

## Step 2: Create the ConfigMap Directory

```bash
mkdir pre-deployment/activemq/
```

---

## Step 3: Create the ConfigMap File

Create the ConfigMap YAML:

```bash
vi pre-deployment/activemq/activemq-jetty-cm.yaml
```

Paste the following content, replacing `<admin password>` and `<user password>` with your chosen passwords:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: activemq-jetty-conf
  namespace: ef-external
data:
  activemq-jetty-conf: |
    admin: <admin password>, admin
    user: <user password>, user
```

---

## Step 4: Apply the ConfigMap

```bash
kubectl apply -f pre-deployment/activemq/activemq-jetty-cm.yaml
```

---

## Step 5: Update the ActiveMQ StatefulSet

Open the StatefulSet file:

```bash
vi cim/StatefulSet/ef-amq-statefulset.yaml
```

### Add the ConfigMap volume

In the `volumes` section:

```yaml
- name: activemq-jetty-conf
  configMap:
    name: activemq-jetty-conf
```

### Mount the volume

In the `volumeMounts` section:

```yaml
- name: activemq-jetty-conf
  mountPath: "/opt/apache-activemq-5.17.1/conf/jetty-realm.properties"
  subPath: activemq-jetty-conf
```

### Remove container security context

ActiveMQ requires root privileges to update passwords. Remove the following lines from the StatefulSet:

```yaml
securityContext:
  runAsUser: 100
  fsGroup: 101
  runAsNonRoot: true
```

### Expose the ActiveMQ dashboard via NodePort

Update the service definition to NodePort so you can access the ActiveMQ web console after redeployment:

```yaml
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
```

---

## Step 6: Redeploy ActiveMQ

```bash
kubectl delete -f cim/StatefulSet/ef-amq-statefulset.yaml
kubectl apply -f cim/StatefulSet/ef-amq-statefulset.yaml
```

---

## Step 7: Access the Admin Panel

Once the pod is running, access the ActiveMQ web console:

```
http://<Host IP>:30001
```

Log in with the updated admin credentials.

---

## Related Articles

- [Vault Dynamic Credentials — ActiveMQ](Vault-Dynamic-Credentials-ActiveMQ.md)
- [Vault Configuration](Vault-Configuration.md)
