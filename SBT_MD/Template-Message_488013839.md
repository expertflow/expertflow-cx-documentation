# CX Knowledgebase : Template Message

**Description**|  Template Messages are pre-defined messages to be sent to the customer. These messages contain fixed text or fields pre-defined in the system.  
---|---  
  
The body should be in JSON format and include the following properties:

**Property**| **Type**| **Desc.**  
---|---|---  
type REQUIRED | String| Value = "TEMPLATE"  
namespaceREQUIRED | String|   
name REQUIRED | String| name of the message  
language OPTIONAL | String| unicode of the language  
component OPTIONAL | List{component object}| See the object detail [here](component_494108684.html).
