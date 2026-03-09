# CX Knowledgebase : Redis Log Monitoring via slowlogs

The purpose of this guide is to view queries/commands execution time, to identify which commands are taking longer to execute than the expected behavior.  
  
## Enabling Redis CLI

  1. First we will enable redis client which we will use to interact to the master redis. The below command will list down the steps to enable and connect to the redis-client pod from your terminal.



[code] 
    helm status -n ef-external redis
[/code]

  2. Once you are inside the redis cli use the following commands to enable slowlogs. Below command allows you to set execution timeframe for the commands to be listed in the slowlog buffer, if any command is taking longer than the time defined in `<threshold_in_microseconds>` will be noted in slow logs.



[code] 
    CONFIG SET slowlog-log-slower-than <threshold_in_microseconds>
[/code]

  3. To view the slowlogs data run the following command. `<enteries>` define the amount of queries logged by the system that exceeded your defined threshold



[code] 
    SLOWLOG GET <no-of-enteries>
[/code]

  4. To avoid massive entries and system exhaustion due to logging we can define a buffer size to limit the amount of logs being saved by using the following command, where `<amount>` defines the maximum amount of entries that can be saved.



[code] 
    CONFIG SET slowlog-max-len <amount>
[/code]

  5. To disable slowlogs, to avoid over exhaustion, use the following command



[code] 
    CONFIG SET slowlog-log-slower-than -1
[/code]

## Using monitor 

monitor command can also be used to view the currently on going activity inside the redis-master container. This command should not be used for a longer period of times except when it is necessary to view the ongoing operations.
[code] 
    monitor
[/code]
