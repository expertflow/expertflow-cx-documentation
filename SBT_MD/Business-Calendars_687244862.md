# CX Knowledgebase : Business Calendars

The Business Calendars feature allows administrators to define and manage operational schedules, including working hours, holidays, and out-of-office periods. Businesses can create multiple, distinct calendars to represent the schedules of different sites, channels, or teams.

A key benefit is the ability to communicate active working hours to customers, setting clear expectations for availability. 

This feature replaces the older **EF Business Calendars** module in **SupervisorTools**.

Each event in a calendar is of one of the following types:

  * Business hour

  * Out of office

  * Holiday




## **Core Concepts: Calendars and Events**

A **Calendar** is a container for events, typically representing the schedule for a specific site, channel, or operational unit. **Events** are**** individual entries within a calendar. There are three event types:

  * **Business Hours:** Standard working hours and shifts.

  * **Out of Office:** Periods when staff are unexpectedly unavailable.

  * **Holiday:** Scheduled days off, such as public holidays. 


![Screenshot from 2024-07-15 16-14-21.png](attachments/687244862/687244892.png?width=571)

## **Creating a Calendar**

  1. Navigate to the **All Calendars** list.

  2. Click the **+** icon to add a new calendar.

  3. Provide a descriptive **Name**.

  4. (Optional) Add a **Description**.

  5. Select a **Color** to easily identify the calendar in the list.

  6. You can create as many calendars as needed to reflect your business structure.




Once a calendar is created, you can begin adding events to it.

### **Managing Events in a Calendar**

#### **Business Hours Events**

Use this event type to define standard shift patterns.

  * **Mandatory Fields:** `Title` and `Start Date`.

  * **Multiple Shifts:** A single event can contain multiple shifts (e.g., a morning shift and an evening shift). On the calendar view, the event will span from the start of the earliest shift to the end of the latest shift.

  * **Recurrence:** Configure how the event repeats:

    * **Does Not Repeat:** A one-time event (default).

    * **Daily:** Repeats every day. You can set a validity period or have it repeat indefinitely.

    * **Custom (Weekly):** Repeats on specific days of the week (e.g., every Monday, Wednesday, Friday).

  * **Calendar Assignment:** Each event is assigned to a single calendar during creation.


![image-20250313-071817.png](attachments/687244862/963969061.png?width=554)

#### **Out of Office Events**

Use this event type to mark unscheduled or unexpected unavailability.

  * It includes all the fields and recurrence options of a Business Hours event.

  * **Additional Field:** A `Message` to provide context for the unavailability.

  * **All-Day Option:** You can mark the event for an entire day. When selected, you specify a date range instead of specific start and end times.




An admin can update or delete that particular event as well.

![image-20250313-065843.png](attachments/687244862/963936262.png?width=554)

Creating an Out Of Office Event

#### **Holiday Events**

Use this event type for scheduled closures.

  * **Recurrence Options:** Limited to **Does Not Repeat** and **Custom**.

  * **Date Range:** When using "Custom" recurrence (e.g., every Sunday), you define a validity period. The system will only create events for the recurring days that fall within that range.

    * _Example:_ A holiday recurring every Sunday from July 14th to July 22nd will only create events on July 14th and July 21st.


![image-20250313-065925.png](attachments/687244862/963706977.png?width=555)

Creating a Holiday Event

The user will be able to update title / colour and timings of a single event and will be able to see the option for this event or all events. However, if the admin changes the start date / validity period / Recurrence , the option for editing this event will not be there, and the event will be updated as per the selected date, validity period, and recurrence. 

For example, if we have an event starting from Dec 16 and ending at 25 December and ifwe changed the start Date to 18 then option for selecting this event will be gone and update all events will be seen and updated events will take effect starting from 18 december to 25th of December.

### **Calendar Views & Editing**

Administrators can view events in **Daily, Weekly, or Monthly** views and make edits directly from these views.

#### **Important Note on Editing Recurring Events:**

  * Editing basic details like `Title`, `Color`, or `Timings` allows you to apply the change to **this event only** or to **all events** in the series.

  * However, if you change the `Start Date`, `Validity Period`, or `Recurrence` pattern, the option to edit "this event only" is removed. The entire series of events will be updated based on the new parameters.




#### **Timezone & Daylight Savings Support**

The system automatically handles timezone conversions for global teams.

  * Events are created in the administrator's local timezone.

  * Other administrators in different timezones will see the event timings converted to their own local time.

  * If an event spans two days in a viewer's timezone (e.g., an 11 PM - 8 AM shift), the calendar will display it correctly across both days. The precise timings are always visible in the Day or Week view.

  * A page refresh may be required for the front-end to update and display times according to a new timezone.




#### **Displaying Hours on the Customer Widget**

Once calendars are populated with events, they can be linked to customer-facing channels.

  1. While **creating a new Web Channel** , navigate to the **Channel Tab**.

  2. In the **Calendars** section, a dropdown list will display all available calendars.

  3. Select the appropriate calendar to display its hours on the web widget.

  4. The default selection is **"None"** if you do not wish to show any hours.


![BCCalendarList.png](attachments/687244862/976519287.png?width=602)

#### **How it Works:**

  * The shift timings from the selected calendar are displayed on the customer widget for the associated **Service Identifier**.

  * Timings are visible on the **widget pop-up form** and the **pre-conversation form** below the title field.




For now, only **Business Hour** events are displayed on the customer widget. If multiple business-hour events are scheduled for the same day, they are consolidated. The widget will show the earliest start time and the latest end time of all shifts for that day.

![BC-1.png](attachments/687244862/976322886.png?width=276)
