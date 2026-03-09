# CX Knowledgebase : Business Calendars Limitations

  * An event can be a part of a single calendar at the moment.

  * Admin can view events of a single calendar on the User Interface and if there are multiple calendar with multiple events, admin can check the respective calendar to view the events of that particular calendar.

  * Shifts can only span a **single** day. If a shift extends into the next day, the admin should create a new event for the following day.

Multiple shifts can be scheduled, but these shifts must be validated individually. For example, a shift cannot be scheduled from 10:00 A.M. to 08:00 A.M.; the system will throw a validation error stating that the end time cannot be before the start time. This validation applies to individual shifts but not across multiple shifts. For instance, one shift can be from 10:00 A.M. to 04:00 P.M., and another shift can be from 02:00 P.M. to 10:00 P.M.

  * Details of each shift will be visible in the event preview dialog, including the title, timings, event date, etc.

  * The event minimum time will be considered the start time of all shifts, and the end time will be the highest time of all shifts. For example, with the above two shifts, the start time of the contact center will be 10:00 A.M., and the end time will be 10:00 P.M.

  * In recurring events, if the recurrence is set to **custom Date** such as the validity period is set in such a way that it exceeds **365 occurrences,** the system will ignore those extra occurrences. For example, if the recurrence is set to **daily** with a start date of July 24, 2024, and the validity period is until December 24, 2025, the system will only generate 365 events no matter what is the validity period.

  * Similarly, if the recurrence is set to **weekly** and an event is to be repeated on Friday, then it will have four events in a month and 52 events in a year. This event will continue to repeat for approximately the next 7 years, given the limit of 365 occurrences.

  * We do not support the events to be created for **unlimited time period such as never.**

  * Permissions related to Business calendars are yet to be implemented on Key Cloak side and will be implemented on Business calendars side along with it. 

  * Events with day night shift or spanning into next day are not supported for now. Events can be created only withing 24 hours of the day.

  * We support to show to only Business hour Type events timings on customer widget at the moment. If multiple business hours events are created for today then these shifts will be grouped and minimum shift start time and maximum shift end time will be shown on the customer widget. 



