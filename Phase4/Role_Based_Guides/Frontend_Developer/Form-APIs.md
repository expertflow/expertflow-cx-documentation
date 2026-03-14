---
title: "Form APIs"
summary: "Reference for the ExpertFlow CX Form APIs — covering endpoints for creating, reading, updating, and deleting forms, as well as validating form fields."
audience: [developer]
product-area: [platform]
doc-type: reference
difficulty: intermediate
keywords: ["form API CX", "create form API CX", "get form CX", "delete form CX", "form validation API CX", "form CRUD CX"]
aliases: ["CX form API reference", "forms API CX", "form builder API CX"]
last-updated: 2026-03-10
---

# Form APIs

The Form APIs provide programmatic access to ExpertFlow CX forms — enabling external applications to create, retrieve, update, and delete forms, and to validate form field submissions.

---

## Available Endpoints

| Operation | Endpoint |
|---|---|
| **Create Form** | Create a new form definition |
| **Get Form** | Retrieve a form by ID |
| **Update Form** | Update an existing form |
| **Delete Form** | Delete a form |
| **Get Form Validations** | Validate form field values against the form schema |

---

## Use Cases

- Dynamically display pre-chat forms in custom customer widget implementations.
- Validate customer-submitted form data on the server side before creating a chat session.
- Programmatically provision forms as part of a deployment automation pipeline.

---

## API Reference

Full API specifications for all Form endpoints are available in the ExpertFlow CX API documentation:

**API Documentation**: `https://api.expertflow.com`

---

## Related Articles

- [Form Builder User Guide](../Solution_Admin/Form-Builder-User-Guide.md)
- [JavaScript SDK for Customer-Facing Channels](JavaScript-SDK.md)
- [Customer-Facing SDK for Omnichannel Communication](Customer-Facing-SDK.md)
- [Routing Engine Developer Guide](Routing-Engine-Developer-Guide.md)
