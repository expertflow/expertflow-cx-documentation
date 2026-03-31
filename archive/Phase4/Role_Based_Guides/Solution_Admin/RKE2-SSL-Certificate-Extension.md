---
audience: [solution-admin]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Extending RKE2 SSL Certificate Expiry

This procedure describes how to extend the lifetime of self-signed RKE2/K3s certificates from the default 365 days to 10 years (3650 days) for existing deployments.

## Important Note
**Downtime is involved.** This process requires stopping the RKE2 server service. Plan for a maintenance window.

## Procedure

1. **Update Configuration**:
   Add the expiration override to the RKE2 default configuration file.
   ```bash
   echo "CATTLE_NEW_SIGNED_CERT_EXPIRATION_DAYS=3650" >> /etc/default/rke2-server
   ```

2. **Stop RKE2 Service**:
   ```bash
   systemctl stop rke2-server
   ```

3. **Rotate Certificates**:
   Manually trigger the rotation to generate the new long-life certificates.
   ```bash
   rke2 certificate rotate
   ```

4. **Restart RKE2 Service**:
   ```bash
   systemctl start rke2-server
   ```

5. **Verify**:
   Check the new expiration dates in the certificate table.
   ```bash
   rke2 certificate check --output table
   ```

## References
- [Official SUSE/RKE2 Support KB](https://support.scc.suse.com/s/kb/How-to-extend-RKE2-K3s-self-signed-certificate-expiration?language=en_US)
