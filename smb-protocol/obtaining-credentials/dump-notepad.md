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

<figure><img src="../../.gitbook/assets/image (22).png" alt=""><figcaption><p>Extract credentials from (unsaved) notepad files</p></figcaption></figure>
