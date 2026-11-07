---
description: An alternative to ldapsearch
---

# Query ADWS

If you need to query raw LDAP values over ADWS you can use the `--query` option with filters. This performs the same WS-Enumeration query as the built-in flags but with a custom LDAP filter and attribute list.

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --query "(sAMAccountName=Administrator)" "sAMAccountName,description"
```

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --query "(objectCategory=computer)" "sAMAccountName,operatingSystem"
```
