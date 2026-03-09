# CX Knowledgebase : MongoDB slow query logs

The purpose of this document is to enable logging for slow queries in Mongo, taking too long or causing a heavy load on the Mongo server.  
  
### Prerequisites

This document requires that you should be able to login to the Mongo primary pod, either by running the mongo-client pod or by directly executing into the primary pod. When running bitnami based helm chart, you can get instructions for interacting with the primary pod by running `helm -n ef-external status mongo`.

## Profiler Overhead

When enabled, profiling affects database performance, especially when configured with a profiling level of 2, or when using a low threshold value with a profiling level of 1.

Profiling also uses disk space, because profiling writes logs to the `system.profile` collection, and the MongoDB `logfile`.

## WARNING

Consider performance and storage implications before you enable the profiler in a production deployment.

### The `system.profile` Collection

### Enabling the slow logs

In Mongo, the slow query logs are enabled by a built-in system function called Profiling. Appropriate functions like get or set can be used to retrieve or update the required information in the profiler respectively.

Once logged into the primary pod, we can enable the slow query log using
[code] 
    db.setProfilingLevel( 1, { slowms: 200 } )
[/code]

The above profiler settings enable slow query logs for all the queries taking more than 200 milliseconds while capturing 100% or all the queries falling under the selected criteria. However, if you want to select only a percentage of those queries for example, if you are looking for only 50% of the randomly selected queries, the below command can be used
[code] 
    db.setProfilingLevel( 1, { slowms:200, sampleRate: 0.50 } )
[/code]

### Extract the slow query log

When the slow query logs are enabled in the Mongo server, a new collection in each database is created with the name of `system.profile` which can used to extract the slow query logs.

To view the slow query logs, switch to the required db 
[code] 
    use ccm_db;
[/code]

To return the most recent 10 log entries in the `system.profile` collection, run ;
[code] 
    db.system.profile.find().limit(10).sort( { ts : -1 } ).pretty()
[/code]

To return all operations except command operations ($cmd), run a query similar to the following:
[code] 
    db.system.profile.find( { op: { $ne : 'command' } } ).pretty()
[/code]

To return operations for a particular collection, run a query similar to the following. This example returns operations in the `mydb` database's `test` collection:
[code] 
    db.system.profile.find( { ns : 'ccm_db.ChannelConnector' } ).pretty()
[/code]

To return operations that take longer than 5 milliseconds to complete, run:
[code] 
    db.system.profile.find( { millis : { $gt : 5 } } ).pretty()
[/code]

To return operations for a specific time range, run:
[code] 
    db.system.profile.find( {   
         ts : {
              $gt: new ISODate("2024-05-10T03:00:00Z"),      
              $lt: new ISODate("2024-05-11T03:40:00Z")   
              }
      } ).pretty()
[/code]

The following example looks at the time range, suppresses the `user` field from the output to make it easier to read, and sorts the results by how long each operation took to run:
[code] 
    db.system.profile.find( {   
           ts : {      
           $gt: new ISODate("2024-06-12T03:00:00Z"),      
           $lt: new ISODate("2024-06-12T03:40:00Z")   
           }
           }, 
           { user: 0 } ).sort( { millis: -1 } )
[/code]

### Show the Five Most Recent Events

On a database that has profiling enabled, the `show profile` helper in `mongosh` displays the 5 most recent operations that took at least 1 millisecond to execute. Run `show profile` from `mongosh`:
[code] 
    show profile
[/code]

### Disable Profiling

To disable profiling, run the following example in `mongosh`:
[code] 
    db.setProfilingLevel(0)
[/code]

### Suggested reading

<https://www.mongodb.com/docs/manual/tutorial/manage-the-database-profiler/>
