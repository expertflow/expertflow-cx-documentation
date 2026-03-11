# CX Knowledgebase : Quorum-based Cluster

A typical quorum-based high availability cluster with majority-voting mechanism. For environments limited to two physical sites, it requires a **Witness** on a neutral location. 

## Considerations for Witness Location

Enterprises often struggle with Quorum based deployment because they only have two major data centers. The Witness should **not** be placed in either of the two main physical sites. It must be deployed in a **third, independent location**. Here are the most common and practical solutions for creating that third, independent location:

  1. **A Public Cloud VM (Most Popular):** This is the modern standard. Deploy a small, low-cost VM (e.g., Azure B1s, AWS t3.micro) in a cloud region that is geographically distinct from your two primary sites. The network latency is typically low enough for the witness heartbeat, and the cost is minimal.

  2. **A Small Colocation Rack:** Rent a very small space in a colocation facility in a different city. This provides full control but is more expensive and complex than a cloud VM.

  3. **A Different Building/Campus within the Enterprise:** If your two main sites are in different cities, you could place the witness in a small server room at a corporate office or a smaller regional office in a third city. The key is that it must have **independent power and network infrastructure** from both primary sites.




## Limitations

  * Needs majority nodes online (no quorum = no service).

  * Small clusters (e.g., 3 nodes) can tolerate only 1 node failure.

  * Medium/Large clusters (e.g., 5 nodes) can tolerate 2 nodes failure.




## Deployment Prerequisites

  * Redundant network connectivity across all sites.

  * Network latency below 40 ms.




## Hardware Requirement

Site Name| Node| CPU Cores| RAM (GB)| Storage (GB)| Operating System  
---|---|---|---|---|---  
Site A| Core Platform| 16| 32| 300| Ubuntu-24.04-LTS  
Site A| Reporting| 8| 16| 100| Ubuntu-24.04-LTS  
Site A| Voice Platform| 16| 32| 250| Debian-12  
Site B| Core Platform| 16| 32| 300| Ubuntu-24.04-LTS  
Site B| Reporting| 8| 16| 100| Ubuntu-24.04-LTS  
Site B| Voice Platform| 16| 32| 250| Debian-12  
Neutral Site| Witness| 2| 4| 100| Ubuntu-24.04-LTS  
  
## Quorum-based Cluster: Failover & Recovery Impact

  * **The system is highly resilient** to the failure of an entire site, with automatic failover and minimal downtime.

  * **The loss of the Arbiter alone is not critical** as long as the two main sites are connected.

  * **Recovery is typically automatic** for single failures, making the system robust and manageable.




| **Scenario**| **Components Failed**| **Components Active**| **Business Impact**  
---|---|---|---|---  
1| **Normal Operation** | None | Site A (Active), Site B (Passive), Witness | No impact. All services available.   
2| **Site Failure** | One Site (e.g., Site A - Active) | Site B (Passive), Witness | **Brief service interruption** during automatic failover, then service resumes on Site B.   
3| **Network Split** | Link between Site A and Site B | Site A, Site B, Witness | **Brief interruption** for some users. Service continues automatically on one site.   
4| **Witness Failure** | Witness | Site A (Active), Site B (Passive) | **No impact.** Full service continues. Resilience to network splits is temporarily lost.   
5| **Witness Failure & Link between two sites is down**| Witness + Link between sites | Site A and Site B (isolated) | **No Impact :** Full service continues.  
6| **Active Site & Witness Failure**| Site A (Active) + Witness | Site B (Passive only) | **Total service outage.** Requires manual intervention to restore.   
7| **Failed Site Recovers** | (Previously failed site rejoins) | Site B (Active), Site A (Passive), Witness | **No impact.** Service continues without interruption. Site A automatically syncs data in the background.   
8| **Witness Recovers** | (Previously failed Witness rejoins) | Site A (Active), Site B (Passive), Witness | **No impact.** Full resilience is restored automatically.   
9| **Recovery from Total Outage**| (Link and/or nodes are restored) | Sites and Witness are restored | **Service restored after manual intervention.** Impact duration depends on admin action. 
