# Enumerate Users by Bruteforcing RID

Enumerate users by bruteforcing the RID on the remote target

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --rid-brute
```

Export the bruteforced usernames to a file (machine accounts are excluded)

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --rid-brute --export output.txt
```

An explicit max RID can be given to extend the range searched:

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --rid-brute 10000 --export output.txt
```
