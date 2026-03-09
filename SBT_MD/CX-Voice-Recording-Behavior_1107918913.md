# CX Knowledgebase : CX Voice Recording Behavior

### Expected Recording Rules

  * Each call leg that is present in CX is always pushed.

  * Recording for a call leg is paused during hold, and resumed in the same file when call leg is resumed.

  * The separate legs that can appear in CX are inbound IVR, basic inbound/outbound/campaign progressive outbound, consult, queue/named transfer, consult transfer, silent monitor and consult/barge conference.

  * For conference calls, the recording pushed to CX will from the perspective of the new agent in the conversation i.e. consulted agent for consult conference and silent monitor for barge conference.

    * In a three-person conference if an agent leaves, then the conference recording of the other agent will include the recording of the remaining call until it ends or is transferred.

    * For example, in a conference A1A2C1, if A1 leaves and A2C1 is established, the conference recording for A2 will include audio from the conference as well as the resulting A2C1 call.

  * There are no recordings pushed against silent monitor or inbound IVR legs.

  * In the case of consulting an external party, the consult call will be recorded on EFSwitch, however the link for it will not be pushed to CX due to no associated call leg in CX. 

    * This extends to consult transfer and consult conference legs with an externally consulted party. 

  * In the case of consult conference with and externally consulted party, the first call leg (basic inbound/outbound A1C1) will contain the recording of the conference from the CX agent’s perspective (A1).




### Progressive Outbound

Not supported or tested at this time. Links may be pushed but not expected to support all cases.

### Outbound

| **Case**| **Issues**| **Recording Content**| **Developer’s**  
**Comments**| **QA Comments/Status**  
(CX)| **QA Comments/Status**  
(VRS)  
---|---|---|---|---|---|---  
1| A1C1| none| A1C1| | PASSED| PASSED  
2| A1C1, hold, resume| after resuming, audio is distorted| A1C1| Zeeshan to test.   
if the issue persists, Shamel to discuss with the voice subsystem team.| PASSED(Audio issue fixed now CCC-1799)| PASSED(Audio issue fixed now CCC-1799)  
3| A1C1, queue transfer A2| none| A1C1  
A2C1| | PASSED| PASSED  
4| A1C1, named transfer A2| none| A1C1  
A2C1| | PASSED| PASSED  
5| A1C1, queue consult A1A2| none| A1C1  
A1A2| | PASSED| PASSED  
6| A1C1, named consult A1A2| none| A1C1  
A1A2| | PASSED| PASSED  
7| A1C1, A1A2, retrieve A1C1, retrieve A1A2, end A1A2, retrieve A1C1, end A1C1| In first retrieve A1C1 audio is distorted, last retrieve has ok audio  
consult retrieve has ok audio| A1C1  
A1A2| Zeeshan to test.   
if the issue persists, Shamel to discuss with the voice subsystem team.| PASSED  
(as per given behavior)| PASSED  
(as per given behavior)  
  
