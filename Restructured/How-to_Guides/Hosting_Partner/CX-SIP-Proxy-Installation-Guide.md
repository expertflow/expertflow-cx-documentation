---
title: "CX SIP Proxy Installation Guide"
summary: "Step-by-step installation guide for the ExpertFlow CX SIP Proxy — covering OpenSIPS 3.4 installation on Debian 12, MariaDB database setup, and the OpenSIPS Control Panel (opensips-cp 9.3.4) with Apache2 and PHP 7.4."
audience: [hosting-partner]
product-area: [voice, platform]
doc-type: how-to
difficulty: intermediate
keywords: ["OpenSIPS 3.4 install CX", "CX SIP proxy install", "opensips-cp install", "SIP proxy Debian 12 CX", "MariaDB OpenSIPS CX"]
aliases: ["install OpenSIPS CX", "SIP proxy setup CX", "opensips-cp 9.3.4 CX"]
last-updated: 2026-03-10
---

# CX SIP Proxy Installation Guide

This guide installs OpenSIPS 3.4, MariaDB, and the OpenSIPS Control Panel on a Debian 12 server. Run these steps on **every node** in your deployment (both nodes in an HA setup).

## Prerequisites

- Debian 12 (Bookworm) server
- Root or sudo access
- Ports 5060 (TCP/UDP) and 5555 (BIN) open in the firewall

---

## Step 1: Install OpenSIPS 3.4

Add the OpenSIPS 3.4 apt repository and install OpenSIPS with all modules:

```bash
sudo apt-get install -y curl gnupg2 wget

# Add OpenSIPS repository
echo "deb https://apt.opensips.org bookworm 3.4-releases" | sudo tee /etc/apt/sources.list.d/opensips.list
curl -s https://apt.opensips.org/opensips-org.gpg | sudo tee /usr/share/keyrings/opensips-org.gpg > /dev/null

sudo apt-get update
sudo apt-get install -y opensips opensips-cli opensips-*
```

Enable and start the OpenSIPS service:

```bash
sudo systemctl enable opensips
sudo systemctl start opensips
```

---

## Step 2: Install MariaDB

OpenSIPS uses MariaDB to store dialplan rules, dispatcher sets, and load balancer groups.

```bash
sudo apt-get install -y mariadb-server
sudo systemctl enable mariadb
sudo systemctl start mariadb
sudo mysql_secure_installation
```

Create the OpenSIPS database:

```bash
opensips-cli -x database create opensips
```

This command creates the `opensips` database schema using the credentials configured in `/etc/opensips/opensips-cli.cfg`.

---

## Step 3: Install PHP 7.4

The OpenSIPS Control Panel requires PHP 7.4. Add the Sury PHP repository:

```bash
sudo apt-get install -y apt-transport-https lsb-release ca-certificates
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list

sudo apt-get update
sudo apt-get install -y php7.4 php7.4-mysql php7.4-xml php7.4-ssh2 libapache2-mod-php7.4
```

---

## Step 4: Install Apache2

```bash
sudo apt-get install -y apache2
sudo systemctl enable apache2
sudo systemctl start apache2
```

---

## Step 5: Install OpenSIPS Control Panel

Download and install opensips-cp version 9.3.4:

```bash
cd /var/www/html
sudo wget https://github.com/OpenSIPS/opensips-cp/archive/refs/tags/9.3.4.tar.gz
sudo tar -xzf 9.3.4.tar.gz
sudo mv opensips-cp-9.3.4 opensips-cp
```

Configure the database connection in the control panel:

```bash
sudo cp /var/www/html/opensips-cp/config/db.inc.php.sample /var/www/html/opensips-cp/config/db.inc.php
sudo nano /var/www/html/opensips-cp/config/db.inc.php
```

Update the database credentials to match your MariaDB setup.

---

## Step 6: Configure Apache VirtualHost

Create a VirtualHost for the control panel:

```bash
sudo nano /etc/apache2/sites-available/opensips-cp.conf
```

Add the following configuration:

```apacheconf
<VirtualHost *:80>
    ServerAdmin admin@localhost
    DocumentRoot /var/www/html/opensips-cp
    ServerName opensips-cp.local

    <Directory /var/www/html/opensips-cp>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/opensips-cp-error.log
    CustomLog ${APACHE_LOG_DIR}/opensips-cp-access.log combined
</VirtualHost>
```

Enable the site and restart Apache:

```bash
sudo a2ensite opensips-cp.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

The OpenSIPS Control Panel is now accessible at `http://<server-ip>/`.

---

## Next Steps

- [Configuring the Dispatcher in CX SIP Proxy](Configuring-Dispatcher-in-CX-SIP-Proxy.md)
- [Configuring the Load Balancer in CX SIP Proxy](Configuring-Load-Balancer-in-CX-SIP-Proxy.md)
- [HA in EF SIP Proxy](HA-in-EF-SIP-Proxy.md)

---

## Related Articles

- [CX SIP Proxy Deployment Guide](CX-SIP-Proxy-Deployment-Guide.md)
- [Load Balancing via Dispatcher Module](Load-Balancing-Dispatcher-Module.md)
