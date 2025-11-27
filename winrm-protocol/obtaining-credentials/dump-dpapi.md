---
description: Dump DPAPI credentials using NetExec
---

# 🆕 Dump DPAPI

You can dump Credential Manager secrets for the connecting user with the following option: `--dpapi`.
Admin rights not needed.

```bash
nxc winrm <ip> -u user -p password --dpapi
```
### Example

The Puppy machine on HackTheBox is a good example of this technique

{% embed url="https://www.hackthebox.com/machines/puppy" %}
