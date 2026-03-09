# CX Knowledgebase : RKE2 uninstallation

## Purpose

The purpose of this document is to uninstall the Kubernetes distribution RKE.

### Step 1: uninstall the RKE2 and clean up files used by RKE2

you can run following command on control plane and worker node.
[code] 
    cd /usr/bin/
[/code]

Run the following command:
[code] 
    rke2-uninstall.sh
[/code]

### Step 2: Generic step for **both Control-Plane and Worker Nodes.**

Clean up the existing installation + volume data ( DATA deletion warning ).
[code] 
    rm -rf /var/lib/rancher  /etc/rancher /var/lib/longhorn/ /etc/cni /opt/cni  /var/openebs/;
[/code]

### Step 3: Reboot the system
[code] 
    reboot
[/code]

  


  

