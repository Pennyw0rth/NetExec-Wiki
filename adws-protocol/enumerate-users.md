# Enumerate Users

To enumerate all domain users via ADWS:

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --users
```

To enumerate only **active** users (excludes disabled accounts):

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --active-users
```
