# Dump SAM

### Dump SAM hashes using methods from secretsdump.py

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```bash
nxc smb 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --sam
```

### Dump SAM including password history
```bash
nxc smb 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --sam --history
```

If this command fail you can also try the old method (similar to secretdump)

```bash
nxc smb 192.168.1.0/24 -u UserName -p 'PASSWORDHERE' --sam secdump
```
