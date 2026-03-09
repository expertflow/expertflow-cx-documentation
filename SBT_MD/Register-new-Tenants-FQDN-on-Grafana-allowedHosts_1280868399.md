# CX Knowledgebase : Register new Tenants FQDN on Grafana allowedHosts

This guide shows how to register newly added Tenants FQDN to Grafana allowedHosts, so that Grafana will be able to make requests to those FQDNs.

  1. Once a new tenant is created, we need to register the tenant's FQDN in the list of allowedHosts.

  2. Open Grafana on a separate browser, `https://<CX_TENANT_URL>/grafana` to access the grafana configuration portal.

  3. Login using the admin user and password.

  4. Go to `Connections` > `DataSources` > `infinity_cim_json_api` > `Security` >`Allowed Hosts` > `Click on Add button` > `Click on Save and Test`

  5. Edit `infinity_cim_json_api` datasource.

![imageedit_19_6966720613.gif](attachments/1280868399/1281097750.gif?width=1011)
  6. We also need to add it on the datasource file, so that in case application goes down, it will be able to add the registered hosts during restart.

  7. Edit `post-deployment/config/grafana/supervisor-dashboards/datasource.yml`

  8. Go under `infinity_cim_json_api` > `jsonData` > `allowedHosts` and add all the tenants fqdn. eg
[code] ############################################  INFINITY API PLUGIN CONFIGURATION ##########################################
           - name: infinity_cim_json_api
             jsonData:
               allowedHosts:
                 - "*"
                 - "https://example1.com"
                 - "https://example2.com"
                 - "https://example3.com"
                 - "https://example4.com"
         
[/code]

  9. Re-apply data-source manifest.

  10. 
[code]# Delete secret
         kubectl -n expertflow  delete secret ef-grafana-datasource-secret
         
         # Re-apply secret
         kubectl -n expertflow  create secret generic ef-grafana-datasource-secret --from-file=post-deployment/config/grafana/supervisor-dashboards/datasource.yml
[/code]



