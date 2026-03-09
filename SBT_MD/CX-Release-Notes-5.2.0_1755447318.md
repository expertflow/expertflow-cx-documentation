# CX Knowledgebase : CX Release Notes 5.2.0

**Release Name**|  CX5.2.0  
---|---  
**Release Ready Date**|   
**Release Summary**|   
  
## For New Deployments

For fresh deployment, see this guide

## Upgrade Existing

To upgrade from [CX5.1.0 to CX5.2.0](Upgrade-Guide-CX5.1.0-to-CX5.2.0_1755447383.html), see Upgrade Guide 

## New in CX5.2.0

This is a patch release on top of CX5.1.0, which includes targeted enhancements and critical fixes to improve 

### Platform & Security Improvements

**Feature(s)**| **Description**  
---|---  
**Message broker upgrade to Apache Artemis**|  Replaces the legacy ActiveMQ message broker with Apache Artemis to improve scalability, reliability, and cloud-native compatibility. The new broker supports high-availability deployments and simplifies operations while preserving existing messaging patterns for connected services.   
Use [this guide](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/1268056065/Apache+ActiveMQ+Artemis+Deployment+Latest+Stable+Version+as+a+System+Service) to deploy Artemis in a fresh environment.  
Use [this guide ](https://expertflow-docs.atlassian.net/wiki/spaces/DTDO/pages/1268056065/Apache+ActiveMQ+Artemis+Deployment+Latest+Stable+Version+as+a+System+Service)to migrate from the previous Helm-based ActiveMQ setup to Artemis.  
  
### Enhancements/Improvements

|   
---|---  
  
## Compatible with

This release has been thoroughly tested with various [environments and tools](https://docs.expertflow.com/cx-knowledgebase/latest/compatibility-guides).

## Release Test Highlights

## Planned Epics

![](images/icons/grey_arrow_down.png)Expand to view epics planned for this release  
  
Key | Summary | T | Assignee | Status | P  
[CIM-13375](https://expertflow-docs.atlassian.net/browse/CIM-13375) |  [ Replace AMQ with Apache Artemis ](https://expertflow-docs.atlassian.net/browse/CIM-13375) |  [![Epic](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10307?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-13375) |  Devops@expertflow.com  |  Release-Ready  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg)  
  
[ 1 issue ](https://expertflow-docs.atlassian.net/issues/?jql=category+in+%28CX%29+AND+issuetype+in+%28Epic%29+AND+fixVersion+%3D+CX5.2.0+ORDER+BY+priority+DESC+++++&src=confmacro "View all matching issues in JIRA.")

## Planned Features

![](images/icons/grey_arrow_down.png)Expand to view features planned for this release  
  
Key | Summary | T | Due | Assignee | P | Status  
[CIM-32914](https://expertflow-docs.atlassian.net/browse/CIM-32914) |  [ Tenant Management Portal ](https://expertflow-docs.atlassian.net/browse/CIM-32914) |  [![New Feature](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10311?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32914) |  |  Nabeel Jhatial  |  ![Major](https://expertflow-docs.atlassian.net/images/icons/priorities/major.svg) |  In-Progress   
[CIM-32386](https://expertflow-docs.atlassian.net/browse/CIM-32386) |  [ Connect Multiple LinkedIn pages with one tenant ](https://expertflow-docs.atlassian.net/browse/CIM-32386) |  [![New Feature](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10311?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32386) |  16/Jan/26  |  Ahmed Hasan  |  ![Minor](https://expertflow-docs.atlassian.net/images/icons/priorities/minor.svg) |  QA-Ready   
[CIM-31806](https://expertflow-docs.atlassian.net/browse/CIM-31806) |  [ MVP1- Agent Desk Summary and Sentiments Visibility ](https://expertflow-docs.atlassian.net/browse/CIM-31806) |  [![New Feature](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10311?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-31806) |  |  Nabeel Jhatial  |  ![Minor](https://expertflow-docs.atlassian.net/images/icons/priorities/minor.svg) |  In-Review   
  
[ 3 issues ](https://expertflow-docs.atlassian.net/issues/?jql=category+in+%28CX%29+AND+issuetype+%3D+%22New+Feature%22+AND+fixVersion+%3D+CX5.2.0+ORDER+BY+priority+DESC++++&src=confmacro "View all matching issues in JIRA.")

## Planned Bugs

![](images/icons/grey_arrow_down.png)Expand to view bugs planned for this release  
  
Key | Summary | T | Assignee | P | Status  
  
[ No issues found ](https://expertflow-docs.atlassian.net/issues/?jql=category+in+%28CX%29+AND+issuetype+in+%28Bug%29+AND+fixVersion+%3D+CX5.2.0+ORDER+BY+priority+DESC++++&src=confmacro)

## Issues Opened in this release

![](images/icons/grey_arrow_down.png)Expand to view bugs opened in this release but will remain open for the future.  
  
Key | Summary | T | Assignee | P | Status  
[CIM-32613](https://expertflow-docs.atlassian.net/browse/CIM-32613) |  [ CLONE 5.1 - Not able to store conversation data via customer widget other then string type. ](https://expertflow-docs.atlassian.net/browse/CIM-32613) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32613) |  Abdullah Hanan  |  ![Blocker](https://expertflow-docs.atlassian.net/images/icons/priorities/blocker.svg) |  Release-Ready   
[CIM-31850](https://expertflow-docs.atlassian.net/browse/CIM-31850) |  [ CLONE - Conversation remains stuck when it's transfered to other agent and the agent doesn't accept it. ](https://expertflow-docs.atlassian.net/browse/CIM-31850) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-31850) |  Faraz Usman  |  ![Blocker](https://expertflow-docs.atlassian.net/images/icons/priorities/blocker.svg) |  Release-Ready   
[CIM-30510](https://expertflow-docs.atlassian.net/browse/CIM-30510) |  [ APISIX dataplane issue ](https://expertflow-docs.atlassian.net/browse/CIM-30510) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-30510) |  Devops@expertflow.com  |  ![Blocker](https://expertflow-docs.atlassian.net/images/icons/priorities/blocker.svg) |  Open   
[CXIM-377](https://expertflow-docs.atlassian.net/browse/CXIM-377) |  [ Information Disclosure on Grafana ](https://expertflow-docs.atlassian.net/browse/CXIM-377) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CXIM-377) |  Devops@expertflow.com  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  In-Review   
[CIM-32942](https://expertflow-docs.atlassian.net/browse/CIM-32942) |  [ Rasa deployed using Helm is not functioning ](https://expertflow-docs.atlassian.net/browse/CIM-32942) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32942) |  Devops@expertflow.com  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Discovery   
[CIM-32616](https://expertflow-docs.atlassian.net/browse/CIM-32616) |  [ CLONE 5.1 - In case of 2FA, QM is unable to call evaluator from keycloak ](https://expertflow-docs.atlassian.net/browse/CIM-32616) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32616) |  Abdullah Hanan  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32615](https://expertflow-docs.atlassian.net/browse/CIM-32615) |  [ CLONE 5.1 - Form Multiple submission against a single conversation ](https://expertflow-docs.atlassian.net/browse/CIM-32615) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32615) |  Abdullah Hanan  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32614](https://expertflow-docs.atlassian.net/browse/CIM-32614) |  [ CLONE 5.1 - Comment truncation issue on Facebook page for agent responses. ](https://expertflow-docs.atlassian.net/browse/CIM-32614) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32614) |  Aeiman Afzal  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32572](https://expertflow-docs.atlassian.net/browse/CIM-32572) |  [ CLONE 5.1 - Invalid Image handling in case of Forwarding ](https://expertflow-docs.atlassian.net/browse/CIM-32572) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32572) |  Talha  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32571](https://expertflow-docs.atlassian.net/browse/CIM-32571) |  [ CLONE 5.1 - QUEUED conversations Not Routed After Routing Engine Restart ](https://expertflow-docs.atlassian.net/browse/CIM-32571) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32571) |  Aeiman Afzal  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32565](https://expertflow-docs.atlassian.net/browse/CIM-32565) |  [ CLONE 5.1 - WrapUp Forms removed on Unified Admin Pod restart ](https://expertflow-docs.atlassian.net/browse/CIM-32565) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32565) |  Abdullah Hanan  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32564](https://expertflow-docs.atlassian.net/browse/CIM-32564) |  [ CLONE 5.1 - Incorrect Session End Event Triggered After Agent Finding Time Expires ](https://expertflow-docs.atlassian.net/browse/CIM-32564) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32564) |  umar.ikhlaq  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32547](https://expertflow-docs.atlassian.net/browse/CIM-32547) |  [ CLONE 5.1 - Make MessagePayloadSize over socket configurable in Agent Manager ](https://expertflow-docs.atlassian.net/browse/CIM-32547) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32547) |  Talha  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32545](https://expertflow-docs.atlassian.net/browse/CIM-32545) |  [ CLONE 5.1 - Fix for Conversations Stuck Due to Direct Transfer RONA Events ](https://expertflow-docs.atlassian.net/browse/CIM-32545) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32545) |  Aeiman Afzal  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-32215](https://expertflow-docs.atlassian.net/browse/CIM-32215) |  [ Handling on missing inline image incase of no content during reply/forward scenario's due to initial spacing in editor ](https://expertflow-docs.atlassian.net/browse/CIM-32215) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-32215) |  Talha  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-31635](https://expertflow-docs.atlassian.net/browse/CIM-31635) |  [ Wrap-up details and notes data missing due to replication key mismatch in reporting connector ](https://expertflow-docs.atlassian.net/browse/CIM-31635) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-31635) |  Rohail Iqbal  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-30869](https://expertflow-docs.atlassian.net/browse/CIM-30869) |  [ Slowness in Routing Engine caused chats to remain in queue under load (CX-4.10) ](https://expertflow-docs.atlassian.net/browse/CIM-30869) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-30869) |  Muhammad Zubair  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Re-opened   
[CIM-30809](https://expertflow-docs.atlassian.net/browse/CIM-30809) |  [ Message count mismatch in load test for CX-4.10 – Expected 179K & Received 138K ](https://expertflow-docs.atlassian.net/browse/CIM-30809) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-30809) |  Shakir Abbas  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Open   
[CIM-30801](https://expertflow-docs.atlassian.net/browse/CIM-30801) |  [ The supervisor dashboard frontend rendering is slow under load ](https://expertflow-docs.atlassian.net/browse/CIM-30801) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-30801) |  Abraham Lugonzo  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Release-Ready   
[CIM-30411](https://expertflow-docs.atlassian.net/browse/CIM-30411) |  [ After VM reboot APISIX pods in crashloop back state ](https://expertflow-docs.atlassian.net/browse/CIM-30411) |  [![Bug](https://expertflow-docs.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium)](https://expertflow-docs.atlassian.net/browse/CIM-30411) |  Sabahat Haneef  |  ![Critical](https://expertflow-docs.atlassian.net/images/icons/priorities/critical.svg) |  Open   
  
Showing 20 out of [ 126 issues ](https://expertflow-docs.atlassian.net/issues/?jql=category+in+%28cx%29+AND+issuetype+%3D+Bug+AND+affectedVersion+in+%28CX4.5%2C+CX4.5.1%2C+CX4.5.2%2C+CX4.5.3%2C+CX4.5.4%2C+CX4.6%2C+CX4.7%2C++CX4.8%2C+CX4.9%2C+CX4.9.2%2C+CX4.9.3%2C+CX4.9.4%2C+CX4.9.5%2C+CX4.10%2C+CX4.10.1%2C+CX4.10.2%2C+CX4.10.3%2C+CX5.0%2C+CX5.1.0%29++AND+status+not+in+%28Done%2C+Closed%2C+Resolved%29++ORDER+BY+priority+DESC++&src=confmacro "View all matching issues in JIRA.")
