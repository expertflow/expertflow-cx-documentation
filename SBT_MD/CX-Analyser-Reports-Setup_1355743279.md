# CX Knowledgebase : CX Analyser Reports Setup

### To set up CX Analyser reports:

### 1\. Go to Metabase and log in with the admin user.  


###   
2\. Click on the settings gear icon, then click on admin settings:  


![image-20251015-120455.png](attachments/1355743279/1355284710.png?width=1002)

### 3\. Then, on the admin page, click on databases, then click on Add database:  


![image-20251015-120816.png](attachments/1355743279/1355710485.png?width=1002)

### 4\. Add database and click save (**Remember the Display name of the database, which we will use in the import command**):

During update change database “expertflow” .

![image-20251015-120955.png](attachments/1355743279/1354891496.png?width=458)

### **5\. Go to Table Metadata to verify that all the tables are visible.**

![image-20251107-055151.png](attachments/1355743279/1428619313.png?width=1413)

### 6\. Please make sure that all the tables are not hidden. If any table is hidden, unhide the table by clicking the cross-eye icon. 

![image-20251107-055532.png](attachments/1355743279/1428848665.png?width=508)

### 7\. After successfully creating the database, go to this location on the Metabase machine:
[code] 
    cd kubernetes/external/metabase-reports/metabase_reporting_update_tool/
[/code]

### 8\. Run the following command:  


Before running the command, ensure you choose the correct folder for MySQL or MSSQL reports
[code] 
    For Multi-tenancy, set the tenant collection name like: "T1 Reports" and use the database name created for the tenant in the command.
    
    python3 metabase_import.py https://<Metabase-FQDN>/metabase/api/ <admin-email> <admin-password> <db-display-name> <mysql> "<Tenent-collection-name>"
    
    EXAMPLE: python3 metabase_import.py https://t1.expertflow.com/metabase/api/ metabaseadmin@gmail.com password123 cim_etl_report mysql "EF Reports"
    
    The command may take some time to complete.
    If it runs successfully, you’ll see “✓ Cards imported” at the end.
    If not, it will display an error message.
[/code]

### 9\. After running the command, go to Metabase, click the **report folder** , click the **(…)** icon, then click **Move questions into their dashboards:**

![image-20251015-130231.png](attachments/1355743279/1354924248.png?width=1018)

### 10\. Next, click on **Preview the changes:**

![image-20251015-130438.png](attachments/1355743279/1355022539.png?width=557)

### 11\. Next, click on **Move these questions:**

![image-20251015-130533.png](attachments/1355743279/1354956978.png?width=912)

### 12\. Reports are now successfully imported.
