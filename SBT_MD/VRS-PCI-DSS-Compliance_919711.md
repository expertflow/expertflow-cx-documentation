# CX Knowledgebase : VRS PCI DSS Compliance

**Compliance**  
| **Compliance Status**  
---|---  
  
#### Password Management

  1. The system should enforce policy for each newly created user, to change immediately the password supplied by the admin at the time of the creation.
  2. Password must be at least 4 and at most 16 characters long. It may contain numbers, characters, symbols and (should contain) a combination of upper and lower case letters. Each new password should start with a character and must have its first letter in uppercase.
  3. Every new/changed password must not be the same as the last 4 (recently set) passwords.
  4. Users should be restricted to a maximum of 4 random login attempts. As soon as it completes the fourth wrong attempt to login into the application, the system should block the user for a certain period. This period may be extended to 30 or 60 mins

|  VRS use KeyCloak for user authentication. All KeyCloak password enforcement policies may be implemented when authenticating the user from KeyCloak. For VRS Cisco integration, the agent-name/password is synchronized with Cisco Finesse. VRS doesn't enforce any password policies in this case.  
  
#### Encrypt transmission of cardholder/caller/user data across open, public networks

  1. Use strong cryptography and security protocols such as SSL/TLS, SSH or IPSec to safeguard sensitive cardholder data during transmission over open, public networks (e.g. Internet, wireless technologies, Global System for Mobile Communications [GSM], General Packet Radio Service [GPRS]).
  2. Encrypt using strong cryptography all non-console administrative access such as browser/web-based management tools.

| Web-based access is secured via SSL.   
  
#### Implement Strong Access Control Measures

  1. Limit access to system components and cardholder data to only those individuals whose job requires such access.
  2. Establish an access control system for systems components with multiple users that restricts access based on a user’s need to know, and is set to “deny all” unless specifically allowed.
  3. Implement two-factor authentication for remote access to the network by employees, administrators, and third parties.
  4. Render all passwords unreadable during storage and transmission, for all system components, by using strong cryptography.
  5. Ensure proper user identification and authentication management.

| 

  1. Role-based security for the VRS users
  2. For the recordings stored on the hard-disk, the system admin needs to protect it from unauthorised access. 
  3. Two-factor authentication with Cisco integration is not tested. 
  4. SSL is used for transport security
  5. User identification is done using 

  
  
  
  
#### Maintain a Vulnerability Management Program

  * Establish a process to identify security vulnerabilities, using reputable outside sources for security vulnerability information, and assign a risk ranking (for example, as “high,” “medium,” or “low”) to newly discovered security vulnerabilities.
  * Develop internal and external software applications (including web-based administrative access to applications) securely, as follows:
    * In accordance with PCI DSS (for example, secure authentication and logging)

| Not scanned  
  
  

