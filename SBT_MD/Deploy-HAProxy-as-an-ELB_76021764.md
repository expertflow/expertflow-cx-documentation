# CX Knowledgebase : Deploy HAProxy as an ELB

  1. Install HAProxy
[code] # On Ubuntu
         apt update
         apt install -y haproxy
         systemctl enable haproxy
         systemctl start haproxy
         
         # On RedHat
         yum update
         yum install haproxy -y
         systemctl enable haproxy
         systemctl start haproxy
[/code]

  2. For SSL termination, edit `haproxy.cfg` with the following
[code] global
                 log /dev/log    local0
                 log /dev/log    local1 notice
                 chroot /var/lib/haproxy
                 stats socket /run/haproxy/admin.sock mode 660 level admin
                 stats timeout 30s
                 user haproxy
                 group haproxy
                 daemon
         
                 # Default SSL material locations
                 ca-base /etc/ssl/certs
                 crt-base /etc/ssl/private
                 maxconn 2000000
                 # Default ciphers to use on SSL-enabled listening sockets.
                 # For more information, see ciphers(1SSL). This list is from:
                 #  https://hynek.me/articles/hardening-your-web-servers-ssl-ciphers/
                 #ssl-default-bind-ciphers  ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES:!aNULL:!MD5:!DSS
                 ssl-default-bind-ciphers ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+3DES:!aNULL:!MD5:!DSS
                 ssl-default-bind-options force-tlsv12 no-sslv3 no-tls-tickets
                 tune.ssl.default-dh-param 2048
                 nbproc 8
                 cpu-map  1 1
                 cpu-map  2 2
                 cpu-map  3 3
                 cpu-map  4 4
                 stats bind-process 4
         
         defaults
                 log     global
                 mode    http
                 option  httplog
                 option forwardfor
                 option  dontlognull
                 timeout connect 50000s
                 timeout client  50000s
                 timeout server  50000s
                 retries 4
                 maxconn 2000000
                 errorfile 400 /etc/haproxy/errors/400.http
                 errorfile 403 /etc/haproxy/errors/403.http
                 errorfile 408 /etc/haproxy/errors/408.http
                 errorfile 500 /etc/haproxy/errors/500.http
                 errorfile 502 /etc/haproxy/errors/502.http
                 errorfile 503 /etc/haproxy/errors/503.http
                 errorfile 504 /etc/haproxy/errors/504.http
         
         frontend www-http
             mode http
             stats enable
             stats uri /haproxy?stats
             bind 0.0.0.0:80
             http-request set-header X-Forwarded-Proto http
             option http-server-close
             option forwardfor except 127.0.0.1
             option forwardfor header X-Real-IP
             # CHANGE ME 
             acl host_ef_cx hdr(host) -i <FQDN>
             # 
             acl is_websocket hdr(Upgrade) -i WebSocket
             acl is_websocket hdr_beg(Host) -i wss
             use_backend ef_cx if host_ef_cx
         
         frontend www-https
             bind *:443 ssl crt /etc/ssl/certificate.pem alpn h2,http/1.1
             option http-server-close
             redirect scheme https if !{ ssl_fc }
             http-request set-header X-Forwarded-Proto https if { ssl_fc }
             option forwardfor except 127.0.0.1
             option forwardfor header X-Real-IP
             # CHANGE ME
             acl host_ef_cx hdr(host) -i FQDN
             # 
             acl is_websocket hdr(Upgrade) -i WebSocket
             acl is_websocket hdr_beg(Host) -i wss
             use_backend ef_cx if host_ef_cx
         
         
         frontend kubernetes
         	bind LB_IP:6443
         	option tcplog
         	mode tcp
         	default_backend kubernetes-master-nodes
         
         backend kubernetes-master-nodes
         	mode tcp
         	balance roundrobin
         	option tcp-check
                 server CP_NODE_1 CP_NODE_1_IP:6443 check fall 3 rise 2
                 server CP_NODE_2 CP_NODE_2_IP:6443 check fall 3 rise 2
                 server CP_NODE_3 CP_NODE_3_IP:6443 check fall 3 rise 2
         
         frontend supervisor
         	bind LB_IP:9345
         	option tcplog
         	mode tcp
         	default_backend supervisor
         
         backend supervisor
         	mode tcp
         	balance roundrobin
         	option tcp-check
                 server CP_NODE_1 CP_NODE_1_IP:9345 check fall 3 rise 1
                 server CP_NODE_2 CP_NODE_2_IP:9345 check fall 3 rise 1
                 server CP_NODE_3 CP_NODE_3_IP:9345 check fall 3 rise 1
         
         backend ef_cx
                 redirect scheme https if !{ ssl_fc }
                 mode http
                 balance roundrobin
                 option tcp-check
                 server WORKER_NODE_1 WORKER_NODE_1_IP:80 check fall 3 rise 2
                 server WORKER_NODE_1 WORKER_NODE_1_IP:80 check fall 3 rise 2
                 server WORKER_NODE_1 WORKER_NODE_1_IP:80 check fall 3 rise 2
