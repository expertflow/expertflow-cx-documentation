# CX Knowledgebase : EFCX Logs Traversal Guide

Following are the Micro services logging best practices we have implemented in Expertflow CX solution.

## Logging Structure 

### Logs Pattern 

Most of the components uses the same logging pattern.
[code] 
    DateTime | Log Level | Class Name | Method Name | Line:line-num | Log Message | Correlation ID | Topic ID | Thread ID
    
    Topic ID and Thread ID are optional in components where Topic ID / Thread ID is not applicable.
[/code]

### Correlation ID

A correlation ID is a unique ID that is assigned to every request. So, when a request is distributed across multiple services, we can follow that request across different services using the correlation id in logging information.   


### Logging Level

A logging level is a way of classifying the entries in your log file in terms of urgency. Classifying helps filter log files during search and helps control the amount of information in your logs. Logging levels distinguish various log events from each other. They are a way of filtering important information about your system’s state and reduce information noise or alert fatigue. See [this](https://sematext.com/blog/logging-levels/ "Follow link") for for details on log levels types and how to choose them in your application. . The [standard ranking](https://www.tutorialspoint.com/log4j/log4j_logging_levels.htm) of logging levels is as follows: ALL < TRACE < DEBUG < INFO < WARN < ERROR < FATAL < OFF.  


  


  
|   
  
---|---  
  
#### ALL

| This log level logs any logging levels that are defined. It logs everything and includes custom logging levels as well. It is the combination of all other logging levels.  
  
#### TRACE

| The TRACE log level captures all the details about the behavior of the application. It is mostly diagnostic and is more granular and finer than DEBUG log level. This log level is used in situations where you need to see what happened in your application or what happened in the third-party libraries used. You can use the TRACE log level to query parameters in the code or interpret the algorithm’s steps.  
  
#### DEBUG

| With DEBUG, you are giving diagnostic information in a detailed manner. It is verbose and has more information than you would need when using the application. DEBUG logging level is used to fetch information needed to diagnose, troubleshoot, or test an application. This ensures a smooth running application.  
  
#### INFO

| INFO messages are like the normal behavior of applications. They state what happened. For example, if a particular service stopped or started or you added something to the database. These entries are nothing to worry about during usual operations. The information logged using the INFO log is usually informative, and it does not necessarily require you to follow up on it.  
  
#### WARN

| The WARN log level is used when you have detected an unexpected application problem. This means you are not quite sure whether the problem will recur or remain. You may not notice any harm to your application at this point. This issue is usually a situation that stops specific processes from running. Yet it does not mean that the application has been harmed. In fact, the code should continue to work as usual. You should eventually check these warnings just in case the problem reoccurs.  
  
#### ERROR

| Unlike the FATAL logging level, error does not mean your application is aborting. Instead, there is just an inability to access a service or a file. This ERROR shows a failure of something important in your application. This log level is used when a severe issue is stopping functions within the application from operating efficiently. Most of the time, the application will continue to run, but eventually, it will need to be addressed.  
**FATAL**|  FATAL means that the application is about to stop a serious problem or corruption from happening. The FATAL level of logging shows that the application’s situation is catastrophic, such that an important function is not working. For example, you can use FATAL log level if the application is unable to connect to the data store.  
**OFF**|  This log level does not log anything. This OFF level is used to turn off logging and is the greatest possible rank. With this log level, nothing gets logged at all.  
  
  


### Option for changing the logs level

Each component includes a rest end point that enables users to switch to a different log level without having to restart the pods. 

  


To change the logs for all components other than **Agent-Manager** and **Unified-admin** , use the curl command below.
[code] 
    curl --location '{FQDN}/{COMPONENT}/actuator/loggers/com.ef.ccm' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: connect.sid=s%3A3cNmgwXSACa0XFtEw2p4BPFghTWeNusg.bxQiSIz%2Br2wKE1Obwg2%2FR%2Fy1W53cp1kKB5XFcJhO6CM' \
    --data '{
        "configuredLevel": "DEBUG"
    }'
    
    Example for CCM
    
    curl --location 'https://cim.expertflow.com/ccm/actuator/loggers/com.ef.ccm' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: connect.sid=s%3A3cNmgwXSACa0XFtEw2p4BPFghTWeNusg.bxQiSIz%2Br2wKE1Obwg2%2FR%2Fy1W53cp1kKB5XFcJhO6CM' \
    --data '{
        "configuredLevel": "DEBUG"
    }'
[/code]

  


  


  


  

