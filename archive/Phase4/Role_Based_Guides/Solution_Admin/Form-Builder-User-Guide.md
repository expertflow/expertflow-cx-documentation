---
title: "Form Builder User Guide"
summary: "How-to guide for creating and managing forms in ExpertFlow CX Form Builder — covering form structure (sections, questions, weightage), all question types (Input, Options, Textarea), character limits, audio attachments, and restrictions."
audience: [solution-admin]
product-area: [channels, digital]
doc-type: how-to
difficulty: beginner
keywords: ["form builder CX", "create form CX", "survey form CX", "pre-chat form CX", "QM form CX", "form questions CX", "form weightage CX", "form builder user guide CX"]
aliases: ["CX form builder", "build form CX", "form creation CX", "questionnaire builder CX"]
last-updated: 2026-03-10
---

# Form Builder User Guide

The Form Builder in ExpertFlow CX enables administrators to create forms for multiple use cases — pre-chat data collection, post-interaction surveys, and Quality Management (QM) evaluations — all from a single interface.

> **Form types are deprecated as of CX 4.10.** A form you create is no longer limited to a single use case. The same form can be used as a pre-chat form, a survey, or a QM evaluation form.

---

## Form Structure

Every form is composed of the following hierarchy:

```
Form
└── Section(s)
    └── Question(s) [Attributes]
        └── Option(s) [for MCQ / Dropdown / Checkbox types]
```

| Element | Description |
|---|---|
| **Form** | The top-level container. Has a title, description, and optional weightage. |
| **Section** | Groups related questions. Optional by default; mandatory when weightage is enabled. |
| **Question (Attribute)** | An individual question on the form. Has a label, help text, type, and optional weightage. |
| **Option** | A selectable answer for MCQ, Dropdown, Checkbox, Star Rating, and NPS questions. |

---

## Create a Form

1. Navigate to **Unified Admin → Form Builder**.
2. Click **New Form**.
3. Enter a **Form Title** (max 500 characters) and optional **Description** (max 1000 characters).
4. Enable **Sections** if you want to group questions, or enable **Weightage** if you need scored evaluation.
5. Add questions using the **Add Question** button. Configure each question's type, label, and settings.
6. Save.

---

## Question Types

### Input Questions

Use for free-text or structured data entry.

| Value Type | Description |
|---|---|
| `alphaNumeric` | Alphanumeric characters only |
| `alphaNumericSpecial` | Alphanumeric plus special characters |
| `email` | Email address format |
| `number` | Numeric value |
| `phoneNumber` | Phone number format |
| `password` | Masked input |
| `positiveNumber` | Positive numeric value only |
| `url` | URL format |
| `IP` | IP address (with or without port) |
| `date` | Date picker |
| `time` | Time picker |
| `dateTime` | Date and time picker |
| `shortAnswer` | Short sentence (single line) |
| `file` | Media file upload |

**File upload configuration** (for `file` type):

| Field | Description |
|---|---|
| `restrictFile` | Set `true` to enforce file type validation |
| `fileExtension` | Allowed extensions (e.g., `["PNG", "JPG", "PDF"]`) |
| `fileNumber` | Maximum number of files (1–10) |
| `fileSize` | Maximum file size in MB |

### Options Questions

Use for single-select or multiple-select choices.

| Value Type | HTML Type | Selection |
|---|---|---|
| `boolean` | Yes/No | Single select |
| `mcqs` | Multiple Choice | Single select |
| `checkbox` | Checkboxes | Multiple select |
| `dropdown` | Dropdown list | Single select |
| `5-star-rating` | 5-Star Rating | Single select |
| `nps` | Net Promoter Score (0–10) | Single select |

### Textarea Questions

| Value Type | Description |
|---|---|
| `paragraph` | Long-form text (multi-line input) |

---

## Weightage

Weighted forms score responses numerically. Enable weightage at the form level to activate scoring.

**How weightage is calculated:**

```
Question Score = (Question Weightage / 100) × Section Weightage
```

**Example:**

```
Form [100]
└── Section 1 [30]
│   ├── Question 1 [20]  →  20/100 × 30 = 6 points
│   ├── Question 2 [40]  →  40/100 × 30 = 12 points
│   └── Question 3 [40]  →  40/100 × 30 = 12 points
└── Section 2 [40]
│   ├── Question 1 [50]  →  50/100 × 40 = 20 points
│   └── Question 2 [50]  →  50/100 × 40 = 20 points
└── Section 3 [30]
    ├── Question 1 [30]  →  30/100 × 30 = 9 points
    ├── Question 2 [30]  →  30/100 × 30 = 9 points
    └── Question 3 [40]  →  40/100 × 30 = 12 points
```

**Weightage rules:**
- Weightage values range from **0% to 100%**.
- Weightage only applies to **MCQ** and **Dropdown** question types (single select).
- Option-level weightage defines the score contribution of each selectable option.
- When weightage is enabled, only MCQ and Dropdown question types are permitted in the form.

---

## Audio Prompts on Questions

Each question can have an **audio file attachment** for IVR prompt use cases:

- Attach up to one audio file per question.
- Supported format: **MP3** only.
- Maximum file size: **5 MB**.

---

## Character Limits

| Field | Maximum Characters |
|---|---|
| Form Title | 500 |
| Form Description | 1000 |
| Section Name | 500 |
| Section Description | 500 |
| Attribute Label | 500 |
| Attribute Helping Text | 100 |
| Category Label | 500 |
| Option Label | 500 |

---

## Form Builder Restrictions

| Feature | Default | Notes |
|---|---|---|
| **Sections** | Disabled | Can be enabled manually. Automatically enabled when weightage is turned on. |
| **Weightage** | Disabled | Can be enabled. When enabled, only MCQ and Dropdown types are allowed. |
| **Multiple Choice Categories** | Enabled | Can be disabled. Only available for Checkbox-type questions. |
| **Single Select** | N/A | Applies to MCQ and Dropdown questions. |
| **Multiple Select** | N/A | Applies to Checkbox questions only. |

---

## Related Articles

- [Creating Survey Forms and Flows](../Designer/Creating-Survey-Forms-and-Flows.md)
- [Designing Evaluation Forms](../Quality_Management/Designing-Evaluation-Forms.md)
- [Configuring the Customer Widget](Configuring-the-Customer-Widget.md)
- [Configuring Wrap-up Forms](Configuring-Wrap-up-Forms.md)
