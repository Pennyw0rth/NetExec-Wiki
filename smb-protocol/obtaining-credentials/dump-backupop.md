# 🆕 Dump with BackupOperator Priv

{% hint style="success" %}
You don't need to local admin privilege on the remote target if you are in SeBackupPrivilege
{% endhint %}

If the controlled user has the SeBackupPrivilege, it can dump SAM, SYSTEM, SECURITY and therefore the NTDS.dit on the target system. No admin privs needed!

```bash
nxc smb <ip> -u username -p password -M backup_operator
```

![image](https://github.com/user-attachments/assets/88d5aa2d-4369-4dac-815f-1dbe80b12ad6)
