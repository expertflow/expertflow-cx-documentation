# CX Knowledgebase : Translation support at customer widget

**Steps required for the configuration of translations in the customer widget**  


  1. cd into `{your-cx-solution}/kubernetes`

  2. Add translation files inside `pre-deployment/app-translations/customer-widget/i18n/` ( the translation files can be found in the `cim-skeleton` project)

  3. Mounting the volumes in the customer widget section in core helm-charts 



[code] 
    extraVolumes:
          - name: ef-widget-translation
            configMap:
               name: ef-widget-translations-cm
    extraVolumeMounts:
          - name: ef-widget-translation
            mountPath: /usr/share/nginx/html/widget-assets/i18n/
            
[/code]

  3. Apply config map  
`kubectl -n expertflow create configmap ef-widget-translations-cm --from-file=pre-deployment/app-translations/customer-widget/i18n/`

  4. restart the customer widget component



[code] 
    helm upgrade --install --namespace expertflow --create-namespace   ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx
[/code]

  
**For updating the translation file in customer widget**

  1. cd into `{your-cx-solution}/kubernetes`

  2. make changes in desired file at `pre-deployment/app-translations/customer-widget/i18n/`

  3. delete the config map `kubectl delete cm ef-widget-translations-cm -n expertflow`

  4. Apply config map  
`kubectl -n expertflow create configmap ef-widget-translations-cm --from-file=pre-deployment/app-translations/customer-widget/i18n `  
_make sure you are at_`{your-cx-solution}/kubernetes` _before running the above command_

  5. restart the customer widget component



[code] 
    helm upgrade --install --namespace expertflow --create-namespace   ef-cx  --debug --values helm-values/ef-cx-custom-values.yaml expertflow/cx
[/code]
