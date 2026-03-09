# CX Knowledgebase : Handling Superset Session Timeout

## Problem Statement:

The superset does not enforce a sufficient session timeout, allowing unauthorized users to access sensitive data after a user has left the application. This increases the risk of session hijacking and unauthorized access. Sessions are meant to be temporary, and when a user is inactive for a certain period, their session should expire. However, in this case, the application maintains active sessions beyond a reasonable period of inactivity, which could potentially allow malicious actors to exploit this vulnerability

## Solution:

Implementation of Session Timeout by writing custom implementation in **superset_config.py** file and then importing it via environment variable in kubernetes deployment of Superset.

### Step 1: Write Session Lifetime Implementation inside Superset Configmap:

Inside Superset Configmap, write a custom implementation for Session Lifetime under **data.** This configuration implements session timeout and security enhancements through several layers:

**Session Timeout Configuration** :

  1. Sets `PERMANENT_SESSION_LIFETIME` to 3600 seconds (1 hour)

  2. After this period, users will be automatically logged out

  3. You can adjust the timeout duration by modifying this value



[code] 
    # configmap.yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: superset-config
    data:
      superset_config.py: |
        # Session timeout configuration (in seconds)
        PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
        SESSION_COOKIE_SAMESITE = 'Strict'
        SESSION_COOKIE_SECURE = True
        SESSION_COOKIE_HTTPONLY = True
        
        # Force HTTPS
        PREFERRED_URL_SCHEME = 'https'
        
        # Session protection
        SESSION_PROTECTION = 'strong'
        
        # Enable CSP headers
        HTTP_HEADERS = {
            'X-Frame-Options': 'SAMEORIGIN',
            'X-XSS-Protection': '1; mode=block',
            'X-Content-Type-Options': 'nosniff',
            'Content-Security-Policy': "default-src 'self' 'unsafe-inline' 'unsafe-eval'"
        }
[/code]

### Step 2: Import the changes required in superset deployment.yaml file:

Ensure these settings exist in your deployment:
[code] 
    spec:
      template:
        spec:
          containers:
            - name: superset
              volumeMounts:
                - name: config-volume
                  mountPath: /app/pythonpath
              env:
                - name: SUPERSET_CONFIG_PATH
                  value: /app/pythonpath/superset_config.py
                - name: FLASK_APP
                  value: superset.app:create_app()
          volumes:
            - name: config-volume
              configMap:
                name: superset-config
[/code]

### Step 3: Apply the updated Configmap and Deployment:
[code] 
    kubectl apply -f updated-configmap.yaml
    kubectl apply -f updated-deployment.yaml
[/code]

## Notes

  * The PERMANENT_SESSION_LIFETIME value (3600 seconds = 1 hour) can be adjusted based on your requirements

  * All security headers can be customized in the HTTP_HEADERS section



