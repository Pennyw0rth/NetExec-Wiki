---
description: Dump Notepad++ unsaved documents
---

# 🆕 Dump Notepad++

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Finding credentials in text files never happens, right? Right??

Well, even typing in sensible content into unsaved notepad++ documents can be dangerous, as they still leave traces on the system.

```bash
nxc smb <ip> -u username -p password -M notepad++
```

Made by [@Dfte](https://x.com/Defte_)
