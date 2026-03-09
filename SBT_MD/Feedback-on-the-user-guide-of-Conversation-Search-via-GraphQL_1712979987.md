# CX Knowledgebase : Feedback on the user guide of Conversation Search via GraphQL

## **Structural & navigational improvements**

**a. Add a short “Getting Started” section**

Right after **Overview** , add something like:

  * **Audience** : “Intended for developers integrating with CX via GraphQL.”

  * **Endpoint** : GraphQL endpoint URL (if stable) and required HTTP method.

  * **Auth prerequisites** : “Requires a valid JWT / API token/session (link to auth doc).”

  * **Minimal query** : A very small example that just returns `id` and `creationTime` of the latest 10 conversations.




This anchors new readers before diving into operators and limitations.

**b. Introduce an explicit “API Reference” section**

Right now, the arguments of `searchConversations` are implied through examples. Add a dedicated section:

And sub‑sections:

  * `filter: ConversationFilterInput`

  * `pagination: PaginationInput`

  * `sort: SortInput`

  * `searchTerm: String`




For each, describe:

  * **Type**

  * **Is it optional?**

  * **Defaults** (e.g. default limit, offset, sort order if omitted)

  * **Interaction rules** (e.g. “`filter` and `searchTerm` are combined with logical AND”)




**c. Reformat “Allowed Filter Fields” into a table**

The current bullet list is useful but dense. A table will make it much easier to design filters:

Field| Type| Description / Example  
---|---|---  
`id`| String| Conversation ID  
`creationTime`| DateTime| ISO 8601, e.g. `"2024-01-01T00:00:00Z"`  
`customer._id`| String| Customer identifier  
`agentParticipants.username`| String| Agent username, supports partial text operators  
`wrapUps.value`| String| Wrap-up / disposition value  
`durationInSeconds`| Number| Conversation duration in seconds  
…| …| …  
  
Also, explicitly mention for each if **text operators** (`contains`, `starts_with`) are allowed, or only comparison operators.

**d. Group “Pagination” and “Sorting” into a “Result Shaping” section**

To improve flow:

Also clarify default values:

  * What is the **default**`limit` and **maximum allowed**`limit`?

  * What is the default `sortBy`/`sortOrder` if `sort` is omitted?




**e. Expand “Best Practices”**

This section is valuable but short. Suggested bullets to add:

  * Prefer **indexed fields** (like `creationTime`, `customer._id`) in filters for performance.

  * Avoid using `contains` on high-cardinality fields in very large datasets unless necessary.

  * Use **narrow time ranges** when filtering on timestamps to reduce scan size.

  * Combine `searchTerm` with structured filters (e.g. creation range + direction) for precise results.




## **Content gaps & missing clarifications**

**a. Clarify interaction between**`filter` and `searchTerm`

The doc doesn’t tell the reader how these combine:

  * Are they **ANDed** (filter by fields AND search by name)?

  * Does `searchTerm` internally expand into `OR` conditions on allowed search fields?

  * Can `searchTerm` be used together with `sort` and `pagination` (it is in example, but state it explicitly)?




Add an explicit statement such as:

> When both `filter` and `searchTerm` are provided, conversations must match **both** the structured filter and the search term.

…and perhaps a combined example:
[code] 
    query {
      searchConversations(
        searchTerm: "ahsan"
        filter: {
          and: [
            { key: "conversationDirection", operator: equal_to, value: "INBOUND" }
            { key: "creationTime", operator: greater_than_equal_to, value: "2024-01-01T00:00:00Z" }
          ]
        }
        pagination: { limit: 10, offset: 0 }
        sort: { sortBy: "creationTime", sortOrder: DESC }
      ) {
        totalDocs
        docs { id customer { firstName } creationTime }
      }
    }
[/code]

**b. Clarify default behavior more fully**

You mention:

> If no query parameters are provided, the API will return the top 10 most recent conversations based on `creationTime` in descending order.

Recommended clarifications:

  * Confirm that this is effectively:

    * `limit = 10`, `offset = 0`

    * `sortBy = "creationTime"`, `sortOrder = DESC`

  * What happens if:

    * Only `filter` is provided? (still default sort by `creationTime DESC`?)

    * Only `pagination` is provided but no `sort`? (same default sort?)

  * Is there a **max limit** to prevent abuse (e.g. 100 / 1000)?




**c. Add error handling section**

You mention “Any attempt to filter using other fields will result in a validation error”, but don’t show examples.

Add:

Also clarify behavior when:

  * `value` type doesn’t match the field type (e.g. string for a numeric field).

  * Unsupported operator is used for a field type.




**d. Add response examples**

You already give request examples; add a **short sample response** for at least one or two queries. For example, under “Search via searchTerm”:
[code] 
    {
      "data": {
        "searchConversations": {
          "totalDocs": 2,
          "limit": 10,
          "offset": 0,
          "docs": [
            {
              "customer": {
                "_id": "123",
                "firstName": "Ahsan",
                "phoneNumber": "+923001234567",
                "isAnonymous": false,
                "additionalDetail": null
              }
            },
            …
          ]
        }
      }
    }
