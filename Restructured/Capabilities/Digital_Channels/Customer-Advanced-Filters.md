---
title: "Customer Advanced Filters"
summary: "Explanation of the Customer Advanced Filters feature in ExpertFlow CX — how to create, save, and reuse customized customer list filters using AND/OR conditions for contact segmentation and outbound campaigns."

product-area: [channels, digital]
doc-type: explanation
difficulty: beginner
keywords: ["customer advanced filters", "customer list filter", "customer segmentation CX", "CX filter conditions", "AND OR filter", "customer search filter", "searchable attribute", "contact segmentation"]
aliases: ["advanced customer filter", "customer search CX", "filter customer list"]
last-updated: 2026-03-10
---

# Customer Advanced Filters

The Customer Advanced Filters feature allows administrators and agents to build customized customer list views using AND/OR filter conditions. These saved filters can be reused for contact segmentation, targeted outbound campaigns, and reporting purposes.

## How It Works

Filters are built from **customer attributes** that are marked as **Searchable**. The filter engine supports AND/OR logic to combine multiple conditions into a precise query.

### Searchable Attributes

An attribute must be marked as **Searchable** before it can be used in a filter. The following attributes are searchable by default:

| Attribute | Notes |
|---|---|
| `firstName` | Searchable by default |
| `phoneNumber` | Searchable by default |
| `labels` | Searchable by default |

Custom attributes can be marked as Searchable at creation time or by editing an existing attribute. Once an attribute is set as Searchable, it cannot be reverted to non-searchable.

## Creating an Advanced Filter

1. Navigate to the **Customer List** from the main menu.
2. Click the **Advanced Filter** button.
3. Define a **title** (filter name) for later reference.
4. Add one or more conditions. For each condition, select:
   - The **attribute** to filter on
   - The **condition operator** (depends on the attribute's data type)
   - The **value** to match
5. Combine conditions using **AND** (all must match) or **OR** (any can match).
6. Click **Save and Apply** to apply the filter immediately and save it for future use.

### Condition Operators by Attribute Type

| Attribute Type | Available Operators |
|---|---|
| String | Starts with, Ends with, Contains, Equal to |
| Boolean | Equal to, Not Equal |

## Accessing Saved Filters

1. Open the **Customer List**.
2. Click the **Saved Filters** dropdown.
3. Select a previously saved filter from the list.

The customer list updates to show only matching customers.

## Example Use Cases

**Example 1 — Exact match with exclusion:**
Find customers whose first name contains "test" AND phone number is not equal to "123".

**Example 2 — Multi-condition OR segmentation:**
Find customers whose:
- First name starts with "nabeel" AND email contains "frontend"
- OR first name starts with "faraz" AND email contains "core"
- OR email contains "support"

This type of filter can be saved and reused when running targeted campaigns against specific customer segments.

## Related Articles

- [Customer Labels](Customer-Labels.md)
- [Managing Outbound Campaigns](../../How-to_Guides/Administrator/Managing-Outbound-Campaigns.md)
- [Customer Interaction Profiles Overview](../../How-to_Guides/Administrator/Customer-Interaction-Profiles-Overview.md)
