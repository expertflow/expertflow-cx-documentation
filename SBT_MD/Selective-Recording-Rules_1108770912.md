# CX Knowledgebase : Selective Recording Rules

Recording Rules are the rules which will be used to Record/Do Not Record a specific call which satisfies the Mask.  
This feature enables users to create, edit and delete recording rules based on a Rule Mask.  


![image-20250527-144756.png](attachments/1108770912/1109164052.png?width=1349)

Here is the Add Rule page

![image-20250527-152633.png](attachments/1108770912/1108279420.png?width=663)

**Rule Priority:** All the displayed rules are shown based on priority. The Top Rule will have the highest Priority. If two rules are in conflict, the one with higher priority will be prioritized.

**Rule:** Record/Do Not Record.  
**Rule Type:** Phone Number

**Rule Mask:** The rule against which the decision is made to either Record or Do Not Record a call.

Valid Formats for Mask:   
123* : Phone numbers which start with 123

*123*: Phone numbers which have consecutive 123 in between

*123: Phone numbers which end with 123

123??: Last two digit wild card

123?: Last digit wild card

**Days of Week:** Select the days for which the rule is applicable   
**From/To Time: 00:00 - 23:59** time interval in which rule is applicable

**Screen Capture:** User Based decision  


**Features:**

  1. **Add Button:** Create a new recording rule. A new added rule will have the lowest priority.

  2. **Edit Button:** Edit all the values of a rule.

  3. **Delete Button:** Delete an existing rule.

  4. **Infinite Scroll:** Recording Rules are fetched dynamically on scroll, resulting in fast load times and a better experience. When all rules are fetched, the scroll will end.

  5. **Drag and Drop:** A Rule can be dragged and dropped to it desired priority.




### Limitations

  * Screen Capture Usage: As of now the screen capture Usage is at 100% which is not configurable. 



