# CX Knowledgebase : Agent Availability Report

**Report Summary**|  Provides MRD-wise agent's availability statistics for each agent of the team to take necessary measures to improve the contact center performance.   
---|---  
  
## Report Columns

**Fields**| **Description**  
---|---  
Date | Shows the date  
Agent Name| Shows the name of the agent available  
Agent Extension| Shows the extension of the agent  
MRD Name| Shows the name of MRD on which the agent is available. For instance, Chat MRD, Voice MRD  
Logged-in Duration| Shows the total logged in duration of the agent that for how long he has been logged in.**Format** hours:minutes:seconds (00:00:00)  
NOT-Ready Duration| Shows the total duration for which the agent remains in a NOT_READY state on this particular MRD.**Format** hours:minutes:seconds (00:00:00)  
Ready Duration| Shows the total duration for which the agent remains in a READY state on this particular MRD.**Format** hours:minutes:seconds (00:00:00)  
Active Duration| Shows the total duration for which the agent remains in ACTIVE state on this particular MRD.**Format** hours:minutes:seconds (00:00:00)  
Busy Duration| This is the total duration for which the agent remains in a BUSY state on this particular MRD.**Format** hours:minutes:seconds (00:00:00)  
PENDING_NOT_READY Duration| Shows the total duration for which the agent remains in a PENDING_NOT_READY state on this particular MRD.**Format** hours:minutes:seconds (00:00:00)  
Total Talk Duration| Shows the total talk duration for which the agent remains in ACTIVE and BUSY state. **Format** hours:minutes:seconds (00:00:00)  
Availability %| This shows the percentage of time for which the agent remains available/ready to handle requests on a particular MRD. This will be calculated as:(Total Ready Duration + Total Active Duration / Total Logged-in Duration) * 100  
  
![](attachments/2527630/2562785.png?width=800)

## Report Filters

The following report filters are available

  * Date/Time - You can choose the date to filter the data for the specific date

  * Agent - Choose the agent to see MRD-wise statistics of the agent

  * MRD - Choose one MRD/all MRDs



