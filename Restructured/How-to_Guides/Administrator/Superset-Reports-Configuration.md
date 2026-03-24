---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# EFCX Reports Configuration (Superset)

This guide provides instructions for importing and configuring EFCX reports in Apache Superset 2.0.

## Database Connection Configuration

1. Navigate to the `databases` directory in your reporting package.
2. Open `cim_reporting_database.yaml`.
3. Update the `sqlalchemy_uri` field based on your database type:
   - **MySQL**: `mysql+mysqldb://Username:Password@ServerAddress:Port/DatabaseName`
   - **MsSQL**: `mssql+pymssql://Username:Password@ServerAddress:Port/DatabaseName`
4. Re-zip the parent folder containing the updated configuration.

## Importing Dashboards

1. Log in to the Superset Administration console (`https://server-ip:port/`).
2. Navigate to **Dashboards** -> **Import Dashboards**.
3. Select your updated `.zip` file and click **IMPORT**.

## Post-Import Configuration

### UTC Offset
Set the correct UTC offset for your reports to ensure accurate time-based data. Refer to the [UTC Offset Guide](../../Capabilities/Reporting_and_Analytics/UTC-Offset-Reports.md).

### SSL Configuration (Optional)
If your database requires SSL:
1. Copy the contents of your `myCert.cert` file.
2. In Superset, go to **Settings** -> **Database Connections**.
3. Edit your connection and go to the **Advanced** tab.
4. Paste the certificate into the **Root Certificate** field and click **Finish**.

**Note:** Do not import both MsSQL and MySQL reports on the same Superset instance.
