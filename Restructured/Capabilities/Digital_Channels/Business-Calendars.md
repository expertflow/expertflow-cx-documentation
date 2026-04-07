---
title: "Business Calendars"
summary: "How-to guide for creating and managing Business Calendars in ExpertFlow CX — covering calendar creation, event types (business hours, out of office, holiday), recurrence, timezone handling, and linking calendars to the customer widget."

product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["business calendars", "business hours CX", "out of office calendar", "holiday schedule", "CX calendar", "customer widget hours", "operational schedule", "working hours configuration"]
aliases: ["business calendar setup", "configure business hours", "CX operational schedule"]
last-updated: 2026-03-10
---

# Business Calendars

The Business Calendars feature lets administrators define and manage operational schedules — including working hours, out-of-office periods, and holidays — and display them to customers on the web widget. Multiple calendars can be created to represent different sites, channels, or teams.

> This feature replaces the older **EF Business Calendars** module in SupervisorTools.

---

## Core Concepts

| Term | Description |
|---|---|
| **Calendar** | A container for events, typically representing the schedule of a site, channel, or team. |
| **Business Hours event** | Standard working hours or shifts. |
| **Out of Office event** | Unscheduled unavailability with an optional explanation message. |
| **Holiday event** | Scheduled closures such as public holidays. |

---

## Creating a Calendar

1. Navigate to **Business Calendars → All Calendars**.
2. Click the **+** icon to add a new calendar.
3. Provide a descriptive **Name** (e.g., `UK Support Team`).
4. Optionally add a **Description**.
5. Select a **Color** to distinguish this calendar in the list view.
6. Click **Save**.

You can create as many calendars as needed to reflect your business structure. Once created, add events to the calendar.

---

## Adding Events to a Calendar

### Business Hours Events

Use this event type for standard working shifts.

1. Open the calendar and click **+ Add Event**.
2. Select **Business Hours** as the event type.
3. Fill in:
   - **Title** (required)
   - **Start Date** (required)
   - **Shift times**: Add one or more shifts. A single event can contain multiple shift windows (e.g., morning and evening shifts).
4. Configure **Recurrence**:
   - **Does Not Repeat**: One-time event (default).
   - **Daily**: Repeats every day. Set a validity period or leave open-ended.
   - **Custom (Weekly)**: Repeats on selected days (e.g., Monday, Wednesday, Friday). Set a validity period.
5. The calendar view displays the event spanning from the earliest shift start to the latest shift end.
6. Click **Save**.

> **Shift validation**: Each shift must have an end time after its start time. Overlapping shifts across multiple windows are not validated — two shifts can share overlapping time ranges.

### Out of Office Events

Use this event type to mark unexpected or temporary unavailability.

1. Add a new event and select **Out of Office**.
2. Fill in the same fields as a Business Hours event.
3. Add an optional **Message** to explain the unavailability.
4. To mark a full day, enable **All Day** — this changes the input to a date range instead of specific times.
5. Click **Save**.

Existing Out of Office events can be updated or deleted at any time.

### Holiday Events

Use this event type for planned, recurring closures.

1. Add a new event and select **Holiday**.
2. Recurrence is limited to:
   - **Does Not Repeat**
   - **Custom**: Select specific days of the week and define a validity period.
3. The system creates holiday events only for dates within the validity period that match the recurrence pattern.
   - _Example_: A holiday recurring every Sunday from July 14 to July 22 generates events only on July 14 and July 21.
4. Click **Save**.

---

## Editing Recurring Events

Recurring events can be edited from the **Daily**, **Weekly**, or **Monthly** calendar view.

| Change type | Edit scope options |
|---|---|
| Title, Color, or Timings | "This event only" OR "All events in series" |
| Start Date, Validity Period, or Recurrence | "All events in series" only (single-event edit is removed) |

> When you change the Start Date or Validity Period, the entire series is recalculated from the new parameters.

---

## Timezone and Daylight Saving Support

- Events are stored in the creating administrator's local timezone.
- Other administrators in different timezones see events converted to their local time automatically.
- If a shift spans midnight in the viewer's timezone (e.g., an 11 PM – 8 AM shift), the calendar correctly shows it across both days. The Day and Week views always display precise start and end times.
- A browser page refresh may be required after changing timezone settings.

---

## Linking a Calendar to the Customer Widget

Business hour timings from a calendar can be displayed on the customer-facing web widget.

1. When **creating or editing a Web Channel** in Unified Admin, navigate to the **Channel** tab.
2. In the **Calendars** section, select the calendar to associate with this channel from the dropdown.
3. The default is **None** (no hours displayed).
4. Save the channel.

**How it appears to customers:**
- Business Hour event timings are shown on the widget popup form and on the pre-conversation form below the title field.
- Only **Business Hours** event types are displayed — Out of Office and Holiday events are not shown on the widget.
- If multiple Business Hour events are scheduled for the same day, the widget consolidates them: it shows the earliest start time and the latest end time across all shifts for that day.

---

## Related Articles

- [Business Calendars Limitations](Business-Calendars-Limitations.md)
- [Configuring the Customer Widget](../../How-to_Guides/Administrator/Configuring-the-Customer-Widget.md)
- [Customer Widget](Customer-Widget-Features-Capabilities.md)
