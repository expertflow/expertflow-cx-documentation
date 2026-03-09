# CX Knowledgebase : Recording Links In EF CX

This document aims to describe the process of pushing recording links to EFCX and retrieving files for the respective recording solutions. The implementation within CX Core is described here: 

<https://expertflow-docs.atlassian.net/wiki/x/2QESLg?atlOrigin=eyJpIjoiNjI5OGM5MDBkYWJkNDNiOWE3ZDQ4NDEyNmVlNmNjNmUiLCJwIjoiYyJ9>

## Eleveo

### Pushing Links to EFCX

  1. Fetch voice activities from CX:

     1. Get last pushed time from cache (or use default interval)

     2. Call CX voice activities API between start time and end time:

        1. end time= current time - eleveo processing time (time it takes for Eleveo to process recordings).

        2. start time = endtime - interval (either default or duration between current time and last pushed time).

     3. Sort each set of CX Call Legs.

  2. Get recording information from Eleveo:

     1. Use dialogId of each leg to get Eleveo recording information from API.

     2. Create list of Eleveo call legs per call.

     3. Merge the legs that are split due to HOLD.

  3. Push links to EF CX:

     1. Compare sorted lists of CX Call Legs to Eleveo call legs.

     2. Create links with CX Legs IDs and push to CX.




### Retrieving Files From Eleveo

  1. The recording link pushed to CX is clicked on:

     1. CX leg ID in received in the format: **dialogId** :agentExtension:ani:**legStartTime**

  2. Use dialogId from leg ID to fetch Eleveo recording information:

     1. Get Eleveo recording information from API.

     2. Sort list of legs provided by Eleveo.

     3. Merge Hold ended legs.

     4. The leg with the closest start time to that in the CX leg ID is chosen.

     5. Get Eleveo Leg Id(s) of that leg (multiple IDs if merged legs).

  3. The file is obtained from Eleveo APIs:

     1. If multiple files are present (due to HOLD) then they are all retrieved and merged sequentially.

  4. Return recording file to CX.




## CX Voice

### Pushing Links to EFCX

  1. Fetch voice activities from CX:

     1. Get last pushed time from cache (or use default interval).

     2. Call CX voice activities API between current time and time before interval.

     3. Sort each set of CX Call Legs.

  2. Check EFSwitch for recordings per call leg:

     * Use CX Leg Ids as dialogId to fetch file paths from Efswitch database.

     * From filepaths fetch files that match the respective CX Leg IDs.

  3. Push links to EF CX:

     1. Compare sorted lists of CX Call Legs to EFSwitch call legs.

     2. Create links with CX Legs IDs and push to CX.




### Retrieving Files From EFSwitch

  1. The recording link pushed to CX is clicked on:

     1. CX leg ID in received in the format: **dialogId** :agentExtension:ani:**legStartTime**

  2. Info the the leg ID is used to get files from EFSwitch:

     1. The dialogId is used to get the filepath from EFSwitch database.

     2. Within the path, the files matching the first three sections of the leg ID (**dialogId** :agentExtension:ani) are returned.

     3. The leg with the closest start time to that in the CX leg ID is chosen.

  3. The file is picked from the system.

  4. The file is returned to CX.



