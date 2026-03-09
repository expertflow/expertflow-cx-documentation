# CX Knowledgebase : Update Form

This API allows you to update an existing form.The endpoints, properties and code examples are given as follows:

**PUT/ forms**

The body should be in JSON format and include the following properties:

**Request**

**Parameter**| **Description**| **Type**| **Properties**  
---|---|---|---  
formTitle REQUIRED| Name of the form| String| -  
formDescription OPTIONAL| Description of the form| String| -  
attributes REQUIRED| Attributes are fields (key-value) pairs required in the form. More than one field can be added separated the comma.| Object| 

  1. **key** \- String - auto-generated and auto-updated if the label of the attribute is changed.
  2. **label** \- String - name of the field e.g. "First Name"
  3. **helpText** \- String - alt text for the field e.g. "This is helping text"
  4. **attributeType** \- List - type of the field. There are two options:
     1. Input - Input fields such as text
     2. Options - allows custom categories to be created by user. Each category has to be unique and cannot be repeated.
  5. **valueType** \- String - value type of the field (Validation API will be called to validate the custom type) e.g. "String100"
  6. **isRequired** \- Boolean - check if it mandatory to be filled
  7. **categoryOptions** \- Object - will be enabled if **attributeType = Options**. This is a sub-category in Options.

  
  
**Response**

**Code**| **Description**  
---|---  
**200**|  Code 200 implies that the form/form fields have been updated successfully.  
  
  

[code] 
    {
        "id":"1",
        "formTitle": "New Form",
        "formDescription": "This is helping text.",
        "attributes": [
            {
                "key": "first_name",
                "label": "First Name",
                "helpText": "This is helping text",
                "attributeType": "INPUT",
                "valueType": "String100",
                "isRequired": true,
                "categoryOptions": {}
            },
            {
                "key": "state_name",
                "label": "State Name",
                "helpText": "This is helping text",
                "attributeType": "OPTIONS",
                "valueType": "StringList",
                "isRequired": true,
                "categoryOptions": 
                {
                    "isMultipleChoice": true,
                    "categories": [
                        {
                            "categoryName": "Category1",
                            "values": [
                                "Badin",
                                "Chaman",
                                "Balakot"
                            ]
                        }
                    ]
                }
            }
        ]
    }
[/code]

  


  


  

