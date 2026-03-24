---
title: "HA in EF SIP Proxy"
summary: "Step-by-step guide for configuring High Availability in the ExpertFlow SIP Proxy — covering OpenSIPS clustering configuration, Keepalived/VRRP virtual IP setup, the PHP authentication fix for control panel SSH, and the keepalived reboot workaround."
audience: [hosting-partner, platform-operator]
product-area: [voice, platform]
doc-type: how-to
difficulty: advanced
keywords: ["EF SIP proxy HA CX", "OpenSIPS HA CX", "keepalived OpenSIPS CX", "VRRP SIP proxy CX", "OpenSIPS clustering CX", "SIP proxy failover CX"]
aliases: ["SIP proxy high availability CX", "OpenSIPS keepalived CX", "HA SIP proxy setup CX"]
last-updated: 2026-03-10
---

# HA in EF SIP Proxy

This guide configures High Availability (HA) for the ExpertFlow SIP Proxy using **OpenSIPS clustering** (for state synchronization) and **Keepalived/VRRP** (for virtual IP failover). Perform all steps on both the primary and backup nodes unless noted otherwise.

## Prerequisites

- Two nodes with OpenSIPS 3.4 installed and configured. See [CX SIP Proxy Installation Guide](CX-SIP-Proxy-Installation-Guide.md).
- Port **5555** (BIN protocol) open between both nodes.
- A virtual IP address reserved for the cluster (not assigned to either node's NIC).

---

## Step 1: Enable OpenSIPS Clustering in opensips.cfg

Edit `/etc/opensips/opensips.cfg` on both nodes.

### Load the required modules

Add these module lines:

```cfg
loadmodule "proto_bin.so"
loadmodule "clusterer.so"
loadmodule "usrloc.so"
```

### Configure proto_bin (inter-node transport)

```cfg
modparam("proto_bin", "bin_port", 5555)
```

### Configure the clusterer module

```cfg
modparam("clusterer", "db_url", "mysql://opensips:opensips@localhost/opensips")
modparam("clusterer", "my_node_id", <NODE_ID>)
```

Replace `<NODE_ID>` with `1` on the primary node and `2` on the backup node.

### Configure usrloc with cluster sharing

```cfg
modparam("usrloc", "db_mode", 2)
modparam("usrloc", "replication_mode", 2)
modparam("usrloc", "full-sharing-cluster", 1)
```

Restart OpenSIPS after editing:

```bash
sudo systemctl restart opensips
```

---

## Step 2: Add Cluster Nodes via Control Panel

On the **primary node** only:

1. Log in to the OpenSIPS Control Panel.
2. Navigate to **System → Clusterer**.
3. Add the primary node:
   - **Cluster ID**: `1`
   - **Node ID**: `1`
   - **BIN URL**: `bin:<primary-node-ip>:5555`
   - **Seed**: `Yes` (primary node is the cluster seed)
4. Add the backup node:
   - **Cluster ID**: `1`
   - **Node ID**: `2`
   - **BIN URL**: `bin:<backup-node-ip>:5555`
   - **Seed**: `No`

---

## Step 3: Configure Keepalived for Virtual IP

Install Keepalived on both nodes:

```bash
sudo apt-get install -y keepalived
```

Create `/etc/keepalived/keepalived.conf` on each node:

**Primary node:**

```
vrrp_instance VI_1 {
    state MASTER
    interface eth0
    virtual_router_id 51
    priority 100
    advert_int 1
    unicast_src_ip <primary-node-ip>
    unicast_peer {
        <backup-node-ip>
    }
    virtual_ipaddress {
        <virtual-ip>/24
    }
}
```

**Backup node:**

```
vrrp_instance VI_1 {
    state BACKUP
    interface eth0
    virtual_router_id 51
    priority 90
    advert_int 1
    unicast_src_ip <backup-node-ip>
    unicast_peer {
        <primary-node-ip>
    }
    virtual_ipaddress {
        <virtual-ip>/24
    }
}
```

Replace `<primary-node-ip>`, `<backup-node-ip>`, and `<virtual-ip>` with your actual addresses. Adjust `interface` to match your network interface name.

> **Important**: Do **not** run `sudo systemctl enable keepalived`. See the reboot workaround in Step 6.

---

## Step 4: Fix PHP SSH Authentication in Control Panel

The opensips-cp 9.3.4 control panel uses a PHP function (`ssh2_auth_pubkey_file`) for SSH authentication that is incompatible with some environments. Replace it with password-based authentication.

Edit the control panel functions file:

```bash
sudo nano /var/www/html/opensips-cp/lib/opensips/functions.inc.php
```

Find the line containing `ssh2_auth_pubkey_file` and replace it with:

```php
ssh2_auth_password($connection, $username, $password);
```

Save the file. No service restart is required.

---

## Step 5: Add Virtual IP Sockets to opensips.cfg

OpenSIPS must listen on the virtual IP so it can accept SIP traffic when the virtual IP is active on this node. Add the virtual IP as a listen socket in `opensips.cfg` on **both nodes**:

```cfg
listen=udp:<virtual-ip>:5060
listen=tcp:<virtual-ip>:5060
```

Restart OpenSIPS after editing:

```bash
sudo systemctl restart opensips
```

---

## Step 6: Configure the Keepalived Module and Reboot Workaround

### Add the keepalived module configuration

In the OpenSIPS Control Panel, navigate to **System → Keepalived** and add a keepalived module entry with your virtual IP and interface details.

The JSON configuration format:

```json
{
  "virtual_ip": "<virtual-ip>",
  "interface": "eth0",
  "node_role": "MASTER"
}
```

Set `"node_role"` to `"MASTER"` on the primary and `"BACKUP"` on the secondary.

### Reboot workaround for keepalived

Running `systemctl enable keepalived` can cause OpenSIPS and Keepalived to start in the wrong order on reboot, resulting in Keepalived failing to acquire the virtual IP. Instead, use a crontab entry:

```bash
sudo crontab -e
```

Add:

```
@reboot sleep 5 && sudo systemctl restart opensips.service
```

Then start Keepalived manually (do not enable it):

```bash
sudo systemctl start keepalived
```

This ensures OpenSIPS is fully up before Keepalived begins its VRRP election.

---

## Verifying HA

After completing setup on both nodes:

1. Confirm the virtual IP is active on the primary: `ip addr show eth0`
2. Confirm OpenSIPS is listening on the virtual IP: `ss -tulnp | grep 5060`
3. Stop OpenSIPS on the primary and verify the virtual IP moves to the backup within a few seconds.
4. Restart the primary and confirm it reclaims the virtual IP.

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [CX SIP Proxy Installation Guide](CX-SIP-Proxy-Installation-Guide.md)
- [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md)

