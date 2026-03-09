# CX Knowledgebase : Contact Message

**Description**|  Contact message is primarily used to send details of a contact (name, email, phone etc.) to the recipient.  
---|---  
  
The method to send contact message is given as follows:

  * Specify the type = "CONTACT". Body should be in JSON format with following properties:




  


**Property**| **Desc.**  
---|---  
type - String - Required| Value = "CONTACT"  
markdownText - String - Optional| contains custom plain text sent by end user.  
additionalDetails - String - Optional| Additional details such as timedate object values can be passed.  
contacts:| Contacts contains parameters such as name, phone and additional details.  
contacts: name - String - Required| Contains information about the name._Parameters:_

  * formattedName="someName" - Required
  * addtionalNameDetails (first_name,last_name,middle_name,name_suffix,name_prefix) - Optional

  
contacts: phone - String - Required| Contains phone number information._Parameters:_

  * phone="+923xxxx" - Required
  * addtionalPhoneDetails (type = "CELL", wa_id) - Optional

  
contacts: addtionalContactDetails - String - Optional|  _Parameters:_

  * addresses=(street,city,state,zip,country,country_code,type)
  * emails=(email, type)
  * org= (company,department,title)
  * urls=(url,type)
  * ims=(service,userId)
  * birthday="yy-mm-dd"

  
  
  


  


  


  


  

[code] 
    "body": {
            "type": "CONTACT",
            "markdownText": null,
            "additionalDetails": null,
            "contacts": [
                {
                    "name": {
                        "formattedName": "Dummy Name",
                        "additionalNameDetails": {
                            "first_name": "Dummy",
                            "last_name": "Name",
                            "middle_name": null,
                            "name_suffix": null,
                            "name-prefix": null
                        }
                    },
                    "phones": [
                        {
                            "phone": "+92123456489789",
                            "additionalPhoneDetails": {
                                "type": "CELL",
                                "wa_id": null
                            }
                        }
                    ],
                    "additionalContactDetails": {
                        "addresses": [
                            {
                                "street": "3b Block 3",
                                "city": "Lahore",
                                "state": null,
                                "zip": "54700",
                                "country": "Pakistan",
                                "country_code": "pk",
                                "type": "HOME"
                            }
                        ],
                        "emails": [
                            {
                                "email": "email@expertflow.com",
                                "type": "INTERNET"
                            }
                        ],
                        "org": {
                            "company": "Expertflow",
                            "department": "SW",
                            "title": "Software Engineer"
                        },
                        "urls": [
                            {
                                "url": "www.expertflow.com",
                                "type": "HomePage"
                            }
                        ],
                        "ims": [
                            {
                                "service": "SKYPE",
                                "userId": "Expertflow"
                            }
                        ],
                        "birthday": "1990-05-06"
                    }
                }
            ]
        }
[/code]

  


  


  

