# Broken Links Tracker

> Last updated: 2026-04-07 — all items from the previous list have been fixed.
> `onBrokenLinks` in `docusaurus.config.js` is now set to `'throw'` so future broken links will fail the build.

## Fixed in this session

### Root Cause 1 — Files moved to new sections, references not updated

- [x] `Capabilities/Conversation-View.md` — 3 links: `../../How-to_Guides/...` → `../How-to_Guides/...`
- [x] `Capabilities/Workforce_Management/Workforce-Management-Overview.md` — `Platform_Overview/WFM-Compatibility-Guide` → `Reference/WFM-Compatibility-Guide`
- [x] `Capabilities/Reporting_and_Analytics/Real-time-Contact-Center-Analytics.md` — `Digital_Channels/Agent-Hand-Raise` → `How-to_Guides/Agent/Agent-Hand-Raise`
- [x] `Capabilities/Voice_and_Video/Voice-Recording-and-Compliance-Features.md` — `Dialer-Performance-Benchmarks.md` → `Reference/Dialer-Performance-Benchmarks`
- [x] `Platform_Overview/Voice-Recording-and-Compliance-Features.md` — same Dialer-Performance-Benchmarks fix
- [x] `How-to_Guides/Administrator/Priority-Routing.md` — `Digital_Channels/Customer-Labels` → `Customer_Management/Customer-Labels`
- [x] `How-to_Guides/Supervisor_and_QA_Lead/Handle-Voice-Recording.md` — `Digital_Channels/Conversation-View` → `Capabilities/Conversation-View`
- [x] `How-to_Guides/Administrator/Routing-Strategy-Pull-Mode.md` — flat `Twitter-Channel-Overview` / `Email-Channel-Overview` → `Twitter/index.md` / `Email/index.md`
- [x] `How-to_Guides/Administrator/LinkedIn-Account-Onboarding.md` — `LinkedIn-Channel-Overview.md` → `Capabilities/Digital_Channels/LinkedIn/index.md`
- [x] `How-to_Guides/Administrator/LinkedIn-Configuration-Guide.md` — same LinkedIn fix
- [x] `How-to_Guides/Administrator/Twitter-Configuration-Guide.md` — `Twitter-Channel-Overview.md` → `Capabilities/Digital_Channels/Twitter/index.md`
- [x] `Getting_Started/For_Platform_Operators/index.md` — `How-to_Guides/Platform_Operator/Hardware-Sizing-Calculator` → `Reference/Architecture_and_Infrastructure/Hardware-Sizing-Calculator`

### Root Cause 2 — Digital_Channels/index.md flat-file model vs. subfolder reality

- [x] `Capabilities/Digital_Channels/index.md` — rewrote Social Media and Email tables to use correct subfolder and cross-section paths
- [x] `Capabilities/Digital_Channels/Channel-Features.md` — fixed 5 links (Conversation-View, Consult-Transfer, Agent-Hand-Raise, Customer-Labels, Customer-Advanced-Filters)
- [x] `Capabilities/Digital_Channels/Email/index.md` — `Email-Limitations.md` → `../Email-Limitations.md`
- [x] `Capabilities/Digital_Channels/Email-Configuration-IMAP-SMTP.md` — `Email-Channel-Overview.md` → `Email/index.md`
- [x] `Capabilities/Digital_Channels/Email-Configuration-MS-Exchange.md` — same Email fix

### Root Cause 3 — Quick-start files linked by name, implemented as index.md

- [x] `Getting_Started/index.md` — all 5 `*-Quick-Start.md` links changed to folder paths (e.g., `For_Supervisors_and_QA_Leads/`)
- [x] `How-to_Guides/Supervisor_and_QA_Lead/Silent-Monitoring.md` — `Supervisor-and-QA-Lead-Quick-Start.md` → `Monitoring-Your-Team-in-Real-Time.md`

### Root Cause 4 — Conversation-Studio-Configuration-Guide.md never created

- [x] `Getting_Started/For_Conversation_Designers/index.md` — replaced with `How-to_Guides/Conversation_Designer/Conversation-Studio-Authoring.md`
- [x] `Capabilities/Digital_Channels/WhatsApp/index.md` — replaced with `How-to_Guides/Conversation_Designer/Conversation-Studio-Authoring.md`

### Fix 5 — Prevent recurrence

- [x] `docs-site/docusaurus.config.js` — changed `onBrokenLinks: 'warn'` to `onBrokenLinks: 'throw'`

## Open items

> None known. Run `npm run build` in `docs-site/` to confirm clean build.
