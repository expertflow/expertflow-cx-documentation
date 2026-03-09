# CX Knowledgebase : Conversion of Single Node MongoDB to ReplicaSet

**WARNING**  
  
This procedure requires downtime for the Expertflow CX solution, please plan accordingly.

### Steps involved in converting the single node MonogDB to ReplicaSet

Shutdown all the ef-cx deployments in expertflow namespace 
[code] 
    kubectl -n expertflow scale deploy --replicas=0 -l app.kubernetes.io/instance=ef-cx
    kubectl -n expertflow scale deploy --replicas=0 -l app.kubernetes.io/instance=cx-channels
    kubectl -n expertflow scale deploy --replicas=0 -l app.kubernetes.io/instance=cx-agent-desk
[/code]

Temporarily stop the Reporting scheduler cron
[code] 
    kubectl -n expertflow patch cronjobs cx-reporting-cron -p '{"spec" : {"suspend" : true }}'
[/code]

Stop Surveys and Campaigns deployment objects
[code] 
    kubectl -n expertflow scale deploy -l app.kubernetes.io/instance=cx-campaigns  --replicas=0 
    kubectl -n expertflow scale deploy -l app.kubernetes.io/instance=cx-surveys  --replicas=0
[/code]

#### Backup the mongoDB

Please take back up the existing single node MongoDB using [Mongo, PostgreSQL Backup/Restore Procedure for EF-CX on Kubernetes ( manual procedure )](/wiki/pages/createpage.action?spaceKey=CX&title=Mongo%2C%20PostgreSQL%20Backup%2FRestore%20Procedure%20for%20EF-CX%20on%20Kubernetes%20%28%20manual%20procedure%20%29) to secure location

Uninstall the existing MongoDB solution using 
[code] 
    helm -n ef-external uninstall mongo
[/code]

Delete the mongoDB PVCs using the following command:
[code] 
    kubectl delete pvc -n ef-external datadir-mongo-mongodb-0 datadir-mongo-mongodb-1
[/code]

Deploy MongoDB in ReplicaSet using [Deployment of Mongo using ReplicaSet](Deployment-of-Mongo-using-ReplicaSet_774569985.html)

Restore the backup taken using [Mongo, PostgreSQL Backup/Restore Procedure for EF-CX on Kubernetes ( manual procedure )](/wiki/pages/createpage.action?spaceKey=CX&title=Mongo%2C%20PostgreSQL%20Backup%2FRestore%20Procedure%20for%20EF-CX%20on%20Kubernetes%20%28%20manual%20procedure%20%29) to the new MongoDB in HA/ReplicaSet

Delete the secret object in expertflow namespace using
[code] 
    kubectl -n expertflow delete secret mongo-mongodb-ca
[/code]

Recreate the secret from new deployment of MongoDB using
[code] 
    kubectl get secret mongo-mongodb-ca -n ef-external  -o yaml | sed 's/namespace: ef-external/namespace: expertflow/' | kubectl create -f -
[/code]

Edit/update the ef-connections variable responsible for connecting to the MongoDB Host string by editing the `helm-values/ef-cx-custom-values.yaml`

  * Comment/diable the existing the `MONGODB_HOST`

  * Add/update a new variable `MONGODB_HOST: mongo-mongodb-0.mongo-mongodb-headless.ef-external.svc.cluster.local:27017,mongo-mongodb-1.mongo-mongodb-headless.ef-external.svc.cluster.local:27017`

  * Add/update a new variable `MONGODB_READ_PREFERENCE: "secondaryPreferred"`

  * Add/update a new variable `MONGODB_REPLICASET: "expertflow"`

  * Add/update a new variable `MONGODB_REPLICASET_ENABLED: "true"`




Start all the deployments in expertflow namespace by executing 
[code] 
    helm upgrade --install --namespace expertflow --create-namespace  ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx
[/code]

Delete the config-map responsible for reportingConnector’s MongoDB connection string
[code] 
    kubectl -n expertflow delete configmap ef-reporting-connector-conf-cm 
[/code]

Edit the `pre-deployment/reportingConnector/reporting-connector.conf` and enable below given parameters and commenting the existing entries by putting # at the start 
[code] 
    #UNCOMMENT BELOW LINES IF YOU WANT TO USE MONGO replicaset
    mongo_host1=mongo-mongodb-0.mongo-mongodb-headless.ef-external.svc.cluster.local
    mongo_port1=27017
    mongo_host2=mongo-mongodb-1.mongo-mongodb-headless.ef-external.svc.cluster.local
    mongo_port2=27017
    mongo_host3=mongo-mongodb-0.mongo-mongodb-headless.ef-external.svc.cluster.local
    mongo_port3=27017
    mongo_host4=mongo-mongodb-0.mongo-mongodb-headless.ef-external.svc.cluster.local
    mongo_port4=27017
    mongo_host5=mongo-mongodb-0.mongo-mongodb-headless.ef-external.svc.cluster.local
    mongo_port5=27017
    mongo_host6=mongo-mongodb-0.mongo-mongodb-headless.ef-external.svc.cluster.local
    mongo_port6=27017
    
[/code]

Create the config-map with updated connection string
[code] 
    kubectl -n expertflow create configmap ef-reporting-connector-conf-cm --from-file=pre-deployment/reportingConnector/reporting-connector.conf
[/code]

Run helm upgrade to restart the deployment of reportingConnector
[code] 
    helm upgrade --install --namespace expertflow --set global.efCxReleaseName="ef-cx"   cx-reporting --debug --values helm-values/cx-reporting-scheduler-custom-values.yaml  expertflow/reporting 
[/code]

Rollout a restart of all other deployments to take effect of the new MongoDB connection string
[code] 
    kubectl -n expertflow rollout restart deploy 
    kubectl -n expertflow scale deploy --replicas=1 -l app.kubernetes.io/instance=cx-transflux
    kubectl -n expertflow scale deploy --replicas=1 -l app.kubernetes.io/instance=cx-agent-desk
    kubectl -n expertflow scale deploy --replicas=1 -l app.kubernetes.io/instance=cx-channels
[/code]

Enable the Reporting scheduler cron
[code] 
    kubectl -n expertflow patch cronjobs cx-reporting-cron -p '{"spec" : {"suspend" : false }}'
[/code]

Start Surveys and Campaigns deployment objects
[code] 
    kubectl -n expertflow scale deploy -l app.kubernetes.io/instance=cx-campaigns  --replicas=1
    kubectl -n expertflow scale deploy -l app.kubernetes.io/instance=cx-surveys  --replicas=1
[/code]
