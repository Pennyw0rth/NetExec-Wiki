# Enumerate Groups

To list all domain groups via ADWS:

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --groups
```

To enumerate members of a specific group:

```bash
nxc adws 192.168.1.100 -u user -p password -d domain.local --groups "Domain Admins"
```
