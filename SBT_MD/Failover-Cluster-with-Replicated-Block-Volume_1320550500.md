# CX Knowledgebase : Failover Cluster with Replicated Block Volume

This deployment topology is suitable for environments that require site-level redundancy and there is no neutral location for a **Witness** node. 

## Solution Prerequisites

  1. Replicated Read/Write Block Volume attachment on both site-A and Site-B recommended via vSphere vSAN or Enterprise Storage Solution with near real time replication

  2. Redundant network connectivity across both sites.

  3. Network latency below 40 ms.




# Hardware Requirement

Site Name| Node| CPU Cores| RAM (GB)| Storage (TB)| Operating System  
---|---|---|---|---|---  
Site A| Core Platform| 16| 32| 300| Ubuntu-24.04-LTS  
Site A| Reporting| 8| 16| 100| Ubuntu-24.04-LTS  
Site A| Voice Platform| 16| 32| 250| Debian-12  
Site B| Core Platform| 16| 32| 300| Ubuntu-24.04-LTS  
Site B| Reporting| 8| 16| 100| Ubuntu-24.04-LTS  
Site B| Voice Platform| 16| 32| 250| Debian-12  
  
## Failover Scenarios

**Scenario**| **Components Failed**| **Components Active**| **Business Impact**  
---|---|---|---  
**Normal Operation**|  None| Site-A | Solution is available  
**Site Failure**|  Active Site| Standby site is active.| **Brief service interruption** during failover, then service resumes on Standby Site
