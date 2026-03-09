# CX Knowledgebase : ETCD Backup and Restore

This document demonstrates the restoration of the cluster from ETCD backup.  
  
/var/lib/rancher/rke2 is the default data directory for rke2.

## Snapshots

Snapshots are enabled by default.

The snapshot directory defaults to `/var/lib/rancher/rke2/server/db/snapshots`.

## Single-node 

  1. You must stop RKE2 service if it is enabled via systemd. 



[code] 
    systemctl stop rke2-server
[/code]

  2. Select the snapshot.



[code] 
    ls /var/lib/rancher/rke2/server/db/snapshots/
[/code]

3\. Next, you will initiate the restore from snapshot.
[code] 
    rke2 server --cluster-reset --cluster-reset-restore-path=/var/lib/rancher/rke2/server/db/snapshots/<SNAPSHOT>
[/code]

  4. Once the restore process is complete, start the rke2-server service.



[code] 
    systemctl start rke2-server
[/code]

## Multi-node cluster

## Restoring a Snapshot to Existing Nodes[​](https://docs.rke2.io/backup_restore#restoring-a-snapshot-to-existing-nodes)

When RKE2 is restored from backup, it moves the old data directory to “/var/lib/rancher/rke2/server/db/etcd-old-%date%/ ” and sets up a new single-member etcd cluster.

  1. You must stop RKE2 service on all server nodes if it is enabled via systemd. 



[code] 
    systemctl stop rke2-server
[/code]

  2. Select the snapshot.



[code] 
    ls /var/lib/rancher/rke2/server/db/snapshots/
[/code]

  3. Next, you will initiate the restore from the snapshot on the first server node with the following commands:



[code] 
    rke2 server --cluster-reset --cluster-reset-restore-path=/var/lib/rancher/rke2/server/db/snapshots/<SNAPSHOT>
[/code]

  3. Once the restore process is complete, start the rke2-server service on the first server node as follows:



[code] 
    systemctl start rke2-server
[/code]

run the following commands on the other server node in the cluster

  1. Remove the rke2 db directory on the other server nodes as follows:



[code] 
    rm -rf /var/lib/rancher/rke2/server/db
[/code]

  2. Start the rke2-server service on other server nodes with the following command:



[code] 
    systemctl start rke2-server
[/code]

When rke2 resets the cluster, it creates an empty file at `/var/lib/rancher/rke2/server/db/reset-flag`. This file is harmless to leave in place, but must be removed in order to perform subsequent resets or restores. This file is deleted when rke2 starts normally.
[code] 
    rm -rf /var/lib/rancher/rke2/server/db/reset-flag
[/code]

## Restoring a Snapshot to New Nodes

For rke2 v.1.20.9 and earlier, back up and restore certificates first due to a known issue with bootstrap data not saving on restore. See the note below for additional version-specific restore details.

  1. Back up the following: `/var/lib/rancher/rke2/server/cred`, `/var/lib/rancher/rke2/server/tls`, `/var/lib/rancher/rke2/server/token`, `/etc/rancher` , `/var/openebs`.

  2. Restore the certs in Step 1 above to the first new server node.

  3. Install rke2 on the first new server node by running the following command:



[code] 
    curl -sfL https://get.rke2.io |INSTALL_RKE2_TYPE=server  sh - 
[/code]

  4. Stop RKE2 service on all server nodes if it is enabled and initiate the restore from the snapshot on the first server node with the following commands:



[code] 
    systemctl stop rke2-server
    rke2 server \
      --cluster-reset \
      --cluster-reset-restore-path=<PATH-TO-SNAPSHOT>
[/code]

  5. Once the restore process is complete, start the rke2-server service on the first server node as follows:



[code] 
    systemctl start rke2-server
[/code]
