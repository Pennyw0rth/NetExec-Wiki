# 🆕 Enumerate Primary Site Server and Distribution Point via recon6

The **Primary Site Servers** and **Distribution Points** of an SCCM infrastructure expose information to remote authenticated users via the registry hive **HKLM\SOFTWARE\Microsoft\SMS**.

```bash
nxc smb IP_PSS -u username -p password -M sccm-recon6
```

## Information Collected

- **General**
  - Whether the server is a **Distribution Point (DP)** and/or **Management Point (MP)**
  - The related **database servers** and whether **SMB signing** is required
  - The **current user** SID

- **If the server is a Distribution Point**
  - Related **site code**
  - Related **site server**
  - Related **Management Point (MP)**
  - Whether **PXE** is installed
  - Whether **anonymous HTTP access** is allowed