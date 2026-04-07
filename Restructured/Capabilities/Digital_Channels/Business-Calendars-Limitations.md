---
title: "Business Calendars Limitations"
summary: "Reference listing known limitations of the Business Calendars feature in ExpertFlow CX — covering event scope, shift constraints, recurrence limits, overnight shifts, and customer widget display restrictions."

product-area: [channels, digital]
doc-type: reference
difficulty: beginner
keywords: ["business calendar limitations", "business hours limitations", "CX calendar known issues", "calendar recurrence limit", "overnight shift limitation", "business calendar restrictions"]
aliases: ["calendar limitations", "business hours known issues", "CX calendar constraints"]
last-updated: 2026-03-10
---

# Business Calendars Limitations

This page documents known limitations of the Business Calendars feature in ExpertFlow CX.

## Event and Calendar Scope

- An event can belong to **only one calendar** at a time. There is no shared event across multiple calendars.
- The UI displays events for a **single selected calendar** at a time. To view events on multiple calendars, switch between them manually.

## Shift Constraints

- Shifts can only span a **single calendar day**. If a shift extends beyond midnight into the next day, create a separate event for the continuation on the following day.
- **Overnight shifts** (e.g., night shifts that span two dates) are not supported. All shift times must start and end within the same 24-hour period.
- Each individual shift is validated: a shift's end time must be after its start time. A shift from 10:00 AM to 08:00 AM will be rejected.
- **Cross-shift validation is not enforced**: two shifts within the same event can have overlapping time ranges (e.g., 10:00 AM – 4:00 PM and 2:00 PM – 10:00 PM is valid). The system will calculate the overall event span as the earliest start to the latest end (10:00 AM – 10:00 PM in this example).

## Recurrence Limits

- The system supports a maximum of **365 occurrences** per recurring event, regardless of validity period.
  - A daily event starting July 24, 2024 with a validity period until December 24, 2025 will only generate 365 events.
  - A weekly event repeating every Friday generates 4 events/month and 52 events/year. At 365 occurrences, the series extends approximately 7 years.
- **Indefinite ("never-ending") recurrence is not supported.** All recurring events must have a defined validity period.

## Editing Recurring Events

- If you change the **Start Date**, **Validity Period**, or **Recurrence** pattern of an event, the option to edit "this event only" is removed. The entire series is updated from the new parameters.

## Permissions

- Role-based permissions for Business Calendars have not yet been implemented in Keycloak. Until implemented, calendar management is not restricted by Keycloak roles.

## Customer Widget Display

- Only **Business Hours** event types are shown on the customer widget. Out of Office and Holiday events are not displayed to customers.
- When multiple Business Hour events exist for the same day, the widget consolidates them to show the **minimum start time** and **maximum end time** across all shifts — individual shift windows are not shown separately.

## Related Articles

- [Business Calendars](Business-Calendars.md)
- [Customer Widget](Customer-Widget-Features-Capabilities.md)
