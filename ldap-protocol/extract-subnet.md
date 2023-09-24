---
description: Extract subnet over an active directory environment
---

# Extract subnet

```
$ poetry run NetExec ldap <ip> -u <user> -p <pass> -M get-network
$ poetry run NetExec ldap <ip> -u <user> -p <pass> -M get-network -o ONLY_HOSTS=true
$ poetry run NetExec ldap <ip> -u <user> -p <pass> -M get-network -o ALL=true
```
