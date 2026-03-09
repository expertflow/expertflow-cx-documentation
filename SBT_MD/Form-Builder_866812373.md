# CX Knowledgebase : Form Builder

Enables business administrators with comprehensive control over form creation, management, and utilization. This offers flexible options to introduce new question types, structure content using sections, and assign weighted scoring to responses, which elevates both user experience and the depth of data insights. 

## **Form types are deprecated.**

There will be no form types available in the form builder from now onward. A form that is created will have no specific type and can be used in any case (pre-chat, survey, quality management).

  * Form Type is deprecated from **CX4.10** and subsequent releases




The screenshot below provides a clear view of the redesigned form UI. 

![image-20250611-111009.png](attachments/866812373/1136033987.png?width=800)

Refer to the [user guide](Form-Builder-User-Guide_946602145.html) for detailed instructions on how to utilize the form.

## Form Key Structures

**Sections**| 

  * Allow adding multiple sections

  
---|---  
**Questions (Attributes)**| 

  * **INPUT**
    * **alphaNumeric**(Alpha Numeric Character)
    * **alphaNumericSpecial** (Alpha Numeric Special Character)
    * **email** (Email)
    * **number** (Number)
    * **phoneNumber**(Phone Number)
    * **password** (Password)
    * **positiveNumber** (Positive Number)
    * **url** (URL)
    * **IP** (IP address with or without port)
    * **date** (Date)
    * **time** (Time)
    * **dateTime** (DateTime)
    * **shortAnswer** (Short Sentence)
    * **file** (Media File)
  * **OPTIONS**
    * **boolean** (Yes/No) → Single Select
    * **mcqs** (Multiple Choice) → Single Select
    * **checkbox** (Checkboxes) → Multiple Select
    * **dropdown** (Dropdown) → Single Select
    * **5-star-rating** (5 Star Rating) → Single Select
    * **nps** (Net Promotor Score) → Single Select
  * **TEXTAREA**
    * **paragraph** (Long Sentences)

  
**Weightage**| 

  * Questionnaire weightage formula being used on section to question level =>, for example, if the section is assigned 50 weightage and the question is assigned 30 weightage, then the formula will look like: “ 30/100 * 50 ”

