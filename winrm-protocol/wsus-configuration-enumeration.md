# WSUS Configuration Enumeration

This module (`wsus_enum`) enumerates a host's **Windows Update configuration** to determine whether it is configured to use a **WSUS server** and whether that configuration is vulnerable to **WSUS spoofing**.

`wsus_enum` collects the relevant Windows Update settings (**registry values**) and evaluates whether the machine is enforcing a WSUS server. The module reports the configured `WUServer / WUStatusServer` values as well as flags such as `UseWUServer`, `NoAutoUpdate` and `AUOptions`.

```bash
nxc winrm <ip> -u user -p pass -M wsus_enum
```

If WinRM is not available, you can run the module over SMB (**requires administrative privileges**):

```bash
nxc smb <ip> -u user -p pass -M wsus_enum
```
