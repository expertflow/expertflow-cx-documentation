# CX Knowledgebase : Guide for Standard Tier Upgrade

## **Introduction**

This document outlines the steps required to upgrade your LinkedIn application from the Development Tier to the Standard Tier, enabling access to advanced features of the Community Management API. This guide is intended for developers and administrators responsible for managing LinkedIn integrations within their organisation.

The Standard Tier approval process involves completing a detailed access request form through the LinkedIn Developer Portal, supported by documentation and a use case demonstration.

You must have an existing LinkedIn application with Development Tier access and a verified LinkedIn Page before proceeding with this guide.

## Access the Community Management Upgrade Form

  1. Log in to the [LinkedIn Developer Portal](https://www.linkedin.com/developers).

  2. Navigate to your application and go to the Products tab.

  3. Click Upgrade options under Community Management API.

  4. Start completing the Upgrade Request Form.




### Step 1: Company Information

  * Enter your company’s legal name (include any alternative or registered names if applicable).

  * Provide your official company website.


![image-20250220-082258.png](attachments/911343642/911016002.png?width=800)

### Step 2: Registered Address

  * Fill in the following fields:

    * Street Address

    * City

    * State/Province

    * Zip/Postal Code

    * Country


![image-20250220-082607.png](attachments/911343642/910590833.png?width=800)

### Step 3: Existing Tier Access

  * Check Yes if your company already has Standard Tier access for any other LinkedIn applications.


![image-20250220-082834.png](attachments/911343642/911081599.png?width=800)

### Step 4: Primary Use Case

  * Select:  
Platform: To integrate LinkedIn into an externalized self-service SaaS platform

  * Write the company description in the text field (sample given):


![image-20250220-083222.png](attachments/911343642/911343672.png?width=800)

  * **For Use Cases Enabled, select** :

    * Page Management: Create and manage company posts, comments, reactions, and monitor engagement.

    * Page Analytics: Track post analytics and performance.


![image-20250220-083420.png](attachments/911343642/911147093.png?width=800)

  * copy paste the following in the use case description




![](images/icons/grey_arrow_down.png)use case description

## Application Flow 

**Post Creation & Engagement:** An admin posts content on LinkedIn, prompting user interactions.

**Real-Time Detection:** The LinkedIn Connector detects new comments and triggers a chat session with an agent via ExpertFlow EFCX.

**Agent Response:** The agent replies within EFCX. This response can be Reply To a Comment React to a Comment, or Delete a Comment. This response is posted back to LinkedIn through the API.

**Traceability & Reporting:** The conversation is logged with a reason code for analytics and performance tracking.

## Authentication & Deployment 

The connector is deployed on Kubernetes. OAuth 2.0 tokens are manually generated via the LinkedIn Developer Portal and stored in Connector Config Maps. 

Token renewal currently requires manual intervention by support personnel.

## Data Management

The connector tracks the Post ID and total comment count to detect new interactions. When a new comment is detected, it captures and passes the Post ID, Comment ID, and Comment Text to EFCX for processing. Once a response is formulated, it is posted back to LinkedIn using the LinkedIn Comment to post a reply on the LinkedIn page.

### Step 5: Customer Information

Answer the following:

  * Where are most of your customers based?

  * How many clients use the product being integrated with the Community Management API?

  * What category best describes your primary customers?

  * If your product supports managing individual profiles:

    * Check **Others** , and enter **N/A**


![image-20250220-090734.png](attachments/911343642/911147202.png?width=800)

  * What industries are most common among your customers? 




### Step 6: Privacy and Compliance

  * Paste the ExpertFlow privacy policy link into the designated box: <https://www.expertflow.com/privacy-policy/>


![image-20250220-090707.png](attachments/911343642/911769605.png?width=800)

Answer the compliance questions as follows:

  * Does your organization have a person/team (internal or external) responsible for compliance with applicable privacy regulations and industry-standard privacy practices? → **Yes**

  * Does your organization have the capability to securely delete all data obtained via our Community Management APIs if required by LinkedIn? **→ YES**

  * Is personal data (including profile data or activity data) obtained via our Community Management APIs used for advertising or sales use cases? → **NO**

  * Is personal data (including profile data or activity data) obtained via our Community Management APIs for the purpose of managing a specific customer’s page shared with other customers? →**NO**

  * Do you have partnerships with any other platforms? → Select **Facebook, Twitter and other.**




### **Step 7: Provide Demonstration Details**

  * Upload a video showing your application’s functionality. [Demo Video](https://drive.google.com/file/d/1yzYD11sZHBYOqnuWpbh8CB8aIo39gzKj/view?usp=sharing)

  * Please provide test login details (uname/pwd) and a link to the product/service you’re integrating the Community Management APIs with




![](images/icons/grey_arrow_down.png)AgentDesk details

[https://<fqdn>/unified-agent/#/login](https://fnbdemo.expertflow.com/unified-agent/#/login)  
username: linkedinuser  
password: v1!6BDh69i5V

![image-20250220-091430.png](attachments/911343642/911343833.png?width=800)

### **Step 8: Final Review and Submission**

  * Review the form to ensure all information is correct.

  * Once complete, click **Submit** to initiate the review process.




  * They always send a confirmation email from [developer-access@linkedin.com](mailto:developer-access@linkedin.com) asking for a walkthrough video with English commentary, after you have requested for the standard tier. Same details you have provided in the form need to be passed in the email.

  * Keep monitoring the emails as they can ask explanation on some user case handling in your application.



