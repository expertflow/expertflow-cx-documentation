# CX Knowledgebase : PCI DSS Compliance

The Payment Card Industry Data Security Standard (PCI DSS) provides a baseline of technical and operational requirements designed to protect account data. It is a set of security standards to protect user data and reduce the risk of fraud and data breaches. Expertflow understands the importance of safeguarding sensitive information, especially regarding financial data. This article explains how Expertflow ensures PCI DSS compliance within our system.

PCI DSS Requirements| **Compliance**| **Expertflow CX Compliance**  
---|---|---  
**Build and Maintain a Secure Network and Systems**| |   
  
  1. Install and maintain a firewall configuration to protect cardholder data.

| COMPLIANT | Expertflow CX can be integrated with firewalls.  
  
  2. Do not use vendor-supplied defaults for system passwords and other security parameters.

| COMPLIANT | Passwords are configurable and are backed by password policy.  
**Protect Cardholder Data**| |   
  
  3. Protect stored cardholder data.

| PARTIAL-COMPLIANT | CX message content is encrypted at rest (in case if customer shares payment card information with the agent via messages).Call recordings are also encrypted at rest.Note: Call transcripts don’t eradicate cardholder data if it’s communicated during the call.  
  
  4. Encrypt transmission of cardholder data across open, public networks.

| COMPLIANT | Expertflow CX uses TLS for secure communication. See [Data Encryption](Data-Encryption_884932744.html) for details.  
**Maintain a Vulnerability Management Program**| |   
  
  5. Protect all systems against malware and regularly update antivirus software or programs.

| NOT APPLICABLE | Customer/Partner responsibility  
  
  6. Develop and maintain secure systems and applications.

| COMPLIANT | Different security compliances are applied at various stages of CI. A packaged release is also periodically scanned via a vulnerability scanner, and security patches are released to tackle newly identified vulnerabilities.  
**Implement Strong Access Control Measures**| |   
  
  7. Restrict access to cardholder data by business need to know.

| COMPLIANT | Role-based access controls (RBAC) and group-based access controls (GBAC) are implemented in Expertflow CX so that only authorized Agents can access the application. For more details, see [_Agent Authorization with Agent Desk_](/wiki/pages/createpage.action?spaceKey=SBT&title=Agent%20Authorization%20with%20Agent%20Desk&linkCreation=true&fromPageId=608927784)  
  
  8. Identify and authenticate access to system components.

| COMPLIANT | Same as above.  
  
  9. Restrict physical access to cardholder data.

| NOT APPLICABLE | It’s a partner’s responsibility.  
**Regularly Monitor and Test Networks**| |   
  
  10. Track and monitor all access to network resources and cardholder data.

| NOT APPLICABLE | Customer/Partner responsibility  
11\. Regularly test security systems and processes | COMPLIANT | A packaged release is periodically scanned via a vulnerability scanner. For newly identified vulnerabilities, security maintenance releases are announced.  
12\. Maintain an Information Security Policy. Maintain a policy that addresses information security for all personnel.| COMPLIANT | See [Information Security Policy](https://www.expertflow.com/information-security-policy/).
