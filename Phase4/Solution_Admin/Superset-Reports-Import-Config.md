---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Superset Reports Configuration (Import & SSL)

This guide details the process for importing reports into Apache Superset 2.0 and configuring SSL for database connections.

## 1. Import Dashboards
1. Download the correct report package for your database (MsSQL or MySQL).
2. **Important**: Do not import both MsSQL and MySQL reports on the same server.
3. Unzip the package and navigate to the `databases` directory.
4. Edit `cim_reporting_database.yaml`:
   - Update `sqlalchemy_uri` with your connection string.
   - **MySQL**: `mysql+mysqldb://User:Pass@Host:Port/DB`
   - **MsSQL**: `mssql+pymssql://User:Pass@Host:Port/DB`
5. Re-zip the parent folder.
6. In Superset, go to **Import Dashboards**, select your zip file, and click **IMPORT**.

## 2. Post-Import Settings
- **UTC Offset**: Set the correct UTC offset for your reports to ensure accurate time-based data.
- **Old Reports**: If you need to replace existing reports, follow the cleanup guide before re-importing.

## 3. SSL Configuration
If your database requires SSL:
1. Open your `myCert.cert` file and copy the text.
2. In Superset, go to **Settings > Database Connection**.
3. Edit your connection, go to the **Advanced Tab**, and paste the certificate into the **Root Certificate** field.
4. Click **Finish** to save.

For more details on enabling Alerts and Reports, see the [Superset Alerts Guide](../Archive-Notice.md).