Difference in call and audio duration.  
Sample: 11 June,**22:13:29**  
8| A1C1, queue consult A1A2, transfer| none| A1C1  
A1A2  
A2C1| | PASSED| PASSED  
9| A1C1, named consult A1A2, transfer| none| A1C1  
A1A2  
A2C1| | PASSED| PASSED  
10| A1C1, hold, resume, queue transfer to A2, hold, resume| A1C1 audio is distorted after resume  
queue transfer audio is ok  
resumed A1C1 audio is ok| A1C1  
A2C1| Zeeshan to test.   
if the issue persists, Shamel to discuss with the voice subsystem team.| PASSED| PASSED  
11| A1C1, hold, resume, direct transfer A2, consult A1, retrieve A2C1, retrieve A2A1, consult transfer A1, direct transfer A2| A1C1 audio is distorted after resume  
both retrieved audios are ok| A1C1 first leg  
A2C1 direct transfer first  
A1A2  
A1C1 consult transfer  
A2C1 direct transfer second| Zeeshan to test.   
if the issue persists, Shamel to discuss with the voice subsystem team.| All audios are fine.  
4 legs created and recording saved for each.  
(Consult not created in CX)| All audios are fine.  
5 legs created and recording saved for each.Call Duration issue. Sample: 11 june  
**17:34:23** recording[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)  
12| A1C1, S1 monitors| monitoring impossible| | | |   
13| A1C1, A1E1 external consult| A1E1 recording file has missing params in the filename, likely due to case not being covered in script| A1C1  
A1E1 (not pushed to CX)| This will need to be fixed once we show the consult leg in CX.| PASSED| PASSED  
14| A1C1, A1E1 external consult, E1C1 external consult transfer| A1E1 recording file has missing params in the filename, likely due to case not being covered in script| A1C1  
A1E1 (not pushed to CX)  
A2E1 (not pushed to CX)| This will need to be fixed once we show the consult leg in CX.| PASSED| PASSED  
15| A1C1, E1C1 external transfer| none| A1C1  
E1C1 (not pushed to CX)| This will need to be fixed once we show the consult leg in CX.| PASSED| PASSED  
16| A1C1, external A1E1, A1E1C1, A1 leaves, E1C1 ends| none| A1C1, A1 perspective in A1E1C1E1 perspective not shown in CX, but file is recorded| | PASSED| PASSED  
17| A1C1, external A1E1, A1E1C1, E1 leaves, A1C1 ends| none| A1C1, A1 perspective in A1E1C1, and A1C1 after E1 leftE1 perspective not shown in CX, but file is recorded| | PASSED| PASSED  
18| A1C1, external A1E1, A1E1C1, C1 leaves| none| A1C1, A1 perspective in A1E1C1E1 perspective not shown in CX, but file is recorded| | PASSED| PASSED  
19| A1C1, A1A2 (Agent Consult), A1A2C1, A1 left, A2C1 end| | | | PASSED| PASSED  
20| A1C1, A1A2 (Agent Consult), A1A2C1, A2 left, A1C1 end| | | | PASSED| PASSED  
21| A1C1, A1A2 (Agent Consult), A1A2C1, C1 left, A1A2 end| | | | PASSED| PASSED  
22| A1C1, A1A2 (Queue Consult), A1A2C1, A1 left, A2C1 end| | | | PASSED| PASSED  
23| A1C1, A1A2 (Queue Consult), A1A2C1, A2 left, A1C1 end| | | | PASSED| PASSED  
24| A1C1, A1A2 (Queue Consult), A1A2C1, C1 left, A1A2 end| | | | PASSED| PASSED  
  
### Inbound

