# CX Knowledgebase : Customer Schema

Allows the business administrator or anybody who has permission to customize the Customer fields.  
  
With this interface, the administrator can define the desired customer fields that are required to store important data about business customers. For instance, a company might want to store their customers' home addresses while another might not require that.

## To define Customer data fields

Select **Customer Schema** from the main menu.

Click the **Create New Attribute** button to add a new customer field.

![](attachments/2525665/2571462.png?height=250)

 _Create new attribute_

Use the following table to add the attribute:

**Field**| **Description**  
---|---  
Label| Give a name to the attribute, such as `home address` in the example above.  
Description| Give an optional description to specify what type of customer information this field will store.  
Field Type| Possible values are:

  * Alphanumeric
  * Boolean
  * Email
  * Ip
  * Name
  * Number
  * Phonenumber
  * Password
  * String
  * Url

See the data dictionary for more details on the field types above.  
Number of characters| This determines the number of characters the field value will take in.Only available in case of field type, **String.**  
Mandatory Attribute| Set a field as required or optional. If marked, you need to specify a default value of the mandatory attribute. This value will be used by the system while creating the anonymous customer profiles.  
PII| This allows to mask the data encapsulated in the field marked as PII.  
Channel Identifier| Mark if the attribute is a Channel Identifier or a non-identifier. If yes, select the channel for which this attribute will serve as a channel identifier.  
This allows to set an identifier for a channel, for the system to identify an incoming customer using the value of this attribute. For instance, a mobile number could be set as a channel identifier of WhatsApp while an email id can serve as an identifier for Webchat.Note that a channel identifier attribute is a multi-valued attribute. That is, it can store multiple identities of the same channel. For now, a maximum of 10 values can be stored under a single channel identifier attribute.  
  
You can reorder the attributes list on the **Customer Attributes** screen. The order saved here will be used to render the customer fields on the Customer form. 

The following attributes are created by default in the system and cannot be deleted from system-created attributes. 

  * First Name

  * Phone number

  * Web

  * Voice




You may change the following for the **First Name** attribute:

  * Label

  * Description

  * Default Value




Note that the default value of the “First Name” field is set to “John Doe”. However, this can be modified and replaced with your specified name. 

  

