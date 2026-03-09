# CX Knowledgebase : Business Features

The basic business features of VRS are to record Cisco voice calls and give users the ability to search and play them.

### Call Recording:

VRS can record Cisco contact center calls for up to 100 concurrent agents

### Search Recordings on VRS UI:

![](attachments/thumbnails/917618/921020)

### Playback Recordings:

![](attachments/thumbnails/917618/921015)

### Downloading:

![](attachments/thumbnails/917618/921017)

### **Call Recording Encryption:**

Encrypted recorded files. Unable to be opened or played directly.   


![Screenshot from 2025-03-17 15-25-56.png](attachments/918121/969474254.png?width=838)

### **Archival Service:**

Optimize storage and ensure seamless voice recording management with the Archival Service. 

![Screenshot from 2025-03-17 15-30-53.png](attachments/918121/969801935.png?width=852)

### **Pause and Resume Recording for Compliance:**

Enhance security and achieve PCI DSS compliance with the **Pause and Resume Recording** feature keeping sensitive information hidden. 

![image-20241104-053630.png](attachments/918121/970063936.png?width=604)

### **Audit Logs for Security & Compliance:**

Improve security monitoring, compliance, and troubleshooting with the **Audit Logs** feature. 

![image-20250317-103919.png](attachments/918121/970391618.png?width=812)

### **Screen Recording for Enhanced Interaction Monitoring;**

Capturing agents’ on-screen activities during customer interactions, providing a comprehensive view of engagements.

![Screenshot from 2025-03-17 16-03-55.png](attachments/918121/969900159.png?width=894)![Screenshot from 2025-03-17 16-08-17.png](attachments/918121/970457221.png?width=886)

### **High Availability for Uninterrupted Recording:**

The Voice Recording Solution now supports **High Availability (HA)** to ensure continuous recording and seamless failover. Two SIP trunks are configured on CUCM in HA mode, directing call events to two VRS servers. If one server becomes unavailable, call traffic automatically switches to the second, preventing disruptions.

To optimize storage, a **Replay Server** with higher capacity centralizes recordings, with an automated **rsync** job transferring files from VRS Servers A and B. A configurable retention policy ensures efficient storage management by automatically deleting older recordings from VRS servers after a set period.
