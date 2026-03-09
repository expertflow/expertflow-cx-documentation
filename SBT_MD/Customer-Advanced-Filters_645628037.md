# CX Knowledgebase : Customer Advanced Filters

This feature allows the creation of filters within CX Customers to generate more, customized customer lists for specific purposes. These filters may later be accessed from anywhere to get customized lists for use cases such as precise contact segmentation to run targeted campaigns. 

The more precise customer lists can be generated using AND/OR operators while generating the customized filters.

To use an attribute in an advanced filter, it must be marked as **"Searchable"**. You can also mark an attribute searchable at the creation time or by editing an existing attribute. The following attributes are searchable by default:

  * **firstName**

  * **phoneNumber**

  * **labels**




![advanced filters-1.png](attachments/645628037/928284700.png?width=789)

### Steps for Managing the Advanced Filters

Open the **Customer List** from the main menu and click the **Advance Filter** button.

  * Define a title or a filter name. 

  * Add conditions such as:

    * **Starts with** : e.g., "First Name starts with 'Jo'"

    * **Ends with** : e.g., "Last name ends with 'Miller'"

    * **Equal to** : e.g. Email equal to “@expertflow.com“




Conditions are displayed based on the attribute's data type to ensure relevant filtering options. For **string attributes** , you can use conditions like _Starts with_ , _Ends with_ , _Contains_ , and _Equal to_. For **boolean attributes** , only the _Equal to_ and _Not Equal_ conditions are available, allowing you to filter between _true_ or _false_ values.

For further details on supported conditions, visit: 

[Backend Support for Advanced Filters](Backend-Support-for-Advanced-Filters_621117443.html#Conditions%3A)

![advanced filters-2.png](attachments/645628037/927924241.png?width=1021)

Once all conditions are added, click **Save and Apply** to apply the filter and save it for later use. 

![advanced filters-6.png](attachments/645628037/928219138.png?width=979)

To access a saved filter later on, open the **Saved Filters** drop-down and select a filter from the list.

![advanced filters-5.png](attachments/645628037/927989763.png?width=997)

### Example Use Cases

The following are the example use cases of some custom filters.

  * **Example 1** : Create a filter where customers have a Firstname that contains the text **tes t** and their Phone number is not equal to **123**


![image-20241104-073858.png](attachments/645628037/646381569.png?width=1063)

  * **Example 2** : Find customers whose first name starts with **nabeel** and email contains **frontend,** or whose first name starts with **faraz** and email contains **core,** or whose email contains **support**

Customers who match any of the following criteria:

    * Their first name starts with **nabeel** and their email contains **frontend**

    * Their first name starts with **faraz** and their email contains **core**

    * Their email contains **support**


![advanced filter creation for example 2.png](attachments/645628037/927891457.png?width=923)![advanced filter-example2.png](attachments/645628037/927105197.png?width=1001)

Once an attribute is set as “Searchable”, it cannot be unset later on. 
