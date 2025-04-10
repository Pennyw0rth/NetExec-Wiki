# Enumerate Domain Groups

Enumerate all groups in the Domain:

```bash
nxc ldap <ip> -u <username> -p <password> --groups
```

To enumerate all members in specific group via LDAP:

```bash
nxc ldap <ip> -u <username> -p <password> --groups "Domain Admins"
```
