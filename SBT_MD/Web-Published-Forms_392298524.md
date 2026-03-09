# CX Knowledgebase : Web Published Forms

The form builder allows the business to publish forms to a unique URL. One can use these published forms to collect information through web surveys or can embed them within web applications. Every form submission is recorded as a customer experience activity/conversation data.  
  
## **Form Builder**

The Form Builder, a core component of Unified Admin, enables users to create custom forms seamlessly. This tool streamlines business operations by supporting diverse attributes for applications such as CX Surveys, Quality Management Evaluations, Web Widget Conversation Forms, and Agent Desk Wrap-up Forms. The intuitive drag-and-drop interface, real-time previews, and built-in validation enable users to meet specific business needs without requiring technical expertise.

To create a new form, click [here](https://expertflow-docs.atlassian.net/wiki/x/1YGqMw?atlOrigin=eyJpIjoiZjMyNDcyNmEyOGI1NGZkZmFjM2Y5MDFmYTJlZmI3ZjIiLCJwIjoiYyJ9).

Each newly created form has a unique form ID, and based on that, a unique URL for a specific form can be generated, consisting of the following payload.

**Query Param**| **Value Example**| **Description**  
---|---|---  
`formUrl`| `https://<FQDN>/unified-admin`| The FQDN URL to the form page being referenced  
`formId`| `6708d42b6637fa002797c631`| A unique identifier for the form being accessed or filled out.  
`serviceIdentifier`| `1122`| An identifier for a particular channel within the Expertflow system related to this form.  
`channelCustomerIdentifier`| `01234774404`| The customer provides a Customer identifier on a specific channel in the form of a phone number or other unique identifier.  
`conversationId`| `670e04694204bd088cfcb2f5`| A unique conversation ID of the active conversation of the customer.  
`customerId`| `6704f444a0162c4d7ba05900`| A unique identifier for the customer involved in the interaction.  
`channelSessionId`| `670e0468d653273b87e2e993`| A session ID for the customer's interaction within the current channel.  
`type`| `survey`| The type of form being accessed, which in this case is a `survey`  
  
`formUrl` and `formId` are two compulsory query parameters that render a web-published form. The rest are optional and required based on the use cases. 

### Web Published Forms via Short URL APIs

  * Web-published forms can be accessed using either:

    * Traditional (long) URLs with full query parameters, or

    * Simplified **short URLs** for easier sharing and access.

  * **Security checks** are built in to ensure that only authorized users can access and submit forms securely. An **authentication token** is included in the response from the short URL API and is used during form submission.

  * Each short URL has a **configurable expiry time** , managed through `configMaps` in Unified Admin. After this time, the link automatically becomes inactive and cannot be used.

  * Once a user submits the form, the system uses the `isSubmitted` flag to **prevent multiple submissions** for the same interaction. This ensures feedback is collected only once per interaction . After the form is submitted, a submission check is enforced using the `isSubmitted` flag to prevent multiple submissions

  * ⚠️ **Note:** Short URL states (e.g., `isSubmitted`) are currently managed in-memory. If the server restarts or crashes, this data will be lost

  * ⚠️ These security checks, such as one-time submission and link expiration, apply only to short URLs. Long URLs do not have these restrictions.




**NOTE:** The URL for the survey form will be sent in the conversation as per the Bot’s Training and the conditions it has been trained against.

  * The system will send a survey form at the end of the conversation, and customers can access and submit that form by clicking on that URL. 


![image-20241015-110620.png](attachments/392298524/591364172.png?width=283)

  * A form with all its questions will be displayed, which looks like this:


![image-20241028-050839.png](attachments/392298524/625737730.png?width=1027)

Below is the list of different types of questions, and see how they look before and after submission.

**Option Type**| **Before Submission**| **After Submission**  
---|---|---  
**5-Star Rating**| ![image-20241015-083052.png](attachments/392298524/591659014.png?width=457)| ![image-20241015-083301.png](attachments/392298524/591822849.png?width=422)  
**5-Star Rating** **Smiley (filled)**| ![image-20241015-083120.png](attachments/392298524/591364126.png?width=397)| ![image-20241015-083153.png](attachments/392298524/591462437.png?width=467)  
**5-Star Rating** **Smiley (outline)**| ![image-20241015-083238.png](attachments/392298524/590086243.png?width=435)| ![image-20241015-080937.png](attachments/392298524/591298582.png?width=441)  
**5-Star Rating** **Linear Scale**| ![image-20241015-081028.png](attachments/392298524/591298588.png?width=477)| ![image-20241015-081041.png](attachments/392298524/590217318.png?width=477)  
**Rating Bar**| ![image-20241015-080221.png](attachments/392298524/590381147.png?width=477)| ![image-20241015-080238.png](attachments/392298524/591036429.png?width=399)  
**Radio Button**| ![image-20241015-080306.png](attachments/392298524/591560710.png?width=419)| ![image-20241015-080321.png](attachments/392298524/591462421.png?width=333)  
**NPS Type**| ![image-20240718-073535.png](attachments/392298524/393674767.png?width=477)| ![image-20240718-075634.png](attachments/392298524/393379856.png?width=929)  
**INPUT / TEXTAREA Type**| ![image-20241028-051505.png](attachments/392298524/625639436.png?width=493)| ![image-20241028-051505.png](attachments/392298524/625639436.png?width=493)  
  
**Submission Case:**

  * **Success Case:**


![image-20250309-082326.png](attachments/392298524/951550289.png?width=322)

  * **Already Submitted Case:**  



![image-20250804-084259.png](attachments/392298524/1224015879.png?width=351)

  * **Failure Case:**


![image-20250309-082155.png](attachments/392298524/951910413.png?width=337)

#### **Validation Patterns for Questions in Web-Published Forms:**

**Attribute**| **Allowed Pattern**| **Min/Max**  
---|---|---  
AlphaNumeric| Only alphabets and numbers are allowed. Spaces are also permitted.| {1 - 100}  
AlphaNumericSpecial| Only alphabets, numbers, and special characters like `_@.,;:~=*'%$!^/#&+()?{}><|-` are allowed.| {0 - 200}  
Email| A valid email address format is required. It includes letters, numbers, dots, and special characters like `+`, `-`, and `_` followed by `@` and a domain name.Examples:

  1. `john.doe+123@example.com`
  2. `john.doe_123@example.com`

| {0 - 100}  
URL| A valid URL format, including the protocol (`http`, `https`, etc.), domain, and optional paths, parameters, or fragments.Examples:

  1. `https://www.google.com/search?q=openai`
  2. `http://www.wikipedia.org/wiki/Main_Page`

| {0-500}  
IP| Valid IPv4 and IPv6 addresses are allowed. IPv4 addresses consist of four decimal numbers separated by dots, while IPv6 addresses are hexadecimal numbers separated by colons.Examples:

  1. `IPV6 address: 2001:0db8:85a3:0000:0000:8a2e:0370:7334`
  2. `IPV4 address: 192.168.0.1`

| {0-150}  
Number| Allows positive and negative numbers, as well as decimals.| None  
Password| This pattern enforces the following password requirements: 

  1. At least one lowercase letter (a-z)
  2. At least one uppercase letter (A-Z)
  3. At least one digit (0 - 9)
  4. Only allows lowercase letters, uppercase letters, digits, and spaces
  5. Length: The password must be at least 8 characters long and no longer than 256 characters

Examples:

  1. `Password123`
  2. `SecurePass 2024`

| {8 - 256}  
Positive Number| Allows only positive numbers.| None  
Phone Number| Allows only numbers. A `+` sign is optional at the start.

  1. `+123`
  2. `123`
  3. `+123.456`
  4. `123.456`
  5. `.456`
  6. `+92 312 1231234`
  7. `+92-32-1231234`

| None  
Short Answer| Text allowed| {1 - 100}  
Paragraph| Text allowed| {1 - 2000}  
Date| Date Format by default| N/A  
Time| Time Format by default| N/A  
File| N/A| N/A  
Yes No| N/A| N/A  
Multiple Choice Question| N/A| N/A  
Dropdown| N/A| N/A  
5 Star Question| N/A| N/A  
NPS (Net Promotor Score)| N/A| N/A  
  
### Form Data as an Activity

When a form is submitted, it will be stored as an activity in the EFCX system against that specific active or past conversation.

Two possible ways to submit the form:

  * Push Form Data as a third-party activity for past conversations 

  * Push Form Data for active conversations




### Sample Payload of FormData as an Activity:

The `data` field contains the actual form submission data:

  * `id`: Identifier for the form data.

  * `header`: Header information for the form submission, including sender and session details.

  * `body`: The main content of the form submission, including:

    * `type`: Type of data, e.g., `FORM_DATA`.

    * `markdownText`: will always be `null`.

    * `formId`: Unique identifier for the form.

    * `formTitle`: Title of the form, e.g., `PCS Activity Form`.

    * `enableWeightage`: Boolean indicating if weightage is enabled.

    * `enableSections`: Boolean indicating if sections are enabled.

    * `formWeightage`: Overall weightage of the form (if applicable).

    * `sentiment`: Sentiment of the responses (if applicable).

    * `formScore`: Overall score of the form (if application.

    * `additionalDetail`: if applicable, can have additional information as an object, otherwise `null`.

      * `actor`: This defines the actor of the client application

        * `type`: Quality Manager, Evaluator, Customer, Agent, Supervisor, UCCE Ivr Call. 

        * `id`: actor ID

      * `submissionSource`: "Quality Management Review", “Agent Quiz”, "Agent Guidance", “Agent Wrapup”, "Web PCS", "IVR PCS", “Pre-chat", "Chatbot prompt"

      * `review`: Review information can be passed in this object. Currently passing review ID.

        * `id`: review ID.

      * `reviewer`: may be deprecated in the future, as we introduced the actor as an object.

        * `id`: reviewer id 

        * `name`: reviewer name

      * `agentReviewed`: This is being used to push reviewed agent information

        * `id`: agent reviewed id.

        * `name`: agent reviewed name

    * `sections`: Array of sections within the form, each containing:

      * `sectionId`: Unique identifier for the section.

      * `sectionName`: Name of the section.

      * `sectionWeightage`: Weightage of the section (if applicable).

      * `sectionScore`: Score of the section (if applicable).

      * `attributes`: Array of attributes (questions) within the section, each containing:

        * `id`: Unique identifier for the attribute.

        * `label`: Label for the attribute.

        * `valueType`: Type of value, e.g., `boolean`, `nps`, `5-star-rating`.

        * `attributeType`: Type of attribute, e.g., `INPUT`, `OPTIONS`, `TEXTAREA`.

        * `skipType`: Skip type (if applicable).

        * `attributeAttachment`: Attachment associated with the attribute.

        * `attributeScore`: Score of the attribute (if application.

        * `answer`: Array of answers, each containing:

          * `label`: Label for the answer.

          * `value`: Value of the answer.

          * `isSelected`: Boolean value to represent the selected answer. 

          * `additionalAttributes`: Additional attributes for the answer. (if applicable)

            * `optionWeightage`: Weightage of the option (if applicable).

            * `enableStyle`: Boolean indicating if Answer contains styles or not.

            * `optionStyle`: Object containing styles of the option (if applicable, only in case enableStyle is `true`).  
\- `name`: Name of any icon (if applicable).  
\- `type`: Type of any icon (if applicable).  
\- `color`: Color code as a string of any selected option, like `NPS,` eg, `#00000`.   
\- `media`: U`RL` of the icon of any selected option, eg, `https://xyz.com/file-server/xyz.png`



