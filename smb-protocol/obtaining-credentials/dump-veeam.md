---
description: Dump passwords used by Veeam for backup jobs
---

# Dump Veeam

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Veeam stores credentials for server and client used for backup jobs in a SQL database. In most configurations this SQL database is on the same system as the veeam server. If this is not the case the module might not work. Please open an issue on github if the module finds a veeam installation, but can't successfully extract credentials.

```bash
nxc smb 192.168.56.22 -u eddard.stark -p FightP3aceAndHonor! -M veeam
```

