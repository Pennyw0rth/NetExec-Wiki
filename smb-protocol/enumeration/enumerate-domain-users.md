# Enumerate Domain Users

Enumerate domain users on the remote target

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --users
```

Export domain users on the remote target

```bash
nxc smb <ip> -u UserNAme -p 'PASSWORDHERE' --users-export output.txt
```
