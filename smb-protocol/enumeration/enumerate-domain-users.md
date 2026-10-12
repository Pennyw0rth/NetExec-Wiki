# Enumerate Domain Users

Enumerate domain users on the remote target

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --users
```

Export domain users on the remote target

```bash
nxc smb <ip> -u UserNAme -p 'PASSWORDHERE' --users --export output.txt
```

> `--users-export` still works the same way but is deprecated in favor of `--users --export`.

Enumerate just the **active** (non-disabled) domain users

```bash
nxc smb <ip> -u UserNAme -p 'PASSWORDHERE' --active-users
```

Export just the active users to a file

```bash
nxc smb <ip> -u UserNAme -p 'PASSWORDHERE' --active-users --export output.txt
```
