---
audience: [solution-admin]
doc-type: reference
difficulty: beginner
aliases: []
---

# Adding Languages and Timezones

Expertflow CX allows you to define system-wide locales and timezones to ensure the agent interface is rendered in the user's local context.

## Configuration Path
Go to **General → Locale Settings** in the Unified Admin.

## Supported Settings

### 1. Supported Languages
You can enable the following languages for the AgentDesk UI:
- English, French, Spanish, Italian, German
- Arabic, Urdu (RTL Support)
- Bulgarian, Swahili

### 2. Default Language
Select one language from the supported list to act as the system default. The interface will automatically render in this language if the translation files are present.

### 3. Timezones
Choose the desired system timezone.
- **Current Default**: UTC.
- **Note**: Individual agent timezone overrides are handled via profile settings.

## Impact
These settings primarily impact the **AgentDesk** interface and do not currently affect customer-facing widgets (which are configured separately in the Widget settings).
