# CX Knowledgebase : Collection Removal from MongoDB

Follow the below mentioned steps to delete the collection(s) from MongoDB . Incase , it is required.

### **Step 1 :** Get pod
[code] 
    kubectl get pods -n ef-external
[/code]

  


![](attachments/2526725/2550604.png?height=250)

### **Step 2 :** Log-in to mongoDB pod

**Command format :**
[code] 
    kubectl exec -it <pod-name> -n <namespace> -- mongosh
[/code]

**Example command :**
[code] 
    kubectl exec -it mongo-mongodb-0 -n ef-external -- mongosh
[/code]

![](attachments/2526725/2550624.png?width=744)

### **Step 3 :** Delete collection

##### i) To list all databases 
[code] 
    show dbs;
[/code]

##### ii) Use any database on which you want to perform any operation.
[code] 
    use conversation-manager_db;
[/code]

##### iii) To list all collections in the selected database.
[code] 
    show collections;
[/code]

##### **iv) Now you can drop the required collection.**
[code] 
     db.CustomerTopicEvents.drop();
[/code]

  


![](attachments/2526725/2550619.png?width=744)
