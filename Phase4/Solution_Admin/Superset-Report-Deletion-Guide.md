---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Deleting Reports from Superset 2.0

This procedure details how to completely remove EFCX reports and database connections from Apache Superset to prepare for a clean re-import.

## Procedure

1. **Delete Dashboards**:
   - Go to the **Dashboards** menu.
   - Click **Bulk Select**, check all dashboards, and click **DELETE**.
   - Type `DELETE` in the confirmation box to finalize.

2. **Delete Charts**:
   - Go to the **Charts** menu.
   - Select all items and follow the same deletion process as dashboards.

3. **Delete Datasets**:
   - Go to the **Datasets** menu and remove all linked datasets.

4. **Delete Database Connection**:
   - Navigate to **Settings > Database Connections**.
   - Click the **Delete** icon next to the EFCX database (e.g., `cim_reporting`).
   - Type `DELETE` to confirm.

## Result
All EFCX reporting metadata and connections are now removed. You may now proceed with importing a new package via the [Superset Import Guide](../Archive-Notice.md).
