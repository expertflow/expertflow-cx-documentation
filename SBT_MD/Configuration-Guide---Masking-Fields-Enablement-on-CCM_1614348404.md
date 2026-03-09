# CX Knowledgebase : Configuration Guide - Masking Fields Enablement on CCM

This configuration is required only in CX-4.10.5 and onwards

The intended audience for this guide is anyone who is configuring CX solution either on local or customer environment.

There is a temporary implementation that securely manages sensitive information within channel connector settings, ensuring that these details are not exposed in API responses or application logs. This update significantly enhances the security of channel connector settings, preventing unauthorized access to confidential credentials. 

For this, there are 2 new environment variables added under **Customer Channel Manager (CCM)** chart. 

  1. `IS_PASSWORD_MASKING_ENABLED`

  2. `PASSWORD_MASKING_ENABLED_FIELDS`




Its default values are already part of the **CX-4.10.5** chart. To enable it, the Enabled flag will be set to `true,` and Fields contains all the fields that are used in Unified Admin → Channel Manager → Channel Connector settings as Keys. All the fields mentioned in this field will be masked in all API responses, events, and logs with asterisk.
