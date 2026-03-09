# CX Knowledgebase : customer object

Object Name| customer  
---|---  
Description| It is a dynamic object that can be modified by the admin. By default, it contains four attributes id, firstName, isAnoymous and additionalDetail given as follows. It can be sent as `null` or customer information can also be sent by 3rd party.  
  
  


Parameter| Type| Description  
---|---|---  
Id REQUIRED| UUID| This is the UUID in the format `a5c80b3f-ea41-4caf-979d-641a1c32f9bd`  
firstName OPTIONAL| String| First name of the customer.  
isAnonymous REQUIRED| Bool| If no name is specified, then it is marked true.  
additionalDetail OPTIONAL| Map (String, Object)| Any additional information related to the customer can be sent in the form of `key: value` pairs.
