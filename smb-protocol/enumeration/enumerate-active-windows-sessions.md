# Enumerate active Windows sessions

When connecting to a Windows server via GUI interface (local connection or RDP) a windows session will be created. These session can be listed using the following option

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --qwinsta
```

Note that if a session if found, an attacker will be able to:
* Impersonate the primary token for that user (if credentials are stored in memory) ;
* Run tasks on behalf of that user.

Sometimes you'll end up having to hunt for a specific user which can be done filling the username you are looking for:

```bash
nxc smb 192.168.1.0/24 -u UserNAme -p 'PASSWORDHERE' --qwinsta username
```