[/code]

  3. For SSL passthrough, use the following `HAProxy confiugration `
[code] global
                 log /dev/log    local0
                 log /dev/log    local1 notice
                 chroot /var/lib/haproxy
                 stats socket /run/haproxy/admin.sock mode 660 level admin
                 stats timeout 30s
                 user haproxy
                 group haproxy
                 daemon
         
                 maxconn 2000000
                 nbproc 8
                 cpu-map  1 1
                 cpu-map  2 2
                 cpu-map  3 3
                 cpu-map  4 4
                 stats bind-process 4
         
         defaults
                 log     global
                 mode    http
                 option  httplog
                 option forwardfor
                 option  dontlognull
                 timeout connect 50000s
                 timeout client  50000s
                 timeout server  50000s
                 retries 4
                 maxconn 2000000
                 errorfile 400 /etc/haproxy/errors/400.http
                 errorfile 403 /etc/haproxy/errors/403.http
                 errorfile 408 /etc/haproxy/errors/408.http
                 errorfile 500 /etc/haproxy/errors/500.http
                 errorfile 502 /etc/haproxy/errors/502.http
                 errorfile 503 /etc/haproxy/errors/503.http
                 errorfile 504 /etc/haproxy/errors/504.http
         
         
         frontend kubernetes
             bind LB_IP:6443
             option tcplog
             mode tcp
             default_backend kubernetes-master-nodes
          
         backend kubernetes-master-nodes
             mode tcp
             balance roundrobin
             option tcp-check
                 server CP_NODE_1 CP_NODE_1_IP:6443 check fall 3 rise 2
                 server CP_NODE_2 CP_NODE_2_IP:6443 check fall 3 rise 2
                 server CP_NODE_3 CP_NODE_3_IP:6443 check fall 3 rise 2
          
         frontend supervisor
             bind LB_IP:9345
             option tcplog
             mode tcp
             default_backend supervisor
          
         backend supervisor
             mode tcp
             balance roundrobin
             option tcp-check
                 server CP_NODE_1 CP_NODE_1_IP:9345 check fall 3 rise 1
                 server CP_NODE_2 CP_NODE_2_IP:9345 check fall 3 rise 1
                 server CP_NODE_3 CP_NODE_3_IP:9345 check fall 3 rise 1
         
         frontend www-http
         	bind *:80
         	reqadd X-Forwarded-Proto:\ http
         	default_backend ef_cx-http
         
         frontend www-https
         	bind *:443 ssl crt /etc/haproxy/cert.pem
         	reqadd X-Forwarded-Proto:\ https
         	default_backend ef_cx-https   
         
         backend ef_cx-http
         	mode http
         	option httpchk HEAD /healthz HTTP/1.0
         	server WORKER_NODE_1 WORKER_NODE_1_IP:80 check weight 1 maxconn 1024
         	server WORKER_NODE_2 WORKER_NODE_2_IP:80 check weight 1 maxconn 1024
         	server WORKER_NODE_3 WORKER_NODE_3_IP:80 check weight 1 maxconn 1024  
         backend ef_cx-https
         	mode http
         	option httpchk HEAD /healthz HTTP/1.0
         	server WORKER_NODE_1 WORKER_NODE_1_IP:443 check weight 1 maxconn 1024 ssl verify none
         	server WORKER_NODE_2 WORKER_NODE_2_IP:443 check weight 1 maxconn 1024 ssl verify none
         	server WORKER_NODE_3 WORKER_NODE_3_IP:443 check weight 1 maxconn 1024 ssl verify none
[/code]