1| **Case**| **Issues**| **Recording Content**| **Developer’s**  
**Comments**| **QA Comments/Status**  
(CX Voice)| **QA Comments/Status**  
(VRS)  
---|---|---|---|---|---|---  
2| A1C1| none| A1C1| | PASSED| PASSED  
3| A1C1, hold, resume| none| A1C1| | PASSED| PASSED  
4| A1C1, hold, resume, queue transfer to A2, hold, resume| none| A1C1  
A2C1| | PASSED| PASSED  
5| A1C1, queue consult A2| none| A1C1  
A1A2| | PASSED| PASSED  
6| A1C1, queue consult A2, retrieve A1C1, end A1A2, end A1C1| none| A1C1  
A1A2| | PASSED| PASSED  
7| A1C1, queue consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | PASSED| PASSED  
8| A1C1, hold, resume, queue consult A2| none| A1C1  
A1A2| | PASSED| PASSED  
9| A1C1, hold, resume, queue consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | PASSED| PASSED  
10| A1C1, consult A2| none| A1C1  
A1A2| | PASSED| PASSED  
11| A1C1, consult A2, retrieve A1C1, end A1A2, end A1C1| none| A1C1  
A1A2| | PASSED| PASSED  
12| A1C1, consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | PASSED| PASSED  
13| A1C1, hold, resume, consult A2| none| A1C1  
A1A2| | PASSED| PASSED  
14| A1C1, hold, resume, consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | PASSED| PASSED  
15| A1C1, named transfer to A2| none| A1C1  
A2C1| | PASSED| PASSED  
16| A1C1, Queue transfer to A2| | | | PASSED| PASSED  
17| A1C1, named transfer to A2, hold, resume| none| A1C1  
A2C1| | PASSED| PASSED  
18| A1C1, hold, resume, named transfer to A2| none| A1C1  
A2C1| | PASSED| PASSED  
19| A1C1, hold, resume, named transfer to A2, hold, resume| none| A1C1  
A2C1| | PASSED| PASSED  
20| A1C1, consult A2, transfer| none| A1C1  
A1A2  
A2C1| | Recordings ok  
Call and Audio duration difference in Consult legCCC-1814| Recordings ok  
Call and Audio duration difference in Consult legCCC-1814  
21| A1C1, consult A2, retrieve A1C1, retrieve A1A2, transfer| none| A1C1  
A1A2  
A2C1| | PASSED| PASSED  
22| A1C1, hold, resume, consult A2, transfer| none| A1C1  
A1A2  
A2C1| | Recording okCall and Audio duration difference for A1C1 and Consult leg   
[CCC-1814](https://expertflow-docs.atlassian.net/browse/CCC-1814)  
[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)Sample: 12 June, **17:48:58**|  Recording ok  
Call and Audio duration difference for A1C1 and Consult leg   
[CCC-1814](https://expertflow-docs.atlassian.net/browse/CCC-1814)  
[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)Sample: 12 June, **17:48:58**  
23| A1C1, hold, resume, consult A2, retrieve A1C1, retrieve A1A2, transfer| none| A1C1  
A1A2  
A2C1| | Recording okCall and Audio duration difference for A1C1 and Consult leg.   
[CCC-1814](https://expertflow-docs.atlassian.net/browse/CCC-1814)  
[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)  
Sample:  
12 June, **17:54:34**|  Recording okCall and Audio duration difference for A1C1 and Consult leg.   
[CCC-1814](https://expertflow-docs.atlassian.net/browse/CCC-1814)  
[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)  
Sample:  
12 June, **17:54:34**  
24| A1C1, transfer to A2, consult A1, transfer A1| none| A1C1 first leg  
A2C1  
A1A2  
A1C1 consult transfer| | A1C1 first leg  
A2C1  
A1C1 consult transfer| A1C1 first leg  
A2C1  
A1A2  
A1C1 consult transfer  
  
Call and Audio Duration issue.  
Sample: 11 June, **19:13:41**  
25| A1C1, consult A2, transfer A2, transfer A1| none| A1C1 first leg  
A1A2  
A2C1  
A1C1 direct transfer| | Recording okCall and Audio duration difference for A1C1 and Consult leg.   
[CCC-1814](https://expertflow-docs.atlassian.net/browse/CCC-1814)  
[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)  
Sample: 12 June, **17:59:42**|  Recording okCall and Audio duration difference for A1C1 and Consult leg.   
[CCC-1814](https://expertflow-docs.atlassian.net/browse/CCC-1814)  
[CCC-1812](https://expertflow-docs.atlassian.net/browse/CCC-1812)  
Sample: 12 June, **17:59:42**  
26| A1C1, hold, resume, direct transfer A2, consult A1, retrieve A2C1, retrieve A2A1, consult transfer A1, direct transfer A2| none| A1C1 first leg  
A2C1direct transfer first  
A1A2  
A1C1 consult transfer  
A2C1 direct transfer second| | PASSED| PASSED  
27| A1C1, S1 monitors| none| A1C1| | PASSED| PASSED  
28| A1C1, S1 Barges, A1C1S1, S1 leaves, A1C1 ends| none| A1C1  
S1 perspective in A1S1C1  
A1 perspective in A1C1S1 is recorded, including A1C1 after S1 leaves but not shown in CX| After S1 leaves the A1S1C1 leg the remaining call recording (A1C1) will not be available on CX| PASSED| Remaining call recording (A1C1) also not available in VRS  
29| A1C1, S1 Barges, A1C1S1, A1 leaves, S1C1 ends| none| A1C1  
S1 perspective in A1S1C1, including S1C1  
A1 perspective in A1C1S1 is recorded but not shown in CX| | PASSED| PASSED  
30| A1C1, S1 Barges, A1C1S1, S1 hold, S1 resume, S1 leave, A1C1 ends| none| A1C1  
S1 perspective in A1S1C1  
A1 perspective in A1C1S1 is recorded, including A1C1 after S1 leaves but not shown in CX| | PASSED| PASSED  
31| A1C1, S1 Barges, A1C1S1, A1 hold, S1 hold, A1 resume, S1 resume, S1 leave A1C1 ends| none| A1C1  
S1 perspective in A1S1C1  
A1 perspective in A1C1S1 is recorded, including A1C1 after S1 leaves but not shown in CX| | PASSED| PASSED  
32| A1C1, S1 Barges, A1C1S1, C1 leaves| none| A1C1  
S1 perspective in A1S1C1  
A1 perspective in A1C1S1 is recorded but not shown in CX| | PASSED| PASSED  
33| A1C1, A1A2, A1A2C1, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, including A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | PASSED| PASSED  
34| A1C1, A1A2, A1A2C1, C1 leaves| none| A1C1  
A1A2  
A2 perspective in A1A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | PASSED| PASSED  
35| A1C1, A1A2, A1A2C1, A1 leaves, A2C1 hold, A2C1 resume, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, including A2C1, and after resume  
A1 perspective in A1A2C1 is recorded but not shown in CX| | PASSED| PASSED  
36| A1C1, A1A2, A1A2C1, A2 hold, A2 resume, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, after resume, including A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | PASSED| PASSED  
37| A1C1, A1A2, A1A2C1, A1 hold, A2 hold, A1 resume, A2 resume, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, after resume, including A2C1  
A1 perspective in A1A2C1 is recorded, including after resume but not shown in CX| | PASSED| Hold Time not displayed in A1A2C1 leg.  
[CCC-1819](https://expertflow-docs.atlassian.net/browse/CCC-1819)  
38| A1C1, external A1E1, A1E1C1, A1 leaves, C1E1 ends from CX perspective.| none| A1C1, A1 perspective in A1E1C1E1 perspective not shown in CX, but file is recorded| E1 perspctive not shown in CX, but file is recorded.  
  
Should we record the external leg with the customer.| PASSED| PASSED  
  
39| A1C1, external A1E1, A1E1C1, E1 leaves, A1C1 ends| none| A1C1, A1 perspective in A1E1C1, and A1C1 after E1 leftE1 perspective not shown in CX, but file is recorded| | PASSED| PASSED  
40| A1C1, A1E1 external consult| A1E1 recording file has missing params in the filename, likely due to case not being covered in script| A1C1  
A1E1 (not pushed to CX)| | PASSED| PASSED  
41| A1C1, A1E1 external consult, E1C1 external consult transfer| A1A2 recording file has missing params in the filename, likely due to case not being covered in script| A1C1  
A1E1 (not pushed to CX)  
E1C1 (not pushed to CX)| A1E1 (not pushed to CX)  
  
This will need to be fixed once we show the consult leg in CX.| PASSED| PASSED  
42| A1C1, E1C1 external transfer| none| A1C1  
E1C1 (not pushed to CX)| This will need to be fixed once we show the consult leg in CX.| PASSED| PASSED  
43| A1C1, A1A2 (Agent Consult), A1A2C1, A1 left, A2C1 end| | | | 

  * Recording link pushed for A1C1 and A1A2C1.

| 

  * All call legs recorded including A1A2.

  
44| A1C1, A1A2 (Agent Consult), A1A2C1, A2 left, A1C1 end| | | | 

  * A1C1 and A1A2C1 recording link pushed to CX.
  * A1C1 not recorded as A2 left and call records in its perspective.

| 

  * All call legs recorded including A1A2.
  * A1C1 not recorded as A2 left and call records in its perspective.

  
45| A1C1, A1A2 (Agent Consult), A1A2C1, C1 left, A1A2 end| | | | 

  * Recording link pushed for A1C1 and A1A2C1

| 

  * All call legs recorded, A1C1, A1A2 and A1A2C1 

  
46| A1C1, A1A2 (Queue Consult), A1A2C1, A1 left, A2C1 end| | | | 

  * A1C1 and A1A2C1 recording link pushed.

| 

  * All call legs recorded including A1A2.

  
47| A1C1, A1A2 (Queue Consult), A1A2C1, A2 left, A1C1 end| | | | 

  * A1C1 and A1A2C1 recording linked pushed.
  * A1C1 not recorded as A2 left and call records in its perspective.

| 

  * All call legs recorded including A1A2.
  * A1C1 not recorded as A2 left and call records in its perspective.

  
48| A1C1, A1A2 (Queue Consult), A1A2C1, C1 left, A1A2 end| | | | 

  * A1C1 and A1A2C1 recording link pushed.

| 

  * All call legs recorded, A1C1, A1A2 and A1A2C1


