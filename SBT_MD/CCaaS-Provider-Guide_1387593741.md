# CX Knowledgebase : CCaaS Provider Guide

This guide is designed for Managed Service Providers (MSPs) and System Integrators (SIs) looking to offer Expertflow CX as a Contact Center as a Service (CCaaS) platform, detailing the solution's capabilities, architecture, and deployment options.

With multitenancy, you can set up multiple virtually independent contact centers (tenants) provisioned from the same underlying infrastructure. Each tenant operates as a complete, independent contact center environment possessing its own configurations, agents, teams, customers, and interactions.

## CCaaS Provider Benefits

Expertflow CX’s multi-tenant architecture is engineered to reduce operational costs, increase customer capacity, and ensure market reach for your CCaaS offering.

  * **Launch Your Own CCaaS Offering:** Quickly transition to a service model, ready to onboard customers immediately.

  * **Fully White-Label Capability:** The solution can be rebranded under your name (available upon request), establishing your unique market identity.

  * **Reduced Infrastructure Cost:** A single multi-tenant instance efficiently serves multiple tenants, significantly lowering your operational expenses.

  * **High Margins:** Flexible licensing and reduced infrastructure costs support profitable and sustainable business models.

  * **Scalable Architecture:** Add new customers rapidly with minimal additional hardware per tenant. 

  * **Fast Go-to-Market:** Start selling and onboarding customers in days by leveraging Expertflow’s ready-to-use, managed cloud environment.

  * **Flexible Licensing:** Choose between **White Label License** (full branding under your name) or **Standard License** (co-branded with Expertflow) to align with your pricing and marketing strategy.




## Multi-tenant Architecture and Key Features

Expertflow CX utilizes a logically isolated, physically shared multi-instance architecture deployed on Linux and Kubernetes.

Following is the multi-tenancy architecture.

### Shared Platform (Core and Databases)

The core infrastructure is shared across all tenants to maximize resource utilization and simplify maintenance (single patch cycle).

  * **CX-Core Cluster:** Provides unified routing, agent state, and digital channel management across all tenants.

  * **Databases:** Databases run in a dedicated, high-availability cluster, using tenant identifiers for robust data isolation.




### Tenant Isolation and Customization

While the platform is shared, each tenant is logically separated, autonomously managing its resources, data, and customer experience elements:

  * **Configuration Isolation:** Each tenant maintains an exclusive environment covering agent teams, routing strategies, skill definitions, and conversation flows (designed in Conversation Studio).

  * **Data Separation:** All sensitive data, including customer records and interaction history, are stored in separate databases (one per tenant) on the shared database **cluster** , ensuring strict data sovereignty and security.




## Deployment Options

Partners have two distinct models for leveraging the Expertflow CX platform:

### Partner-Managed Deployment (Partner Hosted Cloud)

The partner assumes full control and responsibility for the infrastructure.

Aspect| Responsibility| Partner Value  
---|---|---  
**Infrastructure (Hardware)**| **Partner** (Owner/Manager)| Full control over hardware specifications, geographic location, and CapEx/OpEx model.  
**Platform Deployment**| **Partner**|  Deploys CX-Core, installs Kubernetes, manages all updates, and scales shared resources.  
**Tenant Isolation**| **Partner**|  Responsible for correctly sizing the shared base and provisioning incremental hardware/resources per new tenant.  
**Resource Guide**| |  Refer to [CX Hardware Requirements: Multi-Tenant Partner Sizing](/wiki/pages/createpage.action?spaceKey=SBT&title=Hardware%20Requirements%3A%20Multi-Tenant%20Hosted%20Solution%20%28Partner%20Sizing%20Guide%29&linkCreation=true&fromPageId=1387593741) for detailed scaling increments.  
  
### Expertflow-Managed Deployment (Expertflow Cloud Hosted)

The partner focuses purely on sales, licensing, and customer integration, abstracting all hardware management.

Aspect| Responsibility| Partner Value  
---|---|---  
**Infrastructure (Hardware)**| **Expertflow** (Owner/Manager)| Zero hardware management or capital investment required from the partner.  
**Platform Deployment**| **Expertflow**|  Expertflow handles all scaling, HA/DR, and core platform maintenance.  
**Tenant Isolation**| **Expertflow**|  Expertflow manages the underlying capacity allocation and resource guarantee per tenant license.  
**Resource Guide**| |  Refer to [Partner Guide: Expertflow Cloud Hosting](/wiki/pages/createpage.action?spaceKey=SBT&title=Partner%20Guide%3A%20Onboarding%20Tenants%20to%20Expertflow%20Cloud&linkCreation=true&fromPageId=1387593741) for capacity allocation and licensing structure
