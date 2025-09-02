# 🆕 Enumerate Primary Site Server and Distribution Point via recon6

This module extracts information from **Primary Site Servers** and **Distribution Points** of an SCCM infrastructure via the registry hive **HKLM\SOFTWARE\Microsoft\SMS**. This method is known as RECON 6.

```bash
nxc smb ip_pss -u username -p password -M sccm-recon6
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