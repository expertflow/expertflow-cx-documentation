# CX Knowledgebase : CX High Availability

There are multiple deployment topologies depending upon the available environment. 

## Quorum-based Cluster

A typical quorum-based high availability cluster with majority-voting mechanism. For environments limited to two physical sites, it requires a **Witness** on a neutral location. 

See [Quorum-based Cluster](Quorum-based-Cluster_1320452440.html) for details.

## Failover Cluster with Replicated Block Volume

This deployment topology is suitable for environments that require site-level redundancy and there is no neutral location for a **Witness** node. 

See [Failover Cluster with Replicated Block Volume](Failover-Cluster-with-Replicated-Block-Volume_1320550500.html) for details.

The options mentioned cover base components for Voice and Core CX platform. It does not include hardware requirements of add-on components: 

  * Quality Management

  * Workforce Management

  * AI 



