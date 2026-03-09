# CX Knowledgebase : Deploy NGINX as an ELB

  1. Install NGINX using below given steps
[code] # For RHEL
         yum install nginx -y
         
         # For Ubuntu
         apt update 
         apt install nginx -y
[/code]

  2. Move existing `nginx.conf` to a backup file and create a new one for the below mentioned configurations.
[code] sudo mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
         sudo vim /etc/nginx/nginx.conf
[/code]

  3. Copy the following configurations in the blank `nginx.conf` file. Replace the WORKER_NODE and CP_NODE with appropriate values.
[code] user nginx;
         worker_processes 4;
         worker_rlimit_nofile 40000;
         error_log /var/log/nginx/error.log;
         pid /run/nginx.pid;
         
         # Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
         include /usr/share/nginx/modules/*.conf;
         
         events {
             worker_connections 8192;
         }
         
         stream {
         upstream backend {
                 least_conn;
                 server CP_NODE_1:9345 max_fails=3 fail_timeout=5s;
                 server CP_NODE_2:9345 max_fails=3 fail_timeout=5s;
                 server CP_NODE_3:9345 max_fails=3 fail_timeout=5s;
            }
         
            # This server accepts all traffic to port 9345 and passes it to the upstream. 
            # Notice that the upstream name and the proxy_pass need to match.
         server {
               listen 9345;
                   proxy_pass backend;
            }
         upstream ef_cx_api {
                 least_conn;
                 server CP_NODE_1:6443 max_fails=3 fail_timeout=5s;
                 server CP_NODE_2:6443 max_fails=3 fail_timeout=5s;
                 server CP_NODE_3:6443 max_fails=3 fail_timeout=5s;
             }
         server {
                 listen     6443;
                 proxy_pass ef_cx_api;
                 }
         upstream ef_cx_http {
                 least_conn;
                 server WORKER_NODE_1:80 max_fails=3 fail_timeout=5s;
                 server WORKER_NODE_2:80 max_fails=3 fail_timeout=5s;
                 server WORKER_NODE_1:80 max_fails=3 fail_timeout=5s;
             }
         server {
                 listen     80;
                 proxy_pass ef_cx_http;
                 }
         upstream ef_cx_https {
                 least_conn;
                 server WORKER_NODE_1:443 max_fails=3 fail_timeout=5s;
                 server WORKER_NODE_2:443 max_fails=3 fail_timeout=5s;
                 server WORKER_NODE_3:443 max_fails=3 fail_timeout=5s;
             }
         server {
                 listen     443;
                 proxy_pass ef_cx_https;
                 }
         }
[/code]

  4. Start the nginx service 



[code] 
    systemctl enable --now nginx
[/code]
