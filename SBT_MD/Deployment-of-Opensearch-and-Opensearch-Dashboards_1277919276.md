# CX Knowledgebase : Deployment of Opensearch and Opensearch Dashboards

This guide is intended for operations and web administration teams. It provides a structured, step-by-step procedure for deploying OpenSearch and OpenSearch Dashboards to ensure reliable and scalable log retention.  
  
##   
Step 1: Deploy the Opensearch and Opensearch Dashboards

Create a shell script to deploy OpenSearch and OpenSearch Dashboards using the following command:-
[code] 
    vi deploy_opensearch.sh
[/code]

Copy the following content and paste it into the shell script.
[code] 
    #!/bin/bash
    
    # ==============================================================================
    # Automated OpenSearch & Dashboards Deployment & Management Script
    #
    # Version: 2.2
    # Release Date: 2025-07-29
    #
    # This script automates the installation, configuration, and management of a
    # single-node OpenSearch cluster and Dashboards. It includes robust error
    # handling, idempotency checks, and lifecycle management features.
    #
    # ==============================================================================
    
    # --- Script Setup ---
    # Exit on any error, and on unset variables.
    set -euo pipefail
    
    # --- Global Variables ---
    LOG_FILE="/tmp/opensearch_deploy.log"
    INSTALL_NGINX_PROXY=false
    FQDN=$(hostname -f 2>/dev/null || echo "$(hostname)")
    OPENSEARCH_URL="https://localhost:9200"
    PASSWORD_FILE="/etc/opensearch/.admin_password"
    
    # --- Helper & Execution Functions ---
    
    # Clear log file at the start of the script
    rm -f "$LOG_FILE"
    
    # Centralized command execution function
    execute() {
        local cmd="$1"
        local msg="$2"
        local mode="${3:-quiet}"
        
        echo -n "=> $msg... "
        
        if [ "$mode" == "verbose" ]; then
            echo " (running...)"
            # Execute command with live output, appending to log file
            if sudo -E bash -c "$cmd" 2> >(tee -a "$LOG_FILE" >&2) | tee -a "$LOG_FILE"; then
                echo -n "=> $msg... "
                echo -e "\e[32mOK\e[0m"
            else
                echo -n "=> $msg... "
                echo -e "\e[31mFAILED\e[0m"
                echo "--------------------- ERROR LOG ----------------------" >&2
                echo "Error details were logged above and also saved to $LOG_FILE" >&2
                echo "------------------------------------------------------" >&2
                exit 1
            fi
        else
            # Execute command quietly, appending to log file
            if sudo -E bash -c "$cmd" >> "$LOG_FILE" 2>&1; then
                echo -e "\e[32mOK\e[0m"
            else
                echo -e "\e[31mFAILED\e[0m"
                echo "--------------------- ERROR LOG ----------------------" >&2
                cat "$LOG_FILE" >&2
                echo "------------------------------------------------------" >&2
                exit 1
            fi
        fi
    }
    
    # Function to execute curl commands against OpenSearch API
    execute_curl() {
        local method="$1"
        local endpoint="$2"
        local data="$3"
        local msg="$4"
    
        # Get admin password from file or prompt if it doesn't exist
        if [ -z "${OPENSEARCH_ADMIN_PASSWORD:-}" ]; then
            if [ -f "$PASSWORD_FILE" ]; then
                OPENSEARCH_ADMIN_PASSWORD=$(sudo cat "$PASSWORD_FILE")
            else
                read -sp "Enter OpenSearch 'admin' password: " OPENSEARCH_ADMIN_PASSWORD
                echo
            fi
        fi
    
        local cmd="curl -s -k -w '\n%{http_code}' -u 'admin:${OPENSEARCH_ADMIN_PASSWORD}' -X ${method} '${OPENSEARCH_URL}${endpoint}' -H 'Content-Type: application/json' -d '${data}'"
        
        echo -n "=> $msg... "
        
        # Execute command and capture output and http_code
        local response
        response=$(eval "$cmd")
        local http_code
        http_code=$(echo "$response" | tail -n1)
        local body
        body=$(echo "$response" | sed '$d')
    
        if [[ "$http_code" -ge 200 && "$http_code" -lt 300 ]]; then
            echo -e "\e[32mOK ($http_code)\e[0m"
            echo "$body" >> "$LOG_FILE"
        else
            echo -e "\e[31mFAILED ($http_code)\e[0m"
            echo "--------------------- ERROR LOG ----------------------" >&2
            echo "$body" >&2
            echo "------------------------------------------------------" >&2
            exit 1
        fi
    }
    
    
    log() {
        echo "--------------------------------------------------"
        echo "=> $1"
        echo "--------------------------------------------------"
    }
    
    usage() {
        echo "OpenSearch & Dashboards Deployment & Management Script (v2.2)"
        echo ""
        echo "Usage: $0 [COMMAND] [OPTIONS]"
        echo ""
        echo "Commands:"
        echo "  install [--with-nginx] [--password <pass>] Install OpenSearch and Dashboards."
        echo "  status                        Show details of the current installation."
        echo ""
        echo "  ism-create-interactive        Interactively create a simple ISM policy."
        echo "  ism-policy-apply              Create or update an ISM policy from a JSON file."
        echo "      --name <policy_name>      (Required) The name of the policy."
        echo "      --file <path_to.json>     (Required) Path to the policy JSON file."
        echo "  ism-policy-get                View a specific ISM policy."
        echo "      --name <policy_name>      (Required) The name of the policy to view."
        echo "  ism-policy-delete             Delete an ISM policy."
        echo "      --name <policy_name>      (Required) The name of the policy to delete."
        echo "  ism-policy-list               List all existing ISM policies."
        echo ""
        echo "  ism-attach                    Attach a policy to a specific index."
        echo "      --policy <policy_name>    (Required) The policy to attach."
        echo "      --index <index_name>      (Required) The index to attach to."
        echo "  ism-remove                    Remove a policy from an index."
        echo "      --index <index_name>      (Required) The index to remove from."
        echo ""
        echo "  --enable-nginx                Enable Nginx reverse proxy after installation."
        echo "  --disable-nginx               Disable Nginx reverse proxy."
        echo "  --uninstall                   Uninstall the entire OpenSearch stack."
        echo "  --help                        Display this help message."
        echo ""
    }
    
    # --- Core Logic Functions ---
    
    detect_os() {
        if [ -f /etc/os-release ]; then
            . /etc/os-release
            OS_ID=$ID
        else
            execute "false" "Cannot detect OS distribution."
        fi
    }
    
    #preflight_checks() {
    #    log "Running pre-flight checks"
    #    local missing_packages=()
    #    for pkg in curl gpg jq; do
    #        if ! command -v $pkg &> /dev/null; then
    #            missing_packages+=($pkg)
    #        fi
    #    done
    #    if [ ${#missing_packages[@]} -gt 0 ]; then
    #        echo "Error: Required packages are missing: ${missing_packages[*]}" >&2
    #        echo "Please install them and run the script again." >&2
    #        exit 1
    #    fi
    #    echo "=> All required packages are present."
    #}
    
    #fix_apt_sources() {
    #    log "Checking and optimizing APT sources"
    #    local sources_files
    #    # Get a list of all apt source files that contain a regional mirror URL
    #    sources_files=$(grep -lE "[a-z]{2}\.archive\.ubuntu\.com" /etc/apt/sources.list /etc/apt/sources.list.d/*.list 2>/dev/null || true)
    
    #    if [ -n "$sources_files" ]; then
    #        echo "Regional mirror detected. Switching to the main global repository."
    #        for file in $sources_files; do
    #            execute "cp ${file} ${file}.bak" "Backing up ${file}"
    #            execute "sed -i -E 's/([a-z]{2}\\.)?archive\\.ubuntu\\.com/archive.ubuntu.com/g' ${file}" "Updating ${file}"
    #        done
    #        echo "Switched to main Ubuntu repository to prevent regional mirror issues."
    #    else
    #        echo "=> APT sources appear to be using the main repository already. No changes needed."
    #    fi
    #}
    
    
    apply_prerequisites() {
        log "Applying universal system prerequisites"
        if ! grep -q "vm.max_map_count=262144" /etc/sysctl.conf; then
            execute "echo 'vm.max_map_count=262144' | tee -a /etc/sysctl.conf" "Setting vm.max_map_count"
            execute "sysctl -p" "Applying new sysctl config"
        else
            echo "=> Setting vm.max_map_count... SKIPPED (already set)"
        fi
        execute "swapoff -a" "Disabling swap"
        execute "sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab" "Making swap disable persistent"
    }
    
    configure_jvm_heap() {
        log "Configuring JVM heap size to 4GB"
        execute "mkdir -p /etc/opensearch/jvm.options.d" "Creating jvm.options.d directory"
        execute "echo -e '# Set the initial and maximum heap size to the same value\n-Xms4g\n-Xmx4g' | tee /etc/opensearch/jvm.options.d/heap.options" "Writing heap options file"
    }
    
    deploy_debian() {
        log "Starting deployment for Debian/Ubuntu"
        #fix_apt_sources
        #execute "apt-get update && apt-get upgrade -y" "Updating system packages" "verbose"
        #execute "apt-get install -y curl gnupg lsb-release ca-certificates apt-transport-https" "Installing dependencies"
        execute "curl -fsSL https://artifacts.opensearch.org/publickeys/opensearch.pgp | gpg --dearmor -o /etc/apt/trusted.gpg.d/opensearch.gpg" "Importing OpenSearch GPG key"
        execute "echo 'deb https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/apt stable main' | tee /etc/apt/sources.list.d/opensearch-2.x.list" "Adding OpenSearch repository"
        execute "echo 'deb https://artifacts.opensearch.org/releases/bundle/opensearch-dashboards/2.x/apt stable main' | tee -a /etc/apt/sources.list.d/opensearch-2.x.list" "Adding Dashboards repository"
        #execute "apt-get update" "Refreshing package lists"
        
        export OPENSEARCH_INITIAL_ADMIN_PASSWORD
        execute "apt-get install -y opensearch opensearch-dashboards" "Installing OpenSearch and Dashboards"
        
        if [ "$INSTALL_NGINX_PROXY" = true ]; then
            execute "apt-get install -y nginx" "Installing Nginx"
        fi
    }
    
    deploy_rhel() {
        log "Starting deployment for RHEL/CentOS/Rocky"
        execute "dnf update -y" "Updating system packages" "verbose"
        execute "dnf install -y curl gnupg" "Installing dependencies"
        execute "curl -SL https://artifacts.opensearch.org/releases/bundle/opensearch/2.x/opensearch-2.x.repo -o /etc/yum.repos.d/opensearch-2.x.repo" "Adding OpenSearch repository"
        execute "curl -SL https://artifacts.opensearch.org/releases/bundle/opensearch-dashboards/2.x/opensearch-dashboards-2.x.repo -o /etc/yum.repos.d/opensearch-dashboards-2.x.repo" "Adding Dashboards repository"
        execute "dnf clean all" "Cleaning DNF cache"
    
        export OPENSEARCH_INITIAL_ADMIN_PASSWORD
        execute "dnf install -y opensearch opensearch-dashboards" "Installing OpenSearch and Dashboards"
    
        if [ "$INSTALL_NGINX_PROXY" = true ]; then
            execute "dnf install -y nginx" "Installing Nginx"
        fi
    }
    
    configure_opensearch() {
        log "Configuring OpenSearch"
        cat <<EOF | sudo tee -a /etc/opensearch/opensearch.yml > /dev/null
    
    # --- Script Modifications ---
    network.host: 0.0.0.0
    discovery.type: single-node
    EOF
        echo "=> Appending network settings to opensearch.yml... OK"
    }
    
    configure_dashboards() {
        log "Configuring OpenSearch Dashboards"
        local dashboards_host="0.0.0.0"
        if [ "$INSTALL_NGINX_PROXY" = true ]; then
            dashboards_host="127.0.0.1"
        fi
        
        # Overwrite the config file with a minimal, correct version
        export CONFIG_CONTENT
        CONFIG_CONTENT=$(cat <<EOF
    # OpenSearch Dashboards configuration file, managed by script.
    
    server.host: "${dashboards_host}"
    opensearch.hosts: ["https://localhost:9200"]
    opensearch.ssl.verificationMode: none
    opensearch.username: "admin"
    opensearch.password: "${OPENSEARCH_INITIAL_ADMIN_PASSWORD}"
    opensearch_security.cookie.secure: false
    EOF
    )
        execute 'echo "$CONFIG_CONTENT" | tee /etc/opensearch-dashboards/opensearch_dashboards.yml' "Writing opensearch_dashboards.yml"
        unset CONFIG_CONTENT
    }
    
    configure_nginx_proxy() {
        log "Configuring Nginx as a reverse proxy for Dashboards"
        execute "mkdir -p /etc/nginx/ssl" "Creating Nginx SSL directory"
        execute "openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/opensearch_dashboards.key -out /etc/nginx/ssl/opensearch_dashboards.crt -subj '/C=US/ST=State/L=City/O=Organization/CN=${FQDN}'" "Generating self-signed SSL certificate"
        
        export NGINX_CONFIG
        NGINX_CONFIG=$(cat <<EOF
    server {
        listen 80;
        server_name ${FQDN};
        return 301 https://\$host\$request_uri;
    }
    server {
        listen 443 ssl http2;
        server_name ${FQDN};
        ssl_certificate /etc/nginx/ssl/opensearch_dashboards.crt;
        ssl_certificate_key /etc/nginx/ssl/opensearch_dashboards.key;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        location / {
            proxy_pass http://127.0.0.1:5601;
            proxy_set_header Host \$host;
            proxy_set_header X-Real-IP \$remote_addr;
            proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto \$scheme;
            proxy_http_version 1.1;
            proxy_set_header Connection "upgrade";
            proxy_set_header Upgrade \$http_upgrade;
            proxy_read_timeout 90s;
        }
    }
    EOF
    )
        execute 'echo "$NGINX_CONFIG" | tee /etc/nginx/conf.d/opensearch-dashboards.conf' "Writing Nginx config file"
        unset NGINX_CONFIG
        execute "nginx -t" "Testing Nginx configuration"
        execute "systemctl enable nginx" "Enabling Nginx service"
        execute "systemctl restart nginx" "Restarting Nginx service"
    }
    
    start_services() {
        log "Starting and enabling services"
        execute "systemctl daemon-reload" "Reloading systemd daemon"
        execute "systemctl enable opensearch" "Enabling OpenSearch service"
        execute "systemctl start opensearch" "Starting OpenSearch service"
    
        # Wait for OpenSearch to be ready
        echo -n "=> Waiting for OpenSearch to initialize..."
        local retries=30
        local count=0
        while ! curl -s -k -u "admin:${OPENSEARCH_INITIAL_ADMIN_PASSWORD}" "$OPENSEARCH_URL" > /dev/null; do
            if [ $count -ge $retries ]; then
                echo -e "\e[31m FAILED\e[0m"
                echo "OpenSearch did not start in time. Please check the logs." >&2
                exit 1
            fi
            echo -n "."
            sleep 2
            ((count++))
        done
        echo -e "\e[32m OK\e[0m"
    
        execute "systemctl enable opensearch-dashboards" "Enabling Dashboards service"
        execute "systemctl start opensearch-dashboards" "Starting Dashboards service"
    }
    
    # --- Main Functions for User Actions ---
    
    generate_password() {
        # Generate a 16-character password. Use openssl if available, fallback to urandom.
        if command -v openssl &> /dev/null; then
            openssl rand -base64 12
        else
            LC_ALL=C tr -dc 'A-Za-z0-9!#%&()*+,-./:;<=>?@[]^_{|}~' < /dev/urandom | head -c 16
        fi
    }
    
    run_installation() {
        log "Starting OpenSearch Installation"
        
        if command -v opensearch &> /dev/null; then
            echo "OpenSearch appears to be already installed. Please uninstall first or use other management commands." >&2
            exit 1
        fi
        
        # Handle password
        if [ -n "${USER_PASSWORD:-}" ]; then
            OPENSEARCH_INITIAL_ADMIN_PASSWORD=$USER_PASSWORD
            echo "=> Using user-provided password."
        else
            OPENSEARCH_INITIAL_ADMIN_PASSWORD=$(generate_password)
            echo "=> Generated a secure random password."
        fi
    
        detect_os
        #preflight_checks
        apply_prerequisites
    
        if [ "$OS_ID" = "ubuntu" ] || [ "$OS_ID" = "debian" ]; then
            deploy_debian
        elif [ "$OS_ID" = "rhel" ] || [ "$OS_ID" = "centos" ] || [ "$OS_ID" = "rocky" ]; then
            deploy_rhel
        else
            execute "false" "Unsupported OS: $OS_ID"
        fi
    
        configure_opensearch
        configure_jvm_heap
        configure_dashboards
    
        if [ "$INSTALL_NGINX_PROXY" = true ]; then
            configure_nginx_proxy
        fi
    
        start_services
    
        # Securely store the password
        execute "mkdir -p /etc/opensearch" "Creating /etc/opensearch directory"
        execute "echo \"$OPENSEARCH_INITIAL_ADMIN_PASSWORD\" | tee $PASSWORD_FILE" "Storing admin password"
        execute "chmod 600 $PASSWORD_FILE" "Securing password file"
    
        local primary_ip
        primary_ip=$(hostname -I | awk '{print $1}')
    
        log "Deployment Complete!"
        echo "=================================================="
        if [ -z "${USER_PASSWORD:-}" ]; then
            echo "OpenSearch Admin Password: ${OPENSEARCH_INITIAL_ADMIN_PASSWORD}"
        else
            echo "OpenSearch Admin Password: [USER PROVIDED]"
        fi
    
        if [ "$INSTALL_NGINX_PROXY" = true ]; then
            echo "Access OpenSearch Dashboards at: https://${primary_ip}"
            echo
            echo "NOTE: The self-signed SSL certificate was issued for the hostname '${FQDN}'."
            echo "You will receive a browser security warning. This is expected."
        else
            echo "Access OpenSearch Dashboards at: http://${primary_ip}:5601"
        fi
        echo "=================================================="
    }
    
    run_uninstall() {
        log "Uninstalling OpenSearch Stack"
        echo -e "\n\e[1;31m!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WARNING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        echo "This operation is IRREVERSIBLE."
        echo "It will permanently delete:"
        echo "  - OpenSearch, Dashboards, and Nginx packages."
        echo "  - All configuration files."
        echo "  - ALL DATA AND INDEXES stored in OpenSearch (/var/lib/opensearch)."
        echo -e "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\e[0m\n"
        read -p "To confirm this destructive action, type 'yes-delete-all-data': " confirm
        if [ "$confirm" != "yes-delete-all-data" ]; then
            echo "Uninstallation cancelled."
            exit 1
        fi
        
        detect_os
        execute "systemctl stop opensearch opensearch-dashboards nginx || true" "Stopping services"
        execute "systemctl disable opensearch opensearch-dashboards nginx || true" "Disabling services"
    
        if [ "$OS_ID" = "ubuntu" ] || [ "$OS_ID" = "debian" ]; then
            execute "apt-get purge -y opensearch opensearch-dashboards nginx" "Purging packages"
            execute "apt-get autoremove --purge -y" "Removing orphaned dependencies"
            execute "rm -f /etc/apt/sources.list.d/opensearch-2.x.list" "Removing repository file"
            execute "find /etc/apt/ -name '*.bak' -delete" "Removing repository backup files"
        elif [ "$OS_ID" = "rhel" ] || [ "$OS_ID" = "centos" ] || [ "$OS_ID" = "rocky" ]; then
            execute "dnf remove -y opensearch opensearch-dashboards nginx" "Removing packages"
            execute "rm -f /etc/yum.repos.d/opensearch-2.x.repo /etc/yum.repos.d/opensearch-dashboards-2.x.repo" "Removing repository files"
        fi
    
        execute "rm -rf /etc/opensearch /etc/opensearch-dashboards /var/lib/opensearch" "Removing data and config directories"
        execute "rm -rf /etc/nginx/conf.d/opensearch-dashboards.conf /etc/nginx/ssl" "Removing Nginx config"
        execute "sed -i '/vm.max_map_count=262144/d' /etc/sysctl.conf && sysctl -p" "Reverting kernel parameters"
        execute "rm -f $LOG_FILE" "Removing log file"
        log "Uninstallation complete."
    }
    
    run_enable_nginx() {
        log "Enabling Nginx Reverse Proxy"
        detect_os
    
        if ! command -v nginx &> /dev/null; then
            if [ "$OS_ID" = "ubuntu" ] || [ "$OS_ID" = "debian" ]; then
                execute "apt-get update && apt-get install -y nginx" "Installing Nginx" "verbose"
            elif [ "$OS_ID" = "rhel" ] || [ "$OS_ID" = "centos" ] || [ "$OS_ID" = "rocky" ]; then
                execute "dnf install -y nginx" "Installing Nginx" "verbose"
            fi
        fi
    
        execute "sed -i 's/server.host:.*/server.host: \"127.0.0.1\"/' /etc/opensearch-dashboards/opensearch_dashboards.yml" "Configuring Dashboards for local listening"
        configure_nginx_proxy
        execute "systemctl restart opensearch-dashboards" "Restarting Dashboards service"
        
        log "Nginx proxy has been enabled."
        echo "Access Dashboards at: https://$(hostname -I | awk '{print $1}')"
    }
    
    run_disable_nginx() {
        log "Disabling Nginx Reverse Proxy"
        execute "systemctl stop nginx || true" "Stopping Nginx"
        execute "systemctl disable nginx || true" "Disabling Nginx"
        execute "rm -f /etc/nginx/conf.d/opensearch-dashboards.conf" "Removing Nginx config"
        execute "rm -rf /etc/nginx/ssl" "Removing Nginx SSL directory"
        execute "sed -i 's/server.host:.*/server.host: \"0.0.0.0\"/' /etc/opensearch-dashboards/opensearch_dashboards.yml" "Configuring Dashboards for public listening"
        execute "systemctl restart opensearch-dashboards" "Restarting Dashboards service"
        
        log "Nginx proxy has been disabled."
        echo "Access Dashboards at: http://$(hostname -I | awk '{print $1'}):5601"
    }
    
    # --- ISM Management Functions ---
    
    run_ism_create_interactive() {
        log "Interactive ISM Policy Creator"
        read -p "Enter a name for the new policy (e.g., 30-day-delete): " policy_name
        read -p "Enter the index pattern this policy will apply to (e.g., my-logs-*): " index_pattern
        read -p "Enter number of days for the 'hot' phase (e.g., 7): " hot_days
        
        local policy_json
        policy_json=$(cat <<EOF
    {
        "policy": {
            "description": "A simple hot-to-delete policy.",
            "default_state": "hot",
            "states": [
                {
                    "name": "hot",
                    "actions": [ { "rollover": { "min_index_age": "${hot_days}d" } } ],
                    "transitions": [ { "state_name": "delete" } ]
                },
                { "name": "delete", "actions": [ { "delete": {} } ] }
            ],
            "ism_template": { "index_patterns": ["${index_pattern}"], "priority": 100 }
        }
    }
    EOF
    )
        execute_curl "PUT" "/_plugins/_ism/policies/${policy_name}" "$policy_json" "Creating ISM policy '${policy_name}'"
        echo "ISM Policy '${policy_name}' created. It will apply to new indices matching '${index_pattern}'."
    }
    
    run_ism_policy_apply() {
        if [ ! -f "$POLICY_FILE" ]; then execute "false" "Policy file not found at '$POLICY_FILE'"; fi
        local policy_json
        policy_json=$(cat "$POLICY_FILE")
        execute_curl "PUT" "/_plugins/_ism/policies/${POLICY_NAME}" "$policy_json" "Applying policy '${POLICY_NAME}' from file"
        echo "Policy '${POLICY_NAME}' has been created/updated."
    }
    
    run_ism_policy_get() {
        log "Fetching ISM Policy: ${POLICY_NAME}"
        execute_curl "GET" "/_plugins/_ism/policies/${POLICY_NAME}" "" "Fetching policy '${POLICY_NAME}'"
        echo "--- Policy Details for ${POLICY_NAME} ---"
        cat "$LOG_FILE" | sed '$d' | jq .
        echo "------------------------------------"
    }
    
    run_ism_policy_delete() {
        log "Deleting ISM Policy: ${POLICY_NAME}"
        read -p "Are you sure you want to delete the policy '${POLICY_NAME}'? (y/n): " confirm
        if [ "$confirm" != "y" ]; then echo "Deletion cancelled."; exit 1; fi
        execute_curl "DELETE" "/_plugins/_ism/policies/${POLICY_NAME}" "" "Deleting policy '${POLICY_NAME}'"
        echo "Policy '${POLICY_NAME}' deleted."
    }
    
    run_ism_policy_list() {
        log "Listing all ISM Policies"
        execute_curl "GET" "/_plugins/_ism/policies/" "" "Listing all policies"
        echo "--- All ISM Policies ---"
        cat "$LOG_FILE" | sed '$d' | jq .
        echo "------------------------"
    }
    
    run_ism_attach() {
        log "Attaching policy '${POLICY_NAME}' to index '${INDEX_NAME}'"
        local data
        data="{\"policy_id\": \"${POLICY_NAME}\"}"
        execute_curl "POST" "/_plugins/_ism/add/${INDEX_NAME}" "$data" "Attaching policy"
        echo "Policy attached."
    }
    
    run_ism_remove() {
        log "Removing policy from index '${INDEX_NAME}'"
        execute_curl "POST" "/_plugins/_ism/remove/${INDEX_NAME}" "" "Removing policy"
        echo "Policy removed."
    }
    
    run_status() {
        log "Fetching Installation Status"
        if [ ! -f "$PASSWORD_FILE" ]; then
            echo "Could not find password file at '$PASSWORD_FILE'." >&2
            echo "Status cannot be determined. The installation may be incomplete or the password was not saved." >&2
            exit 1
        fi
        local password
        password=$(sudo cat "$PASSWORD_FILE")
    
        local url
        if [ -f /etc/nginx/conf.d/opensearch-dashboards.conf ]; then
            url="https://$(hostname -I | awk '{print $1}')"
        else
            url="http://$(hostname -I | awk '{print $1'}):5601"
        fi
    
        echo "--- OpenSearch Installation Details ---"
        echo "Dashboard URL: $url"
        echo "Admin User:    admin"
        echo "Admin Password: $password"
        echo "---------------------------------------"
    }
    
    # --- Script Entrypoint ---
    
    # Check for root privileges
    if [ "$EUID" -ne 0 ]; then
      echo "Please run this script as root or with sudo." >&2
      exit 1
    fi
    
    # Main command router
    COMMAND="${1:---help}"
    shift || true
    
    # Parse arguments for all commands
    while [[ $# -gt 0 ]]; do
        key="$1"
        case $key in
            --with-nginx) INSTALL_NGINX_PROXY=true; shift;;
            --password) USER_PASSWORD="$2"; shift; shift;;
            --name) POLICY_NAME="$2"; shift; shift;;
            --file) POLICY_FILE="$2"; shift; shift;;
            --policy) POLICY_NAME="$2"; shift; shift;;
            --index) INDEX_NAME="$2"; shift; shift;;
            *) echo "Error: Unknown argument '$1'" >&2; usage; exit 1;;
        esac
    done
    
    case "$COMMAND" in
        install) run_installation ;;
        status) run_status ;;
        ism-create-interactive) run_ism_create_interactive ;;
        ism-policy-apply)
            if [ -z "${POLICY_NAME:-}" ] || [ -z "${POLICY_FILE:-}" ]; then echo "Error: --name and --file are required." >&2; usage; exit 1; fi
            run_ism_policy_apply ;;
        ism-policy-get)
            if [ -z "${POLICY_NAME:-}" ]; then echo "Error: --name is required." >&2; usage; exit 1; fi
            run_ism_policy_get ;;
        ism-policy-delete)
            if [ -z "${POLICY_NAME:-}" ]; then echo "Error: --name is required." >&2; usage; exit 1; fi
            run_ism_policy_delete ;;
        ism-policy-list) run_ism_policy_list ;;
        ism-attach)
            if [ -z "${POLICY_NAME:-}" ] || [ -z "${INDEX_NAME:-}" ]; then echo "Error: --policy and --index are required." >&2; usage; exit 1; fi
            run_ism_attach ;;
        ism-remove)
            if [ -z "${INDEX_NAME:-}" ]; then echo "Error: --index is required." >&2; usage; exit 1; fi
            run_ism_remove ;;
        --uninstall) run_uninstall ;;
        --enable-nginx) run_enable_nginx ;;
        --disable-nginx) run_disable_nginx ;;
        --help|-h) usage ;;
        *) echo "Error: Unknown command '$COMMAND'" >&2; usage; exit 1 ;;
    esac
[/code]

make this script executable using the following command.
[code] 
    chmod +x deploy_opensearch.sh
[/code]

Run the script to install OpenSearch.
[code] 
    ./deploy_opensearch.sh install
[/code]

##   
Step 2: Setup OpenSearch

Once installation is completed, access the dashboards with `<host IP>:5601` on browser and login using the credentials provided in previous step.

After logging in, UI will look like this:-

![image-20250915-131641.png](attachments/1277919276/1303183361.png?width=1800)
