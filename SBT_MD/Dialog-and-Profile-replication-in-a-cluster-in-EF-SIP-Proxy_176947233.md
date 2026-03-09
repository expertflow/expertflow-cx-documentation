# CX Knowledgebase : Dialog and Profile replication in a cluster in EF SIP Proxy

In a clustered environment within EF SIP proxy, dialog and profile replication play critical roles in ensuring seamless communication and maintaining consistency across nodes. Dialog replication refers to the process of synchronizing ongoing dialogs between nodes, ensuring that all nodes within the cluster have real-time access to the same dialog state. Profile replication involves replicating call profiles across nodes. Profiles replication allows to know the number of all calls within the cluster. Also, we can limit the number of concurrent calls for one profile.

### Requirements

To share the dialogs and profiles with all nodes of the EF SIP Proxy cluster, we require a minimum of two EF SIP Proxy servers with clustering configured. Additionally, it is essential to ensure that the machines are running PHP 7.4. The control panel may experience issues if other PHP versions are used.

### Step 1: Configuring clustering

To configure clustering follow [this document.](HA-in-EF-SIP-Proxy_173670574.html)

### Step 2: Modifying opensips.cfg

  * Open `opensips.cfg` file in server 1 to change the dialog location module configuration, and add lines for dialog and profiles.
[code] #### Dialog Module
        loadmodule "dialog.so"
        modparam("dialog", "profiles_with_value", "caller ; domain") #to track dialog profiles based on the values of caller and domain
        modparam("dialog", "db_mode", 2) #enabling dialog state storage in the DB
        modparam("dialog", "dialog_replication_cluster", CLUSTER_ID) #enable dialog replication across the cluster with CLUSTER ID
        modparam("dialog", "db_url",
                "mysql://opensips:opensipsrw@localhost/opensips")
        modparam("dialog", "profile_replication_cluster", 1) # #enable profile replication across the cluster with CLUSTER ID
        modparam("dialog", "profiles_no_value", "CCcalls/b") # specify profile for dialogs with no profile value
[/code]

  * Replace` CLUSTER_ID ` with the real ID of the cluster set in Step 1

  * Add the following lines `in if(is_method("INVITE")) {}` condition of `route{}`
[code] if(is_method("INVITE")) {
                        create_dialog("B");  # Create a new dialog of type "B"
                        $DLG_timeout=7200;  # Set the dialog timeout to 7200 seconds
                        set_dlg_profile("CCcalls/b");  # Set the dialog profile to "CCcalls/b"
                        set_dlg_sharing_tag("vip");  # Set a sharing tag for the dialog
                        set_dlg_profile("caller","$fU@$fd");  # Set the dialog profile for the "caller" attribute 
                        set_dlg_profile("domain","$fd");  # Set the dialog profile for the "domain" attribute
                        get_profile_size("caller","$fU@$fd",$var(ccaller));  # Get the size of the "caller" profile
                        get_profile_size("domain","$fd",$var(cdomain));  # Get the size of the "domain" profile
                        xlog("L_INFO", "Number of calls from user $fU@$fd is $var(ccaller)\n");  # Log the number of calls for user
                        xlog("L_INFO", "Number of calls from domain $fd is $var(cdomain)\n");  # Log the number of calls for domain
                }
[/code]

  * Save this file and restart opensips.
[code] sudo systemctl restart opensips.service
[/code]

  * Repeat the same process for the other node server.




### Testing

  * Make some calls from any of the node and run the following commands to 

  * List all the ongoing dialogs in the cluster
[code] opensips-cli -x mi dlg_list
[/code]

  * List all the dialogs of `CCcalls/b` profile
[code] opensips-cli -x mi profile_list_dlgs CCcalls/b
[/code]

  * List the contexts of all dialogs
[code] opensips-cli -x mi dlg_list_ctx
[/code]

  * Get the number of ongoing calls of `CCcalls/b` profile
[code] opensips-cli -x mi profile_get_size CCcalls/b
[/code]



