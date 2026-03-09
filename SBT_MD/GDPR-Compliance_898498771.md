# CX Knowledgebase : GDPR Compliance

The General Data Protection Regulation (GDPR) is a comprehensive data protection law that sets strict guidelines for how personal data is collected, processed, stored, and shared, to give individuals greater control over their data. This article explains how Expertflow complies with the **General Data Protection Regulation (GDPR).**

| **Requirement**| **Compliance**| **Expertflow CX Compliance**  
---|---|---|---  
1| **Data Encryption** Implement strong encryption mechanisms to protect personal data both at rest and in transit.| COMPLIANT | Expertflow CX uses TLS for secure communication. See [Data Encryption](Data-Encryption_884932744.html) for details.  
2| **Access controls** Enforce role-based access controls (RBAC) to limit access to personal data only to authorized individuals.| COMPLIANT | Role-based access controls (RBAC) and group-based access controls (GBAC) are implemented in Expertflow CX so that only authorized Agents can access the application. For more details see [Agent Authorization with Agent Desk](/wiki/pages/createpage.action?spaceKey=SBT&title=Agent%20Authorization%20with%20Agent%20Desk&linkCreation=true&fromPageId=898498771)  
3| **Anonymization & Pseudonymization**  
Implement data masking or tokenization to reduce exposure of personal data.| COMPLIANT | To protect users’ personal information, we offer the PII data masking features:

  * [**PII data masking in logs**](PII-Data-Masking_884113585.html)
  * [**PII data masking in AgentDesk**](PII-Data-Masking_884113585.html)

  
4| **Audit Logs** Record all actions related to personal data access, modification, and deletion.  
and ensure logs cannot be modified or deleted.| COMPLIANT | Centralized audit logging is on the roadmap for 2025.  
5| **Pause-and-resume recording** Allow agents to pause call recordings when discussing sensitive personal data.|  COMPLIANT | 