![](images/icons/grey_arrow_down.png)Sample Weighted Form:

  * Form → [**100**] ← Form Weightage
    * Section 1 → [**30**] ← Section Weightage
      * Question 1 → [**20**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 5 → [**0**] ← Option Weightage
      * Question 2 → [**40**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**0**] ← Option Weightage
      * Question 3 → [**40**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 3 → [**0**] ← Option Weightage
    * Section 2 → [**40**] ← Section Weightage
      * Question 1 → [**50**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 3 → [**0**] ← Option Weightage
      * Question 2 → [**50**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 3 → [**0**] ← Option Weightage
    * Section 3 → [**30**] ← Section Weightage
      * Question 1 → [**30**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 3 → [**0**] ← Option Weightage
      * Question 2 → [**30**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 3 → [**0**] ← Option Weightage
      * Question 3 → [**40**] ← Question Weightage
        * Option 1 → [**100**] ← Option Weightage
        * Option 2 → [**50**] ← Option Weightage
        * Option 3 → [**0**] ← Option Weightage

  
**Question (Attribute) Level Weightage**| (Allowed only on MCQ and Dropdown Type Questions)

  1. Allow businesses to set weightage from the form level to the question’s option level.
  2. Weightage values range from 0% to 100%
  3. Weightage only applies to Multiple Choice (MCQs) and Dropdown (dropdown) type questions.

  
**Max Character Limits**| 

  * Form Title: **500**
  * Form Description: **1000**
  * Section Name: **500**
  * Section Description: **500**
  * Attribute Label: **500**
  * Attribute Helping Text: **100**
  * Category Label: **500**
  * Option Label: **500**

  
**P rompts in Question (Attribute)**| 

  * **Audio File Attachments for Question Prompts**
    * Against each question, one can add Audio-type file attachments to allow businesses to fulfill IVR prompt use cases.
    * The maximum file limit is 5MB
    * File Engine Supported audio file type: mp3.

  
  
## Form Builder Restrictions

**Sections**|  By default, sections will be disabled, but can be enabled. In case of the weighted form section is automatically enabled.  
---|---  
**Weightage**|  By default, disabled, but it can be enabled.

  * Given weightage will only apply for single select MCQs/Dropdown type questions (weightage calculation will only apply to these), and should be fine if enabled.
  * When weightage is enabled, only multiple-choice and Dropdown value types are allowed.

  
**Multiple Choice Categories**|  Enabled by default, can be disabled. Only available for checkbox-type questions.  
**Single Select**|  Single Select only applies to MCQs/Dropdown-type questions.  
**Multiple Select**|  Multiple Select only applies to Checkbox-type questions.  
  
## Questions (Attributes)

A detailed schema for all possible questions in a form with screenshots is available.

**Value Type (Question)**| **Attribute Type (HTML)**| **Question (Attribute) Schema**| **Question (Attribute) Screenshots**  
---|---|---|---  
  
  * **alphaNumeric**
  * **alphaNumericSpecial**
  * **email**
  * **number**
  * **phoneNumber**
  * **password**
  * **positiveNumber**
  * **url**
  * **ip**
  * **date**
  * **time**
  * **dateTime**
  * **shortAnswer**

|  INPUT| ![](images/icons/grey_arrow_down.png)All Input Sample Schema
[code] 
    {
        "_id": "65cc566711819b00328db0a9",  // String (ObjectId)
        "attributeType": "INPUT",  // String (Field type)
        "helpText": "Enter AlphaNumeric Text Here ..",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "what_is_your_name?",  // String (Unique key for the attribute)
        "label": "What is your name?",  // String (Label for the attribute)
        "valueType": "alphaNumeric",  // String (Value type which will be added by customer)
        "attributeWeightage": 10,  // Number (Overall attribute weightage for the question)
        "attributeAttachment": "https://file-server.expertflow.com/xyz"  // String (Optional media file to be attached)
    }
[/code]

| ![image-20250206-111648.png](attachments/866812373/866714770.png?width=484)  
**file** (file upload)| INPUT| ![](images/icons/grey_arrow_down.png)Input File Type Sample Schema
[code] 
    {
        "_id": "65cc566711819b00328db0a9",  // String (ObjectId)
        "attributeType": "INPUT",  // String (Field type)
        "helpText": "Enter AlphaNumeric Text Here ..",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "what_is_your_name?",  // String (Unique key for the attribute)
        "label": "What is your name?",  // String (Label for the attribute)
        "valueType": "file",  // String (Value type which will be added by customer)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String (Optional media file to be attached)
        "fileData": {
            "restrictFile": true,  // Boolean (If set to false then no file type validation will be done)
            "fileExtension": ["PNG", "JPG", "JPEG", "DOC", "MOV", "MP3"],  // Array of Strings (Allowed file extensions)
            "fileNumber": 5,  // Number (Maximum 10 and minimum 1)
            "fileSize": 5,  // Number (in MB)
            "destinationFolder": "https://file-server.expertflow.com/file/"  // String (Destination folder for the file)
        }
    }
[/code]

| ![image-20250206-111719.png](attachments/866812373/866943497.png?width=644)  
**paragraph**|  TEXTAREA| ![](images/icons/grey_arrow_down.png)Paragraph Sample Schema
[code] 
    {
        "_id": "65cc566711819b00328db0a9",  // String (ObjectId)
        "attributeType": "TEXTAREA",  // String (Field type)
        "helpText": "Enter Paragraph Text Here ..",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "what_is_your_name?",  // String (Unique key for the attribute)
        "label": "What is your name?",  // String (Label for the attribute)
        "valueType": "paragraph",  // String (Value type which will be added by customer)
        "attributeAttachment": "https://file-server.expertflow.com/xyz"  // String (Optional media file to be attached)
    }
[/code]

| ![image-20250206-111742.png](attachments/866812373/867401851.png?width=644)  
**boolean** (Yes/No)| OPTIONS| ![](images/icons/grey_arrow_down.png)Boolean Sample Schema
[code] 
    {
        "_id": "65dc26ba07c232003325b8bf",  // String (ObjectId)
        "attributeType": "OPTIONS",  // String (Field type)
        "helpText": "Enter Customer Type Here...",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "customer_type",  // String (Unique key for the attribute)
        "label": "Customer Type",  // String (Label for the attribute)
        "valueType": "boolean",  // String (Boolean, YES/NO Question valueType)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String (Optional Media File to be attached)
        "attributeWeightage": null,  // Null or Number (Overall attributeWeightage will be null or 0 in case of boolean)
        "attributeOptions": {
            "enableCategory": false,  // Boolean
            "enableStyle": true,  // Boolean (Assuming style can be enabled for boolean)
            "reverseOrder": false,  // Boolean (If 'true' attributeData will be in reversed order)
            "isMultipleChoice": false,  // Boolean (will be false in case of boolean)
            "attributeData": [
                {
                    "label": "Label Name",  // String
                    "values": [
                        {
                            "label": "Yes",  // String
                            "value": true,  // Boolean
                            "optionStyle": {
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": null  // String
                            },
                            "optionWeightage": null  // Null or Number (weightage will be null or 0 in case of boolean)
                        },
                        {
                            "label": "No",  // String
                            "value": false,  // Boolean
                            "optionStyle": {
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": null  // String
                            },
                            "optionWeightage": null  // Null or Number (weightage will be null or 0 in case of boolean)
                        }
                    ]
                }
            ]
        }
    }
[/code]

| ![image-20250206-111815.png](attachments/866812373/867565674.png?width=644)  
**mcqs** (Multiple Choice → Single Select)| OPTIONS| ![](images/icons/grey_arrow_down.png)Multiple Choice Sample Schema
[code] 
    {
        "_id": "65dc26ba07c232003325b8bf",  // String (ObjectId)
        "attributeType": "OPTIONS",  // String (Field type)
        "helpText": "Enter Customer Type Here...",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "customer_type",  // String (Unique key for the attribute)
        "label": "Customer Type",  // String (Label for the attribute)
        "valueType": "mcq",  // String (Multiple Choice, Single Select)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String or Null (Optional Media File to be attached otherwise "null")
        "attributeWeightage": 10,  // Number (Overall attributeWeightage for the question)
        "attributeOptions": {
            "enableCategory": false,  // Boolean (In case of MCQ type question, category can be enabled)
            "enableStyle": false,  // Boolean (Emojis cannot be enabled for mcq)
            "reverseOrder": false,  // Boolean (Reverse Order cannot be 'true' in case of mcq type question)
            "isMultipleChoice": false,  // Boolean (will be false in case of mcq)
            "attributeData": [
                {
                    "label": "Label Name",  // String
                    "values": [
                        {
                            "label": "One",  // String
                            "value": null,  // Null (value is not specified for mcq options)
                            "optionStyle": null,  // It may be Null or Object with keys value null in it
                            "optionWeightage": 10  // Number (weightage can be enabled in case of mcq)
                        },
                        {
                            "label": "Two",  // String
                            "value": null,  // Null (value is not specified for mcq options)
                            "optionStyle": null,  // It may be Null or Object with keys value null in it
                            "optionWeightage": 10  // Number (weightage can be enabled in case of mcq)
                        }
                        // More objects can be added here
                    ]
                }
                // More objects will only be added in case of 'enableCategory' is 'true'
            ]
        }
    }
[/code]

| ![image-20250206-111832.png](attachments/866812373/867008900.png?width=644)  
**checkbox** (Multi-Select)| OPTIONS| ![](images/icons/grey_arrow_down.png)Checkboxes Sample Schema
[code] 
     {
        "_id": "65dc26ba07c232003325b8bf",  // String (ObjectId)
        "attributeType": "OPTIONS",  // String (Field type)
        "helpText": "Enter Customer Type Here...",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "customer_type",  // String (Unique key for the attribute)
        "label": "Customer Type",  // String (Label for the attribute)
        "valueType": "checkbox",  // String (checkbox)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String or Null (Optional Media File to be attached otherwise "null")
        "attributeWeightage": null,  // Null or Number (Overall attributeWeightage for the question type checkboxes will be 'null' or 0)
        "attributeOptions": {
            "enableCategory": false,  // Boolean (In case of checkbox type question, category can be enabled)
            "enableStyle": false,  // Boolean (Emojis cannot be enabled for checkbox)
            "reverseOrder": false,  // Boolean (Reverse Order cannot be 'true' in case of checkbox type question)
            "isMultipleChoice": true,  // Boolean (will be true in case of checkbox)
            "attributeData": [
                {
                    "label": "Label Name",  // String
                    "values": [ 
                        {
                            "label": "One",  // String
                            "value": null,  // Null (value is not specified for checkbox options)
                            "optionStyle": null,  // It may be Null or Object with keys value null in it  
                            "optionWeightage": null  // Null or Number (weightage for checkbox options)
                        },
                        {
                            "label": "Two",  // String
                            "value": null,  // Null (value is not specified for checkbox options)
                            "optionStyle": null,  // It may be Null or Object with keys value null in it
                            "optionWeightage": null  // Null or Number (weightage for checkbox options)
                        }
                        // More objects can be added here
                    ]
                }
                // More objects will only be added in case 'enableCategory' is 'true'
            ]
        }
    }
[/code]

| ![image-20250206-111858.png](attachments/866812373/867434599.png?width=644)  
**dropdown** (Multiple Choice → Single Select)| OPTIONS| ![](images/icons/grey_arrow_down.png)Dropdown Sample Schema
[code] 
    {
        "_id": "65dc26ba07c232003325b8bf",  // String (ObjectId)
        "attributeType": "OPTIONS",  // String (Field type)
        "helpText": "Enter Customer Type Here...",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "customer_type",  // String (Unique key for the attribute)
        "label": "Customer Type",  // String (Label for the attribute)
        "valueType": "dropdown",  // String (dropdown)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String or Null (Optional Media File to be attached otherwise "null")
        "attributeWeightage": 10,  // Number (Overall attributeWeightage for the question)
        "attributeOptions": {
            "enableCategory": false,  // Boolean (In case of Dropdown type question, category can be enabled)
            "enableStyle": false,  // Boolean (Emojis cannot be enabled for dropdown)
            "reverseOrder": false,  // Boolean (Reverse Order cannot be 'true' in case of dropdown type question)
            "isMultipleChoice": false,  // Boolean (will be false in case of dropdown)
            "attributeData": [
                {
                    "label": "Label Name",  // String
                    "values": [
                        {
                            "label": "One",  // String
                            "value": null,  // Null (value is not specified for dropdown options)
                            "optionStyle": null,  //  It may be Null or Object with keys value null in it 
                            "optionWeightage": 10  // Number (weightage can be enabled in case of mcq)
                        },
                        {
                            "label": "Two",  // String
                            "value": null,  // Null (value is not specified for dropdown options)
                            "optionStyle": null,  //  It may be Null or Object with keys value null in it 
                            "optionWeightage": 10  // Number (weightage can be enabled in case of mcq)
                        }
                        // More objects can be added here
                    ]
                }
            ]
        }
    }
[/code]

| ![image-20250206-111917.png](attachments/866812373/866780047.png?width=644)  
**5-star-rating** (5-Star Rating)| OPTIONS| ![](images/icons/grey_arrow_down.png)5 Star Rating Sample Schema
[code] 
    {
        "_id": "65dc26ba07c232003325b8bf",  // String (ObjectId)
        "attributeType": "OPTIONS",  // String (Field type)
        "helpText": "Enter Customer Type Here...",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "customer_type",  // String (Unique key for the attribute)
        "label": "Customer Type",  // String (Label for the attribute)
        "valueType": "5-star-rating",  // String (5-star-rating)
        "attributeWeightage": 10,  // Number (Overall attributeWeightage for the question)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String or Null (Optional Media File to be attached otherwise "null")
        "attributeOptions": {
            "enableCategory": false,  // Boolean (In case of Dropdown type question, category can be enabled)
            "enableStyle": true,  // Boolean (Emojis can not be enabled for dropdown)
            "reverseOrder": false,  // Boolean (Reverse Order can be 'true' in case of rating type question)
            "isMultipleChoice": false,  // Boolean (will be false in case of dropdown)
            "attributeData": [
                {
                    "label": "Label Name",  // String
                    "values": [
                        {
                            "label": "Very Dissatisfied",  // String
                            "value": 1,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null (weightage can be null)
                        },
                        {
                            "label": "Dissatisfied",  // String
                            "value": 2,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null (weightage can be null)
                        },
                        {
                            "label": "Neutral",  // String
                            "value": 3,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null (weightage can be null)
                        },
                        {
                            "label": "Satisfied",  // String
                            "value": 4,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null (weightage can be null)
                        },
                        {
                            "label": "Very Satisfied",  // String
                            "value": 5,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": "https://cx-frontend.expertflow.com/unified-admin/assets/images/form-assets/emoticon-filled-1.svg",  // String
                                "type": "filled",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null (weightage can be null)
                        }
                    ]
                }
            ]
        }
    }
[/code]

| ![image-20250206-111940.png](attachments/866812373/866714777.png?width=644)  
**nps** → (Net Promoter Score)| OPTIONS| ![](images/icons/grey_arrow_down.png)NPS Sample Schema
[code] 
    {
        "_id": "65dc26ba07c232003325b8bf",  // String (ObjectId)
        "attributeType": "OPTIONS",  // String (Field type)
        "helpText": "Enter Customer Type Here...",  // String (Placeholder of field)
        "isRequired": true,  // Boolean (Check if field is required or not)
        "key": "customer_type",  // String (Unique key for the attribute)
        "label": "Customer Type",  // String (Label for the attribute)
        "valueType": "nps",  // String (Boolean, checkbox, mcq, dropdown, rating, nps)
        "attributeWeightage": 10,  // Number (Overall attributeWeightage for the question)
        "attributeAttachment": "https://file-server.expertflow.com/xyz",  // String or Null (Optional Media File to be attached otherwise "null")
        "attributeOptions": {
            "enableCategory": false,  // Boolean
            "enableStyle": false,  //Boolean
            "reverseOrder": false, //Boolean
            "isMultipleChoice": false,  // Boolean (Only true in case of checkboxes)
            "attributeData": [
                {
                    "label": "",  // String
                    "values": [
                        {
                            "label": "Very Dissatisfied",  // String
                            "value": 0,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 1,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 2,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 3,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 4,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 5,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 6,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 7,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 8,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 9,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        },
                        {
                            "label": "",  // String
                            "value": 10,  // Number
                            "optionStyle": {  // Object
                                "name": "Filled Smile",  // String
                                "media": null,  // String
                                "type": "nps",  // String
                                "color": "#ffffff"  // String
                            },
                            "optionWeightage": null  // Null or Number
                        }
                    ]
                }
            ]
        }
    }
[/code]

| ![image-20250206-112020.png](attachments/866812373/867074381.png?width=644)  
  
## Form Schema
[code] 
    {
        "id": "65b248c710e57100322c5f88",
        "state": "unpublished",
        "formTitle": "Form Builder",
        "formDescription": "",
        "enableSections": true,
        "enableWeightage": false,
        "section": 
          [
            {
              "sectionName": "Section Name",
              "sectionKey": "section_name",
              "sectionWeightage": 100,
              "attributes": 
                [
                  // ALL INPUT AND TEXTAREA AND OPTIONS TYPE QUESTIONS LEGAL in this FORM
                ]
            }
         ]
    }
[/code]

## Impacts of Form Type Removal

| **Impact Area**| **Details**  
---|---|---  
1| **Form Types**| 

  * Form types removed.- No restrictions on selecting question types.
  * Generic forms support all question types.

  
2| **Mixed Questions**| 

  * Forms can include both weighted and non-weighted questions.
  * Single-select types (MCQs, dropdowns) can have optional weightage.

  
3| **Section Behavior**| 

  * New forms start with no sections.
  * When adding a section: 
    * Two sections are created. 
    * Existing questions go to the first section.
    * The second section is empty.

  
4| **Weighted Form Behavior**| 

  * Forms are non-weighted by default.
  * Enabling weightage: 
    * Two sections are created.
    * Existing questions move to the first section.
    * The second section is empty.

  
5| **General Impact**| 

  * Features previously dependent on form types will be affected.

  
6| **Web-Published Forms**| 

  * All question types are supported.
  * Mixed forms are supported.
  * If weightage is enabled:
    * Scores are computed.
    * Non-weighted questions score 0.

  
7| **Customer Widget**| 

  * Supports all question types and sections.
  * Weighted forms are allowed, but score calculations are **not** considered.

  
8| **Pre-Chat Form (Web Channel)**| 

  * In multi-section forms:
    * All questions are extracted and sent as key-value pairs.
    * Sections are not preserved.

  
9| **QM Forms**| 

  * Support all question types and sections.
  * Mixed forms are allowed.
  * Non-weighted questions get a score of 0.

  
10| **Wrap-Up Form**| 

  * Auto-created on first launch.
  * Cannot be deleted, but can be edited.
  * Only supports: 
    * Checkboxes, 
    * MCQs, 
    * Dropdowns.
  * Strictly non-weighted.
  * No sections allowed.

  
  
## Upgrade Form Schema to New Forms 

This update applies to **CX4.10** and all subsequent releases.

**Script# 1: Remove formType.**  
**Purpose:** Removes the formType field from all documents in a collection.  
**Usage:** This aligns the documents with the new, more generic schema.
[code] 
    const connection_string = "string_to_replace";
    
    db = connect(connection_string);
    
    function updateFormSchema() {
        const result = db.getCollection('forms').updateMany(
          { "formType": { "$exists": true } },
          { "$unset": { "formType": "" } }
        );
        console.log(`${result.modifiedCount} documents have been updated.`);
    }
    
    updateFormSchema();
[/code]

## Downgrade Form Schema to Old Forms

**Script# 2: Add formType: “Generic”.**  
**Purpose:** Adds formType: "Generic" to all documents where it does not already exist.  
**Usage:** This is for reverting documents to a schema structure that expects a formType.
[code] 
    const connection_string = "string_to_replace";
    
    db = connect(connection_string);
    
    function updateFormSchema() {
        const result = db.getCollection('forms').updateMany(
          { "formType": { "$exists": false } },
          { "$set": { "formType": "Generic" } }
        );
        console.log(`${result.modifiedCount} documents have been updated.`);
    }
    
    updateFormSchema();
[/code]

**Note:** Use the mongo shell terminal to execute the upgrade/downgrade commands. Replace the connection string with the actual one.

## Introducing New APIs in Form Builder 

### **Multi-level Pagination for Form Schema API**

This update applies to **CX4.10.3** and all subsequent releases.

Introduces **multi-level pagination** in the Form Schema API to optimize performance when handling large forms. Instead of returning the complete nested form structure in a single response, the API now supports incremental loading through four dedicated paginated endpoints

#### 1\. Paginate Sections in a Form

**Endpoint:**
[code] 
    GET {{unifiedAdminUrl}}/forms/paginatedForm/{formId}?level=sections&page=1&limit=10
[/code]

**Response:** Returns a paginated list of sections with metadata. Each section includes a `totalAttributes` count instead of the full attribute array.
[code] 
    {
        "metadata": {
            "totalSections": 2,
            "currentPage": 1,
            "totalPages": 1,
            "hasMore": false
        },
        "sections": [
            {
                "_sectionIndex": 0,
                "_id": "68c1571060b5643e7b8462e9",
                "sectionName": "New Section112",
                "sectionDescription": "",
                "totalAttributes": 1
            },
            {
                "_sectionIndex": 1,
                "_id": "68c1576d60b5643e7b846313",
                "sectionName": "New Section 2",
                "sectionDescription": "",
                "totalAttributes": 5
            }
        ]
    }
[/code]

#### 2\. Paginate Attributes within a Section

**Endpoint:**
[code] 
    GET {{unifiedAdminUrl}}/forms/paginatedForm/{formId}?level=attributes&sectionIndex=0&page=1&limit=10
[/code]

**Response:** Returns a paginated list of attributes for the given section. Each attribute includes a `totalCategories` count instead of the full category array.
[code] 
    {
        "metadata": {
            "totalAttributes": 1,
            "currentPage": 1,
            "totalPages": 1,
            "hasMore": false
        },
        "attributes": [
            {
                "_attributeIndex": 0,
                "_id": "68c1577e60b5643e7b84632a",
                "label": "New Question2",
                "key": "new_question2",
                "attributeType": "INPUT",
                "valueType": "email",
                "isRequired": true,
                "helpText": "",
                "attributeWeightage": null,
                "totalCategories": 0
            }
        ]
    }
[/code]

#### 3\. Paginate Categories within an Attribute

**Endpoint:**
[code] 
    GET {{unifiedAdminUrl}}/forms/paginatedForm/{formId}?level=categories&sectionIndex=0&attributeIndex=0&page=1&limit=5
[/code]

**Response:** Returns a paginated list of categories for the given attribute. Each category includes `_categoryIndex` and `totalOptions`.
[code] 
    {
        "metadata": {
            "totalCategories": 6,
            "currentPage": 1,
            "totalPages": 3,
            "hasMore": true
        },
        "categories": [
            {
                "_categoryIndex": 0,
                "label": "Billing Issues",
                "totalOptions": 3
            },
            {
                "_categoryIndex": 1,
                "label": "Technical Support",
                "totalOptions": 3
            }
        ]
    }
[/code]

#### 4\. Paginate Options within a Category

**Endpoint:**
[code] 
    GET {{unifiedAdminUrl}}/forms/paginatedForm/{formId}?level=options&sectionIndex=0&attributeIndex=0&categoryIndex=0&page=1&limit=25
[/code]

**Response:** Returns a paginated list of options for the given category along with metadata.
[code] 
    {
        "metadata": {
            "totalOptions": 3,
            "currentPage": 1,
            "totalPages": 3,
            "hasMore": true
        },
        "options": [
            {
                "label": "Incorrect Invoice",
                "value": null,
                "optionWeightage": null,
                "optionStyle": {
                    "color": null,
                    "media": null,
                    "name": null,
                    "type": null
                },
                "_optionIndex": 0
            }
        ]
    }
[/code]

## **Search Capability in Wrap-up Form**

This update applies to **CX4.10.3** and all subsequent releases.

Allows agents to **search wrap-up codes (wrapcodes)** within a form using a keyword. Instead of scrolling through long lists of codes, agents can type into a search bar and instantly filter the available wrapcodes. This improves **efficiency, accuracy, and reduces Average Handle Time (AHT)**.

**Endpoint:**
[code] 
    GET {{unifiedAdminUrl}}/wrapupSearch/{formId}?q=<keyword>&sectionIndex=<number>&attributeIndex=<number>&page=<number>&limit=<number>
[/code]

**Path Parameter**

  * `formId` → Unique ID of the form.




**Query Parameters**

  * `q` → Keyword to search wrap codes (case-insensitive).

  * `sectionIndex` → Index of the section in the form schema.

  * `attributeIndex` → Index of the attribute inside the section.

  * `page` → Current page number for pagination.

  * `limit` → Maximum number of wrap codes per page (default/recommended: 20)

  * 
[code]{
            "metadata": {
                "totalMatches": 1,
                "currentPage": 1,
                "totalPages": 1,
                "hasMore": false
            },
            "attributeOptions": {
                "enableCategory": true,
                "isMultipleChoice": true
            },
            "results": [
                {
                    "categoryName": "Feedback/Complaint",
                    "label": "Suggestion for Improvement",
                    "value": null,
                    "optionWeightage": null,
                    "optionStyle": {
                        "name": null,
                        "type": null,
                        "color": null,
                        "media": null
                    },
                    "display": "Suggestion for Improvement",
                    "_indices": {
                        "sectionIndex": 0,
                        "attributeIndex": 0,
                        "categoryIndex": 4,
                        "optionIndex": 2
                    }
                }
            ]
        }
[/code]




## **Partial Updates for Form Schema (HTTP PATCH)**

This update applies to **CX4.10.3** and all subsequent releases.

Introduces **partial updates** for form schemas using the HTTP **PATCH** method. Instead of sending the full form object (via `PUT`), clients can now update only the specific fields that need modification.

This approach provides:

  * **Efficiency** : Only the changed data is sent, reducing payload size and bandwidth.

  * **Lower Server Load** : The server processes smaller updates instead of entire form documents.




**Endpoint** :
[code] 
    PATCH {{unifiedAdminUrl}}/forms/{formId}
[/code]

**Path Parameter**

  * `formId` → Unique ID of the form to update.




**Request Body (Patch Operations Array)**  
Each operation follows the structure inspired by JSON Patch (RFC 6902).

  * `op` → The operation to perform (`add`, `replace`, or `remove`).

  * `path` → JSON Pointer string that specifies the target field.

  * `value` → The new value (only required for `add` and `replace`).




## Example Patch Payloads

### 1\. Replace a Form Title
[code] 
    [
      { "op": "replace", "path": "/formTitle", "value": "New Updated Form Title" }
    ]
[/code]

### 2\. Add a New Attribute to the First Section
[code] 
    [
      {
        "op": "add",
        "path": "/sections/0/attributes/-",
        "value": {
          "label": "New Question",
          "key": "new_question",
          "attributeOptions": { "attributeData": [] }
        }
      }
    ]
[/code]

### **3\. Remove the Second Option from the First Category of the First Attribute**
[code] 
    [
      {
        "op": "remove",
        "path": "/sections/0/attributes/0/attributeOptions/attributeData/0/values/1"
      }
    ]
[/code]

**Sample Response :**
[code] 
    {
        "message": "Form updated successfully",
        "actions": [
            {
                "op": "replace",
                "path": "/formTitle",
                "value": "Pre Chat form"
            }
        ]
    }
[/code]
