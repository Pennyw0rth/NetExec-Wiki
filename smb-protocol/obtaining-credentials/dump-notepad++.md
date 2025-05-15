---
description: Dump Notepad++ unsaved documents
---

# 🆕 Dump Notepad++

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Finding credentials in text files never happens, right? Right??

Well, even typing in sensible content into unsaved notepad++ documents can be dangerous, as they still leave traces on the system. This module dumps currently unsaved notepad++ documents:

```bash
nxc smb <ip> -u username -p password -M notepad++
```

![Dumping unsaved notepad++ documents](https://github.com/user-attachments/assets/462b4dc3-1d7e-4fca-9292-04e4e4c39156)
