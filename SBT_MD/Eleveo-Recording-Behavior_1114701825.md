# CX Knowledgebase : Eleveo Recording Behavior

### Expected Recording Rules

  * Each call leg that is present in CX is always pushed.

  * Recording for a call leg is paused during hold, and resumed in the same file when call leg is resumed.

  * The separate legs that can appear in CX are basic inbound/outbound, consult, queue/named transfer, consult transfer, consult conference.

  * For conference calls, the recording pushed to CX will from the perspective of the new agent in the conversation i.e. consulted agent for consult conference.

    * In a three-person conference if an agent leaves, then the conference recording of the other agent will include the recording of the remaining call until it ends or is transferred.

    * For example, in a conference A1A2C1, if A1 leaves and A2C1 is established, the conference recording for A2 will include audio from the conference as well as the resulting A2C1 call.

  * Silent monitoring and barge in Cisco is not supported in CX so recordings will not be pushed for those cases.




### Cisco Campaign Calls

Not supported or tested at this time.

### Outbound

| **Case**| **Issues**| **Recording Content**| **Comments**| **Case Status**| **QA Comments**  
---|---|---|---|---|---|---  
1| A1C1| none| A1C1| | |   
2| A1C1, hold, resume| none| A1C1| | |   
3| A1C1, queue transfer A2| none| A1C1   
A2C1| | |   
4| A1C1, named transfer A2| none| A1C1  
A2C1| | |   
5| A1C1, queue consult A1A2| none| A1C1  
A2C1| | |   
6| A1C1, named consult A1A2| none| A1C1  
A2C1| | |   
7| A1C1, A1A2, retrieve A1C1, retrieve A1A2, end A1A2, retrieve A1C1, end A1C1| none| A1C1  
A1A2| | |   
8| A1C1, queue consult A1A2, transfer| none| A1C1  
A1A2  
A2C1| | |   
9| A1C1, named consult A1A2, transfer| none| A1C1  
A1A2  
A2C1| | |   
10| A1C1, hold, resume, queue transfer to A2, hold, resume| none| A1C1  
A2C1| | |   
11| A1C1, hold, resume, direct transfer A2, consult A1, retrieve A2C1, retrieve A2A1, consult transfer A1, direct transfer A2| 5 legs in CX as expected, however both A2 transfer recordings are combined by middleware   
as side effect of logic that merges retrieved calls| A1C1 first leg  
A2C1 both direct transfers  
A1A2  
A1C1 consult transfer  
A2C1 both direct transfers| | |   
12| outbound A1C1, A1A2, A1A2C1, A1 leaves, A2C1 ends| none| A1C1A1A2| | |   
13| outbound A1C1, A1A2, A1A2C1, C1 leaves, A1A2 ends| Case broken in CX. No conference leg created when C1 leaves.| A1C1  
Conference leg not created in CX so no recording pushed| | |   
14| outbound A1C1, A1A2, A1A2C1, A1 hold, A2 hold, A1 resume, A2 resume, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, including A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | |   
15| outbound A1C1, transfer A2, consult A1, A1A2C1, A2 leaves, A1C1 end| none| A1C1A2C1A1A2A1A2C1A2 perspective in A1A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | |   
  
### Inbound

1| **Case**| **Issues**| **Recording Content**| **Comments**| **Case Status**| **QA Comments**  
---|---|---|---|---|---|---  
2| A1C1| none| A1C1| | |   
3| A1C1, hold, resume| none| A1C1| | |   
4| A1C1, hold, resume, queue transfer to A2, hold, resume| none| A1C1  
A2C1| | |   
5| A1C1, queue consult A2| none| A1C1  
A1A2| | |   
6| A1C1, queue consult A2, retrieve A1C1, end A1A2, end A1C1| none| A1C1  
A1A2| | |   
7| A1C1, queue consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | |   
8| A1C1, hold, resume, queue consult A2| none| A1C1  
A1A2| | |   
9| A1C1, hold, resume, queue consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | |   
10| A1C1, consult A2| none| A1C1  
A1A2| | |   
11| A1C1, consult A2, retrieve A1C1, end A1A2, end A1C1| none| A1C1  
A1A2| | |   
12| A1C1, consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | |   
13| A1C1, hold, resume, consult A2| none| A1C1  
A1A2| | |   
14| A1C1, hold, resume, consult A2, retrieve A1C1, retrieve A1A2, end A1A2, end A1C1| none| A1C1  
A1A2| | |   
15| A1C1, named transfer to A2| none| A1C1  
A2C1| | |   
16| A1C1, named transfer to A2, hold, resume| none| A1C1  
A2C1| | |   
17| A1C1, hold, resume, named transfer to A2| none| A1C1  
A2C1| | |   
18| A1C1, hold, resume, named transfer to A2, hold, resume| none| A1C1  
A2C1| | |   
19| A1C1, consult A2, transfer| none| A1C1  
A1A2  
A2C1| | |   
20| A1C1, consult A2, retrieve A1C1, retrieve A1A2, transfer| none| A1C1  
A1A2  
A2C1| | |   
21| A1C1, hold, resume, consult A2, transfer| none| A1C1  
A1A2  
A2C1| | |   
22| A1C1, hold, resume, consult A2, retrieve A1C1, retrieve A1A2, transfer| none| A1C1  
A1A2  
A2C1| | |   
23| A1C1, transfer to A2, consult A1, transfer A1| none| A1C1 first leg  
A2C1  
A1A2  
A1C1 consult transfer| | |   
24| A1C1, consult A2, transfer A2, transfer A1| none| A1C1 first leg  
A1A2  
A2C1  
A1C1 direct transfer| | |   
25| A1C1, hold, resume, direct transfer A2, consult A1, retrieve A2C1, retrieve A2A1, consult transfer A1, direct transfer A2| 5 legs in CX as expected, however both A2 transfer recordings are combined by middleware   
as side effect of logic that merges retrieved calls| A1C1 first leg  
A2C1 both direct transfers  
A1A2  
A1C1 consult transfer  
A2C1 both direct transfers| | |   
26| A1C1, A1A2, A1A2C1, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, including A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | |   
27| A1C1, A1A2, A1A2C1, C1 leaves| Case broken in CX. No conference leg created when C1 leaves.| A1C1  
Conference leg not created in CX so no recording pushed| | |   
28| A1C1, A1A2, A1A2C1, A1 leaves, A2C1 hold, A2C1 resume, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, including A2C1, and after resume  
A1 perspective in A1A2C1 is recorded but not shown in CX| | |   
29| A1C1, A1A2, A1A2C1, A2 hold, A2 resume, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, after resume, including A2C1  
A1 perspective in A1A2C1 is recorded but not shown in CX| | |   
30| A1C1, A1A2, A1A2C1, A1 hold, A2 hold, A1 resume, A2 resume, A1 leaves, A2C1 ends| none| A1C1  
A1A2  
A2 perspective in A1A2C1, after resume, including A2C1  
A1 perspective in A1A2C1 is recorded, including after resume but not shown in CX| | | 
