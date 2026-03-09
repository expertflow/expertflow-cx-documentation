# CX Knowledgebase : Benchmarking for CX Dialer

**CX Dialer**  
---  
**Version**|  4.5-SR11  
  
### Free SWITCH VM Hardware Specifications

Here are the specifications of the virtual machine where EF - CX Dialer and FreeSWITCH are running:

**Specification**| **Details**  
---|---  
**Cores**|  8  
**RAM**|  12-16 GB  
**ROM**|  150 GB  
  
### Software Specifications

**Specification**| **Details**  
---|---  
**Operating System**|  Linux  
**OS Distribution**|  Debian 12  
**FusionPBX**|  Version 5.2.2  
  
### POST API - Testing Statistics

We conducted IVR-based calls to 2000 customer numbers using the Dialer, running tests at intervals of 500, 1000, 1500, and 2000 calls.

Scheduler POST API = [https://FQDN/scheduler/scheduled-activities](https://efcx-qa3.expertflow.com/scheduler/scheduled-activities) (where FQDN is the CX server FQDN)

For **10 calls per second** of Dialer, here are the stats:

**Test No.**| **Number of requests per second**| **Contacts in Dialer Database**| **Number of connected call**| **Number of failed calls**| **Host Free SWITCH CPU usage**| **Call Results**  
---|---|---|---|---|---|---  
1| 500| 500| 500| 0| 40.3%| NORMAL_CLEARING  
2| 1000| 962| 962| 0| 57.1%| NORMAL_CLEARING  
3| 1500| 1500| 1500| 0| 81.8%| NORMAL_CLEARING  
4| 2000| 1972| 1972| 0| 89.3%| NORMAL_CLEARING  
  
For **30 calls per second** of Dialer, here are the stats:

**Test No.**| **Number of requests per second**| **Contacts in Dialer Database**| **Number of connected calls**| **Number of failed calls**| **Host Free SWITCH CPU usage**| **Call Results**  
---|---|---|---|---|---|---  
1| 500| 497| 497| 0| 41.0%| NORMAL_CLEARING  
2| 1000| 994| 994| 0| 69.8%| NORMAL_CLEARING  
3| 1500| 1326| 1326| 0| 100.0%| NORMAL_CLEARING  
4| 2000| 1990| 1990| 0| 100.0%| NORMAL_CLEARING
