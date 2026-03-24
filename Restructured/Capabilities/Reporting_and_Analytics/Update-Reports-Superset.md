---
title: "Updating Historical Reports in Superset"
summary: "How-to guide for updating ExpertFlow CX historical reports in Apache Superset 2.0 after a version upgrade — covering report file selection, database connection string configuration, and dashboard import steps for MySQL and MS SQL deployments."

product-area: [channels, digital]
doc-type: how-to
difficulty: intermediate
keywords: ["Superset reports update", "Superset 2.0 reports", "historical reports upgrade", "CX Superset import", "Superset database connection", "MySQL reports Superset", "MSSQL reports Superset", "dashboard import Superset"]
aliases: ["update Superset dashboards", "import CX reports Superset", "Superset report upgrade"]
last-updated: 2026-03-10
---

# Updating Historical Reports in Superset

After each ExpertFlow CX version upgrade, the historical reports package must be updated in Apache Superset. Report files are database-specific — download and use only the file matching your deployment's database type (MySQL or MS SQL).

> **Important**: If you previously imported MySQL reports, do not import the MS SQL report file, and vice versa. Mixing report files causes import failures.

## Prerequisites

- Apache Superset 2.0 is deployed and accessible.
- You know which database type your CX reporting database uses (MySQL or MS SQL).
- You have Superset admin credentials.

---

## Step 1: Download the Correct Report File

Download the report package matching your CX version and database type from the ExpertFlow documentation resources. The zip file is versioned by CX release (e.g., `SR22`, `CX4.1`, `CX4.3`, `CX4.10`).

> If you previously imported reports for an earlier CX version, you **must remove all existing dashboards, charts, databases, and datasets** from Superset before importing the new file — unless the release notes indicate otherwise. Check the release guidance for your specific version.

---

## Step 2: Extract and Configure the Database Connection String

1. Extract (unzip) the downloaded report package.
2. Navigate to the `databases` folder inside the extracted directory.
3. Open the file `cim_reporting_database.yaml` in a text editor.
4. Locate the `sqlalchemy_uri` field and update it with your database connection string:

**MySQL format:**
```
mysql+mysqldb://Username:Password@ServerAddress:PortNumber/DatabaseName
```

**MS SQL format:**
```
mssql+pymssql://Username:Password@ServerAddress:PortNumber(Default:1433)/DatabaseName
```

Replace `Username`, `Password`, `ServerAddress`, `PortNumber`, and `DatabaseName` with your actual values. Do not modify any other fields in the YAML file.

---

## Step 3: Re-zip the Package

After saving the updated YAML file, re-zip the complete folder (including all subdirectories) into a new zip archive. This updated zip is what you will import into Superset.

---

## Step 4: Import into Superset

1. Log in to the Superset administration console at `https://<superset-server>:<port>/`.
2. Navigate to **Dashboards → Dashboard List** (or use the URL `https://<superset-server>:<port>/dashboard/list`).
3. Click the **Import dashboards** button (import icon in the top right of the dashboard list).
4. Select the updated zip file you created in Step 3.
5. Click **Import**.

---

## Step 5: Verify the Import

After the import completes, Superset will display the updated dashboards and charts. Confirm:

- All expected dashboards are present.
- Charts load without database connection errors.
- Filters and date range selectors work correctly.

If the import fails with a connection error, double-check the `sqlalchemy_uri` format and credentials in Step 2.

---

## Report Files by CX Version (MySQL)

| CX Version | Notable Changes |
|---|---|
| CX 4.1 | Added: Agent Task Detail Report, Agent Availability Report, Queue Flushed Conversation Count |
| CX 4.3 | Added: Agent State Analysis Report |
| CX 4.10 | Configuration changes — full reimport required |

For each version not listed above, assume all reports have undergone configuration changes and a full reimport is required.

---

## Related Articles

- [Superset Reports Configuration](../../How-to_Guides/Administrator/Superset-Reports-Configuration.md)
- [Superset Reports Import Config](../../How-to_Guides/Administrator/Superset-Reports-Import-Config.md)
- [Reports and Analytics](Reports-and-Analytics.md)
