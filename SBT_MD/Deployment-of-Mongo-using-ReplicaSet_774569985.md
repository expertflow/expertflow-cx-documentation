# CX Knowledgebase : Deployment of Mongo using ReplicaSet

Deployments where MongoDB is used in ReplicaSet mode is usually needed for 

  * high availability and redundancy 

  * isolating the read and write pipes for heavier workloads

  * backups are less disturbing for the whole solution when using replica-set setup, as all the read queries are being taken from the secondary node, while the primary node is spared to serve client requests.




#### Considerations

To deploy MongoDB in HA mode for Expertflow CX , please consider below given points.

  * MongoDB in HA should be deployed when using multi-node cluster, with replica members spread across different nodes. If one of the node goes down, the other node will take over and solution will survive

  * Current implement of the Expertflow MongoDB HA can be run on a single node ( not recommended ) 

  * MongoDB requires hardware specs given below 




**Entity**| **Spec**  
---|---  
Number of replicas| 2 ( 1 primary and 1 secondary )   
RAM| 4 GB per replica  
CPU Cores| 1 CPU Core per replica  
  
Default replicaset name is “expertflow” when using MongoDB HA

#### Deployment

Deploy the MongoDB in HA using replica-set, follow these steps

clone the values file for the MongoDB helm chart
[code] 
    helm show values expertflow/mongodb-ha > helm-values/mongo-db-ha-custom-values.yaml
[/code]

Edit/update values required in `helm-values/mongo-db-ha-custom-values.yaml` for-example, the default password under the auth section
[code] 
    auth:
      rootPassword: "Expertflow123"
[/code]

Deploy MongoDB by running the following command.
[code] 
    helm upgrade --install=true --namespace=ef-external --values=helm-values/mongo-db-ha-custom-values.yaml mongo expertflow/mongodb
[/code]

Check the MongoDB deployment status by running the following command:
[code] 
    kubectl -n ef-external rollout status sts mongo-mongodb
[/code]

sample output 
[code] 
    # kubectl -n ef-external get pods
    NAME                   READY   STATUS    RESTARTS   AGE
    mongo-mongodb-0        1/1     Running   0          8m10s
    mongo-mongodb-1        1/1     Running   0          6m42s
    mongo-mongodb-client   1/1     Running   0          5s
    
[/code]
