# CX Knowledgebase : Backend Support for Advanced Filters

## What are Advanced Filters:

To provide users with greater flexibility and control over the customers data, advance filters have been introduced in system that when applied, returns us only those customers that fits the criteria.

### More about Filter Object:

The filter object has two primary fields:

  1. Filter Name - Always unique and case sensitive

  2. Filter Query - A complex query containing multiple query conditions combined together with _“and”, “or“._ The query is a string with predefined JSON syntax.




### Attributes that can be used in filters:

By default, following customerSchema attributes are set “isSearchAble = true” and can be used in filters:

  1. firstName

  2. phoneNumber

  3. labels




To use any other customerSchema attribute in filters, first one must edit the customerSchema attribute and set “isSearchAble” to “true”.

Note: To enhance system performance and reduce the filter execution time, only those customer attributes can be used in filter queries whose _“isSearchAble”_ flag is set to _“true”._

## Filter Query Syntax Guidelines:

### Logical Operators:

  1. Use `"or"` and `"and"` keys to define logical groupings. Each should hold an array of conditions or nested groups.




Example:
[code] 
    { "or": [ <condition1>, <condition2>, { "and": [ <condition3>, <condition4> ] } ] }
[/code]

### Conditions:

  1. Define each condition as an object with the _field name as the key_ and an _operation-object as the value_.

  2. Supported operators:

     * **equalTo** : Exact match with the specified value.

     * **notEqualTo** : Match if the value does not equal the specified value.

     * **greaterThan** : Match if the value is greater than the specified value.

     * **greaterThanOrEqualTo** : Match if the value is greater than or equal to the specified value.

     * **lessThan** : Match if the value is less than the specified value.

     * **lessThanOrEqualTo** : Match if the value is less than or equal to the specified value.

     * **startsWith** : Match if the string begins with the specified characters.

     * **endsWith** : Match if the string ends with the specified characters.

     * **contains** : Partial match within a string containing the specified substring.

     * **notContains** : Match if the string does not contain the specified substring.

     * **isEmpty** : Match if the field has no value or is empty.

     * **isNotEmpty** : Match if the field has a value or is not empty.




Examples usage each operator:
[code] 
    { "firstName": { "equalTo": "Faraz" } }
    { "status": { "notEqualTo": "inactive" } }
    { "age": { "greaterThan": 25 } }
    { "age": { "greaterThanOrEqualTo": 18 } }
    { "price": { "lessThan": 100 } }
    { "price": { "lessThanOrEqualTo": 50 } }
    { "phoneNumber": { "startsWith": "123" } }
    { "email": { "endsWith": "@example.com" } }
    { "description": { "contains": "urgent" } }
    { "notes": { "notContains": "confidential" } }
    { "middleName": { "isEmpty": true } }
    { "lastName": { "isNotEmpty": true } }
[/code]

### Nested Queries:

Conditions can be nested within `"and"` or `"or"` arrays to create more complex filters.

Example Structure:

A query with both `"or"` and `"and"` conditions:
[code] 
    {
      "or": [
        { "field1": { "equalTo": "value1" } },
        {
          "and": [
            { "field2": { "contains": "value2" } },
            { "field3": { "equalTo": "value3" } }
          ]
        },
        { "field4": { "startsWith": "value4" } }
      ]
    }
[/code]

### Filters CRUD APIs:

GraphQL is used in implementation of all the filter crud APIs. Following are the APIs available:

  1. CreateFilter API:


![image-20241025-103810.png](attachments/621117443/620691512.png?width=1017)

  2. getFilterByName:


![image-20241025-103903.png](attachments/621117443/621019187.png?width=1017)

  3. getFilterByID:


![image-20241025-104016.png](attachments/621117443/621412373.png?width=1017)

  4. getAllFilters (paginated response):


![image-20241025-104528.png](attachments/621117443/620822569.png?width=1017)

  5. updateFilterByID:


![image-20241025-104241.png](attachments/621117443/621936671.png?width=1017)

  6. deleteFilterByID:


![image-20241025-104335.png](attachments/621117443/621477922.png?width=1017)

Want to try the filters CRUD yourself?Check this postman collection and get some hands on the APIs:

[https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/folder/8262326-3e19d0c1-793b-4ee1-901e-94ac07aeae8c](https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/folder/8262326-3e19d0c1-793b-4ee1-901e-94ac07aeae8c)

## Using Filters to Get the Customers' Profiles:

We have provide a new GraphQL based API that takes filterQuery (either takken from saved filter or newly made at runtime) as a parameter and in return provides us paginated response of customers’ profiles.

Here is how this API look like:

  1. getCustomerByFilterQuery:


![image-20241025-105655.png](attachments/621117443/621510670.png?width=1122)

Note: All the constraints that have been mentioned for filterQuery in Filters section also apply to the filterQuery passed in this API.

Want to use this API? checkout this postman collection:

<https://expertflow.postman.co/workspace/Expertflow~f8480e26-6001-4a5f-8435-d0adbf5d7f5c/folder/8262326-38f3ba06-9227-41e4-8c26-b4adc892dc01>
