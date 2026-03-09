# CX Knowledgebase : Cisco Sync Service

This enables smooth integration between Cisco and CX by syncing Cisco users and teams into the CX. This synchronization ensures that key CX components, such as Quality Manager (QM), Campaigns, or any outbound flows, can operate smoothly using up-to-date Cisco data.  
  
In case of QM integration with Cisco, Cisco Agents and Teams should be visible in CX before creating CX Conversations for quality monitoring of calls handled by Cisco agents.

🔄 **Purpose and Functionality**

  * Facilitates a **one-way sync** from Cisco to CX for both users and teams.

  * Ensures **real-time visibility** of Cisco Agents and Teams within CX, which is essential for initiating CX Conversations for call quality monitoring.

  * Supports operational components that rely on accurate user data, including QM, Campaigns, or any outbound flows.




🛠️ **Operational Flow**

  * When a user’s information (e.g., team assignment or role) is updated in Cisco, these changes are automatically reflected in CX during the next sync cycle.

  * Newly created teams in Cisco are dynamically mirrored in CX to maintain consistency.

  * Users sync into **CX-IAM** for identity and access management, while teams sync directly to **CX**.




📌 **Use Case Example**

Before launching quality monitoring activities through QM, all relevant Cisco Agents and Teams must be present in CX. The Cisco Sync Service ensures this prerequisite is met automatically, streamlining the setup process and improving operational readiness.

## Expected Behavior of Teams/Users Sync for QM:

Following are the points regarding the expected behavior of sync implementation based on different scenarios:

  * Its one way sync i.e, all the information on Cisco side will be synced on CX side.

  * If the user/team info is updated on Cisco side, then it will also update on CX once sync instance runs.

  * If Cisco team/user doesn't exist on the CX side, then it will be created.

  * If membership of agent/supervisor on Cisco side changes, then it will also update on CX side; agent/supervisor will be removed from previous teams and assigned to new teams.

  * If agent/supervisor is deleted on Cisco side then that user will be disabled on CX side.

  * The team deletion on Cisco side is not handled on CX Side. One must manually delete the team on the CX side.

  * If a team has multiple supervisors on the Cisco side, then one of them will become primary supervisor on the CX side, and all others will be secondary supervisors. (There is no distinction between primary and secondary supervisors)

  * There shouldn’t be same-named teams on the CX side while syncing Cisco teams. (Manually creating a team on CX side with the same name as Cisco team)




There shouldn’t exist a CX team with same name as of Cisco Team. e.g: Default team existing in CX already. Make sure only Cisco Teams exist in CX if Cisco is enabled, no CX teams should exist in that case in CX Core.

Error Message in that case is as follows:
[code] 
    {
        "error_message": "Error occurred while Syncing Cisco Data in Keycloak and CX",
        "error_detail": {
            "error_message": "Finesse Team Sync Error: Error occured while creating cx core team. TEAM ID: 2, TEAM NAME: Web-RTC",
            "error_detail": {
                "status": 409,
                "reason": "CX Team Web-RTC already exists against this Cisco Team with different ID, Causing Conflict."
            }
        }
    }
[/code]

## Deployment

To deploy Cisco Sync Service in the CX Solution, need to follow the steps mentioned in [the guide](https://docs.expertflow.com/cx/4.10/deployment-guide-cisco-sync-service).

## Pipelines

A pipeline is created on the EF Data Platform that consistently controls and monitors the sync service job. To set up the pipeline, one needs to deploy the EF Data Platform as per the following guides:

  * [EF Data Platform Deployment Guide](https://expertflow-docs.atlassian.net/wiki/spaces/EF/pages/772243470/EF+Data+Platform+Deployment)

  * [Cisco Agent/Team Sync Pipeline (Monitoring and Control)](https://expertflow-docs.atlassian.net/wiki/spaces/CXDOC/pages/1102577846/Cisco+Agent+Team+Sync+Pipeline)



