# CX Knowledgebase : UTC Offset - Reports

## Overview  
  
The  _UTC offset_ is the difference in hours and minutes between Coordinated Universal Time (UTC) and local solar time, at a particular place.

### Background

In our reporting DB, all the data is being stored at UTC+0 (with zero offset). The customer needs to insert the offset into a table, called, "**reports_offset** " in the reporting DB so that the timestamps in historical reports on Superset are shown as per the customer's local time.

### Steps:

Following steps needs to be followed.

  


#### Step 1

Visit the website [https://www.google.com](https://www.google.com/) & search "UTC offset for {your city/country name here}".

  


**Example :** UTC offset for South Africa

  


![](attachments/2526326/2557067.png?width=550)

  


  


#### Step 2

You need to pick this offset value and convert it into minutes using formula → offset * 60.

**Example 1 :** If you are living in South Africa & selected to go with offset UTC+2. This means that 2 hours (2*60 = 120 minutes) will be added to UTC+0 timestamps & you'll see the timestamps fields as per your local time in reports.

**Example 2:** If the offset is UTC -1.5 , then this means that you are living 1.5 hours before the UTC+0 timezone. Then, you need to **subtract 90 minutes** from UTC timestamps.

Please carefully consider the arithmetic sign with offset value**i.e.** \+ (plus) or - (minus). You need to mention this sign in table along-with minutes.

  


#### Step 3

Run the following SQL query to update this offset into the table "**reports_offset** " in reporting DB.
[code] 
    UPDATE reports_offset SET offset_in_minutes =-120;
[/code]

  


#### Step 4

Verify that your offset_in_minutes has been updated.

  


![](attachments/2526326/2551656.png?height=250)

  


  


  


  


  


  

