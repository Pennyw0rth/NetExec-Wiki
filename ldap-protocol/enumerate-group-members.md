# Enumerate Domain Groups

Enumerate all groups in the Domain:

```
nxc ldap <ip> -u <username> -p <password> --groups
```

To enumerate all members in specific group via LDAP:

```
nxc ldap <ip> -u <username> -p <password> --groups "Domain Admins"
```
