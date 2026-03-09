# CX Knowledgebase : Routing Attribute

Serves as a Skill assigned to an Agent or a Supervisor. An agent can be assigned an unlimited number of unique Routing-attributes.

## Types of Routing Attributes

The following are two types:

  * **Proficiency** : A value on a scale of 1 to 10. This implies how much proficient an Agent is on a particular skill. For instance, if an Agent is assigned an attribute, named, `English`, with a value of 8, this means that the agent is proficient enough in the English language to assist English-speaking customers. 

  * **Boolean:** `True or False`. This assumes that an agent has a skill or does not have a skill. 




Routing Attributes are configured (Create, Retrieve, Update, Delete) in the Unified-admin. While creating an Attribute, the admin can specify a default value. This default value is automatically assigned to the agent at the time of attribute assignment. The admin may change the value for each attribute assigned to an agent at the time of the attribute assignment. 

A Routing Attribute entity contains the following fields:

**Field**| **Description**  
---|---  
**Id**|  A unique identifier (assigned automatically by the Routing Engine configurations backend).  
**Name**|  Name of the routing attribute.  
**Description**|  Short description of the routing attribute.  
**Type**|  Boolean or Proficiency-level.  
**Default-value**|  An integer value. 0 or 1 for the boolean type and 1 - 10 for the proficiency-level type. At the time of assigning a routing attribute to an agent, if a value is not provided then this default value is used.  
  
  

