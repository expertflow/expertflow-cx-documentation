# CX Knowledgebase : Connecting to Databases with TLS Enabled

This document provides instructions for connecting to MongoDB, Redis, and PostgreSQL when TLS is enabled.

### Redis

Export all cert files using the following commands:-
[code] 
    mkdir /tmp/redis_certs/
    CERTFILES=($(kubectl get secret redis-crt -n ef-external -o go-template='{{range $k,$v := .data}}{{$k}}{{"\n"}}{{end}}'))
    for f in ${CERTFILES[*]}; do   kubectl get secret redis-crt  -n ef-external -o go-template='{{range $k,$v := .data}}{{ if eq $k "'$f'"}}{{$v  | base64decode}}{{end}}{{end}}' > /tmp/redis_certs/${f} 2>/dev/null; done
[/code]

Export Redis Password:-
[code] 
    export REDIS_PASSWORD=$(kubectl get secret --namespace ef-external redis -o jsonpath="{.data.redis-password}" | base64 -d)
[/code]

Start a Redis client pod:-
[code] 
    kubectl run --namespace ef-external redis-client   --env REDIS_PASSWORD=$REDIS_PASSWORD  --image gitimages.expertflow.com/general/redis:CIM-4292-6.2-debian-10-k8s --command -- sleep infinity
[/code]

Now you can mount the secret `redis-crt` inside the client pods and use TLS certificates.
[code] 
    kubectl cp --namespace ef-external /tmp/redis_certs/tls.crt redis-client:/tmp/tls.crt
    kubectl cp --namespace ef-external /tmp/redis_certs/tls.key redis-client:/tmp/tls.key
    kubectl cp --namespace ef-external /tmp/redis_certs/ca.crt redis-client:/tmp/ca.crt
[/code]

Exec into client pod:-
[code] 
    kubectl exec --tty -i redis-client \
       --namespace ef-external -- bash
[/code]

verify the connection using the following command in the client pod:-
[code] 
    I have no name!@redis-client:/$ REDISCLI_AUTH="$REDIS_PASSWORD" redis-cli -h redis-master --tls --cert /tmp/tls.crt --key /tmp/tls.key --cacert /tmp/ca.crt
    redis-master:6379>
    redis-master:6379> CONFIG GET databases
    1) "databases"
    2) "16"
[/code]

###  MongoDB

  1. export all the cert files in `ef-external` namespace using



[code] 
    mkdir /tmp/mongodb_certs
    CERTFILES=($(kubectl get secret mongo-mongodb-ca -n ef-external -o go-template='{{range $k,$v := .data}}{{$k}}{{"\n"}}{{end}}'))
    for f in ${CERTFILES[*]}; do   kubectl get secret mongo-mongodb-ca  -n ef-external -o go-template='{{range $k,$v := .data}}{{ if eq $k "'$f'"}}{{$v  | base64decode}}{{end}}{{end}}' > /tmp/mongodb_certs/${f} 2>/dev/null; done
[/code]

The above script will export all the certs to local directory `/tmp/mongodb_certs`.

  2. Run the following command to export MongoDB Password:-



[code] 
    kubectl get secret --namespace ef-external mongo-mongodb -o jsonpath="{.data.mongodb-root-password}" | base64 -d
[/code]

  3. Run the mongoDB client pod



[code] 
    kubectl run --namespace ef-external mongo-mongodb-client --env="MONGODB_ROOT_PASSWORD=$MONGODB_ROOT_PASSWORD" --image docker.io/bitnami/mongodb:6.0.2-debian-11-r1 
[/code]

  4. copy the certificate files inside the client pod



[code] 
    kubectl -n ef-external cp /tmp/mongodb_certs mongo-mongodb-client:/tmp/
[/code]

  5. Connect to the mongoDB pod using SSL/TLS certs
[code] kubectl -n ef-external exec -it mongo-mongodb-client  -- bash
[/code]

     6. once inside the mongodb-client pod, combine both cert and key file using
[code] cat /tmp/mongodb_certs/mongodb-ca-cert /tmp/mongodb_certs/mongodb-ca-key > /tmp/mongodb_certs/combined.pem
[/code]

     7. verify the connection using tls
[code] mongosh admin --host "mongo-mongodb" \
    --authenticationDatabase admin \
    -u root \
    -p $MONGODB_ROOT_PASSWORD \
    --tls  \
    --tlsAllowInvalidHostnames  \
    --tlsAllowInvalidCertificates \
    --tlsCertificateKeyFile /tmp/mongodb_certs/client-pem  \
    --tlsCAFile /tmp/mongodb_certs/client-pem
[/code]




![](images/icons/grey_arrow_down.png)Sample Run
[code] 
    I have no name!@mongo-mongodb-client:/$ mongosh admin --host "mongo-mongodb" --authenticationDatabase admin -u root -p $MONGODB_ROOT_PASSWORD --tls  --tlsAllowInvalidHostnames  --tlsAllowInvalidCertificates --tlsCertificateKeyFile /tmp/client-pem  --tlsCAFile /tmp/mongo/client-pem
    Current Mongosh Log ID: 663b303a12c4a32b93ff8546
    Connecting to:          mongodb://<credentials>@mongo-mongodb:27017/admin?directConnection=true&authSource=admin&tls=true&tlsAllowInvalidHostnames=true&tlsAllowInvalidCertificates=true&tlsCertificateKeyFile=%2Ftmp%2Fmongo%2Fcombined.pem&tlsCAFile=%2Ftmp%2Fmongo%2Fclient-pem&appName=mongosh+1.6.0
    Using MongoDB:          6.0.2
    Using Mongosh:          1.6.0
    For mongosh info see: https://docs.mongodb.com/mongodb-shell/
    ------
       The server generated these startup warnings when booting
       2024-05-08T07:42:12.444+00:00: /sys/kernel/mm/transparent_hugepage/enabled is 'always'. We suggest setting it to 'never'
       2024-05-08T07:42:12.445+00:00: /sys/kernel/mm/transparent_hugepage/defrag is 'always'. We suggest setting it to 'never'
       2024-05-08T07:42:12.445+00:00: vm.max_map_count is too low
    ------
    admin> show dbs;
    admin   100.00 KiB
    config   12.00 KiB
    local    72.00 KiB
    admin>
[/code]

Sometimes, the mongodb client pod doesn’t inherit the `MONGODB_ROOT_PASSWORD` environment variable, and user will have to enter the password manually.

### PostgreSQL

  1. Export all cert files using the following commands:-



[code] 
    mkdir /tmp/postgresql_certs/
    CERTFILES=($(kubectl get secret ef-postgresql-crt -n ef-external -o go-template='{{range $k,$v := .data}}{{$k}}{{"\n"}}{{end}}'))
    for f in ${CERTFILES[*]}; do   kubectl get secret ef-postgresql-crt  -n ef-external -o go-template='{{range $k,$v := .data}}{{ if eq $k "'$f'"}}{{$v  | base64decode}}{{end}}' > /tmp/postgresql_certs/${f} 2>/dev/null; done
[/code]

Export Postgres Password:-
[code] 
    export POSTGRES_PASSWORD=$(kubectl get secret --namespace ef-external ef-postgresql -o jsonpath="{.data.password}" | base64 -d)
[/code]

Start a Postgresql client pod by running this command:-
[code] 
    kubectl run ef-postgresql-client --rm --tty -i --restart='Never' --namespace ef-external --image docker.io/bitnami/postgresql:14.5.0-debian-11-r21 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
          --command -- psql --host ef-postgresql -U sa -d licenseManager -p 5432
[/code]
