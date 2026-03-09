# CX Knowledgebase : HIPAA Compliance

The Health Insurance Portability and Accountability Act (HIPAA) establishes standards to protect sensitive patient health information (PHI) from being disclosed without the patient's consent or knowledge. Expertflow takes the following measures for [HIPAA Technical Safeguards](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html).  
  
**HIPAA Technical Safeguards**| **Compliance**| **Expertflow CX Compliance**  
---|---|---  
**Access Control**. A regulated entity must implement technical policies and procedures for its electronic information systems that maintain ePHI to allow only authorized persons to access ePHI.|  COMPLIANT | 

  * Role-based access controls (RBAC) and group-based access controls (GBAC) are implemented in Expertflow CX so that only authorized Agents can access the application. For more details see [Agent Authorization with Agent Desk](/wiki/pages/createpage.action?spaceKey=SBT&title=Agent%20Authorization%20with%20Agent%20Desk&linkCreation=true&fromPageId=826802235)
  * To protect patients’ personal information, we offer the PII data masking features:
    * [**PII data masking in AgentDesk**](PII-Data-Masking_884113585.html)

  
**Authentication**. A regulated entity must implement procedures to verify that a person seeking access to ePHI is who they say they are.| COMPLIANT | All agents must authenticate themselves to use Expertflow CX, also as an added layer of security Two-factor authentication can be used as a second form of verification. For more details see [Identity and Access Management](/wiki/pages/createpage.action?spaceKey=SBT&title=Identity%20and%20Access%20Management&linkCreation=true&fromPageId=826802235).  
**Transmission Security.** A regulated entity must implement technical security measures to guard against unauthorized access to ePHI that is being transmitted over an electronic network.|  COMPLIANT| Expertflow CX uses TLS for secure communication. See [Data Encryption](Data-Encryption_884932744.html) for details.  
**Audit Controls**. A regulated entity must implement hardware, software, and/or procedural mechanisms to record and examine activity in information systems that contain or use ePHI. A regulated entity must implement policies and procedures to ensure that ePHI is not improperly altered or destroyed. Electronic measures must be put in place to confirm that ePHI has not been improperly altered or destroyed.| COMPLIANT| Centralized audit logging is available via OpenSearch. Event logging for IAM is also available. Event logging for CX Components is on RoadMap.
