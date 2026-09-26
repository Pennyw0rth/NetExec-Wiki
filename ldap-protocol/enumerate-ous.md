# Enumerate Organizational Units

Enumerate all OUs in the Domain:

```bash
nxc ldap <ip> -u <username> -p <password> --ous
```

To enumerate all members in specific OU via LDAP:

```bash
nxc ldap <ip> -u <username> -p <password> --ous "Domain Controllers"
```
