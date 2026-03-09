# CX Knowledgebase : Application Security

Application Security (AppSec) is a critical component of our software development lifecycle (SDLC) to protect Expertflow CX application from threats and vulnerabilities. This page outlines the principles, policies, and best practices we follow to ensure our applications are protected against security threats and vulnerabilities.

  * Why - what business value would this feature/implementation give? What would be the benefit? Directly linked to the painpoint of your customer

  * What - What are you doing to achieve that business value? This is about product description, capabilities in very simple language without using any bloated terms. 

  * How - Configuration guides, technologies used, solution architecture, technical workflow steps




## CX Core

### Encryption at rest for CX Messages

From CX4.10 onwards, all message content processed within Expertflow is being encrypted using the AES-256 algorithm. For more details, please visit the [Data Encryption](Data-Encryption_884932744.html) section.

### PII data masking for Application logs

For enhanced security, the Customer’s PII (Personally Identifiable Information) is redacted from application logs. For more details, please visit the [PII Data Masking](PII-Data-Masking_884113585.html) section.

### Cross-site scripting (XSS) attack prevention

To mitigate the risk of Cross-Site Scripting (XSS) attacks, all user-generated data originating from customer widgets, such as pre-chat forms and message content, is securely encoded at the Web Channel Manager level (websocket server). This ensures that potentially malicious inputs (e.g, `<script>`) are safely converted to their HTML-encoded equivalents (e.g., `&lt;script&gt;`). This encoding is applied at both receiving and sending points to ensure comprehensive protection against XSS vulnerabilities.

## AgentDesk

### PII data masking for Customer Attributes

For enhancing customer privacy, the Customer’s PII (Personally Identifiable Information) has been masked for the Junior Agent Role in the AgentDesk application. For more details, please visit the [PII Data Masking](PII-Data-Masking_884113585.html) section.

## Customer Web Widget

### Secure Transcript URL

To download the chat transcript, a URL is generated at the end of each chat session. From CX4.10, we have improved the URL’s structure to enhance the protection of PII and prevent unauthorized access to customer metadata via shared URLs. This aligns with privacy-first design standards and secure data handling practices.

## Voice Recording

### Encryption at rest for voice recording

### Pause and resume voice recording
