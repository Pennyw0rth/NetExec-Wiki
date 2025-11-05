# Enumerate Users

Enumerate valid Active Directory usernames **without credentials** using Kerberos `AS-REQ` requests (no pre-authentication).

This method is stealthier than LDAP/SMB enumeration and does not increment `badPwdCount`.

```bash
nxc kerberos <DC_IP> -d <DOMAIN> -u <userlist.txt> [--threads <N>]
```

To export all users to a file:
```bash
nxc kerberos <DC_IP> -d <DOMAIN> -u <userlist.txt> [--threads <N>] --users-export output.txt
```

