---
title: "Load Balancing via the Dispatcher Module"
summary: "How-to guide for configuring load balancing in opensips.cfg using the OpenSIPS Dispatcher module — covering module loading, route implementation with ds_select_dst, failure route with ds_mark_dst and ds_next_dst, control panel destination setup, and the SQL fix for opensips-cp 9.3.4."
audience: [hosting-partner]
product-area: [voice, platform]
doc-type: how-to
difficulty: advanced
keywords: ["OpenSIPS dispatcher module CX", "ds_select_dst CX", "opensips.cfg load balancing CX", "dispatcher failure route CX", "SIP proxy LB opensips.cfg CX"]
aliases: ["dispatcher module LB CX", "opensips.cfg dispatcher CX", "SIP load balancing config CX"]
last-updated: 2026-03-10
---

# Load Balancing via the Dispatcher Module

This guide configures load balancing in `opensips.cfg` using the OpenSIPS **Dispatcher** module. The Dispatcher module selects SIP destinations from pre-configured sets and handles failover using failure routes.

> This guide covers the `opensips.cfg` implementation. To configure destinations via the control panel UI, see [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md).

---

## Step 1: Load the Required Modules

Edit `/etc/opensips/opensips.cfg` and add the following module declarations:

```cfg
loadmodule "db_mysql.so"
loadmodule "dispatcher.so"
```

Configure the dispatcher module parameters:

```cfg
modparam("dispatcher", "db_url", "mysql://opensips:opensips@localhost/opensips")
modparam("dispatcher", "ds_ping_interval", 10)
modparam("dispatcher", "ds_probing_mode", 1)
modparam("dispatcher", "ds_ping_reply_codes", "class=2;class=3;class=4")
```

| Parameter | Value | Description |
|---|---|---|
| `db_url` | MariaDB connection string | Database containing dispatcher sets |
| `ds_ping_interval` | `10` | Seconds between SIP OPTIONS health probes |
| `ds_probing_mode` | `1` | Probe only inactive destinations |
| `ds_ping_reply_codes` | `class=2;class=3;class=4` | Response codes that indicate a healthy destination |

---

## Step 2: Implement the Dialplan Route

Add a route block that uses `dp_translate` to look up the dialplan and then `ds_select_dst` to select a destination:

```cfg
route[to_media_vbb] {
    if (!dp_translate("1", "$rU/$rU")) {
        xlog("L_ERR", "Dialplan translation failed for $rU\n");
        send_reply("404", "Not Found");
        exit;
    }

    if (!ds_select_dst(1, 2, "f")) {
        xlog("L_ERR", "No dispatcher destinations available in set 1\n");
        send_reply("503", "Service Unavailable");
        exit;
    }

    t_on_failure("ds_failure");
    route(relay);
}
```

### ds_select_dst Parameters

```
ds_select_dst(<set_id>, <algorithm>, <flags>)
```

| Parameter | Value | Description |
|---|---|---|
| `set_id` | `1` | Dispatcher set to select from (1=CVP, 2=Cube, etc.) |
| `algorithm` | `2` | Round-robin selection |
| `flags` | `"f"` | Use the full destination URI |

**Algorithm values:**
- `0` — Hash over the Call-ID
- `1` — Hash over the From URI
- `2` — Round-robin
- `4` — Hash over the To URI
- `6` — Random

---

## Step 3: Add a Failure Route

The failure route handles cases where the selected destination is unreachable. It marks the failed destination and retries with the next available one:

```cfg
failure_route[ds_failure] {
    if (t_is_canceled()) {
        exit;
    }

    # Mark the failed destination as problematic
    ds_mark_dst("p");

    # Try the next destination in the set
    if (ds_next_dst()) {
        t_on_failure("ds_failure");
        route(relay);
    } else {
        xlog("L_ERR", "All dispatcher destinations failed for $rU\n");
        send_reply("503", "Service Unavailable");
        exit;
    }
}
```

| Function | Description |
|---|---|
| `ds_mark_dst("p")` | Marks the current destination as probing-required (temporarily removes from active rotation) |
| `ds_next_dst()` | Selects the next available destination in the set; returns `false` if none remain |

---

## Step 4: Add Destinations via Control Panel

Add destination entries to the dispatcher set using the OpenSIPS Control Panel:

1. Navigate to **System → Dispatcher**.
2. Click **Add Destination**.
3. Set the **Set ID** to match the set referenced in your `ds_select_dst` call.
4. Enter the **SIP URI** (`sip:<ip>:<port>`), **Socket**, **State**, and **Weight**.
5. Save.

After adding destinations, reload the dispatcher in OpenSIPS:

```bash
opensips-cli -x mi ds_reload
```

---

## Step 5: Fix the opensips-cp 9.3.4 SQL Insert Bug

The opensips-cp 9.3.4 control panel has a bug in the dispatcher destination INSERT query — it uses the wrong number of parameters, causing destination saves to fail silently.

To fix it, edit the dispatcher database helper:

```bash
sudo nano /var/www/html/opensips-cp/modules/system/dispatcher/dispatcher_db.php
```

Find the INSERT query line and ensure it has exactly **8 question marks** to match the 8 columns in the `dispatcher` table:

```php
// Correct version — 8 parameters
$query = "INSERT INTO dispatcher (setid, destination, socket, state, weight, attrs, description, flags)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
```

If the query has fewer or more `?` placeholders, correct them to match the 8-column schema. Save the file and reload the control panel page.

---

## Reloading After Changes

Any time you add, modify, or remove dispatcher destinations via the control panel or database, reload the dispatcher without restarting OpenSIPS:

```bash
opensips-cli -x mi ds_reload
```

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md)
- [Configuring the Load Balancer in CX SIP Proxy](Configuring-Load-Balancer-in-CX-SIP-Proxy.md)
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)
