# CX Knowledgebase : CX Historical Reports- Supporting Tables

We are using the following tables as an supporting tables to present the historical reports.  
  
  * report_configs
  * reports_offset
  * weekdays



## **report_configs**

We have designed this table as a universal storage for various configurations employed in our reports. It comprises two columns: the **config_key** and the corresponding **config_value**.

Currently, we have just two configurations in place. These values are updated through the ETL job (configs) for the time being.

  


![](attachments/2527591/2562591.png?width=1000)

**Please take note:** In the near future, if any additional configurations are required for the reports, you can utilize this table to set the corresponding keys and values. Consequently, the reports will display the latest values based on the provided keys.

## **reports_offset**

This table serves the purpose of storing the "offset_in_minutes." This offset is subsequently applied to all timestamps in the historical database, either by addition or subtraction. Since all timestamps are originally in UTC+0, this table is utilized to retrieve the offset value and apply it to the timestamps, thereby displaying the records in local timestamps.

  


**Further Details** : [UTC Offset - Reports](UTC-Offset---Reports_2526326.html)

![](attachments/2527591/2562630.png?height=150)

Ensure that this table contains only **one** record; refrain from adding multiple entries to it.

  


## **weekdays**

This table is used to provide us the data of week number , year , week start date & week end date. We are using this information in multiple reports including "Queue-wise Stats Summary Report" & "Historical Conversation Summary Report". A stored procedure is utilized to generate data for this table. 

The week's starting day differs from country to country. For instance, our customer SA_1 is located in South Africa, where the week starts on **Sunday**. Therefore, when generating data for this table using the stored procedure, it is crucial to ensure that the correct week start day is passed as per the customer's country's specifications.

  


![](attachments/2527591/2562655.png?height=400)