[/code]

This helps users quickly validate that their integration works as expected.

**e. Versioning & compatibility note**

You mention:

> partial search via searchTerm is enabled by default for customer.fistName attribute in CX-4.10.5, CX-5.1 and upcoming releases on top.

Suggested improvements:

  * Correct typo: `customer.fistName` → `customer.firstName`.

  * Add a **small compatibility note/table** :




Version| `searchTerm` support  
---|---  
CX < 4.10.5| Not supported  
CX 4.10.5| Supported for `customer.firstName`  
CX 5.1+| Supported for `customer.firstName` (default enabled)  
  
  * Clarify whether users on older versions should expect a **schema error** or **ignored argument** if they pass `searchTerm`.




**f. Authentication & security**

If not covered elsewhere, add either:

  * A brief “Authentication” subsection with a link to the main auth doc, or

  * A short sentence: “All `searchConversations` requests must be authenticated. See Authentication Guide”.




Also mention:

  * Whether results are scoped by tenant / org / permissions.

  * That users only see conversations they are allowed to see (if applicable).




## **Operator & field semantics**

**a. Supported operators matrix**

Right now, “Supported Operators” is flat. It would help to show which operators work on which **field types**. For example:

Operator| String fields| Number fields| DateTime fields| Notes  
---|---|---|---|---  
`equal_to`| ✅| ✅| ✅|   
`greater_than`| ❌ / N/A| ✅| ✅|   
`contains`| ✅| ❌| ❌| Case-insensitive  
`starts_with` / `ends_with`| ✅| ❌| ❌| Strings only  
  
This prevents incorrect assumptions, especially with timestamps and numeric fields.

**b. Case-insensitivity scope**

You state:

> Partial text matches … are case insensitive.

Clarify explicitly:

  * This applies to `starts_with`, `ends_with`, `contains` on string fields.

  * `equal_to` for string fields – is it case‑sensitive or insensitive? (State clearly.)

  * `searchTerm` – confirm it is case‑insensitive as well.




If behavior differs between fields, note that.

## **5\. Limitations & performance**

**a.**`STRING_LIST` limitation

This section is good but can be a bit sharper:

  * Emphasize that behavior is **unsupported** and results are **unreliable** (not just “may” be unexpected).

  * Add a guidance sentence:

    * “If you need to search inside list values, consider normalizing your schema so that each searchable value is stored as an individual document field that can be indexed.”




You might also:

  * Add a simple **“do/don’t” example** of `conversationData` design.




**b. Indexing & performance hints**

It would help advanced users if you mention:

  * Which fields are **indexed** (if you can share that).

  * That queries combining multiple indexed fields under `AND` perform best.

  * That `contains` on large text fields may be slower than exact or prefix matches.




Even a short note like:

> For best performance, prefer filters on indexed fields such as `creationTime`, `customer._id`, and `wrapUps.value`. Avoid using `contains` on high‑cardinality fields when a more specific filter is available.

would help.

## **Consistency, naming & small fixes**

**a. Field naming consistency**

You use:

  * In filters: `customer._id`

  * In `docs` example:
[code] docs {
          id
          customer {
            id
          }
        }
[/code]




Then in `searchTerm` example:
[code] 
    customer {
      _id
      firstName
      ...
    }
[/code]

This is confusing. Suggestions:

  * Choose **one canonical field name** in the schema (either `id` or `_id`) and use it consistently in all examples, _or_

  * If both exist for a reason, explicitly explain:

    * “`_id` is the internal Mongo identifier; `id` is the GraphQL‑level ID,” etc.

  * Ensure the “Allowed Filter Fields” and examples all use the **same string** : `customer._id` vs `customer.id`.




**b. Typo fixes**

  * `customer.fistName` → `customer.firstName`.

  * Ensure all field names and capitalization in the narrative match the code listings (`creationTime`, `endTime`, etc.).




**c. Headings & capitalization**

For consistency:

  * `### Search via searchTerm (partial search):`  
→ consider “### Search via `searchTerm` (partial search)” to visually mark the argument name.

  * Ensure all section titles follow a consistent case style (e.g. Title Case or sentence case).




## **Example-focused refinements**

**a. Explain what each example demonstrates**

Before each GraphQL example, add a **one‑line explanation** :

  * “This example filters conversations by `customer._id` and direction **INBOUND**.”

  * “This example demonstrates a time range filter on `creationTime` and `endTime`.”

  * “This example shows a partial text match on `agentParticipants.username` using `contains`.”




This helps readers scan for the pattern they need.

**b. Add a combined filters + searchTerm + pagination example**

You already have separate examples; one combined example (as suggested above) will show the **typical real‑world usage**.
